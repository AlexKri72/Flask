# Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# 📌 Создайте модуль приложения и настройте сервер и маршрутизацию.
# 📌 Создайте класс User с полями id, name, email и password.
# 📌 Создайте список users для хранения пользователей.
# 📌 Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# 📌 Создайте маршрут для отображения списка пользователей (метод GET).
# 📌 Реализуйте вывод списка пользователей через шаблонизатор Jinja.


from  fastapi import FastAPI,HTTPException,Request
from  pydantic import BaseModel
from  typing import List
from  fastapi.responses import HTMLResponse
from  fastapi.templating import Jinja2Templates


app= FastAPI()
templates=Jinja2Templates(directory='lesson05.templates')

class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str

tasks=[]
for i in range(10):
    tasks.append(Task(
        id=i,
        title=f'title{i}',
        description=f'description{i}',
        status=f'status{i}')
    )

@app.get('/',response_class=HTMLResponse)
async def read_tasks(request: Request):
    return templates.TemplateResponse('index.html',{'requests':request,'tasks':tasks})
@app.get('/tasks/',response_model=List[Task])
async def get_tasks():
    return tasks

@app.post('/tasks/',response_model=Task)
async def create_tasks(task: Task):
    task.id=len(tasks)+1
    tasks.append(task)
    return task


@app.put('/tasks/',response_model=Task)
async def update_tasks(task_id:int, task: Task):
    for i in range(len(tasks)):
        if tasks[i].id==task_id:
            task.id=task_id
            tasks[i]=task
            return task
    raise  HTTPException('Task not found')



@app.delete('/tasks/{task_id}')
async def update_tasks(task_id:int):
    for i in range(len(tasks)):
        if tasks[i].id==task_id:
            del tasks[i]
            return {'Task delete'}
    raise  HTTPException(status_code=404, detail='Task not found')
