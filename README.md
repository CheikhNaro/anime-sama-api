# Anime-Sama API

API Python pour le catalogue et les épisodes **Anime-Sama** (anime-sama.to).  
Extrait et mise à jour du projet [anime-sama-cli](https://github.com/Sky-NiniKo/anime-sama_api), réutilisable sur un site de streaming, une CLI, un bot, etc.

## Dépendance

- **Python** 3.10+
- **httpx** (installé automatiquement)

## Utilisation rapide

```python
import asyncio
from anime_sama_api import AnimeSama, find_site_url

async def main():
    # Trouver l’URL actuelle du site (anime-sama change parfois de domaine)
    url = await find_site_url()
    if not url:
        url = "https://anime-sama.to/"

    api = AnimeSama(url)

    # Catalogue complet
    catalogues = await api.all_catalogues()

    # Recherche
    results = await api.search("One Piece")

    # Détails d’un animé : saisons, synopsis, etc.
    for cat in results[:1]:
        seasons = await cat.seasons()
        synopsis = await cat.synopsis()
        for season in seasons:
            episodes = await season.episodes()
            for ep in episodes[:2]:
                # URLs des lecteurs vidéo (VOSTFR, VF, etc.)
                best = ep.best(prefer_languages=["VOSTFR", "VF"])
                if best:
                    print(ep.name, "->", best)

    # Planning de la semaine
    days = await api.planning()

    # Derniers épisodes ajoutés (accueil)
    new = await api.new_episodes()

asyncio.run(main())
```

## Principaux types

| Type | Rôle |
|------|------|
| `AnimeSama` | Client principal : recherche, catalogue, planning, nouveaux épisodes |
| `find_site_url()` | Récupère l’URL actuelle du site (redirections anime-sama.pw) |
| `Catalogue` | Un animé : nom, URL, genres, catégories, langues, image ; méthodes `seasons()`, `synopsis()`, etc. |
| `Season` | Une saison ; méthode `episodes()` |
| `Episode` | Un épisode ; `languages.availables` (VF, VOSTFR…), `best(langues)` pour une URL de lecteur |
| `PlanningDay` / `PlanningEntry` | Planning de la semaine (jours, titres, horaires, langues) |
| `EpisodeRelease` | Résumé d’un nouvel épisode (accueil) |
| `Lang` / `LangId` | Langues (VOSTFR, VF, etc.) et identifiants internes |
