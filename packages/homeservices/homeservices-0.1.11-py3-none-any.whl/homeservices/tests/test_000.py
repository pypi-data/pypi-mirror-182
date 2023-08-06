import unittest
import os
import sys
import inspect
from pathlib import Path

THIS_FOLDER = os.path.dirname(inspect.getfile(inspect.currentframe()))
sys.path.insert(0, os.path.dirname(THIS_FOLDER))
from webservice import HomeServices  # noqa


class Testing(unittest.TestCase):
    templates_path = "{}/templates".format(Path().absolute())
    static_path = "{}/static".format(Path().absolute())
    service = HomeServices(template_folder=templates_path, static_folder=static_path, db_connector='mock')
    client = service.getApp().test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_alexaintent(self):
        response = self.client.get('/alexaintent')
        self.assertEqual(response.status_code, 404)
        response = self.client.get('/alexaintent?sensor=buhardilla')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/alexaintent?sensor=unexisting')
        self.assertEqual(response.status_code, 404)

    def test_customsensor(self):
        response = self.client.get('/customsensor')
        self.assertEqual(response.status_code, 404)
        response = self.client.get('/customsensor?sensor=buhardilla')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/customsensor?sensor=unexisting')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
