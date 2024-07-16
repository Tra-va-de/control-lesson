from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    REDIS_URL: str
    CACHE_EXPIRE_IN_SECONDS: int = 300  # 5 минут
    TEST_DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()