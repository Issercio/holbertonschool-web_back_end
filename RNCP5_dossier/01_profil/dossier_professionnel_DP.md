# DOSSIER PROFESSIONNEL (DP)

**Titre professionnel visé :** Développeur Web et Web Mobile (DWWM)
**Code RNCP :** 37674
**Niveau :** 5 (Bac+2)
**Référentiel :** REAC DWWM V04 — 24/05/2023

> Document conforme au modèle du Ministère du Travail, de l'Emploi et de l'Insertion.
> Le DP est complété par un livret d'évaluation (équipe campus) et les relevés de scores Holberton.
> **But** : document support pour l'entretien final avec le jury.

---

## Sommaire

1. Identité du candidat
2. Présentation du parcours du candidat
3. Activité type 1 — Développer la partie front-end d'une application web ou web mobile sécurisée
   - CP1 — Maquetter des interfaces utilisateur web ou web mobile
   - CP2 — Réaliser des interfaces utilisateur statiques web ou web mobile
   - CP3 — Développer la partie dynamique des interfaces utilisateur web ou web mobile
4. Activité type 2 — Développer la partie back-end d'une application web ou web mobile sécurisée
   - CP4 — Mettre en place une base de données relationnelle
   - CP5 — Développer des composants d'accès aux données SQL et NoSQL
   - CP6 — Développer des composants métier côté serveur
5. Titres, diplômes, CCP obtenus antérieurement
6. Déclaration sur l'honneur
7. Documents annexes illustrant la pratique professionnelle

---

## 1. Identité du candidat

| Champ | Information |
|---|---|
| Nom de naissance | JAILLE |
| Nom d'usage | JAILLE |
| Premier prénom | Dimitri |
| Date de naissance | *(à compléter)* |
| Lieu de naissance | *(à compléter)* |
| Adresse | *(à compléter)* |
| Code postal / Ville | *(à compléter)* |
| Téléphone | *(à compléter)* |
| Courriel | *(à compléter)* |

---

## 2. Présentation du parcours du candidat

Au cours de l'année scolaire 2025-2026, j'ai suivi la formation « Développeur Web et Web Mobile » (DWWM, niveau 5) à Holberton School. Cette formation intensive, fondée sur l'apprentissage par projets et le *peer-learning*, couvre l'ensemble des compétences du REAC : développement front-end (HTML, CSS, JavaScript), développement back-end (Python, Flask, SQL), gestion de bases de données, sécurité applicative et déploiement.

En parallèle, j'ai réalisé un projet professionnel pour l'entreprise **Pivoine & Lilas**, artisan fleuriste, en binôme avec **Mattieu Mourroux** (co-développeur). Ce projet consistait à concevoir et développer une application e-commerce complète (FloraShop) permettant la vente en ligne de compositions florales, la gestion d'un panier, le paiement sécurisé via Stripe et l'administration des produits et catégories.

### Formation

| Période | Intitulé de la formation | Organisme / École | Obtention |
|---|---|---|---|
| 2025-2026 | Développeur Web et Web Mobile (DWWM) — RNCP Niveau 5 | Holberton School | En cours |

### Expérience professionnelle

| Période | Intitulé du poste | Entreprise / Structure | Principales activités |
|---|---|---|---|
| Juin 2025 | Développeur Web (projet en entreprise) | Pivoine & Lilas (artisan fleuriste) | Conception, développement et déploiement d'une application e-commerce full-stack (FloraShop) : maquettage responsive, intégration HTML/CSS, développement JavaScript (panier, paiement Stripe), base de données PostgreSQL, API REST Flask-RESTX, sécurité applicative |

### Compétences complémentaires

- **Langues :** Français (langue maternelle), Anglais (technique, lecture de documentation)
- **Outils de versionnement :** Git, GitHub
- **Méthodologie :** Apprentissage par projets, peer-learning, revue de code collaborative
- **Compétences transversales :** Travail en binôme, communication technique, résolution de problèmes, veille technologique continue

---

## 3. Activité type 1 — Développer la partie front-end d'une application web ou web mobile sécurisée

### CP1 — Maquetter des interfaces utilisateur web ou web mobile

#### Exemple n°1

**Intitulé de l'exemple :** Maquettage responsive de l'application FloraShop — Pivoine & Lilas

**À quel emploi, stage ou projet cet exemple se rattache-t-il ?**

