import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_script import Shell, Manager
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret key of flask api'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
manager = Manager(app)

def make_shell_context():
         return dict(app=app, db=db, User=User)
manager.add_command("shell", Shell(make_context=make_shell_context))

class User(db.Model):
    """class for users in db"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hashed = db.Column(db.String(128))
    status = db.Column(db.Boolean)

    def __init__(self, username):
        self.username = username
        self.status = False

    @property
    def password(self):
        raise AttributeError('password is not readable')

    @password.setter
    def password(self, password):
        self.password_hashed = generate_password_hash(password)

    def verify(self, password):
        return check_password_hash(self.password_hashed, password)

    def login(self):
        self.status = True

    def logout(self):
        if self.status:
            self.status = False
            return True
        else:
            return False

    def __repr__(self):
        return '<User id: {}, username: {}>'.format(str(self.id), self.username)

"""
class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    author_id = db.Column(db.Integer, db.Foreign_key('User.id'))

    def __init__(self, title, author_id):
        self.title = title
        self.author_id = author_id
"""

@app.route('/api/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).all()
    if user:
        return jsonify({'status' : 'fail', 'message' : 'username already exists'})
    new_user = User(username)
    new_user.password = password
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'status' : 'success', 'user' : {
    'id' : new_user.id, 'username' : new_user.username}})

@app.route('/api/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).all()
    if not user:
        return jsonify({'status' : 'fail', 'message' : 'user does not exist'})
    user = user[0]
    if user.verify(password):
        user.login()
        return jsonify({'status' : 'success'})
    else:
        return jsonify({'status' : 'fail', 'message' : 'username and password do not match'})

@app.route('/api/logout/<string:name>')
def logout(name):
    user = User.query.filter_by(username=name).all()
    if not user:
        return jsonify({'status' : 'fail', 'message' : 'user does not exist'})
    user = user[0]
    if user.logout():
        return jsonify({'status' : 'success'})
    return jsonify({'status' : 'fail', 'message' : 'user did not log in'})


#@app.route('/api/articles')
#def get_articles():


@app.route('/api/user/<string:name>')
def get_user_info(name):
    user = User.query.filter_by(username=name).all()
    if not user:
        return jsonify({'status' : 'fail', 'message' : 'user does not exist'})
    user = user[0]
    return jsonify({'status' : 'success',
    'user' : {'id' : user.id, 'username' : user.username}})

#@app.route('/api/message')

if __name__ == '__main__':
    #db.drop_all()
    #db.create_all()
    if not os.path.exists('db.sqlite'):
        db.create_all()
    #manager.run()
    app.run(debug=True)
