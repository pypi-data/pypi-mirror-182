"""
"""

from typing import Optional
from evergate._internal.tokenstorage import TokenStorage
from evergate._internal.requesting import get_from_esi, post_to_esi
from evergate.datamodel.blueprint import Blueprint
from evergate.datamodel.character import (Character, CharacterAffiliation,
                                          CharacterMedal, CharacterPortrait,
                                          CharacterRoles, CharacterStanding,
                                          CharacterTitle, CorporationHistory,
                                          JumpFatigue)
from evergate.datamodel.agent import AgentResearch
from evergate.datamodel.notification import ContactNotification, Notification


def get_character_affiliations(
    character_ids: list[int]) -> list[CharacterAffiliation]:
  """Get the corporation and alliance affiliations for a list of character ids.

  Args:
    character_ids (list[int]): A list of character ids.

  Returns:
    list[CharacterAffiliation]: A list of CharacterAffiliation objects.
  """
  res = post_to_esi("/characters/affiliation/", body=character_ids)
  return [CharacterAffiliation(**affiliation) for affiliation in res]


def get_character(character_id: int) -> Character:
  """Get the character information for a character id.

  Args:
    character_id (int): The character id.

  Returns:
    Character: A Character object.
  """

  res = get_from_esi(f"/characters/{character_id}/")
  return Character(**res)


def get_character_research(character_id: int) -> AgentResearch:
  """Get the research information for a character id.

  Args:
    character_id (int): The character id.

  Returns:
    AgentResearch: An AgentResearch object.
  """

  res = get_from_esi(f"/characters/{character_id}/agents_research/",
                     token=TokenStorage().get())
  return [AgentResearch(**research) for research in res]


def get_character_blueprints(character_id: int,
                             page: Optional[int] = None) -> list[Blueprint]:
  """Get the blueprints for a character id.

  Args:
    character_id (int): The character id.

  Returns:
    list[Blueprint]: A list of Blueprint objects.
  """

  res = get_from_esi(f"/characters/{character_id}/blueprints/",
                     query={"page": page},
                     token=TokenStorage().get())
  return [Blueprint(**blueprint) for blueprint in res]


def get_corporation_histories(character_id: int) -> list[CorporationHistory]:
  """Get the corporation histories for a character id.

  Args:
    character_id (int): The character id.

  Returns:
    list[CorporationHistory]: A list of corporation histories.
  """

  res = get_from_esi(f"/characters/{character_id}/corporationhistory/")
  return [CorporationHistory(**history) for history in res]


def calculate_cspa_charge(character_id: int, characters: list[int]) -> int:
  """Calculate the charge of CONCORD Spam Prevention Act for sending messages to the characters.

  Args:
    character_id (int): The id of character to send messages from.
    characters (list[int]): A list of character ids to send messages to.

  Returns:
    int: The aggregated charge of CONCORD Spam Prevention Act.
  """

  res = post_to_esi(f"/characters/{character_id}/cspa/",
                    token=TokenStorage().get(),
                    body=characters)
  return res


def get_character_jump_fatigue(character_id: int) -> JumpFatigue:
  """Get the jump fatigue information for a character id.

  Args:
    character_id (int): The character id.

  Returns:
    JumpFatigue: information about the jump fatigue of the character.
  """

  res = get_from_esi(f"/characters/{character_id}/fatigue/",
                     token=TokenStorage().get())
  return JumpFatigue(**res)


def get_character_medals(character_id: int) -> list[CharacterMedal]:
  """Get the medals that a character has.

  Args:
    character_id (int): The character id.

  Returns:
    list[CharacterMedal]: A list of Medal objects.
  """

  res = get_from_esi(f"/characters/{character_id}/medals/",
                     token=TokenStorage().get())
  return [CharacterMedal(**medal) for medal in res]


def get_character_notifications(character_id: int) -> list[Notification]:
  """Get the notifications for a character id.

  Args:
    character_id (int): The character id.

  Returns:
    list[Notification]: A list of Notification objects.
  """

  res = get_from_esi(f"/characters/{character_id}/notifications/",
                     token=TokenStorage().get())
  return [Notification(**notification) for notification in res]


def get_character_contact_notifications(
    character_id: int) -> list[ContactNotification]:
  """Get the contact notifications for a character id.

  Args:
    character_id (int): The character id.

  Returns:
    list[ContactNotification]: A list of Notification objects.
  """

  res = get_from_esi(f"/characters/{character_id}/notifications/contacts/",
                     token=TokenStorage().get())
  return [ContactNotification(**notification) for notification in res]


def get_character_portrait(character_id: int) -> CharacterPortrait:
  """Get the portrait url for a character id.

  Args:
    character_id (int): The character id.

  Returns:
    CharacterPortrait: The urls of the portrait.
  """

  res = get_from_esi(f"/characters/{character_id}/portrait/")
  return CharacterPortrait(**res)


def get_character_roles(character_id: int) -> CharacterRoles:
  """Get the roles for a character id.

  Args:
    character_id (int): The character id.

  Returns:
    CharacterRoles: A dictionary containing the roles.
  """

  res = get_from_esi(f"/characters/{character_id}/roles/",
                     token=TokenStorage().get())
  return CharacterRoles(**res)


def get_character_standings(character_id: int) -> list[CharacterStanding]:
  """Get the standings for a character id.

  Args:
    character_id (int): The character id.

  Returns:
    list[CharacterStanding]: A list of Standing objects.
  """

  res = get_from_esi(f"/characters/{character_id}/standings/",
                     token=TokenStorage().get())
  return [CharacterStanding(**standing) for standing in res]


def get_character_titles(character_id: int) -> list[CharacterTitle]:
  """Get the titles for a character id.

  Args:
    character_id (int): The character id.

  Returns:
    list[CharacterTitle]: A list of CharacterTitle objects.
  """

  res = get_from_esi(f"/characters/{character_id}/titles/",
                     token=TokenStorage().get())
  return [CharacterTitle(**title) for title in res]
