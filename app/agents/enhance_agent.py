from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

async def enhance_section(user_message: str, resume_text: str):
    prompt = f"""
    You are a professional Resume Enhancement Agent.

    USER REQUEST:
    {user_message}

    CURRENT RESUME:
    {resume_text}

    TASK:
    - Identify which resume section needs improvement (summary, skills, achievements, experience)
    - Rewrite ONLY that section professionally
    - DO NOT return the full resume unless the user explicitly asks
    """

    result = await llm.ainvoke(prompt)
    return result.content
