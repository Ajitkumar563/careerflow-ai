# 🚀 Careerflow Resume AI  
**AI-powered Resume Optimizer, JD Matcher & ATS Enhancement Tool**

Careerflow-AI is a fully automated system that:
- Reads & extracts text from resumes (PDF/DOCX)
- Enhances or rewrites resumes using OpenAI models  
- Matches resumes with job descriptions  
- Translates resumes into different languages  
- Stores conversation logs + resume versions in Firebase  
- Provides an interactive chat-based UI

---

## ⭐ Features

### 🔹 Resume Understanding
Extracts text using:
- `docx2txt`
- `PyMuPDF (fitz)`
- `pdfplumber`

### 🔹 Smart AI Router  
Automatically detects user intent and chooses the correct agent:
| User Intent | Agent Used |
|-------------|------------|
| “Optimize my resume”, “Rewrite summary” | `company_agent` |
| “Match to this JD”, “Improve for Data Scientist role” | `jd_agent` |
| “Translate to German/Spanish/Hindi” | `translation_agent` |

### 🔹 Firebase Integration
Stores:
- Resume versions  
- Chat history  

### 🔹 Beautiful Frontend
- Clean upload section  
- Chat-style conversation  
- Loader animation  
- Smooth UX  

---

# 📊 System Architecture

> **Add this image after downloading your FigJam flowchart**

```md
![System Architecture](assets/flowchart.png)

![Upload Screen](assets/upload-screen.png)
![Chat Screen](assets/chat-screen.png)



careerflow-ai/
│
├── app/
│   ├── agents/
│   │   ├── company_agent.py
│   │   ├── jd_agent.py
│   │   ├── translation_agent.py
│   │
│   ├── firebase.py
│   ├── resume_parser.py
│   ├── router.py
│   ├── main.py
│
├── frontend/
│   ├── index.html
│
├── .gitignore
├── README.md
├── requirements.txt
├── .env


conda create -n careerflow python=3.10
conda activate careerflow


pip install -r requirements.txt


OPENAI_API_KEY=your_key
FIREBASE_PATH=app/firebase.json


## Run The Server (Uvicorn)

uvicorn app.main:app --reload

## Run on custom host/port:
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
