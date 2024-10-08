from fastapi import FastAPI
from .routes import router
from .database import engine
from . import models

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)

# Include the API routes
app.include_router(router)
