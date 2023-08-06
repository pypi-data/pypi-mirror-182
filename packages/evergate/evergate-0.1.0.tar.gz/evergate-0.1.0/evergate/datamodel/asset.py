"""
"""
from enum import Enum

from pydantic import BaseModel, Field

from evergate.datamodel.vector import Vector3d


class BlueprintCapableLocationFlag(str, Enum):
  """Location flags to indicate the types of containers that can hold results of blueprint runs.
  """
  AutoFit = "AutoFit"
  Cargo = "Cargo"
  CorpseBay = "CorpseBay"
  DroneBay = "DroneBay"
  FleetHangar = "FleetHangar"
  Deliveries = "Deliveries"
  HiddenModifiers = "HiddenModifiers"
  Hangar = "Hangar"
  HangarAll = "HangarAll"
  LoSlot0 = "LoSlot0"
  LoSlot1 = "LoSlot1"
  LoSlot2 = "LoSlot2"
  LoSlot3 = "LoSlot3"
  LoSlot4 = "LoSlot4"
  LoSlot5 = "LoSlot5"
  LoSlot6 = "LoSlot6"
  LoSlot7 = "LoSlot7"
  MedSlot0 = "MedSlot0"
  MedSlot1 = "MedSlot1"
  MedSlot2 = "MedSlot2"
  MedSlot3 = "MedSlot3"
  MedSlot4 = "MedSlot4"
  MedSlot5 = "MedSlot5"
  MedSlot6 = "MedSlot6"
  MedSlot7 = "MedSlot7"
  HiSlot0 = "HiSlot0"
  HiSlot1 = "HiSlot1"
  HiSlot2 = "HiSlot2"
  HiSlot3 = "HiSlot3"
  HiSlot4 = "HiSlot4"
  HiSlot5 = "HiSlot5"
  HiSlot6 = "HiSlot6"
  HiSlot7 = "HiSlot7"
  AssetSafety = "AssetSafety"
  Locked = "Locked"
  Unlocked = "Unlocked"
  Implant = "Implant"
  QuafeBay = "QuafeBay"
  RigSlot0 = "RigSlot0"
  RigSlot1 = "RigSlot1"
  RigSlot2 = "RigSlot2"
  RigSlot3 = "RigSlot3"
  RigSlot4 = "RigSlot4"
  RigSlot5 = "RigSlot5"
  RigSlot6 = "RigSlot6"
  RigSlot7 = "RigSlot7"
  ShipHangar = "ShipHangar"
  SpecializedFuelBay = "SpecializedFuelBay"
  SpecializedOreHold = "SpecializedOreHold"
  SpecializedGasHold = "SpecializedGasHold"
  SpecializedMineralHold = "SpecializedMineralHold"
  SpecializedSalvageHold = "SpecializedSalvageHold"
  SpecializedShipHold = "SpecializedShipHold"
  SpecializedSmallShipHold = "SpecializedSmallShipHold"
  SpecializedMediumShipHold = "SpecializedMediumShipHold"
  SpecializedLargeShipHold = "SpecializedLargeShipHold"
  SpecializedIndustrialShipHold = "SpecializedIndustrialShipHold"
  SpecializedAmmoHold = "SpecializedAmmoHold"
  SpecializedCommandCenterHold = "SpecializedCommandCenterHold"
  SpecializedPlanetaryCommoditiesHold = "SpecializedPlanetaryCommoditiesHold"
  SpecializedMaterialBay = "SpecializedMaterialBay"
  SubSystemSlot0 = "SubSystemSlot0"
  SubSystemSlot1 = "SubSystemSlot1"
  SubSystemSlot2 = "SubSystemSlot2"
  SubSystemSlot3 = "SubSystemSlot3"
  SubSystemSlot4 = "SubSystemSlot4"
  SubSystemSlot5 = "SubSystemSlot5"
  SubSystemSlot6 = "SubSystemSlot6"
  SubSystemSlot7 = "SubSystemSlot7"
  FighterBay = "FighterBay"
  FighterTube0 = "FighterTube0"
  FighterTube1 = "FighterTube1"
  FighterTube2 = "FighterTube2"
  FighterTube3 = "FighterTube3"
  FighterTube4 = "FighterTube4"
  Module = "Module"


