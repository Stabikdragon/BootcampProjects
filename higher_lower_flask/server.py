from flask import Flask
import random

app = Flask(__name__)

num = random.randint(0, 9)
print(num)


@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://i.giphy.com/media/iB5aKC0dcRnK8/giphy.webp"</img>'


@app.route('/<int:number>')
def yay(number):
    if number < num:
        return "Too low!"
    elif number > num:
        return "Too high!"
    else:
        return "you got it!"

if __name__ == "__main__":
    app.run(debug=True)
