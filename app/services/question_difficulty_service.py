from sqlalchemy.orm import Session

from app.models.question import Question

from app.models.user_answer import (
    UserAnswer
)


def update_question_difficulty(
    db: Session,
    question_id: int
):
    answers = db.query(
        UserAnswer
    ).filter(
        UserAnswer.question_id == question_id
    ).all()

    total_answers = len(answers)

    if total_answers == 0:
        return None

    correct_answers = len([
        answer
        for answer in answers
        if answer.is_correct
    ])

    success_rate = (
        correct_answers / total_answers
    ) * 100

    question = db.query(
        Question
    ).filter(
        Question.id == question_id
    ).first()

    if not question:
        return None

    if success_rate >= 80:
        question.difficulty = "easy"

    elif success_rate >= 50:
        question.difficulty = "medium"

    else:
        question.difficulty = "hard"

    db.commit()

    db.refresh(question)

    return question