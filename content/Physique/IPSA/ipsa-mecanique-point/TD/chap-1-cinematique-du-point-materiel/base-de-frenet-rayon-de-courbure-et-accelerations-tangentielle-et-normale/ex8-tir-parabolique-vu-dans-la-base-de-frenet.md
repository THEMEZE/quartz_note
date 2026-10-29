---
title: "Exercice 8 — Tir parabolique vu dans la base de Frenet"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/index|⬅ Retour]] · <a href="/pdfs/td3_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td3_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td3_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td3_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 8. Tir parabolique vu dans la base de Frenet

Un projectile est lancé du sol, à l'instant $t=0$, depuis l'origine $O$, avec une vitesse de norme $v_0$ faisant l'angle
$\alpha_0$ avec l'horizontale $Ox$ (l'axe $Oy$ est vertical vers le haut). Il n'est soumis qu'à la pesanteur : son
accélération est le vecteur constant $\vec a=-g\,\vec u_y$ (résistance de l'air négligée). On étudie ce mouvement
dans la base de Frenet.

**q1.** **1/ Composantes de l'accélération.**


(a) Écrire $\vec v(t)$ et $v(t)$. Exprimer l'angle $\varphi(t)$ de $\vec v$ avec l'horizontale.

(b) Calculer $a_T(t)$ et $a_N(t)$. En quels instants $a_T=0$ ? Comment varie $a_T$ ? Que vaut $a_N$ au sommet ? Vérifier $a_T^2+a_N^2=g^2$.

(c) Interpréter physiquement le signe de $a_T$ en montée et en descente.

> [!tip]- 💡 Coup de pouce
> $\vec a=(0;-g)$, $\vec v=(v_x;v_y)$ avec $v_x=v_0\cos\alpha_0$, $v_y=v_0\sin\alpha_0-gt$. Utilisez $a_T=\vec a\cdot\vec v/v$ et $a_N=|a_xv_y-a_yv_x|/v$.


> [!success]- ✅ Correction
> $a_T=-\dfrac{g\,v_y}v=-g\sin\varphi$, $a_N=\dfrac{g\,v_x}v=g\cos\varphi$ ; $a_T=0$ au sommet ($v_y=0$) où $a_N=g$.


> [!example]- 📝 Solution détaillée
> **(a) Vitesse et angle**
>
> $\vec v=(v_x\ ;\ v_y)$, $v_x=v_0\cos\alpha_0$ constant, $v_y=v_0\sin\alpha_0-gt$ :
> $$v=\sqrt{v_0^2\cos^2\alpha_0+(v_0\sin\alpha_0-gt)^2},\qquad\tan\varphi=\frac{v_0\sin\alpha_0-gt}{v_0\cos\alpha_0}.$$
> L'angle $\varphi$ décroît de $\alpha_0$ (départ) à $0$ (sommet, $t_s=\dfrac{v_0\sin\alpha_0}g$) puis à $-\alpha_0$ (arrivée au sol).
>
> **(b) $a_T$ et $a_N$**
>
> $\vec a\cdot\vec v=-g\,v_y$ donc
> $$\boxed{a_T=-\frac{g\,v_y}v=-g\sin\varphi},\qquad\boxed{a_N=\frac{|a_xv_y-a_yv_x|}v=\frac{g\,v_x}v=g\cos\varphi}.$$
> Vérification : $a_T^2+a_N^2=g^2(\sin^2\varphi+\cos^2\varphi)=g^2$ $\surd$. $a_T=0$ lorsque $v_y=0$, c'est-à-dire au sommet ($t=t_s$), où $\varphi=0$ et $a_N=g$ : toute l'accélération est normale, dirigée vers le bas, centre de courbure sous le sommet. Au départ ($\varphi=\alpha_0$) : $a_T=-g\sin\alpha_0$, $a_N=g\cos\alpha_0$.
>
> **(c) Interprétation**
>
> En **montée** ($v_y>0$, $\varphi>0$) : $a_T<0$, la norme de la vitesse **diminue** (la pesanteur « freine » la montée). Au **sommet** : $a_T=0$, la norme de la vitesse est **minimale** ($v=v_x$). En **descente** ($\varphi<0$) : $a_T>0$, la norme **augmente**. À l'arrivée à la même hauteur qu'au départ, $v=v_0$ (symétrie). $a_N=g\cos\varphi$ est maximal ($=g$) au sommet : la trajectoire y est la plus courbée.


**q2.** **2/ Rayon de courbure.**


(a) Établir $R(t)=\dfrac{v^3}{g\,v_x}$ puis $R=\dfrac{v_x^2}{g\cos^3\varphi}$. En déduire le rayon de courbure minimal $R_{\min}$ et son lieu.

(b) Application. $v_0=20\ \mathrm{m/s}$, $\alpha_0=60^\circ$, $g=9{,}81\ \mathrm{m\,s^{-2}}$ : calculer $t_s$, $R_{\min}$, $R(0)$, les instants où $a_T=-a_N$ (angle de $45^\circ$) et la durée totale du vol.

(c) Représenter la trajectoire, $\vec v$, $\vec\tau$, $\vec n$, $a_T\vec\tau$ et $a_N\vec n$ à $t=0{,}75\ \mathrm s$, $t_s$ et $2{,}78\ \mathrm s$, ainsi que le cercle osculateur au sommet.

> [!tip]- 💡 Coup de pouce
> $R=\dfrac{v^2}{a_N}$ avec $a_N=\dfrac{g\,v_x}v$. Puis $v=\dfrac{v_x}{\cos\varphi}$. Pour (e), $a_T=-a_N\iff\tan\varphi=\pm1$ (en valeur absolue $|a_T|=a_N$).


> [!success]- ✅ Correction
> $R=\dfrac{v^3}{gv_x}=\dfrac{v_x^2}{g\cos^3\varphi}$ ; $R_{\min}=\dfrac{v_x^2}g$ au sommet. AN : $t_s=1{,}77$ s, $R_{\min}=10{,}2$ m, $R(0)=81{,}5$ m, $|a_T|=a_N$ à $t=0{,}75$ s et $2{,}78$ s ; durée totale $3{,}53$ s.


> [!example]- 📝 Solution détaillée
> **(d) Rayon de courbure**
>
> $$R=\frac{v^2}{a_N}=\frac{v^2}{g\,v_x/v}=\boxed{\frac{v^3}{g\,v_x}}.$$
> Avec $v=v_x/\cos\varphi$ : $\boxed{R=\dfrac{v_x^2}{g\cos^3\varphi}}$. Comme $\cos\varphi\le1$, $R$ est **minimal** quand $\cos\varphi=1$, c'est-à-dire au **sommet** :
> $$\boxed{R_{\min}=\frac{v_x^2}g=\frac{v_0^2\cos^2\alpha_0}g}.$$
> Au départ : $R(0)=\dfrac{R_{\min}}{\cos^3\alpha_0}=\dfrac{v_0^2}{g\cos\alpha_0}$. Limite $\varphi\to\pm90^\circ$ : $R\to\infty$ (trajectoire quasi rectiligne).
>
> **(e) Application numérique**
>
> $v_x=20\cos60^\circ=10\ \mathrm{m/s}$ ; $v_{y0}=20\sin60^\circ=17{,}3\ \mathrm{m/s}$. $t_s=\dfrac{17{,}3}{9{,}81}\approx\boxed{1{,}77\ \mathrm s}$ ; durée totale $2t_s\approx3{,}53\ \mathrm s$. $R_{\min}=\dfrac{100}{9{,}81}\approx\boxed{10{,}2\ \mathrm m}$ ; $R(0)=\dfrac{R_{\min}}{\cos^3(60^\circ)}=\dfrac{10{,}2}{0{,}125}\approx81{,}5\ \mathrm m$. $|a_T|=a_N\iff|v_y|=v_x=10\ \mathrm{m/s}$ : $17{,}3-9{,}81\,t=\pm10$ donne $t=0{,}746\ \mathrm s$ et $t=2{,}785\ \mathrm s$ (angle $\pm45^\circ$, symétriques par rapport au sommet $\surd$). À ces instants $a_T=\mp6{,}94$ et $a_N=6{,}94\ \mathrm{m\,s^{-2}}$ (soit $g/\sqrt2$).
>
> **(f) Représentation**
>
> Parabole d'axe vertical, de sommet à la hauteur $y_s=\dfrac{v_{y0}^2}{2g}\approx15{,}3\ \mathrm m$ et d'abscisse $x_s=v_xt_s\approx17{,}7\ \mathrm m$, de portée $35{,}3\ \mathrm m$. Au sommet : $\vec v$ horizontal, $\vec g$ vertical vers le bas, $\vec n=-\vec u_y$ ; cercle osculateur de centre $(17{,}7;\ 15{,}3-10{,}2)=(17{,}7;\ 5{,}1)$ et de rayon $10{,}2\ \mathrm m$. Aux deux autres points, $\vec g$ se décompose en $a_T\,\vec\tau$ (le long de la trajectoire : vers l'arrière en montée, vers l'avant en descente) et $a_N\,\vec n$ (vers le bas, côté concave) de même norme $6{,}94\ \mathrm{m\,s^{-2}}$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex1-base-de-frenet-demonstrations-de-cours-et-applications|Exercice 1 — Base de Frenet : démonstrations de cours et applications]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex2-mouvement-curviligne-uniforme-cercle-parabole-applications|Exercice 2 — Mouvement curviligne uniforme : cercle, parabole, applications]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex3-circuit-de-monaco-courbure-et-acceleration-a-vitesse-constante|Exercice 3 — Circuit de Monaco : courbure et accélération à vitesse constante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex4-abscisse-curviligne-et-rayon-de-courbure-d-une-trajectoire-parabolique|Exercice 4 — Abscisse curviligne et rayon de courbure d'une trajectoire parabolique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex5-cycloide-point-d-une-roue-qui-roule-sans-glisser|Exercice 5 — Cycloïde : point d'une roue qui roule sans glisser]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex6-raccordement-routier-en-clothoide-courbure-variable-et-jerk|Exercice 6 — Raccordement routier en clothoïde (courbure variable et « jerk »)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex7-cercle-d-adherence-freiner-et-tourner-en-meme-temps|Exercice 7 — Cercle d'adhérence : freiner et tourner en même temps]]

