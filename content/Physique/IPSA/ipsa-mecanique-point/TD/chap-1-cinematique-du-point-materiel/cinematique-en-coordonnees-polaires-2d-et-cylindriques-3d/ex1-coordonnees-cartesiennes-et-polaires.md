---
title: "Exercice 1 — Coordonnées cartésiennes et polaires"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · <a href="/pdfs/td2_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td2_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td2_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 1. Coordonnées cartésiennes et polaires

On se place dans un plan muni d'un repère cartésien $Oxy$. Un point $M$ du plan peut être repéré soit par
ses coordonnées cartésiennes $(x,y)$, soit par ses **coordonnées polaires** $(r,\theta)$ : $r=OM$ est la
distance de $M$ à l'origine et $\theta$ est l'angle orienté entre l'axe $Ox$ et le vecteur $\overrightarrow{OM}$.

**q1.** (a) Rappeler les formules de passage entre coordonnées cartésiennes et coordonnées polaires.

> [!tip]- 💡 Coup de pouce
> Faites un schéma : le point $M$, ses projections sur $Ox$ et $Oy$, et le triangle rectangle de côtés $x$ et $y$.


> [!success]- ✅ Correction
> $x=r\cos\theta$, $y=r\sin\theta$ ; $r=\sqrt{x^2+y^2}$, $\cos\theta=x/r$, $\sin\theta=y/r$ (soit $\tan\theta=y/x$ avec une discussion sur le quadrant).


> [!example]- 📝 Solution détaillée
> **(a) Polaire vers cartésien**
>
> Dans le triangle rectangle formé par $O$, la projection de $M$ sur $Ox$ et $M$, l'hypoténuse vaut $r$ et l'angle en $O$ vaut $\theta$ :
> $$\boxed{x=r\cos\theta,\qquad y=r\sin\theta}.$$
>
> **(a) Cartésien vers polaire**
>
> Par Pythagore, puis en divisant :
> $$\boxed{r=\sqrt{x^2+y^2}},\qquad \cos\theta=\frac xr,\qquad \sin\theta=\frac yr,\qquad \tan\theta=\frac yx\ (x\neq0).$$
> Pour déterminer $\theta$, on regarde le signe de $x$ et de $y$ (quadrant). Exemple : $M(-1,1)$ a pour coordonnées polaires $r=\sqrt2$ et $\theta=3\pi/4$, alors que $\arctan(-1)=-\pi/4$. Pour $M=O$, $r=0$ et $\theta$ est indéterminé.


**q2.** - [(b)] Une courbe a pour équation cartésienne $x^2+y^2=4$. De quelle courbe s'agit-il ? Quelle est son équation en coordonnées polaires ?
- [(c)] Une courbe a pour équation cartésienne $x=y$. De quelle courbe s'agit-il ? Quelle est son équation en coordonnées polaires ?

> [!tip]- 💡 Coup de pouce
> Remplacez $x$ et $y$ par $r\cos\theta$ et $r\sin\theta$ et simplifiez. Pour (c), que se passe-t-il quand $r=0$ ?


> [!success]- ✅ Correction
> (b) Cercle de centre $O$ et de rayon $2$ : $r=2$. (c) Droite passant par $O$, de pente $1$ : $\theta=\pi/4\ [\pi]$.


> [!example]- 📝 Solution détaillée
> **(b) Cercle**
>
> $x^2+y^2=r^2(\cos^2\theta+\sin^2\theta)=r^2$, donc l'équation devient $r^2=4$, soit $\boxed{r=2}$ (avec $r\geq0$), $\theta$ quelconque. C'est un **cercle de centre $O$ et de rayon $2$**.
>
> **(c) Droite**
>
> $x=y\iff r\cos\theta=r\sin\theta\iff r(\cos\theta-\sin\theta)=0$. Soit $r=0$ (l'origine, qui appartient à la droite), soit $\tan\theta=1$, c'est-à-dire
> $$\boxed{\theta=\frac\pi4\ [\pi]}.$$
> C'est la **droite passant par $O$ de pente $1$**, première bissectrice des axes : la demi-droite $\theta=\pi/4$ ($r>0$) dans le premier quadrant, et la demi-droite $\theta=5\pi/4$ ($r>0$) dans le troisième. On peut aussi écrire $\theta=\pi/4$ en autorisant $r<0$.
>
> **Bilan comparatif**
>
> Le cercle centré en $O$ est « $r=$ constante » ($\theta$ libre) ; la droite passant par $O$ est « $\theta=$ constante » ($r$ libre). Les rôles sont symétriques.


**q3.** (d) En coordonnées polaires, $M$ a pour équations horaires $r(t)=3$ et $\theta(t)=\dfrac\pi6\,t$ (unités S.I.). Quelle est sa trajectoire ? Déterminer les équations horaires de $M$ en coordonnées cartésiennes.

> [!tip]- 💡 Coup de pouce
> $r$ est constant : quelle courbe obtient-on ? Reportez ensuite $r$ et $\theta(t)$ dans $x=r\cos\theta$ et $y=r\sin\theta$.


> [!success]- ✅ Correction
> Cercle de centre $O$ et de rayon $3$ m, parcouru à vitesse angulaire constante $\omega=\pi/6$ rad/s (période $12$ s). $x(t)=3\cos(\pi t/6)$ et $y(t)=3\sin(\pi t/6)$.


> [!example]- 📝 Solution détaillée
> **(d) Trajectoire**
>
> La distance à l'origine reste égale à $3$ m : la trajectoire est le **cercle de centre $O$ et de rayon $3$ m**. L'angle $\theta(t)=\frac\pi6 t$ croît linéairement : le cercle est parcouru à vitesse angulaire constante $\omega=\pi/6$ rad/s, dans le sens trigonométrique, avec la période $T=2\pi/\omega=12$ s.
>
> **(d) Équations horaires cartésiennes**
>
> $$\boxed{x(t)=3\cos\!\left(\frac{\pi t}{6}\right)},\qquad \boxed{y(t)=3\sin\!\left(\frac{\pi t}{6}\right)}.$$
> Vérification : $x^2+y^2=9$. Quelques positions : $t=0$ en $(3,0)$ ; $t=3$ s en $(0,3)$ ; $t=6$ s en $(-3,0)$ ; $t=12$ s de retour en $(3,0)$. On retrouve exactement la structure de l'exercice du TD1 sur le mouvement circulaire en base cartésienne, mais écrite ici en deux lignes en polaire : $r=3$, $\theta=\omega t$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-derivee-d-un-vecteur-unitaire-tournant|Exercice 1 — Dérivée d'un vecteur unitaire tournant]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]]

