import os
import json
import unittest
from shutil import copy

from app import app, db, Property

basedir = os.path.abspath(os.path.dirname(__file__))

class BasicTestCase(unittest.TestCase):

    def test_app_is_running(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_database(self):
        tester = os.path.exists("properties.db")
        self.assertTrue(tester)


class APITestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        # copy the original database
        copy(os.path.join(basedir, 'properties.db'), os.path.join(basedir, 'properties.test.db'))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'properties.test.db')

    def tearDown(self):
        os.remove(os.path.join(basedir, 'properties.test.db'))

    def test_property_list_api(self):
        response = self.app.get("/api/properties/")
        data = json.loads(response.get_data())

        self.assertEqual(response.status_code, 200)

        non_unselected_properties = Property.query.filter((Property.selected == None) | (Property.selected == 1)).all()
        self.assertEqual(len(data), len(non_unselected_properties))

    def test_property_select_api(self):
        api = "/api/properties/1"

        # test valid put request with selected is true
        put_data = {
            'property_id': 1,
            'selected': True
        }

        response = self.app.put(api, data=json.dumps(put_data), content_type='application/json')
        data = json.loads(response.get_data())

        self.assertEqual(response.status_code, 200)
        self.assertTrue('property_id' in data)
        self.assertEqual(data['property_id'], 1)

    def test_property_unselect_api(self):
        api = "/api/properties/1"

        # test valid put request with selected is false
        put_data = {
            'property_id': 1,
            'selected': False
        }

        response = self.app.put(api, data=json.dumps(put_data), content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        non_unselected_properties = Property.query.filter((Property.selected == None) | (Property.selected == 1)).all()
        self.assertEqual(len(data), len(non_unselected_properties))

    def test_property_not_found(self):
        api = "/api/properties/2000"

        # test valid put request with selected is false
        put_data = {
            'property_id': 2000,
            'selected': False
        }

        response = self.app.put(api, data=json.dumps(put_data), content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()