from main import app
import json
import unittest
from tests.skeleton_test import Skeleton_test

class Test_login(Skeleton_test):
    """This class test login"""

    def test_login(self):
        """testing succesful login"""
        # first we register
        name = "dennis"
        email = "dennohmwangi$@gmail.com"
        password = "deno0707"
        wrong_password = "notpassword"

        register_payload = json.dumps(
            {"name": name, "email": email, "password": password}
        )
        login_payload = json.dumps({"username": email, "password": password})
        # response = self.app.post(url_to_register, headers={"Content-Type": "application/json"},data=payload)
        self.app.post(
            "http://127.0.0.1:8000/user",
            headers={"Content-Type": "application/json"},
            data=register_payload,
        )

        # posting to login endpoint
        response = self.app.post(
            "http://127.0.0.1:8000/Login",
            headers={"Content-Type": "application/json"},
            data=login_payload,
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 201)

    def test_unsucceful_login(self):
        """Tests unsuccessfull login"""
        fullname = "morgan"
        email = "morgan@gmail"
        password = "morgan"
        wrong_password = "notpassword"

        register_payload = json.dumps(
            {"name": fullname, "email": email, "password": password}
        )
        login_payload = json.dumps({"username": email, "password": wrong_password})
        # response = self.app.post(url_to_register, headers={"Content-Type": "application/json"},data=payload)
        self.app.post(
            "http://127.0.0.1:8000/user",
            headers={"Content-Type": "application/json"},
            data=register_payload,
        )

        # posting to login endpoint
        response = self.app.post(
            "http://127.0.0.1:8000/Login",
            headers={"Content-Type": "application/json"},
            data=login_payload,
        )

        self.assertEqual(response.status_code, 404)
        self.assertNotEqual(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()