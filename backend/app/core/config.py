from functools import lru_cache
from pydantic import AnyUrl, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    project_name: str = Field("Stock Analytics API", validation_alias="PROJECT_NAME")
    environment: str = Field("local", validation_alias="ENVIRONMENT")
    api_v1_prefix: str = Field("/api/v1", validation_alias="API_V1_PREFIX")
    secret_key: str = Field("change-me", validation_alias="SECRET_KEY")
    log_level: str = Field("INFO", validation_alias="LOG_LEVEL")
    database_url: AnyUrl = Field(
        "mysql+pymysql://user:password@localhost:3306/stock_analytics",
        validation_alias="DATABASE_URL",
    )
    cors_origins: list[str] = Field(default_factory=lambda: ["*"])
    version: str = "0.1.0"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


@lru_cache
def get_settings() -> Settings:
    return Settings()  # pragma: no cover


settings = get_settings()
