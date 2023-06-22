from flask import Flask, render_template

app = Flask(__name__)
import requests


@app.route('/guess/<name>')
def home(name):
    name = name.title()
    AGIFY_ENDPOINT = f"https://api.agify.io/?name={name}"
    GENDER_ENDPOINT = f"https://api.genderize.io?name={name}"

    agify_response = requests.get(url=AGIFY_ENDPOINT).json()["age"]
    gender_response = requests.get(url=GENDER_ENDPOINT).json()["gender"]
    return render_template("index.html", name=name, age=agify_response, gender=gender_response)


if __name__ == "__main__":
    app.run(debug=True)
