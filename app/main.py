# !/usr/bin/env python
# Fast API first app!
from fastapi import FastAPI, Request, Form, Body



# Create an instance of Fast API
app = FastAPI()
app.title = "Movies API!"
app.version = "v0.0.1"

# Movies dict list
movies_list = movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'
    },
    {
        'id': 2,
        'title': 'Super Mario Bros',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Terror'
    },
    {
        'id': 3,
        'title': 'Suzume',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Drama'
    }
]

API_ENDPOINTS = {
    
}

# Create our first endpoint
@app.get('/', tags=["Home"])
def message():
    """
    Just print a custom message.
    :return: message dict.
    """
    return {
        "message": "Hello Norber, this the real world -the matrix-!"
    }

@app.get("/movies", tags=["Movies List"])
def list_movies():
    """
    The list of movies to return.
    :return:
    """
    return movies_list

@app.get("/movies/{id}", tags=["Movies List"])
def list_endpoint_id(id: int):
    """
    Returns the movie info from the
    given id.
    :param id: The movie id requested.
    :return:
    """
    no_item_msg = (
        "No item available for the requested id: {id}"
    )
    movie_title = [ movie.get("title") for movie in movies_list if movie.get("id") == id ]
    if not movie_title:
        return no_item_msg.replace("{id}", str(id))
    return {
        "id": id,
        "title": f"The selected movie is: {movie_title[0]!r}"
    }

@app.get("/movies/", tags=["Movies List"])
def category_filter(category: str, year: int):
    """
    Filters per category given a category
    string query parameter.

    :param category: A string category name.
    :return: A string message with the movie
        category selected.
    """
    no_category_msg = (
        "There's no category called '{category}'"
    )
    movie_category = [ movie.get("title") for movie in movies_list if movie.get("category") == category]
    if not movie_category:
        return no_category_msg.replace("{category}", category)
    return f"{movie_category[0]!r}"

@app.post("/movies", tags=["Movies List"])
def add_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: str = Body(), rating: int = Body(), category: str = Body()):
    """
    
    :param id: 
    :param title: 
    :param overview: 
    :param year: 
    :param rating: 
    :param category: 
    :return: 
    """
    new_movie = {
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category,
    }
    movies_list.append(new_movie)
    return movies_list
    