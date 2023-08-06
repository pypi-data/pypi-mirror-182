import time

from .models import AioapiConfig

# import anyio
# from asyncer import asyncify


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
