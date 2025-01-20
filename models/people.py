from typing import Optional
from pydantic import BaseModel

from config.db import conn


class People(BaseModel):
    image:str
    name:str
    occupation:str
    description:str
    docs:list
    docname:list
    category:str