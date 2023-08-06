class DbConnector(object):
    conn = None

    def __init__(self, config):
        pass

    def read_last_measures(self, number_of_measures: int, sensor_id: int) -> list:
        raise Exception('Need to overload this function')


def dbconnector_factory(config: dict, db_type: str = 'influx') -> DbConnector:
    if db_type == 'influx':
        from dbconnector.influx_connector import InfluxConnector
        return InfluxConnector(config)
    elif db_type == 'mock':
        from dbconnector.mock_connector import MockConnector
        return MockConnector(config)
