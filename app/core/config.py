from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    POSTGRES_DATABASE_URL: str = Field(..., env="POSTGRES_URL")
    POSTGRES_USER: str = Field(..., env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(..., env="POSTGRES_PASSWORD")
    POSTGRES_HOST: str = Field(..., env="POSTGRES_HOST")
    POSTGRES_DB_NAME: str = Field(..., env="POSTGRES_DB")
    RESET_PASSWORD_SECRET_TOKEN: str = Field(..., env="RESET_PASSWORD_SECRET_TOKEN")
    USER_VERIFICATION_SECRET_TOKEN: str = Field(
        ..., env="USER_VERIFICATION_SECRET_TOKEN"
    )
    JWT_STRATEGY_SECRET: str = Field(..., env="JWT_STRATEGY_SECRET")
    API_V1_PREFIX: str = Field(..., env="API_V1_PREFIX")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
