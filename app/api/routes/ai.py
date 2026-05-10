from fastapi import APIRouter
from app.services.question_classifier_service import (
    classify_question_type
)
from app.services.ai_service import generate_question
from app.services.question_explanation_service import (
    generate_explanation
)
from app.services.question_generator_service import (
    generate_mcq_questions
)

router = APIRouter()


@router.get("/generate")
async def ai_generate_question(
    topic: str
):
    result = await generate_question(
        topic
    )

    return {
        "result": result
    }


@router.get("/generate-mcq")
async def ai_generate_mcq(
    topic: str,
    count: int = 10
):
    result = await generate_mcq_questions(
        topic=topic,
        count=count
    )

    return {
        "result": result
    }
@router.post("/classify-question")
async def classify_question(
    question_text: str
):
    result = await classify_question_type(
        question_text
    )

    return {
        "question_type": result
    }
@router.post("/generate-explanation")
async def explanation(
    question_id: int,
    db: Session = Depends(get_db)
):
    result = await generate_explanation(
        db=db,
        question_id=question_id
    )

    return result