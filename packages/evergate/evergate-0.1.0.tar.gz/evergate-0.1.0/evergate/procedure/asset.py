"""
"""

from typing import Optional
from evergate._internal.requesting import get_from_esi, post_to_esi
from evergate._internal.tokenstorage import TokenStorage
from evergate.datamodel.asset import Asset, AssetLocation, AssetName


def get_character_assets(character_id: int, page: Optional[int]) -> list[Asset]:
  """Get the assets for a character id.

  Args:
    character_id (int): The character id.

  Returns:
    list[Asset]: A list of Asset objects.
  """

  res = get_from_esi(f"/characters/{character_id}/assets/",
                     query={"page": page},
                     token=TokenStorage().get())
  return [Asset(**asset) for asset in res]


def get_character_asset_locations(character_id: int,
                                  item_ids: list[int]) -> list[AssetLocation]:
  """Get the asset locations for a character id.

  Args:
    character_id (int): The character id.
    item_ids (list[int]): A list of item ids.

  Returns:
    list[AssetLocation]: A list of AssetLocation objects.
  """

  res = post_to_esi(f"/characters/{character_id}/assets/locations/",
                    body=item_ids,
                    token=TokenStorage().get())
  return [AssetLocation(**asset) for asset in res]


def get_character_asset_names(character_id: int,
                              item_ids: list[int]) -> list[AssetName]:
  """Get the asset names for a character id.

  Args:
    character_id (int): The character id.
    item_ids (list[int]): A list of item ids.

  Returns:
    list[AssetName]: A list of AssetName objects.
  """

  res = post_to_esi(f"/characters/{character_id}/assets/names/",
                    body=item_ids,
                    token=TokenStorage().get())
  return [AssetName(**asset) for asset in res]


def get_corporation_assets(corporation_id: int, page: Optional[int]) -> list[Asset]:
  """Get the assets for a corporation id.

  Args:
    corporation_id (int): The corporation id.

  Returns:
    list[Asset]: A list of Asset objects.
  """

  res = get_from_esi(f"/corporations/{corporation_id}/assets/",
                     query={"page": page},
                     token=TokenStorage().get())
  return [Asset(**asset) for asset in res]


def get_corporation_asset_locations(corporation_id: int,
                                    item_ids: list[int]) -> list[AssetLocation]:
  """Get the asset locations for a corporation id.

  Args:
    corporation_id (int): The corporation id.
    item_ids (list[int]): A list of item ids.

  Returns:
    list[AssetLocation]: A list of AssetLocation objects.
  """

  res = post_to_esi(f"/corporations/{corporation_id}/assets/locations/",
                    body=item_ids,
                    token=TokenStorage().get())
  return [AssetLocation(**asset) for asset in res]


def get_corporation_asset_names(corporation_id: int,
                                item_ids: list[int]) -> list[AssetName]:
  """Get the asset names for a corporation id.

  Args:
    corporation_id (int): The corporation id.
    item_ids (list[int]): A list of item ids.

  Returns:
    list[AssetName]: A list of AssetName objects.
  """

  res = post_to_esi(f"/corporations/{corporation_id}/assets/names/",
                    body=item_ids,
                    token=TokenStorage().get())
  return [AssetName(**asset) for asset in res]
