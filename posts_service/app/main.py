from fastapi import FastAPI
import os
from .routes import router as comments_router
from .database import client

app = FastAPI()

app.include_router(comments_router, prefix="/comments", tags=["comments"])

@app.on_event("startup")
async def startup_db_client():
    try:
        await client.admin.command('ping')
        print("Successfully connected to MongoDB!")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        raise

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
@app.get("/")
def read_root():
    return {"message": "Comments Service"}