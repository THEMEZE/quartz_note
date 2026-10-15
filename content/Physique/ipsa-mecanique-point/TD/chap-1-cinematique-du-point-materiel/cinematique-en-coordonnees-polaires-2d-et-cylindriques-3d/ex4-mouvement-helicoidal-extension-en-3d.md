---
title: "Exercice 4 — Mouvement hélicoïdal (extension en 3D)"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td2_PhV111_corrige.pdf) · [📄 Énoncé](/pdfs/td2_PhV111_enonces.pdf) · [📄 Aides](/pdfs/td2_PhV111_aides.pdf) · [📄 Fiche enseignant](/pdfs/td2_PhV111_fiche.pdf)

### Exercice 4. Mouvement hélicoïdal (extension en 3D) *(facultatif)*

Dans l'espace muni d'un repère cartésien $Oxyz$, un point $M$ décrit une **hélice circulaire** d'axe $Oz$,
d'équations horaires (en coordonnées cylindriques)
$$\begin{cases}r(t)=a\\\theta(t)\\z(t)=h\,\theta(t)\end{cases}$$
où $a$ et $h$ sont des paramètres constants et $\theta(t)$ est l'angle entre $Ox$ et $\overrightarrow{Om}$,
$m$ étant la projection du point $M$ sur le plan $Oxy$. On note $\dot\theta$ la vitesse angulaire.

**q1.** (a) Compléter la figure avec les données du problème : représenter l'axe $Oz$, le point $M$, sa projection $m$ sur $Oxy$, les coordonnées cylindriques $(r,\theta,z)$ et la base $(\vec u_r,\vec u_\theta,\vec k)$.

> [!tip]- 💡 Coup de pouce
> $\overrightarrow{OM}=\overrightarrow{Om}+\overrightarrow{mM}$ avec $\overrightarrow{Om}=a\,\vec u_r$ et $\overrightarrow{mM}=z\,\vec k$.


> [!success]- ✅ Correction
> $\overrightarrow{OM}=a\,\vec u_r+h\theta\,\vec k$ ; $\vec u_r$ dirigé de $O$ vers $m$, $\vec u_\theta$ perpendiculaire à $\vec u_r$ dans le plan horizontal, $\vec k$ vertical ascendant.


> [!example]- 📝 Solution détaillée
> **(a) Construction de la figure**
>
> On trace le cylindre d'axe $Oz$ et de rayon $a$. Le point $m$ est la projection de $M$ sur $Oxy$, à la distance $a$ de $O$, à l'angle $\theta$ de $Ox$. On trace alors :
>
>
> - $\vec u_r$ : horizontal, de $O$ vers $m$ (direction radiale) ;
> - $\vec u_\theta$ : horizontal, perpendiculaire à $\vec u_r$, dans le sens des $\theta$ croissants ;
> - $\vec k$ : vertical, vers le haut ; $\overrightarrow{mM}=z\,\vec k$ avec $z=h\theta$.
>
>
> Le vecteur position est $\overrightarrow{OM}=a\,\vec u_r+h\theta\,\vec k$. Quand $\theta$ augmente de $2\pi$, le point revient à la même position $m$ mais à l'altitude $2\pi h$ plus haute : c'est le **pas** de l'hélice.


**q2.** (b) Établir l'expression du vecteur vitesse $\vec v$ et du vecteur accélération $\vec a$ de $M$ et leur norme.

> [!tip]- 💡 Coup de pouce
> Dérivez $\overrightarrow{OM}=a\,\vec u_r+h\theta\,\vec k$ par rapport au temps. $a$, $h$ et $\vec k$ sont constants ; seuls $\vec u_r$ et $\theta$ varient.


> [!success]- ✅ Correction
> $\vec v=a\dot\theta\,\vec u_\theta+h\dot\theta\,\vec k$, $\|\vec v\|=|\dot\theta|\sqrt{a^2+h^2}$ ; $\vec a=-a\dot\theta^2\,\vec u_r+a\ddot\theta\,\vec u_\theta+h\ddot\theta\,\vec k$, $\|\vec a\|=\sqrt{a^2\dot\theta^4+(a^2+h^2)\ddot\theta^2}$.


