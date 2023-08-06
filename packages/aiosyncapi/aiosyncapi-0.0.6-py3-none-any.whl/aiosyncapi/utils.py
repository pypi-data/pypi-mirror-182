import datetime
import re
import time

import orjson
from pydantic import BaseModel as PydanticBase


def to_camel(string: str) -> str:
    split_string = string.split("_")
    if len(split_string) > 1:
        word_list = [split_string[0].lower()]
        for word in split_string[1:]:
            word_list.append(word.capitalize())
        string = "".join(word_list)
    return string


def snake_case(any_string: str):
    """method to camel case to snake case"""
    any_string = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", any_string)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", any_string).lower()


def title_case(any_string: str) -> str:
    split_string = any_string.split("_")
    if len(split_string) > 1:
        word_list = []
        for word in split_string:
            word_list.append("{word} ".format(word=word.capitalize()))
        any_string = "".join(word_list)
    else:
        any_string = any_string.capitalize()
    return any_string.strip()


def snake2camel(snake: str, start_lower: bool = False) -> str:
    camel = snake.title()
    camel = re.sub("([0-9A-Za-z])_(?=[0-9A-Z])", lambda m: m.group(1), camel)
    if start_lower:
        camel = re.sub("(^_*[A-Z])", lambda m: m.group(1).lower(), camel)
    return camel


def to_no_underscore(string: str) -> str:
    if string:
        split_string = string.split("_")
        if len(split_string) > 1:
            word_list = []
            for word in split_string:
                word_list.append("{word} ".format(word=word.capitalize()))
            string = "".join(word_list)
        else:
            string = string.capitalize()
    return string


class BaseModel(PydanticBase):
    class Config:
        """base pydantic config"""

        alias_generator = to_camel
        arbitrary_types_allowed = True
        use_enum_values = True
        json_loads = orjson.loads
        json_dumps = orjson.dumps
        allow_population_by_field_name = True
        smart_union = True
        json_encoders = {
            datetime.datetime: lambda v: round(v.timestamp()) * 1000,
            datetime.date: lambda v: round(time.mktime(v.timetuple())) * 1000,
        }
