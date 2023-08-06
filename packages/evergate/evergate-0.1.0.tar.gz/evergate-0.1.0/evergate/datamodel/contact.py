"""Data models for contacts between entities on EVE Online.
"""

from enum import Enum
from pydantic import BaseModel, Field


class ContactType(str, Enum):
  character = "character"
  corporation = "corporation"
  alliance = "alliance"
  faction = "faction"


class Contact(BaseModel):
  """A data model for a contact between entities on EVE Online.

  Attributes:
    contact_id (int): An id of the entity that this contact is to.
    contact_type (ContactType): A type of the entity that this contact is to.
    label_ids (list[int]): A list of label ids applied to this contact.
    standing (float): The standing from the owner of this contact to the entity that this contact is to.
  """
  contact_id: int = Field(
      description="An id of the entity that this contact is to.")
  contact_type: ContactType = Field(
      description="A type of the entity that this contact is to.")
  label_ids: list[int] = Field(
      description="A list of label ids applied to this contact.")
  standing: float = Field(
      description=
      "The standing from the owner of this contact to the entity that this contact is to."
  )


class ContactLabel(BaseModel):
  """A data model for a label applied to a contact.

  Attributes:
    label_id (int): An id of this label.
    name (str): A name of this label.
  """
  label_id: int = Field(description="An id of this label.")
  label_name: str = Field(description="A name of this label.")
