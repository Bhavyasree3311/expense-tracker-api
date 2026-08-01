# Smart Expense Tracker API

## 📌 Overview

Smart Expense Tracker API is a REST API built using FastAPI. It helps users manage their daily expenses by allowing them to add, view, filter, calculate totals, and delete expenses.

## 🚀 Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Delete an expense
- Store data permanently in JSON

## 🛠 Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- JSON

## 📂 Project Structure

expense-tracker-api/
│
├── src/
│ ├── main.py
│ ├── routes.py
│ ├── models.py
│ └── storage.py
│
├── tests/
│ └── test_api.py
│
├── expenses.json
├── requirements.txt
└── README.md

## ▶️ Run Project

python -m uvicorn src.main:app --reload

## 📖 API Endpoints

GET /

POST /expenses

GET /expenses

GET /expenses/category/{category}

GET /expenses/total

DELETE /expenses/{id}

## 🧪 Run Tests

python -m pytest

## 👨‍💻 Author

Bhavyasree