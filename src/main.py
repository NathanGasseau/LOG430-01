"""Jeu Devine le Nombre : L'utilisateur tente de trouver un nombre entre 1 et 100."""

import random


def verifier_nombre(secret, tentative):
    """Compare la tentative de l'utilisateur avec le nombre secret."""
    if tentative < secret:
        return ">"
    if tentative > secret:
        return "<"
    return "="


def devine_le_nombre():
    """Fait deviner un nombre aléatoire entre 1 et 100 par recherche binaire automatique."""
    print("🎯 Bienvenue dans le jeu : Devine le Nombre !")
    print("Je pense à un nombre entre 1 et 100... À toi de le deviner.")

    nombre_secret = random.randint(1, 100)
    compteur_tentative = 0
    trouve = False
    min_val = 1
    max_val = 100

    while not trouve:
        compteur_tentative += 1

        # Générer une tentative automatique dans la plage actuelle
        tentative = (min_val + max_val) // 2
        print(f"Tentative {compteur_tentative}: {tentative}")

        # Vérifier la tentative
        resultat = verifier_nombre(nombre_secret, tentative)

        if resultat == ">":
            print("C'est plus grand ! 🔼")
            min_val = tentative + 1
        elif resultat == "<":
            print("C'est plus petit ! 🔽")
            max_val = tentative - 1
        else:
            print(f"🎉 Bravo ! Nombre trouvé en {compteur_tentative} tentatives : {nombre_secret}")
            trouve = True


if __name__ == "__main__":
    devine_le_nombre()
