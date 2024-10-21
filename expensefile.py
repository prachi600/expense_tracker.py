import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as file:
                self.expenses = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.expenses = []

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file)

    def add_expense(self, amount, category, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        expense = {'amount': amount, 'category': category, 'date': date}
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        return self.expenses

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            self.save_expenses()

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_expense(50, 'Food')
    tracker.add_expense(20, 'Transport')
    print("Current Expenses:", tracker.view_expenses())
    tracker.delete_expense(0)
    print("After Deletion:", tracker.view_expenses())