| Champ | Information |
|---|---|
| Intitulé | Projet FloraShop — application e-commerce pour Pivoine & Lilas |
| Dates | Juin 2025 |
| Lieu | Holberton School / Pivoine & Lilas |
| Activité / service | Développement Web — conception des interfaces utilisateur |

**Contexte et/ou enjeux de l'activité décrite :**

L'entreprise Pivoine & Lilas, artisan fleuriste, souhaitait disposer d'une boutique en ligne permettant à ses clients de parcourir le catalogue, d'ajouter des produits au panier et de payer en ligne. Le besoin principal était de concevoir des interfaces accessibles aussi bien sur bureau (1 280 × 800 px) que sur mobile (393 × 852 px, simulation iPhone), avec une charte graphique « vintage » fidèle à l'identité de la marque.

J'ai maquetté 16 pages HTML couvrant l'intégralité du parcours utilisateur :

- **Pages publiques :** Accueil, Shop (461 lignes), Panier (375 lignes), Checkout (588 lignes), Payment (406 lignes), Contact, Événementiel, Entreprises, Portfolio
- **Pages d'authentification :** Register, Forgot-password, Verify-code
- **Pages privées :** Account, Abonnement (182 lignes), Subscription payment (593 lignes)
- **Page d'administration :** Admin (748 lignes)

Chaque maquette intégrait une approche *mobile-first* avec deux points de rupture CSS : 900 px (tablette) et 600 px (mobile), une grille flexible (`grid-template-columns: repeat(auto-fill, minmax(260px, 1fr))`) et un menu de navigation adaptatif.

**Informations complémentaires (outils, méthodes, démarches, résultats) :**

- **Charte graphique :** couleur primaire #bc6288 (rose vintage), accent #d2a0b5, fond #fff6f2 (crème), texte #231111 (brun foncé), ombres `0 2px 12px rgba(188,98,136,0.07)`
- **Typographie :** EB Garamond (titres éditoriaux) et Inter (corps de texte), chargées via Google Fonts
- **Outils :** HTML5, CSS3 avec variables CSS (`:root` — 6 variables `--vintage-*`), Jinja2
- **Enchaînement des maquettes :** Accueil → Shop (filtres par catégorie/prix) → Panier → Checkout → Paiement Stripe → Confirmation
- **Résultat :** 16 pages maquettées et validées, couvrant les parcours client, authentification et administration ; navigation responsive avec badge compteur de panier ; conformité totale à la charte Pivoine & Lilas

---

### CP2 — Réaliser des interfaces utilisateur statiques web ou web mobile

#### Exemple n°1

**Intitulé de l'exemple :** Intégration HTML5/CSS3 responsive des interfaces FloraShop

**À quel emploi, stage ou projet cet exemple se rattache-t-il ?**

| Champ | Information |
|---|---|
| Intitulé | Projet FloraShop — application e-commerce pour Pivoine & Lilas |
| Dates | Juin 2025 |
| Lieu | Holberton School / Pivoine & Lilas |
| Activité / service | Développement Web — intégration front-end |

**Contexte et/ou enjeux de l'activité décrite :**

À partir des maquettes validées, j'ai intégré 16 templates Jinja2 en HTML5 sémantique (`<header>`, `<nav>`, `<aside>`, `<main>`, `<footer>`), accompagnés de 3 fichiers CSS totalisant 932 lignes (style.css, account.css, subscription.css). L'objectif était de produire des interfaces conformes aux maquettes, accessibles (attributs `alt` sur les images, association label/input, contraste suffisant) et parfaitement responsive sur les trois résolutions cibles.

**Techniques mises en œuvre :**

- **CSS Variables :** système de thème centralisé via `:root` avec 6 variables `--vintage-*` permettant de modifier la charte en un point unique
- **Flexbox :** navigation et alignements de conteneurs
- **CSS Grid :** grille de produits avec `auto-fill` et `minmax(260px, 1fr)`, passage de 3 colonnes (bureau) à 1 colonne (mobile)
- **Media queries :** 2 points de rupture (900 px et 600 px) — adaptation des tailles de police, marges, menus
- **Transitions :** effets visuels fluides (0,18 s à 0,3 s) pour les survols de boutons et cartes
- **Validation HTML5 :** attributs `type="email"`, `required`, `type="password"` sur les formulaires

**Informations complémentaires (outils, méthodes, démarches, résultats) :**

