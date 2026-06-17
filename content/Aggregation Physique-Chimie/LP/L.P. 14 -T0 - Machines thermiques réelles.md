---
title: L.P. 14 -T0 - Machines thermiques réelles
tags:
  - Agrégation
  - Physique
  - Oral
---
⚙️ Machines thermiques réelles — version support PDF (optimisée oral)
=====================================================================

* * *

PAGE 1 — TITRE + PROBLÉMATIQUE
==============================

Machines thermiques réelles : du cycle idéal aux contraintes physiques
----------------------------------------------------------------------

**Problématique :**

> Comment la thermodynamique permet-elle de passer d’un cycle idéal réversible à une description quantitative des machines réelles, en intégrant irréversibilités et contraintes de puissance ?

* * *

I — Cadre théorique : machines thermiques cycliques
===================================================

* * *

1\. Définition générale
-----------------------

Machine thermique :

> système fluide parcourant un cycle et échangeant travail et chaleur avec des réservoirs.

$$
\Delta U = 0 \quad \text{sur un cycle}
$$

Donc :

$$
W + Q_c + Q_f = 0
$$

* * *

2\. Machines dithermes
----------------------

Deux sources :

*   chaude  $T_c$ 
*   froide  $T_f$ 

Inégalité de Clausius :

$$
\frac{Q_c}{T_c} + \frac{Q_f}{T_f} \le 0
$$

👉 égalité ⇔ réversibilité

* * *

3\. Rendement et limite de Carnot
---------------------------------

$$
\eta = \frac{-W}{Q_c}
$$

Cycle de Carnot :

$$
\eta_C = 1 - \frac{T_f}{T_c}
$$

👉 résultat fondamental :

> aucun moteur réel ne dépasse Carnot

* * *

II — Pourquoi les machines réelles ne sont pas réversibles
----------------------------------------------------------

* * *

1\. Origine des irréversibilités
--------------------------------

*   transferts thermiques avec ΔT fini
*   frottements mécaniques
*   viscosité interne
*   détente non quasi-statique

👉 conséquence :

$$
\sigma > 0
$$

* * *

2\. Compromis fondamental
-------------------------

Machine idéale :

*   réversible
*   rendement maximal
*   puissance nulle

Machine réelle :

*   irréversible
*   puissance finie
*   rendement réduit

👉 idée clé :

> on paie la puissance par une perte de réversibilité

* * *

3\. Exemple conceptuel : puissance d’un moteur endoréversible
-------------------------------------------------------------

Modèle :

*   sources effectives  $T'_c, T'_f$ 
*   transferts limités

Résultat typique :

$$
P \propto (T_c - T'_c)\left(1 - \frac{T'_f}{T'_c}\right)
$$

👉 maximum pour compromis thermique

* * *

III — Du modèle aux machines réelles
====================================

* * *

1\. Limitations du cycle de Carnot
----------------------------------

*   temps infini
*   gradients thermiques nuls
*   puissance nulle

👉 donc irréalisable physiquement

* * *

2\. Nécessité d’une approche expérimentale
------------------------------------------

On ne suit plus un cycle idéal mais :

*   mesures (P, T, h)
*   reconstruction du cycle

* * *

3\. Diagrammes thermodynamiques
-------------------------------

Outils essentiels :

*    $P-h$  (frigoristes)
*    $T-s$ 
*    $P-v$ 

👉 lecture directe des transferts :

$$
q = \Delta h \quad , \quad w = -\sum q
$$

* * *

IV — Machine frigorifique réelle
================================

* * *

1\. Structure d’un cycle réel
-----------------------------

Étapes :

1.  compression
2.  condensation
3.  détente
4.  évaporation

* * *

2\. Choix du fluide
-------------------

Contraintes :

*   température d’ébullition adaptée
*   chaleur latente élevée
*   stabilité chimique

👉 enjeu industriel + environnemental

* * *

3\. Lecture énergétique sur diagramme  $P-h$ 
---------------------------------------------

Transferts :

$$
q_f = h_2 - h_1
$$
 
$$
q_c = h_4 - h_3
$$
 
$$
w = -(q_f + q_c)
$$

* * *

4\. Performance
---------------

Coefficient de performance :

$$
e = \frac{q_f}{w}
$$

Carnot :

$$
e_C = \frac{T_f}{T_c - T_f}
$$

* * *

5\. Effet des irréversibilités
------------------------------

Compression réelle :

*   entropie créée
*   augmentation du travail requis
*   baisse du COP

👉 résultat expérimental :

> perte directe de performance

* * *

V — Synthèse physique
=====================

* * *

1\. Trois niveaux de description
--------------------------------

| Niveau | Description |
| --- | --- |
| idéal | Carnot, réversible |
| semi-idéal | endoréversible |
| réel | irréversible mesuré |

* * *

2\. Idée centrale
-----------------

> Une machine réelle est une compétition entre production de travail et création d’entropie.

* * *

3\. Lecture moderne
-------------------

*   optimisation sous contraintes
*   thermodynamique hors équilibre
*   rôle des diagrammes comme “géométrie expérimentale”

* * *

CONCLUSION
==========

*   Carnot fixe une borne
*   les irréversibilités fixent la réalité
*   les diagrammes remplacent les solutions analytiques
*   la puissance impose toujours une dissipation

* * *

🔧 CE QUI REND CE PDF “AGREGATION-READY”
========================================

### indispensables :

*   schéma machine frigorifique
*   diagramme P-h annoté
*   tableau Carnot vs réel
*   encadré “irréversibilité = puissance”