import os

from uuid import uuid4


UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


def save_uploaded_file(
    file,
    folder: str = "general"
):
    folder_path = os.path.join(
        UPLOAD_DIR,
        folder
    )

    os.makedirs(
        folder_path,
        exist_ok=True
    )

    extension = (
        file.filename.split(".")[-1]
    )

    filename = (
        f"{uuid4()}.{extension}"
    )

    file_path = os.path.join(
        folder_path,
        filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:
        buffer.write(
            file.file.read()
        )

    return file_path