import re


def normalize_text(
    text: str
):
    text = text.lower()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()