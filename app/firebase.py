import os
import firebase_admin
from firebase_admin import credentials, firestore

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIREBASE_PATH = os.path.join(BASE_DIR, "firebase.json")

if not os.path.exists(FIREBASE_PATH):
    raise FileNotFoundError(f"firebase.json not found at: {FIREBASE_PATH}")

cred = credentials.Certificate(FIREBASE_PATH)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

def save_version(resume_text):
    db.collection("resume_versions").add({
        "resume": resume_text
    })

def save_conversation(user_msg, bot_msg):
    db.collection("conversation").add({
        "user": user_msg,
        "bot": bot_msg
    })
