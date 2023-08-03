# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.
import random

from flask import Flask, render_template, jsonify
from Lesson03.models03_1 import db, Student, Facultet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello word!'


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('База данных создана')


@app.route('/fill-db/')
def fill_db():
    for i in range(1, 8):
        new_facultet = Facultet(fac_name=f'Facultet{i}')
        db.session.add(new_facultet)
    db.session.commit()
    print('Fill facultets table')

    for i in range(1, 6):
        new_student = Student(
            name=f'name{i}',
            lastname=f'lastname{i}',
            age=i,
            gender=random.choice(['man', 'women']),
            group=random.choice(['1A', '2B', '3A']),
            id_facultet=random.choice(1, 2, 3)
        )
        db.session.add(new_student)
    db.session.commit()
    print('Fill students table')

@app.route('/print-students/')
def print_students():
    student=Student.query.all()
    context={'student':student}
    return render_template('students',**context)


if __name__ == '__main__':
    app.run(debug=True)
