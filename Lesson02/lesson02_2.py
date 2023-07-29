# Создать страницу, на которой будет изображение и ссылка на другую страницу, на которой будет отображаться форма
# для загрузки изображений.


from flask import Flask,render_template

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

@app.route('/login/')
def login():
    return render_template('/login.html')

if __name__=='__main__':
    app.run()