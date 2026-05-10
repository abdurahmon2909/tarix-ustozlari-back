from openai import OpenAI

from app.core.config import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


async def parse_questions_from_text(
    text: str
):
    prompt = f"""
    Quyidagi matndan tarix testlarini ajrat.

    JSON formatda qaytar.

    Har bir savolda:
    - question
    - options
    - answer
    - difficulty
    - topic
    - explanation

    Matn:
    {text[:15000]}
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