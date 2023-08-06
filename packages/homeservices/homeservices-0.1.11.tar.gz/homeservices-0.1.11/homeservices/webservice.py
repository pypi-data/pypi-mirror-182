from flask import Flask, request, make_response, Response
from flask_compress import Compress
from urllib import parse
import json

from baseutils_phornee import ManagedClass
from baseutils_phornee import Config

from dbconnector.db_connector import dbconnector_factory


class HomeServices(ManagedClass):

    def __init__(self,  template_folder: str, static_folder: str, db_connector: str = 'influx') -> None:
        """_summary_

        Args:
            template_folder (string): Path for the Flask templates
            static_folder (string): Path for the Flask static info
        """
        self.app = Flask(__name__,  template_folder=template_folder, static_folder=static_folder)
        self.app.add_url_rule('/', 'index', self.index, methods=['GET'])
        self.app.add_url_rule('/alexaintent', 'alexaintent', self.alexa_intent, methods=['GET'])
        self.app.add_url_rule('/customsensor', 'customsensor', self.custom_sensor, methods=['GET'])
        Compress(self.app)

        conf_params = {'modulename': self.getClassName(), 'execpath': __file__}
        self.config = Config(conf_config=conf_params)

        self.db_conn = dbconnector_factory(self.config, db_connector)

    @classmethod
    def getClassName(cls) -> str:
        """
        Returns:
           string: class name
        """
        return "homeservices"

    def getApp(self) -> Flask:
        """
        Returns:
            Flask app: The flask app
        """
        return self.app

    def run(self) -> None:
        """Execution of the application
        """
        self.app.run()
        # self.app.run(host='0.0.0.0')

    def index(self) -> Response:
        """Main entry point

        Returns:
            http_response: response string
        """
        return 'This is the Pi server.'

    def _read_last_measures(self, number_of_measures: int, sensor_name: str) -> list:
        sensor_table = {'jardín': 2, 'cocina': 1, 'buhardilla': 3}

        points = None

        if sensor_name in sensor_table:
            points = self.db_conn.read_last_measures(number_of_measures, sensor_table[sensor_name])

        return points

    def custom_sensor(self) -> Response:
        """Answer to sensor requests. It returns

        Returns:
            http_response: json with temperature and humidity information
        """
        if request.method == 'GET':
            params = parse.parse_qs(parse.urlparse(request.url).query)
            # Parse GET param
            if 'sensor' in params:
                sensor = params['sensor'][0]

                points = self._read_last_measures(1, sensor)

                if points:
                    point = points[0]

                    response = make_response(json.dumps('{{"temp" : {}, "hum" : {} }}'.format(point['temp'],
                                                                                              point['humidity'])))
                    response.mimetype = "application/json"
                    response.headers['Pragma'] = 'no-cache'
                    response.headers["Expires"] = 0
                    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
                else:
                    response = make_response("Sensor not found", 404)
            else:
                response = make_response("Sensor not specified", 404)
            return response

    def alexa_intent(self) -> Response:
        """Function to be called from alexa intent, that will return human-readable string to be speeched out by Alexa

        Returns:
           http_response: Verbose string human-readable with the information of the sensor temperature
        """
        if request.method == 'GET':
            params = parse.parse_qs(parse.urlparse(request.url).query)
            # Parse GET param
            if 'sensor' in params:
                sensor = parse.parse_qs(parse.urlparse(request.url).query)['sensor'][0]

                points = self._read_last_measures(4, sensor)

                trend = ''
                if points and len(points) == 4:
                    delta = points[0]['temp'] - points[3]['temp']
                    if delta > 0.6:
                        trend = ' y subiendo a saco'
                    elif delta > 0.3:
                        trend = ' y subiendo'
                    elif delta > 0.1:
                        trend = ' y subiendo ligeramente'
                    elif delta < -0.6:
                        trend = ' y bajando a saco'
                    elif delta < -0.3:
                        trend = ' y bajando'
                    elif delta < -0.1:
                        trend = ' y bajando ligeramente'

                    response_phrase = """Hace {} grados{},
                                         y la humedad es del {:.0f} por ciento.""".format(points[0]['temp'],
                                                                                          trend,
                                                                                          points[0]['humidity'])
                    if points[0]['humidity'] > 98:
                        response_phrase += " Es muy posible que esté lloviendo."

                    if points[0]['temp'] < 5:
                        response_phrase += " ¡Joder, que frio hace!."
                    elif points[0]['temp'] < 10:
                        response_phrase += " Hace bastante fresquete."
                    elif points[0]['temp'] > 30:
                        response_phrase += " ¡Que calor hace!."
                    elif points[0]['temp'] > 35:
                        response_phrase += " ¡Joder, que nos achicharramos!."
                    response = make_response(response_phrase.encode('UTF-8'))
                    response.mimetype = "text/plain"
                    response.headers['Pragma'] = 'no-cache'
                    response.headers["Expires"] = 0
                    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
                else:
                    response = make_response("Sensor not found", 404)
            else:
                response = make_response("Sensor not specified", 404)

            return response
