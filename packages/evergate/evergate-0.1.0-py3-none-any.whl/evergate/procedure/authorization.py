"""
"""

from evergate._internal.tokenstorage import TokenStorage


def add_token(character_name: str,
              token: str,
              set_as_default: bool = False) -> None:
  """Adds a token to the token storage.

  Args:
    character_name (str): A name of the character.
    token (str): A token of the character.
    set_as_default (bool, optional): Sets the token as the default token. Defaults to False.
  """

  ts = TokenStorage()
  ts.add_token(character_name, token)

  if set_as_default or TokenStorage.get_default_character_name() is None:
    TokenStorage.set_default_character_name(character_name)


def expire_token(character_name: str) -> None:
  """Expires a token in the token storage.

  Args:
    character_name (str): A name of the character.
  """

  TokenStorage().expire_token(character_name)
