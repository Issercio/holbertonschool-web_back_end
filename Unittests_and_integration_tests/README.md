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

## Ajout 28/03/2026 :

### Test de la fonction get_json

- Ajout de la classe `TestGetJson` pour tester la fonction utilitaire `get_json`.
- Les appels HTTP externes sont mockés avec `unittest.mock.patch` pour garantir l'absence de requêtes réelles.
- Les cas de test vérifient que la fonction retourne bien le payload attendu et que `requests.get` est appelé une seule fois avec la bonne URL.

Exemple de test paramétré :
- URL : http://example.com, payload : {"payload": True}
- URL : http://holberton.io, payload : {"payload": False}

## Dépendances

- `requests`
- `parameterized`

## Style

Le code respecte la norme pycodestyle (2.5) et chaque module, classe et fonction est documenté.

---

Ce fichier README sera complété à chaque nouvelle fonctionnalité ou ajout de test.
