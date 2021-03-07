import os
import datetime as dt

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

from models import Song, Article

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ifugbxrsglfgxk:0138a2c1e6ce6a504b323be66555d49eb6d7fe39aad717a09d57255771fa1a97@ec2-54-166-242-77.compute-1.amazonaws.com:5432/d8ci38lfi0klnu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
#
# from flask import Flask, render_template, url_for, request
# app = Flask(__name__)
#
# engine = create_engine('postgres://ifugbxrsglfgxk:0138a2c1e6ce6a504b323be66555d49eb6d7fe39aad717a09d57255771fa1a97@ec2-54-166-242-77.compute-1.amazonaws.com:5432/d8ci38lfi0klnu')
# #If not online add os.getenv into create_engine
# db = scoped_session(sessionmaker(bind=engine))

mixed=False
songs=False
prods=False

@app.route("/")
def home():
    return render_template('home.html', title="Home")

##################################################################################################################
@app.route('/music/')
def music():
    # Songs =  db.execute("SELECT song_title, artist, year FROM songs WHERE mix_eng = 'Dayngerous' ORDER BY year DESC").fetchall()
    Songs = Song.query.order_by(Song.year.desc()).all()
        #print(f'{mix.song_title}')
    return  render_template('music.html', names=Songs, items=True, title="Music Discog")

@app.route("/music/mixes")
def mixed_by_me():
    # myMixes =  db.execute("SELECT song_title, artist, year FROM songs WHERE mix_eng = 'Dayngerous' ORDER BY year DESC").fetchall()
    myMixes = Song.query.filter_by(mix_eng="Dayngerous").order_by(Song.year.desc()).all()
    if not myMixes:
        return render_template('music.html', message = "You have no Mixes", items=False, mixed=True)
    else:
        return  render_template('music.html', names=myMixes, items=True, title="Music Discog", mixed=True)

@app.route("/music/songs")
def songs_by_me():
    # mySongs =  db.execute("SELECT song_title, artist, year FROM songs WHERE artist = 'Dayngerous' ORDER BY year DESC").fetchall()
    mySongs = Song.query.filter_by(artist="Dayngerous").order_by(Song.year.desc()).all()
    if not mySongs:
        return render_template('music.html', message = "You have no Songs", items=False, title="Music Discog",  songs=True)
    else:
        return  render_template('music.html', names = mySongs, items=True, title="Music Discog", songs=True)

@app.route("/music/prods")
def prod_by_me():
    # myProds =  db.execute("SELECT song_title, artist, year FROM songs WHERE producer = 'Dayngerous' ORDER BY year DESC").fetchall()
    myProds = Song.query.filter_by(producer="Dayngerous").order_by(Song.year.desc()).all()
    if not myProds:
        return render_template('music.html', message = "You have no Productions", items=False, title="Music Discog", prods=True)
    else:
        return  render_template('music.html', names = myProds, items=True, title="Music Discog", prods=True)

###########################################################################################################################

@app.route("/edu/")
def edu():
    return render_template('home.html', title="Education")

############################################################################################################################
@app.route("/code/")
def coding():
    return redirect(url_for('home'))

############################################################################################################################

@app.route("/blog/")
def blog():
    blogs = Article.query.order_by(Article.date_published.desc()).all()
    return render_template('blogs/blog.html', blogs=blogs, title="Blog")

#############################################################################################################################

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    return render_template('blog.html', name=name)

@app.route('/post', methods=['POST'])
def post():
    blog_title = request.form.get('Title')
    img_url = request.form.get('img-url')
    article = request.form.get('article')
    blog_post= Article(blog_title=blog_title, img_url=img_url, article=article )
    db.session.add(blog_post)
    db.session.commit()
    return redirect(url_for('blog'))

@app.route('/author')
def author():
    return render_template('author.html', title="Create a New Article")

if __name__ == '__main__':
    app.run(debug=True)
