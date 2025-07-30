import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Load environment variables from .env
load_dotenv()

# Import API routers
from src.api import data_api, knowledge_api, model_api, user_api, predict_api

app = FastAPI(
    title="DataSwift API",
    description="A comprehensive data science platform API",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-frontend.vercel.app",
        "https://dataswift-frontend.onrender.com",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(data_api.router, prefix="/api/data", tags=["data"])
app.include_router(knowledge_api.router, prefix="/api/knowledge", tags=["knowledge"])
app.include_router(model_api.router, prefix="/api/model", tags=["model"])
app.include_router(predict_api.router, prefix="/api/predict", tags=["predict"])
app.include_router(user_api.router, prefix="/api/user", tags=["user"])

@app.get("/")
async def root():
    return {"message": "Welcome to DataSwift API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "DataSwift API"}

# Example: Accessing MongoDB URI from environment
MONGODB_URI = os.getenv("MONGODB_URI")

if __name__ == "__main__":
    # Use PORT from environment if available (for Render), else default to 8000
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)