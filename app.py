from starter import app 
from handler import jwt_loader,error_handler
if __name__ == '__main__': 
    app.run(host=app.config.get('HOST','0.0.0.0') ,  port=app.config.get('PORT', 5000)) 