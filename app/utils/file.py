import os


def get_file_extension(
    filename: str
):
    return os.path.splitext(
        filename
    )[1]


def is_pdf(
    filename: str
):
    return (
        get_file_extension(
            filename
        ).lower() == ".pdf"
    )