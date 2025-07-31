import pymysql
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def get_connection():
    return pymysql.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB,
    )
          
from models.user_auth_model import User
   


import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))




