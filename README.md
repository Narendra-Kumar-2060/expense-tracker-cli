# Expense Tracker CLI

A command-line personal finance tracking application built with Python and SQLite. Track both **expenses** and **income**, monitor your net balance, and manage your transactions efficiently.

## Features

- ✅ **Track Expenses** - Add expenses with amount, category, description, and payment method
- ✅ **Track Income** - Add money received from various sources
- ✅ **Payment Methods** - Support for UPI and Cash payments
- ✅ **View Transactions** - See all transactions with clear + (income) and - (expense) indicators
- ✅ **Today's Summary** - View today's transactions with expense, income, and net balance
- ✅ **Monthly Reports** - View monthly summaries with totals
- ✅ **Delete Transactions** - Remove unwanted entries by ID
- ✅ **Automatic Timestamps** - Date and time are recorded automatically
- ✅ **Persistent Storage** - SQLite database stores all data locally

## Tech Stack

- Python 3
- SQLite3
- Datetime module (Python standard library)

## Installation

```bash
# Clone the repository
git clone https://github.com/Narendra-Kumar-2060/expense-tracker.git
cd expense-tracker

# No external dependencies required (uses only Python standard library)

# Run the application
python main.py help
```

## Usage

### Commands

| Command                                                 | Description                                |
| ------------------------------------------------------- | ------------------------------------------ |
| add <amount> <category> [description] [payment_method]  | Add an expense                             |
| income <amount> <source> [description] [payment_method] | Add income received                        |
| list                                                    | Show all transactions                      |
| today                                                   | Show today's transactions with net balance |
| month <year-month>                                      | Show month transactions with net balance   |
| delete <id>                                             | Delete a transaction by ID                 |
| help                                                    | Show help message                          |

### Valid Categories (for expenses)

- Food
- Transport
- Shopping
- Bills
- Entertainment
- Health
- Other

### Valid Payment Methods

- upi
- cash

### Examples

```bash
# Add expenses
python main.py add 25.50 Food "Lunch at cafe" upi
python main.py add 15.00 Transport "Bus fare" cash
python main.py add 500.00 Shopping Groceries

# Add income
python main.py income 50000 Salary "Monthly salary" upi
python main.py income 2000 Friend "Loan repayment" cash
python main.py income 1000 Freelance "Website design"

# View all transactions
python main.py list

# View today's transactions
python main.py today

# View November 2024 transactions
python main.py month 2024-11

# Delete transaction with ID 3
python main.py delete 3
```

## Sample Output

### Today's Transactions

```
=== TODAY'S TRANSACTIONS (2026-05-11) ===
--------------------------------------------------
+ ₹50000 - Salary (upi): Monthly salary
- ₹25.5 - Food (upi): Lunch at cafe
- ₹15.0 - Transport (cash): Bus fare
--------------------------------------------------
Total Expense: ₹40.5
Total Income:  ₹50000
Net Balance:   ₹49959.5
```

### All Transactions

```
=== ALL TRANSACTIONS ===
----------------------------------------------------------------------
ID: 1 | 2026-05-11 14:30 | +₹50000 | Salary | Monthly salary | upi
ID: 2 | 2026-05-11 14:32 | -₹25.5 | Food | Lunch at cafe | upi
ID: 3 | 2026-05-11 14:33 | -₹15.0 | Transport | Bus fare | cash
----------------------------------------------------------------------
```

## Database Schema

| Column           | Type    | Description                           |
| ---------------- | ------- | ------------------------------------- |
| id               | INTEGER | Primary key (auto-increment)          |
| date             | TEXT    | YYYY-MM-DD format                     |
| time             | TEXT    | HH:MM format                          |
| amount           | REAL    | Transaction amount (must be > 0)      |
| category         | TEXT    | Category (expense) or source (income) |
| description      | TEXT    | Optional description                  |
| payment_method   | TEXT    | Payment method (upi/cash)             |
| transaction_type | TEXT    | Type of transaction (expense/income)  |

## Configuration

- The database file expenses.db is automatically created in the project directory on first run
- Payment methods can be extended by modifying VALID_METHOD in database.py
- Expense categories can be extended by modifying VALID_CATEGORIES in database.py

## Future Improvements

- Add more payment methods (card, bank transfer)
- Edit existing transactions
- Export reports to CSV/PDF
- Budget limits by category
- Search by date range or category
- Data visualization with charts
- GUI version (Tkinter/PyQt)
- Monthly recurring transactions
- Backup and restore functionality

## License

MIT
