from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


app = Flask(__name__)

db = SQLAlchemy()


class Book(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(db.String, nullable=False)
    author: Mapped[str] = mapped_column(db.String, nullable=False)
    rating: Mapped[float] = mapped_column(db.Float, nullable=False)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.id))
    all_books = result.scalars().all()
    if not all_books:
        return "<p>Library is empty.</p> <a href=add> Add New BOOk </a>"
    else:
        return render_template('index.html', all_books=all_books)


@app.route("/add", methods=("POST", "GET"))
def add():
    form_data = request.form.to_dict()
    title = form_data.get('title')
    author = form_data.get('author')
    rating = form_data.get('rating')
    if request.method == "POST":
        with app.app_context():
            new_book = Book(title=title, author=author, rating=rating)
            db.session.add(new_book)
            db.session.commit()
        return redirect('/')
    return render_template('add.html')


@app.route("/edit", methods=("POST", "GET"))
def edit():
    book_id = request.args.get('id')
    book_info = db.get_or_404(Book, book_id)
    if request.method == "POST":
        book_update = db.get_or_404(Book, book_id)
        book_update.rating = request.form.get('rating')
        db.session.commit()
        return redirect('/')
# asdf

    print(book_id)
    print(book_info.author)
    return render_template('edit_rating.html', item=book_info)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_info = db.get_or_404(Book, book_id)
    db.session.delete(book_info)
    db.session.commit()
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)
