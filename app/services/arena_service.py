import random

from sqlalchemy.orm import Session

from app.models.arena_match import ArenaMatch
from app.models.question import Question


def create_arena_match(
    db: Session,
    player_one_id: int
):
    match = ArenaMatch(
        player_one_id=player_one_id,
        status="waiting"
    )

    db.add(match)

    db.commit()

    db.refresh(match)

    return match


def generate_battle_questions(
    db: Session,
    limit: int = 10
):
    questions = db.query(
        Question
    ).filter(
        Question.battle_allowed == True
    ).all()

    random.shuffle(questions)

    return questions[:limit]