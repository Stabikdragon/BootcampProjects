from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired
import requests

URL_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
API_KEY = "4fe14549d330e22c5495f5c6861a7374"
API_READ_ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ZmUxNDU0OWQzMzBlMjJjNTQ5NWY1YzY4NjFhNzM3NCIsInN1YiI6IjY1MTkzZDA2MDcyMTY2MDBjNTY3MDlhMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wmpSm8h62lFKAqFoHTR0yWvZR1_mx6NA2e1xKAWfXu4'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Top-Movies.db"
Bootstrap5(app)

HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ZmUxNDU0OWQzMzBlMjJjNTQ5NWY1YzY4NjFhNzM3NCIsInN1YiI6IjY1MTkzZDA2MDcyMTY2MDBjNTY3MDlhMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.wmpSm8h62lFKAqFoHTR0yWvZR1_mx6NA2e1xKAWfXu4"
}


class MyForm(FlaskForm):
    new_rating = StringField(label='New rating - from 1-10')
    new_review = StringField(label='Your review')
    done = SubmitField(label='Done')


class AddForm(FlaskForm):
    new_movie = StringField(label='Movie Title')
    add_movie_button = SubmitField(label='Add Movie')


class Base(DeclarativeBase):
    pass


db = SQLAlchemy()


class Movie(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(db.String, unique=True )
    year: Mapped[int] = mapped_column(db.Integer, nullable=True)
    description: Mapped[str] = mapped_column(db.String, nullable=True )
    rating: Mapped[float] = mapped_column(db.Float , nullable=True)
    ranking: Mapped[int] = mapped_column(db.Integer , nullable=True)
    review: Mapped[str] = mapped_column(db.String , nullable=True)
    img_url: Mapped[str] = mapped_column(db.String , nullable=True)


db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", all_movies=all_movies)


@app.route('/edit', methods=("GET", "POST"))
def edit():
    form = MyForm()
    movie_id = request.args.get('id')
    movie_info = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        update_rating = form.new_rating.data
        update_review = form.new_review.data
        movie_info.rating = update_rating
        movie_info.review = update_review
        db.session.commit()
        return redirect('/')

    return render_template('edit.html', movie=movie_info, form=form)


@app.route('/delete', methods=("POST", "GET"))
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect('/')


@app.route('/add', methods=("GET", "POST"))
def add():
    form = AddForm()
    new_movie_title = form.new_movie.data
    params = {
        'query': f'{new_movie_title}',
    }
    response = requests.get(URL_ENDPOINT, headers=HEADERS, params=params)
    movie_db_results = response.json()['results']
    if form.validate_on_submit():
        print(movie_db_results)
        return render_template('select.html', movie=movie_db_results)
    return render_template("add.html", form=form)


@app.route('/add_to_database', methods=("POST", "GET"))
def add_to_database():
    URL_ID_ENDPOINT = "https://api.themoviedb.org/3/movie/"
    id_to_search = request.args.get('id')
    response = requests.get(f'{URL_ID_ENDPOINT}{id_to_search}', headers=HEADERS).json()
    new_movie = Movie(id=response["id"], title=response["title"],
                      img_url=f'https://image.tmdb.org/t/p/original{response["poster_path"]}',
                      year=response["release_date"][:4], description=response["overview"])
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for('edit',  id=id_to_search))



if __name__ == '__main__':
    app.run(debug=True)
