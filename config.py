

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD ="your_password"
MYSQL_DB = "studentdb"

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
