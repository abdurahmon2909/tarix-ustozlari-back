from sqlalchemy.orm import Session

from app.models.test_category import (
    TestCategory
)

from app.models.test_subcategory import (
    TestSubcategory
)


def get_categories(
    db: Session
):
    return db.query(
        TestCategory
    ).all()


def get_subcategories(
    db: Session,
    category_id: int
):
    return db.query(
        TestSubcategory
    ).filter(
        TestSubcategory.category_id == category_id
    ).all()