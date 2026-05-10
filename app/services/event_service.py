from sqlalchemy.orm import Session

from app.models.event import Event


def get_events(
    db: Session
):
    return db.query(
        Event
    ).order_by(
        Event.event_date.asc()
    ).all()


def create_event(
    db: Session,
    title: str,
    description: str,
    event_date,
    image_url: str | None = None,
):
    event = Event(
        title=title,
        description=description,
        event_date=event_date,
        image_url=image_url,
    )

    db.add(event)

    db.commit()

    db.refresh(event)

    return event