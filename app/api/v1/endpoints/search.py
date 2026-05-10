from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import (
    get_db
)

from app.schemas.search import (
    SearchResponse
)

from app.services.search_service import (
    search_questions_service
)

router = APIRouter()


@router.get(
    "",
    response_model=list[
        SearchResponse
    ]
)
async def search(
    query: str,
    db: Session = Depends(get_db)
):
    return search_questions_service(
        db=db,
        query=query
    )