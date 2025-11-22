from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

async def translate_text(user_message: str, resume_text: str):
    prompt = f"""
    You are a professional Resume Translation Agent.

    USER REQUEST:
    {user_message}

    RESUME TEXT:
    {resume_text}

    TASK:
    1. Detect which language the user wants (German, Spanish, French, Hindi, etc.)
    2. Translate ONLY the resume text.
    3. Maintain formatting, bullet points, and structure.
    """

    result = await llm.ainvoke(prompt)
    return result.content
