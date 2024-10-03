from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()


conn = MongoClient("mongodb+srv://swasthikp03:swasthik@swasthikprabhu.fabhbaq.mongodb.net")

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
    



