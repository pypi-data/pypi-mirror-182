"""
"""

from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class CharacterAffiliation(BaseModel):
  """A data model for a character's affiliation.

  Attributes:
    character_id (int): An id of the character.
    corporation_id (int): An id of the character's corporation.
    alliance_id (int): An id of the character's alliance.
    faction_id (int): An id of the faction that this character is fighting for.
  """
  character_id: int = Field(description="An id of the character.")
  corporation_id: int = Field(
      description="An id of the character's corporation.")
  alliance_id: Optional[int] = Field(
      description="An id of the character's alliance.")
  faction_id: Optional[int] = Field(
      None,
      description="An id of the faction that this alliance is fighting for.")


class CharacterGender(str, Enum):
  """Gender types of a character.
  """
  male = "male"
  female = "female"


class Character(BaseModel):
  """A data model for a character on EVE Online.

  Attributes:
    alliance_id (Optional[int]): An id of the alliance that this character is in.
    birthday (str): The birthday of this character.
    bloodline_id (int): An id of this character's bloodline.
    corporation_id (int): An id of the corporation that this character is in.
    description (str): The description of this character.
    faction_id (Optional[int]): An id of the faction that this character is fighting for.
    gender (CharacterGender): the gender of this character.
    name (str): The name of this character.
    race_id (int): An id of the race of this character.
    security_status (float): The security status of this character.
    title (str): The individual title of this character.
  """

  alliance_id: Optional[int] = Field(
      None, description="An id of the alliance that this character is in.")
  birthday: datetime = Field(description="The birthday of this character.")
  bloodline_id: int = Field(description="An id of this character's bloodline.")
  corporation_id: int = Field(
      description="An id of the corporation that this character is in.")
  description: str = Field("", description="The description of this character.")
  faction_id: Optional[int] = Field(
      None,
      description="An id of the faction that this character is fighting for.")
  gender: CharacterGender = Field(description="the gender of this character.")
  name: str = Field(description="The name of this character.")
  race_id: int = Field(description="An id of the race of this character.")
  security_status: float = Field(
      0.0, description="The security status of this character.")
  title: str = Field("", description="The individual title of this character.")


class CorporationHistory(BaseModel):
  """A data model for a character's corporation history.

  Attributes:
    corporation_id (int): An id of the corporation.
    is_deleted (bool): Whether the corporation is deleted.
    record_id (int): An incrementing ID that can be used to canonically establish order of records in cases where dates may be ambiguous.
    start_date (str): The timestamp when the character joined the corporation.
  """

  corporation_id: int = Field(description="An id of the corporation.")
  is_deleted: bool = Field(False,
                           description="Whether the corporation is deleted.")
  record_id: int = Field(
      description=
      "An incrementing ID that can be used to canonically establish order of records in cases where dates may be ambiguous."
  )
  start_date: datetime = Field(
      description="The timestamp when the character joined the corporation.")


class JumpFatigue(BaseModel):
  """A data model for information about a character's jump fatigue.

  Attributes:
    jump_fatigue_expire_date (Optional[str]): The datetime when the current jump fatigue expires.
    last_jump_date (Optional[str]): The datetime when the last jump was made.
    last_update_date (Optional[str]): The datetime when the last jump fatigue updated.
  """

  jump_fatigue_expire_date: Optional[datetime] = Field(
      None, description="The datetime when the current jump fatigue expires.")
  last_jump_date: Optional[datetime] = Field(
      None, description="The datetime when the last jump was made.")
  last_update_date: Optional[datetime] = Field(
      None, description="The datetime when the last jump fatigue updated.")


class MedalGraphic(BaseModel):
  """A data model for a medal's graphic.

  Attributes:
    color (int): The color of the medal.
    graphic (str): The graphic of the medal.
    layer (int): The layer of the medal.
    part (int): The part of the medal.
  """

  color: int = Field(-1, description="The color of the medal.")
  graphic: str = Field(description="The graphic of the medal.")
  layer: int = Field(description="The layer of the medal.")
  part: int = Field(description="The part of the medal.")


class MetalStatus(str, Enum):
  """Status types of a medal.
  """
  private = "private"
  public = "public"


class CharacterMedal(BaseModel):
  """A data model for a character's medal.

  Attributes:
    character_id (int): An id of the character.
    corporation_id (int): An id of the corporation that issued the medal.
    date (str): The datetime when the medal was issued.
    description (str): The description of the medal.
    graphics (list[MedalGraphic]): The graphics of the medal.
    issuer_id (int): An id of the issuer of the medal.
    medal_id (int): An id of the medal.
    reason (str): The reason the medal to be granted.
    status (MetalStatus): The status of the medal.
    title (str): The title of the medal.
  """

  corporation_id: int = Field(
      description="An id of the corporation that issued the medal.")
  date: datetime = Field(description="The datetime when the medal was issued.")
  description: str = Field(description="The description of the medal.")
  graphics: list[MedalGraphic] = Field(description="The graphics of the medal.")
  issuer_id: int = Field(description="An id of the issuer of the medal.")
  medal_id: int = Field(description="An id of the medal.")
  reason: str = Field(description="The reason the medal to be granted.")
  status: MetalStatus = Field(description="The status of the medal.")
  title: str = Field(description="The title of the medal.")


