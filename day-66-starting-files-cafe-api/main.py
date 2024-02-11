from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random






TOP_SECRET_API_KEY = "123456789"

app = Flask(__name__)
app.json.sort_keys = False
##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random')
def random_cafe():
    random_cafe = random.choice(db.session.execute(db.select(Cafe)).scalars().all())
    print(random_cafe)
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all')
def all_cafes():
    results = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    all_dict = [item.to_dict() for item in results]
    return jsonify(cafes=all_dict)


@app.route('/search')
def search_cafe():
    search_word = request.args.get('loc')
    results = db.session.execute(db.select(Cafe).where(Cafe.location == search_word)).scalars().all()
    all_dict = [item.to_dict() for item in results]
    if results:
        return jsonify(cafes=all_dict)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

    print(search_word)
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=bool(request.form.get("loc")),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_cafe_price(cafe_id):
    cafe=db.get_or_404(Cafe, cafe_id)
    cafe.coffee_price = request.form.get("coffee_price")
    db.session.commit()
    print(cafe.id)
    return jsonify(cafe=cafe.to_dict())


## HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>')
def delete_cafe(cafe_id):
    api_key = "TopSecretAPIKey"
    if request.args.get('api-key') == api_key:

        cafe=db.get_or_404(Cafe, cafe_id)
        print(cafe.name)
        db.session.delete(cafe)
        db.session.commit()
        return redirect('/')
    else:
        return jsonify(error = "403: not found")


if __name__ == '__main__':
    app.run(debug=True)
