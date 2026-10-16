---
title: "Exercice 5 — Perle sur une tige tournante"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · <a href="/pdfs/td2_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 5. Perle sur une tige tournante *(facultatif)*

Dans un plan horizontal, une tige rectiligne $OA$ tourne autour de $O$ à vitesse angulaire **constante**
$\omega$ : l'angle $\theta$ entre $Ox$ et la tige vaut $\theta(t)=\omega t$. Une petite perle $M$ coulisse sur la
tige ; sa position est repérée par $r(t)=OM$. On étudie deux mouvements de la perle sur la tige :


- **cas A** : la perle est entraînée à vitesse radiale constante $u$ à partir de $O$, soit $r(t)=ut$ ;
- **cas B** : la perle est **libre** sur une tige lisse : la tige ne peut exercer sur elle qu'une action perpendiculaire à la tige, donc l'accélération n'a **aucune composante radiale**, $a_r=0$. La perle est lâchée à $r(0)=r_0$ avec $\dot r(0)=0$.

**q1.** **Cas A : $r(t)=ut$, $\theta(t)=\omega t$.**


(a) Déterminer l'équation polaire $r(\theta)$ de la trajectoire et la nommer. Quel est l'écart radial entre deux tours successifs ?

(b) Calculer $\vec v$ et $\vec a$ dans la base polaire, puis leurs normes. Identifier dans $\vec a$ le terme centripète et le terme de Coriolis.

> [!tip]- 💡 Coup de pouce
> Éliminez $t=\theta/\omega$ dans $r=ut$. Pour $\vec a$, utilisez $a_r=\ddot r-r\dot\theta^2$ et $a_\theta=r\ddot\theta+2\dot r\dot\theta$ avec $\ddot r=0$ et $\ddot\theta=0$.


**q2.** (a) Calculer l'angle $\beta$ entre $\vec v$ et la tige. Que devient-il quand $t\to\infty$ ?

(b) Calculer le rayon de courbure $\rho(t)$ de la trajectoire. Donner sa valeur en $t=0$ et son comportement aux temps longs. Commenter.

> [!tip]- 💡 Coup de pouce
> $\tan\beta=r\dot\theta/\dot r$. Pour $\rho$, calculez $v_ra_\theta-v_\theta a_r$ avec les composantes de la question (b).


**q3.** **Cas B : perle libre, $a_r=0$, $r(0)=r_0$, $\dot r(0)=0$.**


(a) Montrer que la condition $a_r=0$ conduit à $\ddot r=\omega^2r$ et en déduire $r(t)$.

(b) Déterminer $\vec v$ et $\vec a$ et calculer $\|\vec v\|$. Vérifier que $\vec a\ne\vec0$.

(c) Donner l'équation polaire $r(\theta)$ de la trajectoire et la limite de l'angle $\beta$ entre $\vec v$ et la tige quand $t\to\infty$.

(d) Application numérique : $r_0=10$ cm, tige de longueur $1{,}00$ m tournant à $1$ tour par seconde. À quel instant la perle quitte-t-elle la tige ? Avec quelle vitesse ?

> [!tip]- 💡 Coup de pouce
> $a_r=\ddot r-r\omega^2$ car $\dot\theta=\omega$. L'équation $\ddot r=\omega^2r$ a pour solutions $\cosh\omega t$ et $\sinh\omega t$ : lesquelles vérifient $\dot r(0)=0$ ?


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]]