class CharacterPortrait(BaseModel):
  """A data model for a character's portrait.

  Attributes:
    px64x64 (str): The 64px square image of the portrait of the character.
    px128x128 (str): The 128px square image of the portrait of the character.
    px256x256 (str): The 256px square image of the portrait of the character.
    px512x512 (str): The 512px square image of the portrait of the character.
  """

  px64x64: str = Field(
      description="The 64px square image of the portrait of the character.")
  px128x128: str = Field(
      description="The 128px square image of the portrait of the character.")
  px256x256: str = Field(
      description="The 256px square image of the portrait of the character.")
  px512x512: str = Field(
      description="The 512px square image of the portrait of the character.")


class RoleType(str, Enum):
  """The role types of a character.
  """

  Account_Take_1 = "Account_Take_1"
  Account_Take_2 = "Account_Take_2"
  Account_Take_3 = "Account_Take_3"
  Account_Take_4 = "Account_Take_4"
  Account_Take_5 = "Account_Take_5"
  Account_Take_6 = "Account_Take_6"
  Account_Take_7 = "Account_Take_7"
  Accountant = "Accountant"
  Auditor = "Auditor"
  Communications_Officer = "Communications_Officer"
  Config_Equipment = "Config_Equipment"
  Config_Starbase_Equipment = "Config_Starbase_Equipment"
  Container_Take_1 = "Container_Take_1"
  Container_Take_2 = "Container_Take_2"
  Container_Take_3 = "Container_Take_3"
  Container_Take_4 = "Container_Take_4"
  Container_Take_5 = "Container_Take_5"
  Container_Take_6 = "Container_Take_6"
  Container_Take_7 = "Container_Take_7"
  Contract_Manager = "Contract_Manager"
  Diplomat = "Diplomat"
  Director = "Director"
  Factory_Manager = "Factory_Manager"
  Fitting_Manager = "Fitting_Manager"
  Hangar_Query_1 = "Hangar_Query_1"
  Hangar_Query_2 = "Hangar_Query_2"
  Hangar_Query_3 = "Hangar_Query_3"
  Hangar_Query_4 = "Hangar_Query_4"
  Hangar_Query_5 = "Hangar_Query_5"
  Hangar_Query_6 = "Hangar_Query_6"
  Hangar_Query_7 = "Hangar_Query_7"
  Hangar_Take_1 = "Hangar_Take_1"
  Hangar_Take_2 = "Hangar_Take_2"
  Hangar_Take_3 = "Hangar_Take_3"
  Hangar_Take_4 = "Hangar_Take_4"
  Hangar_Take_5 = "Hangar_Take_5"
  Hangar_Take_6 = "Hangar_Take_6"
  Hangar_Take_7 = "Hangar_Take_7"
  Junior_Accountant = "Junior_Accountant"
  Personnel_Manager = "Personnel_Manager"
  Rent_Factory_Facility = "Rent_Factory_Facility"
  Rent_Office = "Rent_Office"
  Rent_Research_Facility = "Rent_Research_Facility"
  Security_Officer = "Security_Officer"
  Starbase_Defense_Operator = "Starbase_Defense_Operator"
  Starbase_Fuel_Technician = "Starbase_Fuel_Technician"
  Station_Manager = "Station_Manager"
  Trader = "Trader"


class CharacterRoles(BaseModel):
  """A data model for a character's roles.

  Attributes:
    roles (list[RoleType]): The roles of the character.
    roles_at_base (list[RoleType]): The roles at base of the character.
    roles_at_hq (list[RoleType]): The roles at HQ of the character.
    roles_at_other (list[RoleType]): The roles at other of the character.
  """

  roles: Optional[list[RoleType]] = Field(
      None, description="The roles of the character.")
  roles_at_base: Optional[list[RoleType]] = Field(
      None, description="The roles at base of the character.")
  roles_at_hq: Optional[list[RoleType]] = Field(
      None, description="The roles at HQ of the character.")
  roles_at_other: Optional[list[RoleType]] = Field(
      None, description="The roles at other of the character.")


class StandingType(str, Enum):
  """The standing types of a character.
  """

  agent = "agent"
  npc_corp = "npc_corp"
  faction = "faction"


class CharacterStanding(BaseModel):
  """A data model for a character's standing.

  Attributes:
    from_id (int): An id of the entity that the character has a standing with.
    from_type (str): The type of the entity that the character has a standing
      with.
    standing (float): The standing of the character with the entity.
  """

  from_id: int = Field(
      description="An id of the entity that the character has a standing with.")
  from_type: StandingType = Field(
      description=
      "The type of the entity that the character has a standing with.")
  standing: float = Field(
      description="The standing of the character with the entity.")


class CharacterTitle(BaseModel):
  """A data model for a character's title.

  Attributes:
    name (str): The name of the title.
    title_id (int): The id of the title.
  """

  name: str = Field(description="The name of the title.")
  title_id: int = Field(description="The id of the title.")
