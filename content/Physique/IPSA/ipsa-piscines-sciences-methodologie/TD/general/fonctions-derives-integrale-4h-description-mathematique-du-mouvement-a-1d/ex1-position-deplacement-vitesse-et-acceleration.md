---
title: "Exercice 1 — Position, déplacement, vitesse et accélération"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/fonctions-derives-integrale-4h-description-mathematique-du-mouvement-a-1d/index|⬅ Retour]] · <a href="/pdfs/td3_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td3_PhV110.pdf" target="_blank" rel="noopener">📄 PDF</a> · <a href="/pdfs/td3_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 1. Position, déplacement, vitesse et accélération

Ce premier exercice pose les bases de la description mathématique du mouvement à une dimension (cinématique 1D) sur un axe $(Ox)$.

**1.**

  **a)** **Notions fondamentales**



(a) Expliquer la différence entre un référentiel et un repère. Citer quelques exemples.

(b) Définitions : forme différentielle et dérivée
    

- Représenter sur un schéma l'axe $(Ox)$ et la position de $M$ à différents instants $t$, séparés par un intervalle de temps identique.
- Rappeler la définition du déplacement $\Delta x$, de la vitesse moyenne $v_{x,\text{moy}}(t)$ et de l'accélération moyenne $a_{x,\text{moy}}(t)$ entre $t_1$ et $t_2 = t_1 + \Delta t$.
- Rappeler la définition du déplacement élémentaire $\mathrm{d}x$, de la vitesse instantanée $v_x(t)$ et de l'accélération $a_x(t)$.

(c) Distinction entre grandeurs algébriques et normes :
    

- Différence entre $v_x(t)$ et $v(t) = \|\vec{v}(t)\|$ ? Dans quel cas sont-elles égales ?
- Interpréter physiquement le signe de $x(t)$, $\mathrm{d}x$, $v_x(t)$ et $a_x(t)$.
- Préciser le signe de $v_x$ et $a_x$ si le mobile se déplace vers les $x$ croissants en accélérant, puis vers les $x$ décroissants en ralentissant.

(d) Forme intégrale :
    

- Exprimer $x(t)$ à partir de $v_x(t)$ et $x_0 = x(0)$.
- Exprimer $v_x(t)$ à partir de $a_x(t)$ et $v_x(0)$.

> [!example]- 📝 Solution détaillée
> **Résolution des notions fondamentales**
>
> (a) Un **référentiel** est un solide de référence auquel est liée une horloge. Un **repère** est un système d'axes mathématiques muni d'une origine $O$ et de vecteurs unitaires liant la géométrie au référentiel.\\
>    *Exemples*  : Référentiel terrestre (repère cartésien attaché au laboratoire), référentiel géocentrique.
>
> (b) - $\Delta x = x(t_2) - x(t_1)$ ; $v_{x,\text{moy}} = \frac{\Delta x}{\Delta t}$ ; $a_{x,\text{moy}} = \frac{\Delta v_x}{\Delta t}$.
> - $\mathrm{d}x = v_x(t)\mathrm{d}t$ ; $v_x(t) = \frac{\mathrm{d}x}{\mathrm{d}t}$ ; $a_x(t) = \frac{\mathrm{d}v_x}{\mathrm{d}t} = \frac{\mathrm{d}^2 x}{\mathrm{d}t^2}$.
>
> (c) - $v_x(t)$ est une grandeur algébrique (peut être négative), tandis que $v(t) = |v_x(t)| \ge 0$. Elles sont égales si le mouvement s'effectue dans le sens des $x$ positifs ($v_x \ge 0$).
> - $x(t)$ : position à droite ($>0$) ou à gauche ($<0$) de l'origine $O$. $\mathrm{d}x$ et $v_x(t)$ : déplacement vers les $x$ croissants ($>0$) ou décroissants ($<0$). $a_x(t)$ : accélération orientée vers les $x$ positifs ($>0$) ou négatifs ($<0$).
> - Vers les $x$ croissants en accélérant : $v_x > 0$ et $a_x > 0$.
> - Vers les $x$ décroissants en ralentissant : $v_x < 0$ et $a_x > 0$ (car $v_x \cdot a_x < 0$).
>
> (d) - $x(t) = x_0 + \int_{0}^{t} v_x(u)\,\mathrm{d}u$
> - $v_x(t) = v_x(0) + \int_{0}^{t} a_x(u)\,\mathrm{d}u$


