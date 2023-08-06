from influxdb import InfluxDBClient
from .db_connector import DbConnector


class InfluxConnector(DbConnector):
    def __init__(self, config):
        host = config['influxdbconn']['host']
        user = config['influxdbconn']['user']
        password = config['influxdbconn']['password']
        bucket = config['influxdbconn']['bucket']

        self.conn = InfluxDBClient(host=host, username=user, password=password, database=bucket)

    def read_last_measures(self, number_of_measures: int, sensor_id: int) -> list:
        query = """SELECT * from DHT22 WHERE sensorid='{}'
                ORDER BY time DESC LIMIT {}""".format(sensor_id, number_of_measures)
        result_set = self.conn.query(query)
        points = list(result_set.get_points())

        return points
