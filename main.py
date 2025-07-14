from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine
Base.metadata.create_all(bind=engine)

app= FastAPI(title="This is a FastApi app with Aurthentication and Authorization",)
app.include_router(router)

@app.get("/")
def home():
    return {"message": "WELCOME TO NAVEE'S FASTAPI APP...."}

