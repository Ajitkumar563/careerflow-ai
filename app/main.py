from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.router import route_message
from app.resume_parser import extract_resume_text
from app.firebase import save_version, save_conversation

app = FastAPI()

# 🔥 Mount your custom frontend folder
app.mount("/frontend", StaticFiles(directory="app/frontend"), name="frontend")

CURRENT_RESUME = ""


@app.get("/")
async def home():
    return FileResponse("app/frontend/index.html")


@app.post("/upload-resume")
async def upload_resume(file: UploadFile):
    global CURRENT_RESUME
    CURRENT_RESUME = await extract_resume_text(file)
    return {"status": "uploaded", "length": len(CURRENT_RESUME)}


@app.post("/chat")
async def chat(message: str = Form(...)):
    global CURRENT_RESUME

    response, updated_resume, agent_used = await route_message(message, CURRENT_RESUME)

    if updated_resume:
        CURRENT_RESUME = updated_resume
        save_version(updated_resume)

    save_conversation(message, response)

    return {"agent": agent_used, "response": response, "updated_resume": updated_resume}
