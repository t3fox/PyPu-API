from fastapi import APIRouter
from config.db import db

from schemas.people import peoples, channels

gob = APIRouter()



@gob.get("/gob")
async def represents():
    
    data = await db.govermentx068.find().to_list(length=None)     
    return peoples(data)

@gob.get("/gob/channels")
async def gobchannels():

    data = await db.gobxchannels.find().to_list(length=None)
    return channels(data)

