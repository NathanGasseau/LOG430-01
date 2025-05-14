import sys
import os

# Ajouter le répertoire 'src' au chemin de recherche des modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import verifier_nombre 

def test_trop_petit():
    resultat = verifier_nombre(secret=42, tentative=30)
    assert resultat == ">"

def test_trop_grand():
    resultat = verifier_nombre(secret=42, tentative=60)
    assert resultat == "<"

def test_exact():
    resultat = verifier_nombre(secret=42, tentative=42)
    assert resultat == "="
