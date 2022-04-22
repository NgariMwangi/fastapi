import unittest
import json
# from main import app
# from configs import configs
from configs import configs
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI,status,Response,HTTPException
import models, schemas, models, database
# from configs.configs import engine
from main import app
from fastapi.testclient import TestClient
# app.config.from_object(TestingConfig)
# def get_db():
#     db=SessionLocal() 
#     try:
#         yield db
#     finally:
#         db.close()



class Skeleton_test(unittest.TestCase):
    # """This is a skeleton for all all tests"""
    def setUp(self):
        self.app = TestClient(app)

    def tearDown(self,db:Session=Depends(configs.get_db)):
        # """teardown method deletes all record after test is run"""
        # db.session.remove()
        models.Base.metadata.create_all(configs.engine)
        models.Base.metadata.drop_all(configs.engine)
