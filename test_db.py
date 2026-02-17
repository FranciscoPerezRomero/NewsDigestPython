from db.database import create_User

user_id = create_User("Carlos", "carlos@ejemplo.com")
print(f"Usuario creado con ID: {user_id}")