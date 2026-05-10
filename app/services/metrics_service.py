from sqlalchemy.orm import Session

from app.models.system_metric import (
    SystemMetric
)


def save_metric(
    db: Session,
    metric_name: str,
    metric_value: float,
):
    metric = SystemMetric(
        metric_name=metric_name,
        metric_value=metric_value,
    )

    db.add(metric)

    db.commit()

    db.refresh(metric)

    return metric


def get_metrics(
    db: Session
):
    return db.query(
        SystemMetric
    ).all()