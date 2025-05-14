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

    while not trouve:
        try:
            tentative = int(input("Entrez votre supposition : "))
            cptTentative += 1

            if (verifier_nombre(nombre_secret, tentative) == ">"):
                print("C'est plus grand ! 🔼")
            elif (verifier_nombre(nombre_secret, tentative) == "<"):
                print("C'est plus petit ! 🔽")
            else:
                print(f"🎉 Bravo ! Vous avez trouvé le nombre {nombre_secret} en {cptTentative} tentatives.")
                trouve = True
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

if __name__ == "__main__":
    devine_le_nombre()
