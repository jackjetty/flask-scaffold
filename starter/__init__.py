import os
import bcrypt
import yaml
import logging
from logging.config import fileConfig, dictConfig
from datetime import date, datetime
from flask import Flask , Response , jsonify
from flask.json import JSONEncoder
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import (JWTManager)
from flask_bcrypt import Bcrypt
from flask_apscheduler import APScheduler 
from config.setting import configs 
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__,template_folder='../template')
# db init
db = SQLAlchemy()
# encrypt init
bcrypt = Bcrypt()
# cross origin request
cors = CORS()
# apscheduler
scheduler=APScheduler()
# json web token support
jwt = JWTManager()
# logger config
logger = app.logger
class JSONResponse(Response):
    @classmethod
    def force_type(cls,rv,environ=None):
        if isinstance(cls,rv,environ=None):
            if isinstance(rv,dict):
                rv=jsonify(rv)
            return super(JSONResponse,cls).force_tye(rv,environ)


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, (date, datetime)):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


def create_app(profile=None):
    logger.info("***create app**")
    load_dotenv(find_dotenv(), verbose=True)
    profile = os.environ.get('FLASK_PROFILE_ACTIVE', 'dev') if profile is None else profile
    app.config.from_object(configs[profile])
    log_file_path = app.config['LOG_FILE']
    log_config = os.path.abspath(log_file_path)
    with open(log_config) as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    #app.response_class=JSONResponse
    app.config['JSON_AS_ASCII'] = False
    app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    scheduler.init_app(app)
    scheduler.start()
    #app.json_encoder = CustomJSONEncoder
    cors.init_app(app, resources={r"/api/v1/*": {"origins": "*"}})
    from api import api_v1
    app.register_blueprint(api_v1)
    return app

app = create_app()
