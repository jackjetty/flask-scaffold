import os
from  datetime import  datetime, timedelta
from urllib.parse import quote_plus as urlquote

class Config:
    PROFILE = 'development'
    HOST = 'localhost'
    PORT = 10036
    LOG_FILE = ''
    DB_HOST =os.getenv("DB_HOST",'127.0.0.1')   
    DB_PORT =os.getenv("DB_PORT",3306)   
    DB_USERNAME =os.getenv("DB_USERNAME", 'root')   
    DB_PASSWORD = os.getenv("DB_PASSWORD", 'root')   
    DB_SCHEMA_NAME = os.getenv("DB_SCHEMA_NAME", 'customer_flow')    
    JWT_SECRET_KEY="C*F-JaNdRgUkXn2r5u8x/A?D(G+KbPeShVmYq3s6v9y$B&E)H@McQfTjWnZr4pmt"
    JWT_HEADER_NAME="Authorization"
    JWT_HEADER_TYPE = 'Bearer'
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
    JWT_ACCESS_TOKEN_EXPIRES= timedelta(seconds=60*60*8)
    JWT_ENCODE_ISSUER="Swire CAS"
    JWT_ALGORITHM = 'HS256'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8'.format(
        DB_USERNAME, urlquote(DB_PASSWORD), urlquote(DB_HOST), DB_PORT, DB_SCHEMA_NAME)


class DevConfig(Config):
    DEBUG = True
    PROFILE = 'dev'
    HOST = '0.0.0.0'
    LOG_FILE = './logging.yaml'
    #MAIL_TEMPLATE_PATH="./template/render.html" 


class TestConfig(Config):
    DEBUG = True
    PROFILE = 'test'
    HOST = '0.0.0.0'
    LOG_FILE = './logging.yaml'
    
class ProdConfig(Config):
    DEBUG = False
    PROFILE = 'prod'
    PORT=10024
    HOST = '0.0.0.0'
    LOG_FILE = './logging.yaml'


configs = dict(
    dev=DevConfig(),
    test=TestConfig(),
    prod=ProdConfig() 
)

