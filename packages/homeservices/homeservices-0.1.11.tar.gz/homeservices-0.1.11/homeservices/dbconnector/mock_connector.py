from .db_connector import DbConnector


class MockConnector(DbConnector):
    def read_last_measures(self, number_of_measures: int, sensor_id: int) -> list:
        measures = {1: [{'time': '2022-12-19T13:32:02.501231Z', 'humidity': 53.3, 'sensorid': '1', 'temp': 20.3},
                        {'time': '2022-12-19T13:30:02.442527Z', 'humidity': 53.3, 'sensorid': '1', 'temp': 20.3},
                        {'time': '2022-12-19T13:28:03.145696Z', 'humidity': 53.3, 'sensorid': '1', 'temp': 20.3},
                        {'time': '2022-12-19T13:26:02.852427Z', 'humidity': 53.4, 'sensorid': '1', 'temp': 20.2}],
                    2: [{'time': '2022-12-19T13:32:02.501231Z', 'humidity': 53.3, 'sensorid': '2', 'temp': 20.3},
                        {'time': '2022-12-19T13:30:02.442527Z', 'humidity': 53.3, 'sensorid': '2', 'temp': 20.3},
                        {'time': '2022-12-19T13:28:03.145696Z', 'humidity': 53.3, 'sensorid': '2', 'temp': 20.3},
                        {'time': '2022-12-19T13:26:02.852427Z', 'humidity': 53.4, 'sensorid': '2', 'temp': 20.2}],
                    3: [{'time': '2022-12-19T13:32:02.501231Z', 'humidity': 53.3, 'sensorid': '3', 'temp': 20.3},
                        {'time': '2022-12-19T13:30:02.442527Z', 'humidity': 53.3, 'sensorid': '3', 'temp': 20.3},
                        {'time': '2022-12-19T13:28:03.145696Z', 'humidity': 53.3, 'sensorid': '3', 'temp': 20.3},
                        {'time': '2022-12-19T13:26:02.852427Z', 'humidity': 53.4, 'sensorid': '3', 'temp': 20.2}]
                    }
        points = measures[sensor_id][-number_of_measures:]

        return points
