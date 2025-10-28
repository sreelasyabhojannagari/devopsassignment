from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import random
import os

app = Flask(__name__)
app.secret_key = "super_secret_key"

USERS_FILE = "users.json"

# Load users from JSON
def load_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump({}, f)
    with open(USERS_FILE, "r") as f:
        return json.load(f)

# Save users to JSON
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# Home redirects to login
@app.route('/')
def index():
    return redirect(url_for('login'))

# Login
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users = load_users()
        if username in users and users[username] == password:
            session["username"] = username
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password", "error")
    return render_template("login.html")

# Register
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users = load_users()
        if username in users:
            flash("Username already exists", "error")
        else:
            users[username] = password
            save_users(users)
            flash("Registration successful! Please login.", "success")
            return redirect(url_for("login"))
    return render_template("register.html")

# Rock-Paper-Scissors game
@app.route('/home', methods=["GET", "POST"])
def home():
    if "username" not in session:
        return redirect(url_for("login"))

    user_choice = None
    computer_choice = None
    result = None
    options = ["Rock", "Paper", "Scissors"]

    if request.method == "POST":
        user_choice = request.form.get("choice")
        computer_choice = random.choice(options)

        # Determine winner
        if user_choice == computer_choice:
            result = "It's a Tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You Win! 🎉"
        else:
            result = "Computer Wins! 💻"

        flash(result, "info")  # Show result as flash message

    return render_template("home.html", username=session["username"],
                           user_choice=user_choice, computer_choice=computer_choice)

# Logout
@app.route('/logout')
def logout():
    session.pop("username", None)
    flash("Logged out successfully", "success")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
