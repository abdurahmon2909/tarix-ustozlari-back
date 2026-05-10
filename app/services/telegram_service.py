import hashlib
import hmac

from urllib.parse import (
    parse_qsl
)

from app.core.config import (
    settings
)


def validate_telegram_auth(
    init_data: str
):
    parsed_data = dict(
        parse_qsl(init_data)
    )

    received_hash = parsed_data.pop(
        "hash",
        None
    )

    data_check_string = "\n".join(
        [
            f"{k}={v}"
            for k, v in sorted(
                parsed_data.items()
            )
        ]
    )

    secret_key = hashlib.sha256(
        settings.BOT_TOKEN.encode()
    ).digest()

    calculated_hash = hmac.new(
        secret_key,

        data_check_string.encode(),

        hashlib.sha256
    ).hexdigest()

    return (
        calculated_hash
        == received_hash
    )