import unittest
import os
import sys
import inspect

THIS_FOLDER = os.path.dirname(inspect.getfile(inspect.currentframe()))
sys.path.insert(0, os.path.dirname(THIS_FOLDER))
# from influxdb_wrapper import InfluxDBConn  # noqa
from influxdb_wrapper import InfluxMockDBConn  # noqa


class Testing(unittest.TestCase):
    db = InfluxMockDBConn()
    db.openConn(None)

    def test_index(self):
        points = [
                    {
                        "tags": {"sensorid": 0},
                        "fields": {"temp": 20.0, "humidity": 50.0}
                    }
                ]
        self.db.insert('DHT22', points)


if __name__ == '__main__':
    unittest.main()
