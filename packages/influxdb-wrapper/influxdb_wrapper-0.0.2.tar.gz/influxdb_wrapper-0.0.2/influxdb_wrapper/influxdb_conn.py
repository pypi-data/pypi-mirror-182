from .db_conn import DBConn, DBOpenException, DBExceptionNotOpen, DBGetLockException, DBReleaseLockException
from datetime import datetime
from influxdb import InfluxDBClient
from copy import deepcopy


class InfluxDBConn(DBConn):
    def __init__(self):
        super().__init__()
        self.conn = None

    def openConn(self, params, autocommit=True):
        host = params['host']
        user = params['user']
        password = params['password']
        bucket = params['bucket']

        self.conn = InfluxDBClient(host=host, username=user, password=password, database=bucket)

    def closeConn(self):
        self.conn.close()

    def insert(self, table, rows):
        if not self.conn:
            raise DBExceptionNotOpen('Database not opened')

        points = deepcopy(rows)
        for point in points:
            point["measurement"] = table
            if 'time' not in point or not point['time']:
                point['time'] = datetime.utcnow()

        self.conn.write_points(points)

    def getLock(self, lockname):
        raise

    def releaseLock(self, lockname):
        raise
