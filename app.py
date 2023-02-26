from flask import Flask, request, render_template, redirect, url_for

from models import budgets
from forms import BudgetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "abrakadabra"

@app.route("/budgets/", methods=["GET", "POST"])
def budget_list():
    form = BudgetForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            budgets.create(form.data)
            budgets.save_all()
        return redirect(url_for("budget_list"))
    return render_template("budgets.html", form=form, budgets=budgets.all(), error=error)

@app.route("/budgets/<int:budget_id>/", methods=["GET", "POST"])
def budget_details(budget_id):
    budget = budgets.get(budget_id - 1)
    form = BudgetForm(data = budget)

    if request.method == "POST":
        if form.validate_on_submit():
            budgets.update(budget_id - 1, form.data)
        return redirect(url_for("budget_list"))
    return render_template("budget.html", form=form, budget_id=budget_id)

if __name__ == "__main__":
    app.run(debug=True)