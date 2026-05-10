from sqlalchemy.orm import Session

from app.models.question import (
    Question
)

from app.models.test_session import (
    TestSession
)

from app.core.exceptions import (
    NotFoundException
)


def get_tests_service():
    return [
        {
            "id": 1,

            "title":
                "O'zbekiston tarixi",

            "topic":
                "Temuriylar"
        }
    ]


def get_session_questions_service(
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

    questions = db.query(
        Question
    ).limit(10).all()

    return {
        "questions": questions
    }