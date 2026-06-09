import sqlite3

conn = sqlite3.connect("celiac.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS analizler_v2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    yas INTEGER,
    cinsiyet TEXT,
    karin_agrisi INTEGER,
    diyare INTEGER,
    kilo_kaybi INTEGER,
    iga REAL,
    ttg_iga REAL,
    ema_iga INTEGER,
    hla INTEGER,
    anemi INTEGER,
    risk INTEGER,
    oneri TEXT
)
""")

conn.commit()
conn.close()

print("analizler_v2 tablosu oluşturuldu.")