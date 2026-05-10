def calculate_percentile(
    user_score: float,
    all_scores: list[float]
):
    if not all_scores:
        return 0

    below = len([
        score
        for score in all_scores
        if score < user_score
    ])

    percentile = (
        below / len(all_scores)
    ) * 100

    return round(
        percentile,
        2
    )