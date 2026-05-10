import os

from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile

from app.services.pdf_service import (
    extract_text_from_pdf
)

from app.services.book_parser_service import (
    analyze_book_text
)

from app.services.question_import_service import (
    parse_questions_from_text
)

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):
    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:
        buffer.write(
            await file.read()
        )

    extracted_text = extract_text_from_pdf(
        file_path
    )

    return {
        "filename": file.filename,
        "text_length": len(extracted_text),
    }


@router.post("/analyze-book")
async def analyze_book(
    file: UploadFile = File(...)
):
    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:
        buffer.write(
            await file.read()
        )

    extracted_text = extract_text_from_pdf(
        file_path
    )

    analysis = await analyze_book_text(
        extracted_text
    )

    return {
        "analysis": analysis
    }


@router.post("/import-questions")
async def import_questions(
    file: UploadFile = File(...)
):
    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as buffer:
        buffer.write(
            await file.read()
        )

    extracted_text = extract_text_from_pdf(
        file_path
    )

    questions = await parse_questions_from_text(
        extracted_text
    )

    return {
        "questions": questions
    }