from flask import Flask, render_template, request

app = Flask(__name__)
expenses = []

@app.route("/")
def home():
    return render_template("index.html", expenses=expenses)

@app.route("/about")
def about():
    return "Welcome to the Expense Tracker project!"

@app.route("/health")
def health():
    return "Expense Tracker is running successfully!"

@app.route("/add", methods=["POST"])
def add_expense():
    name = request.form.get("expense_name", "").strip()
    amount_text = request.form.get("amount", "").strip()

    try:
        amount = float(amount_text)
        if not name or amount <= 0:
            return "Invalid input! Enter a name and an amount above zero."
    except ValueError:
        return "Invalid amount! Please enter a valid number."

    expenses.append({"name": name, "amount": amount})
    return render_template("index.html", expenses=expenses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001,
            debug=False, use_reloader=False)
