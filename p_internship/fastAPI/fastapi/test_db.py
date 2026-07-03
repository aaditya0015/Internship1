from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:root@localhost:8080/todo_db"

engine = create_engine(DATABASE_URL)

try:
    connection = engine.connect()
    print("✅ Connected successfully!")
    connection.close()
except Exception as e:
    print("❌ Connection failed")
    print(e)