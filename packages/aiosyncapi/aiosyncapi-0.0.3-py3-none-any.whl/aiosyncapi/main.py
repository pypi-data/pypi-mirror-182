import time

# import anyio
# from asyncer import asyncify

from aiosyncapi.types import AioapiConfig


def do_sync_work(name: str):
    time.sleep(1)
    return f"Hello, {name}"


# async def main():
#     message = await asyncify(do_sync_work)(name="World")
#     print(message)


class Aioapi:
    """combines all the parts of the asyncapi schema"""

    def __init__(self, config: AioapiConfig) -> None:
        print(config.dict())


aioapi: Aioapi = Aioapi(
    config=AioapiConfig(
        api_title="First asyncapi",
    )
)
