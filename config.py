import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://root:123456@localhost/product_python')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
