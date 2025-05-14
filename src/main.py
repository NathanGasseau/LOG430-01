import random

def devine_le_nombre():
    print("🎯 Bienvenue dans le jeu : Devine le Nombre !")
    print("Je pense à un nombre entre 1 et 100... À toi de le deviner.")

    nombre_secret = random.randint(1, 100)
    tentative = 0
    trouve = False

    while not trouve:
        try:
            guess = int(input("Entrez votre supposition : "))
            tentative += 1

            if guess < nombre_secret:
                print("C'est plus grand ! 🔼")
            elif guess > nombre_secret:
                print("C'est plus petit ! 🔽")
            else:
                print(f"🎉 Bravo ! Vous avez trouvé le nombre {nombre_secret} en {tentative} tentatives.")
                trouve = True
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

if __name__ == "__main__":
    devine_le_nombre()
