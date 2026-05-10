import random
import string

from sqlalchemy.orm import Session

from app.models.quiz_room import QuizRoom

from app.models.quiz_room_player import (
    QuizRoomPlayer
)


def generate_room_code():
    return "".join(
        random.choices(
            string.ascii_uppercase
            + string.digits,
            k=6
        )
    )


def create_room(
    db: Session,
    title: str,
    owner_user_id: int,
    max_players: int = 50,
):
    room_code = generate_room_code()

    room = QuizRoom(
        title=title,
        room_code=room_code,
        owner_user_id=owner_user_id,
        max_players=max_players,
    )

    db.add(room)

    db.commit()

    db.refresh(room)

    return room


def join_room(
    db: Session,
    room_code: str,
    user_id: int,
):
    room = db.query(
        QuizRoom
    ).filter(
        QuizRoom.room_code == room_code
    ).first()

    if not room:
        return None

    player_count = db.query(
        QuizRoomPlayer
    ).filter(
        QuizRoomPlayer.room_id == room.id
    ).count()

    if player_count >= room.max_players:
        return None

    existing = db.query(
        QuizRoomPlayer
    ).filter(
        QuizRoomPlayer.room_id == room.id,
        QuizRoomPlayer.user_id == user_id
    ).first()

    if existing:
        return existing

    player = QuizRoomPlayer(
        room_id=room.id,
        user_id=user_id,
    )

    db.add(player)

    db.commit()

    db.refresh(player)

    return player