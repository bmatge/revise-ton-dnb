"""Contenu des 6 fiches de révision (cartes mentales) maths.

Le rendu Jinja parcourt l'arborescence Fiche → Branch → Leaf pour produire
la carte mentale. Les dataclasses sont définies dans `app.core.fiches`
(partagées avec français et histoire-géo-EMC).
"""

from __future__ import annotations

from app.core.fiches import Branch, Fiche, Leaf


# ============================================================================
# Les 6 fiches
# ============================================================================


FICHES: list[Fiche] = [
    # ------------------------------------------------------------------ 1
    Fiche(
        slug="calcul-litteral-equations",
        title="Calcul littéral, équations et identités remarquables",
        subtitle="Développer, factoriser, résoudre — et tous les tricks qui font gagner du temps",
        central="Comment manipuler une expression algébrique ?",
        intro=(
            "C'est le cœur du DNB : presque chaque sujet contient un calcul "
            "littéral, une identité remarquable ou une équation à résoudre. "
            "L'objectif : reconnaître la situation, choisir la bonne technique, "
            "et appliquer les bons réflexes."
        ),
        branches=[
            Branch(
                label="Développer",
                color="rose",
                icon="D",
                leaves=[
                    Leaf(
                        "Distributivité simple",
                        examples=["k(a + b) = ka + kb", "3(x + 5) = 3x + 15"],
                        tip="On distribue le facteur devant à chaque terme entre parenthèses.",
                    ),
                    Leaf(
                        "Double distributivité",
                        examples=["(a + b)(c + d) = ac + ad + bc + bd", "(x + 2)(x + 3) = x² + 3x + 2x + 6 = x² + 5x + 6"],
                        tip="Chaque terme du premier facteur multiplie chaque terme du second.",
                    ),
                    Leaf(
                        "IR développées",
                        examples=[
                            "(a + b)² = a² + 2ab + b²",
                            "(a − b)² = a² − 2ab + b²",
                            "(a + b)(a − b) = a² − b²",
                        ],
                        tip="Trois identités remarquables à connaître par cœur.",
                    ),
                ],
            ),
            Branch(
                label="Factoriser",
                color="indigo",
                icon="F",
                leaves=[
                    Leaf(
                        "Facteur commun",
                        examples=["ka + kb = k(a + b)", "6x + 9 = 3(2x + 3)", "x(x + 2) + 3(x + 2) = (x + 2)(x + 3)"],
                        tip="On cherche ce qui se répète dans tous les termes (un nombre, une variable, ou même une parenthèse).",
                    ),
                    Leaf(
                        "IR factorisées",
                        examples=[
                            "a² + 2ab + b² = (a + b)²",
                            "a² − 2ab + b² = (a − b)²",
                            "a² − b² = (a − b)(a + b)",
                        ],
                        tip="Lire l'IR « à l'envers » : si on voit deux carrés et un double produit, on peut factoriser.",
                    ),
                    Leaf(
                        "Astuce du facteur caché",
                        examples=["(x − 3) et (3 − x) = −(x − 3)", "donc x(x − 3) + 5(3 − x) = x(x − 3) − 5(x − 3) = (x − 3)(x − 5)"],
                        tip="Quand deux parenthèses semblent différentes, vérifie si l'une est l'opposée de l'autre.",
                    ),
                ],
            ),
            Branch(
                label="Identités remarquables",
                color="emerald",
                icon="IR",
                leaves=[
                    Leaf(
                        "Les 3 IR",
                        examples=[
                            "(a + b)² = a² + 2ab + b²",
                            "(a − b)² = a² − 2ab + b²",
                            "(a − b)(a + b) = a² − b²",
                        ],
                    ),
                    Leaf(
                        "Comment les reconnaître ?",
                        tip="Présence de carrés (x², 9, 25...) ET d'un double produit (2 × premier × second).",
                    ),
                    Leaf(
                        "Exemple guidé : (5x − 2)²",
                        examples=[
                            "a = 5x, b = 2",
                            "a² = (5x)² = 25x²",
                            "2ab = 2 × 5x × 2 = 20x",
                            "b² = 2² = 4",
                            "→ (5x − 2)² = 25x² − 20x + 4",
                        ],
                    ),
                    Leaf(
                        "Exemple guidé : 49x² − 16",
                        examples=[
                            "49x² = (7x)²  et  16 = 4²",
                            "Donc 49x² − 16 = (7x)² − 4² = (7x − 4)(7x + 4)",
                        ],
                        tip="Différence de deux carrés → factorisation immédiate.",
                    ),
                ],
            ),
            Branch(
                label="Résoudre une équation du 1er degré",
                color="violet",
                icon="=",
                leaves=[
                    Leaf(
                        "Méthode standard",
                        tip="1. Développer si nécessaire. 2. Regrouper les x d'un côté, les nombres de l'autre. 3. Diviser par le coefficient de x.",
                    ),
                    Leaf(
                        "Exemple : 3(x − 2) = 5x + 4",
                        examples=[
                            "3x − 6 = 5x + 4   (développé)",
                            "3x − 5x = 4 + 6   (on regroupe)",
                            "−2x = 10",
                            "x = −5",
                        ],
                    ),
                    Leaf(
                        "Trick : supprimer les dénominateurs",
                        examples=[
                            "x/3 + 2 = x/2 − 1",
                            "On multiplie les deux membres par 6 (PPCM de 3 et 2) :",
                            "2x + 12 = 3x − 6",
                            "x = 18",
                        ],
                        tip="Multiplier par le PPCM des dénominateurs élimine les fractions d'un seul coup.",
                    ),
                    Leaf(
                        "Trick : faire passer du x à droite quand le coef est négatif à gauche",
                        examples=["−2x + 5 = 3x − 10", "→ 5 + 10 = 3x + 2x", "→ 15 = 5x  →  x = 3"],
                        tip="On évite les nombres négatifs en faisant passer les x du côté où le coef est positif.",
                    ),
                ],
            ),
            Branch(
                label="Équation produit",
                color="amber",
                icon="×",
                leaves=[
                    Leaf(
                        "Règle d'or",
                        tip="Un produit de facteurs est nul si et seulement si l'un au moins des facteurs est nul. A × B = 0 ⇔ A = 0 ou B = 0.",
                    ),
                    Leaf(
                        "Exemple : (x − 3)(2x + 5) = 0",
                        examples=[
                            "x − 3 = 0  ou  2x + 5 = 0",
                            "x = 3      ou  x = −5/2",
                            "Solutions : S = { 3 ; −5/2 }",
                        ],
                    ),
                    Leaf(
                        "Stratégie : factoriser d'abord",
                        examples=[
                            "x² − 9 = 0",
                            "(x − 3)(x + 3) = 0   (IR)",
                            "x = 3  ou  x = −3",
                        ],
                        tip="Si on voit une équation pas du 1er degré, on essaie de la factoriser pour se ramener à un produit nul.",
                    ),
                    Leaf(
                        "Cas x² = a (avec a ≥ 0)",
                        examples=["x² = 16  →  x = 4  ou  x = −4", "x² = 5  →  x = √5  ou  x = −√5"],
                        tip="Toujours deux solutions opposées (sauf si a = 0).",
                    ),
                ],
            ),
            Branch(
                label="Tips & tricks au DNB",
                color="slate",
                icon="!",
                leaves=[
                    Leaf("Avant de résoudre", tip="Toujours simplifier au maximum : factoriser, supprimer les dénos, regrouper."),
                    Leaf("Repérer une IR cachée", tip="Si tu vois deux carrés (avec une variable au carré) et un double produit, c'est probablement une IR."),
                    Leaf("Vérifier ta solution", tip="Remplace la valeur trouvée dans l'équation initiale : les deux membres doivent être égaux."),
                    Leaf("Calcul mental utile", examples=["11² = 121", "12² = 144", "13² = 169", "14² = 196", "15² = 225", "25² = 625"]),
                    Leaf("Ne pas confondre", tip="(a + b)² ≠ a² + b² (l'erreur la plus pénalisée du DNB). Il manque le double produit 2ab."),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------ 2
    Fiche(
        slug="pythagore-thales",
        title="Pythagore et Thalès",
        subtitle="Calculer une longueur, démontrer un angle droit ou un parallélisme",
        central="Quel théorème pour quelle situation ?",
        intro=(
            "Les deux théorèmes les plus utilisés au DNB. Pythagore travaille "
            "dans un triangle rectangle, Thalès quand on a deux droites parallèles "
            "qui coupent deux sécantes. Bien identifier la configuration, c'est "
            "déjà avoir résolu la moitié de l'exercice."
        ),
        branches=[
            Branch(
                label="Théorème de Pythagore",
                color="rose",
                icon="P",
                leaves=[
                    Leaf(
                        "Énoncé",
                        examples=["Si ABC est rectangle en C, alors AB² = AC² + BC²"],
                        tip="L'hypoténuse² = somme des carrés des deux autres côtés. L'hypoténuse est en face de l'angle droit.",
                    ),
                    Leaf(
                        "Quand l'utiliser ?",
                        tip="On a un triangle rectangle, on connaît 2 côtés, on cherche le 3e.",
                    ),
                    Leaf(
                        "Calculer l'hypoténuse",
                        examples=["AC = 3, BC = 4 → AB² = 9 + 16 = 25 → AB = 5"],
                    ),
                    Leaf(
                        "Calculer un côté de l'angle droit",
                        examples=["AB = 13, AC = 5 → BC² = AB² − AC² = 169 − 25 = 144 → BC = 12"],
                        tip="Soustraction (et pas addition) quand on cherche un côté de l'angle droit.",
                    ),
                ],
            ),
            Branch(
                label="Réciproque et contraposée de Pythagore",
                color="indigo",
                icon="R",
                leaves=[
                    Leaf(
                        "Réciproque",
                        examples=["Si AB² = AC² + BC², alors ABC est rectangle en C."],
                        tip="Sert à DÉMONTRER qu'un triangle est rectangle.",
                    ),
                    Leaf(
                        "Méthode pour appliquer la réciproque",
                        tip="1. Calculer AB² (le plus grand côté au carré). 2. Calculer AC² + BC². 3. Comparer. Si égal → rectangle ; si différent → pas rectangle.",
                    ),
                    Leaf(
                        "Contraposée",
                        examples=["Si AB² ≠ AC² + BC², alors ABC n'est pas rectangle en C."],
                        tip="Sert à DÉMONTRER qu'un triangle n'est PAS rectangle.",
                    ),
                ],
            ),
            Branch(
                label="Théorème de Thalès",
                color="emerald",
                icon="T",
                leaves=[
                    Leaf(
                        "Configuration",
                        tip="Deux droites sécantes en A, coupées par deux droites parallèles (BC) // (B'C'). Configuration en triangle ou en papillon.",
                    ),
                    Leaf(
                        "Égalité des rapports",
                        examples=["AB/AB' = AC/AC' = BC/B'C'"],
                        tip="Les longueurs des « petits » sur les « grands » sont toutes égales.",
                    ),
                    Leaf(
                        "Méthode pour calculer une longueur",
                        examples=[
                            "Données : AB = 4, AB' = 6, BC = 5, on cherche B'C'.",
                            "AB / AB' = BC / B'C'",
                            "4 / 6 = 5 / B'C'",
                            "B'C' = (5 × 6) / 4 = 7,5",
                        ],
                        tip="Produit en croix une fois les rapports posés.",
                    ),
                ],
            ),
            Branch(
                label="Réciproque de Thalès",
                color="violet",
                icon="R",
                leaves=[
                    Leaf(
                        "Énoncé",
                        tip="Si A, B, B' sont alignés et A, C, C' sont alignés (dans le même ordre) ET AB/AB' = AC/AC', alors (BC) // (B'C').",
                    ),
                    Leaf(
                        "Méthode",
                        tip="1. Vérifier l'alignement et l'ordre des points. 2. Calculer AB/AB' et AC/AC'. 3. Si égaux → parallèles. Sinon → non parallèles.",
                    ),
                    Leaf(
                        "Attention à l'ordre",
                        tip="Les points doivent être dans le même ordre sur les deux droites (sinon configuration papillon : on autorise mais c'est plus subtil).",
                    ),
                ],
            ),
            Branch(
                label="Tips & tricks au DNB",
                color="amber",
                icon="!",
                leaves=[
                    Leaf("Toujours faire un schéma annoté", tip="Note les longueurs connues directement sur le triangle. Ça évite 90 % des erreurs."),
                    Leaf("Repérer l'hypoténuse", tip="C'est toujours le côté en face de l'angle droit, et c'est le plus long."),
                    Leaf("Valeurs exactes vs arrondies", tip="On garde les √ jusqu'à la fin, on n'arrondit qu'une fois et au moment demandé."),
                    Leaf("Triplets pythagoriciens à connaître", examples=["(3, 4, 5)", "(5, 12, 13)", "(8, 15, 17)", "(7, 24, 25)"]),
                    Leaf("Configuration Thalès : triangle ou papillon ?", tip="Triangle : A à l'extérieur, BC et B'C' du même côté. Papillon : les parallèles sont de part et d'autre de A."),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------ 3
    Fiche(
        slug="trigonometrie",
        title="Trigonométrie dans le triangle rectangle",
        subtitle="Calculer un angle ou un côté avec sin, cos, tan",
        central="Quelle formule trigonométrique choisir ?",
        intro=(
            "Quand un exercice donne un angle (autre que l'angle droit) et "
            "demande de calculer une longueur, ou inversement, c'est de la "
            "trigonométrie. Mnémo à connaître par cœur : SOH-CAH-TOA."
        ),
        branches=[
            Branch(
                label="Vocabulaire (par rapport à un angle aigu)",
                color="rose",
                icon="V",
                leaves=[
                    Leaf("Hypoténuse", tip="Le côté opposé à l'angle droit. C'est le plus long."),
                    Leaf("Côté opposé", tip="En face de l'angle considéré (qui n'est pas l'angle droit)."),
                    Leaf("Côté adjacent", tip="À côté de l'angle considéré (ce n'est ni l'opposé, ni l'hypoténuse)."),
                ],
            ),
            Branch(
                label="Les 3 formules : SOH-CAH-TOA",
                color="indigo",
                icon="F",
                leaves=[
                    Leaf("SOH", examples=["sin(angle) = Opposé / Hypoténuse"]),
                    Leaf("CAH", examples=["cos(angle) = Adjacent / Hypoténuse"]),
                    Leaf("TOA", examples=["tan(angle) = Opposé / Adjacent"]),
                    Leaf(
                        "Mnémo",
                        tip="« SOH-CAH-TOA » se lit S-O-H, C-A-H, T-O-A : trois lettres pour chaque formule, dans l'ordre.",
                    ),
                ],
            ),
            Branch(
                label="Trouver une longueur",
                color="emerald",
                icon="L",
                leaves=[
                    Leaf(
                        "Méthode",
                        tip="1. Repérer l'angle connu. 2. Identifier le côté connu et le côté cherché par rapport à cet angle. 3. Choisir sin/cos/tan selon les côtés en jeu. 4. Résoudre par produit en croix.",
                    ),
                    Leaf(
                        "Exemple",
                        examples=[
                            "Angle Â = 35°, hypoténuse = 10. On cherche le côté opposé.",
                            "sin(35°) = opposé / 10",
                            "opposé = 10 × sin(35°) ≈ 5,74",
                        ],
                    ),
                ],
            ),
            Branch(
                label="Trouver un angle",
                color="violet",
                icon="A",
                leaves=[
                    Leaf(
                        "Méthode",
                        tip="1. Identifier les deux côtés connus par rapport à l'angle cherché. 2. Choisir la formule. 3. Utiliser la fonction inverse de la calculatrice : sin⁻¹, cos⁻¹, tan⁻¹.",
                    ),
                    Leaf(
                        "Exemple",
                        examples=[
                            "Hypoténuse = 13, côté adjacent = 5. On cherche l'angle Â.",
                            "cos(Â) = 5 / 13",
                            "Â = cos⁻¹(5/13) ≈ 67,4°",
                        ],
                    ),
                ],
            ),
            Branch(
                label="Tips & tricks au DNB",
                color="amber",
                icon="!",
                leaves=[
                    Leaf(
                        "Calculatrice en mode degré",
                        tip="Vérifier qu'elle affiche DEG ou D (pas RAD ni GRAD). C'est l'erreur n°1 en trigo.",
                    ),
                    Leaf(
                        "Encadrement des fonctions",
                        tip="0 ≤ sin(angle) ≤ 1 et 0 ≤ cos(angle) ≤ 1 toujours. tan peut dépasser 1.",
                    ),
                    Leaf(
                        "Arrondi",
                        tip="On arrondit à la fin du calcul, pas en cours de route. L'énoncé précise généralement à combien de décimales.",
                    ),
                    Leaf(
                        "Astuce d'identification rapide",
                        examples=[
                            "Tu connais hypoténuse et opposé ? → sin",
                            "Tu connais hypoténuse et adjacent ? → cos",
                            "Tu connais opposé et adjacent ? → tan",
                        ],
                    ),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------ 4
    Fiche(
        slug="fonctions",
        title="Fonctions linéaires et affines",
        subtitle="Reconnaître, calculer une image, lire un graphique",
        central="Quelle fonction et comment l'utiliser ?",
        intro=(
            "Au DNB on rencontre surtout deux types de fonctions : linéaires "
            "(modélisent une proportionnalité) et affines (linéaire décalée "
            "verticalement). Savoir passer entre formule, tableau de valeurs "
            "et graphique est essentiel."
        ),
        branches=[
            Branch(
                label="Fonction linéaire",
                color="rose",
                icon="L",
                leaves=[
                    Leaf("Forme", examples=["f(x) = a × x", "f(x) = 3x ; g(x) = −2x"], tip="« a » est le coefficient de la fonction."),
                    Leaf(
                        "Représentation graphique",
                        tip="Une droite qui passe TOUJOURS par l'origine O(0 ; 0).",
                    ),
                    Leaf(
                        "Lien avec la proportionnalité",
                        tip="Une fonction linéaire modélise une situation de proportionnalité. Le coefficient « a » est le coefficient de proportionnalité.",
                    ),
                ],
            ),
            Branch(
                label="Fonction affine",
                color="indigo",
                icon="A",
                leaves=[
                    Leaf("Forme", examples=["f(x) = a × x + b", "f(x) = 3x − 5"], tip="« a » : coefficient directeur. « b » : ordonnée à l'origine."),
                    Leaf(
                        "Représentation graphique",
                        tip="Une droite qui ne passe PAS par l'origine (sauf si b = 0, auquel cas c'est linéaire).",
                    ),
                    Leaf(
                        "Sens de variation",
                        examples=["a > 0 → fonction croissante (la droite monte)", "a < 0 → fonction décroissante (la droite descend)"],
                    ),
                ],
            ),
            Branch(
                label="Image et antécédent",
                color="emerald",
                icon="I",
                leaves=[
                    Leaf(
                        "Image de x",
                        examples=["f(x) = 2x + 3, alors f(4) = 2 × 4 + 3 = 11"],
                        tip="On remplace x par sa valeur dans la formule.",
                    ),
                    Leaf(
                        "Antécédent de y",
                        examples=[
                            "f(x) = 2x + 3. On cherche l'antécédent de 11.",
                            "On résout 2x + 3 = 11",
                            "2x = 8 → x = 4",
                        ],
                        tip="On résout l'équation f(x) = y.",
                    ),
                    Leaf("Vocabulaire", tip="L'image se calcule, l'antécédent se résout."),
                ],
            ),
            Branch(
                label="Lecture graphique",
                color="violet",
                icon="G",
                leaves=[
                    Leaf(
                        "Lire une image",
                        tip="On part de x sur l'axe horizontal, on monte (ou descend) jusqu'à la droite, puis on lit la valeur sur l'axe vertical.",
                    ),
                    Leaf(
                        "Lire un antécédent",
                        tip="L'inverse : on part de y sur l'axe vertical, on va horizontalement jusqu'à la droite, puis on lit x sur l'axe horizontal.",
                    ),
                    Leaf(
                        "Calculer le coefficient directeur",
                        examples=["Avec deux points (x₁, y₁) et (x₂, y₂) :", "a = (y₂ − y₁) / (x₂ − x₁)"],
                        tip="Différence des ordonnées sur différence des abscisses.",
                    ),
                    Leaf(
                        "Lire b",
                        tip="b = f(0), c'est la valeur de y quand la droite coupe l'axe vertical.",
                    ),
                ],
            ),
            Branch(
                label="Tips & tricks au DNB",
                color="amber",
                icon="!",
                leaves=[
                    Leaf(
                        "Linéaire ou affine ?",
                        tip="La droite passe par O ? Linéaire. Sinon : affine. Un tableau est-il proportionnel ? Linéaire.",
                    ),
                    Leaf(
                        "Trouver l'expression d'une fonction affine",
                        tip="1. Calculer a avec deux points. 2. Trouver b en lisant l'ordonnée à l'origine OU en remplaçant un point dans f(x) = ax + b.",
                    ),
                    Leaf(
                        "Tracer rapidement y = ax + b",
                        tip="Placer le point (0, b), puis se déplacer de +1 en x et de +a en y pour obtenir un second point.",
                    ),
                    Leaf(
                        "Vérifier qu'un point appartient à la droite",
                        tip="On remplace les coordonnées dans l'équation. Si l'égalité est vraie, le point est sur la droite.",
                    ),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------ 5
    Fiche(
        slug="proportionnalite",
        title="Proportionnalité, pourcentages, vitesses",
        subtitle="Reconnaître la proportionnalité et calculer dans la vie courante",
        central="Comment exploiter une proportionnalité ?",
        intro=(
            "Les problèmes concrets du DNB (recettes, échelles, vitesses, "
            "soldes...) reposent presque tous sur la proportionnalité. La "
            "reconnaître et savoir calculer un pourcentage ou une vitesse "
            "rapporte beaucoup de points faciles."
        ),
        branches=[
            Branch(
                label="Reconnaître la proportionnalité",
                color="rose",
                icon="P",
                leaves=[
                    Leaf(
                        "Dans un tableau",
                        tip="On divise chaque valeur de la 2e ligne par la valeur de la 1re : si on trouve toujours le même nombre, c'est proportionnel. Ce nombre est le coefficient de proportionnalité.",
                    ),
                    Leaf(
                        "Sur un graphique",
                        tip="C'est proportionnel si et seulement si le graphique est une droite passant par l'origine (0 ; 0).",
                    ),
                    Leaf(
                        "Avec une formule",
                        tip="y = k × x → proportionnel. y = ax + b avec b ≠ 0 → pas proportionnel.",
                    ),
                ],
            ),
            Branch(
                label="Calculer dans un tableau",
                color="indigo",
                icon="C",
                leaves=[
                    Leaf(
                        "Quatrième proportionnelle",
                        examples=[
                            "Tableau :  3 → 12  /  5 → ?",
                            "Coefficient : 12 / 3 = 4",
                            "Donc ? = 5 × 4 = 20",
                        ],
                    ),
                    Leaf(
                        "Produit en croix",
                        examples=[
                            "Tableau :  3 → 12  /  5 → ?",
                            "? = (5 × 12) / 3 = 20",
                        ],
                        tip="On multiplie en diagonale puis on divise par celui qui reste.",
                    ),
                ],
            ),
            Branch(
                label="Pourcentages",
                color="emerald",
                icon="%",
                leaves=[
                    Leaf(
                        "x % de N",
                        examples=["20 % de 150 = (20 × 150) / 100 = 30"],
                        tip="Multiplier par x/100.",
                    ),
                    Leaf(
                        "Augmentation de x %",
                        examples=["+15 % → multiplier par 1,15", "+5 % → multiplier par 1,05"],
                        tip="On multiplie par (1 + x/100).",
                    ),
                    Leaf(
                        "Diminution de x %",
                        examples=["−20 % → multiplier par 0,80", "−30 % → multiplier par 0,70"],
                        tip="On multiplie par (1 − x/100).",
                    ),
                    Leaf(
                        "Pourcentages successifs",
                        examples=[
                            "Soldes : −30 % puis −10 % supplémentaires",
                            "Coefficient global : 0,70 × 0,90 = 0,63",
                            "Soit une réduction de 37 % au total (et non 40 %)",
                        ],
                        tip="On MULTIPLIE les coefficients, on n'ADDITIONNE pas les pourcentages.",
                    ),
                ],
            ),
            Branch(
                label="Vitesse, distance, durée",
                color="violet",
                icon="V",
                leaves=[
                    Leaf(
                        "La formule clé",
                        examples=["distance = vitesse × durée", "vitesse = distance / durée", "durée = distance / vitesse"],
                        tip="Triangle « D = V × T » : on cache ce qu'on cherche, et la formule apparaît.",
                    ),
                    Leaf(
                        "Cohérence des unités",
                        examples=[
                            "vitesse en km/h ↔ distance en km, durée en h",
                            "vitesse en m/s ↔ distance en m, durée en s",
                        ],
                        tip="Les unités doivent être cohérentes AVANT de calculer.",
                    ),
                    Leaf(
                        "Conversions à connaître",
                        examples=[
                            "1 h = 60 min = 3600 s",
                            "1 km = 1000 m",
                            "1 m/s = 3,6 km/h (multiplier par 3,6)",
                            "1 km/h = 1/3,6 m/s (diviser par 3,6)",
                        ],
                    ),
                    Leaf(
                        "Convertir une durée décimale",
                        examples=[
                            "1,5 h = 1 h 30 min",
                            "2,25 h = 2 h 15 min",
                            "0,1 h = 6 min   (et non 10 min !)",
                        ],
                        tip="0,1 h = 0,1 × 60 = 6 min. Multiplier la partie décimale par 60.",
                    ),
                ],
            ),
            Branch(
                label="Tips & tricks au DNB",
                color="amber",
                icon="!",
                leaves=[
                    Leaf("Convertir AVANT de calculer", tip="On homogénéise les unités au début. Sinon, erreur garantie."),
                    Leaf(
                        "Soldes : pas d'addition de %",
                        tip="−10 % puis −20 % ≠ −30 %. Toujours multiplier les coefficients (0,9 × 0,8 = 0,72 = −28 %).",
                    ),
                    Leaf(
                        "Augmentation puis diminution du même %",
                        examples=["+10 % puis −10 % ≠ retour à la valeur initiale", "1,1 × 0,9 = 0,99 → on perd 1 %"],
                    ),
                    Leaf(
                        "Échelles",
                        examples=["Échelle 1/200 : 1 cm sur le plan = 200 cm = 2 m en vrai"],
                        tip="Une échelle est une proportionnalité entre dimensions sur le plan et dimensions réelles.",
                    ),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------ 6
    Fiche(
        slug="statistiques-probabilites",
        title="Statistiques et probabilités",
        subtitle="Lire des données, calculer une probabilité, faire un arbre",
        central="Quel calcul pour quelle question ?",
        intro=(
            "Au DNB il y a presque toujours une question de stats (lecture d'un "
            "tableau, calcul de moyenne ou médiane) et une question de probabilité "
            "(souvent avec un arbre ou une urne). Les calculs sont simples, "
            "l'enjeu est de bien identifier ce qu'on demande."
        ),
        branches=[
            Branch(
                label="Vocabulaire stats",
                color="rose",
                icon="S",
                leaves=[
                    Leaf("Effectif", tip="Nombre de fois qu'une valeur apparaît dans la série."),
                    Leaf("Effectif total", tip="Somme de tous les effectifs."),
                    Leaf(
                        "Fréquence",
                        examples=["fréquence = effectif / effectif total", "Donne un nombre entre 0 et 1, ou un pourcentage."],
                    ),
                ],
            ),
            Branch(
                label="Indicateurs de position",
                color="indigo",
                icon="M",
                leaves=[
                    Leaf(
                        "Moyenne",
                        examples=[
                            "Série : 4, 7, 9, 10, 15",
                            "Moyenne = (4 + 7 + 9 + 10 + 15) / 5 = 9",
                        ],
                        tip="Somme des valeurs / nombre de valeurs.",
                    ),
                    Leaf(
                        "Moyenne pondérée",
                        examples=[
                            "Notes 12 (coef 2), 14 (coef 3), 8 (coef 1)",
                            "Moyenne = (12×2 + 14×3 + 8×1) / (2+3+1) = 74/6 ≈ 12,3",
                        ],
                        tip="Somme des (valeur × coefficient) / somme des coefficients.",
                    ),
                    Leaf(
                        "Médiane",
                        examples=[
                            "Série classée : 4, 7, 9, 10, 15 (5 valeurs)",
                            "Médiane = la 3e valeur = 9",
                        ],
                        tip="On classe la série puis on prend la valeur du milieu. 50 % des valeurs sont en dessous, 50 % au-dessus.",
                    ),
                    Leaf(
                        "Médiane (effectif pair)",
                        examples=["Série : 4, 7, 9, 10, 15, 20 → médiane = (9 + 10) / 2 = 9,5"],
                        tip="Si pair : moyenne des deux valeurs centrales.",
                    ),
                    Leaf(
                        "Étendue",
                        examples=["Série : 4, 7, 9, 10, 15 → étendue = 15 − 4 = 11"],
                        tip="Valeur maximale − valeur minimale.",
                    ),
                ],
            ),
            Branch(
                label="Probabilités : règles de base",
                color="emerald",
                icon="P",
                leaves=[
                    Leaf(
                        "Définition",
                        examples=["P(événement) = nombre de cas favorables / nombre de cas possibles"],
                        tip="Valable en situation d'équiprobabilité (chaque issue a la même chance).",
                    ),
                    Leaf("Encadrement", tip="0 ≤ P(A) ≤ 1. Probabilité 0 = impossible. Probabilité 1 = certain."),
                    Leaf(
                        "Événement contraire",
                        examples=["P(non A) = 1 − P(A)"],
                        tip="Astuce : si calculer A est compliqué, calculer son contraire et soustraire à 1.",
                    ),
                    Leaf(
                        "Exemple : dé à 6 faces",
                        examples=[
                            "P(obtenir un 6) = 1/6",
                            "P(obtenir un nombre pair) = 3/6 = 1/2",
                            "P(ne pas obtenir un 6) = 1 − 1/6 = 5/6",
                        ],
                    ),
                ],
            ),
            Branch(
                label="Arbre de probabilités",
                color="violet",
                icon="T",
                leaves=[
                    Leaf(
                        "Construction",
                        tip="Chaque branche représente une issue. Sur chaque branche, on note la probabilité. La somme des probas qui partent d'un nœud vaut 1.",
                    ),
                    Leaf(
                        "Le long d'une branche : on multiplie",
                        examples=["P(A et B) = P(A) × P(B)"],
                        tip="Pour la probabilité d'un chemin complet, on multiplie les probabilités le long du chemin.",
                    ),
                    Leaf(
                        "Plusieurs chemins : on additionne",
                        examples=["P(au moins un succès) = somme des probabilités des chemins favorables"],
                    ),
                    Leaf(
                        "Exemple : 2 tirages avec remise",
                        examples=[
                            "Urne : 3 rouges, 2 bleues. P(R) = 3/5, P(B) = 2/5.",
                            "P(2 rouges) = 3/5 × 3/5 = 9/25",
                            "P(une de chaque) = (3/5 × 2/5) + (2/5 × 3/5) = 12/25",
                        ],
                    ),
                ],
            ),
            Branch(
                label="Tips & tricks au DNB",
                color="amber",
                icon="!",
                leaves=[
                    Leaf(
                        "Vérification du tableau",
                        tip="Toujours vérifier que la somme des effectifs = effectif total annoncé.",
                    ),
                    Leaf(
                        "Médiane vs moyenne",
                        tip="Une valeur extrême tire la moyenne mais pas la médiane. Si l'énoncé demande « la valeur typique », pense médiane.",
                    ),
                    Leaf(
                        "Probabilité = fraction simplifiée",
                        examples=["3/6 → 1/2", "20/100 → 1/5"],
                        tip="On simplifie la fraction au maximum dans la réponse.",
                    ),
                    Leaf(
                        "Repérer la question",
                        examples=[
                            "« Quelle est la probabilité que... » → cas favorables / cas possibles",
                            "« Au moins un... » → souvent plus simple via le contraire (1 − P(aucun))",
                        ],
                    ),
                    Leaf(
                        "Avec/sans remise",
                        tip="Avec remise : les probabilités ne changent pas d'un tirage à l'autre. Sans remise : il faut recalculer (effectif total diminué de 1).",
                    ),
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
