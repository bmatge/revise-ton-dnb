"""Modèle de données partagé pour les fiches de révision (cartes mentales).

Chaque matière (français, maths, histoire-géo-EMC) déclare ses fiches dans
son propre `app/<matiere>/fiches/data.py`, mais réutilise les dataclasses
ci-dessous pour garantir un format homogène et permettre aux templates de
les rendre de la même façon.

Trois niveaux d'arborescence :

    Fiche
    ├── Branche 1 (couleur, icône)
    │   ├── Feuille 1 (label, exemples, astuce)
    │   └── Feuille 2 ...
    └── Branche 2 ...
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Leaf:
    """Feuille de la carte mentale : un concept précis avec exemples."""

    label: str
    examples: list[str] = field(default_factory=list)
    tip: str | None = None


@dataclass
class Branch:
    """Branche thématique : regroupe plusieurs feuilles autour d'un sous-thème.

    Le nom de couleur (`color`) doit correspondre à une clé du dict `_palette`
    déclaré dans les templates `fiche.html` de chaque matière. Valeurs
    actuellement supportées : rose, indigo, emerald, amber, violet, slate.
    """

    label: str
    color: str
    icon: str
    leaves: list[Leaf] = field(default_factory=list)


@dataclass
class Fiche:
    """Carte mentale complète."""

    slug: str
    title: str
    subtitle: str  # accroche courte sur la home matière
    central: str   # concept central (3-6 mots)
    intro: str     # phrase d'intro pour cadrer la fiche
    branches: list[Branch] = field(default_factory=list)
