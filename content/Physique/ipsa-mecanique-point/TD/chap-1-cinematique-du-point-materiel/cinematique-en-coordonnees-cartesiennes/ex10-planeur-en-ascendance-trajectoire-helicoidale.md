---
title: "Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · <a href="/pdfs/td1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 10. Planeur en ascendance : trajectoire hélicoïdale *(facultatif)*

Un planeur spirale dans une ascendance thermique. Dans le référentiel terrestre, supposé galiléen, muni d'un repère cartésien $Oxyz$ avec $Oz$ vertical ascendant, on modélise son mouvement par les équations horaires
$$x(t)=R\cos(\omega t),\qquad y(t)=R\sin(\omega t),\qquad z(t)=z_0+v_z\,t,$$
avec $R=50$ m, $\omega=0{,}20~\mathrm{rad\,s^{-1}}$, $v_z=1{,}5~\mathrm{m\,s^{-1}}$ (taux de montée) et $z_0=600$ m. Le planeur est assimilé à un point matériel $M$. On prendra $g=9{,}81~\mathrm{m\,s^{-2}}$.

**q1.** - [(a)] Déterminer le vecteur vitesse $\vec v$ et sa norme. Que remarque-t-on ?
- [(b)] Déterminer le vecteur accélération $\vec a$ et sa norme. Calculer $\vec v\cdot\vec a$. Que conclut-on sur le mouvement ?
- [(c)] Calculer numériquement $\|\vec v\|$ et $\|\vec a\|$.

> [!tip]- 💡 Coup de pouce
> Dérivez chaque coordonnée : le terme $z_0$ disparaît et $v_z$ est constante. Pour la norme, utilisez $\cos^2+\sin^2=1$. Pour le produit scalaire, développez composante par composante.


**q2.** - [(d)] Déterminer le pas $p$ de l'hélice, l'angle $\gamma$ que fait la vitesse avec l'horizontale, et la longueur d'une spire. Application numérique.
- [(e)] Calculer le rayon de courbure $\rho$ de la trajectoire. Le comparer à $R$ et commenter.
- [(f)] Déterminer l'équation de la projection de la trajectoire dans le plan $Oxz$. De quelle courbe s'agit-il ?

> [!tip]- 💡 Coup de pouce
> Un tour dure $T=2\pi/\omega$ ; le pas est la hauteur gagnée pendant $T$. Pour $\rho$, utilisez $a=v^2/\rho$ car $\vec a\perp\vec v$. Pour (f), éliminez $t$ entre $x(t)$ et $z(t)$ en écrivant $\omega t=\omega(z-z_0)/v_z$.


**q3.** - [(g)] À $t=0$, le planeur est en $M_0=(R,0,z_0)$ et le pilote lâche un objet (sans vitesse relative par rapport au planeur). Déterminer la durée de chute jusqu'au sol ($z=0$) et le point d'impact. On néglige les frottements de l'air.
- [(h)] À quelle distance de l'axe $Oz$ l'objet touche-t-il le sol ? Que vaut la norme de sa vitesse à l'impact ?

> [!tip]- 💡 Coup de pouce
> L'objet quitte $M_0$ avec la vitesse $\vec v(0)=(0,\ R\omega,\ v_z)$, puis il est soumis à la seule pesanteur : $\vec a=-g\,\vec u_z$. Écrivez ses équations horaires, puis résolvez $z=0$. La norme de la vitesse à l'impact se trouve par la conservation de l'énergie mécanique.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex6-parabole-de-s-rete-et-tir-sur-une-pente|Exercice 6 — Parabole de sûreté et tir sur une pente]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex7-balle-rebondissante-et-paradoxe-de-zenon|Exercice 7 — Balle rebondissante et paradoxe de Zénon]]

