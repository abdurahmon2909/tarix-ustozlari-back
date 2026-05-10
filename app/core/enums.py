from enum import Enum


class QuestionTypeEnum(
    str,
    Enum
):
    MCQ = "mcq"

    MATCHING = "matching"

    CHRONOLOGY = "chronology"

    MAP = "map"

    OPEN_ANSWER = "open_answer"

    TABLE_ANALYSIS = (
        "table_analysis"
    )


class DifficultyEnum(
    str,
    Enum
):
    EASY = "easy"

    MEDIUM = "medium"

    HARD = "hard"