"""Tests unitaires pour la fonction verifier_nombre du jeu Devine le Nombre."""

import sys
import os

# Ajouter le répertoire 'src' au chemin de recherche des modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import verifier_nombre  # noqa: E402


def test_trop_petit():
    """Teste une tentative trop petite par rapport au nombre secret."""
    resultat = verifier_nombre(secret=42, tentative=30)
    assert resultat == ">"


def test_trop_grand():
    """Teste une tentative trop grande par rapport au nombre secret."""
    resultat = verifier_nombre(secret=42, tentative=60)
    assert resultat == "<"


def test_exact():
    """Teste une tentative exactement égale au nombre secret."""
    resultat = verifier_nombre(secret=42, tentative=42)
    assert resultat == "="
