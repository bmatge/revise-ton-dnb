"""Contenu des 5 fiches de révision (cartes mentales) histoire-géo-EMC.

Le rendu Jinja parcourt l'arborescence Fiche → Branch → Leaf pour produire
la carte mentale. Les dataclasses sont définies dans `app.core.fiches`
(partagées avec français et mathématiques).

Les 5 thèmes couvrent les chapitres les plus tombés au DNB en
développement construit : WW1, WW2 (et la France), Ve République,
guerre froide, aménager le territoire français.

Complémentaire du module repères : ici on structure un thème (acteurs,
causes, conséquences, dates clés) plutôt que de lister les repères
individuels.
"""

from __future__ import annotations

from app.core.fiches import Branch, Fiche, Leaf


# ============================================================================
# Les 5 fiches
# ============================================================================


FICHES: list[Fiche] = [
    # ------------------------------------------------------------------ 1
    Fiche(
        slug="premiere-guerre-mondiale",
        title="La Première Guerre mondiale (1914-1918)",
        subtitle="Causes, phases, guerre totale, traités — la Grande Guerre",
        central="Pourquoi 1914-1918 est une guerre totale ?",
        intro=(
            "La Première Guerre mondiale est le premier grand conflit mondial : "
            "elle mobilise les soldats au front mais aussi les civils à l'arrière, "
            "transforme les économies et les sociétés, et redessine la carte de "
            "l'Europe. Au DNB, c'est l'un des thèmes les plus fréquents en DC."
        ),
        branches=[
            Branch(
                label="Causes et déclenchement",
                color="rose",
                icon="1",
                leaves=[
                    Leaf(
                        "Tensions européennes",
                        tip="Course aux armements, nationalismes, rivalités coloniales depuis la fin du XIXe siècle.",
                    ),
                    Leaf(
                        "Système des alliances",
                        examples=[
                            "Triple-Entente : France, Royaume-Uni, Russie",
                            "Triple-Alliance : Allemagne, Autriche-Hongrie, Italie",
                        ],
                        tip="Toute crise locale peut déclencher un conflit généralisé par jeu d'alliances.",
                    ),
                    Leaf(
                        "Étincelle : Sarajevo",
                        examples=["28 juin 1914 : assassinat de l'archiduc François-Ferdinand"],
                        tip="L'engrenage des déclarations de guerre se met en marche en août 1914.",
                    ),
                ],
            ),
            Branch(
                label="Les phases du conflit",
                color="indigo",
                icon="2",
                leaves=[
                    Leaf(
                        "Guerre de mouvement (août-déc. 1914)",
                        examples=["Invasion de la Belgique et du Nord de la France", "Bataille de la Marne (sept. 1914) : Joffre stoppe l'avancée allemande"],
                    ),
                    Leaf(
                        "Guerre de position / des tranchées (1915-1917)",
                        examples=[
                            "Verdun (févr.-déc. 1916) : 300 000 morts, symbole de l'horreur",
                            "Somme (juil.-nov. 1916) : 1 million de victimes au total",
                        ],
                        tip="Front figé, vie dans la boue, gaz toxiques, obus en pluie.",
                    ),
                    Leaf(
                        "Guerre globale (1917)",
                        examples=[
                            "Avril 1917 : entrée des États-Unis aux côtés de l'Entente",
                            "Octobre 1917 : révolution russe → retrait russe du conflit (Brest-Litovsk, mars 1918)",
                        ],
                    ),
                    Leaf(
                        "Issue (1918)",
                        examples=["Offensive de printemps allemande échoue", "Armistice signé à Rethondes (Compiègne) le 11 novembre 1918"],
                    ),
                ],
            ),
            Branch(
                label="Une guerre totale",
                color="emerald",
                icon="T",
                leaves=[
                    Leaf(
                        "Mobilisation des civils",
                        examples=["Économie de guerre : usines reconverties pour produire armes et munitions", "Femmes au travail dans les usines (« munitionnettes »)"],
                        tip="Toute la société participe à l'effort de guerre.",
                    ),
                    Leaf(
                        "Propagande et censure",
                        tip="Contrôle de l'information, « bourrage de crâne », caricatures pour mobiliser l'opinion.",
                    ),
                    Leaf(
                        "Violences extrêmes",
                        examples=[
                            "Armes nouvelles : mitrailleuses, gaz, lance-flammes, chars, aviation",
                            "Génocide des Arméniens par l'Empire ottoman (1915-1916) : ~1,2 million de morts",
                        ],
                    ),
                    Leaf(
                        "Bilan humain",
                        examples=["~10 millions de morts dont 1,4 million de Français", "Millions de blessés et mutilés (« Gueules cassées »)"],
                    ),
                ],
            ),
            Branch(
                label="Conséquences et traité de Versailles",
                color="violet",
                icon="3",
                leaves=[
                    Leaf(
                        "Traité de Versailles (28 juin 1919)",
                        examples=[
                            "Article 231 : Allemagne déclarée seule responsable de la guerre",
                            "Pertes territoriales : Alsace-Lorraine rendue à la France, perte des colonies",
                            "Réparations financières énormes",
                            "Armée allemande limitée à 100 000 hommes",
                        ],
                        tip="Vécu comme un « diktat » par les Allemands → rancœur, terreau du nazisme.",
                    ),
                    Leaf(
                        "Une carte redessinée",
                        examples=[
                            "Disparition de 4 empires : Allemand, Austro-Hongrois, Ottoman, Russe",
                            "Nouveaux États : Pologne, Tchécoslovaquie, Yougoslavie",
                        ],
                    ),
                    Leaf(
                        "SDN (Société des Nations)",
                        tip="Première organisation internationale pour maintenir la paix. Idée du président américain Wilson, mais les USA n'y entrent finalement pas. Échec face aux dictatures dans les années 1930.",
                    ),
                ],
            ),
            Branch(
                label="À retenir absolument",
                color="amber",
                icon="!",
                leaves=[
                    Leaf("Dates clés", examples=["1914 : début", "1916 : Verdun", "11 novembre 1918 : armistice", "1919 : traité de Versailles"]),
                    Leaf(
                        "Personnages",
                        examples=[
                            "Joffre : vainqueur de la Marne",
                            "Clemenceau : « Père la Victoire », chef du gouvernement en 1917-20",
                            "Pétain : héros de Verdun",
                            "Wilson : président américain, idée de la SDN",
                        ],
                    ),
                    Leaf(
                        "Notions",
                        examples=[
                            "Poilus : surnom des soldats français (à cause des conditions de vie)",
                            "Tranchée : ligne de défense creusée dans le sol",
                            "Guerre totale : mobilise militaires, civils, économie",
                            "Génocide : extermination planifiée d'un groupe",
                        ],
                    ),
                    Leaf(
                        "Plan type pour un DC",
                        tip="1. Une guerre d'un type nouveau (mondiale, longue, technique). 2. Une guerre totale (front + arrière, civils mobilisés). 3. Des conséquences durables (carte, sociétés, traumatismes).",
                    ),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------ 2
    Fiche(
        slug="seconde-guerre-mondiale",
        title="La Seconde Guerre mondiale et la France",
        subtitle="Vichy, Résistance, Shoah, Libération — l'épreuve la plus dure du XXe siècle",
        central="Comment la France traverse-t-elle la guerre ?",
        intro=(
            "La Seconde Guerre mondiale (1939-1945) est un conflit d'anéantissement "
            "à l'échelle planétaire. Pour la France, elle se traduit par une "
            "défaite éclair, l'occupation, la collaboration de Vichy, mais aussi "
            "par la Résistance et la libération. Au DNB, on attend que tu connaisses "
            "les deux faces : la France de Vichy ET la France qui résiste."
        ),
        branches=[
            Branch(
                label="Un conflit d'anéantissement",
                color="rose",
                icon="1",
                leaves=[
                    Leaf(
                        "Les régimes totalitaires expansionnistes",
                        examples=[
                            "Allemagne nazie (Hitler) : Anschluss 1938, Munich 1938, invasion Pologne sept. 1939",
                            "Italie fasciste (Mussolini), Japon militariste",
                        ],
                    ),
                    Leaf(
                        "Phases mondiales",
                        examples=[
                            "1939-1941 : victoires de l'Axe (Blitzkrieg)",
                            "1942-1943 : tournant (Stalingrad, El Alamein, Midway)",
                            "1944-1945 : reconquête alliée, capitulations",
                        ],
                    ),
                    Leaf(
                        "Bilan",
                        examples=[
                            "50 à 60 millions de morts dont une majorité de civils",
                            "Première guerre où civils > militaires",
                            "Bombes atomiques sur Hiroshima (6 août 1945) et Nagasaki (9 août 1945)",
                        ],
                    ),
                ],
            ),
            Branch(
                label="La défaite et l'Occupation",
                color="indigo",
                icon="2",
                leaves=[
                    Leaf(
                        "Défaite éclair (mai-juin 1940)",
                        tip="L'armée française, supposée la meilleure d'Europe, s'effondre en 6 semaines. Exode de millions de civils sur les routes.",
                    ),
                    Leaf(
                        "Armistice (22 juin 1940)",
                        tip="Pétain demande l'armistice. La France est coupée en deux : zone occupée au nord (Allemands) et zone libre au sud (gouvernement de Vichy).",
                    ),
                    Leaf(
                        "Régime de Vichy",
                        examples=[
                            "Pétain : chef de l'État (juillet 1940)",
                            "Devise : « Travail, Famille, Patrie »",
                            "Régime autoritaire : suppression des partis, censure, propagande",
                        ],
                    ),
                    Leaf(
                        "Collaboration d'État",
                        examples=[
                            "Entrevue de Montoire (24 oct. 1940) : poignée de main Pétain-Hitler",
                            "Politique antisémite : statut des Juifs (3 oct. 1940)",
                        ],
                    ),
                ],
            ),
            Branch(
                label="La France de Vichy",
                color="emerald",
                icon="V",
                leaves=[
                    Leaf(
                        "Politique antisémite",
                        examples=[
                            "Statut des Juifs (oct. 1940 puis juin 1941) : exclusion de la fonction publique, professions libérales",
                            "Rafle du Vél d'Hiv (16-17 juillet 1942) : 13 000 Juifs arrêtés à Paris par la police française",
                        ],
                        tip="Vichy participe activement à la « solution finale » : pas seulement passif.",
                    ),
                    Leaf(
                        "STO (Service du travail obligatoire, 1943)",
                        tip="Réquisition de jeunes Français pour aller travailler en Allemagne. Beaucoup choisissent le maquis pour échapper au STO.",
                    ),
                    Leaf(
                        "Régime autoritaire",
                        examples=["Fin de la République (« Vive Pétain »)", "Jeunesse encadrée (Chantiers de la jeunesse)", "Censure et propagande"],
                    ),
                ],
            ),
            Branch(
                label="La Résistance",
                color="violet",
                icon="R",
                leaves=[
                    Leaf(
                        "Appel du 18 juin 1940",
                        tip="Charles de Gaulle, depuis Londres, appelle à continuer le combat. Naissance de la France libre.",
                    ),
                    Leaf(
                        "Résistance intérieure",
                        examples=[
                            "Maquis (forêts, montagnes) : combat armé",
                            "Journaux clandestins : Combat, Libération, Franc-Tireur",
                            "Sabotages : voies ferrées, lignes de communication",
                            "Réseaux d'évasion (pilotes alliés, persécutés)",
                        ],
                    ),
                    Leaf(
                        "Jean Moulin et le CNR",
                        examples=[
                            "Jean Moulin : envoyé par de Gaulle, unifie la Résistance",
                            "27 mai 1943 : création du CNR (Conseil national de la Résistance) à Paris",
                            "Jean Moulin arrêté à Caluire (juin 1943), torturé, mort en juillet 1943",
                        ],
                    ),
                    Leaf(
                        "Programme du CNR (mars 1944)",
                        tip="Prépare la France d'après-guerre : Sécurité sociale, droit de vote des femmes (1944), nationalisations.",
                    ),
                ],
            ),
            Branch(
                label="La Shoah",
                color="slate",
                icon="!",
                leaves=[
                    Leaf(
                        "La « solution finale »",
                        tip="Conférence de Wannsee (20 janv. 1942) : décision de l'extermination industrielle des Juifs d'Europe.",
                    ),
                    Leaf(
                        "Les camps d'extermination",
                        examples=["Auschwitz-Birkenau (Pologne)", "Treblinka", "Sobibor", "Chambres à gaz, fours crématoires"],
                        tip="À ne pas confondre avec les camps de concentration (travail forcé, mortalité élevée mais pas industrielle).",
                    ),
                    Leaf(
                        "Bilan",
                        examples=[
                            "6 millions de Juifs assassinés (dont 1,5 million d'enfants)",
                            "75 % des Juifs européens",
                            "~250 000 Tsiganes (Porajmos)",
                            "76 000 Juifs de France déportés, ~3 % de survivants",
                        ],
                    ),
                ],
            ),
            Branch(
                label="Libération et après-guerre",
                color="amber",
                icon="3",
                leaves=[
                    Leaf(
                        "Débarquements",
                        examples=[
                            "6 juin 1944 (D-Day) : débarquement en Normandie",
                            "15 août 1944 : débarquement en Provence",
                        ],
                    ),
                    Leaf(
                        "Libération de la France",
                        examples=[
                            "Paris libéré le 25 août 1944 (Leclerc + résistants)",
                            "Discours de De Gaulle à l'Hôtel de Ville",
                        ],
                    ),
                    Leaf(
                        "Capitulations",
                        examples=[
                            "8 mai 1945 : capitulation de l'Allemagne (Reims puis Berlin)",
                            "2 septembre 1945 : capitulation du Japon (après Hiroshima et Nagasaki)",
                        ],
                    ),
                    Leaf(
                        "Procès de Nuremberg (1945-1946)",
                        tip="Jugement des dirigeants nazis. Naissance du concept de « crime contre l'humanité ». Inspiration pour le droit international.",
                    ),
                    Leaf(
                        "Plan type pour un DC sur la France pendant la guerre",
                        tip="1. La défaite et le régime de Vichy (collaboration, antisémitisme). 2. La Résistance intérieure et extérieure (de Gaulle, Jean Moulin, CNR). 3. La libération et l'héritage (procès, programme du CNR).",
                    ),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------ 3
    Fiche(
        slug="ve-republique",
        title="La Ve République",
        subtitle="Naissance, fonctionnement, présidents et alternances",
        central="Comment fonctionne la Ve République ?",
        intro=(
            "La Ve République est née en 1958 dans une crise grave (guerre d'Algérie). "
            "Elle renforce le pouvoir exécutif et donne une place centrale au "
            "président de la République. C'est le régime français actuel, l'un des "
            "plus stables d'Europe avec 65 ans d'existence et plusieurs alternances."
        ),
        branches=[
            Branch(
                label="Naissance (1958)",
                color="rose",
                icon="1",
                leaves=[
                    Leaf(
                        "Crise du 13 mai 1958",
                        tip="À Alger, des partisans de l'Algérie française forment un Comité de salut public. La IVe République, paralysée, ne sait plus gérer la guerre d'Algérie.",
                    ),
                    Leaf(
                        "Retour de De Gaulle",
                        examples=[
                            "1er juin 1958 : De Gaulle nommé président du Conseil",
                            "Il obtient les pleins pouvoirs pour rédiger une nouvelle Constitution",
                        ],
                    ),
                    Leaf(
                        "Référendum du 28 septembre 1958",
                        tip="79,2 % de oui : la nouvelle Constitution est adoptée. Naissance officielle de la Ve République le 4 octobre 1958.",
                    ),
                    Leaf(
                        "Premier président",
                        examples=["De Gaulle élu par grands électeurs en décembre 1958, prend ses fonctions en janvier 1959."],
                    ),
                ],
            ),
            Branch(
                label="Un régime semi-présidentiel",
                color="indigo",
                icon="2",
                leaves=[
                    Leaf(
                        "Renforcement de l'exécutif",
                        tip="Le président devient la clé de voûte des institutions, contrairement aux régimes précédents (parlementaires).",
                    ),
                    Leaf(
                        "Réforme de 1962",
                        tip="Référendum à l'initiative de De Gaulle : le président est désormais élu au suffrage universel direct (et non plus par les grands électeurs).",
                    ),
                    Leaf(
                        "Mandat présidentiel",
                        examples=[
                            "À l'origine : septennat (7 ans)",
                            "Depuis 2000 : quinquennat (5 ans, référendum sous Chirac)",
                            "Depuis 2008 : limité à 2 mandats consécutifs",
                        ],
                    ),
                    Leaf(
                        "La cohabitation",
                        examples=[
                            "1986-1988 : Mitterrand (PS) / Chirac (RPR)",
                            "1993-1995 : Mitterrand (PS) / Balladur (RPR)",
                            "1997-2002 : Chirac (RPR) / Jospin (PS)",
                        ],
                        tip="Période où le président et le Premier ministre sont de bords politiques opposés.",
                    ),
                ],
            ),
            Branch(
                label="Pouvoirs du président",
                color="emerald",
                icon="P",
                leaves=[
                    Leaf("Chef de l'État", tip="Représente la France à l'étranger, garant de l'unité nationale."),
                    Leaf("Chef des armées", tip="Décide de l'usage de la force armée, y compris du nucléaire."),
                    Leaf("Nomme le Premier ministre", tip="Et, sur sa proposition, les autres ministres."),
                    Leaf(
                        "Peut dissoudre l'Assemblée",
                        tip="Article 12 de la Constitution. Provoque de nouvelles élections législatives.",
                    ),
                    Leaf(
                        "Article 16 (pouvoirs exceptionnels)",
                        tip="En cas de menace grave (guerre, catastrophe), le président peut concentrer tous les pouvoirs. Utilisé une seule fois (1961, putsch d'Alger).",
                    ),
                    Leaf("Promulgue les lois", tip="Et peut soumettre une loi au référendum."),
                ],
            ),
            Branch(
                label="Les institutions",
                color="violet",
                icon="I",
                leaves=[
                    Leaf(
                        "Pouvoir exécutif",
                        examples=["Président de la République (élu pour 5 ans)", "Gouvernement : Premier ministre + ministres"],
                    ),
                    Leaf(
                        "Pouvoir législatif (le Parlement)",
                        examples=[
                            "Assemblée nationale : 577 députés, élus pour 5 ans au suffrage universel direct",
                            "Sénat : 348 sénateurs, élus au suffrage indirect par des grands électeurs",
                        ],
                        tip="L'Assemblée nationale a le dernier mot en cas de désaccord avec le Sénat.",
                    ),
                    Leaf(
                        "Pouvoir judiciaire",
                        tip="Tribunaux de droit commun + juridictions spécialisées. Indépendant des autres pouvoirs.",
                    ),
                    Leaf(
                        "Conseil constitutionnel",
                        tip="9 membres, mandat de 9 ans. Vérifie que les lois respectent la Constitution. Saisine possible par le président, les Premiers ministres, ou des parlementaires.",
                    ),
                ],
            ),
            Branch(
                label="Présidents et alternances",
                color="amber",
                icon="!",
                leaves=[
                    Leaf(
                        "Les 8 présidents de la Ve",
                        examples=[
                            "Charles de Gaulle (1959-1969)",
                            "Georges Pompidou (1969-1974, décès en fonction)",
                            "Valéry Giscard d'Estaing (1974-1981)",
                            "François Mitterrand (1981-1995, 2 mandats)",
                            "Jacques Chirac (1995-2007, 2 mandats)",
                            "Nicolas Sarkozy (2007-2012)",
                            "François Hollande (2012-2017)",
                            "Emmanuel Macron (2017-...)",
                        ],
                    ),
                    Leaf(
                        "Dates clés des évolutions",
                        examples=[
                            "1958 : naissance",
                            "1962 : élection au suffrage universel",
                            "1981 : 1ère alternance gauche/droite (Mitterrand)",
                            "2000 : quinquennat (référendum)",
                            "2008 : modernisation (Sarkozy)",
                        ],
                    ),
                    Leaf(
                        "Plan type pour un DC sur la Ve République",
                        tip="1. La naissance et les principes (1958, Constitution, place du président). 2. Le fonctionnement (institutions, pouvoirs, cohabitation). 3. Les évolutions (alternances, réformes, élargissement de la démocratie).",
                    ),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------ 4
    Fiche(
        slug="guerre-froide",
        title="La guerre froide (1947-1991)",
        subtitle="Bipolarité, crises et fin du communisme",
        central="Pourquoi un monde bipolaire pendant 45 ans ?",
        intro=(
            "Après 1945, l'alliance contre le nazisme se brise. Deux blocs "
            "s'opposent — États-Unis et URSS — sans jamais s'affronter "
            "directement (peur du nucléaire). Cet équilibre de la terreur "
            "structure le monde entier pendant 45 ans, jusqu'à la chute de "
            "l'URSS en 1991. Berlin est le symbole de cette guerre froide."
        ),
        branches=[
            Branch(
                label="Origine et bipolarité",
                color="rose",
                icon="1",
                leaves=[
                    Leaf(
                        "Rupture de l'alliance",
                        tip="L'alliance USA-URSS, scellée pour vaincre l'Axe, se brise dès 1945-46. Désaccords sur l'avenir de l'Europe occupée.",
                    ),
                    Leaf(
                        "Doctrine Truman (mars 1947)",
                        tip="« Endiguement » du communisme : les USA s'engagent à soutenir tout pays menacé par le communisme.",
                    ),
                    Leaf(
                        "Plan Marshall (juin 1947)",
                        tip="Aide économique américaine à l'Europe occidentale (13 milliards de dollars). Refusé par les pays de l'Est.",
                    ),
                    Leaf(
                        "Doctrine Jdanov (sept. 1947)",
                        tip="Réplique soviétique : structure le bloc de l'Est (Kominform). Le monde est désormais divisé en deux camps.",
                    ),
                    Leaf(
                        "Les deux blocs",
                        examples=[
                            "Bloc de l'Ouest : USA, démocratie libérale, économie de marché. OTAN (1949)",
                            "Bloc de l'Est : URSS, parti unique, économie planifiée. Pacte de Varsovie (1955)",
                        ],
                    ),
                ],
            ),
            Branch(
                label="Les grandes crises",
                color="indigo",
                icon="2",
                leaves=[
                    Leaf(
                        "Blocus de Berlin (1948-1949)",
                        examples=[
                            "Staline coupe les accès terrestres à Berlin-Ouest",
                            "Les Alliés organisent un pont aérien (Luftbrücke) pendant 11 mois",
                            "Création de la RFA (mai 1949) puis de la RDA (oct. 1949)",
                        ],
                    ),
                    Leaf(
                        "Guerre de Corée (1950-1953)",
                        tip="Première « guerre par procuration » : Corée du Nord (soutenue par URSS et Chine) attaque Corée du Sud (soutenue par USA et ONU). Frontière : 38e parallèle, toujours en vigueur.",
                    ),
                    Leaf(
                        "Crise des missiles de Cuba (oct. 1962)",
                        tip="L'URSS installe des missiles à Cuba (à 150 km de la Floride). Kennedy impose un blocus naval. Le monde frôle la guerre nucléaire pendant 13 jours. Khrouchtchev recule.",
                    ),
                    Leaf(
                        "Guerre du Vietnam (1965-1975)",
                        tip="Les USA s'enlisent face à la guérilla communiste. Première défaite militaire américaine. Profond traumatisme. Évacuation de Saïgon en avril 1975.",
                    ),
                ],
            ),
            Branch(
                label="Berlin, symbole de la guerre froide",
                color="emerald",
                icon="B",
                leaves=[
                    Leaf(
                        "Une ville coupée en quatre (1945-49)",
                        tip="Comme l'Allemagne, Berlin est divisée en 4 zones d'occupation : USA, RU, France, URSS. Mais la ville est entièrement en zone soviétique.",
                    ),
                    Leaf(
                        "Berlin-Ouest, enclave libre",
                        tip="Symbole de la liberté en plein cœur du bloc de l'Est. Vitrine du capitalisme. Beaucoup d'Allemands de l'Est passent à l'Ouest par Berlin.",
                    ),
                    Leaf(
                        "Construction du Mur (13 août 1961)",
                        tip="La RDA construit le Mur de Berlin pour stopper l'hémorragie d'Allemands de l'Est vers l'Ouest. ~140 morts en tentant de le franchir.",
                    ),
                    Leaf(
                        "Chute du Mur (9 novembre 1989)",
                        tip="Sous la pression populaire, la RDA ouvre les frontières. Symbole mondial de la fin de la guerre froide.",
                    ),
                    Leaf(
                        "Réunification allemande",
                        examples=["3 octobre 1990 : la RDA est intégrée à la RFA"],
                    ),
                ],
            ),
            Branch(
                label="Détente et fin",
                color="violet",
                icon="3",
                leaves=[
                    Leaf(
                        "Détente (années 1970)",
                        examples=[
                            "Accords SALT (1972) : limitation des armes stratégiques",
                            "Conférence d'Helsinki (1975) : reconnaissance des frontières et des droits de l'homme",
                        ],
                        tip="Coexistence pacifique : on garde les armes mais on dialogue.",
                    ),
                    Leaf(
                        "Reagan durcit le ton (années 1980)",
                        tip="Élu en 1981, il qualifie l'URSS d'« Empire du mal » et relance la course aux armements (programme « Guerre des étoiles »).",
                    ),
                    Leaf(
                        "Gorbatchev et la perestroïka",
                        examples=[
                            "Mikhaïl Gorbatchev arrive au pouvoir en 1985",
                            "Glasnost (transparence) : ouverture politique, liberté d'expression",
                            "Perestroïka (restructuration) : réformes économiques",
                        ],
                    ),
                    Leaf(
                        "1989 : effondrement de l'Est",
                        examples=[
                            "Pologne, Hongrie, Allemagne de l'Est, Tchécoslovaquie, Roumanie",
                            "Régimes communistes tombent l'un après l'autre",
                        ],
                    ),
                    Leaf(
                        "Fin de l'URSS (25 décembre 1991)",
                        tip="Démission de Gorbatchev, dissolution de l'URSS, naissance de 15 nouveaux États. Fin officielle de la guerre froide.",
                    ),
                ],
            ),
            Branch(
                label="Une « guerre » sans affrontement direct",
                color="amber",
                icon="!",
                leaves=[
                    Leaf(
                        "L'équilibre de la terreur",
                        tip="USA et URSS ne s'affrontent jamais directement par peur de la destruction mutuelle (armes nucléaires).",
                    ),
                    Leaf(
                        "Guerres « périphériques »",
                        tip="Les deux blocs s'opposent par pays interposés : Corée, Vietnam, Afghanistan, Angola...",
                    ),
                    Leaf(
                        "Course aux armements et à l'espace",
                        examples=[
                            "Spoutnik 1 (1957) : 1er satellite, lancé par l'URSS",
                            "Apollo 11 (1969) : premier homme sur la Lune (Armstrong, USA)",
                        ],
                    ),
                    Leaf(
                        "Espionnage, propagande, culture",
                        tip="KGB / CIA, films d'espionnage, JO comme champ de bataille symbolique (boycotts en 1980 et 1984).",
                    ),
                    Leaf(
                        "Plan type pour un DC sur Berlin / la guerre froide",
                        tip="1. La naissance de la rivalité (1947, deux blocs). 2. Une ville/un monde coupé en deux (Mur, crises). 3. La fin (Gorbatchev, 1989, 1991).",
                    ),
                ],
            ),
        ],
    ),
    # ------------------------------------------------------------------ 5
    Fiche(
        slug="amenager-territoire",
        title="Aménager le territoire français (géo)",
        subtitle="Acteurs, espaces, inégalités, exemples concrets",
        central="Comment et pourquoi aménager le territoire ?",
        intro=(
            "Aménager le territoire, c'est l'organiser pour qu'il fonctionne mieux : "
            "réduire les inégalités entre régions, accompagner le développement, "
            "garantir un accès égal aux services. C'est un enjeu majeur dans une "
            "France où coexistent métropoles dynamiques et territoires en difficulté."
        ),
        branches=[
            Branch(
                label="Pourquoi aménager ?",
                color="rose",
                icon="1",
                leaves=[
                    Leaf(
                        "Réduire les inégalités",
                        tip="Entre les métropoles dynamiques et les territoires en difficulté (ruraux, anciens bassins industriels).",
                    ),
                    Leaf(
                        "Accompagner le développement",
                        tip="Construire les infrastructures dont l'économie a besoin : transports, énergie, fibre, logements.",
                    ),
                    Leaf(
                        "Anticiper les mutations",
                        examples=[
                            "Transition écologique (énergies renouvelables, mobilités douces)",
                            "Démographie (vieillissement, métropolisation)",
                            "Mondialisation (interconnexion des territoires)",
                        ],
                    ),
                    Leaf(
                        "Garantir l'accès aux services publics",
                        tip="Écoles, hôpitaux, transports, internet : on doit y avoir accès partout en France, pas seulement dans les grandes villes.",
                    ),
                ],
            ),
            Branch(
                label="Les acteurs",
                color="indigo",
                icon="2",
                leaves=[
                    Leaf(
                        "L'État",
                        examples=[
                            "DATAR (1963) : Délégation à l'aménagement du territoire",
                            "Aujourd'hui : ANCT (Agence nationale de la cohésion des territoires)",
                        ],
                        tip="Définit la stratégie globale, finance les grandes infrastructures.",
                    ),
                    Leaf(
                        "Les collectivités locales",
                        examples=["Régions (13 en métropole)", "Départements (~96 en métropole)", "Communes (~35 000)"],
                        tip="Décentralisation depuis les années 1980 : elles ont de plus en plus de compétences (transports, lycées, collèges...).",
                    ),
                    Leaf(
                        "L'Union européenne",
                        tip="Politique de cohésion : fonds structurels (FEDER, FSE) pour réduire les écarts entre régions européennes.",
                    ),
                    Leaf(
                        "Les acteurs privés",
                        examples=["Entreprises (implantation industrielle)", "Promoteurs immobiliers", "Aménageurs"],
                    ),
                    Leaf(
                        "Les habitants",
                        tip="Enquêtes publiques, associations, contestations (manifestations contre des projets jugés inutiles).",
                    ),
                ],
            ),
            Branch(
                label="Les espaces clés",
                color="emerald",
                icon="3",
                leaves=[
                    Leaf(
                        "Les métropoles",
                        examples=["Paris (mondiale)", "Lyon, Marseille, Toulouse, Lille, Bordeaux, Nantes (régionales)"],
                        tip="Concentrent emplois, fonctions de décision, étudiants, recherche. Moteurs de la croissance.",
                    ),
                    Leaf(
                        "Les espaces productifs",
                        examples=[
                            "Industriels : vallée de la Seine, Rhône, Lyon-Grenoble",
                            "Agricoles : Beauce, Bretagne, Sud-Ouest",
                            "Touristiques : littoraux méditerranéen et atlantique, montagnes",
                            "De services : tertiaire concentré dans les métropoles",
                        ],
                    ),
                    Leaf(
                        "Les espaces ruraux",
                        tip="Très divers : zones rurales en croissance (périurbain) ou en déprise (« diagonale du vide » des Ardennes aux Pyrénées). Vieillissement, désertification médicale.",
                    ),
                    Leaf(
                        "Les outre-mer (DROM)",
                        examples=["Guadeloupe, Martinique, Guyane, La Réunion, Mayotte"],
                        tip="Enjeux spécifiques : éloignement, économies fragiles, biodiversité, vulnérabilité aux risques naturels.",
                    ),
                    Leaf(
                        "Les littoraux",
                        tip="Forte attractivité (héliotropisme) → pression démographique et touristique, érosion, conflits d'usage.",
                    ),
                ],
            ),
            Branch(
                label="Inégalités et fractures",
                color="violet",
                icon="!",
                leaves=[
                    Leaf(
                        "Métropoles vs périphéries",
                        tip="Les métropoles concentrent les richesses ; les périphéries (banlieues, périurbain, ruralités) se sentent parfois oubliées.",
                    ),
                    Leaf(
                        "Centre / banlieues / périurbain",
                        examples=[
                            "Centres-villes : densément peuplés, services nombreux",
                            "Banlieues : très diverses (résidentielles aisées, quartiers populaires)",
                            "Périurbain : maisons individuelles, dépendance à la voiture",
                        ],
                    ),
                    Leaf(
                        "Désindustrialisation",
                        examples=[
                            "Anciens bassins industriels : Nord-Pas-de-Calais, Lorraine, Saint-Étienne",
                            "Friches industrielles, chômage élevé, reconversions difficiles",
                        ],
                    ),
                    Leaf(
                        "Fracture numérique",
                        tip="Zones blanches : pas de couverture mobile ou internet rapide. Plan Très haut débit pour y remédier (fibre partout d'ici 2030).",
                    ),
                    Leaf(
                        "Conflits d'usage",
                        examples=["NIMBY (« pas dans mon jardin ») : éoliennes, prisons, lignes à haute tension"],
                        tip="Les habitants peuvent contester un aménagement perçu comme nuisible localement.",
                    ),
                ],
            ),
            Branch(
                label="Exemples d'aménagement",
                color="amber",
                icon="@",
                leaves=[
                    Leaf(
                        "Lignes à grande vitesse (LGV)",
                        examples=[
                            "Paris-Lyon (1981) : 1ʳᵉ LGV française",
                            "LGV Atlantique, Méditerranée, Est, Sud-Europe-Atlantique...",
                        ],
                        tip="Réduisent les distances-temps et favorisent les métropoles desservies.",
                    ),
                    Leaf(
                        "Ports et aéroports",
                        examples=[
                            "Le Havre, Marseille-Fos : grands ports de conteneurs",
                            "Roissy CDG : 2e aéroport européen pour le fret",
                        ],
                        tip="Hubs internationaux qui connectent la France à la mondialisation.",
                    ),
                    Leaf(
                        "Aménagements urbains",
                        examples=[
                            "Grand Paris Express : 200 km de métro automatique d'ici 2030",
                            "Tramways modernes : Bordeaux, Strasbourg, Nice, Lyon",
                            "Écoquartiers (Lyon Confluence, Bordeaux Bastide)",
                        ],
                    ),
                    Leaf(
                        "Protection et environnement",
                        examples=["10 parcs nationaux", "58 parcs naturels régionaux"],
                        tip="Concilier protection de la biodiversité et activités humaines (tourisme, agriculture).",
                    ),
                    Leaf(
                        "Plan type pour un DC sur l'aménagement",
                        tip="1. Pourquoi aménager (objectifs, défis). 2. Qui aménage (acteurs : État, collectivités, UE, privés, habitants). 3. Quelles inégalités persistent (métropoles vs périphéries, exemples concrets).",
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
