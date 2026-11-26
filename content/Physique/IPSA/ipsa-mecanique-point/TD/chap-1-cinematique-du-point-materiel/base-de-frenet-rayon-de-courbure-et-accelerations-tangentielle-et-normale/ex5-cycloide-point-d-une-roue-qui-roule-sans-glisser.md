---
title: "Exercice 5 — Cycloïde : point d'une roue qui roule sans glisser"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/index|⬅ Retour]] · <a href="/pdfs/td3_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td3_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td3_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 5. Cycloïde : point d'une roue qui roule sans glisser *(facultatif)*

*Difficulté ●●●●○ · ⏱ 45 min · Type : Entraînement / Problème de synthèse*

Une roue de rayon $R_0$ roule **sans glisser** sur l'axe horizontal $Ox$. Son centre $C$ se déplace à
la vitesse constante $\vec V=R_0\omega\,\vec u_x$ ; la roue tourne (dans le sens horaire) à la vitesse angulaire
constante $\omega>0$. On étudie le mouvement d'un point $M$ de la jante (par exemple une valve ou un caillou
coincé dans la bande de roulement). À $t=0$, $M$ est en contact avec le sol, en $O$. On note $\varphi=\omega t$ l'angle
dont la roue a tourné. La trajectoire de $M$ est appelée **cycloïde**.


> [!question]- 🪝 Accroche
> **Un point de la roue est immobile**
>
> *Durée de l'introduction : 3 à 5 min, avant de lire l'énoncé*
>
> *Un cycliste roule à $36$ km/h. Quelle est la vitesse, par rapport au sol, du point de la roue qui touche le sol ? Et du point tout en haut ? Quelle est la forme de la trajectoire d'une valve de chambre à air ? Y a-t-il un moment où elle revient en arrière ?*
>
> **Idée clé : composer translation et rotation.** Dans le référentiel du sol, la position de $M$ est $\overrightarrow{OC}+\overrightarrow{CM}$ : le centre avance, la jante tourne autour du centre. Résultat : la cycloïde. À chaque instant, la roue tourne autour du point de contact $I$ qui est immobile : la vitesse de $M$ est perpendiculaire à $IM$.




> [!abstract]- 🧠 À savoir avant
> **Roulement sans glissement**
>
> Le point de la roue en contact avec le sol a une vitesse nulle (dans le référentiel du sol) : le centre avance de $R_0\varphi$ quand la roue tourne de $\varphi$ ($x_C=R_0\omega t$).
>
> **Base de Frenet**
>
> $\vec a=a_T\,\vec\tau+a_N\,\vec n$, $a_T=\dfrac{\vec a\cdot\vec v}v$, $a_N=\sqrt{a^2-a_T^2}$, $R=\dfrac{v^2}{a_N}$.
>
> **Formules d'angle moitié**
>
> $1-\cos\varphi=2\sin^2\dfrac\varphi2$, $1+\cos\varphi=2\cos^2\dfrac\varphi2$, $\sin\varphi=2\sin\dfrac\varphi2\cos\dfrac\varphi2$.




> [!info]- 🎯 Ce que tu sauras faire
> **Étudier une courbe non triviale avec toute la machinerie de Frenet**
>
> Établir les équations paramétriques de la cycloïde, calculer $\vec v$, $\vec a$, $a_T$, $a_N$, $R$ et la longueur d'une arche, interpréter le point de rebroussement, et relier le résultat à la géométrie du roulement (centre instantané de rotation).




> [!tip]- 📖 Rappel de cours
> **Cycloïde**
>
> $$x=R_0(\varphi-\sin\varphi),\qquad y=R_0(1-\cos\varphi),\qquad\varphi=\omega t.$$
> La vitesse du point de contact est nulle ; le point du haut de la roue va à $2R_0\omega$. La roue tourne à chaque instant autour du point de contact $I$ (centre instantané de rotation) : $\|\vec v\|=\omega\,IM$ et $\vec v\perp\overrightarrow{IM}$.




