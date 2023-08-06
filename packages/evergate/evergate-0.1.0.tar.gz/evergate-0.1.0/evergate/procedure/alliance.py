"""This module contains procedures for alliance-related requests.

get_alliance_ids() -> list[int]:
  Gets a list of all alliance ids.

get_alliance_by_id(alliance_id: int) -> Alliance:
  Gets an alliance by its id.

get_corporations_of_alliance(alliance_id: int) -> list[int]:
  Gets a list of corporation ids of an alliance.

get_alliance_icons(alliance_id: int) -> AllianceIcon:
  Gets a set of icon urls of an alliance.
"""

from evergate._internal.requesting import get_from_esi
from evergate.datamodel.alliance import Alliance, AllianceIcon


def get_alliance_ids() -> list[int]:
  """Gets a list of all alliance ids.

  Returns:
    A list of all alliance ids.
  """

  return get_from_esi("/alliances/")


def get_alliance_by_id(alliance_id: int) -> Alliance:
  """Gets an alliance by its id.

  Args:
    alliance_id (int): An id of the alliance.

  Returns:
    An alliance.
  """

  return Alliance(**get_from_esi(f"/alliances/{alliance_id}/"))


def get_corporations_of_alliance(alliance_id: int) -> list[int]:
  """Gets a list of corporation ids of an alliance.

  Args:
    alliance_id (int): An id of the alliance.

  Returns:
    A list of corporation ids of an alliance.
  """

  return get_from_esi(f"/alliances/{alliance_id}/corporations/")


def get_alliance_icons(alliance_id: int) -> AllianceIcon:
  """Gets a set of icon urls of an alliance.

  Args:
    alliance_id (int): An id of the alliance.

  Returns:
    A set of icon urls of an alliance.
  """

  return AllianceIcon(**get_from_esi(f"/alliances/{alliance_id}/icons/"))
