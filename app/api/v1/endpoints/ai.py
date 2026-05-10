from fastapi import APIRouter

router = APIRouter()


@router.get("/explanation/{question_id}")
async def explanation(
    question_id: int
):
    return {
        "explanation":
            "Bu savolda Amir Temur haqida so'z bormoqda."
    }