# Создать веб-приложение на FastAPI, которое будет предоставлять API для работы с базой данных пользователей.
# Пользователь должен иметь следующие поля:
# ○ ID (автоматически генерируется при создании пользователя)
# ○ Имя (строка, не менее 2 символов)
# ○ Фамилия (строка, не менее 2 символов)
# ○ Дата рождения (строка в формате "YYYY-MM-DD")
# ○ Email (строка, валидный email)
# ○ Адрес (строка, не менее 5 символов)
# API должен поддерживать следующие операции:
# ○ Добавление пользователя в базу данных
# ○ Получение списка всех пользователей в базе данных
# ○ Получение пользователя по ID
# ○ Обновление пользователя по ID
# ○ Удаление пользователя по ID
#  Приложение должно использовать базу данных SQLite3 для хранения пользователей.
import datetime
import typing

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from typing import List
from datetime import date

DATABASE_URL = "sqlite:///mydatabase3.db"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("name", sqlalchemy.String(50)),
    sqlalchemy.Column("lastname", sqlalchemy.String(50)),
    sqlalchemy.Column("birthday", sqlalchemy.String(10)),
    sqlalchemy.Column("email", sqlalchemy.String(50), unique=True),
    sqlalchemy.Column("address", sqlalchemy.String(50)),
)
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI()


class UserIn(BaseModel):
    name: str = Field(min_length=2)
    lastname: str = Field(min_length=2)
    birthday: date = Field()
    email: EmailStr = Field()
    address: str = Field(min_length=5)


class User(BaseModel):
    id: int
    name: str = Field(min_length=2)
    lastname: str = Field(min_length=2)
    birthday: date = Field()
    email: EmailStr = Field()
    address: str = Field(min_length=5)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
async def index():
    return 'Hi!'


@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(
            name=f'name{i}',
            lastname=f'lastname{i}',
            birthday=f'{datetime.date.today()}',
            email=f'mail{i}@mail.ru',
            address=f'address{i}'
        )
        await database.execute(query)
    return {'message': f'{count} fake users create'}


@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    # query = users.insert().values(name=user.name, email=user.email)
    query = users.insert().values(**user.dict())
    last_record_id = await database.execute(query)
    return {**user.name, "id": last_record_id}


@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "id": user_id}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}
