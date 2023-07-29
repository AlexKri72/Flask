# Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов в тексте и переход на страницу с результатом.


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

@app.route('/textinput/',methods=['GET','POST'])
def inputtext():
    if request.method=="POST":
        txt=request.form['text']
        return render_template('textout.html',txtlen=len([word for word in txt.split()]))
    return render_template('/textinput.html')

if __name__=='__main__':
    app.run()