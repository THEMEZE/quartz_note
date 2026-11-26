---
title: "Exercice 4 — Abscisse curviligne et rayon de courbure d'une trajectoire parabolique"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/index|⬅ Retour]] · <a href="/pdfs/td3_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td3_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td3_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 4. Abscisse curviligne et rayon de courbure d'une trajectoire parabolique

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 35 min · Type : Entraînement / Application complète*

Dans le plan $Oxy$, les coordonnées d'une particule sont données en fonction du temps par
$$\begin{cases}x(t)=b\,t\\ y(t)=c\,t\,(t-1)\end{cases}$$
avec $b=2$ (S.I.) et $c=4$ (S.I.).


> [!question]- 🪝 Accroche
> **Une accélération constante, des composantes variables**
>
> *Durée de l'introduction : 3 à 5 min, avant de lire l'énoncé*
>
> *Un projectile lancé dans le vide subit une accélération constante $\vec g$. Pourtant, au sommet de sa trajectoire, on dit qu'il n'a « plus d'accélération tangentielle ». Comment l'accélération peut-elle être constante en vecteur et pourtant « changer » ?*
>
> **Idée clé : $\vec a$ est un vecteur fixe, mais $(\vec\tau,\vec n)$ tourne.** Les composantes $a_T=\vec a\cdot\vec\tau$ et $a_N=\vec a\cdot\vec n$ dépendent de l'angle entre $\vec a$ et la tangente. Au sommet, $\vec a\perp\vec v$ : $a_T=0$ et $a_N=a$.




> [!abstract]- 🧠 À savoir avant
> **Cinématique cartésienne**
>
> $\vec v=(\dot x,\dot y)$, $\vec a=(\ddot x,\ddot y)$, élimination du temps pour trouver la trajectoire.
>
> **Composantes tangentielle et normale**
>
> $a_T=\dfrac{\vec a\cdot\vec v}v$, $a_N=\dfrac{|a_xv_y-a_yv_x|}v=\sqrt{a^2-a_T^2}$, $R=\dfrac{v^2}{a_N}$.
>
> **Abscisse curviligne**
>
> $s(t)=\displaystyle\int_0^t\|\vec v\|\,\mathrm dt'$, avec $\displaystyle\int\sqrt{1+u^2}\,\mathrm du=\tfrac12\left(u\sqrt{1+u^2}+\operatorname{arsinh}u\right)$.




> [!info]- 🎯 Ce que tu sauras faire
> **Mener un calcul complet de $a_T$, $a_N$, $R$ et $s$ à partir d'une loi horaire**
>
> Éliminer le temps, calculer $\vec v$, $\vec a$, leurs composantes tangentielle et normale, le rayon de courbure en un instant donné, vérifier avec la formule en $y(x)$ et calculer la longueur parcourue.




> [!tip]- 📖 Rappel de cours
> **Mouvement à accélération constante**
>
> Si $\vec a$ est un vecteur constant, la trajectoire est une parabole (ou une droite si $\vec v(0)\parallel\vec a$). $\vec a$ est constant, mais $a_T=\vec a\cdot\vec\tau$ et $a_N=\vec a\cdot\vec n$ varient avec la direction de $\vec\tau$.




> [!note]- 🧮 Outils mathématiques
> **Élimination du temps**
>
> $t=x/b$ puis $y=c\,\dfrac xb\left(\dfrac xb-1\right)=\dfrac c{b^2}x^2-\dfrac cbx$.
>
> **Produits scalaire et vectoriel plans**
>
> $\vec a\cdot\vec v=a_xv_x+a_yv_y$, $|\vec a\wedge\vec v|=|a_xv_y-a_yv_x|$.
>
> **Primitive de $\sqrt{1+u^2}$**
>
> $F(u)=\tfrac12\left(u\sqrt{1+u^2}+\ln(u+\sqrt{1+u^2})\right)$, impaire : $\int_{-2}^0\sqrt{1+u^2}\,\mathrm du=F(2)\approx2{,}958$.



**q1.** (a) Déterminer l'équation de la trajectoire et la représenter sur un graphique.

(b) Calculer la vitesse $\vec v$ à l'instant $t$. Tracer $\vec v$ à $t=0$ et $t=0{,}5\ \mathrm s$ sur le graphique.


> [!tip]- 💡 Coup de pouce
> Éliminez $t$ entre $x(t)$ et $y(t)$ : $t=x/b$. Pour la vitesse, dérivez chaque composante. Pour le graphique : zéros de $y$, sommet.




> [!success]- ✅ Correction
> (a) $y=x^2-2x$ : parabole de sommet $(1;-1)$, passant par $(0;0)$ et $(2;0)$. (b) $\vec v=(2;\ 8t-4)$ ; $\vec v(0)=(2;-4)$, $\vec v(0{,}5)=(2;0)$.




