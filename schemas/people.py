def people(item) -> dict:
    return {
        "image":item.get("image",""),
        "name":item.get("name",""),
        "occupation":item.get("occupation",""),
        "description":item.get("description",""),
        "docs":item.get("docs",""),
        "docname":item.get("docname",""),
        "category":item.get("category","")
    }

def peoples(entity) -> list:
    return [people(item) for item in entity]


def channel(item) -> dict:
    return {
        "chan_name":item.get("chann_name",""),
        "description":item.get("description",""),
        "image":item.get("image",""),
        "links":item.get("links",""),
        "coords": item.get("coords",""),
        "category":item.get("category","")
    }

def channels(chann) -> list:
    return [channel(item) for item in chann]