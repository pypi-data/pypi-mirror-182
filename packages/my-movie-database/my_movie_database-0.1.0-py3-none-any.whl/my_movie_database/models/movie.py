from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# Defines the Movie class relationally mapped to an SQL table.
class Movie(Base):
    __tablename__ = "movies"

    id = Column("id", Integer, Sequence("movie_id_seq"), primary_key=True)
    title = Column("title", String)
    year = Column("year", Integer)
    director = Column("director", String)
    rating = Column("rating", Integer)

    def __init__(self, title, year, director, rating):
        self.title = title
        self.year = year
        self.director = director
        self.rating = rating
