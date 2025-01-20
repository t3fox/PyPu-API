from pymongo import AsyncMongoClient
from pymongo.server_api import ServerApi

uri="TU CONEXIÓN"
conn = AsyncMongoClient(uri,server_api=ServerApi('1'))

db = conn.get_default_database()


try:
    
    conn.admin.command("ping")
    print("...::: Conexión a Base de Datos OK :::...")


except Exception as err:

    raise Exception("Error en la conexión", err)
