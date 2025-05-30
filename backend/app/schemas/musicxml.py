# app/schemas/musicxml.py
from pydantic import BaseModel, HttpUrl

class UploadResponse(BaseModel):
    xml_url: HttpUrl
    midi_url: HttpUrl