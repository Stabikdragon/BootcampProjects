# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass

app = Flask(__name__)

db = SQLAlchemy(model_class=Base)


class Book(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(db.String,  nullable=True)
    author: Mapped[str] = mapped_column(db.String, nullable=False)
    rating: Mapped[float] = mapped_column(db.Float, nullable=False)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db.init_app(app)

with app.app_context():
    db.create_all()

with app.app_context():
    new_book = Book( title="Hotte", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()