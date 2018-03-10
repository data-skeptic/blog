## Simple SQL Query Not Working with Pandas Solution

Are you experiencing the problem shown in the trace below?

It's a very obtuse error message that does not help you get to the bottom of it.  Your SQL query probaby contains the `%` symbol, as in

```SELECT email FROM users WHERE name like 'Kyle%'```

Try using a doube `%%` like this:

```SELECT email FROM users WHERE name like 'Kyle%%'```

```---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-23-edfb2833c07f> in <module>()
----> 1 pd.read_sql("SELECT * FROM pg_catalog.pg_tables WHERE tablename like '%user%'", con1)

/opt/anaconda3/envs/ds/lib/python3.5/site-packages/pandas/io/sql.py in read_sql(sql, con, index_col, coerce_float, params, parse_dates, columns, chunksize)
    414             sql, index_col=index_col, params=params,
    415             coerce_float=coerce_float, parse_dates=parse_dates,
--> 416             chunksize=chunksize)
    417 
    418 

/opt/anaconda3/envs/ds/lib/python3.5/site-packages/pandas/io/sql.py in read_query(self, sql, index_col, coerce_float, parse_dates, params, chunksize)
   1085         args = _convert_params(sql, params)
   1086 
-> 1087         result = self.execute(*args)
   1088         columns = result.keys()
   1089 

/opt/anaconda3/envs/ds/lib/python3.5/site-packages/pandas/io/sql.py in execute(self, *args, **kwargs)
    976     def execute(self, *args, **kwargs):
    977         """Simple passthrough to SQLAlchemy connectable"""
--> 978         return self.connectable.execute(*args, **kwargs)
    979 
    980     def read_table(self, table_name, index_col=None, coerce_float=True,

/opt/anaconda3/envs/ds/lib/python3.5/site-packages/sqlalchemy/engine/base.py in execute(self, statement, *multiparams, **params)
   2056 
   2057         connection = self.contextual_connect(close_with_result=True)
-> 2058         return connection.execute(statement, *multiparams, **params)
   2059 
   2060     def scalar(self, statement, *multiparams, **params):

/opt/anaconda3/envs/ds/lib/python3.5/site-packages/sqlalchemy/engine/base.py in execute(self, object, *multiparams, **params)
    937         """
    938         if isinstance(object, util.string_types[0]):
--> 939             return self._execute_text(object, multiparams, params)
    940         try:
    941             meth = object._execute_on_connection

/opt/anaconda3/envs/ds/lib/python3.5/site-packages/sqlalchemy/engine/base.py in _execute_text(self, statement, multiparams, params)
   1095             statement,
   1096             parameters,
-> 1097             statement, parameters
   1098         )
   1099         if self._has_events or self.engine._has_events:

/opt/anaconda3/envs/ds/lib/python3.5/site-packages/sqlalchemy/engine/base.py in _execute_context(self, dialect, constructor, statement, parameters, *args)
   1187                 parameters,
   1188                 cursor,
-> 1189                 context)
   1190 
   1191         if self._has_events or self.engine._has_events:

/opt/anaconda3/envs/ds/lib/python3.5/site-packages/sqlalchemy/engine/base.py in _handle_dbapi_exception(self, e, statement, parameters, cursor, context)
   1394                 )
   1395             else:
-> 1396                 util.reraise(*exc_info)
   1397 
   1398         finally:

/opt/anaconda3/envs/ds/lib/python3.5/site-packages/sqlalchemy/util/compat.py in reraise(tp, value, tb, cause)
    184         if value.__traceback__ is not tb:
    185             raise value.with_traceback(tb)
--> 186         raise value
    187 
    188 else:

/opt/anaconda3/envs/ds/lib/python3.5/site-packages/sqlalchemy/engine/base.py in _execute_context(self, dialect, constructor, statement, parameters, *args)
   1180                         statement,
   1181                         parameters,
-> 1182                         context)
   1183         except BaseException as e:
   1184             self._handle_dbapi_exception(

/opt/anaconda3/envs/ds/lib/python3.5/site-packages/sqlalchemy/engine/default.py in do_execute(self, cursor, statement, parameters, context)
    460 
    461     def do_execute(self, cursor, statement, parameters, context=None):
--> 462         cursor.execute(statement, parameters)
    463 
    464     def do_execute_no_params(self, cursor, statement, context=None):

TypeError: 'dict' object does not support indexing```


