import uuid

def generator():
    return uuid.uuid4().hex[:6].upper()