- **Protection XSS :** auto-échappement natif de Jinja2 activé par défaut
- **Google reCAPTCHA v2 :** intégré sur register.html pour bloquer les inscriptions automatisées
- **Composants réutilisables :** barre de navigation commune, pied de page, formulaire de paiement Stripe Éléments
- **Résultat :** interfaces conformes aux maquettes sur bureau, tablette et mobile ; formulaires accessibles et sécurisés ; intégration validée avec le moteur de templates Flask/Jinja2

---

### CP3 — Développer la partie dynamique des interfaces utilisateur web ou web mobile

#### Exemple n°1

**Intitulé de l'exemple :** Développement JavaScript du panier, du paiement Stripe et de l'authentification côté client

**À quel emploi, stage ou projet cet exemple se rattache-t-il ?**

| Champ | Information |
|---|---|
| Intitulé | Projet FloraShop — application e-commerce pour Pivoine & Lilas |
| Dates | Juin 2025 |
| Lieu | Holberton School / Pivoine & Lilas |
| Activité / service | Développement Web — interactions dynamiques front-end |

**Contexte et/ou enjeux de l'activité décrite :**

L'application nécessitait des interactions dynamiques côté client sans rechargement de page : gestion d'un panier persistant, communication avec l'API REST, authentification par JWT et paiement sécurisé via Stripe.js. J'ai développé deux fichiers JavaScript en ES6+ : **api.js** (261 lignes) et **auth.js** (59 lignes).

**Fonctionnalités dynamiques développées :**

