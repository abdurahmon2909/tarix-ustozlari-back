from openai import OpenAI

from app.core.config import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


async def classify_question_type(
    question_text: str
):
    prompt = f"""
    Quyidagi savol turini aniqlang.

    Variantlar:
    - mcq
    - matching
    - chronology
    - map
    - open_answer
    - table_analysis

    Savol:
    {question_text}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content