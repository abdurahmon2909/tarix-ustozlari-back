from openai import OpenAI

from app.core.config import settings

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


async def analyze_book_text(
    text: str
):
    prompt = f"""
    Quyidagi tarix kitobini analiz qil:

    1. Chapterlarni top
    2. Topiclarni top
    3. Muhim sanalarni top
    4. Muhim shaxslarni top
    5. Test uchun muhim qismlarni ajrat

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