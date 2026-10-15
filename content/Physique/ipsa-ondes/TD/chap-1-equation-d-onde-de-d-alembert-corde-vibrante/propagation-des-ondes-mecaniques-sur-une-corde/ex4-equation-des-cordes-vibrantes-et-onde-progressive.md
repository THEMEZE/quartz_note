---
title: "Exercice 4 — Équation des cordes vibrantes et onde progressive"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · [📄 Énoncé](/pdfs/td1_PhV212_enonce.pdf)

### Exercice 4. Équation des cordes vibrantes et onde progressive

Une corde homogène et inextensible, de masse linéique $\mu$, est tendue
horizontalement (suivant l'axe $Ox$) avec une tension $F$ constante. La corde,
déplacée de sa position d'équilibre en $x=0$, acquiert un mouvement décrit
à l'instant $t$ par le déplacement $y(x,t)$ quasi vertical.

À l'instant $t$, la tension $\vec{T}(x,t)$ exercée par la partie droite sur la
partie gauche fait un angle petit $\alpha(x,t)$ avec l'axe horizontal. On néglige
les forces de pesanteur. Le déplacement transversal $y(x,t)$ obéit à l'équation :
$$\dfrac{\partial^2 y}{\partial x^2} = \dfrac{1}{c^2}\dfrac{\partial^2 y}{\partial t^2}$$

[![Schémat tronçon de corde](/figures/td1_ex3_phv212_demo.svg)](/figures/td1_ex3_phv212_demo.svg)

**q1.** Quelle est la nature de l'onde $y(x,t)$ créée par la perturbation sur la corde ?
Soyez aussi précis que possible. Exprimer la célérité $c$ de l'onde en fonction de $F$ et de $\mu$.

> [!tip]- 💡 Coup de pouce
> **Nature de l'onde et PFD**
>
> Réfléchissez à la direction du déplacement $y$ par rapport à la direction de propagation $x$.
> Pour exprimer $c$, appliquez le PFD projeté transversalement sur un tronçon $[x, x+dx]$.


**q2.** Comment est modifiée l'équation d'onde si on ne néglige plus le poids de la corde ?

> [!tip]- 💡 Coup de pouce
> **Ajout de la pesanteur**
>
> Le poids du tronçon $dm\cdot g = \mu\,g\,dx$ s'ajoute vers le bas dans le bilan des forces transversales.


Une corde vibrante très longue, de masse linéique $\mu = 0.12$ kg/m et de tension $F = 20$ N,
est le siège d'une onde progressive sinusoïdale transversale d'amplitude $a = 2$ mm et de longueur d'onde $\lambda = 0.25$ m.


**3.**

  **a)** Dans ce cas, calculer la vitesse de propagation $c$ de l'onde.

> [!tip]- 💡 Coup de pouce
> **Calcul direct**
>
> Appliquez la formule $c = \sqrt{F/\mu}$ avec les valeurs numériques de la question.


  **b)** Calculer la vitesse transversale maximale d'un élément de corde. Que remarquez-vous ?

> [!tip]- 💡 Coup de pouce
> **Vitesse particulaire vs célérité**
>
> L'onde s'écrit $y(x,t) = a\cos(kx - \omega t + \phi)$. La vitesse transversale est $v_y = \partial_t y$. Son maximum est $v_{\text{max}} = a\omega$ avec $\omega = 2\pi c / \lambda$.


  **c)** Calculer la composante transversale maximale de la tension en un point quelconque de la corde.

> [!tip]- 💡 Coup de pouce
> **Projection de la tension**
>
> La composante transversale de la tension est $T_y = F\sin\alpha \approx F \dfrac{\partial y}{\partial x}$.


  **d)** Quelle est la phase de l'onde lorsque ces deux maxima (vitesse et tension transversale) sont atteints ?
Calculer le déplacement correspondant $y(x,t)$ de l'élément de corde.

> [!tip]- 💡 Coup de pouce
> **Analyse des fonctions sinus / cosinus**
>
> Examinez la phase $\Phi(x,t) = kx - \omega t + \phi$ lorsque $\sin\Phi(x,t) = \pm 1$. Que vaut $\cos\Phi(x,t)$ à cet instant ?


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex8-energie-et-puissance-d-une-onde-sur-une-corde-impedance-caracteristique|Exercice 8 — Énergie et puissance d'une onde sur une corde : impédance caractéristique]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex10-corde-discrete-chaine-de-masses-dispersion-coupure-et-vitesse-de-groupe|Exercice 10 — Corde discrète (chaîne de masses) : dispersion, coupure et vitesse de groupe]]

