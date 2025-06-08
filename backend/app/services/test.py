import shutil
import uuid
from pathlib import Path
from music21 import converter,midi 
# from app.core.config import settings
# from app.schemas.musicxml import UploadResponse

score = converter.parse(r"C:\Users\trext\OneDrive\Documentos\Scores\XMLs\Defying Gravity - Graduation.mxl")
midi_out = score.write("midi", fp=r"C:\Scores\XMLs\Defying Gravity - Graduation.mid")

print(midi_out)
