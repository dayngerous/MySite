# import os
#
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
#
# engine = create_engine('postgres://ifugbxrsglfgxk:0138a2c1e6ce6a504b323be66555d49eb6d7fe39aad717a09d57255771fa1a97@ec2-54-166-242-77.compute-1.amazonaws.com:5432/d8ci38lfi0klnu')
# #If not online add os.getenv into create_engine
# db = scoped_session(sessionmaker(bind=engine))
import os
import csv

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ifugbxrsglfgxk:0138a2c1e6ce6a504b323be66555d49eb6d7fe39aad717a09d57255771fa1a97@ec2-54-166-242-77.compute-1.amazonaws.com:5432/d8ci38lfi0klnu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

filename = 'file.csv'
def main():
    f = open(filename)
    reader = csv.reader(f)
    for song_title, artist, description, producer, mix_eng, year in reader:
        song = Song(song_title=song_title, artist=artist, description=description, producer=producer, mix_eng=mix_eng, year=year )
        db.session.add(flight)
        # db.execute("INSERT INTO songs (song_title, artist, description, producer, mix_eng, year) VALUES (:song_title, :artist, :description, :producer, :mix_eng, :year)",
        #     {'song_title': song_title,'artist': artist,'description': description, 'producer': producer,'mix_eng': mix_eng, 'year': year})

        print(f'Added {song_title} from {artist} to songs database')
    # db.commit()
    db.session.commit()

if __name__ == "__main__":
    main()
