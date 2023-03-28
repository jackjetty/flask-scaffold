from http import HTTPStatus
from flask import  jsonify,current_app,abort,request,g
from flask_restx import Api, Resource, fields,Namespace
from starter import app,  logger ,db 
from model import Mall
import random
mall_api = Namespace('mall', description='app mall related operations')
@mall_api.route('/<int:mall_id>')
@mall_api.doc(description='mall id info' )   
class DoMall(Resource):

    @mall_api.doc(description="mall id should be in avaliable " )
    def get(self, mall_id):
        """Fetch a given resource"""
        session=db.session
        mall=session.query(Mall).filter(Mall.id==mall_id).first()
        app.logger.info(request.method)
        g.setdefault('name',12)
        #g.name=random.randint(1,50)
        #request.args('X-RANOM')=
        #abort(404)
        if mall:
            return mall.name
        return mall_id