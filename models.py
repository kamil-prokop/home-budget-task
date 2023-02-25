import json

class Budget:
    def __init__(self):
        try:
            with open("budget.json", "r") as f:
                self.budget = json.load(f)
        except FileNotFoundError:
            self.budget = []

    def all(self):
        return self.budget
    
    def get(self, id):
        return self.budget[id]
    
    def create(self, data):
        data.pop("csrf_token")
        self.budget.append(data)

    def save_all(self):
        with open("budget.json", "w") as f:
            json.dump(self.budget, f)
    
    def update(self, id, data):
        data.pop("csrf_token")
        self.budget[id] = data
        self.save_all()
    
budget = Budget()