class LocationFlag(str, Enum):
  """Location flags to indicate the types of containers.
  """

  AutoFit = "AutoFit"
  Cargo = "Cargo"
  CorpseBay = "CorpseBay"
  DroneBay = "DroneBay"
  FleetHangar = "FleetHangar"
  Deliveries = "Deliveries"
  HiddenModifiers = "HiddenModifiers"
  Hangar = "Hangar"
  HangarAll = "HangarAll"
  LoSlot0 = "LoSlot0"
  LoSlot1 = "LoSlot1"
  LoSlot2 = "LoSlot2"
  LoSlot3 = "LoSlot3"
  LoSlot4 = "LoSlot4"
  LoSlot5 = "LoSlot5"
  LoSlot6 = "LoSlot6"
  LoSlot7 = "LoSlot7"
  MedSlot0 = "MedSlot0"
  MedSlot1 = "MedSlot1"
  MedSlot2 = "MedSlot2"
  MedSlot3 = "MedSlot3"
  MedSlot4 = "MedSlot4"
  MedSlot5 = "MedSlot5"
  MedSlot6 = "MedSlot6"
  MedSlot7 = "MedSlot7"
  HiSlot0 = "HiSlot0"
  HiSlot1 = "HiSlot1"
  HiSlot2 = "HiSlot2"
  HiSlot3 = "HiSlot3"
  HiSlot4 = "HiSlot4"
  HiSlot5 = "HiSlot5"
  HiSlot6 = "HiSlot6"
  HiSlot7 = "HiSlot7"
  AssetSafety = "AssetSafety"
  Locked = "Locked"
  Unlocked = "Unlocked"
  Implant = "Implant"
  QuafeBay = "QuafeBay"
  RigSlot0 = "RigSlot0"
  RigSlot1 = "RigSlot1"
  RigSlot2 = "RigSlot2"
  RigSlot3 = "RigSlot3"
  RigSlot4 = "RigSlot4"
  RigSlot5 = "RigSlot5"
  RigSlot6 = "RigSlot6"
  RigSlot7 = "RigSlot7"
  ShipHangar = "ShipHangar"
  SpecializedFuelBay = "SpecializedFuelBay"
  SpecializedOreHold = "SpecializedOreHold"
  SpecializedGasHold = "SpecializedGasHold"
  SpecializedMineralHold = "SpecializedMineralHold"
  SpecializedSalvageHold = "SpecializedSalvageHold"
  SpecializedShipHold = "SpecializedShipHold"
  SpecializedSmallShipHold = "SpecializedSmallShipHold"
  SpecializedMediumShipHold = "SpecializedMediumShipHold"
  SpecializedLargeShipHold = "SpecializedLargeShipHold"
  SpecializedIndustrialShipHold = "SpecializedIndustrialShipHold"
  SpecializedAmmoHold = "SpecializedAmmoHold"
  SpecializedCommandCenterHold = "SpecializedCommandCenterHold"
  SpecializedPlanetaryCommoditiesHold = "SpecializedPlanetaryCommoditiesHold"
  SpecializedMaterialBay = "SpecializedMaterialBay"
  SubSystemSlot0 = "SubSystemSlot0"
  SubSystemSlot1 = "SubSystemSlot1"
  SubSystemSlot2 = "SubSystemSlot2"
  SubSystemSlot3 = "SubSystemSlot3"
  SubSystemSlot4 = "SubSystemSlot4"
  SubSystemSlot5 = "SubSystemSlot5"
  SubSystemSlot6 = "SubSystemSlot6"
  SubSystemSlot7 = "SubSystemSlot7"
  FighterBay = "FighterBay"
  FighterTube0 = "FighterTube0"
  FighterTube1 = "FighterTube1"
  FighterTube2 = "FighterTube2"
  FighterTube3 = "FighterTube3"
  FighterTube4 = "FighterTube4"
  Module = "Module"
  SpecializedAsteroidHold = 'SpecializedAsteroidHold'
  Skill = 'Skill'
  BoosterBay = 'BoosterBay'
  SubSystemBay = 'SubSystemBay'
  StructureDeedBay = 'StructureDeedBay'
  SpecializedIceHold = 'SpecializedIceHold'
  FrigateEscapeBay = 'FrigateEscapeBay'
  Wardrobe = 'Wardrobe'


class LocationType(str, Enum):
  """Location types to indicate where the container is located.
  """

  station = "station"
  solar_system = "solar_system"
  item = "item"
  other = "other"


class Asset(BaseModel):
  """A data model for a item as an asset.

  Attributes:
    is_blueprint_copy (bool): Whether the item is a blueprint copy or not.
    is_singleton (bool): Whether the item is stackable or not.
    item_id (int): The item id.
    location_flag (LocationFlag): The location flag of the container where the item is located.
    location_id (int): The location id of the container where the item is located.
    location_type (LocationType): The location type where the item is located.
    quantity (int): The stacked quantity of the item.
    type_id (int): The type id of the item.
  """

  is_blueprint_copy: bool = Field(
      False, description="Whether the item is a blueprint copy or not.")
  is_singleton: bool = Field(
      description="Whether the item is stackable or not.")
  item_id: int = Field(description="The item id.")
  location_flag: LocationFlag = Field(
      description="The location flag of the container where the item is located."
  )
  location_id: int = Field(
      description="The location id of the container where the item is located.")
  location_type: LocationType = Field(
      description="The location type where the item is located.")
  quantity: int = Field(description="The stacked quantity of the item.")
  type_id: int = Field(description="The type id of the item.")


class AssetLocation(BaseModel):
  """A data model for a location of an asset.
  """

  item_id: int = Field(description="The id of the item.")
  position: Vector3d = Field(description="The position of the item.")


class AssetName(BaseModel):
  """A data model for a name of an asset.

  Attributes:
    item_id (int): The id of the item.
    name (str): The name of the item.
  """

  item_id: int = Field(description="The id of the item.")
  name: str = Field(description="The name of the item.")
