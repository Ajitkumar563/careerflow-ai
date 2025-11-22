from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

async def jd_optimize(user_message: str, resume_text: str):
    prompt = f"""
    You are an expert ATS + JD Matching Agent.

    USER MESSAGE:
    {user_message}

    CURRENT RESUME:
    {resume_text}

    TASK:
    - Extract all required skills from the job description
    - Match resume content to the job requirements
    - Add missing skills (only relevant ones)
    - Add quantifiable achievements where possible
    - Rewrite resume for better ATS score
    - Return ONLY the updated resume in text form
    """

    result = await llm.ainvoke(prompt)
    return result.content
