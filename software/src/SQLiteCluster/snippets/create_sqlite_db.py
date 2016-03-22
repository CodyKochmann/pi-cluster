
from log import *

# creates a sqlite database
def create_sqlite_db(db_path):
    log("building : %s"%(db_path))
    import sqlite3
    try:
        conn = sqlite3.connect(db_path)
        conn.commit()
        conn.close()
    except Exception, e:
        log(e)
    return
