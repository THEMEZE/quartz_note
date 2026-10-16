---
title: "Exercice 7 — Courbe de poursuite : les trois drones"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · <a href="/pdfs/td2_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 7. Courbe de poursuite : les trois drones *(facultatif)*

Trois drones $A_1$, $A_2$, $A_3$ sont initialement placés aux sommets d'un triangle équilatéral dont le centre
$O$ est à la distance $R$ de chaque sommet. À $t=0$, chaque drone $A_i$ vole à la **vitesse constante en norme** $v$
en visant en permanence le drone suivant ($A_1\to A_2\to A_3\to A_1$) : son vecteur vitesse est toujours dirigé
vers la position actuelle de sa cible. On généralise ensuite à $n$ mobiles aux sommets d'un polygone régulier à
$n$ côtés.

**q1.** (a) Pourquoi, par symétrie, le triangle reste-t-il équilatéral et son centre $O$ reste-t-il fixe ? En déduire qu'il suffit d'étudier le mouvement de $A_1$ en coordonnées polaires $(r,\theta)$ de centre $O$.

(b) Déterminer l'angle entre le vecteur vitesse de $A_1$ et le rayon $A_1O$ (faire un schéma). En déduire $\dot r$ et $r\dot\theta$ en fonction de $v$.

> [!tip]- 💡 Coup de pouce
> Dans un triangle équilatéral, le rayon $A_1O$ est la bissectrice de l'angle en $A_1$. La vitesse de $A_1$ est dirigée selon $\overrightarrow{A_1A_2}$.


**q2.** (a) Déterminer $r(t)$ et la durée $T$ au bout de laquelle les drones se rencontrent en $O$. Exprimer $T$ en fonction du côté $d$ du triangle initial.

(b) Déterminer $\theta(t)$. Combien de tours effectue chaque drone avant la rencontre ?

(c) Établir l'équation polaire $r(\theta)$ de la trajectoire et la nommer. Calculer la longueur $L$ parcourue par chaque drone.

> [!tip]- 💡 Coup de pouce
> $\dot r$ est constant : intégrez directement. Pour $\theta(t)$, reportez $r(t)$ dans $\dot\theta=\dfrac{v}{2r}$ et intégrez ; attention au comportement de $r\to0$. Pour $r(\theta)$, éliminez $t$ ou calculez $\dfrac{\mathrm dr}{\mathrm d\theta}=\dfrac{\dot r}{\dot\theta}$.


**q3.** (a) Calculer l'accélération $\vec a$ d'un drone dans la base polaire, sa norme et vérifier $\vec a\perp\vec v$. En déduire le rayon de courbure $\rho(r)$.

(b) **Généralisation à $n$ mobiles** (polygone régulier à $n$ côtés). Établir $\dot r$, $r\dot\theta$, $T$, $L$ et $\rho$ en fonction de $n$, $R$ et $v$. Vérifier les cas limites $n=2$ et $n\to\infty$.

(c) Application numérique : trois drones aux sommets d'un triangle équilatéral de côté $d=60$ m, $v=10$ m/s. Calculer $R$, $T$, $L$, le rayon de courbure initial et l'accélération initiale.

> [!tip]- 💡 Coup de pouce
> Dérivez $\dot r=-v\sin(\pi/n)$ et $r\dot\theta=v\cos(\pi/n)$ : $\ddot r=0$, $\dot\theta=\dfrac{v\cos(\pi/n)}r$ puis $\ddot\theta=-\dfrac{v\cos(\pi/n)\,\dot r}{r^2}$. Pour $n$ quelconque, l'angle entre $\vec v$ et $\vec u_r$ vaut $\pi-\left(\dfrac\pi2-\dfrac\pi n\right)$ (vitesse vers $O$).


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]]

