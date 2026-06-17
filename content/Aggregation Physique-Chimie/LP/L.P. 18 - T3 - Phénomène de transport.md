---
title: L.P. 18 - T3 - Phénomène de transport
tags:
  - Agrégation
  - Physique
  - Oral
---
🎯 Structure globale (40 min)
=============================

*   **Introduction (3 min)**
*   **I. Mise en place : transport et réponse linéaire (12 min)**
*   **II. Équation de diffusion : structure et propriétés (12 min)**
*   **III. Comparaisons et applications (10 min)**
*   **Conclusion (3 min)**

* * *

🟦 1. Introduction (3 min)
==========================

### Slide 1 — Expérience

*   diffusion glycérol / eau

👉 observation :

> homogénéisation spontanée

* * *

### Slide 2 — Problématique

> Comment un système hors équilibre évolue-t-il vers l’équilibre ?

👉 idée centrale :

*   transport de grandeurs :
    *   énergie
    *   matière
    *   quantité de mouvement

* * *

🟦 I. Généralités et réponse linéaire (12 min)
==============================================

1) Types de transport
---------------------

### Slide

*   diffusion (microscopique)
*   convection (macroscopique)
*   rayonnement

👉 on se concentre sur :

> **diffusion**

* * *

2) Équilibre thermodynamique local
----------------------------------

### Slide clé

*   échelle mésoscopique :
    
$$
a \ll \delta \ll L
$$

👉 on peut définir :

*    $T(x,t)$ 
*    $P(x,t)$ 

* * *

3) Bilan énergétique
--------------------

### Slide (1D)

$$
\frac{\partial u}{\partial t} = - \frac{\partial j_Q}{\partial x}
$$

👉 structure :

*   conservation
*   flux

* * *

4) Loi phénoménologique (Fourier)
---------------------------------

### Slide clé

 $\vec{j}_Q = -\lambda \nabla T$ 

* * *

### Interprétation

*   flux ∝ gradient
*   signe :  
    → retour à l’équilibre

👉 très important :

> **réponse linéaire**

* * *

5) Généralisation
-----------------

### Slide

*   Fick :
    
$$
\vec{j} = -D \nabla n
$$

👉 message :

> même structure universelle

* * *

🟦 II. Équation de diffusion (12 min)
=====================================

1) Obtention
------------

### Slide clé

 $\frac{\partial T}{\partial t} = D_{th} \Delta T$ 

* * *

👉 avec :

$$
D_{th} = \frac{\lambda}{\rho c}
$$

* * *

2) Irréversibilité
------------------

### Slide

*   non invariant par  $t \to -t$ 

👉 message clé :

> flèche du temps

* * *

### Entropie

$$
\frac{dS}{dt} \ge 0
$$

👉 cohérence avec second principe

* * *

3) Propriété d’échelle (très important)
---------------------------------------

### Slide clé

$$
\ell \sim \sqrt{D t}
$$

* * *

### Interprétation

*   diffusion lente
*   exemple :
    *   sucre dans café

👉 punchline :

> diffusion seule = inefficace

* * *

4) Exploitation expérimentale
-----------------------------

### Slide

*   diffusion glycérol :
    
$$
D \sim \frac{d^2 \alpha^2}{\tau^2}
$$

👉 ordre de grandeur

* * *

🟦 III. Comparaison et applications (10 min)
============================================

1) Nombres sans dimension
-------------------------

### Slide

*   Reynolds :
    
$$
Re = \frac{UL}{\nu}
$$
*   Péclet :
    
$$
Pe = \frac{UL}{D}
$$

* * *

👉 interprétation :

*    $Pe \gg 1$  → convection dominante
*    $Pe \ll 1$  → diffusion dominante

* * *

2) Régime stationnaire
----------------------

### Slide

*   solution :
    
$$
T(x) = ax + b
$$

* * *

### Flux thermique

$$
\Phi = \frac{\lambda A}{L}(T_1 - T_2)
$$

* * *

👉 analogie électrique :

*   résistance thermique

* * *

3) Application
--------------

### Slide

*   double vitrage
*   isolation thermique

* * *

4) Analogies profondes (bonus fort)
-----------------------------------

### Slide

| Transport | Loi |
| --- | --- |
| chaleur | Fourier |
| matière | Fick |
| charge | Ohm |

👉 message clé :

> structure universelle du transport

* * *

🟦 Conclusion (3 min)
=====================

### Slide synthèse

*   diffusion = réponse linéaire
*   équation universelle
*   irréversibilité fondamentale

* * *

### Ouverture

*   phénomènes couplés :
    *   Seebeck
    *   Peltier

* * *

⚠️ Conseils stratégiques (très important)
=========================================

1\. Ce que le jury attend
-------------------------

*   structure :
    > conservation + loi phénoménologique
*   lien avec :
    *   thermodynamique
    *   irréversibilité

* * *

2\. Pièges
----------

❌ oublier équilibre local  
❌ réciter Fourier sans interprétation  
❌ oublier le signe du flux

* * *

3\. Ce qui fait la différence
-----------------------------

👉 dire explicitement :

> Le transport est gouverné par une réponse linéaire à un gradient d’une grandeur intensive

👉 + montrer :

*   analogies entre phénomènes
*   ordres de grandeur