from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def ana_sayfa():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form["age"])
    pain = int(request.form["pain"])
    diarrhea = int(request.form["diarrhea"])

    risk = 10

    if pain == 1:
        risk += 30

    if diarrhea == 1:
        risk += 30

    if age < 30:
        risk += 20

    return render_template(
        "result.html",
        risk=risk
    )


if __name__ == "__main__":
    app.run(debug=True)