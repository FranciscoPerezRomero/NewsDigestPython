import sqlite3
#* Creamos funcion que crea las primeras tablas de la base de datos
def init_db():
    conn = sqlite3.connect('newsdigest.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_tags 
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    tag_name TEXT,
                    FOREIGN KEY (user_id) REFERENCES users(id))''')
    conn.commit()
    conn.close()

def create_User(user_Name,user_Email):
    #* Conexión a base de datos
    conn = sqlite3.connect('newsdigest.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name,email) VALUES (?,?)",(user_Name,user_Email))
        query = cursor.lastrowid
        conn.commit()
        return query
    except sqlite3.IntegrityError:
        return None
    finally:
        conn.close()