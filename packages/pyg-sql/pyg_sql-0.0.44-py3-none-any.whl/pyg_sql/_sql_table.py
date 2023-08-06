import sqlalchemy as sa
from sqlalchemy_utils.functions import create_database
from pyg_base import cache, cfg_read, as_list, dictable, lower, loop, replace, Dict, is_dict, is_dictable, is_strs, is_str, is_int, is_date, dt2str, ulist, try_back, unique, is_primitive
from pyg_encoders import as_reader, as_writer, dumps, loads, encode
from sqlalchemy import Table, Column, Integer, String, MetaData, Identity, Float, DATE, DATETIME, TIME, select, func, not_, desc, asc
from sqlalchemy.orm import Session
from sqlalchemy.engine.base import Engine
from sqlalchemy.types import NUMERIC, FLOAT, INT
import datetime
from copy import copy
from pyg_base import logger, is_regex
from functools import partial
import pandas as pd


_id = '_id'
_doc = 'doc'
_root = 'root'
_deleted = 'deleted'
_archived = 'archived_'
_pd_is_old = pd.__version__.startswith('0')

_types = {str: String, 'str' : String, 
          int : Integer, 'int' : Integer,
          float: Float, 
          'dec' : sa.DECIMAL(0), 'dec1' : sa.DECIMAL(1), 'dec2' : sa.DECIMAL(2), 'dec3' : sa.DECIMAL(3), 'dec4' : sa.DECIMAL(4), 'dec5' : sa.DECIMAL(5), 
          datetime.date: DATE, 'date' : DATE,
          datetime.datetime : DATETIME, 'datetime' : DATETIME,
          datetime.time: TIME, 'time' : TIME,
          bin : sa.VARBINARY}

_orders = {1 : asc, True: asc, 'asc': asc, asc : asc, -1: desc, False: desc, 'desc': desc, desc: desc}

def _data_and_columns(executed):
    columns = list(executed.keys())
    data = list(executed)
    return data, columns

def valid_session(session):
    """
    TO DO: How do we check if db connection expired??

    Parameters
    ----------
    session : db session
        sql database session

    Returns
    -------
    bool
        is the session still valid?

    """
    return session is not None

def _relabel(res, selection, strict = True):
    """
    selection defines the CASE we want the columns to be in
    We convert either columns or dicts into the case from 

    Parameters
    ----------
    res : pd.DataFrame/dict
        original value
    selection : str/list of str
        columnes/keys in the case we want them
    strict : bool, optional
        if False, will replace opportunistically. If True, needs all res & selection to match. The default is True.

    Returns
    -------
    pd.DataFrame/dict
        same object with case matching
        
    Example
    -------
    >>> res = dict(a = 1, b = 2, c = 3)
    >>> selection = ['A', 'B']
    >>> assert _relabel(res, selection) == res                  ## no replacement, strict
    >>> assert _relabel(res, selection, strict = False) == dict(A = 1, B = 2, c = 3) ## replaceme what is possible
    >>> assert _relabel(res, ['A', 'B', 'C']) == dict(A = 1, B = 2, C = 3)
    >>> assert _relabel(res, ['A', 'B', 'C'], True) == dict(A = 1, B = 2, C = 3)

    """
    if not is_strs(selection):
        return res
    lower_selection = lower(as_list(selection))
    if isinstance(res, pd.DataFrame):
        columns = list(res.columns)
        if columns == selection:
            return res
        if lower(list(res.columns)) == lower_selection:
            res.columns = selection
        elif not strict:
            lower2selection = dict(zip(lower_selection, selection))
            res.columns = [lower2selection.get(col.lower(),col) for col in res.columns]    
        return res
    elif isinstance(res, dict):
        if strict and sorted(lower(list(res.keys()))) == sorted(lower_selection):
            columns = res.keys()
            if sorted(columns) == sorted(selection): ## nothing to do
                return res
            lower2selection = dict(zip(lower_selection, selection))
            return type(res)({lower2selection[key.lower()] : value for key, value in res.items()})
        elif not strict:
            lower2selection = dict(zip(lower_selection, selection))
            return type(res)({lower2selection.get(key.lower(), key): value for key, value in res.items()})
        else:
            return res            
    else:
        return res       

def _get_columns(table):
    """
    returns a dict from lower-case columns to actual columns
    works with tables, join objects or sql_cursors
    """
    if isinstance(table, sql_cursor):
        table = table._table
    cols = table.columns
    res = {}
    for col in cols:
        name = col.name.lower()
        res[name] = res.get(name, []) + [col]
    return res


def _pw_filter(col, v):
    if is_regex(v):
        p = v.pattern
        if not p.startswith('%'):
            p = '%' + p
        if not p.endswith('%'):
            p = p + '%'
        return col.like(p)
    elif is_str(v) and v.startswith('%') and v.endswith('%'):
        return col.like(v)
    elif isinstance(v, list):
        return sa.or_(*[_pw_filter(col, i) for i in v])
    else:
        return col == v

@loop(list)
def _like_within_doc(v, k):
    return '%' + dumps(encode({k : v}))[1:-1] + '%'


class sql_df():
    """
    a helper class designd to allow access of DataFrames this way:

    >>> sql_table(...).df()
    >>> sql_table(...).df[::]
    >>> sql_table(...).df[0] ## a pd.Series of the 1st column
    >>> sql_table(...).df[:20] ## a pd.DataFrame of the top 20 rows

    """
    def __init__(self, cursor):
        self.cursor = cursor

    def __call__(self, decimal2float = True, start = None, stop = None, step = None):
        """
        This is a more optimized, faster version for reading the table. 
        It retuns the data as a pd.DataFrame,
        In addition, it converts NUMERIC type (which is cast to decimal.Decimal) into a float

        
        Parameters
        ----------
        decimal2float: bool
            converts sql.types.NUMERIC columns into float

        Returns
        -------
        pd.DataFrame
            The data, optimized as a dataframe.

        
        Example: speed comparison
        --------

        >>> from pyg import * 
        >>> t = sql_table(db = 'db', table = 'tbl', nullable = dict(a = int, b = float, c = str))
        >>> rs =dictable(a = range(100)) * dict(b = list(np.arange(0,100,1.0))) * dict(c = list('abcdefghij'))
        >>> t = t.insert_many(rs)      
        
        ## reading the data as t[::] is slow...
        >>> x = timer(lambda : t[::])()
        2022-08-21 18:03:52,594 - pyg - INFO - TIMER: took 0:00:13.139333 sec
 
        ## reading the data as t.df() is much faster...
        >>> y = timer(lambda : t.df())()
        2022-08-21 18:04:24,809 - pyg - INFO - TIMER: took 0:00:00.456988 sec


        """
        cursor = self.cursor
        statement = cursor.statement()
        if (is_int(start) and start < 0) or (is_int(stop) and stop < 0):
            n = len(cursor)
            start = n + start if is_int(start) and start < 0 else start                            
            stop = n + stop if is_int(stop) and stop < 0 else stop
        if start and cursor.order is not None:
            statement = statement.offset(start)
            stop = stop if stop is None else stop - start
        if stop is not None:
            statement = statement.limit(1+stop)
        if _pd_is_old:
            data, columns = cursor.execute(statement, transform = _data_and_columns)
            res = pd.DataFrame(data, columns = columns)
        else:
            res = cursor.execute(statement, transform = pd.DataFrame)
        if start is not None or stop is not None or step is not None:
            res = res.iloc[slice(start, stop, step)]
        if decimal2float:
            for col in res.columns:
                t = cursor.table.columns[col].type
                if isinstance(t, NUMERIC) and not isinstance(t, (FLOAT, INT)):
                    res[col] = res[col].astype(float)
        return _relabel(res, cursor.selection)
    
    def __getitem__(self, value):
        if isinstance(value, slice):
            start, stop, step = value.start, value.stop, value.step
            return self(start = start, stop = stop, step = step)
        elif isinstance(value, int):
            return pd.Series(self.cursor[value])
        

# def pickle_loads(value):
#     if isinstance(value, dict):
#         return type(value)({k: pickle_loads(v) for k, v in value.items()})
#     elif isinstance(value, (list, tuple)):
#         return type(value)([pickle_loads(v) for v in value])        
#     elif isinstance(value, bytes):
#         return pickle.loads(value)
#     else:
#         return value


@cache
def _servers():
    res = cfg_read().get('sql_server', {})
    if isinstance(res, dict):
        res[None] = res.get('null')
        res[True] = res.get('true')
        res[False] = res.get('false')
        res['None'] = res.get('None', res[None])
    return res

@cache
def _schema(schema = None):
    return schema or cfg_read().get('sql_schema', 'dbo')


@cache
def _databases():
    """
    configures the sql_databases
    from pyg import * 
    
    cfg = cfg_read()
    cfg['sql_database'] = {None : 'db', 'res' : 'res'}
    cfg_write(cfg)

    """
    dbs = cfg_read().get('sql_database', {None: 'master'})
    if isinstance(dbs, str):
        dbs = {dbs : dbs}
    if None not in dbs:
        dbs[None] = dbs.get('null')
    dbs[True] = dbs.get('true')
    dbs[False] = dbs.get('false')
    return dbs

@cache
def _database(db = None):
    dbs = _databases()
    db = dbs.get(db, db)
    db = dbs.get(db, db)
    return db
    
