from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str
    debug: bool = False
    secret_key: str

    class Config:
        env_file = ".env"


settings = Settings()