import sqlite3

def init_db(db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tokens (pair_address TEXT PRIMARY KEY)''')
    conn.commit()
    conn.close()

def token_exists(db_file, pair_address):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('SELECT 1 FROM tokens WHERE pair_address = ?', (pair_address,))
    result = c.fetchone()
    conn.close()
    return result is not None

def add_token(db_file, pair_address):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('INSERT OR IGNORE INTO tokens (pair_address) VALUES (?)', (pair_address,))
    conn.commit()
    conn.close()