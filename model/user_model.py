from turtle import update
from starter import db
from model import BaseModel
from datetime import datetime
class UserModel(BaseModel):

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    account = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(100), nullable=True)
    state = db.Column(db.Integer, nullable=True)
    create_time = db.Column(db.DateTime, nullable=True, default=datetime.now)
    update_time = db.Column(db.DateTime, nullable=True,onupdate=datetime.now)