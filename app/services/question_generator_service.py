from openai import OpenAI

from app.core.config import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


async def generate_mcq_questions(
    topic: str,
    count: int = 10
):
    prompt = f"""
    Tarix fanidan professional multiple choice testlar yarat.

    Mavzu:
    {topic}

    Savollar soni:
    {count}

    JSON formatda qaytar.
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