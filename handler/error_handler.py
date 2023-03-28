from starter import app
from exception  import  BussinessException 
from flask import jsonify,session,request
from util import JsonUtil
from dto import Result 

@app.errorhandler(BussinessException)
def handle_bussiness(error):
    response = jsonify(error.to_dict())
    #response.status_code = error.error_code
    #error.error_code
    return response

 

@app.errorhandler(Exception)
def handle_exception(error):
    app.logger.error(error,exc_info=True, stack_info=True)
    message=str(error)
    message="操作异常" if len(message) > 50 else message
    response = jsonify(JsonUtil.class2dic_no_none(Result.fail(500,str(error)))) 
    #response.status_code = 500
    #error.error_code
    return response
  
 