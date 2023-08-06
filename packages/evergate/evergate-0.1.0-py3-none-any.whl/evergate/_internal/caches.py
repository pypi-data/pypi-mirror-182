"""
evergate._internal.caches

This module is for internal use only.
"""

from dataclasses import dataclass
from typing import Any, Optional
from json import dumps


@dataclass(frozen=True)
class Cache:
  """
  evergate._internal.caches.Cache

  Pairs of ETag and corresponding response.
  """
  etag: str
  value: dict


class CacheStorage:
  """
  evergate._internal.caches.CacheStorage

  This class is intended to cache responses from ESI.
  """

  _cache: dict[tuple, Cache]

  def __init__(self) -> None:
    self._cache = {}

  def find_etag(self, url: str, *parameters: Any) -> Optional[str]:
    """
    Returns ETag for given URL and headers.
    """
    cache = self._cache.get((url, *parameters), None)
    if cache is None:
      return None
    return cache.etag

  def expire(self, url: str, *parameters: Any) -> None:
    """
    Expires cache for given URL and headers.
    """
    self._cache.pop((url, *parameters), None)

  def __getitem__(self, key: tuple) -> Optional[dict]:
    """
    Returns dict object for given URL and headers.
    """
    cache = self._cache.get(key, None)

    if cache is None:
      return None

    return cache.value

  def __setitem__(self, key: tuple, value: tuple[str, dict]) -> None:
    """
    Create a new cache of dict object for given URL and headers.
    """

    self._cache[key] = Cache(*value)

  def __contains__(self, key: tuple) -> bool:
    """
    Returns True if cache exists for given URL and headers.
    """
    return key in self._cache

  @staticmethod
  def dict_as_tuple(value: dict) -> tuple:
    """
    Returns tuple representation of dict.
    """
    return (hash(dumps(value, sort_keys=True)), *value.keys())
