# Создать API для добавления нового пользователя в базу данных.
# Приложение должно иметь возможность принимать POST запросы с данными нового пользователя и сохранять их в базу данных.
# 📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
# 📌 Создайте класс User с полями id, name, email и password.
# 📌 Создайте список users для хранения пользователей.
# 📌 Создайте маршрут для добавления нового пользователя (метод POST).
# 📌 Реализуйте валидацию данных запроса и ответа.


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = []

for i in range(1, 11):
    users.append(User(
        id=i,
        name=f'name{i}',
        email=f'email{i}@mail.ru',
        password=f'password{i}')
    )


@app.get('/')
async def index():
    return 'Hi!'


@app.get('/users/')
async def get_all_users():
    return users


@app.get('/users/{user_id}', response_model=List[User])
async def get_user(user_id: int):
    for i in users:
        if i.id == user_id:
            return {'id':user_id,'name':i.name}
    return HTTPException(status_code=404, detail='This user is not found!')


@app.post('/users/',response_model=User)
async def create_user(user: User):
    user.id=len(users)+1
    users.append(user)
    return user