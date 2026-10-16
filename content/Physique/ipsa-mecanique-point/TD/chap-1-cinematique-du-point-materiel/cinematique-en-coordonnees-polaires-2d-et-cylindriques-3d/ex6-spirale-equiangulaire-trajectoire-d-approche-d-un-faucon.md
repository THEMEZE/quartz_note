---
title: "Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · <a href="/pdfs/td2_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 6. Spirale équiangulaire (trajectoire d'approche d'un faucon) *(facultatif)*

Un faucon vole dans un plan horizontal vers sa proie, immobile en $O$. Il garde la proie dans une direction
qui fait un **angle constant** avec sa vitesse. En coordonnées polaires centrées en $O$, sa trajectoire a pour
équation
$$r(\theta)=r_0\,\mathrm e^{-k\theta},\qquad k>0\ \text{constante},$$
(spirale **logarithmique** ou **équiangulaire**) et il la parcourt avec une vitesse angulaire constante
$\dot\theta=\omega>0$, $\theta(0)=0$.

**q1.** (a) Déterminer $\theta(t)$ puis $r(t)$.

(b) Calculer le vecteur vitesse $\vec v$ dans la base polaire et sa norme. Montrer que l'angle $\gamma$ entre $\vec v$ et la direction de la proie $-\vec u_r$ est constant et exprimer $\tan\gamma$ en fonction de $k$.

> [!tip]- 💡 Coup de pouce
> Intégrez $\dot\theta=\omega$. Pour la vitesse, dérivez $r(t)$. L'angle entre $\vec v$ et $-\vec u_r$ se lit sur les composantes de $\vec v$ : $\tan\gamma=|v_\theta|/|v_r|$.


**q2.** (a) Calculer l'accélération $\vec a$ et sa norme. Pour quelle valeur de $k$ l'accélération est-elle purement orthoradiale ? Que devient-elle pour $k\to0$ ?

(b) Calculer l'accélération tangentielle $a_t=\dfrac{\mathrm dv}{\mathrm dt}$, l'accélération normale $a_n$ et le rayon de courbure $\rho$. Vérifier le cas $k\to0$.

> [!tip]- 💡 Coup de pouce
> $\ddot r=k^2\omega^2r$. Pour $a_n$, utilisez $a_n^2=a^2-a_t^2$.


**q3.** (a) Combien de temps le faucon met-il pour atteindre $O$ ? Combien de tours fait-il ? Calculer la longueur totale $L$ de la trajectoire de $\theta=0$ à $+\infty$ et l'exprimer en fonction de $r_0$ et de l'angle $\gamma$.

(b) Application numérique : $r_0=100$ m, $\gamma=40^\circ$, $\omega=0{,}5$ rad/s. Calculer $k$, $L$, la vitesse initiale, et le rapport $L/r_0$. Commenter.

> [!tip]- 💡 Coup de pouce
> $r\to0$ seulement si $t\to\infty$. Pour $L$, intégrez $\|\vec v\|=\omega r_0\sqrt{1+k^2}\,\mathrm e^{-k\omega t}$ de $0$ à $\infty$. Utilisez $\cos\gamma=k/\sqrt{1+k^2}$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]]

