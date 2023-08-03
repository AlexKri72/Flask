from flask import Flask, render_template, jsonify
from Lesson03.models01 import db, User, Post, Comment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../instance/mydatabase.db'
db.init_app(app)


@app.route('/')
def index():
    return 'Hi!'


@app.route('/data/')
def data():
    return 'Your data!'


@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/users/<username>/')
def users_by_username(username):
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/users/<int:user_id>/')
def get_posts_by_autor(user_id):
    posts = Post.query.filter_by(autor_id=user_id).all()
    if posts:
        return jsonify(
            [{'id': post.id, 'title': post.title, 'content': post.content} for post in posts]
        )
    else:
        return jsonify({'error': 'posts not found'}), 404


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Ok')


@app.cli.command('add-john')
def add_user():
    user = User(username='john', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    print('John add in DB!')


@app.cli.command('edit-john')
def edit_user():
    user = User.query.filter_by(username='john').first()
    user.email = 'new_email@example.com'
    db.session.commit()
    print('Edit John mail in DB!')


@app.cli.command('del-john')
def del_user():
    user = User.query.filter_by(username='john').first()
    db.session.delete(user)
    db.session.commit()
    print('Delete John from DB!')


@app.cli.command('fill-db')
def fill_tables():
    count = 5
    for user in range(1, count + 1):
        new_user = User(username=f'user{user}', email=f'user{user}@example.com')
        db.session.add(new_user)
    db.session.commit()

    for post in range(1, count ** 2):
        autor = User.query.filter_by(username=f'user{post % count + 1}').first()
        new_post = Post(title=f'Post title {post}', content=f'Post content {post}', autor=autor)
        db.session.add(new_post)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)
