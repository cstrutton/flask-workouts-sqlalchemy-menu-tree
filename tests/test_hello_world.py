import unittest
from flask import current_app
from app import create_app #, db


class HelloWorldTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.test_client = self.app.test_client()
#       db.create_all()

    def tearDown(self):
#       db.session.remove()
#       db.drop_all()
        pass

    def test_app_exists(self):
        self.assertFalse(self.app is None)
    
    def test_app_is_testing(self):
        self.assertTrue(self.app.config['TESTING'])
        
    def test_index_returns_helloworld(self):
        rv = self.test_client.get('/')
        assert 'hello world' in rv.data        
        