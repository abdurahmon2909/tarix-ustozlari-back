from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.payment_service import (
    create_payment
)

from app.services.payment_service import (
    mark_payment_success
)

from app.services.subscription_service import (
    activate_subscription
)

router = APIRouter()


@router.post("/create")
async def payment_create(
    user_id: int,
    amount: float,
    payment_provider: str,
    db: Session = Depends(get_db)
):
    return create_payment(
        db=db,
        user_id=user_id,
        amount=amount,
        payment_provider=payment_provider,
    )


@router.post("/success")
async def payment_success(
    payment_id: int,
    transaction_id: str,
    db: Session = Depends(get_db)
):
    payment = mark_payment_success(
        db=db,
        payment_id=payment_id,
        transaction_id=transaction_id,
    )

    if payment:
        activate_subscription(
            db=db,
            user_id=payment.user_id,
        )

    return payment