from sqlalchemy.orm import Session

from app.models.news import News


def get_news(
    db: Session
):
    return db.query(
        News
    ).order_by(
        News.created_at.desc()
    ).all()


def create_news(
    db: Session,
    title: str,
    content: str,
    image_url: str | None = None,
):
    news = News(
        title=title,
        content=content,
        image_url=image_url,
    )

    db.add(news)

    db.commit()

    db.refresh(news)

    return news