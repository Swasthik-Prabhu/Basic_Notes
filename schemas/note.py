def noteEntity(item) -> dict:
    return {
        "id": item["id"],
        "title" : item["title"],
        "desc" : item["desc"],
        "important" : item["important"]
    }
def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]