import datetime

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# Connect to CkEditor
ckeditor = CKEditor(app)


class PostForm(FlaskForm):
    title = StringField('Blog Post Title')
    subtitle = StringField('Subtitle')
    your_name = StringField('Your Name')
    blog_img_url = StringField('Blog Image URL')
    body = CKEditorField('Blog Content')
    submit = SubmitField('Submit')


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/<post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    print(requested_post.title)
    return render_template("post.html", post=requested_post)


@app.route('/new-post', methods=("POST", "GET"))
def add_new_post():
    form = PostForm()
    if form.validate_on_submit():
        new_blog_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            author=form.your_name.data,
            img_url=form.blog_img_url.data,
            body=form.body.data,
            date=datetime.date.today().strftime('%B %d, %Y')
        )
        db.session.add(new_blog_post)
        db.session.commit()
        return redirect('/')

    return render_template("make-post.html", form=form)


class CreatePostForm(PostForm):
    pass


@app.route('/edit-post/<post_id>', methods=("POST", "GET"))
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(title=post.title,
                               subtitle=post.subtitle,
                               img_url=post.img_url,
                               author=post.author,
                               body=post.body)
    if edit_form.validate_on_submit():
        post.title=edit_form.title.data
        post.subtitle=edit_form.subtitle.data
        post.author = edit_form.your_name.data
        post.img_url = edit_form.blog_img_url.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))

    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<post_id>")
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/')
#
# # TODO: delete_post() to remove a blog post from the database
#
# # Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
