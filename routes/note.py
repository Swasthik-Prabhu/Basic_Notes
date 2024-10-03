from fastapi import APIRouter
from models.note import Note

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from fastapi import FastAPI
from pymongo import MongoClient
from config.db import conn
from schemas.note import noteEntity, notesEntity

note  = APIRouter()
templates = Jinja2Templates(directory="templates")



@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "title": doc.get("title","No Title"),
            "desc": doc.get("desc","No Description"),
            "important": doc.get("important")
        })
    return templates.TemplateResponse("index.html", {"request": request, "newDocs":newDocs}) # type: ignore

@note.post("/")
async def create_item(request: Request):
 form  = await request.form()
 formDict = dict(form)
 formDict["important"] = True if formDict.get("important") == "on" else  False # type: ignore
 note = conn.notes.notes.insert_one(formDict)
 return {"Success" : True}





#  def add_note(note: Note):
#     inserted_note = conn.notes.notes.insert_one(dict(note))
#     return noteEntity(inserted_note)