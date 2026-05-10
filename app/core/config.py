from pydantic_settings import (
    BaseSettings
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

    class Config:
        env_file = ".env"


settings = Settings()