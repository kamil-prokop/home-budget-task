import json

class Budgets():
    def __init__(self):
        try:
            with open("budget.json", "r", encoding="UTF-8") as f:
                self.budgets = json.load(f)
        except FileNotFoundError:
            self.budgets = []

    def all(self):
        return self.budgets
    
    def get(self, id):
        return self.budgets[id]
    
    def create(self, data):
        data.pop("csrf_token")
        self.budgets.append(data)

    def save_all(self):
        with open("budget.json", "w", encoding="UTF-8") as f:
            json.dump(self.budgets, f)
    
    def update(self, id, data):
        data.pop("csrf_token")
        self.budgets[id]=data
        self.save_all()
    
budgets = Budgets()