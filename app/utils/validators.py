import re


def validate_full_name(
    full_name: str
):
    full_name = full_name.strip()

    if len(full_name) < 5:
        return False

    pattern = r"^[A-Za-z ]+$"

    if not re.match(
        pattern,
        full_name
    ):
        return False

    words = full_name.split()

    if len(words) < 2:
        return False

    for word in words:
        if len(word) < 2:
            return False

    return True