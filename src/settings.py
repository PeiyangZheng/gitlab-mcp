from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Backwards-compatible field name used elsewhere in the project
    gitlabapi_key: str | None = None

    # New, explicit configuration fields
    GITLAB_URL: str = "https://gitlab.com"
    GITLAB_TOKEN: str = "glpat-vMEuBerXF9_-hVl4mqt8Bm86MQp1Omkwcnp1Cw.01.121p4fkk9"

    BIND_ADDRESS: str = "127.0.0.1"
    BIND_PORT: int = 8000

    # GitLab client tuning
    GITLAB_PER_PAGE: int = 100
    GITLAB_TIMEOUT: int = 30

    gitlab_personal_access_token: str | None = None
    gitlab_api_url: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()

# Backwards compatibility: if only `gitlabapi_key` is set in .env, copy it to GITLAB_TOKEN
if not settings.GITLAB_TOKEN and settings.gitlabapi_key:
    settings.GITLAB_TOKEN = settings.gitlabapi_key
