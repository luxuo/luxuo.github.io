# [Github du projet](https://github.com/luxuo/luxuo.github.io)
## Horaire de travail
Temps total: 150 heures

## Étape 1: phase de recherche (60h)
    Étude initiale du domaine : 6h + 2h (complété)
    Peaufinage et confirmation finale de la question de recherche (calendrier plus détaillé) : 2h (complété)
    Préparation du site web du projet : 4h (complété)
    Étude approfondie du domaine : 40h (35h fait)
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
    - avoir un algorithme de compression à perte qui mesure le taux optimal de perte, qui apprend la fonction du bruit, et qui permet une compression utile en fonction des deux derniers (le problème sera comment on implémente cette fonction de compression dans le contexte d'apprentissage automatique)
    - Le plus grand problème à survenir est de trouver l'implémentation idéale d'un algorithme de compression dans le contexte d'apprentissage automatique (l'extraction utile des données comprimées). si on regarde à l'idée de compression par classe, on a une application spécifique mais j'en suis convaincu qu'il existe une meilleure implémentation. Sûrement ce serait un algorithme hybride des algorithmes d'apprentissage automatique et de compression pûre.
    - Je veux un algorithme d'apprentissage de distribution qui commence comme une distribution uniforme et apprend très peu d'information (surprise de shannon) à l'ajout d'information (de nouvelles données). L'ajout d'information s'augmenterait graduellement à l'ajout des données. Si les données suivent tous la même distribution, l'ajout d'information aura un plateau pour indiquer que la distribution est confortablement apprise (sûrement contrôlé par un hyperparamètre de perte, est-ce que cet hyperparamètre peut-être appris par un algorithme décrite par une idée précédente?).

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



## Commentaires sur l'étude approfondie
#### MDL (TODO à écrire à propos)
#### Notes de cours IFT 6161 (TODO à écrire à propos)
#### [“Low-Resource” Text Classification: A Parameter-Free Classification Method with Compressors](https://aclanthology.org/2023.findings-acl.426.pdf)
    utilise un algorithme non-paramétré (une variante de k-ppv), fonction de distance NCD (normalised compression distance).
    Algo: pour x^ à prédire -> pour chaque (k plus proches) x_i concatener avec x^ pour x_ix^, comprimer x_i pour Cx_i et x_ix^ pour Cx_ix^, calculer la distance NCD et appliquer k-ppv.
    J'aimerai modifier cet algorithme pour que la compression des données soit effectuée par rapport à toute l'ensemble de données d'une classe des données d'entrainement. L'argument est que des parties individuelles de chaque x_i peuvent individuellement être considérée comme aléatoire dans le sens kolmogorov, mais ensemble, contiennent de l'information comprimable plus efficacement. On peut aussi rajouter un élément potentiellement normalisateur de la compression de toutes les données ensemble peu importe la classe. Avec ça, je pourrai essayer de créer une équation qui modélise (un gain d'information?) la séparation du langage de la classe et le langage des données qui permet aux entrées d'avoir des prédictions indépêndantes du langage des données (correspond plus au langage de la classe). L'algorithme ne sera plus capable de faire de la régression du sens de k-ppv (puisqu'il ne sera plus k-ppv).
    Les méthodes non-paramétrées n'introduisent pas un biais inductif lors de l'entraînement. Le compresseur est indépendant du type des données par nature. Le modèle du papier est universel en termes de distributions de données. Cependant, une compression sans perte exige naturellement des données non-bruitées pour bien fonctionner.
    Les résultats avec un algorithme de compression plus performant (bz2) a été trouvé d'avoir une pire performance comparé à gzip (compression moins performante). Les auteurs soupçonnent que c'est dû à la permutation de charactères par bz2 qui nuit à la performance. 
#### [Dimensionality Reduction: A Comparative Review](https://lvdmaaten.github.io/publications/papers/TR_Dimensionality_Reduction_Review_2009.pdf)
TODO Peut-être à ne pas lire... Si ma piste courante (utilisation pure des algorithmes de compression) se mène nulle part, j'y visterai ce papier...
#### [UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction](https://arxiv.org/pdf/1802.03426)
TODO Peut-être à ne pas lire... Une méthode très intéressante à étudier, mais je ne vois plus la pertinence d'y lire.
#### [The Similarity Metric](https://arxiv.org/pdf/cs/0111054)
    Mesure la similarité de deux séquences (IMPORTANT), utilise le principe de la complexité de kolmogorov
    Développe la théorie d'une distance d'information normalisée, et propose une formule de distance d'information qui utilise un algorithme de compression concrèt (au lieu de la complexité kolmogorov).
    Le papier démontre l'application de la notion de distance sur la création d'arbres de similarité des langues et des séquences d'ADN, et conclut l'utilisabilité dans ces cas.
    Je tire une notion de séquence que je vois être très importante sur l'application de la notion de distance. Par exemple, le papier utilise l'algorithme de compression lempel-ziv (gzip) pour créer un arbre de langues. L'algorithme se fie sur les récurrences de séquences binaires. La séquence d'une image est totalement différente de la séquence du langage naturel. Serait-it possible de soit trouver un algorithme ayant une différente interprétation d'une séquence, altérer la notion de séquence dans un algorithme de compression exitant, ou de créer un algorithme de compression avec un interprétation plus générale (ou même universel, ou est-ce essentiellement trouver la complexité de kolmogorov pure) ?
    Utilise ce papier comme référence théorique pour les modifications potentielles de l'algorithme modifié proposé (limitation potentielles théoriques)
#### [The Limits of AI Explainability: An Algorithmic Information Theory Approach](https://arxiv.org/pdf/2504.20676)
    Side quest de lecture. Lecture très brève. pas tant pertinent
#### [On the symmetry of algorithmic information](https://www.researchgate.net/publication/284090758_On_the_symmetry_of_algorithmic_information)
    Rien compris...
#### [Normalized Forms for Two Common Metrics](http://pnylab.com/papers/nmet/nmet.pdf)
    Espaces métrique. Étudie l'idée d'une métrique normalisée. La distance absolue prend seulement en compte le delta des éléments. Par exemple d(0.1,0.2)=d(1000.1,1000.2) dans l'espace euclédien (l2). Le papier veut prendre en compte les distances relatives. L'auteur développe 2 normalisations de métriques 
#### [Few-Shot Non-Parametric Learning with Deep Latent Variable Model](https://arxiv.org/pdf/2206.11573)
TODO à absolument lire
#### ­[Clustering by Compression](https://arxiv.org/pdf/cs/0312044)
TODO à absolument lire
