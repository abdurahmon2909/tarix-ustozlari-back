def process_ocr(
    image_path: str
):
    return {
        "status": "ocr_started",
        "path": image_path
    }