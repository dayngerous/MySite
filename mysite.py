from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html', title="Home")

@app.route("/music")
def music_discog():
    names = [{'text':'Dayngerous'}, {'text':'Backseat'}, {'text':'Fight Night'},{'text':'Peace'},
    {'text':'Peace'}, {'text':'Peace'}, {'text':'Peace'}, {'text':'Peace'}]
    return render_template('music.html', title="Music Discog", names=names)

if __name__ == '__main__':
    app.run(debug=True)
