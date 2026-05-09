"""Routes des fiches de révision (cartes mentales) histoire-géo-EMC.

Deux URL :

    GET /              → liste des 5 fiches
    GET /{slug}        → carte mentale détaillée

Pas de session, pas de DB : du contenu statique rendu en HTML.
"""

from __future__ import annotations

import logging
from pathlib import Path

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.histoire_geo_emc.fiches.data import get_fiche, list_fiches

logger = logging.getLogger(__name__)

router = APIRouter(tags=["histoire-geo-emc-fiches"])

_HERE = Path(__file__).resolve().parent
_APP_DIR = _HERE.parent.parent
_CORE_TEMPLATES = _APP_DIR / "core" / "templates"
_HGEMC_TEMPLATES = _HERE.parent / "templates"
_FICHES_TEMPLATES = _HERE / "templates"

templates = Jinja2Templates(
    directory=[str(_FICHES_TEMPLATES), str(_HGEMC_TEMPLATES), str(_CORE_TEMPLATES)]
)


@router.get("/", response_class=HTMLResponse)
def fiches_index(request: Request):
    """Liste des fiches disponibles."""
    return templates.TemplateResponse(
        request,
        "index.html",
        {"fiches": list_fiches()},
    )


@router.get("/{slug}", response_class=HTMLResponse)
def fiche_detail(request: Request, slug: str):
    """Affiche une fiche détaillée sous forme de carte mentale."""
    fiche = get_fiche(slug)
    if fiche is None:
        raise HTTPException(status_code=404, detail="Fiche introuvable.")
    return templates.TemplateResponse(
        request,
        "fiche.html",
        {"fiche": fiche, "fiches": list_fiches()},
    )


__all__ = ["router"]
