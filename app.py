from flask import Flask, render_template, request, redirect, url_for, render_template_string
from extensions import db
from database import Database
from forms import UpdateForm, AddForm
from apis.tmdb import TheMovieDatabase
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['WTForms_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movie-database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database = Database()
db.init_app(app)
# The above order is important and the line below inits the database
# db.create_all(app=app)

the_movie_database = TheMovieDatabase()


@app.route('/')
def index():
    all_movies = database.get_all_movies()
    return render_template('index.html', movies=all_movies)

@app.route('/add_movie', methods=["GET", "POST"])
def add_movie():
    add_form = AddForm()
    if request.method == "GET":
        return render_template('add.html', form=add_form)
    if request.method == "POST":
        title = request.form['title']
        year = request.form['year']
        search_data = the_movie_database.search_for_movie(title, year=year)
        return render_template('add.html', form=add_form, modal=True, search_data=search_data)

@app.route('/add_movie/<index>')
def add_movie_to_list(index):
    movie_info = the_movie_database.search_data[int(index)]
    database.add_movie(movie_info)
    return redirect('/')

@app.route('/delete/<id>')
def delete_movie(id):
    database.delete_movie(id)
    return redirect(url_for('index'))

@app.route('/update/<id>', methods=["GET", "POST"])
def update(id):
    movie = database.find_by_id(id)
    if request.method == "GET":
        update_form = UpdateForm()
        update_form.rating.render_kw = {"value": movie.rating}
        update_form.ranking.render_kw= {"value": movie.ranking}
        update_form.review.data = movie.review
        return render_template("update.html", movie=movie, form=update_form)
    # Compare and update changes
    if request.method == "POST":
        database.update_movie(movie=movie, data=request.form)

        return redirect('/')

if __name__ == "__main__":
    app.run()
