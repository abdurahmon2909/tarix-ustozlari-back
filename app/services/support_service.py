from sqlalchemy.orm import Session

from app.models.support_ticket import (
    SupportTicket
)


def create_support_ticket(
    db: Session,
    user_id: int,
    subject: str,
    message: str,
):
    ticket = SupportTicket(
        user_id=user_id,
        subject=subject,
        message=message,
    )

    db.add(ticket)

    db.commit()

    db.refresh(ticket)

    return ticket


def get_support_tickets(
    db: Session
):
    return db.query(
        SupportTicket
    ).all()