"""
"""

from typing import Optional, Self


class TokenStorage:
  __slots__ = ("__tokens", "__default")

  _instance: Optional['TokenStorage'] = None

  def __new__(cls: type[Self]) -> Self:
    if cls._instance is None:
      cls._instance = super().__new__(cls)
      cls._instance.__init__()

    return cls._instance

  def __init__(self) -> None:
    self.__tokens = {}
    self.__default = None

  def get(self) -> str:
    if self.__default is None:
      raise ValueError("No default token is set.")

    if self.__default not in self.__tokens:
      raise ValueError("No token with the default character name is set.")

    return self.__tokens[self.__default]

  def add_token(self, character_name: str, token: str) -> None:
    self.__tokens[character_name] = token

  def expire_token(self, character_name: str) -> None:
    self.__tokens.pop(character_name)

  def set_default_character_name(self, character_name: str) -> None:
    self.__default = character_name

  def get_default_character_name(self) -> Optional[str]:
    return self.__default
