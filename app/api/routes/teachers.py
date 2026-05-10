from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.services.teacher_service import (
    get_teachers
)

from app.services.teacher_service import (
    create_teacher
)

from app.services.teacher_service import (
    upload_teacher_material
)

router = APIRouter()


@router.get("/")
async def teachers(
    db: Session = Depends(get_db)
):
    return get_teachers(
        db=db
    )


@router.post("/")
async def teacher_create(
    full_name: str,
    subject: str,
    region: str,
    school_name: str | None = None,
    experience_years: int = 0,
    db: Session = Depends(get_db)
):
    return create_teacher(
        db=db,
        full_name=full_name,
        subject=subject,
        region=region,
        school_name=school_name,
        experience_years=experience_years,
    )


@router.post("/materials")
async def teacher_material(
    teacher_id: int,
    title: str,
    file_url: str,
    material_type: str = "pdf",
    db: Session = Depends(get_db)
):
    return upload_teacher_material(
        db=db,
        teacher_id=teacher_id,
        title=title,
        file_url=file_url,
        material_type=material_type,
    )