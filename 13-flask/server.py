from flask import Flask, render_template, request

app = Flask(__name__)

accounts = {
    '1': {'id':'1','pin':'1111', 'balance':1000},
    '2': {'id':'2','pin':'2222', 'balance':400},
    '3': {'id':'3','pin':'3333', 'balance':38000}
}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/atm")
def atm():
    return render_template("atm.html")

@app.route("/balance", methods=['GET', 'POST'])
def balance():
    if request.method == 'POST':
        account_id = request.form['account_id']
        if account_id in accounts and accounts[account_id]['pin'] == request.form['pin']:
            return render_template("view_balance.html", account=accounts[account_id])
        else:
            return render_template("error.html", error="Wrong account id or pin")
    else:
        return render_template("balance.html")