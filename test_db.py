from db.database import get_all_users

users = get_all_users()
for user in users:
    print(f"ID: {user[0]}, Nombre: {user[1]}, Email: {user[2]}")