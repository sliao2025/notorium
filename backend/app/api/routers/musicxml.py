# app/api/routers/musicxml.py
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.schemas.musicxml import UploadResponse
from app.services.musicxml_service import process_musicxml
from app.core.config import settings

router = APIRouter()

@router.post("/upload", response_model=UploadResponse)
async def upload_musicxml(
    file: UploadFile = File(...),
):
    """
    Accept a MusicXML file, parse it, convert to MIDI, and return URLs.
    """
    try:
        result = await process_musicxml(file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result