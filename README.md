# Expense Tracker CLI

A command-line expense tracking application built with Python and SQLite. Track your daily spending, view reports by day or month, and manage your expenses efficiently.

## Features

- Add expenses with amount, category, and optional description
- View all expenses
- See today's expenses with total
- View monthly expenses with total
- Delete expenses by ID
- Automatic timestamp generation
- Persistent SQLite database

## Tech Stack

- Python 3
- SQLite3
- Datetime module

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

| Command                                 | Description                        |
| --------------------------------------- | ---------------------------------- |
| `add <amount> <category> [description]` | Add a new expense                  |
| `list`                                  | Show all expenses                  |
| `today`                                 | Show today's expenses              |
| `month <year-month>`                    | Show expenses for a specific month |
| `delete <id>`                           | Delete an expense by ID            |
| `help`                                  | Show help message                  |

### Examples

```bash
# Add expenses
python main.py add 25.50 Food Lunch at cafe
python main.py add 15.00 Transport Uber ride
python main.py add 500.00 Shopping Groceries

# View all expenses
python main.py list

# View today's expenses
python main.py today

# View November 2024 expenses
python main.py month 2024-11

# Delete expense with ID 3
python main.py delete 3
```

### Sample Output

```
=== TODAY'S EXPENSES (2026-04-29) ===
₹25.5 - Food: Lunch at cafe
₹15.0 - Transport: Uber ride
Total: ₹40.5
```

## Database Schema

| Column      | Type    | Description                  |
| ----------- | ------- | ---------------------------- |
| id          | INTEGER | Primary key (auto-increment) |
| date        | TEXT    | YYYY-MM-DD format            |
| time        | TEXT    | HH:MM format                 |
| amount      | REAL    | Expense amount (must be > 0) |
| category    | TEXT    | Expense category             |
| description | TEXT    | Optional description         |

## Configuration

The database file expenses.db is automatically created in the project directory on first run.

## Future Improvements

- Export reports to CSV/PDF
- Budget limits by category
- Data visualization with charts
- Edit existing expenses
- Search by category or date range
- GUI version (Tkinter/PyQt)

## License

MIT
