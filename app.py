from flask import Flask, request, render_template, redirect, url_for, jsonify, abort, make_response

from models import budgets

app = Flask(__name__)
app.config["SECRET_KEY"] = "abrakadabra"


@app.route("/api/budgets/", methods=["GET"])
def budgets_list_api():
    return jsonify(budgets.all())


@app.route("/api/budgets/<int:budget_id>", methods=["GET"])
def get_budget(budget_id):
    budget = budgets.get(budget_id)
    if not budget:
        abort(404)
    return jsonify({"budget": budget})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found", "status_code": 404}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad request", "status_code": 400}), 400)


@app.route("/api/budgets/", methods=["POST"])
def create_budget():
    if not request.json or not "pozycja" in request.json:
        abort(400)
    budget = {
        "id": budgets.all()[-1]["id"] + 1,
        "pozycja": request.json["pozycja"],
        "opis": request.json.get("opis", ""),
        "done": False
    }
    budgets.create(budget)
    return jsonify({"budget": budget}), 201


@app.route("/api/budgets/<int:budget_id>", methods=["DELETE"])
def delete_budget(budget_id):
    deleting_result = budgets.delete(budget_id)
    if not deleting_result:
        abort(404)
    return jsonify({"result": deleting_result})


@app.route("/api/budgets/<int:budget_id>", methods=["PUT"])
def update_budget(budget_id):
    budget = budgets.get(budget_id)
    if not budget:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        "pozycja" in data and not isinstance(data.get("pozycja"), str),
        "opis" in data and not isinstance(data.get("opis"), str),
        "done" in data and not isinstance(data.get("done"), bool)
    ]):
        abort(400)
    budget = {
        "pozycja": data.get("pozycja", budget["pozycja"]),
        "opis": data.get("opis", budget["opis"]),
        "done": data.get("done", budget["done"])
    }
    budgets.update(budget_id, budget)
    return jsonify({"budget": budget})

'''
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
'''

    

if __name__ == "__main__":
    app.run(debug=True)