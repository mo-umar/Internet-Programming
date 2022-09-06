import sqlite3
from os.path import join, split

def dictionary_factory(cursor, row):
    col_names = [d[0].lower() for d in cursor.description]
    return dict(zip(col_names, row))

def getConnection():
    this_dir = split(__file__)[0]
    fname = join(this_dir, 'sqlite-sakila.sq')
    conn = sqlite3.connect(fname)
    conn.row_factory = dictionary_factory  # note: no parentheses
    return conn
def do_command(cmd, args=[]):
    try:
        print("Connecting...")
        conn = getConnection()
        crs = conn.cursor()
        crs.execute(cmd, args)
        return crs.fetchall()
    finally:
        conn.close()
        print("Closed")

data = do_command("select * from actor")