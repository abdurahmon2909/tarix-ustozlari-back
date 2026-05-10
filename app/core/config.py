from pydantic_settings import (
    BaseSettings
)

from pydantic_settings import (
    SettingsConfigDict
)


class Settings(BaseSettings):
    PROJECT_NAME: str = (
        "Tarix Backend"
    )

    DATABASE_URL: str

    SECRET_KEY: str

    BOT_TOKEN: str

    REDIS_HOST: str = (
        "localhost"
    )

    REDIS_PORT: int = 6379

    model_config = (
        SettingsConfigDict(
            env_file=".env",
            extra="ignore"
        )
    )


settings = Settings()