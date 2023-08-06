"""
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class CharacterAttribute(BaseModel):
  """A data model for a character attribute.
  """

  charisma: int = Field(description="Character attribute value for charisma.")
  intelligence: int = Field(
      description="Character attribute value for intelligence.")
  memory: int = Field(description="Character attribute value for memory.")
  perception: int = Field(
      description="Character attribute value for perception.")
  willpower: int = Field(description="Character attribute value for willpower.")
  accrued_remap_cooldown_date: Optional[datetime] = Field(
      None,
      description=
      "Neural remapping cooldown after a character uses remap accrued over time"
  )
  bonus_remaps: int = Field(0, description="Number of remainder bonus remaps")
  last_remap_date: Optional[datetime] = Field(None, description="the date when the last remap was executed")
