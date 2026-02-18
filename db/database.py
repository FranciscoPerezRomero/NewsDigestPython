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

#* Función para registro de usuarios
def create_User(user_Name,user_Email):
    #* Conexión a base de datos
    conn = sqlite3.connect('newsdigest.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name,email) VALUES (?,?)",(user_Name,user_Email))
        response = cursor.lastrowid
        conn.commit()
        return response
    except sqlite3.IntegrityError:
        return None
    finally:
        conn.close()

#* Función para registrar intereses en etiquetas de cada usuario
def add_userTags(user_id,tags):
    conn = sqlite3.connect('newsdigest.db')
    cursor = conn.cursor()
    try:
        for tag in tags:
            cursor.execute("INSERT INTO user_tags (tag_name,user_id) VALUES (?,?)",(tag,user_id))
        conn.commit()
    except sqlite3.IntegrityError:
        return None
    finally:
        conn.close()

def get_user_tags(user_id):
    conn = sqlite3.connect('newsdigest.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM user_tags WHERE user_id = ?",(user_id,))
        results = cursor.fetchall()
        user_tags = [tuple[2] for tuple in results]
        return user_tags
    except sqlite3.IntegrityError:
        return None
    finally:
        conn.close()

def get_all_users():
    conn = sqlite3.connect('newsdigest.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        info = cursor.fetchall()
        return info
    except sqlite3.IntegrityError:
        return None
    finally:
        conn.close()