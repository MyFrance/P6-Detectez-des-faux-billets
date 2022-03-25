# P6-Detectez-des-faux-billets (80h)

# Compétences évaluées
#### Réaliser une ACP
#### Utiliser un algorithme de clustering de type Kmeans
#### Modéliser grâce à la régression logistique
#### Interpréter une ACP

# Prérequis
Pour ce projet, il sera nécessaire de savoir manipuler des données en Python. Également, vous devrez effectuer une analyse de statistique descriptive, ainsi qu'une analyse en composantes principales, une classification automatique, et une modélisation de type régression logistique.

# Scénario
Votre société de consulting informatique vous propose une nouvelle mission au ministère de l'Intérieur, dans le cadre de la lutte contre la criminalité organisée, à l'Office central pour la répression du faux monnayage. Votre mission si vous l'acceptez : créer un algorithme de détection de faux billets.

# Mission
Afin d'introduire votre analyse, effectuez une brève description des données (analyses univariées et bivariées).
#### Vous réaliserez une analyse en composantes principales de l'échantillon, en suivant toutes ces étapes :

- analyse de l'éboulis des valeurs propres ;
- représentation des variables par le cercle des corrélations ;
- représentation des individus par les plans factoriels ;
- analyser de la qualité de représentation et la contribution des individus.

Pour chacune de ces étapes, commentez les résultats obtenus. La variable donnant la nature Vrai/Faux du billet sera utilisée comme variable illustrative.

Appliquez un algorithme de classification, puis analysez le résultat obtenu.

Visualisez la partition obtenue dans le premier plan factoriel de l'ACP, puis analysez-la.

Modélisez les données à l'aide d'une régression logistique. Grâce à celle-ci, vous créerez un programme capable d'effectuer une prédiction sur un billet, c'est-à-dire de déterminer s'il s'agit d'un vrai ou d'un faux billet. Pour chaque billet, votre algorithme de classification devra donner la probabilité que le billet soit vrai. Si cette probabilité est supérieure ou égale à 0.5, le billet sera considéré comme vrai. Dans le cas contraire, il sera considéré comme faux.