> [!example]- 📝 Solution détaillée
> **(a) Trajectoire**
>
> $t=\dfrac xb=\dfrac x2$, d'où $y=4\cdot\dfrac x2\left(\dfrac x2-1\right)=x^2-2x$ :
> $$\boxed{y=x^2-2x=(x-1)^2-1}.$$
> Parabole ouverte vers le haut, de sommet $S(1;-1)$, coupant $Ox$ en $x=0$ ($t=0$) et $x=2$ ($t=1$ s). Le point $S$ est atteint à $t=0{,}5$ s. La particule part de $O$, descend jusqu'à $S$ puis remonte vers $(2;0)$.
>
> **(b) Vitesse**
>
> $\dot x=b=2$ et $\dot y=c\,(2t-1)=4(2t-1)=8t-4$ :
> $$\boxed{\vec v=(2\ ;\ 8t-4)\ \mathrm{m/s}},\qquad v=\sqrt{4+(8t-4)^2}.$$
> $t=0$ : $\vec v=(2;-4)$, $v=\sqrt{20}\approx4{,}47\ \mathrm{m/s}$, dirigée vers le bas à droite. $t=0{,}5$ s : $\vec v=(2;0)$, $v=2\ \mathrm{m/s}$, horizontale, vers la droite (sommet de la parabole). Sur le graphique, $\vec v$ est tangent à la trajectoire en chaque point.



**q2.** (a) Montrer que le mouvement a une accélération constante, dont on calculera les composantes tangentielle et normale.

(b) En déduire le rayon de courbure à $t=0{,}5\ \mathrm s$.


> [!tip]- 💡 Coup de pouce
> $a_T=\vec a\cdot\vec v/v$ et $a_N=\sqrt{a^2-a_T^2}$ (ou $|\vec a\wedge\vec v|/v$). Pour (d), $R=v^2/a_N$ ; comparez avec $\dfrac{(1+y'^2)^{3/2}}{|y''|}$.




> [!success]- ✅ Correction
> $\vec a=(0;8)$ constant ; $a_T=\dfrac{8(8t-4)}{v}$, $a_N=\dfrac{16}v$ avec $v=\sqrt{4+(8t-4)^2}$. En $t=0{,}5$ : $a_T=0$, $a_N=8$ ; $R=\dfrac{v^2}{a_N}=\dfrac4{8}=0{,}5\ \mathrm m$.




> [!example]- 📝 Solution détaillée
> **(c) Accélération**
>
> $\ddot x=0$ et $\ddot y=2c=8$ :
> $$\boxed{\vec a=(0\ ;\ 8)\ \mathrm{m\,s^{-2}}}$$
> constante et verticale (dirigée selon $+Oy$).
>
> **(c) Composantes tangentielle et normale**
>
> $\vec a\cdot\vec v=8(8t-4)$ donc $a_T=\dfrac{8(8t-4)}{\sqrt{4+(8t-4)^2}}$. Avec $u=4t-2$, $8t-4=2u$ et $v=2\sqrt{1+u^2}$ :
> $$\boxed{a_T=\frac{8u}{\sqrt{1+u^2}}},\qquad\boxed{a_N=\frac{|a_xv_y-a_yv_x|}v=\frac{16}{2\sqrt{1+u^2}}=\frac8{\sqrt{1+u^2}}}.$$
> Vérification : $a_T^2+a_N^2=\dfrac{64u^2+64}{1+u^2}=64=a^2$ $\surd$. Valeurs : $t=0$ ($u=-2$) : $a_T=-\dfrac{16}{\sqrt5}\approx-7{,}16$ et $a_N=\dfrac8{\sqrt5}\approx3{,}58\ \mathrm{m\,s^{-2}}$ (la particule **ralentit** en descendant vers le sommet) ; $t=0{,}5$ s ($u=0$) : $a_T=0$, $a_N=8\ \mathrm{m\,s^{-2}}$ ; $t=1$ s ($u=2$) : $a_T\approx+7{,}16$ (elle accélère en remontant). Comportement : $a_T$ passe de négatif à positif en s'annulant au sommet, $a_N$ est maximal au sommet.
>
> **(d) Rayon de courbure à $t=0{,}5$ s**
>
> $R=\dfrac{v^2}{a_N}=\dfrac{2^2}8=\boxed{0{,}5\ \mathrm m}$. Contrôle avec la formule des courbes $y(x)$ : au sommet $x=1$, $y'=2x-2=0$ et $y''=2$ donc $R=\dfrac{(1+0)^{3/2}}2=0{,}5\ \mathrm m$ $\surd$. Le centre de courbure est $C=S+R\,\vec n=(1;-1)+0{,}5\,\vec u_y=(1;-0{,}5)$. Au contraire, en $t=0$ : $R=\dfrac{v^2}{a_N}=\dfrac{20}{3{,}58}\approx5{,}59\ \mathrm m$ (confirmé par $\dfrac{(1+y'^2)^{3/2}}{|y''|}$ avec $y'(0)=-2$ : $\dfrac{5^{3/2}}2=5{,}59$ $\surd$).



**q3.** (a) Calculer l'abscisse curviligne $s(t)$ parcourue depuis $t=0$, puis la longueur de l'arc $OP$ de $t=0$ à $t=1\ \mathrm s$. La comparer à la distance en ligne droite $OP$.

(b) Vérifier que, de $t=0$ à $t=0{,}5\ \mathrm s$, $s$ est bien l'aire sous la courbe $v(t)$ (intégrale).


