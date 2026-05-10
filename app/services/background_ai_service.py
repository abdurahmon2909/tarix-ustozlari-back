from app.core.background import (
    executor
)

from app.services.question_explanation_service import (
    generate_explanation
)


def queue_explanation_generation(
    db,
    question_id: int
):
    executor.submit(
        generate_explanation,
        db,
        question_id
    )