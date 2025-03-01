import sqlite3

def save_analysis(texte, prediction, confidence):
    conn = sqlite3.connect("fake_news.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texte TEXT,
            prediction TEXT,
            confidence REAL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.execute("INSERT INTO analyses (texte, prediction, confidence) VALUES (?, ?, ?)", (texte, prediction, confidence))
    conn.commit()
    conn.close()