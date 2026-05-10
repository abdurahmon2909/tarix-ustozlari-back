from sqlalchemy.orm import Session

from app.models.milliy_certificate_result import (
    MilliyCertificateResult
)

from app.utils.grade import calculate_grade


def create_certificate_result(
    db: Session,
    user_id: int,
    session_id: int,
    score: int,
    percentage: float,
    theta: float,
    percentile: float,
):
    grade = calculate_grade(
        percentage
    )

    result = MilliyCertificateResult(
        user_id=user_id,
        session_id=session_id,
        score=score,
        percentage=percentage,
        theta=theta,
        percentile=percentile,
        grade=grade,
    )

    db.add(result)

    db.commit()

    db.refresh(result)

    return result