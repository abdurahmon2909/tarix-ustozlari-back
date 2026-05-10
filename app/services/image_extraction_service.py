import fitz
import os


def extract_images_from_pdf(
    pdf_path: str,
    output_folder: str
):
    document = fitz.open(pdf_path)

    os.makedirs(
        output_folder,
        exist_ok=True
    )

    saved_images = []

    for page_index in range(
        len(document)
    ):
        page = document[page_index]

        images = page.get_images(
            full=True
        )

        for image_index, img in enumerate(images):
            xref = img[0]

            base_image = document.extract_image(
                xref
            )

            image_bytes = base_image["image"]

            image_ext = base_image["ext"]

            image_name = (
                f"page_{page_index + 1}_"
                f"{image_index}.{image_ext}"
            )

            image_path = os.path.join(
                output_folder,
                image_name
            )

            with open(
                image_path,
                "wb"
            ) as f:
                f.write(image_bytes)

            saved_images.append(
                image_path
            )

    return saved_images