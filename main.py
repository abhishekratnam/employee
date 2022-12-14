from database.db import get_db
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from routes.api import router as api_router
import logging
from fastapi import FastAPI
# create logger
from config import logger_init
logger = logger_init('main')

app = FastAPI()


origins = ["http://localhost:8005"]


app.add_middleware(
                            CORSMiddleware,
                            allow_origins=origins,
                            allow_credentials=True,
                            allow_methods=["*"],
                            allow_headers=["*"],)

app.include_router(api_router)