def get_server(server = None):
    """
    Determines the sql server string
    We support a server config which looks like:
        config['sql_server'] = dict(dev = 'server.test', prod = 'prod.server')
    """
    servers = _servers()
    server = server or None
    if isinstance(servers, str):
        if server is None or server is True:
            server = servers
    else:
        server = servers.get(server, server)
        server = servers.get(server, server) #double redirection supported
    if server is None:
        raise ValueError('please provide server or set a "sql_server" in cfg file: from pyg_base import *; cfg = cfg_read(); cfg["sql_server"] = "server"; cfg_write(cfg)')
    return server


def get_driver(driver = None):
    """
    determines the sql server driver
    """
    if driver is None or driver is True:
        driver = cfg_read().get('sql_driver')
    if driver is None:
        import pyodbc
        odbc_drivers = [d for d in pyodbc.drivers() if d.startswith('ODBC')]
        if len(odbc_drivers):
            driver = sorted(odbc_drivers)[-1]
        if driver is None:
            raise ValueError('No ODBC drivers found for SQL Server, please save one: cfg = cfg_read(); cfg["sql_driver"] = "ODBC+Driver+17+for+SQL+Server"; cfg_write(cfg)')    
        else:
            driver = driver.replace(' ', '+')
            return driver
    elif is_int(driver):
        return 'ODBC+Driver+%i+for+SQL+Server'%driver
    else:
        return driver


def _pairs2connection(*pairs, **connection):
    connection = connection.copy()
    for pair in pairs:
        ps = pair.split(';')
        for p in ps:
            if p:
                k, v = p.split('=')
                k = k.strip()
                v = v.strip().replace("'","")
                connection[k] = v
    connection = {k.lower() : replace(replace(v, ' ','+'),['{','}'],'') for k, v in connection.items() if v is not None}
    return connection


def _db(connection):
    db = connection.pop('db', None)
    if db is None:
        db = connection.pop('database', None)
    db = _database(db)
    return db
    

def get_cstr(*pairs, **connection):
    """
    determines the connection string
    """
    connection = _pairs2connection(*pairs, **connection)
    server = get_server(connection.pop('server', None))
    connection['driver'] = get_driver(connection.pop('driver', None))
    db = _db(connection)
    if '//' in server:
        return server
    else:
        params = '&'.join('%s=%s'%(k,v) for k,v in connection.items())
        return 'mssql+pyodbc://%(server)s/%(db)s%(params)s'%dict(server=server, db = db, params = '?' +params if params else '')


def create_schema(engine, schema, create = True):
    if schema is None:
        return
    try:
        if schema not in engine.dialect.get_schema_names(engine):
            if create is True or (is_str(create) and ('s' in create.lower() or 'd' in create.lower())):
                engine.execute(sa.schema.CreateSchema(schema))
            else:
                raise ValueError(f'Schema {schema} does not exist. You have to explicitly mandata the creation of a schema by setting create=True or create="d" or create="s"')
            logger.info('creating schema: %s'%schema)
    except AttributeError: #MS SQL vs POSTGRES
        if not engine.dialect.has_schema(engine, schema):
            engine.execute(sa.schema.CreateSchema(schema))
            logger.info('creating schema: %s'%schema)
    return schema
    
@cache
def _create_engine(cstr):
    return sa.create_engine(cstr)
    

def _get_engine(*pairs, **connection):  
    connection = _pairs2connection(*pairs, **connection)
    server = get_server(connection.pop('server', None))
    if isinstance(server, Engine):
        return server
    connection['driver'] = get_driver(connection.pop('driver', None))
    engine = connection.pop('engine', None)
    create = connection.pop('create', False)
    db = _db(connection)    
    if isinstance(engine, Engine):
        return engine
    cstr = get_cstr(server=server, db = db, **connection)    
    if callable(engine): # delegates connection to another function
        e = Dict(server = server, db = db, environment = server, connection = cstr).apply(engine)
    else:
        e = _create_engine(cstr)
    try:
        sa.inspect(e)
    except Exception:
        if create is True or (is_str(create) and 'd' in create.lower()): ## create can be a "level" specifying if it is to be created
            create_database(cstr)
            logger.info('creating database: %s'%db)
        else:
            raise ValueError('You have to explicitly permission the creation of the database by setting create = True or create ="d"')
    return e


def get_engine(*pairs, **connection):
    """
    returns a sqlalchemy engine object
    accepts either 
    *pairs: 'driver={ODBC Driver 17 for SQL Server}' or
    **connection: keyword arguments that look like driver = 'ODBC Driver 17 for SQL Server'    
    """
    return _get_engine(*pairs, **connection)
    

@cache
def _get_table(table_name, schema, db, server, create, engine = None):
    e = _get_engine(server = server, db = db, schema = schema, create = create, engine = engine)
    meta = MetaData()
    return Table(table_name, meta, autoload_with = e, schema = schema)


def sql_table(table, db = None, non_null = None, nullable = None, _id = None, schema = None, 
              server = None, reader = None, writer = None, pk = None, doc = None, mode = None, 
              spec = None, selection = None, order = None, defaults = None, joint = None, create = None, engine = None):
    """
    Creates a sql table. Can also be used to simply read table from the db

    Parameters
    ----------
    table : str
        name of table can also be passed as 'database.table'.
    db : str, optional
        name of database. The default is None.
    non_null : str/list of strs/dict 
        dicts of non-null column names to their type, optional. The default is None.
    nullable : str/list of strs/dict , optional
        dicts of null-able column names to their type, optional. The default is None.
    _id: str/list of strs/dict , optional
        dicts of column that are auto-completed by the server and the user should not provide these.
    schema : str, optional
        like 'dbo'. The default is None.
    server : str, optional
        Name of connection string. The default is None.
    reader : Bool/string, optional
        How should data be read. The default is None.
    writer : bool/string, optional
        How to transform the data before saving it in the database. The default is None.
    pk : list, optional
        primary keys on which the table is indexed. if pk == 'KEY' then we assume 'KEY' will be uniquely valued. The default is None.
    doc : str / True, optional
        If you want the DOCUMENT (a dict of stuff) to be saved to a single column, specify.
    mode : int, optional
        NOT IMPLEMENTED CURRENTLY
    spec : sqlalchemy selection object
        can specify a filter on the resulting data, applied in a WHERE
    selection: None/str/list(str)
        can specify column selection in a SELECT statement
    order: dict/str/liststr
        can specifiy a SORT statement
    joint: a list of tuples:
        Each tuple contains the object to join the table with, as well as the other parameters used in a sql alchemy join statement 
    create: bool/str
        Creation policy. The "mongo" document store policy is to create a database on the fly.
        Here the policy is more nuanced:
        'd' or True : will create the database, the schema and the table if needed
        's'         : will create a schema & table if database exists but if database doesn't, will throw
        't'         : will create a table if db & schema exists and will throw if either db or schema are missing
        '' or False : will throw
        if create is None:
            if no nullable and no non_null and doc is False:
                create = False
            else:
                create = 's'
    engine: sqlalchemy Engine, None, or a function that returns an engine
        This allows connection management to be delegated to the user who may want to manage her own connection protocol
    defaults:
        this is default variable that is added to the document if it does not have its keys

    Returns
    -------
    res : sql_cursor
        A hybrid object we love.


    Example: simple table creation
    ---------
    >>> from pyg import * 
    >>> table = sql_table(table = 'test', nullable = dict(a = int, b = str), db = 'db')
    >>> table.insert(dict(a = 1, b = 'a'))
    >>> assert len(table) == 1
    >>> table.insert(dictable(a = [2,3], b = 'b'))
    >>> assert len(table) == 3
    >>> assert len(table.inc(table.c.a > 2)) == 1
    >>> assert table.inc(table.c.a > 2)[0] == dict(a = 3, b = 'b')
    >>> table.inc(b = 'a').delete()
    >>> assert len(table) == 2
    >>> assert table.distinct('b') == ['b']

    >>> table.drop()
    
    Example: ensure sql_table defaults for a doc store if 'doc' exists in existing table or no data columns are specified on creation
    --------
    table = sql_table(table = 'test', pk = 'key', schema ='dbo', db = 'db')
    assert table.doc == 'doc'
    table = sql_table(table = 'test', db = 'db', schema = 'dbo')
    assert tbl.doc == 'doc'
    table.drop()

    Example: simple join
        
    """
    if isinstance(table, str):
        values = table.split('.')
        if len(values) == 2:
            schema = schema or values[0]
            if schema != values[0]:
                raise ValueError('schema cannot be both %s and %s'%(values[0], db))
            table = values[1]
        elif len(values)>2:
            raise ValueError('not sure how to translate this %s into a db.table format'%table)
    elif isinstance(table, partial): # support for using the partial rather than the actual table
        db = table.keywords.get('db') if db is None else db
        schema = table.keywords.get('schema') if schema is None else schema
        server = table.keywords.get('server') if server is None else server
        pk = table.keywords.get('pk') if pk is None else pk
        writer = table.keywords.get('writer') if writer is None else writer
        doc = table.keywords.get('doc') if doc is None else doc
        table = table.keywords['table']
    
    ### we resolve some parameters
    if doc is True: #user wants a doc
        doc = _doc
    non_null = non_null or {}
    nullable = nullable or {}
    pks = pk or {}
    if isinstance(pks, list):
        pks = {k : String for k in pks}
    elif isinstance(pks, str):
        pks = {pks : String}
    if isinstance(non_null, list):
        non_null = {k : String for k in non_null}
    elif isinstance(non_null, str):
        non_null = {non_null : String}
    pks.update(non_null)
    if isinstance(nullable, list):
        nullable = {k : String for k in nullable}
    elif isinstance(nullable, str):
        nullable = {nullable: String}
    if isinstance(table, str):
        table_name = table 
    else:
        table_name = table.name
        if schema is None:
            schema = table.schema

    ## do we have any columns in table?
    cols = []
    if isinstance(table, sa.sql.schema.Table):
        for col in table.columns:
            col = copy(col)
            del col.table
            cols.append(col)
    if _id is not None:
        if isinstance(_id, str):
            _id = {_id : int}
        if isinstance(_id, list):
            _id = {i : int for i in _id}
        for i, t in _id.items():
            if i not in [col.name for col in cols]:
                if t == int:                    
                    cols.append(Column(i, Integer, Identity(always = True)))
                elif t == datetime.datetime:
                    cols.append(Column(i, DATETIME(timezone=True), nullable = False, server_default=func.now()))
                else:
                    raise ValueError('not sure how to create an automatic item with column %s'%t)

    col_names = [col.name for col in cols]
    non_nulls = [Column(k, _types.get(t, t), nullable = False) for k, t in pks.items() if k not in col_names]
    nullables = [Column(k.lower(), _types.get(t, t)) for k, t in nullable.items() if k not in col_names] 
    docs = [Column(doc, String, nullable = True)] if doc else []
    cols = cols + non_nulls + nullables + docs

    ## creation logic:
    if create is None:
        create = 's' if len(cols) else False

    ## time to access/create tables        
    e = _get_engine(server = server, db = db, schema = schema, create = create, engine = engine)
    schema = create_schema(e, _schema(schema), create = create)
    try:
        tbl = _get_table(table_name = table_name, schema = schema, db = db, server = server, create = create, engine = e) ## by default we grab the existing table
        if doc is None and _doc in [col.name for col in tbl.columns]:
            doc = _doc
    except sa.exc.NoSuchTableError:        
        if doc is None and len(non_null) == 0 and len(nullable) == 0: #user specified nothing but pk so assume table should contain SOMETHING :-)
            doc = _doc
        meta = MetaData()
        if len(cols) == 0:
            raise ValueError('You seem to be trying to create a table with no columns? Perhaps you are trying to point to an existing table and getting its name wrong?')
        if create is True or (is_str(create) and ('t' in create.lower() or 's' in create.lower() or 'd' in create.lower())):
            logger.info('creating table: %s.%s.%s%s'%(db, schema, table_name, [col.name for col in cols]))
            tbl = Table(table_name, meta, *cols, schema = schema)            
            meta.create_all(e)
        else:
            raise ValueError(f'table {table_name} does not exist. You need to explicitly set create=True or create="t/s/d" to mandate table creation')
    res = sql_cursor(table = tbl, schema = schema, db = db, server = server, engine = e, 
                     reader = reader, writer = writer, defaults = defaults,
                     pk = list(pk) if isinstance(pk, dict) else pk, doc = doc,
                     spec = spec, selection = selection, order = order, joint = joint)
    return res

