from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from wtforms import StringField, SubmitField

# from wtforms.validators import DataRequired
import requests

URL_ENDPOINT="https://api.themoviedb.org/3/authentication"
API_KEY = "4fe14549d330e22c5495f5c6861a7374"
API_READ_ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ZmUxNDU0OWQzMzBlMjJjNTQ5NWY1YzY4NjFhNzM3NCIsInN1YiI6IjY1MTkzZDA2MDcyMTY2MDBjNTY3MDlhMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wmpSm8h62lFKAqFoHTR0yWvZR1_mx6NA2e1xKAWfXu4'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Top-Movies.db"
Bootstrap5(app)


headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ZmUxNDU0OWQzMzBlMjJjNTQ5NWY1YzY4NjFhNzM3NCIsInN1YiI6IjY1MTkzZDA2MDcyMTY2MDBjNTY3MDlhMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wmpSm8h62lFKAqFoHTR0yWvZR1_mx6NA2e1xKAWfXu4"
}

response = requests.get(URL_ENDPOINT, headers=headers)

print(response.text)
class MyForm(FlaskForm):
    new_rating = StringField(label='New rating - from 1-10')
    new_review = StringField(label='Your review')
    done = SubmitField(label='Done')
class AddForm(FlaskForm):
    new_movie = StringField(label='Movie Title')
    add_movie = SubmitField(label='Add Movie')


class Base(DeclarativeBase):
    pass


db = SQLAlchemy()


class Movie(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(db.Integer, nullable=False)
    description: Mapped[str] = mapped_column(db.String, nullable=False)
    rating: Mapped[float] = mapped_column(db.Float, nullable=False)
    ranking: Mapped[int] = mapped_column(db.Integer, nullable=False)
    review: Mapped[str] = mapped_column(db.String, nullable=False)
    img_url: Mapped[str] = mapped_column(db.String, nullable=False)


db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking))
    all_movies = result.scalars().all()
    return render_template("index.html", all_movies=all_movies)


@app.route('/edit', methods=("GET", "POST"))
def edit():
    form = MyForm()
    movie_id = request.args.get('id')
    movie_info = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        update_rating =form.new_rating.data
        update_review=form.new_review.data
        movie_info.rating=update_rating
        movie_info.review=update_review
        db.session.commit()
        return redirect('/')

    return render_template('edit.html', movie=movie_info, form=form)


@app.route('/delete', methods=("POST", "GET"))
def delete():
    movie_id=request.args.get('id')
    movie_to_delete = db.get_or_404(Movie,movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect('/')


@app.route('/add')
def add():
    return render_template("add.html")


if __name__ == '__main__':
    app.run(debug=True)
