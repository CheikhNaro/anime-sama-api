"""
API Anime Sama — client Python pour interagir avec le catalogue et les épisodes
d'Anime-Sama (anime-sama.to). Réutilisable dans une CLI, un site de streaming, un bot, etc.
"""

from .catalogue import Catalogue, Category
from .episode import Episode, Languages, Players
from .langs import Lang, LangId, flags, id2lang, lang2ids
from .season import Season
from .top_level import AnimeSama, EpisodeRelease, find_site_url, PlanningDay, PlanningEntry

__all__ = [
    "AnimeSama",
    "EpisodeRelease",
    "Catalogue",
    "Category",
    "PlanningDay",
    "PlanningEntry",
    "Season",
    "Episode",
    "Players",
    "Languages",
    "Lang",
    "LangId",
    "lang2ids",
    "id2lang",
    "flags",
    "find_site_url",
]
