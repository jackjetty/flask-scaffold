from starter import app,logger,db
import time
import hmac
import hashlib
import os
from flask import Flask, Blueprint,g
from flask_restx import Api, Resource, fields
from api.auth_api import auth_api as auth_ns
from api.admin_api import admin_api as admin_ns
import random
authorizations = {
    'jwt': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api_v1 = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(
    api_v1,
    version="1.0",
    title="flask scaffold API",
    description="A simple demo API",
)

api.add_namespace(auth_ns)
api.add_namespace(admin_ns) 
#@api_v1.before_request
    

@app.teardown_appcontext
def teardown(exc = None):
    #如果使用了事务
    if g.get('transaction',0)==1: 
        if exc is None:
            db.session.commit()
        else:
            db.session.rollback()
        db.session.remove()
    #db.close()