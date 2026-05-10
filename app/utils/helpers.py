from uuid import uuid4


def generate_file_name(
    extension: str
):
    return f"{uuid4()}.{extension}"