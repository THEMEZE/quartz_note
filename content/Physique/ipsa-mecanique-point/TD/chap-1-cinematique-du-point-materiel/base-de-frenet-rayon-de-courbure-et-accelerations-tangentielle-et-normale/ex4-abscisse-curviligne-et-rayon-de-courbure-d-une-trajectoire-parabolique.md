---
title: "Exercice 4 — Abscisse curviligne et rayon de courbure d'une trajectoire parabolique"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/index|⬅ Retour]] · <a href="/pdfs/td3_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td3_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 4. Abscisse curviligne et rayon de courbure d'une trajectoire parabolique

Dans le plan $Oxy$, les coordonnées d'une particule sont données en fonction du temps par
$$\begin{cases}x(t)=b\,t\\ y(t)=c\,t\,(t-1)\end{cases}$$
avec $b=2$ (S.I.) et $c=4$ (S.I.).

**q1.** (a) Déterminer l'équation de la trajectoire et la représenter sur un graphique.

(b) Calculer la vitesse $\vec v$ à l'instant $t$. Tracer $\vec v$ à $t=0$ et $t=0{,}5\ \mathrm s$ sur le graphique.

> [!tip]- 💡 Coup de pouce
> Éliminez $t$ entre $x(t)$ et $y(t)$ : $t=x/b$. Pour la vitesse, dérivez chaque composante. Pour le graphique : zéros de $y$, sommet.


**q2.** (a) Montrer que le mouvement a une accélération constante, dont on calculera les composantes tangentielle et normale.

(b) En déduire le rayon de courbure à $t=0{,}5\ \mathrm s$.

> [!tip]- 💡 Coup de pouce
> $a_T=\vec a\cdot\vec v/v$ et $a_N=\sqrt{a^2-a_T^2}$ (ou $|\vec a\wedge\vec v|/v$). Pour (d), $R=v^2/a_N$ ; comparez avec $\dfrac{(1+y'^2)^{3/2}}{|y''|}$.


**q3.** (a) Calculer l'abscisse curviligne $s(t)$ parcourue depuis $t=0$, puis la longueur de l'arc $OP$ de $t=0$ à $t=1\ \mathrm s$. La comparer à la distance en ligne droite $OP$.

(b) Vérifier que, de $t=0$ à $t=0{,}5\ \mathrm s$, $s$ est bien l'aire sous la courbe $v(t)$ (intégrale).

> [!tip]- 💡 Coup de pouce
> $s(t)=\int_0^tv\,\mathrm dt'$ avec $v=2\sqrt{1+u^2}$, $u=4t'-2$, $\mathrm dt'=\mathrm du/4$ : primitive de $\sqrt{1+u^2}$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex1-base-de-frenet-demonstrations-de-cours-et-applications|Exercice 1 — Base de Frenet : démonstrations de cours et applications]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex5-cycloide-point-d-une-roue-qui-roule-sans-glisser|Exercice 5 — Cycloïde : point d'une roue qui roule sans glisser]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex6-raccordement-routier-en-clothoide-courbure-variable-et-jerk|Exercice 6 — Raccordement routier en clothoïde (courbure variable et « jerk »)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex2-mouvement-curviligne-uniforme-cercle-parabole-applications|Exercice 2 — Mouvement curviligne uniforme : cercle, parabole, applications]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex3-circuit-de-monaco-courbure-et-acceleration-a-vitesse-constante|Exercice 3 — Circuit de Monaco : courbure et accélération à vitesse constante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex7-cercle-d-adherence-freiner-et-tourner-en-meme-temps|Exercice 7 — Cercle d'adhérence : freiner et tourner en même temps]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex8-tir-parabolique-vu-dans-la-base-de-frenet|Exercice 8 — Tir parabolique vu dans la base de Frenet]]

