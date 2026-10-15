---
title: "Chapitre 1 — Ondes mécaniques : introduction"
tags:
  - cours
---

[[physique/ipsa-ondes/index|⬅ Physique des ondes]]

*Cours*

## 1. Qu'est-ce qu'une onde ?

Une onde est la propagation d'une perturbation dans un milieu, sans
transport de matière : chaque point du milieu oscille autour de sa
position d'équilibre, et c'est cette oscillation qui se propage,
décalée dans le temps, aux points voisins.

> [!info] 💡 Remarque
> Ne pas confondre la vitesse de propagation de l'onde $c$ (vitesse à
> laquelle l'information voyage) avec la vitesse d'un point du milieu
> $v_y = \partial y/\partial t$ (mouvement local, transverse pour une
> onde sur une corde).


## 2. Équation de d'Alembert

Pour une corde tendue de masse linéique $\mu$ et de tension $F$, le
déplacement transversal $y(x,t)$ obéit à :
$$\frac{\partial^2 y}{\partial x^2} = \frac{1}{c^2}\frac{\partial^2 y}{\partial t^2},
\qquad c = \sqrt{F/\mu}.$$

[![Exemple d'onde progressive sinusoïdale sur une corde.](/figures/td1_ex1_corde_t0.svg)](/figures/td1_ex1_corde_t0.svg)

> [!question]- 🔭 Aller plus loin — Master
> Cette équation se généralise en 3D à l'équation de d'Alembert
> $\Delta \psi = \dfrac{1}{c^2}\partial_t^2\psi$, point de départ de
> l'électromagnétisme (équation de propagation du champ dans le vide)
> et de l'acoustique 3D.


## 3. Onde plane progressive sinusoïdale

Solution particulière très utilisée : $y(x,t) = a\cos(kx - \omega t + \phi)$,
avec la relation de dispersion $\omega = kc$ (milieu non dispersif).

[![animation](/animations/anim_corde_onde/animation.gif)](/animations/anim_corde_onde/animation.gif)

[🎞️ Voir en .mp4](/animations/anim_corde_onde/animation.mp4)
