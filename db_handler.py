import sqlite3, json, time
from pathlib import Path
APP_DIR = Path(__file__).parent.resolve()
DB_FILE = APP_DIR / "history.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS uploads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        youtube_url TEXT,
        title TEXT,
        facebook_response TEXT,
        ts INTEGER
    )''')
    conn.commit()
    conn.close()

def save_entry(youtube_url, title, facebook_response):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('INSERT INTO uploads (youtube_url, title, facebook_response, ts) VALUES (?,?,?,?)',
                (youtube_url, title, json.dumps(facebook_response), int(time.time())))
    conn.commit()
    conn.close()

def list_entries(limit=50):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute('SELECT youtube_url, title, facebook_response, ts FROM uploads ORDER BY id DESC LIMIT ?', (limit,))
    rows = cur.fetchall()
    conn.close()
    results = []
    for r in rows:
        results.append({'youtube_url': r[0], 'title': r[1], 'facebook_response': json.loads(r[2]), 'ts': r[3]})
    return results
