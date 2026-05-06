# Horaire de travail
Temps total: 150 heures

## Étape 1: phase de recherche (60h)
    Étude initiale du domaine : 6h + 2h (complété)
    Peaufinage et confirmation finale de la question de recherche (calendrier plus détaillé) : 2h (complété)
    Préparation du site web du projet : 4h (complété)
    Étude approfondie du domaine : 40h
    Synthèse de l'étude : 8h -2h


## Étape 2: application des connaissances/ test d'hypothèses (60h)

    Planification, horaire détaillé, objectifs, et limites : 2h
    Application et test d'hypothèses : 58h


## Étape 3: analyse et réflexion (20h)

    Formatages des tests d'hypothèse en données analysables : 8h
    Analyse et réflexion : 8h
    Préparation de la synthèse pour le rapport : 4h


## Étape 4: rapport et présentation (10h)

    Rédaction du rapport : 7h
    Préparation présentation : 3h
    
---

# Question de recherche: 
Est-ce que l'utilisation des algorithmes de compression dans les données d'entrées leur permettent un enrichissement utilisable par les algorithmes d'apprentissage automatique?

## Limitations potentielles

### Matérielles
Ma recherche se produira sur un laptop de gaming, ma capacité d'exécution de code sera limité à ça. Mon budget consiste à trois cartons de berlingots de lait au chocolat et une demie monster (coupé verticalement).

### Théoriques
Le concept d'un code aléatoire défini par la complexité de kolmogorov introduit une limite potentielle de la compression des données bruitées (la chose la plus applicable de ma recherche). J'ai l'intuition que dans mon application des algorithmes de compression sans perte, le bruit introduit des données sera soit imcompressable ou soit introduira plus de bruitage (comme un sur-accommodement sur le bruitage qui ignorera la structure utile). Ceci risque de faire pivoter ma recherche vers des algorithmes de compression avec perte pour améliorer la performance (et éviter des failles potentiellement fondamentales des algorithmes de compression sans perte)

## Brouillon de planification
    Commencer avec un apprentissage supervisé sur des modèles linéaires, élaborer les techniques sur des modèles non-linéares (idéalement les cas MLP comme un autoencodeur)
    SOIT Explorer ensuite les cas d'apprentissage non-supervisé
    OU SOIT Explorer les cas de compression de données de perte acceptable (potentiellement la direction primaire étant donné les limites des algorithmes de compression sans perte sur des données bruitées)

## Bac à sable d'idées
    - Création d'un ACP supervisé (préservation de plus grande variation par rapport au changement des données d'entrées et l'effet sur la sortie), élaboration à un auto-encodeur
    - compression par classe -> compression de chaque données de chaque classe (dans un arbre), apprentissage par arbre. hypothèse : redondance statistique dans les données (interprétée comme chaque classe a un langage) compressé offre une meilleure
    - hypothèse: la compresssion des redondances dans les entrées offrent une meilleure valeur des données

## Commentaires sur l'étude initiale
J'ai lu des sites Wikipédia à propos de la redondance(info théo), MDL, complexité Kolmogorov, compression des données, auto-encodeurs, théorie algorithmique de l'information. Je retiens une notion centrale qui est la complexité de Kolmogorov, et son travail avec Chaitin, Solomonoff. Je trouve que cette piste me semble être digne d'une étude approfondie. De multiples articles décrivent les limites de la compression de données (ex: notion aléatoire Kolmogorov, redondance, etc... ). Avec la connexion entre la compression des données et l'apprentissage automatique, je vois une piste à explorer sur la limite des méthodes d'apprentissage automatique théorique.
* [Bitmaps](https://en.wikipedia.org/wiki/Bitmap_index):  Cool de savoir qu'il existe une méthode d'opérer sur des données comprimées mais ne semble pas trop pertinent à ma recherche
* [Redondance](https://en.wikipedia.org/wiki/Redundancy_(information_theory)): J'aime les formules simples de la redondance de l'information. Limites de compression des données
* [MDL](https://en.wikipedia.org/wiki/Minimum_description_length): Idée centrale de ma recherche, se base sur la complexité de kolmogorov
* [Complexité de Kolmogorov](https://en.wikipedia.org/wiki/Kolmogorov_complexity): Idée centrale de la compression algorithmique des données, offre une limitation importante (impossibilité de prouver l'optimalité)
* [Compression des données](https://en.wikipedia.org/wiki/Data_compression): Offre la connexion avec l'apprentissage automatique
* [Autoencodeurs](https://en.wikipedia.org/wiki/Autoencoder): Inspiration centrale de ma recherche, offre une connexion avec MDL
* [Théorie d'information algorithmique](https://en.wikipedia.org/wiki/Algorithmic_information_theory): Domaine d'étude centrale, ce serait intéressant de trouver plus de ressources utiles (comme des notes de cours ift 6161?????)

De ma lecture secondaire (liens ci-dessous), je n'ai pas trouvé d'autres articles wikipédia qui m'ont ouvert d'autres pistes.
* [Théorie de l'information (bases)](https://en.wikipedia.org/wiki/Information_theory): Entropie, pas trop d'info nouvellement pertinentes
* [Shannon (source coding theorem)](https://en.wikipedia.org/wiki/Shannon%27s_source_coding_theorem): Prends seulement en compte la fréquence des régularités du code (simolification de kolmogorov)
* [Fonction Hartley](https://en.wikipedia.org/wiki/Hartley_function): Extension de la théorie d'information, propriétés intéressantes mais pas de piste pertinente
* [Codage d'entropie](https://en.wikipedia.org/wiki/Entropy_coding): Introduit les techniques de compression par régularisation
* [Correlation totale](https://en.wikipedia.org/wiki/Total_correlation): Extension de la théorie de l'information, implique Dkl. pas de piste intéressante
* [Apprentissage Ockham](https://en.wikipedia.org/wiki/Occam_learning): Presque équivalent à l'apprentissage PAC, formalise la favorisation des explications courtes des données.
* [Apprentissage PAC](https://en.wikipedia.org/wiki/Probably_approximately_correct_learning): Apprentissage algorithmique qui essaie de généraliser en dessous d'une erreur donnée avec une certitude donnée. Piste potentiellement intéressante, mais se trouve hors du contexte 