1. **Panier (localStorage) :** ajout, suppression (`removeFromCart(idx)` avec `Array.splice`), modification des quantités, calcul automatique du total, persistance JSON dans `localStorage`, badge compteur (`cart-count`), reconstruction du DOM via `renderCart()`
2. **Communication API (classe `ApiService`) :** architecture orientée objet avec `async/await` et `fetch`, injection automatique du header `Authorization: Bearer {token}`, méthodes `login()`, `register()`, `logout()`, `getProducts()`, `getCategories()`
3. **Authentification :** stockage du JWT dans `localStorage`, mise à jour dynamique de l'interface (profil, accès admin conditionnel via `is_admin`), gestion login/logout/register
4. **Filtrage produits :** recherche par nom (`searchInput`), filtres par catégorie (chargés dynamiquement depuis l'API), filtres par plage de prix (`minPrice`, `maxPrice`), rendu dans le conteneur `productGrid`
5. **Paiement Stripe :** initialisation de Stripe.js v3, montage d'un élément carte dans `#card-element`, affichage des erreurs en temps réel (`card.on('change')`), création du PaymentIntent via l'API back-end, confirmation avec `stripe.confirmCardPayment()`, vidage du panier après succès
6. **Validation formulaires :** contrôle de correspondance des mots de passe, validation email (HTML5), champs obligatoires

**Informations complémentaires (outils, méthodes, démarches, résultats) :**

- **Architecture :** séparation des préoccupations (api.js pour les appels API, auth.js pour l'authentification)
- **ES6+ :** template literals, arrow functions, destructuring, async/await
- **Manipulation DOM :** `innerHTML`, `textContent`, `addEventListener`, affichage conditionnel (`style.display`)
- **Sécurité :** jamais de données sensibles exposées côté client, token JWT transmis uniquement via header `Authorization`
- **Résultat :** panier fonctionnel et persistant, paiement Stripe opérationnel, authentification complète avec gestion des rôles, filtrage produits en temps réel

---

## 4. Activité type 2 — Développer la partie back-end d'une application web ou web mobile sécurisée

### CP4 — Mettre en place une base de données relationnelle

#### Exemple n°1

**Intitulé de l'exemple :** Conception et mise en place de la base de données PostgreSQL FloraShop (7 tables, 6 migrations Alembic)

**À quel emploi, stage ou projet cet exemple se rattache-t-il ?**

| Champ | Information |
|---|---|
| Intitulé | Projet FloraShop — application e-commerce pour Pivoine & Lilas |
| Dates | Juin 2025 |
| Lieu | Holberton School / Pivoine & Lilas |
| Activité / service | Développement Web — base de données et modélisation |

**Contexte et/ou enjeux de l'activité décrite :**

L'application FloraShop devait stocker les utilisateurs, le catalogue de produits (7 catégories, 10 produits initiaux), les commandes avec leurs lignes, les avis clients et l'historique des prix. J'ai conçu un Modèle Conceptuel de Données (MCD) selon la méthode Merise, puis implémenté le schéma physique en PostgreSQL via l'ORM SQLAlchemy et Flask-Migrate (Alembic).

**Modèle Conceptuel de Données (MCD) — 7 entités, 6 associations :**

| Association | Entités | Cardinalités |
|---|---|---|
| PASSER | User → Order | 0,N — 0,1 (commande invité possible) |
| COMPOSER | Order → OrderItem | 1,N — 1,1 |
| RÉFÉRENCER | OrderItem → Product | 1,1 — 0,N |
| CONTENIR | Category → Product | 1,N — 1,1 |
| RÉDIGER | User → Review | 0,N — 1,1 |
| HISTORISER | Product → Price | 0,N — 1,1 |

**Tables du schéma physique :**

| Table | Colonnes clés | Particularités |
|---|---|---|
| **users** | id SERIAL PK, username VARCHAR(50) UNIQUE, email VARCHAR(120) UNIQUE, password VARCHAR(255), is_admin BOOL | Contrainte d'unicité sur username et email |
| **categories** | id SERIAL PK, name VARCHAR(100) UNIQUE, created_at DATETIME | 7 catégories initiales (Fleurs Fraîches, Vases, Parfums, etc.) |
| **products** | id SERIAL PK, name VARCHAR(255), price FLOAT, category_id FK, is_on_sale BOOL | Clé étrangère vers categories |
| **orders** | id SERIAL PK, user_id FK NULL, email VARCHAR(120), total_amount FLOAT, stripe_payment_intent_id, status VARCHAR(50) default 'pending', created_at | user_id nullable pour commandes invité |
| **order_items** | id SERIAL PK, order_id FK, product_id FK, quantity INT, price FLOAT | Prix figé au moment de l'achat |
| **reviews** | id SERIAL PK, content TEXT, rating INT, user_id FK | Avis clients |
| **prices** | id SERIAL PK, amount FLOAT, is_active BOOL, product_id FK, created_at, updated_at | Historique tarifaire avec drapeau is_active |

**Règles de gestion :**
- RG1 : Unicité username + email par utilisateur
- RG2 : Commandes possibles sans compte (user_id nullable → checkout invité)
- RG3 : Prix figé dans order_items au moment de l'achat
- RG4 : Suppression de catégorie → CASCADE sur les produits liés
- RG5 : Suppression de commande → CASCADE sur les lignes (delete-orphan)
- RG6 : Historique des prix maintenu via le drapeau is_active
- RG7 : Cycle de vie des commandes : pending → paid / failed / cancelled

**Informations complémentaires (outils, méthodes, démarches, résultats) :**

- **SGBD :** PostgreSQL (psycopg2), base `florashop` sur `localhost:5432`
- **ORM :** SQLAlchemy 2.0.23 via Flask-SQLAlchemy 3.1.1
- **Migrations :** Flask-Migrate 4.1.0 (Alembic) — 6 versions :
  1. `c672290307b5` — Migration initiale
  2. `0360f24cade9` — Refactoring initial
  3. `15543caa981b` — Extension du champ password à VARCHAR(255)
  4. `0f84d409baff` — Ajout des promotions
  5. `6c350306a292` — Ajout de la colonne is_on_sale
  6. `415260e111d3` — Retrait de product_id des reviews
- **Résultat :** base de données normalisée, 7 tables interconnectées, migrations versionnées, données initiales (7 catégories, 10 produits, 1 admin)

---

### CP5 — Développer des composants d'accès aux données SQL et NoSQL

#### Exemple n°1

**Intitulé de l'exemple :** Implémentation des composants d'accès aux données avec le pattern Repository et Facade (SQLAlchemy ORM)

**À quel emploi, stage ou projet cet exemple se rattache-t-il ?**

| Champ | Information |
|---|---|
| Intitulé | Projet FloraShop — application e-commerce pour Pivoine & Lilas |
| Dates | Juin 2025 |
| Lieu | Holberton School / Pivoine & Lilas |
| Activité / service | Développement Web — couche d'accès aux données |

**Contexte et/ou enjeux de l'activité décrite :**

Pour garantir la maintenabilité et la séparation des responsabilités, j'ai structuré la couche d'accès aux données selon le **pattern Repository**, où chaque entité (User, Product, Category, Order, Review, Price) dispose d'un repository dédié encapsulant les opérations CRUD. Un **pattern Facade** centralise l'accès à l'ensemble des repositories via un point d'entrée unique.

**Repositories implémentés :**

| Repository | Opérations | Validations |
|---|---|---|
| **UserRepository** | `get_all()`, `get_by_id()`, `create()`, `update()`, `delete()` | Unicité email et username, exclusion du mot de passe dans `to_dict()` |
| **ProductRepository** | CRUD complet | Vérification de la catégorie associée, validation du prix |
| **CategoryRepository** | `get_all()`, `get_by_id()`, `create(name)`, `update(id, name)`, `delete(id)` | Unicité du nom, suppression en cascade des produits |
| **ReviewRepository** | CRUD complet | Vérification de l'utilisateur associé |
| **PriceRepository** | Gestion de l'historique tarifaire | Drapeau `is_active` pour le prix courant |

**Pattern Facade :**

```python
class Facade:
    def __init__(self):
        self.users = UserRepository()
        self.products = ProductRepository()
        self.categories = CategoryRepository()
        self.reviews = ReviewRepository()
        self.prices = PriceRepository()
```

Ce point d'entrée unique simplifie l'accès aux données depuis les contrôleurs API et les services métier.

**Gestion transactionnelle :**
- `db.session.flush()` pour les opérations intermédiaires
- `db.session.commit()` pour la finalisation
- `db.session.rollback()` en cas d'erreur
- Cascade `delete-orphan` pour les relations Order → OrderItem

**Informations complémentaires (outils, méthodes, démarches, résultats) :**

- **ORM :** SQLAlchemy 2.0.23 — aucune requête SQL brute, prévention native des injections SQL
- **Sécurité :** mot de passe jamais exposé dans la sérialisation JSON (`to_dict()` exclut le champ `password`), conversions de type défensives (`int()`, `float()`, `str()`)
- **Architecture :** dossier `app/persistence/` pour les repositories, dossier `app/services/` pour la Facade
- **Résultat :** couche d'accès aux données découplée de la logique métier et des contrôleurs, opérations CRUD complètes avec validations, gestion transactionnelle robuste

---

### CP6 — Développer des composants métier côté serveur

#### Exemple n°1

**Intitulé de l'exemple :** Développement de l'API REST FloraShop (Flask-RESTX, Swagger, JWT, Stripe)

**À quel emploi, stage ou projet cet exemple se rattache-t-il ?**

| Champ | Information |
|---|---|
| Intitulé | Projet FloraShop — application e-commerce pour Pivoine & Lilas |
| Dates | Juin 2025 |
| Lieu | Holberton School / Pivoine & Lilas |
| Activité / service | Développement Web — logique métier et API serveur |

**Contexte et/ou enjeux de l'activité décrite :**

Le back-end de FloraShop expose une API REST documentée via Swagger (OpenAPI 3.0) et implémente les règles métier de l'e-commerce : authentification, gestion du catalogue, traitement des commandes et paiement sécurisé via Stripe. J'ai développé l'ensemble des composants métier serveur en Python avec le framework Flask et l'extension Flask-RESTX.

**Namespaces API :**

| Namespace | Endpoints principaux | Méthodes |
|---|---|---|
| `/api/v1/auth` | `/login`, `/register` | POST |
| `/api/v1/products` | `/`, `/<id>` | GET, POST, PUT, DELETE |
| `/api/v1/categories` | `/`, `/<id>` | GET, POST, PUT, DELETE |
| `/api/v1/users` | `/`, `/<id>` | GET, POST, PUT, DELETE |
| `/api/v1/reviews` | `/`, `/<id>` | GET, POST, PUT, DELETE |
| `/api/v1/payments` | `/create-payment-intent`, `/webhook` | POST |

**Composants métier développés :**

1. **Authentification JWT (PyJWT) :** génération de token à la connexion (claims : sub, email, is_admin, exp), expiration à 1 jour, injection du header `Authorization: Bearer {token}`, contrôle d'accès basé sur les rôles (`is_admin`)

2. **StripeService (paiement sécurisé) :**
   - `create_payment_intent(order_data)` : recalcul du total côté serveur (jamais de confiance envers le client), création de la commande et des lignes en base, appel à `stripe.PaymentIntent.create()`, retour du `client_secret`
   - `handle_webhook(payload, sig_header)` : vérification de la signature (`stripe.Webhook.construct_event()`), traitement des événements `payment_intent.succeeded` / `payment_intent.payment_failed`, mise à jour du statut de la commande
   - `confirm_payment(payment_intent_id)` : passage du statut à « paid »
   - Montant en centimes : `int(total * 100)`, devise EUR, metadata (order_id, email)

3. **Règles métier implémentées :**
   - Recalcul systématique du total depuis les prix en base (jamais accepté du client)
   - Cycle de vie des commandes : pending → paid / failed / cancelled
   - Prix figé dans `order_items.price` au moment de l'achat
   - Unicité des comptes utilisateurs (email + username)
   - Contrôle d'accès admin pour les opérations CRUD sensibles

**Sécurité applicative :**

| Mesure | Implémentation |
|---|---|
| Hachage des mots de passe | `werkzeug.security.generate_password_hash` / `check_password_hash` |
| Prévention injection SQL | SQLAlchemy ORM exclusivement (aucune requête SQL brute) |
| Protection XSS | Auto-échappement Jinja2 |
| Protection CORS | Flask-CORS avec liste blanche d'origines (localhost:5000, localhost:8000) |
| Anti-bot | Google reCAPTCHA v2 sur l'inscription |
| Webhook sécurisé | Vérification de la signature Stripe |

**Informations complémentaires (outils, méthodes, démarches, résultats) :**

- **Stack serveur :** Flask 3.1.0, Flask-RESTX 1.3.0, Flask-SQLAlchemy 3.1.1, Flask-Migrate 4.1.0, Flask-CORS, PyJWT, Werkzeug, python-dotenv
- **Documentation API :** Swagger UI auto-générée accessible à `http://localhost:5000/api/v1`, authentification Bearer documentée
- **Tests :** 7 scénarios exécutés (5 PASS, 1 EXPECTED FAIL Stripe test keys, 1 BLOCKED dépendant) via test_db.py et coverage 7.6.12
- **Veille sécurité :** 12 failles identifiées et documentées (F1 à F12) avec niveaux de gravité (CRITICAL, HIGH, MEDIUM), propositions de correction formulées
- **Résultat :** API REST complète et documentée, paiement Stripe fonctionnel, authentification JWT opérationnelle, sécurité auditée avec plan de remédiation

---

## 5. Titres, diplômes, CCP obtenus antérieurement

| Intitulé du titre, diplôme ou CCP | Date d'obtention | Organisme certificateur |
|---|---|---|
| *(à compléter le cas échéant)* | | |

---

## 6. Déclaration sur l'honneur

Je soussigné **Jaille Dimitri** déclare sur l'honneur que les renseignements fournis dans ce dossier professionnel sont exacts et que je suis le seul auteur des réalisations jointes, à l'exception des contributions réalisées en binôme avec Mattieu Mourroux dans le cadre du projet FloraShop.

Je m'engage à me présenter aux épreuves de validation du titre professionnel **Développeur Web et Web Mobile** (RNCP 37674).

Fait à : ______________________
Le : ______________________
Signature :

---

## 7. Documents annexes illustrant la pratique professionnelle

| N° | Intitulé du document | Nature | CP concernée |
|---|---|---|---|
| 1 | Captures d'écran — Accueil, Shop, Panier, Checkout (desktop et mobile) | Captures d'écran | CP1, CP2 |
| 2 | Charte graphique Pivoine & Lilas (palette, typographie, variables CSS) | Spécification | CP1 |
| 3 | Extraits de code HTML/CSS — templates Jinja2 et fichiers CSS | Code source | CP2 |
| 4 | Extraits de code JavaScript — api.js, auth.js (panier, Stripe, filtres) | Code source | CP3 |
| 5 | MCD Merise — 7 entités, 6 associations, diagramme | Schéma conceptuel | CP4 |
| 6 | Script SQL de création des 7 tables (SERIAL, FK, CASCADE) | Code SQL | CP4 |
| 7 | Historique des 6 migrations Alembic | Listing migrations | CP4 |
| 8 | Extraits de code — Repositories et Facade (Python/SQLAlchemy) | Code source | CP5 |
| 9 | Extraits de code — StripeService, endpoints API REST | Code source | CP6 |
| 10 | Capture Swagger UI (desktop et mobile) | Captures d'écran | CP6 |
| 11 | Tableau des 12 failles de sécurité identifiées (F1-F12) | Audit sécurité | CP3, CP6 |
| 12 | Jeux d'essai — 7 tests unitaires et d'intégration (résultats) | Tests | CP5, CP6 |
