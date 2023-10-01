import sqlite3 as sq
from create_bot import bot


def sql_start():
    global base, cur
    base = sq.connect('data.db')
    cur = base.cursor()
    if base:
        print("Data base connected OK!")
    base.execute('CREATE TABLE IF NOT EXISTS cosmetic(counter INTEGER PRIMARY KEY AUTOINCREMENT, photo TEXT, name TEXT, description TEXT, price TEXT, article TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS sweets(counter INTEGER PRIMARY KEY AUTOINCREMENT, photo TEXT, name TEXT, description TEXT, price TEXT, article TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS box(counter INTEGER PRIMARY KEY AUTOINCREMENT, photo TEXT, name TEXT, description TEXT, price TEXT, article TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS accessories(counter INTEGER PRIMARY KEY AUTOINCREMENT, photo TEXT, name TEXT, description TEXT, price TEXT, article TEXT)')
    base.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER UNIQUE)''')
    base.commit()
 
async def sql_start_bot_write(id):
    base.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (id,))
    base.commit()

async def sql_start_bot_read():
    res = base.execute("SELECT COUNT(*) FROM users")
    count = res.fetchone()[0]
    return count


async def sql_write(data):
    category = data[0]
    photo = data[1]
    name = data[2]
    descrip = data[3]
    price = data[4]
    article = data[5]

    if category == "cosmetic":
        cur.execute('INSERT INTO cosmetic (photo, name, description, price, article) VALUES (?, ?, ?, ?, ?)', (photo, name, descrip, price, article))
    elif category == "sweets":
        cur.execute('INSERT INTO sweets (photo, name, description, price, article) VALUES (?, ?, ?, ?, ?)', (photo, name, descrip, price, article))
    elif category == "box":
        cur.execute('INSERT INTO box (photo, name, description, price, article) VALUES (?, ?, ?, ?, ?)', (photo, name, descrip, price, article))
    else:
        cur.execute('INSERT INTO accessories (photo, name, description, price, article) VALUES (?, ?, ?, ?, ?)', (photo, name, descrip, price, article))
    base.commit()

async def sql_read_cosmetic():
    cur.execute('SELECT * FROM cosmetic')
    rows = cur.fetchall()
    return rows

async def sql_read_sweets():
    cur.execute('SELECT * FROM sweets')
    rows = cur.fetchall()
    return rows

async def sql_read_box():
    cur.execute('SELECT * FROM box')
    rows = cur.fetchall()
    return rows

async def sql_read_accessories():
    cur.execute('SELECT * FROM accessories')
    rows = cur.fetchall()
    return rows


async def sql_delete(category, id):
    if category == "cosmetic":
        cur.execute('DELETE FROM cosmetic WHERE counter = ?', (id,))
    elif category == "sweets":
        cur.execute('DELETE FROM sweets WHERE counter = ?', (id,))
    elif category == "box":
        cur.execute('DELETE FROM box WHERE counter = ?', (id,))
    else:
        cur.execute('DELETE FROM accessories WHERE counter = ?', (id,))
    base.commit()




async def sql_write_pay(id, us, arr):
    data = arr[1]
    price = arr[0]
    cur.execute('REPLACE INTO pay VALUES (?, ?, ?, ?)', (id, us, data, price))
    base.commit()

async def sql_read_pay():
    cur.execute('SELECT * FROM pay')
    rows = cur.fetchall()
    return rows

async def sql_delete_pay(id):
    cur.execute('DELETE FROM pay WHERE id = ?', (id,))
    base.commit()