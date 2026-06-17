---
title: L.P. 13 - T0 - Évolution et condition d’équilibre d’un système thermodynamique fermé
tags:
  - Agrégation
  - Physique
  - Oral
---
🧭 FIL DIRECTEUR (à mettre implicitement dans le PDF)
=====================================================

> Un système fermé évolue spontanément vers un état qui maximise l’entropie.  
> Cette contrainte peut se reformuler comme une minimisation de potentiels thermodynamiques adaptés aux conditions de contact avec l’extérieur.

* * *

🧱 STRUCTURE OPTIMALE DU PDF (40 min)
=====================================

* * *

PAGE 1 — Titre + problématique
==============================

**Évolution et équilibre d’un système thermodynamique fermé**

Problématique :

> Comment le second principe impose-t-il une dynamique vers l’équilibre et conduit-il à des potentiels thermodynamiques minimaux selon les contraintes externes ?

* * *

I — Système isolé : principe variationnel fondamental
=====================================================

1\. Variables internes / contrôles
----------------------------------

*   Système composé : A + B
*   Contraintes globales :
    
$$
U = U_A + U_B,\quad V = V_A + V_B
$$
*   Variables internes :
    
$$
(U_A, V_A)
$$

* * *

2\. Second principe
-------------------

$$
dS_{\text{total}} \ge 0
$$

Développement :

$$
dS = \left(\frac{1}{T_A} - \frac{1}{T_B}\right)dU_A + \left(\frac{P_A}{T_A} - \frac{P_B}{T_B}\right)dV_A
$$

* * *

3\. Condition d’équilibre
-------------------------

À l’équilibre :

$$
T_A = T_B,\quad P_A = P_B
$$

👉 message clé :

> l’équilibre correspond à un extremum d’entropie sous contraintes globales

* * *

II — Systèmes en contact : apparition des potentiels thermodynamiques
---------------------------------------------------------------------

* * *

1\. Contact avec thermostat (T fixé)
------------------------------------

On considère T₀ imposée.

On introduit :

$$
F^* = U - T_0 S
$$

* * *

2\. Critère d’évolution
-----------------------

$$
\Delta F^* \le 0
$$

Donc :

> le système évolue vers une minimisation de  $F^*$ 

* * *

3\. Interprétation physique
---------------------------

*   système isotherme
*   échange thermique avec thermostat
*   travail extrait max :
    
$$
W_{\max} = -\Delta F
$$

👉 message :

> F est une énergie “utile” sous contrainte thermique

* * *

III — Contact thermique + mécanique : Gibbs et structure des équilibres
-----------------------------------------------------------------------

* * *

1\. Pression imposée
--------------------

On ajoute un pressiostat :

$$
G = U - TS + PV
$$

ou à T₀, P₀ fixés :

$$
G^* = G(T_0,P_0)
$$

* * *

2\. Critère d’évolution
-----------------------

$$
\Delta G^* \le 0
$$

* * *

3\. Condition d’équilibre
-------------------------

Minimisation de G :

$$
dG = 0 \Rightarrow T=T_0,\; P=P_0
$$

* * *

4\. Lecture physique
--------------------

*   G gouverne les transformations chimiques et de phase
*   coexistence : minimisation globale avec contraintes

👉 message :

> l’équilibre est sélectionné par un potentiel adapté aux contraintes extérieures

* * *

IV — Stabilité et interprétation profonde
-----------------------------------------

* * *

1\. Condition de stabilité
--------------------------

On impose :

*   stabilité ⇔ minimum du potentiel
*   instabilité ⇔ convexité perdue

Exemples :

$$
C_V > 0,\quad \chi_T > 0
$$

* * *

2\. Lecture géométrique
-----------------------

*   entropie : concave
*   énergie libre : convexe

* * *

3\. Idée centrale
-----------------

> Le second principe impose une dynamique monotone vers un minimum thermodynamique.

* * *

V — Vision unificatrice (très importante pour jury)
===================================================

1\. Schéma conceptuel
---------------------

| Conditions imposées | Potentiel minimisé |
| --- | --- |
| isolé (U,V fixés) | S maximisée |
| T fixé | F minimisée |
| T,P fixés | G minimisée |

* * *

2\. Lecture moderne
-------------------

*   dynamique dissipative
*   système non hamiltonien
*   analogie mécanique dissipative :
    
$$
\lambda \dot{x} = -\frac{dV}{dx}
$$

* * *

3\. Message final
-----------------

> La thermodynamique est une théorie variationnelle contrainte par les conditions de couplage avec l’extérieur.

* * *

🎯 CE QUI FAIT UN BON PDF ICI
=============================

### À inclure absolument

*   1 schéma de système A/B
*   1 diagramme de potentiel (F, G)
*   1 tableau des potentiels
*   1 encadré stabilité
*   1 analogie mécanique dissipative

### À éviter

*   démonstrations longues
*   répétitions du second principe
*   texte continu