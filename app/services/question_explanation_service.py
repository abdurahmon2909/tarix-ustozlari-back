from openai import OpenAI

from sqlalchemy.orm import Session

from app.core.config import settings

from app.models.question import Question

from app.models.question_explanation import (
    QuestionExplanation
)

client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


async def generate_explanation(
    db: Session,
    question_id: int
):
    question = db.query(
        Question
    ).filter(
        Question.id == question_id
    ).first()

    if not question:
        return None

    prompt = f"""
    Quyidagi tarix savoliga
    professional tushuntirish yozing.

    Savol:
    {question.question_text}

    To‘g‘ri javob:
    {question.correct_answer}
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

    explanation_text = (
        response.choices[0]
        .message.content
    )

    explanation = QuestionExplanation(
        question_id=question.id,
        explanation_text=explanation_text
    )

    db.add(explanation)

    db.commit()

    db.refresh(explanation)

    return explanation