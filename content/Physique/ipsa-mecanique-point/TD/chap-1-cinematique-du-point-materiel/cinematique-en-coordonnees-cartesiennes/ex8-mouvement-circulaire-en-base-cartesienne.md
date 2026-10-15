---
title: "Exercice 8 — Mouvement circulaire en base cartésienne"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td1_PhV111_corrige.pdf) · [📄 Énoncé](/pdfs/td1_PhV111_enonces.pdf) · [📄 Aides](/pdfs/td1_PhV111_aides.pdf) · [📄 Fiche enseignant](/pdfs/td1_PhV111_fiche.pdf)

### Exercice 8. Mouvement circulaire en base cartésienne

Un point matériel $M$ se déplace dans un plan muni d'un repère cartésien $(O,\vec\imath,\vec\jmath)$.
Son rayon vecteur $\vec r$ s'écrit en fonction du temps :
$$\vec r(t) = R\cos(\omega t)\,\vec\imath + R\sin(\omega t)\,\vec\jmath \qquad \text{avec } R,\,\omega \text{ constantes}.$$

**q1.** Équations horaires et trajectoire de $M$.


(a) Donner la dimension des constantes $R$ et $\omega$.

(b) Donner l'expression des équations horaires $x(t)$ et $y(t)$ de $M$.

(c) Déterminer l'équation de la trajectoire de $M$ (indication : calculer puis relier $x^2$ et $y^2$). De quelle courbe s'agit-il ?

(d) Représenter graphiquement la trajectoire de $M$, en prenant $R=4\times10^{-2}$ S.I. et $\omega=\pi/6$ S.I.

(e) Préciser sur le graphique la position de $M$ aux instants $t_0=0$ s, $t_1=1$ s, ..., $t_6=6$ s.

(f) Que peut-on dire du mouvement de $M$ ?

> [!tip]- 💡 Coup de pouce
> Utilisez $\cos^2+\sin^2=1$ pour éliminer $t$ entre $x(t)$ et $y(t)$.


> [!success]- ✅ Correction
> $x^2+y^2=R^2$ : cercle de rayon $R$ centré en $O$, parcouru à vitesse angulaire constante $\omega$ (mouvement circulaire uniforme).


> [!example]- 📝 Solution détaillée
> **(a) Dimensions**
>
> $\vec r(t)$ est une longueur, donc $R$ est une longueur : $[R]=\mathrm L$. L'argument $\omega t$ d'un cosinus/sinus doit être sans dimension (un angle, en radian), donc $\omega$ est l'inverse d'un temps : $[\omega]=\mathrm T^{-1}$ (homogène à une vitesse angulaire, en rad/s).
>
> **(b) Équations horaires**
>
> En projetant $\vec r(t)$ sur $(\vec\imath,\vec\jmath)$ :
> $$\boxed{x(t) = R\cos(\omega t)}, \qquad \boxed{y(t) = R\sin(\omega t)}.$$
>
> **(c) Équation de la trajectoire**
>
> On calcule $x^2(t) + y^2(t) = R^2\cos^2(\omega t) + R^2\sin^2(\omega t) = R^2\big(\cos^2(\omega t)+\sin^2(\omega t)\big) = R^2$, indépendamment de $t$. La trajectoire vérifie donc :
> $$\boxed{x^2+y^2=R^2},$$
> c'est l'équation d'un **cercle de rayon $R$ centré en $O$**.
>
> **(d)-(e) Tracé et positions successives**
>
> Avec $R=0{,}04$ m et $\omega=\pi/6$ rad/s (période $T=2\pi/\omega=12$ s), on calcule $\theta(t)=\omega t$ puis $x=R\cos\theta$, $y=R\sin\theta$ :
>
> $$
> \begin{array}{c|ccccccc}
>   t~ (s) & 0 & 1 & 2 & 3 & 4 & 5 & 6 \\
>   \hline 
>   \theta~ (^\circ) & 0 & 30 & 60 & 90 & 120 & 150 & 180 \\
>   x ~ (m) & 0,040 & 0,035 & 0,020 & 0 & -0,020 & -0,035 & -0,040 \\
>   y ~ (m) & 0 & 0,020 & 0,035 & 0,040 & 0,035 & 0,020 & 0
> \end{array}
> $$
>
> %| $t$ (s) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
> %|---|---|---|---|---|---|---|---|
> %| $\theta$ (°) | 0 | 30 | 60 | 90 | 120 | 150 | 180 |
> %| $x$ (m) | 0,040 | 0,035 | 0,020 | 0 | -0,020 | -0,035 | -0,040 |
> %| $y$ (m) | 0 | 0,020 | 0,035 | 0,040 | 0,035 | 0,020 | 0 |
>
> On place ces 7 points sur le cercle de rayon 0,04 m : ils sont **régulièrement espacés angulairement** (30° entre chaque, puisque $\Delta t=1$ s est constant et $\omega$ est constant), ce qui illustre visuellement le caractère uniforme du mouvement.
>
> **(f) Nature du mouvement**
>
> Le point $M$ décrit un **mouvement circulaire uniforme** : trajectoire circulaire de rayon $R$, parcourue à vitesse angulaire constante $\omega$ (le paramètre $\theta(t)=\omega t$ croît linéairement avec le temps).


