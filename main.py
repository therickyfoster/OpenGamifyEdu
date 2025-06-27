from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from app.routes import register_routes

app = FastAPI(title="OpenGamifyEdu")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
register_routes(app)

@app.get("/")
def root():
    return {"message": "Welcome to the OpenGamifyEdu platform!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
