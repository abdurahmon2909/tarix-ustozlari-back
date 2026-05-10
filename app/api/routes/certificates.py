from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.milliy_certificate_session import (
    MilliyCertificateSession
)

from app.models.milliy_certificate_result import (
    MilliyCertificateResult
)

from app.schemas.milliy_certificate import (
    CertificateResultResponse
)

from app.schemas.milliy_certificate import (
    CertificateSessionResponse
)

router = APIRouter()


@router.get(
    "/sessions",
    response_model=list[
        CertificateSessionResponse
    ]
)
async def certificate_sessions(
    db: Session = Depends(get_db)
):
    sessions = db.query(
        MilliyCertificateSession
    ).all()

    return sessions


@router.get(
    "/results",
    response_model=list[
        CertificateResultResponse
    ]
)
async def certificate_results(
    db: Session = Depends(get_db)
):
    results = db.query(
        MilliyCertificateResult
    ).all()

    return results