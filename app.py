from flask import Flask, request, render_template, redirect, url_for

from models import budget
from forms import BudgetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "abrakadabra"

@app.route("/budget/", methods=["GET", "POST"])
def budget_list():
    form = BudgetForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            budget.create(form.data)
            budget.save_all()
        return redirect(url_for("budget_list"))
    return render_template("budgets.html", form=form, budget=budget.all(), error=error)

@app.route("/budget/<int:budget_id/", methods=["GET", "POST"])
def budget_details(budget_id):
    budgeting = budget.get(budget_id - 1)
    form = BudgetForm(data = budgeting)

    if request.method == "POST":
        if form.validate_on_submit():
            budget.update(budget_id - 1, form.data)
        return redirect(url_for("budget_list"))
    return render_template("budget.html", form=form, budget_id=budget_id)

if __name__ == "__main__":
    app.run(debug=True)