class sql_cursor(object):
    """
    # pyg-sql
    
    pyg-sql creates sql_cursor, a thin wrapper on sql-alchemy (sa.Table), providing three different functionailities:

    - simplified create/filter/sort/access of a sql table
    - maintainance of a table where records are unique per specified primary keys while we auto-archive old data
    - creation of a full no-sql like document-store

    pyg-sql supports simple joins but not much more than that.
    
    ## access simplification
    
    sqlalchemy use-pattern make Table create the "statement" and then let the engine session/connection to execute. sql_cursor keeps tabs internally of:

    - the table
    - the engine
    - the "select", the "order by" and the "where" statements

    This allows us to

    - "query and execute" in one go
    - build statements interactively, each time adding to previous "where" or "select"
    

    :Example: table creation
    ------------------------
    >>> from pyg_base import * 
    >>> from pyg_sql import * 
    >>> import datetime
    
    >>> t = sql_table(db = 'test', table = 'students', non_null = ['name', 'surname'], 
                          _id = dict(_id = int, created = datetime.datetime), 
                          nullable =  dict(doc = str, details = str, dob = datetime.date, age = int, grade = float))
    >>> t = t.delete()


    :Example: table insertion
    -------------------------
    >>> t = t.insert(name = 'yoav', surname = 'git', age = 48)
    >>> t = t.insert(name = 'anna', surname = 'git', age = 37)
    >>> assert len(t) == 2
    >>> t = t.insert(name = ['ayala', 'itamar', 'opher'], surname = 'gate', age = [17, 11, 16])
    >>> assert len(t) == 5

    :Example: simple access
    -----------------------
    >>> assert t.sort('age')[0].name == 'itamar'                                                     # youngest
    >>> assert t.sort('age')[-1].name == 'yoav'                                                      # access of last record
    >>> assert t.sort(dict(age=-1))[0].name == 'yoav'                                                # sort in descending order
    >>> assert t.sort('name')[::].name == ['anna', 'ayala', 'itamar', 'opher', 'yoav']
    >>> assert t.sort('name')[['name', 'surname']][::].shape == (5, 2)                              ## access of specific column(s)
    >>> assert t.distinct('surname') == ['gate', 'git']
    >>> assert t['surname'] == ['gate', 'git']
    >>> assert t[dict(name = 'yoav')] == t.inc(name = 'yoav')[0]
    
    
    :Example: access is case-insensitive
    ------------------------------------
    >>> from pyg_sql import *
    >>> t = sql_table(db = 'test', table = 'case_insensitive', nullable = dict(number = int, text = str))
    >>> self = t.delete()

    When we insert, we convert the case to the database columns convention:
        
    >>> assert t.insert_one(doc = dict(NUMBER = 1, TEXT = 'world')) == {'number': 1, 'text': 'world'}
    >>> assert t.insert_one(dict(Number = 2, Text = 'hello')) == {'number': 2, 'text': 'hello'}

    When we access the columns without specification, we get the database column names
    
    >>> assert t[0] == {'number': 1, 'text': 'world'}

    When we filter or sort, we can filter using any case for column names
    
    >>> assert len(t.inc(NUMBER = 2)) == 1

    assert t.sort('TEXT')[0] == {'number': 2, 'text': 'hello'}

    When we SELECT, we can use any case, and key-case will follow your cursor.selection case:
        
    >>> assert t[['NUMBER','TexT']][0] == {'NUMBER': 1, 'TexT': 'world'}
    >>> assert list(t[['Number','Text']].df().columns) == ['Number', 'Text']
    >>> assert sorted(t[['Number','Text']][::].columns) == ['Number', 'Text']

    :Example: simple filtering
    --------------------------
    >>> assert len(t.inc(surname = 'gate')) == 3
    >>> assert len(t.inc(surname = 'gate').inc(name = 'ayala')) == 1    # you can build filter in stages
    >>> assert len(t.inc(surname = 'gate', name = 'ayala')) == 1        # or build in one step
    >>> assert len(t.inc(surname = 'gate').exc(name = 'ayala')) == 2

    >>> assert len(t > dict(age = 30)) == 2
    >>> assert len(t <= dict(age = 37)) == 4
    >>> assert len(t.inc(t.c.age > 30)) == 2  # can filter using the standard sql-alchemy .c.column objects
    >>> assert len(t.where(t.c.age > 30)) == 2  # can filter using the standard sql-alchemy "where" statement 


    Example: simple joining
    -----------------------
    >>> from pyg import * 
    >>> students = sql_table(table = 'students', pk = ['id'], non_null = ['name', 'surname'], db = 'db')
    >>> students.insert([dict(name = 'ann', surname = 'andrews', id = 'a'),
                         dict(name = 'ben', surname = 'baxter', id = 'b'),
                         dict(name = 'charles', surname = 'cohen', id = 'c')])

    >>> subjects = sql_table(table = 'subjects', pk = ['id'], non_null = ['subject', 'teacher'], db = 'db')
    >>> subjects.insert([dict(subject = 'maths', teacher = 'mandy miles', id = 'm'),
                         dict(subject = 'geography', teacher = 'george graham', id = 'g'),
                         dict(subject = 'zoology', teacher = 'zoe zhenya', id = 'z')])

    >>> student_subject = sql_table(table = 'student_subject', non_null = {'student_id':str, 'subject_id':str, 'score': int})
    >>> student_subject.insert([dict(student_id = 'a', subject_id = 'm', score = 90),
                                dict(student_id = 'a', subject_id = 'z', score = 85),
                                dict(student_id = 'b', subject_id = 'm', score = 70),
                                dict(student_id = 'b', subject_id = 'g', score = 60),
                                dict(student_id = 'c', subject_id = 'g', score = 50),
                                dict(student_id = 'c', subject_id = 'z', score = 45),
                                ])
    

    >>> self = student_subject.join(students, dict(student_id = 'id'))

    self[::]
    id|name   |score|student_id|subject_id|surname
    a |ann    |90   |a         |m         |andrews
    a |ann    |85   |a         |z         |andrews
    b |ben    |70   |b         |m         |baxter 
    b |ben    |60   |b         |g         |baxter 
    c |charles|50   |c         |g         |cohen  
    c |charles|45   |c         |z         |cohen  

    self.inc(surname = '%co%')[::]
    dictable[2 x 6]
    id|name   |score|student_id|subject_id|surname
    c |charles|50   |c         |g         |cohen  
    c |charles|45   |c         |z         |cohen  

    >>> self.inc(score = [90,50])[::]
    dictable[2 x 6]
    id|name   |score|student_id|subject_id|surname
    a |ann    |90   |a         |m         |andrews
    c |charles|50   |c         |g         |cohen  

    ## double join
    >>> student_subject.join(students, dict(student_id = 'id')).join(subjects, dict(subject_id = 'id'))[::]
    id|id_1|name   |score|student_id|subject  |subject_id|surname|teacher      
    a |m   |ann    |90   |a         |maths    |m         |andrews|mandy miles  
    a |z   |ann    |85   |a         |zoology  |z         |andrews|zoe zhenya   
    b |m   |ben    |70   |b         |maths    |m         |baxter |mandy miles  
    b |g   |ben    |60   |b         |geography|g         |baxter |pportgeorge graham
    c |g   |charles|50   |c         |geography|g         |cohen  |george graham
    c |z   |charles|45   |c         |zoology  |z         |cohen  |zoe zhenya       

    >>> full_join = student_subject.join(students, dict(student_id = 'id')).join(subjects, dict(subject_id = 'id'))
    >>> full_join.inc(TEACHER = '%mandy%', SCORE = 90)
    sql_cursor: db.dbo.student_subject  
    SELECT student_id, subject_id, score, dbo.students.id, dbo.students.name, dbo.students.surname, dbo.subjects.id AS id_1, dbo.subjects.subject, dbo.subjects.teacher 
    FROM dbo.student_subject JOIN dbo.students ON student_id = dbo.students.id JOIN dbo.subjects ON subject_id = dbo.subjects.id 
    WHERE dbo.subjects.teacher LIKE "%mandy%" AND score = 90
    1 records

    :Example: insertion of "documents" into string columns...    
    ----------------------------------------------------------
    It is important to realise that we already have much flexibility behind the scene in using "documents" inside string columns:

    >>> t = t.delete()
    >>> assert len(t) == 0; assert t.count() == 0
    >>> import numpy as np
    >>> t.insert(name = 'yoav', surname = 'git', details = dict(kids = {'ayala' : dict(age = 17, gender = 'f'), 'opher' : dict(age = 16, gender = 'f'), 'itamar': dict(age = 11, gender = 'm')}, salary = np.array([100,200,300]), ))

    >>> t[0] # we can grab the full data back!

    {'_id': 81,
     'created': datetime.datetime(2022, 6, 30, 0, 10, 33, 900000),
     'name': 'yoav',
     'surname': 'git',
     'doc': None,
     'details': {'kids': {'ayala':  {'age': 17, 'gender': 'f'},
                          'opher':  {'age': 16, 'gender': 'f'},
                          'itamar': {'age': 11, 'gender': 'm'}},
                 'salary': array([100, 200, 300])},
     'dob': None,
     'age': None,
     'grade': None}

    >>> class Temp():
            pass
            
    >>> t.insert(name = 'anna', surname = 'git', details = dict(temp = Temp())) ## yep, we can store actual objects...
    >>> t[1]  # and get them back as proper objects on loading

    {'_id': 83,
     'created': datetime.datetime(2022, 6, 30, 0, 16, 10, 340000),
     'name': 'anna',
     'surname': 'git',
     'doc': None,
     'details': {'temp': <__main__.Temp at 0x1a91d9fd3a0>},
     'dob': None,
     'age': None,
     'grade': None}

    ## primary keys and auto-archive
    
    Primary Keys are applied if the primary keys (pk) are specified. 
    Now, when we insert into a table, if another record with same pk exists, the record will be replaced.
    Rather than simply delete old records, we create automatically a parallel deleted_database.table to auto-archive these replaced records.
    This ensure a full audit and roll-back of records is possible.

    :Example: primary keys and deleted records
    ------------------------------------------
    The table as set up can have multiple items so:
    
    >>> t = t.delete()
    >>> t = t.insert(name = 'yoav', surname = 'git', age = 46)
    >>> t = t.insert(name = 'yoav', surname = 'git', age = 47)
    >>> t = t.insert(name = 'yoav', surname = 'git', age = 48)
    >>> assert len(t) == 3
    
    >>> t = t.delete() 
    >>> t = sql_table(db = 'test', table = 'students', non_null = ['name', 'surname'], 
                          _id = dict(_id = int, created = datetime.datetime), 
                          nullable =  dict(doc = str, details = str, dob = datetime.date, age = int, grade = float), 
                          pk = ['name', 'surname'])         ## <<<------- We set primary keys

    >>> t = t.delete()
    >>> t = t.insert(name = 'yoav', surname = 'git', age = 46)
    >>> t = t.insert(name = 'yoav', surname = 'git', age = 47)
    >>> t = t.insert(name = 'yoav', surname = 'git', age = 48)
    >>> assert len(t) == 1 
    >>> assert t[0].age == 48

    Where did the data go to? We automatically archive the deleted old records for dict(name = 'yoav', surname = 'git') here:

    >>> t.deleted 
    
    t.deleted is a table by same name,
    
    - exists on deleted_test database, 
    - same table structure with added 'deleted' column
    
    >>> assert len(t.deleted.inc(name = 'yoav', age = 46)) > 0
    >>> t.deleted.delete() 

    ## sql_cursor as a document store

    If we set doc = True, the table will be viewed internally as a no-sql-like document store. 

    - the nullable columns supplied are the columns on which querying will be possible
    - the primary keys are still used to ensure we have one document per unique pk
    - the document is jsonified (handling non-json stuff like dates, np.array and pd.DataFrames) and put into the 'doc' column in the table, but this is invisible to the user.

    :Example: doc management
    ------------------------
    
    We now suppose that we are not sure what records we want to keep for each student

    >>> from pyg import *
    >>> import datetime
    >>> t = sql_table(db = 'test', table = 'unstructured_students', non_null = ['name', 'surname'], 
                          _id = dict(_id = int, created = datetime.datetime), 
                          nullable =  dict(doc = str, details = str, dob = datetime.date, age = int, grade = float), 
                          pk = ['name', 'surname'],
                          doc = True)   ##<---- The table will actually be a document store

    We are now able to keep varied structure per each record. We are only able to filter against the columns specified above

    >>> t = t.delete()
    
    >>> doc = dict(name = 'yoav', surname = 'git', age = 30, profession = 'coder', children = ['ayala', 'opher', 'itamar'])
    >>> inserted_doc = t.insert_one(doc)
    >>> assert t.inc(name = 'yoav', surname = 'git')[0].children == ['ayala', 'opher', 'itamar']

    >>> doc2 = dict(name = 'anna', surname = 'git', age = 28, employer = 'Cambridge University', hobbies = ['chess', 'music', 'swimming'])
    >>> _ = t.insert_one(doc2)
    >>> assert t[dict(age = 28)].hobbies == ['chess', 'music', 'swimming']  # Note that we can filter or search easily using the column 'age' that was specified in table. We cannot do this on 'employer'
    
    :Example: document store containing pd.DataFrames.
    ----------
    
    >>> from pyg import *
    >>> doc = dict(name = 'yoav', surname = 'git', age = 35, 
                   salary = pd.Series([100,200,300], drange(2)),
                   costs = pd.DataFrame(dict(transport = [0,1,2], food = [4,5,6], education = [10,20,30]), drange(2)))
    
    >>> t = sql_table(db = 'test', table = 'unstructured_students', non_null = ['name', 'surname'], 
                          _id = dict(_id = int, created = datetime.datetime), 
                          nullable =  dict(doc = str, details = str, dob = datetime.date, age = int, grade = float), 
                          pk = ['name', 'surname'],
                          writer = 'c:/temp/%name/%surname.parquet', ##<---- The location where pd.DataFrame/Series are to be stored
                          doc = True)   

    >>> inserted = t.insert_one(doc)
    >>> import os
    >>> assert 'costs.parquet' in os.listdir('c:/temp/yoav/git') and ('salary.parquet' in os.listdir('c:/temp/yoav/git'))
    
    We can now access the data seemlessly:

    >>> read_from_db = t.inc(name = 'yoav')[0]     
    >>> read_from_file = pd_read_parquet('c:/temp/yoav/git/salary.parquet')
    >>> assert list(read_from_db.salary.values) == [100, 200, 300]
    >>> assert list(read_from_file.values) == [100, 200, 300]
    """
    def __init__(self, table, schema = None, db = None, engine = None, server = None, session = None,
                 spec = None, selection = None, order = None, joint = None, reader = None, writer = None, 
                 pk = None, defaults = None, doc = None, **_):
        """
        Parameters
        ----------
        table : sa.Table
            Our table
        db : string, optional
            Name of the db where table is.
        schema : string, optional
            Name of the db schema for table.
        engine : sa,Engine, optional
            The sqlalchemy engine
        server : str , optional
            The server for the engine. If none, uses the default in pyg config file
        session: db session, optional
            An uncommitted session
        spec : sa.Expression, optional
            The "where" statement
        selection : str/list of str, optional
            The columns in "select"
        order : dict or list, optional
            The columns in ORDER BY. The default is None.
        reader :
            This is only relevant to document store            
        writer : callable/str/bool
            This is only relevant to document store and specifies how documents that contain complicated objects are transformed. e.g. Use writer = 'c:/%key1/%key2.parquet' to specify documents saved to parquet based on document keys        
        doc: bool
            Specifies if to create the table as a document store
            
        """
        if is_str(table):
            table = sql_table(table = table, schema = schema, db = db, server = server)
            
        if isinstance(table, sql_cursor):
            db = table.db if db is None else db
            engine = table.engine if engine is None else engine
            server = table.server if server is None else server
            session = table.session if session is None else session
            spec = table.spec if spec is None else spec
            selection = table.selection if selection is None else selection
            schema = table.schema if schema is None else schema
            order = table.order if order is None else order
            joint = table.joint if joint is None else joint
            reader = table.reader if reader is None else reader
            writer = table.writer if writer is None else writer
            pk = table.pk if pk is None else pk
            doc = table.doc if doc is None else doc
            defaults = table.defaults if defaults is None else defaults
            table = table.table
    
        self.table = table
        self.schema = schema
        self.db = db
        self.server = server
        self.engine = engine or get_engine(db = self.db, server = self.server)
        self.session = session
        self.spec = spec
        self.selection = selection
        self.order = order
        self.joint = joint
        self.reader = reader
        self.writer = writer
        self.pk = pk
        self.defaults = defaults
        self.doc = doc
    
    def copy(self):
        return type(self)(self)

    def connect(self, dry_run = None, session_maker = None):
        """
        Creates a valid session and attach it to the cursor
        
        Parameters:
        -----------
        dry_run: bool
            if set to True, when exiting the context, will rollback rather than commit
        
        session_maker: callable
            a function that takes an engine and return a session-like object.
            This allows user to implement their own logging etc. 
            The resulting session must support 
            * commit, rollback and execute
            * context management (i.e. implement __enter__ and __exit__)            
            
        """
        if session_maker is None:
            session_maker = Session
        if not valid_session(self.session):
            self.session = session_maker(self.engine)
        self.session.dry_run = dry_run
        return self

    
    def execute(self, statement, *args, transform = None, **kwargs):
        """
        executes a statement in two modes:
            if a self.session exists, it assumes we are within a transaction and will simply execute using connection
            if self.session is None, it assumes we basically want to lock and load... will execute and commit

        Parameters
        ----------
        statement : sql statement
        
        Example: committed 
        --------            
        Example: a simple transactional logic
        --------
        with cursor:
            cursor.execute(statement) ## not committed
            cursor.execute(another_statement)

        Example: a simple transactional logic for rolling back
        --------
        with cursor.connect(True):
            cursor.execute(statement)
            cursor.execute(another_statement)
            

        """        
        if valid_session(self.session): ## we are within context
            res = self.session.execute(statement, *args, **kwargs)
            if transform:
                res = transform(res)
        else:
            with self.engine.connect() as connection:
                res = connection.execute(statement, *args, **kwargs)
                if transform:
                    res = transform(res)
        return res
    
    def commit(self):
        if valid_session(self.session):
            if self.session.dry_run:
                self.session.rollback()
            else:
                self.session.commit()
        return self

    def rollback(self):
        if valid_session(self.session):
            self.session.rollback()
        return self
        
    def __enter__(self):
        """
        context manager entry point, creating an ORM session
        
        Example:
        --------
        with sql_table(..) as t:
            t.insert()
            t.delete()
            
        """
        if not valid_session(self.session):
            self.session = Session(self.engine)
            self.session.dry_run = None
        self.session.__enter__()
        return self

    def __exit__(self, type, value, traceback):
        """
        context manager exit point, removing the ORM session
        
        Example:
        --------
        with sql_table(..) as t:
            t.insert()
            t.delete()
            
        """
        self.commit()
        if valid_session(self.session):
            self.session.__exit__(type, value, traceback)
            self.session= None
        return self

    @property
    def _ids(self):
        """
        columns generated by the SQL Server and should not be provided by the user
        """
        return [c.name for c in self.table.columns if c.autoincrement]
    
    def _and(self, doc, keys):
        keys = self._col(keys)
        if len(keys) == 1:
            key = keys[0]
            return self.table.c[key] == doc[key]
        else:
            return sa.and_(*[self.table.c[i] == doc[i] for i in keys])

    def _id(self, doc):
        """
        creates a partial filter based on the document keys
        """
        pks = {i: doc[i] for i in self._pk if i in doc}
        if len(pks):
            return pks
        ids = {i : doc[i] for i in self._ids if i in doc}
        if len(ids):
            return ids
        keys = {i: doc[i] for i in doc if isinstance(doc[i], (int, str, datetime.datetime))}
        if len(keys):
            return keys
        return {}

    @property
    def nullables(self):
        """
        columns that are nullable
        """
        return [c.name for c in self.tbl.columns if c.nullable]
    
    @property
    def non_null(self):        
        """
        columns that must not be Null
        """
        return sorted([c.name for c in self.tbl.columns if c.nullable is False and c.server_default is None])

    @property
    def _columns(self):
        cols = self.columns
        return dict(zip(lower(cols), cols))


    def _kw(self, **kwargs):
        """
        converts kwargs dict into a sqlalchemy filtering expression
        usually, we just use the column names
        If the table is a document store and the key is not in the table columns, we assume the user wants to filter within the documnet
        This is a little bit of a hack since we encode all documents but works quite well for simple queries
        
        Example: query within a document store
        --------
        >>> from pyg import * 
        >>> table = partial(sql_table, db = 'test_db', schema = 'dbo', table = 'hello', nullable = 'a', pk = 'b', doc = True)
        >>> c = db_cell(a = 'a', b = 'b', ccy = 'USD', asset = 'bond', db = table)()
        >>> d = db_cell(a = 'b', b = 'c', ccy = 'EUR', asset = 'bond', db = table)()
        >>> e = db_cell(a = 'a', b = 'd', ccy = 'EUR', asset = 'bond', db = table)()

        >>> self = table()
        >>> assert len(self.inc(ccy = ['USD','EUR'])) == 3
        >>> assert len(self.inc(ccy = ['USD'])) == 1
        >>> assert len(self.inc(ccy = 'EUR')) == 2


        Example: query for a date within a doc store
        --------------------------------------------
        >>> from pyg import * 
        >>> import datetime
        >>> table = partial(sql_table, db = 'test_db', schema = 'dbo', table = 'dates', nullable = dict(a = datetime.datetime), pk = 'b', doc = True)
        >>> c = db_cell(a = dt(2000), b = 'b', ccy = dt(2000), asset = 'bond', db = table)()
        >>> d = db_cell(a = dt(2010), b = 'c', ccy = dt(2010), asset = 'bond', db = table)()
        >>> e = db_cell(a = dt(2020), b = 'd', ccy = 3, asset = 'bond', db = table)()

        >>> self = table()
        >>> assert len(self.inc(ccy = dt(2000))) == 1
        >>> assert len(self.inc(ccy = [dt(2000), dt(2010)])) == 2
        >>> assert len(self.inc(ccy = 3)) == 1
        
        """
        columns = _get_columns(self._table)
        conditions = []
        for k, v in kwargs.items():
            k = k.lower()
            if k in columns:
                col = columns[k]
                if len(col) > 1:
                    raise ValueError(f'condition {k}={v} has two columns {col} by this name so cannot satisfy')
                else:
                    col = col[0]
                conditions.append(_pw_filter(col, v))
            elif self.doc:
                col = columns[self.doc][0]
                vs = _like_within_doc(v, k)
                conditions.append(_pw_filter(col, vs))
            else:
                raise ValueError(f'column {k} not found')
        return sa.and_(*conditions)


    def _c(self, expression):
        """
        converts an expression to a sqlalchemy filtering expression
        
        :Example:
        ---------
        
        >>> expression = dict(a = 1, b = 2)
        >>> assert t._c(expression) == sa.and_(t.c.a == 1, t.c.b == 2)
        c = table.insert_many(dictable(a = ['a','aa','b', 'c'], b = ['bb','b1','c','d']))
        """
        if isinstance(expression, dict):
            return self._kw(**expression)
        elif isinstance(expression, (list, tuple)):
            return sa.or_(*[self._c(v) for v in expression])            
        else:
            return expression  
    
    @property
    def c(self):
        return self.table.c
    
            
    @property
    def _pk(self):
        """
        list of primary keys
        """
        return ulist(sorted(set(as_list(self.pk))))

    @property
    def reset(self):
        res = self.copy()
        res.spec = None
        res.selection = None
        res.order = None
        return res

    def find(self, *args, **kwargs):
        """
        This returns a table with additional filtering. note that you can build it iteratively
        
        :Parameters:
        ------------
        args: list of sa.Expression
            filter based on sqlalchemy tech
        
        kwargs: dict
            simple equality filters
        
        :Example:
        ---------
        >>> t.where(t.c.name == 'yoav')
        >>> t.find(name = 'yoav')
        
        :Example: building query in stages...
        ---------
        >>> t.inc(name = 'yoav').exc(t.c.age > 30) ## all the yoavs aged 30 or less        
        """
        if len(args) == 0 and len(kwargs) == 0:
            return self
        res = self.copy()
        if len(kwargs) > 0 and len(args) == 0:
            e = self._c(kwargs)
        elif len(args) > 0 and len(kwargs) == 0:
            e = self._c(args)
        else:
            raise ValueError('either args or kwargs must be empty, cannot have an "and" and "or" together')            
        if self.spec is None:
            res.spec = e
        else:
            res.spec = sa.and_(self.spec, e)            
        return res

    inc = find
    where = find
    filter = find
    
    def __sub__(self, other):
        """
        remove a column from the selection (select *WHAT* from table)

        :Parameters:
        ----------
        other : str/list of str
            names of columns excluded in SELECT statement
        """
        if self.selection is None:
            return self.select(self.columns - other)
        elif is_strs(self.selection):
            selection = self._col(as_list(self.selection))
            return self.select(ulist(selection) - other)
        else:
            selection = as_list(self.selection)
            other = as_list(other)
            selection = [col for col in selection if col.name not in other]
            return self.select(selection)
            
    def drop(self, deleted = False):
        if self.selection or self.spec:
            raise ValueError('To avoid confusing .delete and .drop, dropping a table can only be done if there is no selection and no filtering')
        if deleted and self._pk:
            self.deleted.drop()
        logger.info('dropping table: %s.%s.%s'%(_database(self.db), 
                                                  self.schema, 
                                                  self.table.name))

        self.table.drop(bind = self.engine)

    
    def join(self, right, onclose = None, isouter = False, full = False):
        res = self.copy()
        res.joint = as_list(self.joint) + [(right, onclose, isouter, full)]
        return res

    @property
    def _table(self):
        """
        a table supporting join objects
        """
        res = self.table
        for j in as_list(self.joint):            
            right, onclose, isouter, full = j
            if isinstance(right, partial):
                right = right()
            if isinstance(right, sql_cursor):
                right = right._table
            if is_strs(onclose):
                onclose = as_list(onclose)
                onclose = dict(zip(onclose, onclose))
            if is_dict(onclose):
                lhs = _get_columns(self.table)
                rhs = _get_columns(right)
                conditions = []
                for l,r in onclose.items():
                    l = lhs[l.lower()]
                    if len(l) > 1:
                        raise ValueError(f'multiple columns of same name {l}')
                    else:
                        l = l[0]
                    if is_str(r):
                        r = rhs[r.lower()]
                        if len(r) > 1:
                            raise ValueError(f'multiple columns of same name {l}')
                        else:
                            r = r[0]
                    conditions.append(l == r)
                onclose = sa.and_(*conditions)
            res = res.join(right, onclose, isouter = isouter, full = full)
        return res

    def exc(self, *args, **kwargs):
        """
        Exclude: This returns a table with additional filtering OPPOSITE TO inc. note that you can build it iteratively
        
        :Parameters:
        ------------
        args: list of sa.Expression
            filter based on sqlalchemy tech
        
        kwargs: dict
            simple equality filters
        
        :Example:
        ---------
        >>> t.where(t.c.name != 'yoav')
        >>> t.exc(name = 'yoav') 
        
        :Example: building query in stages...
        ---------
        >>> t.inc(name = 'yoav').exc(t.c.age > 30) ## all the yoavs aged 30 or less        
        """
        if len(args) == 0 and len(kwargs) == 0:
            return self
        elif len(kwargs) > 0 and len(args) == 0:
            e = not_(self._c(kwargs))
        elif len(args) > 0 and len(kwargs) == 0:
            e = not_(self._c(args))
        else:
            raise ValueError('either args or kwargs must be empty, cannot have an "and" and "or" together')            
        res = self.copy()
        if self.spec is None:
            res.spec = e
        else:
            res.spec = sa.and_(self.spec, e)            
        return res
    
    
    def __len__(self):
        statement = select(func.count()).select_from(self._table)
        if self.spec is not None:
            statement = statement.where(self.spec)
        return self.execute(statement, transform = list)[0][0]
    
    count = __len__


    def _col(self, column):
        columns = self.columns
        cols = dict(zip(lower(columns), columns))
        if is_str(column):
            return cols[column.lower()]
        elif isinstance(column, (list, tuple)):
            return [cols[c.lower()] if isinstance(c,str) else c for c in column]
        elif isinstance(column, dict):
            return type(column)({cols[k.lower()]: v for k, v in column.items()})
        else:
            raise ValueError(f'column {column} cannot be converted to table columns')

    @property    
    def columns(self):
        return ulist([col.name for col in self.table.columns])

    def select(self, *value):
        if len(value) == 0:
            return self
        res = self.copy()
        res.selection = as_list(value)
        return res
    
    def _enrich(self, doc, columns = None):
        """
        We assume we receive a dict of key:values which go into the db.
        some of the values may in fact be an entire document
        """
        docs = {k : v for k, v in doc.items() if isinstance(v, dict)}
        columns = ulist(self.columns if columns is None else columns)
        res = type(doc)({key : value for key, value in doc.items() if key in columns}) ## These are the only valid columns to the table
        if len(docs) == 0:
            return res
        missing = {k : [] for k in columns if k not in doc}
        for doc in docs.values():
            for m in missing:
                if m in doc:
                    missing[m].append(doc[m])
        found = {}
        conflicted = {} #
        for k, v in missing.items():
            if len(v) == 1:
                found[k] = v[0]
            elif len(v) > 1:
                p = [i for i in v if is_primitive(i)]
                if len(set(p)) == 1:
                    found[k] = p[0]
                else:
                    conflicted[k] = v
        if conflicted:
            raise ValueError(f'got multiple possible values for each of these columns: {conflicted}')
        res.update(found)
        return res
                
    def insert_one(self, doc, ignore_bad_keys = False, write = True):
        """
        insert a single document to the table

        Parameters
        ----------
        doc : dict
            record.
        ignore_bad_keys : 
            Suppose you have a document with EXTRA keys. Rather than filter the document, set ignore_bad_keys = True and we will drop irrelevant keys for you

        """
        if self.defaults:
            doc.update({k : v for k,v in self.defaults.items() if k not in doc})
        doc = _relabel(res = doc, selection = self.columns, strict = False) ## we want to replace what is possible
        edoc = self._dock(doc) if write else doc
        ids = self._ids
        columns = self.columns - ids
        if not ignore_bad_keys:
            bad_keys = {key: value for key, value in edoc.items() if key not in columns}
            if len(bad_keys) > 0:
                raise ValueError(f'cannot insert into db a document with these keys: {bad_keys}. The table only has these keys: {columns}')        
        res = self._write_doc(edoc, columns = columns) if write else edoc
        if self._pk and not self._is_deleted():
            doc_id = self._id(res)
            res_no_ids = type(res)({k : v for k, v in res.items() if k not in ids}) if ids else res
            tbl = self.inc().inc(**doc_id)
            read = tbl.sort(ids)._read_statement() ## row format
            docs = tbl._rows_to_docs(reader = False, load = False, **read) ## do not transform the document, keep in raw format?
            if len(docs) == 0:
                self.execute(self.table.insert(),[res_no_ids])
                if ids:    
                    latest = tbl[0]
                    doc.update(latest[ids])
            else:                
                if len(docs) == 1:
                    latest = docs[0] 
                else:
                    latest = docs[-1]
                    tbl.exc(**tbl._id(latest)).full_delete()
                latest = Dict(latest)
                deleted = datetime.datetime.now()
                for d in docs:
                    for i in ids:
                        if i in d:
                            del d[i]
                    d[_deleted] = deleted
                self.deleted.insert_many(docs, write = False)
                self.inc(self._id(latest)).update(**(res_no_ids))
                doc.update(latest[ids])
        else:
            self.execute(self.table.insert(), [res])
        return doc
    
    
    def _dock(self, doc, columns = None):
        """
        converts a usual looking document into a {self.doc : doc} format. 
        We then enrich the new document with various parameters. 
        This prepares it for "docking" in the database
        """
        
        columns = columns or self.columns
        edoc = self._enrich(doc, columns)
        if self.doc is None or self.doc is False or isinstance(edoc.get(self.doc), dict):
            return edoc
        else:
            edoc = {key: value for key, value in edoc.items() if key in columns}
            pk = self._pk + [self.doc]
            drop = [key for key in edoc if key not in pk]
            edoc[self.doc] = type(doc)({k : v for k, v in doc.items() if k not in drop})
            return edoc

    def _writer(self, writer = None, doc = None, kwargs = None):
        doc = doc or {}
        if writer is None:
            writer = doc.get(_root)
        if writer is None:
            writer = self.writer
        return as_writer(writer, kwargs = kwargs)
            
    def _write_doc(self, doc, writer = None, columns = None):
        columns = columns or self.columns
        writer = self._writer(writer, doc = doc, kwargs = doc)
        res = type(doc)({key: self._write_item(value, writer = writer) for key, value in doc.items() if key in columns})
        #res = self._dock(res, columns = columns) if dock else res
        return res

    def _write_item(self, item, writer = None, kwargs = None):
        """
        This does NOT handle the entire document. 
        """
        if not isinstance(item, dict):
            return item
        writer = self._writer(writer, item, kwargs = kwargs)
        res = item.copy()
        for w in as_list(writer):
            res = w(res)
        if isinstance(res, dict):
            res = dumps(res)
        return res
    
    def _undock(self, doc, columns = None):
        """
        converts a document which is of the format {self.doc : doc} into a regular looking document
        """
        if self.doc is None or self.doc is False or not isinstance(doc.get(self.doc), dict):
            return Dict(doc) if type(doc) == dict else doc
        res = doc[self.doc]
        columns = columns or self.columns
        for col in ulist(columns) - self.doc:
            if col in doc and col not in res:
                res[col] = doc[col]
        return Dict(res) if type(res) == dict else res

    def _reader(self, reader = None):
        return as_reader(self.reader if reader is None else reader)

    def _read_item(self, item, reader = None, load = True):
        reader = self._reader(reader)
        res = item
        if is_str(res) and res.startswith('{') and load:
            res = loads(res)
        for r in as_list(reader):
            res = res[r] if is_strs(r) else r(res)
        return res

    def _read_row(self, row, reader = None, columns = None, load = True):
        """
        reads a tuple of values (assumed to match the  columns)
        converts them into a dict document, does not yet undock them
        """
        reader = self._reader(reader)
        res = row
        if isinstance(res, sa.engine.row.LegacyRow):
            res = tuple(res)
        if isinstance(res, (list, tuple)):
            res = type(res)([self._read_item(item, reader = reader, load = load) for item in res])
            if columns:
                if len(columns) != len(res):
                    raise ValueError('mismatch in columns')
                res = dict(zip(columns, res)) # this zip can be evil
        return res
        
    def _read_statement(self, start = None, stop = None, step = None):
        """
        returns a list of records from the database. returns a list of tuples
        """
        statement = self.statement()
        if (is_int(start) and start < 0) or (is_int(stop) and stop < 0):
            n = len(self)
            start = n + start if is_int(start) and start < 0 else start                            
            stop = n + stop if is_int(stop) and stop < 0 else stop
        if start and self.order is not None:
            statement = statement.offset(start)
            stop = stop if stop is None else stop - start
        if stop is not None:
            statement = statement.limit(1+stop)
        data, columns = self.execute(statement, transform = _data_and_columns)
        if start is not None or stop is not None or step is not None:
            data = data[slice(start, stop, step)]
        return dict(data = data, columns = columns)
    
    
    @property
    def df(self):
        """
        This is a more optimized, faster version for reading the table. 
        It retuns the data as a pd.DataFrame,
        In addition, it converts NUMERIC type (which is cast to decimal.Decimal) into a float

        
        Parameters
        ----------
        decimal2float: bool
            converts sql.types.NUMERIC columns into float

        Returns
        -------
        pd.DataFrame
            The data, optimized as a dataframe.

        
        Example: speed comparison
        --------

        >>> from pyg import * 
        >>> t = sql_table(db = 'db', table = 'tbl_df', server = 'DESKTOP-GOQ0NSM', nullable = dict(a = int, b = float, c = str))
        >>> rs = dictable(a = range(100)) * dict(b = list(np.arange(0,100,1.0))) * dict(c = list('abcdefghij'))
        >>> t = t.insert_many(rs)      
        
        ## reading the data as t[::] is slow...
        >>> x = timer(lambda : t[::])()
        2022-08-21 18:03:52,594 - pyg - INFO - TIMER: took 0:00:13.139333 sec
 
        ## reading the data as t.df() is much faster...
        >>> y = timer(lambda : t.df())()
        2022-08-21 18:04:24,809 - pyg - INFO - TIMER: took 0:00:00.456988 sec

        Example: access using get item
        --------
        >>> t.df[:10]
        >>> t.df[100:120]
        >>> t.df[10]
        """
        return sql_df(self)
            
    
    def _rows_to_docs(self, data, reader = None, load = True, columns = None):
        """
        starts at raw values from the database and returns a list of read-dicts (or a single dict) from the database
        """
        if columns is None:
            columns = as_list(self.selection) if self.selection else self.columns
        reader = self._reader(reader)
        if isinstance(data, list):
            return [self._read_row(row, reader = reader, columns = columns, load = load) for row in data]
        else:        
            return self._read_row(data, reader = reader, columns = columns, load = load)

    def docs(self, start = None, stop = None, step = None, reader = None):
        read = self._read_statement(start = start, stop = stop, step = step)
        docs = self._rows_to_docs(reader = reader, **read)
        return dictable(docs)
    
    def read(self, item = 0, reader = None):
        value = len(self) + item if item < 0 else item
        statement = self.statement()
        if self.order is None:
            data, columns = self.execute(statement.limit(value+1), transform = _data_and_columns)
            row = data[value]
        else:
            data, columns = self.execute(statement.limit(value+1), transform = _data_and_columns)
            row = data[0]
        doc = self._rows_to_docs(data = row, reader = reader, columns = columns)
        rtn = self._undock(doc)
        return _relabel(rtn, self.selection)

                
    def __getitem__(self, value):
        """
        There are multiple modes to getitem:
        
        - t['key'] or t['key1', 'key2'] are equivalent to t.distinct('key') or t.distinct('key1', 'key2') 
        - t[['key1', 'key2']] will add a "SELECT key1, key2" to the statent
        - t[0] to grab a specific record. Note: this works better if you SORT the table first!, use t.sort('age')[10] to grab the name of the 11th youngest child in the class
        - t[::] a slice of the data: t.sort('age')[:10] are the 10 youngest students 
        
        :Example: support for columns case matching selection
        ---------
        >>> from pyg import * 
        >>> t = sql_table(db = 'db', table = 't', nullable = ['a', 'b'])
        >>> t.delete()
        >>> t.insert(dict(a = dict(x=1,y=2), b = 2))
        >>> assert t[['A']][::] == dictable(A = '1')
        >>> assert t[['A']].df().columns[0] == 'A'
        >>> assert t[['A']][0] == Dict(A = '1')
        >>> assert t[['A', 'b']].read(0) == Dict(A = '1', b = '2')
        """
        if isinstance(value, list):
            return self.select(value)

        elif isinstance(value, (str, tuple)):
            return self.distinct(*as_list(value))

        elif isinstance(value, dict):
            res = self.inc(**value)
            n = len(res)
            if n == 1:
                return res[0]
            elif n == 0:
                raise ValueError(f'no records found for {value}')
            else:
                raise ValueError(f'multiple {n} records found for {value}')

        elif isinstance(value, slice):
            start, stop, step = value.start, value.stop, value.step
            if step is False:
                step = None
                reader = False
            else:
                reader = None
            read = self._read_statement(start = start, stop = stop, step = step)
            docs = self._rows_to_docs(reader = reader, **read)
            columns = read['columns'] #self.columns
            res = dictable([self._undock(doc, columns = columns) for doc in docs])
            return _relabel(res, self.selection)

        elif is_int(value):
            return self.read(value)
    
    def update_one(self, doc, upsert = True):
        """
        Similar to insert, except will throw an error if upsert = False and an existing document is not there
        """
        if self.defaults:
            doc.update({k : v for k,v in self.defaults.items() if k not in doc})
        existing = self.inc().inc(**self._id(doc))
        n = len(existing)
        if n == 0:
            if upsert is False:
                raise ValueError(f'no documents found to update {doc}')
            else:
                return self.insert_one(doc)
        elif self._pk:
            return self.insert_one(doc)
        elif n == 1:
            doc = _relabel(doc, self.columns, strict = False)
            edoc = self._dock(doc)
            wdoc = self._write_doc(edoc)
            ids = self._ids
            for i in ids:
                if i in wdoc:
                    del wdoc[i]
            existing.update(**wdoc)
            res = existing[0]
            res.update(edoc)
            return self._undock(res)
        elif n > 1:
            raise ValueError(f'multiple documents found matching {doc}')
                
            
    def insert_many(self, docs, write = True):
        """
        insert multiple docs. 

        Parameters
        ----------
        docs : list of dicts, dictable, pd.DataFrame
        """
        rs = dictable(docs)
        if self.defaults:
            rs = rs(**{k : v for k,v in self.defaults.items() if k not in rs.keys()})
        rs = _relabel(rs, self.columns, strict = False)
        if len(rs) > 0:
            if self._pk and not self._is_deleted():
                _ = [self.insert_one(doc, write = write) for doc in rs]
            else:
                columns = self.columns - self._ids
                if write:
                    rows = [self._dock(row, columns) for row in rs]
                    rows = [self._write_doc(row, columns = columns) for row in rows]
                else:
                    rows = list(rs)
                self.execute(self.table.insert(), rows)
        return self

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __add__(self, item):
        """
        if item is dict, equivalent to insert_one(item)
        if item is dictable/pd.DataFrame, equivalent to insert_many(item)
        """
        if is_dict(item) and not is_dictable(item):
            self.insert_one(item)
        else:
            self.insert_many(item)
        return self

        
    def insert(self, data = None, columns = None, **kwargs):
        """
        This allows an insert of either a single row or multiple rows, from anything like 

        :Example:
        ----------
        >>> self.insert(name = ['father', 'mother', 'childa'], surname = 'common_surname') 
        >>> self.insert(pd.DataFrame(dict(name = ['father', 'mother', 'childa'], surname = 'common_surname')))
        
        
        Since we also support doc management, there is a possibility one is trying to enter a single document of shape dict(name = ['father', 'mother', 'childa'], surname = 'common_surname')
        We force the user to use either insert_one or insert_many in these cases.
        
        """
        rs = dictable(data = data, columns = columns, **kwargs) ## this allows us to insert multiple rows easily as well as pd.DataFrame
        if self.defaults:
            rs = rs(**{k : v for k,v in self.defaults.items() if k not in rs.keys()})
        if len(rs)>1:
            pk = self._pk
            if pk:
                u = rs.listby(self._pk)
                u = dictable([row for row in u if len((row - pk).values()[0])>1])
                if len(u):
                    u = u.do(try_back(unique))                
                    u0 = u[0].do(try_back(unique))
                    u0 = {k:v for k,v in u0.items() if k in self._pk or isinstance(v, list)}
                    raise ValueError('When trying to convert data into records, we detected multiple rows with same unique %s, e.g. \n\n%s\n\nCan you please use .insert_many() or .insert_one() to resolve this explicitly'%(self._pk, u0))
            elif self.doc:
                if isinstance(data, list) and len(data) < len(rs):
                    raise ValueError('Original value contained %s rows while new data has %s.\n We are unsure if you are trying to enter documents with list in them.\nCan you please use .insert_many() or .insert_one() to resolve this explicitly'%(len(data), len(rs)))
                elif isinstance(data, dict) and not isinstance(data, dictable):
                    raise ValueError('Original value provided as a dict while now we have %s multiple rows.\nWe think you may be trying to enter a single document with lists in it.\nCan you please use .insert_many() or .insert_one() to resolve this explicitly'%len(rs))
        return self.insert_many(rs)

    def find_one(self, doc = None, *args, **kwargs):
        res = self.find(*args, **kwargs)
        if doc:
            filter_by_doc = self._id(doc)
            if filter_by_doc is not None:
                res = res.find(filter_by_doc)
        if len(res) == 1:
            return res
        elif len(res) == 0:
            raise ValueError('no document found for %s %s %s'%(doc, args, kwargs))
        elif len(res) > 1:
            raise ValueError('multiple documents found for %s %s %s'%(doc, args, kwargs))
    
    
    def _select(self):
        """
        performs a selection based on self.selection

        >>> from pyg import *        
        >>> t1  = sql_table(table = 't1', nullable = ['a', 'b', 'c'], db = 'db')
        >>> t1.insert(dictable(a = 'a', b = ['a','b','c'], c = 'hi'))
        t1[['a','b']].inc(B = 'b')

        >>> t2  = sql_table(table = 't2', nullable = ['x', 'y', 'z'], db = 'db')
        >>> t2.insert(dictable(x = 'x', y = ['a','b','c'], z = 'world'))

        >>> t4  = sql_table(table = 't4', nullable = ['a', 'b', 'c'], db = 'db')
        >>> t4.insert(dictable(a = 'u', b = ['a','b','c'], c = 'beautiful'))

        t1.join(t2, t1.c['b']==t2.c['y'])[['a', 'b', 'z']][::]
        t1.join(t4, 'b').inc(a = 'a')
        [col.name for col in t1.table.join(t4.table, t1.c.b==t4.c.b).columns]
        """
        table = self._table
        if self.selection is None:
            return select(table)
        columns = _get_columns(self._table)
        selection = []
        for col in as_list(self.selection):
            if is_str(col):
                col = col.lower()
                if col in columns:
                    s = columns[col]
                    if len(s) > 1:
                        raise ValueError(f'{col} is in two tables {s} so cannot resolve')
                    else:
                        s = s[0]                        
                    selection.append(s)
                else:
                    raise ValueError(f'{col} not found in the table')
            else:
                selection.append(col) ## it is assumed to be a sqlalchemy selection
        statement = select(selection).select_from(table)
        return statement

    
    def statement(self):
        """
        We build a statement from self.spec, self.selection and self.order objects
        A little like:
        
        >>> self.table.select(self.selection).where(self.spec).order_by(self.order)

        """
        statement = self._select()            
        if self.spec is not None:
            statement = statement.where(self.spec)
        if self.order is not None:
            order = self.order
            cols = _get_columns(self._table)
            if isinstance(order, (str,list)):
                order = {o: 1 for o in as_list(order)}
            order_by = []
            for k, v in order.items():
                col = cols[k.lower()]
                if len(col) > 1:
                    raise ValueError(f'cannot sort as multiple col {k} in join: {col}')
                else:
                    order_by.append(_orders[v](col[0]))
            statement = statement.order_by(*order_by)
        return statement
    
    def update(self, **kwargs):
        if len(kwargs) == 0:
            return self
        statement = self.table.update()
        if self.spec is not None:
            statement = statement.where(self.spec)
        statement = statement.values(kwargs)
        self.execute(statement)
        return self
    
    set = update

    def full_delete(self):
        """
        A standard delete will actually auto-archive a table with primary keys. # i.e. we have full audit
        .full_delete() will drop the currently selected records without archiving them first
        
        """
        statement = self.table.delete()
        if self.spec is not None:
            statement = statement.where(self.spec)
        self.execute(statement)
        return self

    def delete(self, **kwargs):
        res = self.inc(**kwargs)
        ids = self._ids
        if len(res):
            if self._pk and not self._is_deleted(): ## we first copy the existing data out to deleted db
                read = self._read_statement() 
                docs = self._rows_to_docs(reader = False, load = False, **read)
                #docs = self._rows_to_docs(load = True, **read)
                deleted = datetime.datetime.now()
                for doc in docs:
                    doc[_deleted] = deleted
                    for i in ids:
                        if i in doc:
                            del doc[i]
                self.deleted.insert_many(docs, write = False)
            res.full_delete()
        return self

    def sort(self, *order, **orderby):
        """
        Allows sorting of the table by multiple methods:
            
        :Example:
        ---------
        >>> t = sql_table(db = 'db', table = 'tbl_df', server = 'DESKTOP-GOQ0NSM', nullable = dict(a = int, b = float, c = str))
        >>> t.sort(a = 'desc', b = 'asc')
        >>> t.sort(dict(a = 'desc', b = 'asc'))
        >>> t.sort(a = -1, b = 1)
        >>> t.sort('a', 'b')
        >>> t.sort(['a', 'b'])
        """        
        order = as_list(order)
        if len(order) == 1 and isinstance(order[0], dict):
            order = order[0]
        if len(orderby):
            if isinstance(order, dict):
                order.append(orderby)
            elif len(order) == 0:
                order = orderby
            else:
                raise ValueError('cannot mix order and orderby')
        if not order:
            return self
        else:
            res = self.copy()
            res.order = order
            return res
        
    @property
    def name(self):
        """
        table name
        """
        return self.table.name
    
    
    def distinct(self, *keys):
        """
        select DISTINCT *keys FROM TABLE
        """
        keys = as_list(keys)
        if len(keys) == 0 and self.selection is not None:
            keys = as_list(self.selection)
        if is_strs(keys):
            keys = self._col(keys)
            keys = [self.table.columns[k] for k in keys]
        session = Session(self.engine)
        query = session.query(*keys)
        if self.spec is not None:
            query = query.where(self.spec)        
        res = query.distinct().all()
        if len(keys)==1:
            res = [row[0] for row in res]
        return res
    
    def __getattr__(self, attr):
        if attr.lower() in self._columns:
            return self.distinct(attr)
        else:
            raise AttributeError(f"'sql_cursor' object has no attribute '{attr}'")
    
    def __repr__(self):
        statement = self.statement()
        params = statement.compile().params
        prefix = '%s.%s'%(self.schema, self.table.name) if self.schema else self.table.name
        text = str(statement).replace('"','').replace(prefix + '.','')
        for k,v in params.items():
            text = text.replace(':'+k, '"%s"'%v if is_str(v) else dt2str(v) if is_date(v) else str(v))
            
        res = 'sql_cursor: %(db)s.%(table)s%(pk)s %(doc)s %(w)s\n%(statement)s\n%(n)i records'%dict(db = _database(self.db), table = prefix, 
                                                                                              doc = 'DOCSTORE[%s]'%self.doc if self.doc else '', 
                                                                                              w = '\nwriter: %s\n'%self.writer if is_str(self.writer) else '',
                                                                                              pk = self._pk if self._pk else '', 
                                                                                              n = len(self), 
                                                                                              statement = text)
        return res

    def _is_deleted(self):
        return is_str(self.schema) and self.schema.startswith(_archived)

    @property
    def deleted(self):
        if self._is_deleted() or len(self._pk) == 0:
            return self
        else:
            schema = _archived + (self.schema or '')
            # logger.info('archived schema: %s'%schema)
            writer = self.writer
            if is_str(writer) and writer.endswith('.sql'):
                params = writer.split('/')
                params[2] = schema
                writer = '/'.join(params)
                writer = writer.replace('.sql','/%deleted.sql')
            res = sql_table(table = self.table, 
                            db = self.db, 
                            non_null = dict(deleted = datetime.datetime), 
                            server = self.server, 
                            pk = self._pk + [_deleted], 
                            doc = self.doc, 
                            writer = writer, 
                            reader = self.reader, 
                            schema = schema)
            #res.spec = self.spec THIS NEEDS TO BE IMPLEMENTED PROPERLY
            res.order = self.order
            res.selection = self.selection
            return res
                
    @property
    def address(self):
        """
        :Returns:
        ---------
        tuple
            A unique combination of the server address, db name and table name, identifying the table uniquely. This allows us to create an in-memory representation of the data in pyg-cell

        """
        return ('server', self.server), ('db', self.db), ('schema', self.schema), ('table', self.table.name)


