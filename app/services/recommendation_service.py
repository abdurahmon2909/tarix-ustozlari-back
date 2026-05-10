from sqlalchemy.orm import Session

from app.models.topic_progress import (
    TopicProgress
)


def generate_recommendations(
    db: Session,
    user_id: int
):
    weak_topics = db.query(
        TopicProgress
    ).filter(
        TopicProgress.user_id == user_id,
        TopicProgress.mastery_percentage < 60
    ).all()

    recommendations = []

    for topic in weak_topics:
        recommendations.append({
            "topic": topic.topic_name,
            "message": (
                f"{topic.topic_name} "
                f"mavzusini qayta ishlang"
            )
        })

    return recommendations