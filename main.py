import sys
import database
from datetime import datetime


def print_help():
    print("""
USAGE:
    python main.py <command> [arguments]

COMMANDS:
    add <amount> <category> [description] [payment_method]  - Add an expense
    income <amount> <source> [description] [payment_method]  - Add money received
    list                                                   - Show all transactions  
    today                                                  - Show today's transactions
    month <year-month>                                     - Show month transactions (e.g., 2024-11)
    delete <id>                                            - Delete a transaction by ID
    help                                                   - Show this help message

EXAMPLES:
    python main.py add 25.50 Food Lunch upi
    python main.py add 15.00 Transport Bus cash
    python main.py income 5000 Salary "Monthly salary" upi
    python main.py list
    python main.py today
    python main.py month 2024-11
    python main.py delete 3
""")


def main():
    if len(sys.argv) == 1 or sys.argv[1].lower() in ["help", "-h", "--help"]:
        print_help()
        return

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) < 4:
            print("Error: Need amount and category")
            print(
                "Usage: python main.py add <amount> <category> [description] [payment_method]"
            )
            print(
                "Categories: Food, Transport, Shopping, Bills, Entertainment, Health, Other"
            )
            print("Payment methods: upi, cash")
            return

        try:
            amount = float(sys.argv[2])
        except ValueError:
            print("Error: Amount must be a valid number (e.g., 25.50)")
            return

        category = sys.argv[3]
        description = sys.argv[4] if len(sys.argv) > 4 else ""
        payment_method = sys.argv[5] if len(sys.argv) > 5 else "cash"

        database.add_expense(amount, category, description, payment_method)

    elif command == "income":
        if len(sys.argv) < 4:
            print("Error: Need amount and source")
            print(
                "Usage: python main.py income <amount> <source> [description] [payment_method]"
            )
            print("Payment methods: upi, cash")
            return

        try:
            amount = float(sys.argv[2])
        except ValueError:
            print("Error: Amount must be a valid number")
            return

        source = sys.argv[3]
        description = sys.argv[4] if len(sys.argv) > 4 else ""
        payment_method = sys.argv[5] if len(sys.argv) > 5 else "cash"

        database.add_income(amount, source, description, payment_method)

    elif command == "list":
        transactions = database.get_all_expenses()

        if not transactions:
            print("No transactions found")
        else:
            print("\n=== ALL TRANSACTIONS ===")
            print("-" * 70)
            for trans in transactions:
                (
                    trans_id,
                    date,
                    time,
                    amount,
                    category,
                    description,
                    payment_method,
                    trans_type,
                ) = trans

                if trans_type == "income":
                    symbol = "+"
                    amount_display = f"₹{amount}"
                else:
                    symbol = "-"
                    amount_display = f"₹{amount}"

                print(
                    f"ID: {trans_id} | {date} {time} | {symbol}{amount_display} | {category} | {description} | {payment_method}"
                )
            print("-" * 70)

    elif command == "today":
        today = datetime.now().strftime("%Y-%m-%d")
        transactions = database.get_today_expenses(today)

        if not transactions:
            print(f"No transactions for {today}")
        else:
            print(f"\n=== TODAY'S TRANSACTIONS ({today}) ===")
            print("-" * 50)
            total_expense = 0
            total_income = 0

            for trans in transactions:
                (
                    trans_id,
                    date,
                    time,
                    amount,
                    category,
                    description,
                    payment_method,
                    trans_type,
                ) = trans

                if trans_type == "income":
                    print(f"+ ₹{amount} - {category} ({payment_method}): {description}")
                    total_income += amount
                else:
                    print(f"- ₹{amount} - {category} ({payment_method}): {description}")
                    total_expense += amount

            print("-" * 50)
            print(f"Total Expense: ₹{total_expense}")
            print(f"Total Income:  ₹{total_income}")
            print(f"Net Balance:   ₹{total_income - total_expense}")

    elif command == "month":
        if len(sys.argv) < 3:
            print("Error: Need year-month")
            return

        year_month = sys.argv[2]
        transactions = database.get_month_expenses(year_month)

        if not transactions:
            print(f"No transactions for {year_month}")
        else:
            print(f"\n=== {year_month} TRANSACTIONS ===")
            print("-" * 60)
            total_expense = 0
            total_income = 0

            for trans in transactions:
                (
                    trans_id,
                    date,
                    time,
                    amount,
                    category,
                    description,
                    payment_method,
                    trans_type,
                ) = trans

                if trans_type == "income":
                    print(
                        f"{date} | + ₹{amount} | {category} | {description} | {payment_method}"
                    )
                    total_income += amount
                else:
                    print(
                        f"{date} | - ₹{amount} | {category} | {description} | {payment_method}"
                    )
                    total_expense += amount

            print("-" * 60)
            print(f"Total Expense: ₹{total_expense}")
            print(f"Total Income:  ₹{total_income}")
            print(f"Net Balance:   ₹{total_income - total_expense}")

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Need transaction ID")
            return

        try:
            expense_id = int(sys.argv[2])
            database.delete_expense(expense_id)
        except ValueError:
            print("Error: ID must be a number")

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
