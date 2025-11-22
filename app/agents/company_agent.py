from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

async def company_optimize(message: str, resume: str):
    """Optimize resume based on company requirements."""
    
    prompt = f"""
    You are a resume optimization expert.

    User request:
    {message}

    Current Resume:
    {resume}

    Improve the resume according to the company instructions.
    Return ONLY the improved resume text.
    """
    
    result = await llm.ainvoke(prompt)
    return result.content
