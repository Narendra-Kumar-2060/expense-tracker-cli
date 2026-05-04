import sqlite3
from datetime import datetime
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.db")

VALID_CATEGORIES = [
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Entertainment",
    "Health",
    "Other",
]


def setup():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    sql = "CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, date TEXT, time TEXT, amount REAL NOT NULL, category TEXT, description TEXT)"
    cur.execute(sql)
    con.commit()
    con.close()


def add_expense(amount, category, description):
    if amount <= 0:
        print("Amount must be greater than 0")
        return False

    # Validate category (case-insensitive)
    category_clean = category.capitalize()
    if category_clean not in VALID_CATEGORIES:
        print(f"Invalid category. Choose from: {', '.join(VALID_CATEGORIES)}")
        return False
    category = category_clean

    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M")
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    sql = "INSERT INTO expenses (date, time, amount, category, description) VALUES (?, ?, ?, ?, ?)"
    cur.execute(sql, (current_date, current_time, amount, category, description))
    con.commit()
    con.close()
    print("Expense added!")
    return True


def get_today_expenses(date):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    sql = "SELECT * FROM expenses WHERE date = ?"
    cur.execute(sql, (date,))
    rows = cur.fetchall()
    con.close()
    return rows


def get_month_expenses(year_month):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    sql = "SELECT * FROM expenses WHERE date LIKE ?"
    cur.execute(sql, (f"{year_month}%",))
    rows = cur.fetchall()
    con.close()
    return rows


def get_all_expenses():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    sql = "SELECT * FROM expenses"
    cur.execute(sql)
    rows = cur.fetchall()
    con.close()
    return rows


def delete_expense(expense_id):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    cur.execute("SELECT id FROM expenses WHERE id = ?", (expense_id,))
    if not cur.fetchone():
        print(f"Expense with ID {expense_id} not found")
        con.close()
        return False

    cur.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    con.commit()
    con.close()
    print("Expense deleted!")
    return True


setup()
