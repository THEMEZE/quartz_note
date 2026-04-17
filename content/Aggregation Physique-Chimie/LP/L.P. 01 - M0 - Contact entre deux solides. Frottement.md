---
title: L.P. 01 - M0 - Contact entre deux solides. Frottement
tags:
  - Agrégation
  - Physique
  - Oral
---
🎯 Structure globale (40 min)
=============================

*   **Introduction (3 min)**
*   **I. Cinématique et actions de contact (10 min)**
*   **II. Lois du frottement solide (12 min)**
*   **III. Application : oscillateur à frottement solide (12 min)**
*   **Conclusion (3 min)**

* * *

🟦 1. Introduction (3 min)
==========================

### Slide 1 — Accroche

*   marcher, freiner, tenir un objet

👉 question :

> comment modéliser le contact entre solides ?

* * *

### Slide 2 — Difficulté

*   contact réel = zone déformée
*   modèle :  
    → **contact ponctuel**

👉 objectif :

*   lois macroscopiques efficaces

* * *

🟦 I. Description du contact (10 min)
=====================================

1) Cinématique du contact
-------------------------

### Slide clé

$$
\vec{v}_g(S_1/S_2) = \vec{v}(I_g \in S_1) - \vec{v}(I_g \in S_2)
$$

* * *

### Cas importants

*    $\vec{v}_g = 0$  → **adhérence**
*    $\vec{v}_g \neq 0$  → **glissement**

* * *

2) Exemple fondamental : roulement
----------------------------------

### Slide

$$
\dot{x}_C = R \omega
$$

👉 message clé :

> pas de glissement ≠ pas de mouvement

* * *

3) Actions de contact
---------------------

### Slide

$$
\vec{R} = \vec{N} + \vec{T}
$$
*    $\vec{N}$  : normale
*    $\vec{T}$  : tangente (frottement)

* * *

👉 point important :

*   pas de moment si contact ponctuel

* * *

🟦 II. Lois d’Amontons-Coulomb (12 min)
=======================================

1) Frottement statique
----------------------

### Slide clé

$$
|\vec{T}| \leq \mu_s |\vec{N}|
$$

* * *

### Interprétation

*   force d’ajustement
*   empêche le mouvement

* * *

2) Frottement dynamique
-----------------------

### Slide clé

$$
|\vec{T}| = \mu_d |\vec{N}|
$$

avec :

*    $\vec{T} \parallel \vec{v}_g$ 
*    $\vec{T} \cdot \vec{v}_g < 0$ 

* * *

👉 message clé :

> force dissipative

* * *

3) Résultats expérimentaux
--------------------------

### Slide

*    $\mu_s > \mu_d$ 
*   indépendance :
    *   surface
    *   masse

👉 très contre-intuitif → important de le dire

* * *

4) Interprétation microscopique
-------------------------------

### Slide

*   surfaces rugueuses
*   aire réelle  $S_r \ll S_a$ 

👉 relation :

$$
T \propto S_r \propto N
$$

* * *

5) Exemple : plan incliné
-------------------------

### Slide

$$
\tan \alpha = \mu_s
$$

👉 expérience simple

* * *

6) Aspect énergétique
---------------------

### Slide clé

$$
\mathcal{P} = \vec{T} \cdot \vec{v}_g \leq 0
$$

* * *

### Message fort

*   dissipation
*   conversion → chaleur

👉 MAIS :

> peut être moteur (marche, roue)

* * *

🔥 Transition
=============

> Le frottement modifie profondément la dynamique

* * *

🟦 III. Oscillateur avec frottement solide (12 min)
===================================================

1) Mise en équation
-------------------

### Slide clé

$$
m\ddot{x} = -kx + T
$$

avec :

$$
T = \pm \mu mg
$$

* * *

2) Zone d’arrêt
---------------

### Slide clé

$$
|x| < a = \frac{\mu mg}{k}
$$

* * *

👉 message :

> pas une position d’équilibre → une **plage**

* * *

3) Dynamique
------------

### Slide

*   deux équations :
    
$$
\ddot{x} + \omega_0^2 x = \pm a
$$

* * *

👉 interprétation :

*   oscillateur harmonique
*   centre déplacé

* * *

4) Résultat clé
---------------

### Slide

*   amplitudes :
    
$$
x_n = x_0 - 2na
$$

👉 décroissance **linéaire**

* * *

5) Portrait de phase
--------------------

### Slide

*   arcs de cercles
*   centres :
    *    $+a$ 
    *    $-a$ 

* * *

👉 très bon point jury :

*   représentation géométrique

* * *

6) Comparaison frottement fluide
--------------------------------

### Slide

| Frottement | Amortissement |
| --- | --- |
| fluide | exponentiel |
| solide | linéaire |

* * *

👉 message :

> dynamique non linéaire

* * *

🟦 Conclusion (3 min)
=====================

### Slide synthèse

*   contact = interaction complexe
*   lois phénoménologiques
*   frottement = dissipatif mais utile

* * *

### Ouverture

*   tribologie
*   lubrification
*   milieux granulaires

* * *

⚠️ Conseils stratégiques (très important)
=========================================

1\. Ce que le jury attend
-------------------------

*   distinction :
    *   adhérence / glissement
*   compréhension énergétique
*   application non triviale (oscillateur)

* * *

2\. Pièges
----------

❌ dire que T = µN toujours  
❌ oublier le cas statique  
❌ confondre vitesse nulle et repos

* * *

3\. Ce qui fait la différence
-----------------------------

👉 dire explicitement :

> Le frottement statique est une force d’ajustement, pas une loi constitutive stricte

👉 + montrer :

*   zone d’arrêt
*   non-linéarité