from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.transcript_service import TranscriptService

router = APIRouter()
transcript_service = TranscriptService()

class TranscriptRequest(BaseModel):
    transcript: str

class TranscriptResponse(BaseModel):
    status: str
    data: dict

@router.post("/process_transcript", response_model=TranscriptResponse)
async def process_transcript(request: TranscriptRequest):
    """
    Process an interview transcript and convert it to structured CV data.
    
    Args:
        request (TranscriptRequest): The transcript text to process
        
    Returns:
        TranscriptResponse: The processed CV data
        
    Raises:
        HTTPException: If there's an error processing the transcript
    """
    try:
        result = await transcript_service.process_transcript(request.transcript)
        return TranscriptResponse(
            status="success",
            data=result
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing transcript: {str(e)}"
        ) 