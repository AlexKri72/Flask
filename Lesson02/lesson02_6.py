# Создать страницу, на которой будет форма для ввода имени и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.


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


@app.route('/ariphmetic/',methods=['GET','POST'])
def ariphmetic():
    if request.method == 'POST':
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        operation = request.form['operation']
        if operation == '+':
            result = num1 + num2
        if operation == '*':
            result = num1 * num2
        if operation == '/':
            result = num1 / num2
        if operation == '-':
            result = num1 - num2
        return render_template('/ariphmeticresult.html',num1=num1,num2=num2,operation=operation,result=result)
    return render_template('/ariphmetic.html')


@app.route('/age/',methods=['GET','POST'])
def age():
    if request.method == 'POST':
        name= request.form['name']
        age= int(request.form['age'])
        if 0<age<=100:
            return render_template('/greetings.html',name=name)
        else:
            return render_template('ageerror.html')
    return render_template('/age.html')



if __name__=='__main__':
    app.run()