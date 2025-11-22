from langchain_openai import ChatOpenAI

from app.agents.company_agent import company_optimize
from app.agents.jd_agent import jd_optimize
from app.agents.translation_agent import translate_text
from app.agents.enhance_agent import enhance_section

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


async def detect_intent(message: str) -> str:
    prompt = f"""
    Classify the intent from this user message:

    "{message}"

    Choose ONLY one:
    - company
    - jd
    - translation
    - enhancement

    Rules:
    - If message contains Google, Microsoft, Meta → company
    - If message contains 'JD', 'job description', 'match', 'role' → jd
    - If message says 'translate', 'German', 'Spanish', 'French' → translation
    - If message says 'improve', 'rewrite', 'ATS', 'enhance', 'add skills' → enhancement

    Return only the label.
    """
    return (await llm.ainvoke(prompt)).content.strip().lower()


async def route_message(message: str, resume_text: str):
    intent = await detect_intent(message)

    if intent == "company":
        res = await company_optimize(message, resume_text)
        return res, res, "Company Agent"

    elif intent == "jd":
        res = await jd_optimize(message, resume_text)
        return res, res, "JD Agent"

    elif intent == "translation":
        res = await translate_text(message, resume_text)
        return res, res, "Translation Agent"

    else:
        res = await enhance_section(message, resume_text)
        return res, res, "Enhancement Agent"
