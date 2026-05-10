def calculate_percentage(
    correct_answers: int,
    total_questions: int
):
    if total_questions <= 0:
        return 0

    percentage = (
        correct_answers / total_questions
    ) * 100

    return round(
        percentage,
        2
    )


def calculate_xp(
    correct_answers: int,
    total_questions: int
):
    percentage = calculate_percentage(
        correct_answers,
        total_questions
    )

    if percentage >= 90:
        return 100

    if percentage >= 80:
        return 80

    if percentage >= 70:
        return 60

    if percentage >= 60:
        return 40

    return 20


def calculate_sharaf(
    won: bool
):
    return 25 if won else -10