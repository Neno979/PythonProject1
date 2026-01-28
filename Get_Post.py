from flask import Flask , render_template, request

app = Flask(__name__)

@app.context_processor
def color():
    return { "color": "light" }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Get-Post", methods=["GET","POST"])
def getpost():
    if request.method == "GET":
        return render_template("Get_Post.html")
    else:
        currency_name = request.form.get("currency_name")
        currency_amount = request.form.get("currency_amount")
        currency_price = request.form.get("currency_price")
        print(currency_name)
        print(currency_amount)
        print(currency_price)
        return render_template("Get_Post_end.html")

        print(currency_name, currency_amount, currency_price)

if __name__ == "__main__":
    app.run(use_reloader=True)