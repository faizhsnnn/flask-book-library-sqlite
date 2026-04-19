from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String, Float, Integer

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(200), nullable=False)
    rating: Mapped[Float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    books = db.session.execute(db.select(Book)).scalars().all()
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        try:
            rating = float(request.form["rating"])
        except ValueError:
            return "Rating must be a number"

        if rating < 0 or rating > 10:
            return "Rating must be between 0 and 10"
        
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

