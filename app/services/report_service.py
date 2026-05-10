from sqlalchemy.orm import Session

from app.models.report import Report


def create_report(
    db: Session,
    reporter_user_id: int,
    reason: str,
    description: str | None = None,
    reported_question_id: int | None = None,
):
    report = Report(
        reporter_user_id=reporter_user_id,
        reason=reason,
        description=description,
        reported_question_id=reported_question_id,
    )

    db.add(report)

    db.commit()

    db.refresh(report)

    return report


def get_reports(
    db: Session
):
    return db.query(
        Report
    ).all()