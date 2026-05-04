import sys
import database
from datetime import datetime


def print_help():
    print("""
USAGE:
    python main.py <command> [arguments]

COMMANDS:
    add <amount> <category> [description]  - Add an expense
    list                                   - Show all expenses  
    today                                  - Show today's expenses
    month <year-month>                     - Show month expenses (e.g., 2024-11)
    delete <id>                            - Delete an expense by ID
    help                                   - Show this help message

EXAMPLES:
    python main.py add 25.50 Food Lunch
    python main.py add 15.00 Transport Bus
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
            print("Usage: python main.py add <amount> <category> [description]")
            print(
                "Categories: Food, Transport, Shopping, Bills, Entertainment, Health, Other"
            )
            return

        try:
            amount = float(sys.argv[2])
        except ValueError:
            print("Error: Amount must be a valid number (e.g., 25.50)")
            return

        category = sys.argv[3]

        if len(sys.argv) > 4:
            description = sys.argv[4]
        else:
            description = ""

        database.add_expense(amount, category, description)

    elif command == "list":
        expenses = database.get_all_expenses()

        if not expenses:
            print("No expenses found")
        else:
            print("\n=== ALL EXPENSES ===")
            for exp in expenses:
                print(
                    f"ID: {exp[0]} | Date: {exp[1]} | Amount: ₹{exp[3]} | Category: {exp[4]} | {exp[5]}"
                )

    elif command == "today":
        today = datetime.now().strftime("%Y-%m-%d")
        expenses = database.get_today_expenses(today)

        if not expenses:
            print(f"No expenses for {today}")
        else:
            print(f"\n=== TODAY'S EXPENSES ({today}) ===")
            total = 0
            for exp in expenses:
                print(f"₹{exp[3]} - {exp[4]}: {exp[5]}")
                total += exp[3]
            print(f"Total: ₹{total}")

    elif command == "month":
        if len(sys.argv) < 3:
            print("Error: Need year-month")
            return

        year_month = sys.argv[2]
        expenses = database.get_month_expenses(year_month)

        if not expenses:
            print(f"No expenses for {year_month}")
        else:
            print(f"\n=== {year_month} EXPENSES ===")
            total = 0
            for exp in expenses:
                print(f"{exp[1]} - ₹{exp[3]} - {exp[4]}: {exp[5]}")
                total += exp[3]
            print(f"Total: ₹{total}")

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: Need expense ID")
            return

        expense_id = int(sys.argv[2])
        database.delete_expense(expense_id)

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
