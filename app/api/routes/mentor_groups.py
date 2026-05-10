from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.mentor_group_service import (
    create_group
)

from app.services.mentor_group_service import (
    join_group
)

router = APIRouter()


@router.post("/")
async def mentor_group_create(
    teacher_id: int,
    title: str,
    description: str | None = None,
    db: Session = Depends(get_db)
):
    return create_group(
        db=db,
        teacher_id=teacher_id,
        title=title,
        description=description,
    )


@router.post("/join")
async def mentor_group_join(
    group_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):
    return join_group(
        db=db,
        group_id=group_id,
        user_id=user_id,
    )