from extensions import db

class Database():
    def __init__(self):
        self.movie = self.Movie

    class Movie(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, unique=False, nullable=False)
        year = db.Column(db.String, unique=False, nullable=True)
        description = db.Column(db.String, unique=False, nullable=True)
        rating = db.Column(db.Float, unique=False, nullable=True)
        ranking = db.Column(db.Integer, unique=True, nullable=True)
        review = db.Column(db.String, unique=False, nullable=True)
        img_url = db.Column(db.String, unique=False, nullable=True)

    def add_movie(self, movie_data):

        new_movie = self.movie(
            title=movie_data['original_title'],
            year=movie_data['release_date'].split('-')[0],
            description=movie_data['overview'],
            rating=None,
            ranking=None,
            review="",
            img_url=f"https://image.tmdb.org/t/p/w500/{movie_data['poster_path']}",
        )
        db.session.add(new_movie)
        db.session.commit()

    def find_by_id(self, id):
        return self.movie.query.filter_by(id=id).first()

    def get_all_movies(self):
        # movies = db.session.query(self.Movie).all()
        movies = self.movie.query.order_by(self.movie.ranking).all()
        movie_data = []

        for x in movies:
            movie_data.append({
                "id": x.id,
                "title": x.title,
                "year": x.year,
                "description": x.description,
                "rating": x.rating,
                "ranking": x.ranking,
                "review": x.review,
                "img_url": x.img_url
            })
        return movie_data



    def update_movie(self, movie, data):
        # Handle possible illegal values to database
        if not movie.rating:
            movie.rating = 0.0
        if 0 > movie.rating > 10.0:
            movie.rating = 0.0
        if not movie.ranking:
            movie.ranking = 10
        if 0 > movie.ranking > 10:
            movie.ranking = 10

        movie.rating = data['rating']
        movie.ranking = data['ranking']
        movie.review = data['review']
        db.session.commit()

    def delete_movie(self, id):
        try:
            movie = self.find_by_id(id)
            db.session.delete(movie)
            db.session.commit()
        except:
            return False
        finally:
            return True




