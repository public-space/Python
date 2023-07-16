from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_security.utils import hash_password, verify_password
from datetime import datetime
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoursecretkey'  # replace with your own secret key

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)

# User list - in a production app, you'd want to use a database
users = []
try:
    with open('users.json', 'r') as f:
        users = json.load(f)
except FileNotFoundError:
    pass

# Note list
notes = []

# User class
class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user['id'] == int(user_id):
            return User(user['id'], user['username'], user['password'])
    return None

@app.route('/')
@login_required
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.json['username']
        password = request.json['password']
        for user in users:
            if user['username'] == username and verify_password(password, user['password']):
                login_user(User(user['id'], user['username'], user['password']))
                return redirect(url_for('home'))
        return 'Invalid credentials', 401
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.json['username']
        password = hash_password(request.json['password'])
        id = len(users) + 1
        users.append({'id': id, 'username': username, 'password': password})
        with open('users.json', 'w') as f:
            json.dump(users, f)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/add_note', methods=['POST'])
@login_required
def add_note():
    note = request.json['note']
    timestamp = datetime.now().strftime('%H:%M')
    notes.append((timestamp, current_user.username, note))
    return jsonify({"success": True})

@app.route('/get_notes', methods=['GET'])
@login_required
def get_notes():
    return jsonify(notes)

if __name__ == "__main__":
    app.run(debug=True)
