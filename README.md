### ✍️ Auteur
- Nom : Nathan Gasseau
- Cours : LOG430-01
- Session : ÉTÉ 2025


# 🎯 Devine le Nombre

Cette application console Python simule un jeu où l'ordinateur devine automatiquement un nombre généré aléatoirement entre 1 et 100. En utilisant une stratégie de recherche dichotomique, le programme ajuste ses tentatives en fonction des indices reçus (« plus grand » ou « plus petit ») jusqu'à trouver le bon nombre. Aucune saisie manuelle n'est requise.

---

## 🔧 Instructions d’exécution

### Prérequis

- Python 3.10 ou plus récent
- Un terminal ou un IDE comme VS Code

### Étapes pour exécuter l'application

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/NathanGasseau/LOG430-01.git
2. **Se placer dans le bon répertoire:**
   ```bash
   cd "LOG430-01"
2. **Installer les packages:**
   ```bash
   pip install -r requirements.txt
3. **Lancer le jeu:**
   ```bash
   python3 src/main.py
# 📁 Structure du projet
    LOG430-01/
    │
    ├── src/                  # Contient le code source principal
    │   └── main.py           # Script principal du jeu
    ├── tests/                # Contient les tests
    │   └── main_test.py      # Script principal du test du jeu
    │
    ├── .gitignore            # Fichiers à ignorer par Git
    ├── compose.yaml          # Fichier de config Docker Compose
    ├── Dockerfile            # Fichier de condig Docker
    ├── README.md             # Ce fichier
    └── requirements.txt      # Fichier contenant les packages à intstaller
