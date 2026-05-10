import qrcode


def create_qr(data: str, path: str):
    img = qrcode.make(data)

    img.save(path)

    return path