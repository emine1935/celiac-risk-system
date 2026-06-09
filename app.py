from flask import Flask, render_template, request
import sqlite3

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

    # Veritabanına kayıt
    conn = sqlite3.connect("celiac.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO analizler
    (yas, karin_agrisi, ishal, risk)
    VALUES (?, ?, ?, ?)
    """, (age, pain, diarrhea, risk))

    conn.commit()
    conn.close()

    return render_template(
        "result.html",
        risk=risk
    )


@app.route("/admin")
def admin():

    conn = sqlite3.connect("celiac.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM analizler")

    kayitlar = cursor.fetchall()

    toplam = len(kayitlar)

    conn.close()

    return render_template(
        "admin.html",
        kayitlar=kayitlar,
        toplam=toplam
    )


if __name__ == "__main__":
    app.run(debug=True)