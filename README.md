# Projet analyse de données/Analyse catalogue Steam

Sur cette page Github, vous trouverez une analyse approfondie sur un jeu de données récupéré sur [kaggle](kaggle.com/datasets/fronkongames/steam-games-dataset/data). Vous trouverez sur celle-ci 2 notebooks. Le langage utilisé pour le premier notebook est Python et le deuxième est codé en R.

# Jeu de données

Notre jeu de données, récupéré sur kaggle a été fourni par Steam, la plateforme de référence pour acheter et jouer à des jeux vidéos sur PC.
Initialement, le jeu de données est composé plus de 120 000 jeux qui sont décrit par 40 variables regroupant des informations variées comme le nom des jeux, leur date de sortie, leur prix, les avis des utilisateurs (positifs/négatifs) et le temps de jeu moyen etc...

# Les différentes études réalisées

Vous trouverez dans les notebooks plusieurs analyses qui ont permis de répondre à plusieurs problématiques:
1) Est-ce qu'on peut regrouper les jeux dans des classes homogènes?
2) Quels sont les variables intrinsèques à un jeu qui caractérisent le succès sur Steam? Et parmi les jeux à succès, peut-on établir des classes de succès?
3) Existe-il des caractéristiques communes aux jeux d'un même genre?
4) Quel est le profil d'un jeu évalué par la presse spécialisée (le score Metacritic) ?


# Organisation des notebooks

Chacun des deux notebooks commence par la transformation et la suppression de certaines variables afin de réaliser nos analyses sur des données nettoyées. 
Le notebook Python détaille chaque choix et le notebook R contiendra uniquement les transformations.  
Le notebook R contient l'analyse 2, 3 et 4 alors que le notebook Python contiendra l'analyse 1.
