def calculate_theta(
    correct_answers: int,
    total_questions: int
):
    if total_questions == 0:
        return 0

    return round(
        correct_answers / total_questions,
        2
    )