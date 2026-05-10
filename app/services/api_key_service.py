from uuid import uuid4

from sqlalchemy.orm import Session

from app.models.api_key import APIKey


def generate_api_key(
    db: Session,
    name: str,
):
    key = str(uuid4())

    api_key = APIKey(
        name=name,
        key=key,
    )

    db.add(api_key)

    db.commit()

    db.refresh(api_key)

    return api_key


def validate_api_key(
    db: Session,
    key: str,
):
    return db.query(
        APIKey
    ).filter(
        APIKey.key == key,
        APIKey.is_active == True
    ).first()