from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'Привет, незнакомец!'

@app.route('/Николай/')
def nike():
    return  'Привет, Николай!'

@app.route('/Иван/')
def ivan():
    return 'Привет, Ванечка!'

@app.route('/Фёдор/')
@app.route('/Федор/')
@app.route('/Fedor/')
@app.route('/Федя/')
@app.route('/федя/')
def fedor():
    return 'Привет, Феодор!'


if __name__=="__main__":
    app.run(debug=True)