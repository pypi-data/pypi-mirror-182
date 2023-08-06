from .db_conn import DBConn, DBExceptionNotOpen
from datetime import datetime
from copy import deepcopy


class InfluxMockDBConn(DBConn):
    def __init__(self):
        super().__init__()
        self.db_tables = None

    def openConn(self, params, autocommit=True):
        self.db_tables = {}

    def closeConn(self):
        self.conn.close()

    def insert(self, table, rows):
        if self.db_tables is None:
            raise DBExceptionNotOpen('Database not opened')

        points = deepcopy(rows)
        for point in points:
            point["measurement"] = table
            if 'time' not in point or not point['time']:
                point['time'] = datetime.utcnow()
        self.db_tables[table] = points

    def getLock(self, lockname):
        raise

    def releaseLock(self, lockname):
        raise
