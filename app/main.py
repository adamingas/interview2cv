from fastapi import FastAPI
from app.api.routes import transcript

app = FastAPI(
    title="Interview2CV API",
    description="API for processing interview transcripts into CV data",
    version="1.0.0"
)

# Include routers
app.include_router(transcript.router, prefix="/api/v1", tags=["transcript"])