> [!example]- 📝 Solution détaillée
> **(b) Vecteur vitesse**
>
> $$\vec v=a\,\frac{\mathrm d\vec u_r}{\mathrm dt}+h\dot\theta\,\vec k=\boxed{a\dot\theta\,\vec u_\theta+h\dot\theta\,\vec k}.$$
> Les vecteurs $\vec u_\theta$ et $\vec k$ sont orthogonaux et unitaires :
> $$\|\vec v\|=\boxed{|\dot\theta|\sqrt{a^2+h^2}}.$$
>
> **(b) Vecteur accélération**
>
> $$\vec a=a\ddot\theta\,\vec u_\theta+a\dot\theta\,\frac{\mathrm d\vec u_\theta}{\mathrm dt}+h\ddot\theta\,\vec k=\boxed{-a\dot\theta^2\,\vec u_r+a\ddot\theta\,\vec u_\theta+h\ddot\theta\,\vec k}.$$
> Les trois composantes étant orthogonales,
> $$\|\vec a\|=\sqrt{a^2\dot\theta^4+a^2\ddot\theta^2+h^2\ddot\theta^2}=\boxed{\sqrt{a^2\dot\theta^4+(a^2+h^2)\,\ddot\theta^2}}.$$
> On retrouve la formule générale du point de cours avec $\dot r=\ddot r=0$ et $\ddot z=h\ddot\theta$.


**q3.** (c) Montrer que le vecteur vitesse $\vec v$ fait avec le plan $Oxy$ un angle constant.

> [!tip]- 💡 Coup de pouce
> Décomposez $\vec v$ en une partie horizontale (dans $Oxy$) et une partie verticale (selon $\vec k$). L'angle avec le plan est celui entre $\vec v$ et sa partie horizontale.


> [!success]- ✅ Correction
> $\tan\alpha=\dfrac{v_z}{\|\vec v_{\text{hor}}\|}=\dfrac ha$ : indépendant du temps et de $\theta(t)$.


> [!example]- 📝 Solution détaillée
> **(c) Angle avec le plan $Oxy$**
>
> La partie horizontale de $\vec v$ est $a\dot\theta\,\vec u_\theta$, de norme $a|\dot\theta|$ ; la partie verticale est $h\dot\theta\,\vec k$. L'angle $\alpha$ que fait $\vec v$ avec le plan $Oxy$ vérifie
> $$\tan\alpha=\frac{|h\dot\theta|}{a|\dot\theta|}=\boxed{\frac ha}\qquad\Longleftrightarrow\qquad\sin\alpha=\frac{h}{\sqrt{a^2+h^2}}.$$
> Cette valeur ne dépend ni de $t$, ni de $\theta$, ni de la loi $\theta(t)$ choisie (tant que $\dot\theta\neq0$) : l'angle est constant, ce qui est la propriété caractéristique de l'hélice (pente constante).


**q4.** (d) Montrer que, si le mouvement est uniforme, la norme du vecteur vitesse $\|\vec v\|$ est constante et que le vecteur accélération passe par l'axe du cylindre et est parallèle au plan $Oxy$.

> [!tip]- 💡 Coup de pouce
> Mouvement uniforme signifie $\|\vec v\|=$ cte. Que cela impose-t-il à $\dot\theta$, puis à $\ddot\theta$ ? Reportez dans $\vec a$.


> [!success]- ✅ Correction
> $\|\vec v\|=|\dot\theta|\sqrt{a^2+h^2}$ constante $\Rightarrow\dot\theta$ constant $\Rightarrow\ddot\theta=0$ et $\vec a=-a\dot\theta^2\,\vec u_r$ : horizontal, dirigé vers l'axe $Oz$.


> [!example]- 📝 Solution détaillée
> **(d) Norme constante**
>
> Le mouvement est uniforme lorsque $\|\vec v\|$ est constante. Comme $\|\vec v\|=|\dot\theta|\sqrt{a^2+h^2}$ avec $a^2+h^2$ constant et non nul, cela équivaut à $|\dot\theta|=$ cte, donc à $\dot\theta=\omega$ constant et $\ddot\theta=0$. Réciproquement, $\dot\theta$ constant donne $\|\vec v\|$ constante : on a l'équivalence.
>
> **(d) Accélération**
>
> Avec $\ddot\theta=0$, l'expression de la question (b) se réduit à
> $$\boxed{\vec a=-a\omega^2\,\vec u_r},\qquad\|\vec a\|=a\omega^2.$$
> $\vec a$ n'a pas de composante selon $\vec k$ : il est **parallèle au plan $Oxy$**. Il est dirigé selon $-\vec u_r$, c'est-à-dire de $M$ vers le point $(0,0,z)$ de l'axe $Oz$ situé à la même altitude : la droite d'action de $\vec a$ **coupe l'axe du cylindre**, perpendiculairement à celui-ci. On retrouve l'accélération centripète du mouvement circulaire de rayon $a$ : monter à vitesse verticale constante ($\dot z=h\omega$) n'ajoute aucune accélération.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]]

