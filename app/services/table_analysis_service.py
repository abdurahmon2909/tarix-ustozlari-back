from sqlalchemy.orm import Session

from app.models.table_analysis_question import (
    TableAnalysisQuestion
)


def get_table_analysis_questions(
    db: Session
):
    return db.query(
        TableAnalysisQuestion
    ).all()