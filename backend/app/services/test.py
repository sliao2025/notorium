import shutil
import uuid
from pathlib import Path
from music21 import converter,midi 
from app.core.config import settings
from app.schemas.musicxml import UploadResponse

midifile = midi.translate.streamToMidiFile(converter.parse('c:\Users\trext\OneDrive\Documentos\Scores\XMLs\Defying Gravity - Graduation.mxl'))