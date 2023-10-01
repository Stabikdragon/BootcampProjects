from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def info():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        return name


if __name__ == "__main__":
    app.run(debug=True)