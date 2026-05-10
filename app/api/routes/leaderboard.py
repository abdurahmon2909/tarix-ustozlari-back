from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.user import User

router = APIRouter()


@router.get("/")
async def global_leaderboard(
    db: Session = Depends(get_db)
):
    users = db.query(User).order_by(
        User.sharaf.desc()
    ).limit(100).all()

    return users


@router.get("/xp")
async def xp_leaderboard(
    db: Session = Depends(get_db)
):
    users = db.query(User).order_by(
        User.xp.desc()
    ).limit(100).all()

    return users