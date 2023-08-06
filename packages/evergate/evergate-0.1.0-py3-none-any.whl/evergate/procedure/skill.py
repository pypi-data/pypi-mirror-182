"""
"""

from evergate._internal.requesting import get_from_esi
from evergate._internal.tokenstorage import TokenStorage
from evergate.datamodel.skill import CharacterAttribute


def get_character_attributes(character_id: int) -> CharacterAttribute:
  """Get character attributes
    
  Args:
    character_id (int): Character ID
  """

  res = get_from_esi(f"/characters/{character_id}/attributes/",
                     token=TokenStorage().get())

  return CharacterAttribute(**res)
