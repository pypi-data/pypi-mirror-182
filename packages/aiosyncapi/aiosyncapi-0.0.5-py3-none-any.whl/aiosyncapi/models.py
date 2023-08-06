from pydantic import BaseModel

from aiosyncapi.utils import Config


class AioapiConfig(BaseModel, Config):
    api_title: str
    api_version: str = "0.0.1"
