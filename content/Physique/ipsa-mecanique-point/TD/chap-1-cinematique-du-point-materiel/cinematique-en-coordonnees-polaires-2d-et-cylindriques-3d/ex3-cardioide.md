---
title: "Exercice 3 — Cardioïde"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · <a href="/pdfs/td2_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td2_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td2_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 3. Cardioïde *(facultatif)*

Dans le plan $Oxy$, on considère le déplacement d'un mobile assimilé à un point $M$ le long d'une courbe
d'équation polaire
$$r(\theta)=a\,(1+\cos\theta),$$
appelée **cardioïde** (courbe « en forme de cœur »).

**q1.** Étude de la courbe.


(a) Quelle est la dimension de $a$ ?

(b) Choisir une valeur pour $a$ et représenter la cardioïde en plaçant les points correspondant à $\theta=0$, $\theta=\dfrac\pi3$, $\theta=\dfrac\pi2$, $\theta=\dfrac{2\pi}3$, $\theta=\pi$, $\theta=\dfrac{4\pi}3$, $\theta=2\pi$.

(c) Représenter la base polaire $(\vec u_r,\vec u_\theta)$ en un point $P$ de la cardioïde, correspondant à $\theta=\dfrac\pi3$.

> [!tip]- 💡 Coup de pouce
> $r$ est une distance. Pour placer un point, calculez $r(\theta)$, puis $x=r\cos\theta$ et $y=r\sin\theta$. En $P$, $\vec u_r$ est dirigé selon $\overrightarrow{OP}$ et $\vec u_\theta$ en est la rotation de $+90^\circ$.


> [!success]- ✅ Correction
> $[a]=\mathrm L$. Pour $a=2$ cm : $r=4,\ 3,\ 2,\ 1,\ 0,\ 1,\ 4$ cm pour les sept angles ; courbe symétrique par rapport à $Ox$ avec un point de rebroussement en $O$.


> [!example]- 📝 Solution détaillée
> **(a) Dimension de $a$**
>
> $r=a(1+\cos\theta)$ est une longueur et $1+\cos\theta$ est sans dimension : $[a]=\mathrm L$.
>
> **(b) Points de la cardioïde**
>
> On choisit $a=2$ cm. On calcule $r=a(1+\cos\theta)$ puis $x=r\cos\theta$, $y=r\sin\theta$ :
> $$
> \begin{array}{c|ccccccc}
> \theta & 0 & \pi/3 & \pi/2 & 2\pi/3 & \pi & 4\pi/3 & 2\pi\\
> \hline
> r~(\mathrm{cm}) & 4 & 3 & 2 & 1 & 0 & 1 & 4\\
> x~(\mathrm{cm}) & 4 & 1{,}5 & 0 & -0{,}5 & 0 & -0{,}5 & 4\\
> y~(\mathrm{cm}) & 0 & 2{,}6 & 2 & 0{,}87 & 0 & -0{,}87 & 0
> \end{array}
> $$
> La courbe est fermée, symétrique par rapport à $Ox$ ($r(2\pi-\theta)=r(\theta)$). Elle passe par $(2a,0)$ pour $\theta=0$ (point le plus éloigné de $O$) et revient à l'origine pour $\theta=\pi$, où elle présente un **point de rebroussement** (« creux » du cœur).
>
> **(c) Base polaire en $P$**
>
> Pour $\theta=\pi/3$, $P$ est à la distance $r=\tfrac32a$ de $O$, et
> $$\vec u_r=\cos\tfrac\pi3\,\vec\imath+\sin\tfrac\pi3\,\vec\jmath=\tfrac12\vec\imath+\tfrac{\sqrt3}2\vec\jmath,\qquad\vec u_\theta=-\tfrac{\sqrt3}2\vec\imath+\tfrac12\vec\jmath.$$
> On trace $\vec u_r$ le long de la droite $(OP)$, en s'éloignant de $O$, et $\vec u_\theta$ perpendiculaire, orienté dans le sens des $\theta$ croissants. Contrairement au cercle, $\vec u_\theta$ n'est pas tangent à la courbe ici (car $r$ varie avec $\theta$).


