from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'postgres://ifugbxrsglfgxk:0138a2c1e6ce6a504b323be66555d49eb6d7fe39aad717a09d57255771fa1a97@ec2-54-166-242-77.compute-1.amazonaws.com:5432/d8ci3'

db = SQLAlchemy(app)

class songs(db.Model):
    id = db.Column('song_id', db.Integer, primary_key = True)
    song_title = db.Column(db.String(50), nullable=False)
    artist = db.Column(db.String(100))
    description = db.Column(db.String(500))
    producer = db.Column(db.String(100), default=None)
    mix_eng = db.Column(db.String(100))
    year = db.Column(db.DateTime)

    def __init__(self, song_title, artist, descriprion, producer, mix_eng,year):
        self.song_title = song_title
        self.artist = artist
        self.description = descriprion
        self.producer = producer
        self.mix_eng = mix_eng
        self.year = year



db.create_all()
