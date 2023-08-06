"""
evergate._internal.requesting

This module is for internal use only.
"""

from typing import Any, Optional
from requests import get, post, delete, put

from evergate._internal.caches import CacheStorage
from urllib.parse import quote

HOST_URL = 'https://esi.evetech.net/latest'
DATASOURCE = 'tranquility'

cache = CacheStorage()


def format_query(query: dict[str, Any]) -> str:
  """
  Formats query string.
  """

  if query:
    return '?' + '&'.join(
        f"{quote(k)}={quote(['false', 'true'][i] if isinstance(i, bool) else str(i))}"
        for k, v in query.items()
        for i in (v if isinstance(v, list) else [v])
        if i is not None)

  return ''


def post_to_esi(path: str,
                query: Optional[dict] = None,
                headers: Optional[dict] = None,
                body: Optional[dict] = None,
                token: Optional[str] = None) -> dict:
  """
  Sends POST request to ESI.
  """
  query, headers, body = query or {}, headers or {}, body or {}

  query.setdefault('datasource', DATASOURCE)

  if token is not None:
    headers.setdefault('Authorization', f'Bearer {token}')

  req = post(f"{HOST_URL}{path}{format_query(query)}",
             headers=headers,
             json=body)

  data = req.json()

  if req.status_code == 400:
    raise ValueError(f"Bad request: {data['error']}")

  if req.status_code == 420:
    raise RuntimeError(f"ESI rate limit reached: {data['error']}")

  if req.status_code >= 500:
    raise RuntimeError(
        f"Bad response from ESI. It because ESI might be currently down: {data['error']}"
    )

  if req.status_code != 200:
    raise RuntimeError(f"ESI returned {req.status_code}: {data['error']}")

  return data


def get_from_esi(path: str,
                 query: Optional[dict] = None,
                 headers: Optional[dict] = None,
                 token: Optional[str] = None) -> dict:
  """
  Sends GET request to ESI.
  """

  query, headers = query or {}, headers or {}

  query.setdefault('datasource', DATASOURCE)

  if token is not None:
    headers.setdefault('Authorization', f'Bearer {token}')

  cache_key = cache.dict_as_tuple({'q': query, 'h': headers})

  etag = cache.find_etag(path, cache_key)

  if etag is not None:
    headers['If-None-Match'] = etag

  req = get(f"{HOST_URL}{path}{format_query(query)}", headers=headers)

  if req.status_code == 304:
    return cache[path, cache_key]

  data = req.json()

  if req.status_code == 400:
    raise ValueError(f"Bad request: {data['error']}")

  if req.status_code == 420:
    raise RuntimeError(f"ESI rate limit reached: {data['error']}")

  if req.status_code >= 500:
    raise RuntimeError(
        f"Bad response from ESI. It because ESI might be currently down: {data['error']}"
    )

  if req.status_code != 200:
    raise RuntimeError(f"ESI returned {req.status_code}: {data['error']}")

  cache[path, cache_key] = (req.headers['ETag'], data)

  return data


def delete_from_esi(path: str,
                    query: Optional[dict] = None,
                    headers: Optional[dict] = None,
                    token: Optional[str] = None) -> dict:
  """
  Sends DELETE request to ESI.
  """
  query, headers = query or {}, headers or {}

  query.setdefault('datasource', DATASOURCE)

  if token is not None:
    headers.setdefault('Authorization', f'Bearer {token}')

  req = delete(f"{HOST_URL}{path}{format_query(query)}", headers=headers)

  data = req.json()

  if req.status_code == 400:
    raise ValueError(f"Bad request: {data['error']}")

  if req.status_code == 420:
    raise RuntimeError(f"ESI rate limit reached: {data['error']}")

  if req.status_code >= 500:
    raise RuntimeError(
        f"Bad response from ESI. It because ESI might be currently down: {data['error']}"
    )

  if req.status_code != 200:
    raise RuntimeError(f"ESI returned {req.status_code}: {data['error']}")

  return data


def put_to_esi(path: str,
               query: Optional[dict] = None,
               headers: Optional[dict] = None,
               body: Optional[dict] = None,
               token: Optional[str] = None) -> dict:
  """
  Sends PUT request to ESI.
  """
  query, headers, body = query or {}, headers or {}, body or {}

  query.setdefault('datasource', DATASOURCE)

  if token is not None:
    headers.setdefault('Authorization', f'Bearer {token}')

  req = put(f"{HOST_URL}{path}{format_query(query)}",
            headers=headers,
            json=body)

  data = req.json()

  if req.status_code == 400:
    raise ValueError(f"Bad request: {data['error']}")

  if req.status_code == 420:
    raise RuntimeError(f"ESI rate limit reached: {data['error']}")

  if req.status_code >= 500:
    raise RuntimeError(
        f"Bad response from ESI. It because ESI might be currently down: {data['error']}"
    )

  if req.status_code != 200:
    raise RuntimeError(f"ESI returned {req.status_code}: {data['error']}")

  return data
