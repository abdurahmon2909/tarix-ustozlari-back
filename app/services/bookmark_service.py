from sqlalchemy.orm import Session

from app.models.bookmark import Bookmark


def add_bookmark(
    db: Session,
    user_id: int,
    question_id: int,
):
    existing = db.query(
        Bookmark
    ).filter(
        Bookmark.user_id == user_id,
        Bookmark.question_id == question_id
    ).first()

    if existing:
        return existing

    bookmark = Bookmark(
        user_id=user_id,
        question_id=question_id,
    )

    db.add(bookmark)

    db.commit()

    db.refresh(bookmark)

    return bookmark


def get_bookmarks(
    db: Session,
    user_id: int
):
    return db.query(
        Bookmark
    ).filter(
        Bookmark.user_id == user_id
    ).all()