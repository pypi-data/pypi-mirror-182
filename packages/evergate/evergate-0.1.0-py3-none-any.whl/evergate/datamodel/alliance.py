"""Data models for alliances on EVE Online.

AllianceIcon:
  A data model for a set of icons of an alliance.

Alliance:
  A data model for alliances on EVE Online.
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class AllianceIcon(BaseModel):
  """A data model for a set of icons of an alliance.

  Attributes:
    px64x64 (str): 64px square icon
    px128x128 (str): 128px square icon
  """
  px64x64: str = Field(description="64px square icon")
  px128x128: str = Field(description="128px square icon")


class Alliance(BaseModel):
  """A data model for alliances on EVE Online.

  Attributes:
    creator_corporation_id (int): An id of the corporation that created this alliance.
    creator_id (int): An id of the character that created this alliance.
    date_founded (str): Datetime when this alliance was created.
    executor_corporation_id (Optional[int]): An id of the corporation that is the current executor of this alliance. If the alliance had closed, this is set to None.
    faction_id (Optional[int]): An id of the faction that this alliance is fighting for.
    name (str): Alliance name
    ticker (str): Alliance ticker
  """

  creator_corporation_id: int = Field(
      description="An id of the corporation that created this alliance.")
  creator_id: int = Field(
      description="An id of the character that created this alliance.")
  date_founded: datetime = Field(
      description="Datetime when this alliance was created.")
  executor_corporation_id: Optional[int] = Field(
      None,
      description=
      ("An id of the corporation that is the current executor of this alliance. "
       "If the alliance had closed, this is set to None."))
  faction_id: Optional[int] = Field(
      None,
      description="An id of the faction that this alliance is fighting for.")
  name: str = Field(description="Alliance name")
  ticker: str = Field(description="Alliance ticker")
