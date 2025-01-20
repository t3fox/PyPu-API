from fastapi import APIRouter
from config.db import db
from schemas.tramites import tys

ts = APIRouter()

@ts.get("/all_tramits")
async def all_ts():

    data = await db.tzxts.find().to_list(length=None)
    return tys(data)