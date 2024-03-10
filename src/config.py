from pydantic_settings import BaseSettings
import datetime


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    TELEGRAM_TOKEN: str
    TIMEZONE: str = 'Europe/Kiev'

    START_DATE_EXCEL: datetime.date = datetime.date(year=2024, month=3, day=4)

    @property
    def db_uri_asyncpg(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()