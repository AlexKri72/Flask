# Создать API для удаления информации о пользователе из базы данных.
# Приложение должно иметь возможность принимать DELETE запросы и удалять информацию о пользователе из базы данных.
# 📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
# 📌 Создайте класс User с полями id, name, email и password.
# 📌 Создайте список users для хранения пользователей.
# 📌 Создайте маршрут для удаления информации о пользователе (метод DELETE).
# 📌 Реализуйте проверку наличия пользователя в списке и удаление его из списка.


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

@app.put('/users/',response_model=User)
async def update_users(user_id:int, user: User):
    for i in range(len(users)):
        if users[i].id==user_id:
            user.id=user_id
            users[i]=user
            return user
    raise HTTPException( status_code=404,detail='This user is not found')


@app.delete('/users/{user_id}')
async def delete_user(user_id:int):
    for i in range(len(users)):
        if users[i].id==user_id:
            del users[i]
            return {'This user delete'}
    raise HTTPException( status_code=404,detail='This user is not found')
