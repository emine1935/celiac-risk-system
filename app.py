from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def ana_sayfa():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    age = int(request.form["age"])
    gender = request.form["gender"]

    pain = int(request.form["pain"])
    diarrhea = int(request.form["diarrhea"])
    weightloss = int(request.form["weightloss"])

    iga = float(request.form["iga"])
    ttg = float(request.form["ttg"])

    ema = int(request.form["ema"])
    hla = int(request.form["hla"])
    anemia = int(request.form["anemia"])

    risk = 0

    if pain:
        risk += 10

    if diarrhea:
        risk += 10

    if weightloss:
        risk += 10

    if anemia:
        risk += 10

    if ttg > 10:
        risk += 20

    if ema:
        risk += 20

    if hla:
        risk += 20

    if age < 18:
        risk += 5

    if risk > 100:
        risk = 100

    if risk >= 70:
        oneri = """
Yüksek risk grubundasınız.
Bir gastroenteroloji uzmanına başvurmanız önerilir.
Gluten tüketiminizi azaltmanız faydalı olabilir.
"""

    elif risk >= 40:
        oneri = """
Orta risk grubundasınız.
Kan testleri yaptırmanız önerilir.
"""

    else:
        oneri = """
Düşük risk grubundasınız.
Düzenli sağlık kontrollerinizi sürdürünüz.
"""

    conn = sqlite3.connect("celiac.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO analizler_v2
    (
    yas,cinsiyet,karin_agrisi,diyare,
    kilo_kaybi,iga,ttg_iga,
    ema_iga,hla,anemi,
    risk,oneri
    )
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
    """,
    (
    age,
    gender,
    pain,
    diarrhea,
    weightloss,
    iga,
    ttg,
    ema,
    hla,
    anemia,
    risk,
    oneri
    ))

    conn.commit()
    conn.close()

    return render_template(
        "result.html",
        risk=risk,
        oneri=oneri
    )


@app.route("/admin")
def admin():

    conn = sqlite3.connect("celiac.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM analizler_v2")

    kayitlar = cursor.fetchall()

    toplam = len(kayitlar)

    conn.close()

    return render_template(
        "admin.html",
        kayitlar=kayitlar,
        toplam=toplam
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)