"""Tests unitaires pour la fonction verifier_nombre du jeu Devine le Nombre."""
from src.main import verifier_nombre


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
