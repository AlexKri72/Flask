from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

@app.route('/if/')
def html_index():
    context={
        'title':'Ветвление',
        'user':'Крутой хакер',
        'number':1
    }
    return render_template('index.html',**context)

if __name__=='__main__':
    app.run(debug=True)