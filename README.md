# Interview2CV

A FastAPI-based backend service that processes interview transcripts and converts them into structured CV data.

## Architecture

### Overview
The application follows a clean architecture pattern with the following components:

```
interview2cv/
├── app/
│   ├── api/
│   │   └── routes/
│   │       └── transcript.py      # API route handlers
│   ├── core/
│   │   ├── config.py             # Application configuration
│   │   └── security.py           # Security utilities
│   ├── services/
│   │   └── transcript_service.py  # Business logic for transcript processing
│   └── main.py                   # FastAPI application entry point
├── tests/
│   └── api/
│       └── test_transcript.py     # API tests
├── pyproject.toml                # Project dependencies and metadata
└── README.md                     # This file
```

### Components

#### API Layer (`app/api/`)
- Handles HTTP requests and responses
- Implements route handlers for transcript processing
- Manages request validation and response formatting

#### Core Layer (`app/core/`)
- Contains application-wide configurations
- Implements security measures and utilities
- Manages environment variables and settings

#### Services Layer (`app/services/`)
- Implements business logic
- Handles transcript processing and CV generation
- Manages data transformations

### API Endpoints

#### POST /process_transcript
Processes interview transcripts and converts them to structured CV data.

**Request Body:**
```json
{
    "transcript": "string"  // The interview transcript text
}
```

**Response:**
```json
{
    "status": "success",
    "data": {
        // Processed CV data
    }
}
```

## Setup and Installation

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app.main:app --reload
```

## Development

### Running Tests
```bash
pytest
```

### Code Style
The project follows PEP 8 guidelines and uses black for code formatting.

## Environment Variables

Create a `.env` file in the root directory with the following variables:
```
APP_ENV=development
DEBUG=True
```

## Dependencies

- FastAPI: Web framework
- Pydantic: Data validation
- Uvicorn: ASGI server
- pytest: Testing framework

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 