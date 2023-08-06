""""""

from typing import Optional
from evergate._internal.requesting import get_from_esi, post_to_esi, put_to_esi, delete_from_esi
from evergate._internal.tokenstorage import TokenStorage
from evergate.datamodel.contact import Contact, ContactLabel


def get_alliance_contacts(alliance_id: int,
                          page: Optional[int] = None) -> list[Contact]:
  """Gets a list of contacts of an alliance.

  Args:
    alliance_id (int): An id of the alliance.
    page (Optional[int], optional): A page number. Defaults to None.

  Returns:
    A list of contacts of an alliance.
  """

  query = None if page is None else {"page": page}

  return [
      Contact(**contact)
      for contact in get_from_esi(f"/alliances/{alliance_id}/contacts/",
                                  query=query,
                                  token=TokenStorage().get())
  ]


def get_alliance_contact_labels(alliance_id: int) -> list[ContactLabel]:
  """Gets a list of contact labels of an alliance.

  Args:
    alliance_id (int): An id of the alliance.

  Returns:
    A list of contact labels of an alliance.
  """

  return [
      ContactLabel(**label)
      for label in get_from_esi(f"/alliances/{alliance_id}/contacts/labels/",
                                token=TokenStorage().get())
  ]


def get_corporation_contacts(corporation_id: int,
                             page: Optional[int] = None) -> list[Contact]:
  """Gets a list of contacts of a corporation.

  Args:
    corporation_id (int): An id of the corporation.
    page (Optional[int], optional): A page number. Defaults to None.

  Returns:
    A list of contacts of a corporation.
  """

  query = None if page is None else {"page": page}

  return [
      Contact(**contact)
      for contact in get_from_esi(f"/corporations/{corporation_id}/contacts/",
                                  query=query,
                                  token=TokenStorage().get())
  ]


def get_corporation_contact_labels(corporation_id: int) -> list[ContactLabel]:
  """Gets a list of contact labels of a corporation.

  Args:
    corporation_id (int): An id of the corporation.

  Returns:
    A list of contact labels of a corporation.
  """

  return [
      ContactLabel(**label) for label in get_from_esi(
          f"/corporations/{corporation_id}/contacts/labels/",
          token=TokenStorage().get())
  ]


def get_character_contacts(character_id: int,
                           page: Optional[int] = None) -> list[Contact]:
  """Gets a list of contacts of a character.

  Args:
    character_id (int): An id of the character.
    page (Optional[int], optional): A page number. Defaults to None.

  Returns:
    A list of contacts of a character.
  """

  query = None if page is None else {"page": page}

  return [
      Contact(**contact)
      for contact in get_from_esi(f"/characters/{character_id}/contacts/",
                                  query=query,
                                  token=TokenStorage().get())
  ]


def get_character_contact_labels(character_id: int) -> list[ContactLabel]:
  """Gets a list of contact labels of a character.

  Args:
    character_id (int): An id of the character.

  Returns:
    A list of contact labels of a character.
  """

  return [
      ContactLabel(**label)
      for label in get_from_esi(f"/characters/{character_id}/contacts/labels/",
                                token=TokenStorage().get())
  ]


def delete_character_contacts(character_id: int,
                              contact_ids: list[int]) -> None:
  """Deletes contacts of a character.

  Args:
    character_id (int): An id of the character.
    contact_ids (list[int]): A list of contact ids.
  """

  delete_from_esi(f"/characters/{character_id}/contacts/",
                  query={"contact_ids": contact_ids},
                  token=TokenStorage().get())


def post_character_contacts(character_id: int,
                            contact_ids: list[int],
                            standing: float,
                            label_ids: Optional[list[int]] = None,
                            watched: Optional[bool] = None) -> None:
  """Creates new contacts of a character.

  Args:
    character_id (int): An id of the character.
    contact_ids (list[int]): A list of ids of entities to be added for contacts.
    standing (float): A standing of the new contact.
    label_ids (Optional[list[int]], optional): A list of label ids. Defaults to None.
    watched (Optional[bool], optional): A flag indicating if the new contact should be watched. Defaults to None.
  """

  post_to_esi(f"/characters/{character_id}/contacts/",
              query={
                  'label_ids': label_ids,
                  standing: standing,
                  'watched': watched,
              },
              body=contact_ids,
              token=TokenStorage().get())


def put_character_contacts(character_id: int,
                           contact_ids: list[int],
                           standing: float,
                           label_ids: Optional[list[int]] = None,
                           watched: Optional[bool] = None) -> None:
  """Updates contacts of a character.

  Args:
    character_id (int): An id of the character.
    contact_ids (list[int]): A list of ids of entities of existing contacts to be updated.
    standing (float): A standing of the new contact.
    label_ids (Optional[list[int]], optional): A list of label ids. Defaults to None.
  """

  put_to_esi(f"/characters/{character_id}/contacts/",
             query={
                 'label_ids': label_ids,
                 standing: standing,
                 'watched': watched,
             },
             body=contact_ids,
             token=TokenStorage().get())
