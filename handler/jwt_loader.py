from util import JsonUtil
from dto import Result
from flask import jsonify,session,request
from starter import jwt,logger
from storage import LocalStorage
#无效令牌
@jwt.invalid_token_loader
def invalid_token_callback(reason):

    response = jsonify(JsonUtil.class2dic_no_none(Result.fail(401,reason))) 
    response.status_code = 401
    return response


@jwt.expired_token_loader
def invalid_token_callback(jwt_header,jwt_data):

    response = jsonify(JsonUtil.class2dic_no_none(Result.fail(401,'token 过期,请重新登录'))) 
    response.status_code = 401
    return response



#token 失效了的token
@jwt.revoked_token_loader
def revoked_token_callback(jwt_header,jwt_data):

    response = jsonify(JsonUtil.class2dic_no_none(Result.fail(401,'失效token'))) 
    response.status_code = 401
    return response

#token 验证失败
@jwt.token_verification_failed_loader
def token_verification_failed_callback(jwt_header,jwt_data):

    response = jsonify(JsonUtil.class2dic_no_none(Result.fail(401,'传递的token不正确'))) 
    response.status_code = 401
    return response

#未认证
@jwt.unauthorized_loader
def unauthorized_callback(callback):
    response = jsonify(JsonUtil.class2dic_no_none(Result.fail(401,str(callback)))) 
    response.status_code = 401
    return response


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_header, decrypted_token):
    jti = decrypted_token['jti']
    #BLACKLIST
    return decrypted_token['jti'] in LocalStorage.getJwtBlackJtis()


