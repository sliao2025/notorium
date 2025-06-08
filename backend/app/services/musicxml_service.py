import shutil
import uuid
from pathlib import Path
# from fastapi import UploadFile
from music21 import converter,midi 
# from app.core.config import settings
from app.schemas.musicxml import UploadResponse

async def process_musicxml(file):
    xml_url = converter.parse(file)
    midi_url = xml_url.write("midi", fp="midiConversion.mid")
    return(UploadResponse(xml_url, midi_url))