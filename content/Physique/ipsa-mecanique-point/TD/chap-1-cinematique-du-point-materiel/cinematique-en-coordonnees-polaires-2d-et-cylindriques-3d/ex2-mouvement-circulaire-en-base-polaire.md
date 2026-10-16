---
title: "Exercice 2 — Mouvement circulaire en base polaire"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · <a href="/pdfs/td2_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 2. Mouvement circulaire en base polaire

Dans le plan $Oxy$, on considère le déplacement d'un mobile assimilé à un point $M$. L'évolution de son
vecteur position dans la base polaire $(\vec u_r,\vec u_\theta)$ s'écrit
$$\overrightarrow{OM}(t)=R\,\vec u_r\qquad\text{avec } R \text{ constant},$$
et l'évolution de l'angle $\theta$ est donnée par $\theta(t)=\omega t$ avec $\omega$ constant.

**q1.** Trajectoire et base polaire.


(a) Donner la dimension des constantes $R$ et $\omega$.

(b) Quelle est la trajectoire décrite par le mobile $M$ ?

(c) Représenter graphiquement la trajectoire de $M$, en prenant $R=4\times10^{-2}$ S.I. et $\omega=\pi/6$ S.I.

(d) Calculer les coordonnées polaires $(r,\theta)$ de $M$ à $t_0=0$ s, $t_1=1$ s, $t_2=2$ s, $t_3=3$ s.

(e) Représenter ces points sur le graphique, ainsi que la base polaire associée $(\vec u_r,\vec u_\theta)$.

> [!tip]- 💡 Coup de pouce
> $\overrightarrow{OM}=R\,\vec u_r$ : que dire de la distance $OM$ ? Pour (e), $\vec u_r$ pointe de $O$ vers $M$ et $\vec u_\theta$ est $\vec u_r$ tourné de $+90^\circ$.


**q2.** Vitesse et accélération de $M$ en base polaire.


(a) Déterminer l'expression du vecteur vitesse $\vec v$ de $M$ dans la base polaire $(\vec u_r,\vec u_\theta)$. En déduire sa norme $\|\vec v\|$.

(b) Déterminer l'expression du vecteur accélération $\vec a$ de $M$ dans la base polaire. En déduire sa norme $\|\vec a\|$.

(c) Représenter sur le graphique la vitesse $\vec v$ et l'accélération $\vec a$ de $M$ à différents instants $t$ (choisir une échelle adéquate pour la vitesse et pour l'accélération).

(d) En un point de la trajectoire, représenter la base polaire $(\vec u_r,\vec u_\theta)$ et faire apparaître les composantes des vecteurs vitesse $\vec v$ et accélération $\vec a$.

> [!tip]- 💡 Coup de pouce
> Dérivez $R\,\vec u_r$ par rapport au temps. $R$ est constant, mais $\vec u_r$ ne l'est pas : utilisez $\dfrac{\mathrm d\vec u_r}{\mathrm dt}=\dot\theta\,\vec u_\theta$, puis recommencez avec $\vec u_\theta$.


**q3.** Retour sur le mouvement circulaire en base cartésienne. Comparer vos résultats à ceux obtenus dans le TD1 sur le mouvement circulaire.


(a) Le mouvement de $M$ dépend-il du repère choisi ?

(b) Les composantes des vecteurs vitesse et accélération dépendent-elles de la base choisie ?

(c) Le tracé des vecteurs vitesse et accélération dépend-il de la base choisie ?

(d) La norme des vecteurs vitesse et accélération dépend-elle de la base choisie ?

> [!tip]- 💡 Coup de pouce
> Exprimez $\vec u_\theta$ et $\vec u_r$ dans la base cartésienne et comparez avec $\vec v=-R\omega\sin(\omega t)\,\vec\imath+R\omega\cos(\omega t)\,\vec\jmath$ trouvé au TD1.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]]

