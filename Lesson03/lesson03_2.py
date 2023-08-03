# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с указанием их авторов.

from flask import Flask, render_template
from Lesson03.models03_2 import db, Books, Autors

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_03_2.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hello word!'


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('База данных создана')
@app.route('/fill-books/')
def fill_books():
    for i in range(1, 8):
        new_book = Books(title=f'Book{i}')
        db.session.add(new_book)
    db.session.commit()
    print('Books table filled')

@app.route('/fill-autors/')
def fill_autors():
    for i in range(1, 6):
        new_autor = Autors(
            name=f'name{i}',
            lastname=f'lastname{i}',
        )
        db.session.add(new_autor)
    db.session.commit()
    print('Autors table filled')

@app.route('/print-books/')
def print_books():
    book=Books.query.all()
    context={'book':book}
    return render_template('books.html',**context)


if __name__ == '__main__':
    app.run(debug=True)
