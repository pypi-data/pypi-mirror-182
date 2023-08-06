import datetime
import re
import time
from typing import Any, Optional, TypeVar

from pydantic import Field

from .utils import BaseModel

ChannelName = str


class ChannelOperation(BaseModel):
    """event definition"""

    ...


class Channel(BaseModel):
    """represents a single topic/channel/namespace(socketio)"""

    subscribe: Optional[ChannelOperation] = None
    publish: Optional[ChannelOperation] = None


class Channels(BaseModel):
    """represnt all available topics/channels/namespace(socketio) in the given api"""

    __root__: dict[ChannelName, Channel]

    def __getitem__(self, channel_name: ChannelName) -> Channel:
        return self.__root__[channel_name]


class ApiInfo(BaseModel):
    """base data for app api"""

    title: str = Field(..., description="app api title")
    version: str = Field(..., description="app api version")
    description: Optional[str] = Field(None, description="description of app api")


class Aioapi(BaseModel):
    """combines all the parts of the asyncapi schema"""

    """base data for asyncapi spec"""

    info: ApiInfo = Field(description="api base data")
    asyncapi: str = Field(default="2.5.0", description="version of the asyncapi spec")
    chanels: Channels = Field(...)
    # servers
    # components

    def __init__(self) -> None:
        ...
        # print(config.dict(by_alias=True))

    def to_schema_json(self):
        ...
