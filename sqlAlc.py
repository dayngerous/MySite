from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from models import Song

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ifugbxrsglfgxk:0138a2c1e6ce6a504b323be66555d49eb6d7fe39aad717a09d57255771fa1a97@ec2-54-166-242-77.compute-1.amazonaws.com:5432/d8ci38lfi0klnu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)


freak = Song(song_title='Freak', artist='Terrel Cadle', description='Song by TC Vision pioneer', mix_eng='Dayngerous', year=2021 )
db.session.add(freak)
db.session.commit()

# table.query.all() select * from __tablename__
#
# table.query.filter_by(column='').all