**q2.** La courbe est parcourue avec une vitesse angulaire $\dot\theta=\omega$ constante, avec $\theta(0)=0$.


(a) Déterminer l'expression de $\theta(t)$ et en déduire $r(t)$.

(b) Déterminer l'expression du vecteur vitesse $\vec v$ de $M$ dans la base $(\vec u_r,\vec u_\theta)$ et calculer sa norme.

(c) Représenter la vitesse du mobile lorsqu'il se situe au point $P$.

(d) En quel point de la trajectoire la vitesse de $M$ est-elle maximale ?

> [!tip]- 💡 Coup de pouce
> Intégrez $\dot\theta=\omega$. Pour la vitesse, utilisez $\vec v=\dot r\,\vec u_r+r\dot\theta\,\vec u_\theta$ avec $\dot r=-a\omega\sin\omega t$. Pour simplifier la norme, développez $\sin^2+(1+\cos)^2$.


> [!success]- ✅ Correction
> $\theta=\omega t$, $r=a(1+\cos\omega t)$ ; $\vec v=-a\omega\sin(\omega t)\,\vec u_r+a\omega(1+\cos\omega t)\,\vec u_\theta$ ; $\|\vec v\|=2a\omega\,|\cos(\omega t/2)|$ ; vitesse maximale ($2a\omega$) en $\theta=0$, point $(2a,0)$.


> [!example]- 📝 Solution détaillée
> **(d) Équations horaires**
>
> $\dot\theta=\omega$ constant et $\theta(0)=0$ donnent $\boxed{\theta(t)=\omega t}$, donc
> $$\boxed{r(t)=a\,(1+\cos\omega t)}.$$
>
> **(e) Vecteur vitesse**
>
> $\dot r=-a\omega\sin\omega t$ et $r\dot\theta=a\omega(1+\cos\omega t)$ :
> $$\boxed{\vec v=-a\omega\sin(\omega t)\,\vec u_r+a\omega\,(1+\cos\omega t)\,\vec u_\theta}.$$
> Les deux composantes sont orthogonales, donc
> $$\|\vec v\|^2=a^2\omega^2\left[\sin^2\omega t+(1+\cos\omega t)^2\right]=a^2\omega^2\,(2+2\cos\omega t).$$
> Avec $1+\cos\omega t=2\cos^2(\omega t/2)$ :
> $$\boxed{\|\vec v\|=2a\omega\,\left|\cos\frac{\omega t}2\right|}.$$
>
> **(f) Vitesse au point $P$ ($\theta=\pi/3$)**
>
> Pour $\omega t=\pi/3$ : $v_r=-a\omega\sin\frac\pi3=-\frac{\sqrt3}2a\omega\approx-0{,}87\,a\omega$ et $v_\theta=a\omega\left(1+\frac12\right)=\frac32a\omega$. D'où $\|\vec v\|=a\omega\sqrt{\tfrac34+\tfrac94}=\sqrt3\,a\omega\approx1{,}73\,a\omega$, ce qui coïncide avec $2a\omega\cos\frac\pi6=\sqrt3\,a\omega$. En $P$, on trace $\vec v$ avec une composante **rentrante** ($v_r<0$ : le point se rapproche de $O$) et une grande composante orthoradiale ($v_\theta>0$ : le point tourne dans le sens trigonométrique).
>
> **(g) Vitesse maximale**
>
> $\|\vec v\|$ est maximale lorsque $|\cos(\omega t/2)|=1$, soit $\omega t=0\ [2\pi]$, c'est-à-dire $\theta=0$ : le point $(2a,0)$, le plus éloigné de $O$. La vitesse vaut alors $v_{\max}=2a\omega$, dirigée selon $\vec u_\theta=\vec\jmath$ ($v_r=0$ en ce point). À l'inverse, $\|\vec v\|=0$ pour $\omega t=\pi$ : le point passe en $O$, point de rebroussement, où il s'arrête un instant avant de repartir.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]]

