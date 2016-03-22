# creates a sqlite database
def create_sqlite_db(db_path):
    import sqlite3
    conn = sqlite3.connect(db_path)
    conn.commit()
    conn.close()
    return
