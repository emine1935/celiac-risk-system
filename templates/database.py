import sqlite3

conn = sqlite3.connect("celiac.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS analizler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    yas INTEGER,
    karin_agrisi INTEGER,
    ishal INTEGER,
    risk INTEGER
)
""")

conn.commit()
conn.close()

print("Veritabanı oluşturuldu.")