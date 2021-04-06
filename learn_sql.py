from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql
from flask_cors import *  # 导入模块

app = Flask(__name__)  # type:Flask
CORS(app, supports_credentials=True)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@106.53.133.58:3306/sun"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+"G://abc.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRETE_KEY"] = "xxx"
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    content = db.Column(db.String(100000))
    result = db.Column(db.String(64))

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

# class Student(db.Model):
#     __tablename__ = "student"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), nullable=False)
#     gender = db.Column(db.Enum("男", "女"), nullable=False)
#     phone = db.Column(db.String(11),unique=True)
#
#
# class Course(db.Model):
#     __tablename__ = "course"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), nullable=False)
#
#
# class Teacher(db.Model):
#     __tablename__ = "teacher"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), nullable=False)
#     gender = db.Column(db.Enum("男", "女"), nullable=False)
#     phone = db.Column(db.String(11), unique=True)
#
#
# class Grade(db.Model):
#     __tablename__ = "grade"
#     id = db.Column(db.Integer, primary_key=True)



if __name__ == '__main__':
    db.create_all()