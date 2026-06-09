import pandas as pd
import sqlite3

df = pd.read_excel("colyak_hastaligi_ysa_veri_seti (1) (2).xlsx")

conn = sqlite3.connect("celiac.db")

cursor = conn.cursor()

for _, row in df.iterrows():

    risk = 10

    if row["Karin_Agrisi"] == 1:
        risk += 30

    if row["Diyare"] == 1:
        risk += 30

    if row["Yas"] < 30:
        risk += 20

    cursor.execute("""
    INSERT INTO analizler
    (yas, karin_agrisi, ishal, risk)
    VALUES (?, ?, ?, ?)
    """, (
        int(row["Yas"]),
        int(row["Karin_Agrisi"]),
        int(row["Diyare"]),
        risk
    ))

conn.commit()
conn.close()

print("500 kayıt başarıyla eklendi.")