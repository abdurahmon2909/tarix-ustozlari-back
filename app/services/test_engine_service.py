from sqlalchemy.orm import Session

from app.models.question import (
    Question
)

from app.models.test_session import (
    TestSession
)

from app.models.user_answer import (
    UserAnswer
)

from app.models.user_statistics import (
    UserStatistics
)

from app.core.exceptions import (
    NotFoundException
)


def start_test_service(
    db: Session,
    test_id: int,
    user_id: int
):
    session = TestSession(
        user_id=user_id,

        test_id=test_id,

        correct_answers=0,

        wrong_answers=0,

        finished=False
    )

    db.add(session)

    db.commit()

    db.refresh(session)

    return session


def submit_answer_service(
    db: Session,
    session_id: int,
    question_id: int,
    selected_answer: str
):
    session = db.query(
        TestSession
    ).filter(
        TestSession.id == session_id
    ).first()

    if not session:
        raise NotFoundException(
            "Session topilmadi"
        )

    question = db.query(
        Question
    ).filter(
        Question.id == question_id
    ).first()

    if not question:
        raise NotFoundException(
            "Savol topilmadi"
        )

    is_correct = (
        question.correct_answer
        == selected_answer
    )

    answer = UserAnswer(
        user_id=session.user_id,

        question_id=question.id,

        selected_answer=
            selected_answer,

        is_correct=is_correct
    )

    db.add(answer)

    if is_correct:
        session.correct_answers += 1

        question.correct_count += 1

    else:
        session.wrong_answers += 1

        question.wrong_count += 1

    db.commit()

    return {
        "correct": is_correct
    }


def finish_test_service(
    db: Session,
    session_id: int
):
    session = db.query(
        TestSession
    ).filter(
        TestSession.id == session_id
    ).first()

    if not session:
        raise NotFoundException(
            "Session topilmadi"
        )

    total = (
        session.correct_answers
        + session.wrong_answers
    )

    percentage = 0

    if total > 0:
        percentage = int(
            (
                session.correct_answers
                / total
            ) * 100
        )

    statistics = db.query(
        UserStatistics
    ).filter(
        UserStatistics.user_id
        == session.user_id
    ).first()

    if statistics:
        statistics.tests += 1

        statistics.xp += (
            session.correct_answers
            * 10
        )

        statistics.accuracy = (
            percentage
        )

    session.finished = True

    db.commit()

    return {
        "correct":
            session.correct_answers,

        "percentage":
            percentage
    }