**q2.** Vitesse et accélération de $M$.


(a) Déterminer l'expression du vecteur vitesse $\vec v$ de $M$ et de sa norme $\vert \vec v\vert$.

(b) Déterminer l'expression du vecteur accélération $\vec a$ de $M$ et de sa norme $\vert\vec a\vert$.

(c) Représenter sur le graphique la vitesse $\vec v$ et l'accélération $\vec a$ de $M$ aux instants $t_1$ et $t_3$ (échelle adéquate).

(d) En un point de la trajectoire, représenter la base cartésienne $(\vec u_x,\vec u_y)$ et faire apparaître les composantes de $\vec v$ et $\vec a$.

(e) Donner la définition d'un mouvement uniforme. Le mouvement de $M$ peut-il être uniforme si son accélération est non nulle ?

> [!tip]- 💡 Coup de pouce
> Dérivez composante par composante ; pour la norme, ressortez le facteur commun $R\omega$ (ou $R\omega^2$) avant d'utiliser $\cos^2+\sin^2=1$.


> [!success]- ✅ Correction
> $\vec v = -R\omega\sin(\omega t)\vec\imath + R\omega\cos(\omega t)\vec\jmath$, $\|\vec v\|=R\omega$ (constant). $\vec a = -\omega^2\vec r$, $\|\vec a\|=R\omega^2$ (constant). Oui, le mouvement est uniforme malgré $\vec a\neq\vec 0$ : l'accélération est purement centripète.


