Pizza Ordering Web App(DoughDev Pizza)

This is a simple Flask-based web application with authentication features. The project is part of my learning journey in backend and full-stack development, where I’m building a foundation in Flask, SQLAlchemy, user authentication, and web security practices.

Features

User registration and login

Password hashing with werkzeug.security

Session management using Flask-Login

Flash messaging for user feedback

SQLite database with SQLAlchemy ORM

Blueprint structure for clean, modular code

📚 What I’m Learning in the Process

As I build this web app, I’m actively learning:

Flask Basics – app structure, routes, templates, and blueprints

Authentication – handling user login/logout, secure password storage

SQLAlchemy ORM – defining models and querying the database

Flask-Login – managing sessions and restricting access to certain routes

Flask Flash Messages – providing user feedback

Modular Project Structure – separating logic into blueprints (auth, views, models)

Debugging Flask Apps – using print statements, checking routes, and template feedback

Frontend + Backend Connection – linking HTML forms with Flask routes

🛠️ Tech Stack

Backend: Flask (Python)

Database: SQLite (via SQLAlchemy)

Authentication: Flask-Login, Werkzeug security

Frontend: HTML, CSS (basic templates, can expand later)

📂 Project Structure
pizza-ordering-system/
instance/
-database.db
website/
-static/
-images
-style.css Though i have used internal css
-templates/
-base.html
-cart.html
-home.html
-login.html
-menu.html
-signup.html
**init**.py
auth.py
models.py
views.py
main.py
README.md

Getting Started

1. Clone the repo
   git clone https://github.com/KelvinKipchumba67/pizza-ordering-web-app.git
   cd your-repo-name

2.Go to main.py

3. Run the app

✅ Future Improvements

Add email verification

Implement password reset

Improve frontend UI (Bootstrap/Tailwind)

Add user profile & dashboard

Deploy to a cloud service (Heroku/Render)

📖 Learning Mindset

This project is not just about coding — it’s about understanding the fundamentals of web development step by step. I’m documenting my progress and refining my skills in:

Backend development with Flask

Secure authentication practices

Database management with SQLAlchemy

Connecting frontend and backend
