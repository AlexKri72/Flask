# Создать страницу, на которой будет форма для ввода логина и пароля
# При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с ошибкой.

from flask import Flask,render_template,request

app= Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/name/')
def name():
    name='Иван'
    return render_template('/greetings.html',name=name)

@app.route('/index/')
def index():
    return render_template('/index.html')

@app.route('/pic/')
def pic ():
    return render_template('/pic.html')

@app.route('/upload/')
def upload():
    return render_template('/upload.html')

@app.route('/login/',methods=['GET','POST'])
def login():
    l='qwerty'
    p='123'
    if request.method == 'POST':
        login1= request.form['login']
        password1= request.form['password']
        if l==login1 and p==password1:
            return render_template('/greetings.html',name=login1)
        else:
            return render_template('error.html')
    return render_template('/login.html')

if __name__=='__main__':
    app.run()