> [!note]- 🧮 Outils mathématiques
> **Composition de mouvements**
>
> $\overrightarrow{OM}=\overrightarrow{OC}+\overrightarrow{CM}$ avec $\overrightarrow{OC}=(R_0\omega t,R_0)$ et $\overrightarrow{CM}=R_0(-\sin\varphi,-\cos\varphi)$ pour une roue qui tourne dans le sens horaire avec $M$ au bas à $t=0$.
>
> **Angle moitié**
>
> $\sqrt{2(1-\cos\varphi)}=2\sin\dfrac\varphi2$ (pour $\varphi\in[0,2\pi]$) ; $\sin\varphi=2\sin\dfrac\varphi2\cos\dfrac\varphi2$.
>
> **Intégrale de $\sin(\varphi/2)$**
>
> $\displaystyle\int_0^{2\pi}\sin\dfrac\varphi2\,\mathrm d\varphi=\left[-2\cos\dfrac\varphi2\right]_0^{2\pi}=4$.
>
> **Centre instantané de rotation**
>
> Pour un solide plan en mouvement, il existe en général un point $I$ de vitesse nulle (à l'instant considéré) : la vitesse de tout autre point est $\vec v=\vec\Omega\wedge\overrightarrow{IM}$, de norme $\Omega\,IM$, perpendiculaire à $IM$.



**q1.** **1/ Équations de la trajectoire.**


(a) Justifier que $x_C(t)=R_0\omega t$ pour le centre de la roue. Établir les équations horaires $x(t)$ et $y(t)$ de $M$.

(b) Tracer l'arche de cycloïde ($0\le\varphi\le2\pi$) en plaçant les points $\varphi=0,\ \frac\pi2,\ \pi,\ \frac{3\pi}2,\ 2\pi$.


> [!tip]- 💡 Coup de pouce
> $\overrightarrow{OM}=\overrightarrow{OC}+\overrightarrow{CM}$ avec $\overrightarrow{CM}=R_0(-\sin\varphi,-\cos\varphi)$ : à $t=0$ le point est en bas de la roue ($\overrightarrow{CM}=-R_0\vec u_y$) et la roue tourne dans le sens horaire.




> [!success]- ✅ Correction
> $x=R_0(\omega t-\sin\omega t)$, $y=R_0(1-\cos\omega t)$. Points : $(0,0)$, $(0{,}57R_0,R_0)$, $(\pi R_0,2R_0)$, $(5{,}71R_0,R_0)$, $(2\pi R_0,0)$.




> [!example]- 📝 Solution détaillée
> **(a) Équations paramétriques**
>
> Roulement sans glissement : la roue ne glisse pas, donc l'arc de jante qui a touché le sol, de longueur $R_0\varphi$, est égal à la distance parcourue par le centre : $x_C=R_0\varphi=R_0\omega t$ (la vitesse du centre est $V=R_0\omega$). L'altitude du centre est $R_0$. Avec $\overrightarrow{CM}=R_0(-\sin\varphi,\,-\cos\varphi)$ (angle $\varphi$ depuis la verticale descendante, sens horaire) :
> $$\boxed{x(t)=R_0\left(\omega t-\sin\omega t\right)},\qquad\boxed{y(t)=R_0\left(1-\cos\omega t\right)}.$$
> Vérification : $\varphi=0$ donne $(0,0)$ (contact) ; $\varphi=\pi$ donne $(\pi R_0,2R_0)$ (sommet).
>
> **(b) Points de l'arche**
>
> $$\begin{array}{c|ccccc}\varphi&0&\pi/2&\pi&3\pi/2&2\pi\\\hline x/R_0&0&\pi/2-1\approx0{,}57&\pi\approx3{,}14&3\pi/2+1\approx5{,}71&2\pi\approx6{,}28\\y/R_0&0&1&2&1&0\end{array}$$
> L'arche est **symétrique** par rapport à la verticale $x=\pi R_0$, de hauteur $2R_0$ et de largeur $2\pi R_0$ (le périmètre de la roue). Aux extrémités ($\varphi=0,2\pi$), la tangente est **verticale** : points de rebroussement.



**q2.** **2/ Cinématique.**


(a) Calculer $\vec v$ et sa norme. Montrer que $v=2R_0\omega\left|\sin\frac\varphi2\right|$ et que le vecteur tangent est $\vec\tau=\left(\sin\frac\varphi2\ ;\ \cos\frac\varphi2\right)$. Montrer que la droite d'action de $\vec v$ passe par le point le plus haut de la roue.

(b) Calculer $\vec a$ et sa norme. Que remarque-t-on ? Où est dirigée l'accélération ?

(c) Calculer $a_T$, $a_N$ et le rayon de courbure $R$. Vérifier que la normale passe par le point de contact $I$ et que $R=2\,IM$.

(d) Valeurs particulières : sommet ($\varphi=\pi$) et contact ($\varphi\to0$). Commenter.


> [!tip]- 💡 Coup de pouce
> Dérivez $x(t)$ et $y(t)$. Utilisez les angles moitié : $1-\cos\varphi=2\sin^2\frac\varphi2$. Pour (e), $a_T=\vec a\cdot\vec v/v$ puis $a_N=\sqrt{a^2-a_T^2}$ et $R=v^2/a_N$.




> [!success]- ✅ Correction
> $\vec v=R_0\omega(1-\cos\varphi\ ;\ \sin\varphi)$, $v=2R_0\omega\sin\frac\varphi2$ ; $\vec a=R_0\omega^2(\sin\varphi\ ;\ \cos\varphi)$, $a=R_0\omega^2$ constante, dirigée vers $C$ ; $a_T=R_0\omega^2\cos\frac\varphi2$, $a_N=R_0\omega^2\sin\frac\varphi2$ ; $R=4R_0\sin\frac\varphi2$.




> [!example]- 📝 Solution détaillée
> **(c) Vitesse**
>
> $\dot x=R_0\omega(1-\cos\varphi)$, $\dot y=R_0\omega\sin\varphi$ :
> $$\boxed{\vec v=R_0\omega\,(1-\cos\varphi\ ;\ \sin\varphi)}.$$
> Avec $1-\cos\varphi=2\sin^2\frac\varphi2$ et $\sin\varphi=2\sin\frac\varphi2\cos\frac\varphi2$ : $\vec v=2R_0\omega\sin\frac\varphi2\left(\sin\frac\varphi2\ ;\ \cos\frac\varphi2\right)$. D'où
> $$\boxed{v=2R_0\omega\left|\sin\frac\varphi2\right|},\qquad\vec\tau=\left(\sin\frac\varphi2\ ;\ \cos\frac\varphi2\right).$$
> Au sommet ($\varphi=\pi$) : $v=2R_0\omega=2V$ ; au contact ($\varphi=0$) : $v=0$. Le point $T=(R_0\varphi,2R_0)$, point le plus haut de la roue, vérifie $\overrightarrow{MT}=R_0(\sin\varphi,\,1+\cos\varphi)=2R_0\cos\frac\varphi2\left(\sin\frac\varphi2,\cos\frac\varphi2\right)\parallel\vec\tau$ : la tangente à la cycloïde passe par le point haut de la roue. Autrement dit $\vec v\perp\overrightarrow{IM}$ : la roue tourne autour de $I$.
>
> **(d) Accélération**
>
> $\ddot x=R_0\omega^2\sin\varphi$, $\ddot y=R_0\omega^2\cos\varphi$ :
> $$\boxed{\vec a=R_0\omega^2\,(\sin\varphi\ ;\ \cos\varphi)},\qquad\boxed{a=R_0\omega^2=\text{cte}}.$$
> On remarque que $\overrightarrow{MC}=R_0(\sin\varphi,\cos\varphi)$ : $\vec a=\omega^2\,\overrightarrow{MC}$ est dirigée vers le **centre de la roue**. Explication : le centre de la roue est en translation uniforme, donc le mouvement de $M$ par rapport à $C$ est un cercle uniforme dont l'accélération (centripète) est la même dans le référentiel du sol, car le référentiel du centre est en translation rectiligne uniforme (galiléen).
>
> **(e) Composantes et rayon de courbure**
>
> $\vec a\cdot\vec v=R_0^2\omega^3\left[(1-\cos\varphi)\sin\varphi+\sin\varphi\cos\varphi\right]=R_0^2\omega^3\sin\varphi$, donc
> $$a_T=\frac{R_0^2\omega^3\sin\varphi}{2R_0\omega\sin\frac\varphi2}=\boxed{R_0\omega^2\cos\frac\varphi2}.$$
> Alors $a_N=\sqrt{a^2-a_T^2}=\boxed{R_0\omega^2\sin\frac\varphi2}$ et
> $$R=\frac{v^2}{a_N}=\frac{4R_0^2\omega^2\sin^2\frac\varphi2}{R_0\omega^2\sin\frac\varphi2}=\boxed{4R_0\sin\frac\varphi2}.$$
> **Vérification géométrique :** le point de contact $I=(R_0\varphi,0)$ vérifie $\overrightarrow{MI}=R_0(\sin\varphi,-(1-\cos\varphi))=2R_0\sin\frac\varphi2\left(\cos\frac\varphi2,-\sin\frac\varphi2\right)$, vecteur unitaire $\vec n=\left(\cos\frac\varphi2,-\sin\frac\varphi2\right)\perp\vec\tau$. La normale à la trajectoire passe donc par $I$, et $IM=2R_0\sin\frac\varphi2$ ; ainsi $R=2\,IM$ et $v=\omega\,IM$ $\surd$.
>
> **(f) Cas particuliers**
>
> **Sommet** ($\varphi=\pi$) : $v=2R_0\omega$, $a_T=0$ (vitesse maximale), $a_N=R_0\omega^2$, $R=4R_0$ ; $\vec a$ pointe vers le bas, vers $C$. Le cercle osculateur est quatre fois plus grand que la roue et son centre est à $2R_0$ sous le sol (à l'altitude $-2R_0$).
>
> **Contact** ($\varphi\to0^+$) : $v\to0$, $a_T\to R_0\omega^2$ (la vitesse croît à partir de zéro), $a_N\to0$ et $R\to0$ ; $\vec a\to R_0\omega^2\,\vec u_y$ est **verticale** vers le haut. Le point arrive vertical, s'arrête une fraction d'instant puis repart verticalement : c'est un **point de rebroussement** ; $R=0$ ne signifie pas que le mouvement s'interrompt, mais que la tangente tourne de $180^\circ$ en un temps infiniment bref.



**q3.** **3/ Longueur et application numérique.**


(a) Calculer la longueur $L$ d'une arche. Vérifier $R=\left|\dfrac{\mathrm ds}{\mathrm d\alpha}\right|$ avec $\alpha$ l'angle de la tangente avec $Ox$.

(b) Application. Une roue de vélo de rayon $R_0=0{,}35\ \mathrm m$ roule à $36\ \mathrm{km/h}$. Calculer $\omega$, la vitesse et l'accélération du point haut, la période de rotation, la longueur d'une arche et l'accélération (en unités de $g$) d'un caillou sur la jante.


> [!tip]- 💡 Coup de pouce
> $L=\int_0^{2\pi/\omega}v\,\mathrm dt$ avec $v=2R_0\omega\sin\frac{\omega t}2$. Pour $\alpha$ : $\vec\tau=(\sin\frac\varphi2,\cos\frac\varphi2)=(\cos\alpha,\sin\alpha)$ donne $\alpha=\frac\pi2-\frac\varphi2$.




> [!success]- ✅ Correction
> $L=8R_0$ ; $\alpha=\frac\pi2-\frac\varphi2$, $\mathrm ds=2R_0\sin\frac\varphi2\,\mathrm d\varphi$, $\left|\dfrac{\mathrm d\alpha}{\mathrm ds}\right|=\dfrac1{4R_0\sin(\varphi/2)}$ $\surd$. AN : $\omega\approx28{,}6$ rad/s, $v_{haut}=72$ km/h, $a=R_0\omega^2\approx286\ \mathrm{m\,s^{-2}}\approx29\,g$, $T\approx0{,}22$ s, $L=2{,}8$ m.




> [!example]- 📝 Solution détaillée
> **(g) Longueur d'une arche et vérification**
>
> $L=\displaystyle\int_0^{2\pi/\omega}2R_0\omega\sin\frac{\omega t}2\,\mathrm dt=2R_0\int_0^{2\pi}\sin\frac\varphi2\,\mathrm d\varphi=2R_0\cdot4=\boxed{8R_0}$ : quatre fois le diamètre, résultat indépendant de $\omega$ (propriété géométrique de la courbe), comparable au résultat $8a$ de la cardioïde (TD2).
>
> Vérification de $R$ : $\vec\tau=(\cos\alpha,\sin\alpha)=(\sin\frac\varphi2,\cos\frac\varphi2)$ donne $\alpha=\frac\pi2-\frac\varphi2$ donc $\mathrm d\alpha=-\frac12\mathrm d\varphi$ ; $\mathrm ds=v\,\mathrm dt=2R_0\sin\frac\varphi2\,\mathrm d\varphi$. Ainsi
> $$\frac1R=\left|\frac{\mathrm d\alpha}{\mathrm ds}\right|=\frac{1/2}{2R_0\sin\frac\varphi2}\ \Longrightarrow\ R=4R_0\sin\frac\varphi2\ \checkmark.$$
>
> **(h) Application numérique**
>
> $V=36\ \mathrm{km/h}=10\ \mathrm{m/s}$ ; $\omega=\dfrac V{R_0}=\dfrac{10}{0{,}35}\approx28{,}6\ \mathrm{rad/s}$ (environ $4{,}5$ tours par seconde). Période de rotation : $T=\dfrac{2\pi}\omega\approx0{,}22\ \mathrm s$. **Point haut** : $v=2V=20\ \mathrm{m/s}=72\ \mathrm{km/h}$ ; $a=R_0\omega^2=\dfrac{V^2}{R_0}\approx286\ \mathrm{m\,s^{-2}}$ ; $R=4R_0=1{,}4\ \mathrm m$. **Point bas** : $v=0$ (au contact). **Longueur d'une arche** : $L=8R_0=2{,}8\ \mathrm m$ (alors que $2\pi R_0=2{,}2\ \mathrm m$ est la distance parcourue par le centre). Le caillou sur la jante subit en permanence $a=R_0\omega^2\approx286\ \mathrm{m\,s^{-2}}\approx29\,g$ : c'est pourquoi il faut un collage solide et pourquoi les gouttes d'eau se détachent de la roue (dont $a_N$ est trop grande pour la tension superficielle).




> [!note]- 🔗 Liens avec d'autres disciplines
> **Mécanique, ingénierie**
>
> Roues, engrenages (dents en développante de cercle ou en cycloïde dans les horloges), bielle-manivelle, trains (boudin de roue qui dépasse le contact : trochoïde allongée).
>
> **Histoire des sciences**
>
> La cycloïde est la « Hélène des géomètres » (XVIIe siècle) : Galilée, Mersenne, Roberval, Pascal, Huygens, Bernoulli ont étudié sa longueur, son aire, sa tautochronie et sa brachistochronie.
>
> **Physique des vélos et véhicules**
>
> La boue projetée par la roue part tangentiellement à la trajectoire de la roue avec la vitesse $v=2V\sin(\varphi/2)$ : les garde-boue sont placés pour intercepter ces projections.




> [!question]- 🔭 Aller plus loin — CPGE : Développée de la cycloïde (Huygens)
> Le centre de courbure est $C_c=M+R\,\vec n$ avec $\vec n=\left(\cos\frac\varphi2\ ;\ -\sin\frac\varphi2\right)$. Montrer que $C_c=\left(R_0(\varphi+\sin\varphi)\ ;\ -R_0(1-\cos\varphi)\right)$ : c'est la même cycloïde, translatée du vecteur $(-\pi R_0\ ;\ -2R_0)$ (poser $\psi=\varphi+\pi$). Cette propriété permet de construire un pendule **isochrone** (Huygens).




> [!question]- 🔭 Aller plus loin — Licence : Aire sous une arche et brachistochrone
> L'aire sous une arche vaut $\int_0^{2\pi R_0}y\,\mathrm dx=3\pi R_0^2$, soit trois fois l'aire de la roue (Roberval, Galilée). La cycloïde est aussi la courbe de plus courte durée (**brachistochrone**) et la courbe tautochrone : une bille lâchée sans vitesse d'un point quelconque d'une cycloïde inversée arrive en bas au même instant.




> [!question]- 🔭 Aller plus loin — Master : Trochoïdes
> Un point à la distance $d\neq R_0$ du centre décrit une trochoïde : $x=R_0\varphi-d\sin\varphi$, $y=R_0-d\cos\varphi$. Pour $d<R_0$ (point intérieur) la courbe est sans rebroussement ; pour $d>R_0$ (point extérieur, ex. : boudin d'une roue de train) elle présente des boucles qui font **reculer** le point au bas de la roue. Montrer que la vitesse du point bas du boudin est dirigée vers l'arrière.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex1-base-de-frenet-demonstrations-de-cours-et-applications|Exercice 1 — Base de Frenet : démonstrations de cours et applications]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex2-mouvement-curviligne-uniforme-cercle-parabole-applications|Exercice 2 — Mouvement curviligne uniforme : cercle, parabole, applications]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex3-circuit-de-monaco-courbure-et-acceleration-a-vitesse-constante|Exercice 3 — Circuit de Monaco : courbure et accélération à vitesse constante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex4-abscisse-curviligne-et-rayon-de-courbure-d-une-trajectoire-parabolique|Exercice 4 — Abscisse curviligne et rayon de courbure d'une trajectoire parabolique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex6-raccordement-routier-en-clothoide-courbure-variable-et-jerk|Exercice 6 — Raccordement routier en clothoïde (courbure variable et « jerk »)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex7-cercle-d-adherence-freiner-et-tourner-en-meme-temps|Exercice 7 — Cercle d'adhérence : freiner et tourner en même temps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex8-tir-parabolique-vu-dans-la-base-de-frenet|Exercice 8 — Tir parabolique vu dans la base de Frenet]]


