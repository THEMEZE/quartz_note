---
title: "Exercice 12 — (*) Équations horaires 2D ou 3D"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · <a href="/pdfs/td1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 12. (*) Équations horaires 2D ou 3D *(facultatif)*

Un mobile assimilé à un point matériel $M$ est en mouvement dans un référentiel galiléen $\mathcal R$
d'origine $O$ et muni d'un repère cartésien $(Oxyz)$. Il est repéré par ses coordonnées cartésiennes
suivantes, dans six cas indépendants ($a,b,c$ désignant des constantes) :
$$
\begin{array}{llll}
1)\ \begin{cases}x=5t\\y=2\\z=15t\end{cases} &
2)\ \begin{cases}x=2\\y=0\\z=4t^2-8t\end{cases} &
3)\ \begin{cases}x=3\cos(10t)\\y=3\sin(10t)\\z=2\end{cases} \\[2em]
4)\ \begin{cases}x=at^2-bt+c\\y=2c\\z=0\end{cases} &
5)\ \begin{cases}x=3\cos(2t^2)\\y=3\sin(2t^2)\\z=0\end{cases} &
6)\ \begin{cases}x=2t\cos(4t)\\y=2t\sin(4t)\\z=0\end{cases}
\end{array}
$$
Déterminer, pour chaque cas, le vecteur position, le vecteur vitesse et le vecteur accélération du point $M$,
ainsi que leur norme, et caractériser le mouvement obtenu.

**q1.** Cas 1 : $x(t) = 5t$, $y(t)=2$, $z(t)=15t$ (unités SI). Déterminer $\overrightarrow{OM}(t)$, $\vec v(t)$, $\vec a(t)$ et leurs normes ; caractériser le mouvement.

> [!tip]- 💡 Coup de pouce
> Toutes les coordonnées sont des fonctions affines de $t$ : quel type de mouvement cela évoque-t-il ?


**q2.** Cas 2 : $x(t)=2$, $y(t)=0$, $z(t)=4t^2-8t$ (unités SI). Déterminer $\overrightarrow{OM}(t)$, $\vec v(t)$, $\vec a(t)$ et leurs normes ; caractériser le mouvement.

> [!tip]- 💡 Coup de pouce
> Seule la coordonnée $z$ varie, et de façon quadratique : quel est le mouvement le long de $Oz$ ?


**q3.** Cas 3 : $x(t)=3\cos(10t)$, $y(t)=3\sin(10t)$, $z(t)=2$ (unités SI). Déterminer $\overrightarrow{OM}(t)$, $\vec v(t)$, $\vec a(t)$ et leurs normes ; caractériser le mouvement.

> [!tip]- 💡 Coup de pouce
> C'est le mouvement circulaire de l'exercice 3, mais décalé le long de $Oz$.


**q4.** Cas 4 : $x(t)=at^2-bt+c$, $y(t)=2c$, $z(t)=0$ ($a,b,c$ constantes). Déterminer $\overrightarrow{OM}(t)$, $\vec v(t)$, $\vec a(t)$ et leurs normes ; caractériser le mouvement.

> [!tip]- 💡 Coup de pouce
> Comparez à l'exercice 1, question 1 : ici c'est $Ox$ qui joue le rôle de l'axe du mouvement quadratique.


**q5.** Cas 5 : $x(t)=3\cos(2t^2)$, $y(t)=3\sin(2t^2)$, $z(t)=0$ (unités SI). Déterminer $\overrightarrow{OM}(t)$, $\vec v(t)$, $\vec a(t)$ et leurs normes ; caractériser le mouvement.

> [!tip]- 💡 Coup de pouce
> Posez $\\theta(t)=2t^2$ : la trajectoire est-elle circulaire ? La vitesse angulaire $\dot\theta$ est-elle constante ?


**q6.** Cas 6 : $x(t)=2t\cos(4t)$, $y(t)=2t\sin(4t)$, $z(t)=0$ (unités SI). Déterminer $\overrightarrow{OM}(t)$, $\vec v(t)$, $\vec a(t)$ et leurs normes ; caractériser le mouvement.

> [!tip]- 💡 Coup de pouce
> Ici $r(t)=\|\overrightarrow{OM}\|=2t$ n'est plus constant : ce n'est plus un cercle. Identifiez $r(t)$ et $\theta(t)$ pour interpréter le mouvement.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]]

