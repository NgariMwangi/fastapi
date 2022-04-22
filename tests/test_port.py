from tests.skeleton_test import Skeleton_test
from main import app
import unittest
from fastapi.testclient import TestClient


class Port_test(Skeleton_test):
    """this is  test to make sure app is running in prt 5000"""
    def setUp(self): 
        self.app = TestClient(app)
      

    def test_port(self):
        response = self.app.get("http://127.0.0.1:8000/docs")
        self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    unittest.main()


