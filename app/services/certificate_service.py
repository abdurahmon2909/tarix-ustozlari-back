import qrcode


def generate_qr_code(data: str, file_path: str):
    qr = qrcode.make(data)

    qr.save(file_path)

    return file_path