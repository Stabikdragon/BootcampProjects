from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

class MyForm(FlaskForm):
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    email = StringField(label='Email',validators=[DataRequired(),Email() ])
    submit = SubmitField(label='Log in')


app = Flask(__name__)

bootstrap = Bootstrap(app)
app.secret_key = "some secret string"
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    return render_template('login.html', form=form)
    # if form.validate_on_submit():
    #     return render_template('success.html')
    #     print(form.email.data)
    # else:
    #     return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

