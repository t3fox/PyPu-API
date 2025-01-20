def tramitserv(item) -> dict:
    return {
        "dependencia":item.get("dependencia",""),
        "area": item.get("area",""),
        "nombre":item.get("nombre",""),
        "clave": item.get("clave",""),
        "enlace": item.get("enlace",""),
        "categoria":item.get("categoria",""),
        "keywords":item.get("keywords",""),
        "typing":item.get("typing","")
    }

def tys(tramits) -> list:
    return [tramitserv(item) for item in tramits]