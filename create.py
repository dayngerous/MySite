import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ifugbxrsglfgxk:0138a2c1e6ce6a504b323be66555d49eb6d7fe39aad717a09d57255771fa1a97@ec2-54-166-242-77.compute-1.amazonaws.com:5432/d8ci38lfi0klnu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def main():
    db.create_all()


if __name__ == "__main__":
    with app.app_context():
        main()
