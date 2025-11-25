import sqlite3

DB_NAME = "passwords.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (id INTEGER PRIMARY KEY,
                  site TEXT NOT NULL,
                  username TEXT NOT NULL,
                  password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_password(site, username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO passwords (site, username, password) VALUES (?, ?, ?)",
              (site, username, password))
    conn.commit()
    conn.close()

def get_passwords():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT id, site, username, password FROM passwords")
    data = c.fetchall()
    conn.close()
    return data

def delete_password(entry_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM passwords WHERE id=?", (entry_id,))
    conn.commit()
    conn.close()
