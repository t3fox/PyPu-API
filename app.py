# from typing import Union
from fastapi import FastAPI


from routes.gobierno import gob
from routes.tramites import ts


app = FastAPI()


app.include_router(gob)
app.include_router(ts)


