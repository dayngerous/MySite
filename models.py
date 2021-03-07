import datetime as dt

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ifugbxrsglfgxk:0138a2c1e6ce6a504b323be66555d49eb6d7fe39aad717a09d57255771fa1a97@ec2-54-166-242-77.compute-1.amazonaws.com:5432/d8ci38lfi0klnu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


class Song(db.Model):
    __tablename__='songs'
    song_id = db.Column(db.Integer, primary_key=True)
    song_title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    producer = db.Column(db.String, nullable=True)
    mix_eng = db.Column(db.String, nullable=True)
    year = db.Column(db.String, nullable=False)

class Article(db.Model):
    __tablename__='articles'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String, default="Dayne Guy", nullable=False)
    blog_title = db.Column(db.String, nullable=False)
    article = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=True)
    date_published =  db.Column(db.DateTime, nullable=False, default=dt.datetime.now())


db.create_all()
#
# freak = Song(song_title='Freak', artist='Terrel', description='Song by TC Vision pioneer', mix_eng='Dayngerous', year=2021 )
# db.session.add(freak)
# db.session.commit()
