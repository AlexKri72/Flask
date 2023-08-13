# Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# 📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
# 📌 Создайте класс Movie с полями id, title, description и genre.
# 📌 Создайте список movies для хранения фильмов.
# 📌 Создайте маршрут для получения списка фильмов по жанру (метод GET).
# 📌 Реализуйте валидацию данных запроса и ответа.


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str


movies = []
for i in range(1, 11):
    movies.append(Movie(
        id=i,
        title=f'title{i}',
        description=f'description{i}',
        genre=f'genre{i}')
    )


@app.get('/')
async def index():
    return 'Hi!'


@app.get('/movies/')
async def get_all_movies():
    return movies


@app.get('/movies/{genre}', response_model=List[Movie])
async def get_movies(genre):
    film_genre = []
    for i in movies:
        if i.genre == genre:
            film_genre.append(i)
    if film_genre:
        return film_genre
    return HTTPException(status_code=404, detail='This genre is not found!')
