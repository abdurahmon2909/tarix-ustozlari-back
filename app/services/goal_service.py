from sqlalchemy.orm import Session

from app.models.student_goal import (
    StudentGoal
)


def create_goal(
    db: Session,
    user_id: int,
    title: str,
    target_value: int,
):
    goal = StudentGoal(
        user_id=user_id,
        title=title,
        target_value=target_value,
    )

    db.add(goal)

    db.commit()

    db.refresh(goal)

    return goal


def update_goal_progress(
    db: Session,
    goal_id: int,
    current_value: int,
):
    goal = db.query(
        StudentGoal
    ).filter(
        StudentGoal.id == goal_id
    ).first()

    if not goal:
        return None

    goal.current_value = current_value

    db.commit()

    db.refresh(goal)

    return goal