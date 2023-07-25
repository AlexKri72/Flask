from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/about/')
def about():
    return 'about page'

@app.route('/contact/')
def contact():
    return 'contact page'

@app.route('/<int:num1>/<int:num2>/')
def plus(num1,num2):
    return f'{num1} + {num2} = {num1+num2}'

@app.route('/<string:text>/')
def len_str(text):
    return f'{len(text)}'

@app.route('/index/')
def index():
    return render_template('index1.html')

@app.route('/students/')
def students():
    stud=[{
        'Name':'Алексей',
        'Lastname':'Кривоногих',
        'Age':51 ,
        'Averadge': 4.9
    },
    {
        'Name': 'Иван',
        'Lastname': 'Иванов',
        'Age': 15,
        'Averadge': 4.8
    }]
    return render_template('index1.html',context= stud)


@app.route('/news/')
def news():
    news=[['title_new','text_new','data'],
        ['title_new', 'text_new','data']]
    return render_template('index2.html',context= news)

if __name__=='__main__':
    app.run(debug=True)