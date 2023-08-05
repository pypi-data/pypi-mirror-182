from dataclasses import dataclass

from telebox.bot.types.type import Type


@dataclass(unsafe_hash=True)
class WebAppInfo(Type):
    url: str
