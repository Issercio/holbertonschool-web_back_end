# Unittests_and_integration_tests

Ce dossier contient des modules utilitaires, des clients, des fixtures et des tests unitaires pour la manipulation de structures de données imbriquées et l'interfaçage avec l'API GitHub.

## Fichiers présents

- `utils.py` : Fonctions utilitaires génériques (accès à des maps imbriquées, requêtes JSON, décorateur de mémoïsation).
- `client.py` : Client pour interagir avec l'API GitHub d'une organisation.
- `fixtures.py` : Jeux de données de test pour simuler des réponses d'API.
- `test_utils.py` : Tests unitaires pour les fonctions utilitaires, notamment `access_nested_map`.

## Tests

Les tests sont écrits avec `unittest` et `parameterized`.

### Exécution des tests

```bash
python3 -m unittest Unittests_and_integration_tests/test_utils.py
```

## Dépendances

- `requests`
- `parameterized`

## Style

Le code respecte la norme pycodestyle (2.5) et chaque module, classe et fonction est documenté.

---

Ce fichier README sera complété à chaque nouvelle fonctionnalité ou ajout de test.