> [!example]- 📝 Solution détaillée
> **(a) Vecteur vitesse et sa norme**
>
> En dérivant $x(t)$ et $y(t)$ par rapport à $t$ (la base $(\vec\imath,\vec\jmath)$ étant fixe) :
> $$\boxed{\vec v(t) = -R\omega\sin(\omega t)\,\vec\imath + R\omega\cos(\omega t)\,\vec\jmath}.$$
> $$\|\vec v\|^2 = R^2\omega^2\sin^2(\omega t) + R^2\omega^2\cos^2(\omega t) = R^2\omega^2 \quad\Longrightarrow\quad \boxed{\|\vec v\| = R\omega} \ (\text{constant}).$$
>
> **(b) Vecteur accélération et sa norme**
>
> En dérivant à nouveau :
> $$\vec a(t) = -R\omega^2\cos(\omega t)\,\vec\imath - R\omega^2\sin(\omega t)\,\vec\jmath = -\omega^2\big(R\cos(\omega t)\,\vec\imath + R\sin(\omega t)\,\vec\jmath\big),$$
> soit :
> $$\boxed{\vec a(t) = -\omega^2\,\vec r(t)}.$$
> L'accélération est donc en permanence **colinéaire à $\vec r$ et de sens opposé** : elle pointe toujours vers le centre $O$ (accélération centripète). Sa norme :
> $$\boxed{\|\vec a\| = R\omega^2} \ (\text{constante}).$$
>
> **(c)-(d) Représentation graphique**
>
> Aux instants $t_1=1$ s ($\theta=30°$) et $t_3=3$ s ($\theta=90°$), on place $M$ sur le cercle, puis on trace $\vec v$ **tangent au cercle** (perpendiculaire à $\vec r$, dans le sens du mouvement, c'est-à-dire dans le sens trigonométrique ici car $\theta$ croît), et $\vec a$ **radial, pointant vers $O$**. En décomposant sur $(\vec u_x,\vec u_y)$ en un point quelconque, les composantes sont directement celles calculées en (a) et (b) : $v_x=-R\omega\sin\theta$, $v_y=R\omega\cos\theta$, $a_x=-R\omega^2\cos\theta$, $a_y=-R\omega^2\sin\theta$.
>
> **(e) Mouvement uniforme et accélération non nulle**
>
> Un mouvement est dit **uniforme** lorsque la norme du vecteur vitesse (la vitesse "scalaire", ou célérité) est **constante au cours du temps** — ce qui ne préjuge en rien de la direction de $\vec v$, ni de l'accélération.
>
> Ici, on a montré en (a) que $\|\vec v\|=R\omega$ est bien constant : le mouvement circulaire est donc **uniforme**, bien que $\vec a\neq\vec 0$ (question (b)). Ceci est possible car l'accélération est ici **purement radiale (centripète)**, donc perpendiculaire à $\vec v$ à chaque instant : elle ne fait que courber la trajectoire (faire tourner la direction de $\vec v$) sans jamais modifier sa norme. On retiendra que : **accélération non nulle n'implique pas mouvement non uniforme** — seule une composante d'accélération tangentielle (colinéaire à $\vec v$) modifie la norme de la vitesse.


**q3.** Application : le mouvement de révolution de la Lune autour de la Terre s'accomplit en 28 jours sur une trajectoire assimilée à un cercle, parcourue de façon uniforme.


(a) Quelle est la vitesse angulaire du mouvement de révolution de la Lune ?

(b) Quelle serait la vitesse angulaire si soudainement la vitesse (linéaire) était réduite de moitié et si le rayon de l'orbite quadruplait ?

> [!tip]- 💡 Coup de pouce
> Utilisez $\omega = v/R$ (issu de $v=R\omega$, question 2a) pour la question (b).


> [!success]- ✅ Correction
> $\omega \approx 2{,}6\times10^{-6}$ rad/s ; $\omega' = \omega/8$.


> [!example]- 📝 Solution détaillée
> **(a) Vitesse angulaire de la Lune**
>
> La période de révolution est $T = 28$ jours $= 28\times 24\times3600 = 2\,419\,200$ s. Comme le mouvement est circulaire uniforme, $\omega = 2\pi/T$ (l'angle balayé pendant une période complète est $2\pi$) :
> $$\omega = \frac{2\pi}{2\,419\,200} \approx \boxed{2{,}60\times10^{-6}~\text{rad/s}}.$$
>
> **(b) Nouvelle vitesse angulaire après modification de $v$ et $R$**
>
> D'après la question 2(a), $v = R\omega$, donc $\omega = v/R$. Si la vitesse est divisée par 2 ($v' = v/2$) et le rayon multiplié par 4 ($R' = 4R$), la nouvelle vitesse angulaire vaut :
> $$\omega' = \frac{v'}{R'} = \frac{v/2}{4R} = \frac{1}{8}\cdot\frac{v}{R} = \boxed{\frac{\omega}{8}} \approx 3{,}25\times10^{-7}~\text{rad/s}.$$
> La vitesse angulaire est donc divisée par 8 : elle est affectée à la fois par la réduction de la vitesse linéaire (facteur $1/2$) et par l'augmentation du rayon (facteur $1/4$ supplémentaire), les deux effets se cumulant pour ralentir la rotation.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]]

