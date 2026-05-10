from sqlalchemy.orm import Session

from app.models.moderation_queue import (
    ModerationQueue
)


def add_to_moderation(
    db: Session,
    content_type: str,
    content_text: str,
    question_id: int | None = None,
):
    item = ModerationQueue(
        content_type=content_type,
        content_text=content_text,
        question_id=question_id,
    )

    db.add(item)

    db.commit()

    db.refresh(item)

    return item


def approve_content(
    db: Session,
    moderation_id: int,
):
    item = db.query(
        ModerationQueue
    ).filter(
        ModerationQueue.id == moderation_id
    ).first()

    if not item:
        return None

    item.status = "approved"

    db.commit()

    db.refresh(item)

    return item


def reject_content(
    db: Session,
    moderation_id: int,
):
    item = db.query(
        ModerationQueue
    ).filter(
        ModerationQueue.id == moderation_id
    ).first()

    if not item:
        return None

    item.status = "rejected"

    db.commit()

    db.refresh(item)

    return item