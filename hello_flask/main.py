from flask import Flask

app = Flask(__name__)




def make_bold(function):
    def bold():
        return f'<b>{function()}</b>'
    return bold
def make_italic(function):
    def italic():
        return f'<em>{function()}</em>'
    return italic

def make_underlined(function):
    def underline():
        return f'<u>{function()}</u>'
    return underline



@app.route('/')
@make_bold
@make_italic
@make_underlined
def hello_world():
    return '<h1>Hello, World!</h1>'


if __name__ == "__main__":
    app.run(debug=True)

