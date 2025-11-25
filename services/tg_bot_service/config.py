from pydantic_settings import BaseSettings


class TG(BaseSettings):
    token: str

    class Config:
        env_prefix = "TG_"


class FakeLLM(BaseSettings):
    base_url: str

    class Config:
        env_prefix = "LLM_"


class Config(BaseSettings):
    tg: TG = TG()
    fake_llm: FakeLLM = FakeLLM()

    class Config:
        env_prefix = "APP_"


config = Config()
