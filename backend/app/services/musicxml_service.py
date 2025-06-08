import shutil
import uuid
from pathlib import Path
from fastapi import UploadFile
from music21 import converter,midi
from app.core.config import settings
from app.schemas.musicxml import UploadResponse

async def process_musicxml(file):
    midi_url = None
    xml_url = None
    midifile = midi.translate.streamToMidiFile(converter.parse(file))
    return(UploadResponse(xml_url,midi_url))