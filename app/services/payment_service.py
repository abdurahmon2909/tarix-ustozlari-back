from sqlalchemy.orm import Session

from app.models.payment import Payment


def create_payment(
    db: Session,
    user_id: int,
    amount: float,
    payment_provider: str,
):
    payment = Payment(
        user_id=user_id,
        amount=amount,
        payment_provider=payment_provider,
    )

    db.add(payment)

    db.commit()

    db.refresh(payment)

    return payment


def mark_payment_success(
    db: Session,
    payment_id: int,
    transaction_id: str,
):
    payment = db.query(
        Payment
    ).filter(
        Payment.id == payment_id
    ).first()

    if not payment:
        return None

    payment.status = "success"

    payment.transaction_id = (
        transaction_id
    )

    db.commit()

    db.refresh(payment)

    return payment