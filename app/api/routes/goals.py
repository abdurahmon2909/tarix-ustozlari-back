from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.goal_service import (
    create_goal
)

from app.services.goal_service import (
    update_goal_progress
)

router = APIRouter()


@router.post("/")
async def goal_create(
    user_id: int,
    title: str,
    target_value: int,
    db: Session = Depends(get_db)
):
    return create_goal(
        db=db,
        user_id=user_id,
        title=title,
        target_value=target_value,
    )


@router.put("/{goal_id}")
async def goal_update(
    goal_id: int,
    current_value: int,
    db: Session = Depends(get_db)
):
    return update_goal_progress(
        db=db,
        goal_id=goal_id,
        current_value=current_value,
    )