> [!tip]- 💡 Coup de pouce
> $s(t)=\int_0^tv\,\mathrm dt'$ avec $v=2\sqrt{1+u^2}$, $u=4t'-2$, $\mathrm dt'=\mathrm du/4$ : primitive de $\sqrt{1+u^2}$.




> [!success]- ✅ Correction
> $s(0{,}5)\approx1{,}48\ \mathrm m$ ; arc $OP$ : $\approx2{,}96\ \mathrm m$, à comparer à $OP=2\ \mathrm m$ ; l'arc est $48\ \%$ plus long que la corde.




> [!example]- 📝 Solution détaillée
> **(e) Abscisse curviligne**
>
> $s(t)=\displaystyle\int_0^t2\sqrt{1+(4t'-2)^2}\,\mathrm dt'=\dfrac12\int_{-2}^{4t-2}\sqrt{1+u^2}\,\mathrm du=\dfrac12\left[F(u)\right]_{-2}^{4t-2}$ avec $F(u)=\dfrac12\left(u\sqrt{1+u^2}+\operatorname{arsinh}u\right)$ impaire. $F(2)=\dfrac12\left(2\sqrt5+\operatorname{arsinh}2\right)\approx\dfrac12(4{,}472+1{,}444)=2{,}958$.
>
> De $t=0$ à $0{,}5$ s : $s=\dfrac12\left(F(0)-F(-2)\right)=\dfrac12F(2)\approx\boxed{1{,}48\ \mathrm m}$. De $0$ à $1$ s : $s=\dfrac12\left(F(2)-F(-2)\right)=F(2)\approx\boxed{2{,}96\ \mathrm m}$. La distance en ligne droite $OP=2\ \mathrm m$ : la trajectoire est $48\ \%$ plus longue que la corde, car la particule descend de $1\ \mathrm m$ puis remonte de $1\ \mathrm m$ pour avancer de $2\ \mathrm m$ ; borne basse : $s\ge OP$ $\surd$ ; borne haute : $s\le2+2=4\ \mathrm m$ $\surd$.
>
> **(f) Lecture graphique**
>
> $s(t)$ est l'aire sous la courbe $v(t)$ : $v(0)=4{,}47$, $v(0{,}5)=2$, $v(1)=4{,}47\ \mathrm{m/s}$ ; la formule des trapèzes sur $[0;0{,}5]$ donne $\dfrac{4{,}47+2}2\times0{,}5\approx1{,}62$, proche de $1{,}48$ ; la courbe $v(t)$ est convexe, la formule des trapèzes surestime légèrement l'aire $\surd$.




> [!note]- 🔗 Liens avec d'autres disciplines
> **Mécanique du vol et balistique**
>
> Le mouvement d'un projectile dans le vide est à accélération constante $\vec g$ ; $a_T$ et $a_N$ y sont les composantes de $\vec g$ sur la trajectoire (exercice 8).
>
> **Mathématiques**
>
> Longueur d'un arc de parabole : intégrale de $\sqrt{1+u^2}$, qui fait apparaître l'argument sinus hyperbolique.




> [!question]- 🔭 Aller plus loin — CPGE : Centre de courbure et vérification numérique
> Calculer le centre de courbure à $t=0{,}5$ s : $C=(1;-1)+0{,}5\,\vec u_y=(1;-0{,}5)$. Vérifier avec Python (\texttt{np.gradient}) que $R(t)$ calculé numériquement coïncide avec $R=\dfrac{(4+(8t-4)^2)^{3/2}}{16}$.




> [!question]- 🔭 Aller plus loin — Licence : Mouvement uniforme sur la même parabole
> Comparer ce mouvement (accélération constante, vitesse variable) à un mouvement sur la même parabole à vitesse constante $v_0=2\ \mathrm{m/s}$ (exercice 2) : l'accélération au sommet est la même ($8\ \mathrm{m\,s^{-2}}$) ; l'accélération en $x=0$ est différente. Écrire la loi horaire $s(t)=v_0t$ puis $x(t)$.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex1-base-de-frenet-demonstrations-de-cours-et-applications|Exercice 1 — Base de Frenet : démonstrations de cours et applications]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex5-cycloide-point-d-une-roue-qui-roule-sans-glisser|Exercice 5 — Cycloïde : point d'une roue qui roule sans glisser]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex6-raccordement-routier-en-clothoide-courbure-variable-et-jerk|Exercice 6 — Raccordement routier en clothoïde (courbure variable et « jerk »)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex2-mouvement-curviligne-uniforme-cercle-parabole-applications|Exercice 2 — Mouvement curviligne uniforme : cercle, parabole, applications]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex3-circuit-de-monaco-courbure-et-acceleration-a-vitesse-constante|Exercice 3 — Circuit de Monaco : courbure et accélération à vitesse constante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex7-cercle-d-adherence-freiner-et-tourner-en-meme-temps|Exercice 7 — Cercle d'adhérence : freiner et tourner en même temps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex8-tir-parabolique-vu-dans-la-base-de-frenet|Exercice 8 — Tir parabolique vu dans la base de Frenet]]


