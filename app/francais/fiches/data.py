"""Contenu des 6 fiches de révision (cartes mentales).

Chaque fiche est une arborescence à 3 niveaux :

    Fiche
    ├── Branche 1 (couleur)
    │   ├── Feuille 1 (label + exemples + astuce)
    │   └── Feuille 2 ...
    └── Branche 2 ...

Le rendu Jinja parcourt cette structure pour produire la carte mentale.
Les exemples sont tirés des annales DNB 2018-2025 quand c'est pertinent
pour ancrer la fiche dans des situations réelles d'examen.
"""

from __future__ import annotations

from dataclasses import dataclass, field


# ============================================================================
# Modèle de données
# ============================================================================


@dataclass
class Leaf:
    """Feuille de la carte mentale : un concept précis avec exemples."""

    label: str
    examples: list[str] = field(default_factory=list)
    tip: str | None = None


@dataclass
class Branch:
    """Branche thématique : regroupe plusieurs feuilles autour d'un sous-thème."""

    label: str
    color: str  # nom de couleur Tailwind brand : "rose", "indigo", "emerald", etc.
    icon: str  # emoji affiché dans la pastille (côté UI uniquement, pas dans le code)
    leaves: list[Leaf] = field(default_factory=list)


@dataclass
class Fiche:
    """Carte mentale complète."""

    slug: str
    title: str
    subtitle: str  # accroche d'une ligne sur la home
    central: str  # concept central, court (3-6 mots)
    intro: str  # phrase d'intro pour cadrer la fiche
    branches: list[Branch] = field(default_factory=list)


# ============================================================================
# Les 6 fiches
# ============================================================================


