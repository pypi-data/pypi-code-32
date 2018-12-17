"""
MySQLdb - A DB API v2.0 compatible interface to MySQL.

This package is a wrapper around _mysql, which mostly implements the
MySQL C API.

connect() -- connects to server

See the C API specification and the MySQL documentation for more info
on other items.

For information on how MySQLdb handles type conversion, see the
MySQLdb.converters module.
"""

from MySQLdb.release import __version__, version_info, __author__

from . import _mysql

if version_info != _mysql.version_info:
    raise ImportError("this is MySQLdb version %s, but _mysql is version %r" %
                      (version_info, _mysql.version_info))

threadsafety = 1
apilevel = "2.0"
paramstyle = "format"

from ._mysql import *
from MySQLdb.compat import PY2
from MySQLdb.constants import FIELD_TYPE
from MySQLdb.times import Date, Time, Timestamp, \
    DateFromTicks, TimeFromTicks, TimestampFromTicks

try:
    frozenset
except NameError:
    from sets import ImmutableSet as frozenset

class DBAPISet(frozenset):
    """A special type of set for which A == x is true if A is a
    DBAPISet and x is a member of that set."""

    def __eq__(self, other):
        if isinstance(other, DBAPISet):
            return not self.difference(other)
        return other in self


STRING    = DBAPISet([FIELD_TYPE.ENUM, FIELD_TYPE.STRING,
                     FIELD_TYPE.VAR_STRING])
BINARY    = DBAPISet([FIELD_TYPE.BLOB, FIELD_TYPE.LONG_BLOB,
                     FIELD_TYPE.MEDIUM_BLOB, FIELD_TYPE.TINY_BLOB])
NUMBER    = DBAPISet([FIELD_TYPE.DECIMAL, FIELD_TYPE.DOUBLE, FIELD_TYPE.FLOAT,
                     FIELD_TYPE.INT24, FIELD_TYPE.LONG, FIELD_TYPE.LONGLONG,
                     FIELD_TYPE.TINY, FIELD_TYPE.YEAR, FIELD_TYPE.NEWDECIMAL])
DATE      = DBAPISet([FIELD_TYPE.DATE])
TIME      = DBAPISet([FIELD_TYPE.TIME])
TIMESTAMP = DBAPISet([FIELD_TYPE.TIMESTAMP, FIELD_TYPE.DATETIME])
DATETIME  = TIMESTAMP
ROWID     = DBAPISet()

def test_DBAPISet_set_equality():
    assert STRING == STRING

def test_DBAPISet_set_inequality():
    assert STRING != NUMBER

def test_DBAPISet_set_equality_membership():
    assert FIELD_TYPE.VAR_STRING == STRING

def test_DBAPISet_set_inequality_membership():
    assert FIELD_TYPE.DATE != STRING

if PY2:
    def Binary(x):
        return bytearray(x)
else:
    def Binary(x):
        return bytes(x)

def Connect(*args, **kwargs):
    """Factory function for connections.Connection."""
    from MySQLdb.connections import Connection
    return Connection(*args, **kwargs)

connect = Connection = Connect

__all__ = [ 'BINARY', 'Binary', 'Connect', 'Connection', 'DATE',
    'Date', 'Time', 'Timestamp', 'DateFromTicks', 'TimeFromTicks',
    'TimestampFromTicks', 'DataError', 'DatabaseError', 'Error',
    'FIELD_TYPE', 'IntegrityError', 'InterfaceError', 'InternalError',
    'MySQLError', 'NULL', 'NUMBER', 'NotSupportedError', 'DBAPISet',
    'OperationalError', 'ProgrammingError', 'ROWID', 'STRING', 'TIME',
    'TIMESTAMP', 'Warning', 'apilevel', 'connect', 'connections',
    'constants', 'converters', 'cursors', 'debug', 'escape',
    'escape_string', 'get_client_info',
    'paramstyle', 'string_literal', 'threadsafety', 'version_info']

