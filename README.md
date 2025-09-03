# 🍕 DoughDev Pizza Ordering Web App

Welcome to DoughDev Pizza! This is a modern, full-stack pizza ordering web application built with Flask, SQLAlchemy, and Flask-Login. It features user authentication, a dynamic menu, cart management, and a complete checkout flow.

---

## 🚀 Features

- User registration and login
- Secure password hashing
- Session management (Flask-Login)
- Flash messaging for user feedback
- SQLite database with SQLAlchemy ORM
- Modular blueprint structure
- Dynamic pizza menu and cart
- Address collection and order confirmation
- Responsive, colorful UI

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Database:** SQLite (SQLAlchemy ORM)
- **Authentication:** Flask-Login, Werkzeug security
- **Frontend:** HTML, CSS (internal and static)

---

## 📂 Project Structure

```
pizza-ordering-system/
├── instance/
│   └── database.db
├── website/
│   ├── static/
│   │   ├── style.css
│   │   └── images/
│   ├── templates/
│   │   ├── base.html
│   │   ├── cart.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── menu.html
│   │   ├── signup.html
│   │   ├── checkout.html
│   │   └── confirmation.html
│   ├── __init__.py
│   ├── auth.py
│   ├── models.py
│   └── views.py
├── main.py
└── README.md
```

---

## ⚡ Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KelvinKipchumba67/pizza-ordering-web-app.git
   cd pizza-ordering-web-app
   ```
2. **Install dependencies:**
   ```bash
   pip install flask flask_sqlalchemy flask_login werkzeug
   ```
3. **Run the app:**
   ```bash
   python main.py
   ```
4. **Open your browser:**
   Visit `http://127.0.0.1:5000` to start ordering!

---

## 🧑‍💻 Usage

- **Sign up** for a new account
- **Log in** to access the menu and cart
- **Browse the menu** and add pizzas to your cart
- **Proceed to checkout**, enter your delivery address, and place your order
- **View order confirmation** with address and payment info

---

## 🌱 Contributing

Pull requests and suggestions are welcome! If you find a bug or want to add a feature, feel free to open an issue or submit a PR.

---

## 📈 Future Improvements

- Email verification
- Password reset
- Improved frontend UI (Bootstrap/Tailwind)
- User profile & dashboard
- Online payment integration
- Deployment to Heroku/Render

---

## 📖 Learning Mindset

This project is a hands-on journey into web development fundamentals. It covers backend logic, secure authentication, database management, and connecting frontend to backend. Every feature is an opportunity to learn and grow as a developer.

---

**Made with ❤️ by Kelvin Kipchumba**
