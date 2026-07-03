from fastapi import FastAPI
from sqlalchemy import text
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Intern!"}

@app.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected ✅"}
    except Exception as e:
        return {"status": "error", "database": f"not connected ❌ {str(e)}"}
    
@app.get("/users")
def get_users():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM users"))
        return [dict(row._mapping) for row in result]