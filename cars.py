import pygame
from config import CAR_COLORS, CARS_SIZE

# Dictionnaire pour les voitures de différentes couleurs et directions
cars_dict = {
    "left": [],
    "right": []
}

# ======================== PARTIE 2.1 ========================
# TODO : 
# 1. Parcourir la liste des couleurs (CAR_COLORS) à l'aide d'une boucle
# 2. Pour chaque couleur :
#    - Chargez l'image vers la droite ("_right") et celle vers la gauche ("_left") à l'aide de pygame.image.load().
#    - Redimensionnez chaque image à CARS_SIZE à l’aide de la fonction pygame.transform.scale().
#    - Ajoutez les images redimensionnées dans la bonne liste ("left" ou "right") du dictionnaire cars_dict.

# Écrire votre code ici : 

for color in CAR_COLORS:
    left = pygame.image.load(f"images/car_{color}_left.png")
    right = pygame.image.load(f"images/car_{color}_right.png")
    left = pygame.transform.scale(left, CARS_SIZE)
    right = pygame.transform.scale(right, CARS_SIZE)
    cars_dict["left"].append(left)
    cars_dict["right"].append(right)


# ===============================================================
