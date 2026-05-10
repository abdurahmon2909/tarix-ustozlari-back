from sqlalchemy.orm import Session

from app.models.mentor_group import (
    MentorGroup
)

from app.models.mentor_group_student import (
    MentorGroupStudent
)


def create_group(
    db: Session,
    teacher_id: int,
    title: str,
    description: str | None = None,
):
    group = MentorGroup(
        teacher_id=teacher_id,
        title=title,
        description=description,
    )

    db.add(group)

    db.commit()

    db.refresh(group)

    return group


def join_group(
    db: Session,
    group_id: int,
    user_id: int,
):
    existing = db.query(
        MentorGroupStudent
    ).filter(
        MentorGroupStudent.group_id == group_id,
        MentorGroupStudent.user_id == user_id
    ).first()

    if existing:
        return existing

    student = MentorGroupStudent(
        group_id=group_id,
        user_id=user_id,
    )

    db.add(student)

    db.commit()

    db.refresh(student)

    return student