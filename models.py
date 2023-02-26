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
        budget = [budget for budget in self.all() if budget["id"] == id]
        if budget:
            return budget[0]
        return []
    
    def create(self, data):
        self.budgets.append(data)
        self.save_all()

    def delete(self, id):
        budget = self.get(id)
        if budget:
            self.budgets.remove(budget)
            self.save_all()
            return True
        return False

    def update(self, id, data):
        budget = self.get(id)
        if budget:
            index = self.budgets.index(budget)
            self.budgets[index] = data
            self.save_all()
            return True
        return False

    def save_all(self):
        with open("budget.json", "w", encoding="UTF-8") as f:
            json.dump(self.budgets, f)
   
budgets = Budgets()