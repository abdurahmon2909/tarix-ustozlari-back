from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def home_data():
    return {
        "quote":
            "Tarixni bilgan kelajakni quradi",

        "xp": 1250,

        "rank": 12
    }