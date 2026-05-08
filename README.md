# Projet analyse de données/Analyse catalogue Steam

Sur cette page Github, vous trouverez une analyse approfondie sur un jeu de données récupéré sur [kaggle](kaggle.com/datasets/fronkongames/steam-games-dataset/data). Vous trouverez sur cette page Github deux notebooks. Le langage utilisé pour le premier notebook est Python et le deuxième est codé en R.

# Jeu de données
Notre jeu de données, récupéré sur kaggle a été fourni par Steam, la plateforme de référence pour acheter et jouer à des jeux vidéo sur PC.
Initialement, le jeu de données est composé plus de 120 000 jeux qui sont décrit par 39 variables regroupant des informations variées comme le nom des jeux, leur date de sortie, leur prix, les avis des utilisateurs (positifs/négatifs) et le temps de jeu moyen etc...

# Les différentes études réalisées
Vous trouverez dans les notebooks plusieurs analyses qui ont permis de répondre à plusieurs problématiques:
1) Quels sont les variables intrinsèques à un jeu qui caractérisent le succès sur Steam? Et parmi les jeux à succès, peut-on etablir des classes de succès?
2)  Parmi les différents genre de jeux existe-il genre qui caractérise la réussite?
3)   Est-ce qu'on peut regrouper les jeux dans des classes homogènes?
4)   Comment évolue le marché des jeux sur Steam?

# Organisation des notebooks
Dans cette partie, nous allons détailler ce que chaque notebook contient. 
Tout d'abord, chaque notebook commence par la transformation et suppression de certaines variables afin de pouvoir faire nos analyses sur des données nettoyées. Le notebook Python ira dans le détail de chaque choix alors que le notebook R contiendra uniquement les transformations.  
Puis dans le notebook R, on trouvera l'analyse 1, 2 et 4 alors que le notebook Python contiendra l'analyse 3.
