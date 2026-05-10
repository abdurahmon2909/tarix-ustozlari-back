from sqlalchemy.orm import Session

from app.models.teacher import Teacher

from app.models.teacher_material import (
    TeacherMaterial
)


def get_teachers(
    db: Session
):
    return db.query(
        Teacher
    ).all()


def create_teacher(
    db: Session,
    full_name: str,
    subject: str,
    region: str,
    school_name: str | None = None,
    experience_years: int = 0,
):
    teacher = Teacher(
        full_name=full_name,
        subject=subject,
        region=region,
        school_name=school_name,
        experience_years=experience_years,
    )

    db.add(teacher)

    db.commit()

    db.refresh(teacher)

    return teacher


def upload_teacher_material(
    db: Session,
    teacher_id: int,
    title: str,
    file_url: str,
    material_type: str = "pdf",
):
    material = TeacherMaterial(
        teacher_id=teacher_id,
        title=title,
        file_url=file_url,
        material_type=material_type,
    )

    db.add(material)

    db.commit()

    db.refresh(material)

    return material