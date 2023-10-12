from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "My First API"
app.version = "0.0.1"

movies = [
    {
        "id": 1,
        "title": "The Godfather",
        "director": "Francis Ford Coppola",
        "overview": "Spanning the years 1945 to 1955, a chronicle of the fictional Italian-American Corleone crime family.",
        "year": 1972,
        "rating": 9.2,
        "category": "Crime, Drama",
    },
    {
        "id": 2,
        "title": "The Shawshank Redemption",
        "director": "Frank Darabont",
        "overview": "Tests",
        "year": 1994,
        "rating": 9.3,
        "category": "Drama",
    }
]

@app.get("/", tags=["home "])
def message():
    return HTMLResponse('<h1> Welcome to my first API </h1>')

@app.get('/movies', tags=["movies"])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=["movies"])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []

@app.get('/movies/', tags=["movies"])
def get_movies_by_category(category: str):
    for item in movies:
        if item["category"] == category:
            return item
    return []

@app.post('/movies', tags=["movies"])
def create_movie(id: int = Body(), title: str= Body(), director: str= Body(), overview: str= Body(), year: int= Body(), rating: float= Body(), category: str= Body()):
    movies.append({
        "id": id,
        "title": title,
        "director": director,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category,
    })
    return movies

@app.put('/movies/{id}', tags=["movies"])
def update_movie(id: int, title: str= Body(), director: str= Body(), overview: str= Body(), year: int= Body(), rating: float= Body(), category: str= Body()):
    for item in movies:
        if item["id"] == id:
            item["title"] = title
            item["director"] = director
            item["overview"] = overview
            item["year"] = year
            item["rating"] = rating
            item["category"] = category
            return item
    return movies

@app.delete('/movies/{id}', tags=["movies"])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
    return movies