FICHES: list[Fiche] = [
    # ------------------------------------------------------------------ 1
    Fiche(
        slug="classes-grammaticales",
        title="Classes grammaticales",
        subtitle="La nature d'un mot : les 10 classes à connaître par cœur",
        central="Quelle est la nature de ce mot ?",
        intro=(
            "La classe grammaticale (ou « nature ») d'un mot, c'est sa famille. "
            "Elle ne change jamais, peu importe la phrase. On distingue les mots "
            "variables (qui s'accordent) et les mots invariables."
        ),
        branches=[
            Branch(
                label="Mots variables",
                color="rose",
                icon="A",
                leaves=[
                    Leaf(
                        "Nom",
                        examples=["chien, idée, courage (commun)", "Marguerite, Paris (propre)"],
                    ),
                    Leaf(
                        "Déterminant",
                        examples=[
                            "le, la, les, un, une, des (articles)",
                            "mon, ton, son, leur (possessifs)",
                            "ce, cette, ces (démonstratifs)",
                            "trois, quelques, plusieurs (numéraux/indéfinis)",
                        ],
                        tip="Précède toujours un nom",
                    ),
                    Leaf(
                        "Adjectif qualificatif",
                        examples=["petit, courageux, immaculé, atroce"],
                        tip="Donne une qualité à un nom",
                    ),
                    Leaf(
                        "Pronom",
                        examples=[
                            "je, tu, il, le, lui (personnels)",
                            "qui, que, dont, où (relatifs)",
                            "celui, celle (démonstratifs)",
                            "le mien, la tienne (possessifs)",
                        ],
                        tip="Remplace un nom ou un GN",
                    ),
                    Leaf(
                        "Verbe",
                        examples=["parler, comprendre, devenir"],
                        tip="Se conjugue en personne et en temps",
                    ),
                ],
            ),
            Branch(
                label="Mots invariables",
                color="indigo",
                icon="B",
                leaves=[
                    Leaf(
                        "Adverbe",
                        examples=[
                            "rapidement, doucement (manière)",
                            "ici, là, partout (lieu)",
                            "hier, souvent, déjà (temps)",
                            "beaucoup, très, peu (quantité)",
                            "ne... pas, jamais, plus (négation)",
                        ],
                    ),
                    Leaf(
                        "Préposition",
                        examples=["à, de, dans, sans, pour, avec, sur, sous"],
                        tip="Introduit un complément",
                    ),
                    Leaf(
                        "Conjonction de coordination",
                        examples=["mais, ou, et, donc, or, ni, car"],
                        tip="Moyen mnémo : Mais-Où-Et-Donc-Or-Ni-Car",
                    ),
                    Leaf(
                        "Conjonction de subordination",
                        examples=["que, quand, parce que, si, lorsque, bien que"],
                        tip="Introduit une proposition subordonnée",
                    ),
                    Leaf(
                        "Interjection",
                        examples=["oh !, ah !, hélas, zut"],
                    ),
                ],
            ),
            Branch(
                label="Comment trouver la nature ?",
                color="emerald",
                icon="?",
                leaves=[
                    Leaf("Peut-on le conjuguer ?", tip="Oui → verbe"),
                    Leaf("Précède-t-il un nom ?", tip="Souvent → déterminant"),
                    Leaf("Qualifie-t-il un nom ?", tip="Oui → adjectif"),
                    Leaf("Remplace-t-il un GN ?", tip="Oui → pronom"),
                    Leaf("S'accorde-t-il ?", tip="Non → mot invariable (adverbe, prép., conj.)"),
                ],
            ),
            Branch(
                label="Pièges fréquents au DNB",
                color="amber",
                icon="!",
                leaves=[
                    Leaf(
                        "« que »",
                        examples=[
                            "le livre que je lis → pronom relatif",
                            "je pense que tu viens → conjonction de subordination",
                            "il ne fait que dormir → adverbe",
                        ],
                    ),
                    Leaf(
                        "« leur »",
                        examples=[
                            "leurs livres → déterminant possessif (s'accorde)",
                            "je leur parle → pronom personnel (invariable)",
                        ],
                    ),
                    Leaf(
                        "Participe passé employé comme adjectif",
                        examples=[
                            "des soldats embusqués → adjectif",
                            "elle est partie → participe passé du verbe",
                        ],
                    ),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------ 2
    Fiche(
        slug="fonctions-grammaticales",
        title="Fonctions grammaticales",
        subtitle="Le rôle d'un mot dans la phrase : sujet, COD, attribut, CC...",
        central="Quel rôle joue ce mot ?",
        intro=(
            "La fonction d'un mot, c'est le rôle qu'il joue dans la phrase : "
            "qui fait l'action ? sur quoi ? où ? quand ? La fonction change "
            "selon la phrase, contrairement à la classe grammaticale."
        ),
        branches=[
            Branch(
                label="Autour du verbe",
                color="rose",
                icon="V",
                leaves=[
                    Leaf(
                        "Sujet",
                        examples=["[Marguerite] sourit."],
                        tip="Question : « qui est-ce qui ? / qu'est-ce qui ? »",
                    ),
                    Leaf(
                        "COD (complément d'objet direct)",
                        examples=["Penanster regarde [Marguerite]."],
                        tip="Question : « qui ? quoi ? » sans préposition",
                    ),
                    Leaf(
                        "COI (complément d'objet indirect)",
                        examples=["Il parle [à Marguerite]."],
                        tip="Question : « à qui ? de quoi ? » avec préposition",
                    ),
                    Leaf(
                        "COS (complément d'objet second)",
                        examples=["Il offre [un livre] [à son ami]."],
                        tip="Le 2e complément quand il y a déjà un COD",
                    ),
                    Leaf(
                        "Attribut du sujet",
                        examples=["Elle est [belle]. La situation devint [insupportable]."],
                        tip="Avec être, sembler, paraître, devenir, rester, demeurer",
                    ),
                    Leaf(
                        "Attribut du COD",
                        examples=["Je trouve [ce livre] [passionnant]."],
                    ),
                ],
            ),
            Branch(
                label="Compléments circonstanciels (CC)",
                color="indigo",
                icon="…",
                leaves=[
                    Leaf("CC de lieu", examples=["Elle vit [à Paris]."], tip="Question : où ?"),
                    Leaf("CC de temps", examples=["Il est parti [hier]."], tip="Question : quand ?"),
                    Leaf("CC de manière", examples=["Elle parle [doucement]."], tip="Question : comment ?"),
                    Leaf("CC de cause", examples=["Il pleure [de joie]."], tip="Question : pourquoi ?"),
                    Leaf("CC de but", examples=["Il étudie [pour réussir]."], tip="Question : dans quel but ?"),
                    Leaf("CC de moyen", examples=["Elle écrit [au stylo]."], tip="Question : avec quoi ?"),
                ],
            ),
            Branch(
                label="Autour du nom",
                color="emerald",
                icon="N",
                leaves=[
                    Leaf("Épithète", examples=["une voix [tiède]"], tip="Adjectif accolé au nom"),
                    Leaf("Complément du nom", examples=["un club [d'officiers]"], tip="Avec préposition"),
                    Leaf("Apposition", examples=["Marguerite, [infirmière courageuse], ..."], tip="Détaché par virgule"),
                    Leaf("Proposition relative", examples=["un club [qui compte trois membres]"]),
                ],
            ),
            Branch(
                label="Manipulations pour trouver",
                color="amber",
                icon="@",
                leaves=[
                    Leaf("Pronominalisation", tip="COD → le/la/les ; COI → lui/leur/y/en"),
                    Leaf("Déplacement", tip="Le CC se déplace, le COD non"),
                    Leaf("Suppression", tip="Le CC est souvent supprimable, pas le COD"),
                    Leaf("Question", tip="Pose la bonne question avec/sans préposition"),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------ 3
    Fiche(
        slug="expansions-du-nom",
        title="Expansions du nom",
        subtitle="Les 4 façons d'enrichir un nom dans le groupe nominal",
        central="Comment enrichir un nom ?",
        intro=(
            "Une expansion du nom, c'est un mot ou un groupe de mots qui complète "
            "ou précise un nom-noyau dans un groupe nominal. Il y a 4 grandes "
            "façons de le faire."
        ),
        branches=[
            Branch(
                label="Adjectif épithète",
                color="rose",
                icon="1",
                leaves=[
                    Leaf(
                        "Définition",
                        tip="Adjectif accolé directement au nom, sans virgule",
                    ),
                    Leaf(
                        "Exemples",
                        examples=[
                            "des membres [actifs]",
                            "une voix [tiède]",
                            "trois [bons] amis",
                        ],
                    ),
                    Leaf(
                        "À retenir",
                        tip="S'accorde en genre et en nombre avec le nom. Peut être avant ou après.",
                    ),
                ],
            ),
            Branch(
                label="Complément du nom (CDN)",
                color="indigo",
                icon="2",
                leaves=[
                    Leaf(
                        "Définition",
                        tip="Groupe nominal introduit par une préposition (de, à, en, pour, sans, avec...)",
                    ),
                    Leaf(
                        "Exemples",
                        examples=[
                            "un club [d'officiers]",
                            "une infirmière [de guerre]",
                            "un livre [à lire]",
                            "une bague [en or]",
                        ],
                    ),
                    Leaf(
                        "Sens",
                        tip="Précise la matière, l'origine, la possession, la fonction du nom.",
                    ),
                ],
            ),
            Branch(
                label="Apposition",
                color="emerald",
                icon="3",
                leaves=[
                    Leaf(
                        "Définition",
                        tip="Groupe nominal détaché par une virgule, qui désigne la même réalité que le nom-noyau",
                    ),
                    Leaf(
                        "Exemples",
                        examples=[
                            "Marguerite, [infirmière courageuse], soigne les blessés.",
                            "Paris, [capitale de la France], ...",
                        ],
                    ),
                    Leaf(
                        "Astuce",
                        tip="On peut souvent la remplacer par « qui est... »",
                    ),
                ],
            ),
            Branch(
                label="Proposition subordonnée relative",
                color="violet",
                icon="4",
                leaves=[
                    Leaf(
                        "Définition",
                        tip="Proposition introduite par un pronom relatif (qui, que, dont, où, lequel...)",
                    ),
                    Leaf(
                        "Exemples",
                        examples=[
                            "un club [qui compte trois membres]",
                            "le livre [que j'ai lu]",
                            "la maison [où j'ai grandi]",
                        ],
                    ),
                ],
            ),
            Branch(
                label="Méthode au DNB",
                color="amber",
                icon="@",
                leaves=[
                    Leaf("Étape 1", tip="Repère le nom-noyau (le nom enrichi)"),
                    Leaf("Étape 2", tip="Isole chaque expansion (groupe qui qualifie ce nom)"),
                    Leaf("Étape 3", tip="Nomme la nature : adjectif / CDN / apposition / relative"),
                    Leaf("Étape 4", tip="Si on demande la « classe grammaticale », précise-la (adjectif, GN, proposition...)"),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------ 4
    Fiche(
        slug="propositions-subordonnees",
        title="Propositions subordonnées",
        subtitle="Identifier la subordonnée, son subordonnant et sa fonction",
        central="Quelle subordonnée et quelle fonction ?",
        intro=(
            "Une proposition subordonnée dépend d'une autre proposition (la principale). "
            "Elle est introduite par un mot subordonnant. Au DNB on demande sa nature "
            "(quel type ?) et sa fonction (quel rôle dans la principale ?)."
        ),
        branches=[
            Branch(
                label="Subordonnée relative",
                color="rose",
                icon="R",
                leaves=[
                    Leaf(
                        "Subordonnant",
                        tip="Pronom relatif : qui, que, quoi, dont, où, lequel/laquelle",
                    ),
                    Leaf(
                        "Fonction",
                        tip="Complète un nom (= antécédent). Fonction = expansion du nom / complément de l'antécédent.",
                    ),
                    Leaf(
                        "Exemples",
                        examples=[
                            "le livre [que j'ai lu]",
                            "un club [qui compte trois membres]",
                            "la ville [où je vis]",
                        ],
                    ),
                ],
            ),
            Branch(
                label="Subordonnée conjonctive (en « que »)",
                color="indigo",
                icon="C",
                leaves=[
                    Leaf(
                        "Subordonnant",
                        tip="La conjonction « que » (parfois « ce que »)",
                    ),
                    Leaf(
                        "Fonction",
                        tip="Le plus souvent COD du verbe principal. Manipulation : on peut la remplacer par « cela ».",
                    ),
                    Leaf(
                        "Exemples",
                        examples=[
                            "Je compris [que ni Weil ni moi ne pourrions nous entretenir avec elle].",
                            "Elle pense [qu'il viendra].",
                        ],
                    ),
                ],
            ),
            Branch(
                label="Subordonnée circonstancielle",
                color="emerald",
                icon="CC",
                leaves=[
                    Leaf(
                        "Subordonnant",
                        tip="quand, lorsque, parce que, puisque, si, bien que, pour que, avant que...",
                    ),
                    Leaf(
                        "Fonction",
                        tip="Complément circonstanciel (CC) de temps, cause, but, condition, concession. Souvent déplaçable.",
                    ),
                    Leaf(
                        "Exemples",
                        examples=[
                            "[Quand elle sortit], elle ne se déroba point. (CC de temps)",
                            "Il est venu [parce qu'il pleuvait]. (CC de cause)",
                            "[Bien qu'il soit fatigué], il continue. (concession)",
                        ],
                    ),
                ],
            ),
            Branch(
                label="Subordonnée interrogative indirecte",
                color="violet",
                icon="?",
                leaves=[
                    Leaf(
                        "Subordonnant",
                        tip="si, ce que, quand, pourquoi, comment... (mots interrogatifs sans point d'interrogation)",
                    ),
                    Leaf(
                        "Exemples",
                        examples=[
                            "Je me demande [si tu viens].",
                            "Il sait [pourquoi elle pleure].",
                        ],
                    ),
                    Leaf(
                        "Astuce",
                        tip="On la repère parce qu'elle reformule une question dans une phrase déclarative.",
                    ),
                ],
            ),
            Branch(
                label="Méthode au DNB",
                color="amber",
                icon="@",
                leaves=[
                    Leaf("Étape 1", tip="Repère le verbe conjugué de la subordonnée"),
                    Leaf("Étape 2", tip="Repère le mot subordonnant (pronom relatif ou conjonction)"),
                    Leaf("Étape 3", tip="Nomme la nature : relative / conjonctive / circonstancielle / interrogative"),
                    Leaf("Étape 4", tip="Donne la fonction par manipulation (déplacement, remplacement par « cela »...)"),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------ 5
    Fiche(
        slug="conjugaison-temps-modes",
        title="Conjugaison : temps et modes",
        subtitle="Quel temps, quel mode et pour quel effet ?",
        central="Temps, mode et leurs valeurs",
        intro=(
            "Au DNB on demande presque toujours d'identifier le temps et le mode "
            "d'un verbe ET d'expliquer leur valeur (description, action, hypothèse...). "
            "Le mode dit comment l'action est présentée, le temps situe dans le temps."
        ),
        branches=[
            Branch(
                label="Indicatif (réalité, faits)",
                color="rose",
                icon="I",
                leaves=[
                    Leaf(
                        "Présent",
                        examples=["je parle"],
                        tip="Vérité générale, narration, énonciation",
                    ),
                    Leaf(
                        "Imparfait",
                        examples=["je parlais"],
                        tip="Description, action longue, habitude dans le passé",
                    ),
                    Leaf(
                        "Passé simple",
                        examples=["je parlai, il fut"],
                        tip="Action brève, premier plan d'un récit",
                    ),
                    Leaf(
                        "Passé composé",
                        examples=["j'ai parlé"],
                        tip="Action accomplie, lien avec le présent",
                    ),
                    Leaf(
                        "Plus-que-parfait",
                        examples=["j'avais parlé"],
                        tip="Antériorité par rapport à un autre passé",
                    ),
                    Leaf(
                        "Futur simple",
                        examples=["je parlerai"],
                        tip="Action à venir, certaine",
                    ),
                    Leaf(
                        "Futur antérieur",
                        examples=["j'aurai parlé"],
                        tip="Action future achevée avant une autre",
                    ),
                ],
            ),
            Branch(
                label="Subjonctif (incertitude, désir)",
                color="indigo",
                icon="S",
                leaves=[
                    Leaf(
                        "Présent",
                        examples=["que je sois, que tu fasses"],
                        tip="Souhait, conseil, ordre, doute",
                    ),
                    Leaf(
                        "Imparfait",
                        examples=["qu'il fût"],
                        tip="Registre soutenu, littéraire",
                    ),
                    Leaf(
                        "Quand l'utiliser",
                        tip="Après « il faut que », « bien que », « pour que », « avant que », « à condition que »...",
                    ),
                ],
            ),
            Branch(
                label="Conditionnel (hypothèse, politesse)",
                color="emerald",
                icon="C",
                leaves=[
                    Leaf(
                        "Présent",
                        examples=["je voudrais"],
                        tip="Politesse, irréel, action soumise à une condition",
                    ),
                    Leaf(
                        "Passé",
                        examples=["j'aurais voulu"],
                        tip="Regret, irréel du passé",
                    ),
                    Leaf(
                        "Piège : conditionnel ≠ futur",
                        examples=["je serais (cond.) ≠ je serai (futur)"],
                        tip="Le conditionnel a toujours un -r- ET un -ais/-ait",
                    ),
                ],
            ),
            Branch(
                label="Impératif (ordre, conseil)",
                color="violet",
                icon="!",
                leaves=[
                    Leaf(
                        "Forme",
                        examples=["parle, parlons, parlez"],
                        tip="Trois personnes seulement : 2e sg, 1re pl, 2e pl",
                    ),
                    Leaf(
                        "À retenir",
                        tip="Pas de pronom sujet exprimé. À la 2e pers. sg, pas de -s pour les verbes en -er (parle, mange).",
                    ),
                ],
            ),
            Branch(
                label="Modes impersonnels",
                color="slate",
                icon="∞",
                leaves=[
                    Leaf("Infinitif", examples=["parler, finir, prendre"], tip="Forme nominale du verbe"),
                    Leaf("Participe présent", examples=["parlant, finissant"], tip="Toujours en -ant, invariable"),
                    Leaf(
                        "Participe passé",
                        examples=["parlé, fini, pris"],
                        tip="S'accorde avec être, ou avec le COD avant le verbe (avoir)",
                    ),
                    Leaf("Gérondif", examples=["en parlant, en mangeant"], tip="« en » + participe présent"),
                ],
            ),
            Branch(
                label="Pièges fréquents au DNB",
                color="amber",
                icon="!",
                leaves=[
                    Leaf(
                        "Imparfait vs passé simple",
                        tip="Imparfait = arrière-plan, description. Passé simple = action de premier plan.",
                    ),
                    Leaf(
                        "Subjonctif obligatoire",
                        tip="Après « il faut que », « bien que », « pour que », « avant que »...",
                    ),
                    Leaf(
                        "Présent de narration",
                        tip="Présent dans un récit au passé : effet de vivacité, de mise en scène.",
                    ),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------ 10
    Fiche(
        slug="figures-de-style",
        title="Figures de style",
        subtitle="Les identifier, les nommer, expliquer leur effet",
        central="Quelle figure de style ?",
        intro=(
            "Une figure de style est un procédé d'écriture qui crée un effet "
            "particulier (image, surprise, insistance...). Au DNB il faut savoir "
            "l'identifier, la nommer ET expliquer son effet, en citant le texte."
        ),
        branches=[
            Branch(
                label="Analogie (rapprocher des éléments)",
                color="rose",
                icon="≈",
                leaves=[
                    Leaf(
                        "Comparaison",
                        examples=["« Elle était comme un parterre de roses saccagé. » (Dugain)"],
                        tip="Comporte un outil : comme, tel, semblable à, pareil à...",
                    ),
                    Leaf(
                        "Métaphore",
                        examples=["« miroirs de son infortune »", "« cette femme se réfléchissait en nous »"],
                        tip="Comparaison sans outil : on identifie directement A à B.",
                    ),
                    Leaf(
                        "Personnification",
                        examples=["« le vent murmure »", "« la mer se déchaîne »"],
                        tip="Donne des traits humains à un objet, un animal, une idée.",
                    ),
                    Leaf(
                        "Allégorie",
                        examples=["la Mort en faucheuse", "la Justice aux yeux bandés"],
                        tip="Représentation concrète d'une idée abstraite.",
                    ),
                ],
            ),
            Branch(
                label="Insistance (amplifier)",
                color="indigo",
                icon="+",
                leaves=[
                    Leaf(
                        "Hyperbole",
                        examples=["« mourir de rire »", "« il y a mille raisons »"],
                        tip="Exagération pour frapper.",
                    ),
                    Leaf(
                        "Anaphore",
                        examples=["« Moi, président... Moi, président... » (Hollande)"],
                        tip="Répétition d'un mot en début de phrase ou de vers.",
                    ),
                    Leaf(
                        "Gradation",
                        examples=["« Va, cours, vole, et nous venge ! » (Corneille)"],
                        tip="Progression croissante (ou décroissante) d'intensité.",
                    ),
                    Leaf(
                        "Énumération",
                        examples=["« des cris, des pleurs, des plaintes »"],
                        tip="Liste de termes pour amplifier.",
                    ),
                ],
            ),
            Branch(
                label="Opposition (contraster)",
                color="emerald",
                icon="↔",
                leaves=[
                    Leaf(
                        "Antithèse",
                        examples=["« ombre et lumière »", "« la guerre et la paix »"],
                        tip="Deux mots ou idées opposés dans la même phrase.",
                    ),
                    Leaf(
                        "Oxymore",
                        examples=["« soleil noir »", "« douceur tiède »", "« silence assourdissant »"],
                        tip="Antithèse condensée : deux mots opposés accolés.",
                    ),
                    Leaf(
                        "Chiasme",
                        examples=["« il faut manger pour vivre, et non vivre pour manger »"],
                        tip="Croisement en miroir : structure ABBA.",
                    ),
                ],
            ),
            Branch(
                label="Sonorités (jouer avec les sons)",
                color="violet",
                icon="♪",
                leaves=[
                    Leaf(
                        "Allitération",
                        examples=["« Pour qui sont ces serpents qui sifflent sur vos têtes ? »"],
                        tip="Répétition d'un son consonne (ici : s).",
                    ),
                    Leaf(
                        "Assonance",
                        examples=["« Tout m'afflige et me nuit, et conspire à me nuire »"],
                        tip="Répétition d'un son voyelle (ici : i).",
                    ),
                ],
            ),
            Branch(
                label="Substitution (désigner autrement)",
                color="amber",
                icon="→",
                leaves=[
                    Leaf(
                        "Métonymie",
                        examples=["« boire un verre » (= son contenu)", "« lire un Zola »"],
                        tip="Désigner une chose par un autre élément lié (contenant/contenu, auteur/œuvre...).",
                    ),
                    Leaf(
                        "Périphrase",
                        examples=["« la Ville Lumière » pour Paris", "« l'astre du jour » pour le soleil"],
                        tip="Expression de plusieurs mots à la place d'un seul.",
                    ),
                    Leaf(
                        "Euphémisme",
                        examples=["« il nous a quittés » pour « il est mort »"],
                        tip="Atténuer une réalité dure.",
                    ),
                ],
            ),
            Branch(
                label="Méthode au DNB",
                color="slate",
                icon="@",
                leaves=[
                    Leaf("Étape 1", tip="Identifie la figure et nomme-la précisément"),
                    Leaf("Étape 2", tip="Cite les mots concernés entre guillemets"),
                    Leaf("Étape 3", tip="Explique l'effet : que ressent-on ? que comprend-on mieux ?"),
                    Leaf("Astuce", tip="Une figure d'analogie sert souvent à rendre une description plus parlante (« adaptée pour décrire... »)"),
                ],
            ),
        ],
    ),
]


# ============================================================================
# Helpers d'accès
# ============================================================================


def list_fiches() -> list[Fiche]:
    """Renvoie toutes les fiches dans l'ordre canonique d'affichage."""
    return list(FICHES)


def get_fiche(slug: str) -> Fiche | None:
    """Renvoie la fiche correspondant au slug, ou None si inconnue."""
    for f in FICHES:
        if f.slug == slug:
            return f
    return None
