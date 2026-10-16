---
title: "Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · <a href="/pdfs/td1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 11. La valve du vélo : cycloïde d'une roue qui roule *(facultatif)*

Une roue de rayon $R$ roule **sans glisser** sur un sol horizontal rectiligne. Son centre $C$ se déplace à la vitesse constante $V$, parallèlement au sol.
On étudie le mouvement d'un point $M$ de la jante (la valve d'un pneu de vélo, par exemple) dans le référentiel du sol, muni d'un repère $Oxy$ : $Ox$ est horizontal, dans le sens du déplacement, $Oy$ est vertical ascendant, et l'origine $O$ est la position de $M$ à l'instant $t=0$, lorsque $M$ touche le sol. À cet instant, le centre est en $C_0=(0,R)$. On note $\theta(t)$ l'angle dont la roue a tourné depuis $t=0$ (la roue tourne dans le sens horaire, comme il se doit pour avancer vers $+Ox$), et $\omega=\dot\theta$ sa vitesse angulaire, supposée constante.

**q1.** - [(a)] Justifier que la condition de non-glissement impose $V=R\omega$, puis donner la position $(x_C,y_C)$ du centre de la roue à l'instant $t$.
- [(b)] Déterminer les coordonnées $x(t)$ et $y(t)$ du point $M$.
- [(c)] Placer sur un graphique les positions de $M$ pour $\omega t=0,\ \pi/2,\ \pi,\ 3\pi/2,\ 2\pi$ et esquisser la trajectoire sur deux tours de roue.

> [!tip]- 💡 Coup de pouce
> Pour (a), la longueur d'arc de jante qui touche le sol pendant $t$ est $R\theta$ ; elle doit être égale à la distance parcourue par le centre. Pour (b), écrivez $\overrightarrow{OM}=\overrightarrow{OC}+\overrightarrow{CM}$ : au point bas, $\overrightarrow{CM}=-R\,\vec u_y$ ; après une rotation horaire de $\theta$, $\overrightarrow{CM}=R\,(-\sin\theta,\ -\cos\theta)$. Vérifiez qu'à $t=0$ on retrouve $M=O$.


**q2.** - [(d)] Calculer le vecteur vitesse $\vec v$ de $M$ et sa norme (la mettre sous la forme $2V\left|\sin\dfrac{\omega t}{2}\right|$).
- [(e)] Calculer le vecteur accélération $\vec a$ et sa norme. Que remarque-t-on ?
- [(f)] En quels points la vitesse est-elle nulle ? maximale ? Que vaut alors l'accélération ? Commenter.

> [!tip]- 💡 Coup de pouce
> Dérivez chaque coordonnée une fois, puis deux fois. Pour simplifier $\|\vec v\|$, utilisez $1-\cos\theta=2\sin^2(\theta/2)$.


**q3.** - [(g)] Soit $P(t)=(R\omega t,\,0)$ le point du sol qui est, à l'instant $t$, en contact avec la roue. Montrer que $\vec v\perp\overrightarrow{PM}$ et que $\|\vec v\|=\omega\,PM$. Interpréter.
- [(h)] Calculer la longueur $L$ d'une arche de la trajectoire et la comparer à la distance parcourue par le centre pendant le même temps.
- [(i)] Calculer le rayon de courbure $\rho_{\rm top}$ de la trajectoire au sommet.
- [(j)] Un cycliste roule à $V=36~\mathrm{km/h}$ sur des roues de rayon $R=0{,}35$ m. Au sommet de la roue, un grain de boue se détache. En supposant qu'il part avec la vitesse de ce point, où retombe-t-il (par rapport au point de détachement) ?

> [!tip]- 💡 Coup de pouce
> (g) : $\overrightarrow{PM}=R(-\sin\omega t,\ 1-\cos\omega t)$. Calculez le produit scalaire, puis la norme. (h) : $L=\int_0^{2\pi/\omega}\|\vec v\|\,\mathrm dt$. (i) : au sommet, la vitesse est horizontale et l'accélération verticale : $\vec a$ est purement normale, $a=v^2/\rho$. (j) : le grain a la vitesse de $M$ au sommet ($2V$, horizontale) à la hauteur $2R$ : c'est un tir horizontal.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex6-parabole-de-s-rete-et-tir-sur-une-pente|Exercice 6 — Parabole de sûreté et tir sur une pente]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]]

