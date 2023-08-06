"""
"""

from evergate.procedure.authorization import add_token, expire_token
from evergate.procedure.alliance import (get_alliance_ids, get_alliance_by_id,
                                         get_corporations_of_alliance,
                                         get_alliance_icons)
from evergate.procedure.contact import (
    get_alliance_contacts,
    get_alliance_contact_labels,
    get_corporation_contacts,
    get_corporation_contact_labels,
    get_character_contacts,
    get_character_contact_labels,
    post_character_contacts,
    put_character_contacts,
    delete_character_contacts,
)

__all__ = [
    "add_token",
    "expire_token",
    "get_alliance_ids",
    "get_alliance_by_id",
    "get_corporations_of_alliance",
    "get_alliance_icons",
    "get_alliance_contacts",
    "get_alliance_contact_labels",
    "get_corporation_contacts",
    "get_corporation_contact_labels",
    "get_character_contacts",
    "get_character_contact_labels",
    "post_character_contacts",
    "put_character_contacts",
    "delete_character_contacts",
]
