from sqlalchemy.orm import Session

from app.models.ai_recommendation import (
    AIRecommendation
)

from app.models.topic_progress import (
    TopicProgress
)


def generate_ai_recommendations(
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
        text = (
            f"{topic.topic_name} "
            f"mavzusi bo‘yicha "
            f"qo‘shimcha test ishlang"
        )

        recommendation = AIRecommendation(
            user_id=user_id,
            recommendation_text=text
        )

        db.add(recommendation)

        recommendations.append(
            recommendation
        )

    db.commit()

    return recommendations