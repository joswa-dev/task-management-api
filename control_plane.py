from fastapi import FastAPI
from dotenv import load_dotenv
import uvicorn

load_dotenv()

app = FastAPI(title="Aegis Control Plane")


@app.get("/")
def home():
    return {
        "message": "Aegis activated"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


if __name__ == "__main__":
    uvicorn.run(
        "control_plane:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )