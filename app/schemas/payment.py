from pydantic import BaseModel


class PaymentCreateSchema(BaseModel):
    user_id: int

    amount: float

    payment_provider: str