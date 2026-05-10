from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.moderation_service import (
    add_to_moderation
)

from app.services.moderation_service import (
    approve_content
)

from app.services.moderation_service import (
    reject_content
)

router = APIRouter()


@router.post("/")
async def moderation_add(
    content_type: str,
    content_text: str,
    question_id: int | None = None,
    db: Session = Depends(get_db)
):
    return add_to_moderation(
        db=db,
        content_type=content_type,
        content_text=content_text,
        question_id=question_id,
    )


@router.post("/{moderation_id}/approve")
async def moderation_approve(
    moderation_id: int,
    db: Session = Depends(get_db)
):
    return approve_content(
        db=db,
        moderation_id=moderation_id,
    )


@router.post("/{moderation_id}/reject")
async def moderation_reject(
    moderation_id: int,
    db: Session = Depends(get_db)
):
    return reject_content(
        db=db,
        moderation_id=moderation_id,
    )