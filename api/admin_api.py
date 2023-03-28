from http import HTTPStatus
from flask import  jsonify,current_app,abort,request,g
from flask_restx import Api, Resource, fields,Namespace
from starter import app,  logger ,db 
from flask_jwt_extended import (
    jwt_required, create_access_token, create_refresh_token, get_jwt,
    get_jwt_identity
) 
import random
import flask_bcrypt
from util import JsonUtil,ListUtil
from constant import JWTConstant,DBConstant
from exception  import  BussinessException 
from dto import Result 
from model import  UserModel
from util.snowflake import IdWorker
admin_api = Namespace('admin', description='admin related operations')

add_user_parser = admin_api.parser()
add_user_parser.add_argument('account', type=str, required=True, help='account', location='json' )
add_user_parser.add_argument('password', type=str, required=True, help='password', location='json')
add_user_parser.add_argument('name', type=str, required=True, help='name', location='json')

add_user_result=admin_api.model("result",{
    "code": fields.Integer(required=True, description='',default=200),
    "message": fields.String(required=True, description='') ,
    "data":fields.String(required=True, description='') 
})



@admin_api.route('/user')
@admin_api.doc(description=' user' )   
class User(Resource):

    def __init__(self, api=admin_api):
        self.api = api

    @admin_api.doc(parser=add_user_parser,description='add user') 
    @admin_api.marshal_with(add_user_result)
    def post(self):
        g.transaction=1
        args = add_user_parser.parse_args(strict=True)
        account = args['account']
        password = args['password']
        name = args['name']
        userModel=UserModel.query.filter_by(account=account,state=DBConstant.STATE_ENABLE).first()
        #查询用户
        if userModel :
            raise BussinessException(error_code=401,message=' 用户账户{0}，已经存在'.format(account))    
        
        idWorker=IdWorker(1, 2, 0) 
        session =db.session
        userModel=UserModel() 
        userModel.id=idWorker.get_id()
        userModel.name=name
        userModel.account=account
        userModel.state=DBConstant.STATE_ENABLE
        userModel.password=flask_bcrypt.generate_password_hash(account+password)
        session.add(userModel)  
        result=Result.success(userModel.id)  
        return JsonUtil.class2dic_no_none(result)