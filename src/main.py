import random

def verifier_nombre(secret, tentative):
    if tentative < secret:
        return ">"
    elif tentative > secret:
        return "<"
    else:
        return "="

def devine_le_nombre():
    print("🎯 Bienvenue dans le jeu : Devine le Nombre !")
    print("Je pense à un nombre entre 1 et 100... À toi de le deviner.")

    nombre_secret = random.randint(1, 100)
    cptTentative = 0
    trouve = False
    min_val = 1
    max_val = 100

    while not trouve:
        cptTentative += 1

        # Générer une tentative automatique dans la plage actuelle
        tentative = (min_val + max_val) // 2
        print(f"Tentative {cptTentative}: {tentative}")

        # Vérifier la tentative
        resultat = verifier_nombre(nombre_secret, tentative)

        if resultat == ">":
            print("C'est plus grand ! 🔼")
            min_val = tentative + 1  # Augmenter la plage minimale
        elif resultat == "<":
            print("C'est plus petit ! 🔽")
            max_val = tentative - 1  # Réduire la plage maximale
        else:
            print(f"🎉 Bravo ! Vous avez trouvé le nombre {nombre_secret} en {cptTentative} tentatives.")
            trouve = True

if __name__ == "__main__":
    devine_le_nombre()
