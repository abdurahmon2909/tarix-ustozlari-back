from sqlalchemy.orm import Session

from app.models.system_setting import (
    SystemSetting
)


def get_setting(
    db: Session,
    key: str
):
    return db.query(
        SystemSetting
    ).filter(
        SystemSetting.key == key
    ).first()


def set_setting(
    db: Session,
    key: str,
    value: str,
    description: str | None = None,
):
    setting = get_setting(
        db=db,
        key=key
    )

    if setting:
        setting.value = value

        if description:
            setting.description = description

    else:
        setting = SystemSetting(
            key=key,
            value=value,
            description=description,
        )

        db.add(setting)

    db.commit()

    db.refresh(setting)

    return setting