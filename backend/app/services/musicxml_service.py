import shutil
import uuid
from pathlib import Path
from fastapi import UploadFile
from music21 import converter
from app.core.config import settings
from app.schemas.musicxml import UploadResponse

