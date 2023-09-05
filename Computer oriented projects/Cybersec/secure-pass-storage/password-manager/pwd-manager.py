from flask import Flask, request, render_template, redirect, jsonify
from flask_cors import CORS
import bcrypt
import json
import os

# added template_folder parameter
app = Flask(__name__, template_folder='../templates',
            static_folder='../static')
CORS(app)

CREDENTIALS_FILE = 'credentials.json'
MIN_USERNAME_LENGTH = 5
MIN_PASSWORD_LENGTH = 8


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def check_password(hashed_password, user_password):
    return bcrypt.checkpw(user_password.encode(), hashed_password)


def save_credentials(username, email, password):
    hashed_password = hash_password(password)
    credentials = {username: {'email': email,
                              'password': hashed_password.decode()}}

    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, 'r') as file:
            stored_credentials = json.load(file)
    else:
        stored_credentials = {}

    stored_credentials.update(credentials)

    with open(CREDENTIALS_FILE, 'w') as file:
        json.dump(stored_credentials, file)


def validate_login(username, password):
    if not os.path.exists(CREDENTIALS_FILE):
        return False

    with open(CREDENTIALS_FILE, 'r') as file:
        stored_credentials = json.load(file)

    if username in stored_credentials and check_password(stored_credentials[username]['password'].encode(), password):
        return True
    else:
        return False


@app.route('/', methods=['GET'])
def landing():
    return render_template('landing.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        # Do your validation here
        save_credentials(username, email, password)
        return "User registered successfully. Please check your email for verification."
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if validate_login(username, password):
            return redirect("/password_manager")
        else:
            return "Incorrect username or password."
    return render_template('login.html')


@app.route('/password_manager', methods=['GET', 'POST'])
def password_manager():
    if request.method == 'POST':
        website = request.form.get('website')
        username = request.form.get('username')
        password = request.form.get('password')
        return "Password added successfully."
    return render_template('index.html')


@app.route('/addpwd', methods=['GET', 'POST'])
def add_password():
    if request.method == 'POST':
        # Handle form submission and password addition logic here
        return "Password added successfully."
    return render_template('addpwd.html')


def add_password():
    password = request.json['password']
    return jsonify({'message': 'Password added successfully'}), 200


if __name__ == "__main__":
    app.run(debug=True)
