from http import HTTPStatus
from flask import  jsonify,current_app,abort,request,g
from flask_restx import Api, Resource, fields,Namespace
from starter import app,  logger ,db ,cache
from flask_jwt_extended import (
    jwt_required, create_access_token, create_refresh_token, get_jwt,
    get_jwt_identity
) 
import random
import flask_bcrypt
from util import JsonUtil,ListUtil
from constant import JWTConstant,DBConstant
from exception  import  BussinessException 
from dto import Result,  LoginVo ,UserInfoVo
from model import UserModel
from storage import LocalStorage
auth_api = Namespace('auth', description='authorization related operations')
login_parser = auth_api.parser()
login_parser.add_argument('account', type=str, required=True, help='account', location='json' )
login_parser.add_argument('password', type=str, required=True, help='password', location='json')
login_vo = auth_api.model(
    "LoginVo", {
        "userId": fields.String(required=True, description=''), 
        "userName": fields.String(required=True, description=''), 
        "accessToken": fields.String(required=True, description=''), 
        "account": fields.String(required=True, description='')}
)

login_result=auth_api.model("result",{
    "code": fields.Integer(required=True, description='',default=200),
    "message": fields.String(required=True, description='') ,
    "data":fields.Nested(login_vo, description="The Login Vo" ) 
})


logout_result=auth_api.model("result",{
    "code": fields.Integer(required=True, description='',default=200),
    "message": fields.String(required=True, description='') 
})

update_password_parser = auth_api.parser()
update_password_parser.add_argument('oldPassword', type=str, required=True, help='oldPassword', location='json' )
update_password_parser.add_argument('newPassword', type=str, required=True, help='newPassword', location='json')

update_password_result=auth_api.model("result",{
    "code": fields.Integer(required=True, description='',default=200),
    "message": fields.String(required=True, description='')
})


user_info_vo = auth_api.model(
    "UserInfoVo", {
        "userId": fields.String(required=True, description=''), 
        "userName": fields.String(required=True, description=''), 
        "account": fields.String(required=True, description='')}
)

user_info_result=auth_api.model("result",{
    "code": fields.Integer(required=True, description='',default=200),
    "message": fields.String(required=True, description='') ,
    "data":fields.Nested(user_info_vo, description="The User Vo" ) 
})



@auth_api.route('/login')
@auth_api.doc(description='login admin' )   
class AuthLogin(Resource):

    def __init__(self, api=auth_api):
        self.api = api

    @auth_api.doc(parser=login_parser,description='login auth',security='jwt') 
    @auth_api.marshal_with(login_result)
    def post(self):
        args = login_parser.parse_args(strict=True)
        account = args['account']
        password = args['password']
        userModel=UserModel.query.filter_by(account=account,state=DBConstant.STATE_ENABLE).first()
        #查询用户
        if not userModel :
            raise BussinessException(error_code=401,message=' 用户{0}，不存在或者已经失效'.format(account))
        if not flask_bcrypt.check_password_hash(userModel.password, account+password):
            raise BussinessException(error_code=401,message=' 账号或密码出错')     
        
        #logger.info("pmt admin users:%s",adminUserDtos)    
        additional_claims ={}
        additional_claims[JWTConstant.CLAIM_ROLE]=[]
        access_token = JWTConstant.TOKEN_PREFIX+create_access_token(identity=userModel.id,additional_claims=additional_claims)    
        refresh_token = JWTConstant.TOKEN_PREFIX+create_refresh_token(identity=userModel.id,additional_claims=additional_claims) 
        loginVo=LoginVo()
        loginVo.userId=userModel.id
        loginVo.userName=userModel.name
        loginVo.accessToken=access_token
        loginVo.account=userModel.account
        loginVo.roles=[]
        cache.set('user:{}'.format(userModel.id),{"topic": 
        {
            "key0":"value",
            "key1":
            [
                {"key3":1}
            ]
        }
    },timeout=1000)
        logger.info("user info: %s",cache.get('user:{}'.format(userModel.id)))
        result=Result.success(loginVo)
        #g.transaction=1
        return JsonUtil.class2dic_no_none(result)


@auth_api.route('/logout')
class AuthLogout(Resource):

    @jwt_required()
    @auth_api.doc(description='logout user',security='jwt')
    @auth_api.marshal_with(logout_result)
    def post(self):
        jwt = get_jwt()
        jti = get_jwt()['jti']
        LocalStorage.getJwtBlackJtis().append(jti)
        user_id = get_jwt_identity()
        # 操作数据库登出 日志 
        result=Result()
        return JsonUtil.class2dic_no_none(result)


        
@auth_api.route('/user/info')
class AuthUserInfo(Resource):

    @jwt_required()
    @auth_api.doc(description='current user info',security='jwt')
    @auth_api.marshal_with(user_info_result)
    def get(self):
        user_id = get_jwt_identity()
        userModel=UserModel.query.filter_by(id=user_id,state=DBConstant.STATE_ENABLE).first()
        if not userModel :
            raise BussinessException(error_code=401,message=' 当前用户，不存在或者已经失效')
        userInfoVo=UserInfoVo()    
        userInfoVo.userId=userModel.id
        userInfoVo.account=userModel.account
        userInfoVo.roles=[]
        userInfoVo.userName=userModel.name
        result=Result.success(userInfoVo)
        return JsonUtil.class2dic_no_none(result)



@auth_api.route('/password')
class AuthPassword(Resource):
    def __init__(self, api=auth_api):
        self.api = api

    @jwt_required()
    @auth_api.doc(parser=update_password_parser,description='update password',security='jwt' )
    @auth_api.marshal_with(update_password_result)
    def put(self):
        g.transaction=1
        args=update_password_parser.parse_args(strict=True)
        user_id = get_jwt_identity()
        old_password=args['oldPassword']
        new_password=args['newPassword']
        userModel=UserModel.query.filter_by(id=user_id,state=DBConstant.STATE_ENABLE).first()
        if not userModel :
            raise BussinessException(error_code=401,message=' 当前用户，不存在或者已经失效')
        account=userModel.account  
        if not flask_bcrypt.check_password_hash(userModel.password, account+old_password):
            raise BussinessException(error_code=500,message=' 原密码错误') 
        encode_password=flask_bcrypt.generate_password_hash(account+new_password) 
        userModel.password=encode_password
        result=Result()
        return JsonUtil.class2dic_no_none(result)          
         