**2.**

  **a)** **Mouvements particuliers**



(a) Décrire les caractéristiques d'un mouvement rectiligne uniforme (MRU).

(b) Un mouvement uniforme est-il toujours rectiligne ? Justifier par un exemple.

(c) Décrire les caractéristiques d'un mouvement rectiligne uniformément accéléré (MRUA).

> [!example]- 📝 Solution détaillée
> **Résolution sur les mouvements particuliers**
>
> (a) **MRU** : Trajectoire droite, $a_x(t) = 0$, $v_x(t) = \text{Cte}$, $x(t) = v_x t + x_0$.
>
> (b) **Non**. Un mouvement uniforme signifie seulement que la norme de la vitesse est constante ($v = \text{Cte}$). Exemple : le Mouvement Circulaire Uniforme (MCU) où la direction du vecteur vitesse varie en permanence (accélération non nulle).
>
> (c) **MRUA** : Trajectoire droite, $a_x(t) = a_0 = \text{Cte}$, $v_x(t) = a_0 t + v_0$, $x(t) = \frac{1}{2}a_0 t^2 + v_0 t + x_0$.


**3.**

  **a)** En août 2009, Usain Bolt a parcouru 100 m en 9,58 s.



(a) Quelle était sa vitesse moyenne ?

(b) Serait-il en infraction dans une zone limitée à $30\text{ km}\cdot\text{h}^{-1}$ ?

> [!example]- 📝 Solution détaillée
> **Résolution Usain Bolt**
>
> (a) $v_{\text{moy}} = \frac{\Delta x}{\Delta t} = \frac{100}{9,58} \approx 10,44\text{ m}\cdot\text{s}^{-1}$.
>
> (b) En $\text{km}\cdot\text{h}^{-1}$ : $10,44 \times 3,6 = 37,58\text{ km}\cdot\text{h}^{-1}$. $37,58 > 30$, il serait donc en infraction.


**4.**

  **a)** Déterminer l'accélération moyenne dans chacun des trois cas :



(a) Airbus A320 : du repos à $300\text{ km}\cdot\text{h}^{-1}$ en $50\text{ s}$.

(b) Rafale : de $230\text{ km}\cdot\text{h}^{-1}$ à l'arrêt en $4\text{ s}$.

(c) Capsule d'entraînement : atteint $1440\text{ km}\cdot\text{h}^{-1}$ en $2\text{ s}$.

> [!example]- 📝 Solution détaillée
> **Calculs d'accélérations moyennes**
>
> (a) $v = \frac{300}{3,6} = 83,33\text{ m}\cdot\text{s}^{-1} \implies a_{\text{moy}} = \frac{83,33 - 0}{50} = 1,67\text{ m}\cdot\text{s}^{-2}$.
>
> (b) $v = \frac{230}{3,6} = 63,89\text{ m}\cdot\text{s}^{-1} \implies a_{\text{moy}} = \frac{0 - 63,89}{4} = -15,97\text{ m}\cdot\text{s}^{-2}$.
>
> (c) $v = \frac{1440}{3,6} = 400\text{ m}\cdot\text{s}^{-1} \implies a_{\text{moy}} = \frac{400 - 0}{2} = 200\text{ m}\cdot\text{s}^{-2}$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/fonctions-derives-integrale-4h-description-mathematique-du-mouvement-a-1d/ex2-chute-libre-experience-et-modele|Exercice 2 — Chute libre : expérience et modèle]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/fonctions-derives-integrale-4h-description-mathematique-du-mouvement-a-1d/ex3-equations-de-mouvement|Exercice 3 — Équations de mouvement]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/fonctions-derives-integrale-4h-description-mathematique-du-mouvement-a-1d/ex4-mouvement-rectiligne-uniformement-accelere-mrua|Exercice 4 — Mouvement rectiligne uniformément accéléré (MRUA)]]

