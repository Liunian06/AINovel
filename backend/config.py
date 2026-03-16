from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    gemini_api_key: str = ""
    default_ai_provider: str = "openai"
    
    class Config:
        env_file = ".env"

settings = Settings()
