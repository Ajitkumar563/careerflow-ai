import docx2txt
import fitz


async def extract_resume_text(file):
    name = file.filename.lower()
    content = await file.read()

    if name.endswith(".pdf"):
        pdf = fitz.open(stream=content, filetype="pdf")
        text = ""
        for page in pdf:
            text += page.get_text()
        return text

    if name.endswith(".docx"):
        with open("temp_resume.docx", "wb") as f:
            f.write(content)
        return docx2txt.process("temp_resume.docx")

    return "Unsupported file format"
