from random import randint


def generate_battle_result():
    return {
        "user_score": randint(0, 100),
        "opponent_score": randint(0, 100),
    }