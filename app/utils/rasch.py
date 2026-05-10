def estimate_theta(
    correct_answers: int,
    total_questions: int
):
    if total_questions <= 0:
        return 0

    ratio = correct_answers / total_questions

    return round(
        (ratio * 6) - 3,
        2
    )