---
title: "Exercice 8 — Ellipse de Kepler, loi des aires et hodographe"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · <a href="/pdfs/td2_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 8. Ellipse de Kepler, loi des aires et hodographe *(facultatif)*

Une planète $M$ décrit, autour du Soleil placé en $O$ (foyer de l'orbite), une ellipse d'équation polaire
$$r(\theta)=\frac p{1+e\cos\theta},\qquad0\le e<1,$$
où $p$ (le **paramètre**) et $e$ (l'**excentricité**) sont des constantes. Le mouvement est tel que la quantité
$$C=r^2\dot\theta$$
(la **constante des aires**) est conservée. On se place dans la base polaire $(\vec u_r,\vec u_\theta)$ et on note
$\vec u_y$ le vecteur fixe de l'axe $Oy$ (perpendiculaire à l'axe focal $Ox$). Le but est de déterminer toute la
cinématique de ce mouvement **sans aucune hypothèse sur les forces** : on retrouvera la loi de la force.

**q1.** (a) Montrer que $a_\theta=\dfrac1r\dfrac{\mathrm d}{\mathrm dt}(r^2\dot\theta)$. En déduire que la loi des aires $r^2\dot\theta=C$ est équivalente au fait que l'accélération est **radiale** (dirigée selon $\vec u_r$).

(b) Exprimer la vitesse aréolaire $\dfrac{\mathrm dA}{\mathrm dt}$ en fonction de $C$.

> [!tip]- 💡 Coup de pouce
> Développez $\dfrac{\mathrm d}{\mathrm dt}(r^2\dot\theta)=2r\dot r\dot\theta+r^2\ddot\theta$ et comparez avec $r\,a_\theta=r^2\ddot\theta+2r\dot r\dot\theta$. L'aire élémentaire balayée est le secteur de rayon $r$ et d'angle $\mathrm d\theta$.


**q2.** (a) Pour l'ellipse $r=\dfrac p{1+e\cos\theta}$ avec $r^2\dot\theta=C$, calculer $\dot r$ et $r\dot\theta$ en fonction de $C$, $p$, $e$ et $\theta$.

(b) En déduire que $\vec v=\dfrac Cp\left(\vec u_\theta+e\,\vec u_y\right)$ et calculer $\|\vec v\|^2$.

(c) Montrer que l'hodographe est un cercle dont on précisera le centre et le rayon.

> [!tip]- 💡 Coup de pouce
> $\dot r=\dfrac{\mathrm dr}{\mathrm d\theta}\dot\theta=\dfrac{r^2}pe\sin\theta\cdot\dfrac C{r^2}$. Pour (d), écrivez $e\sin\theta\,\vec u_r+e\cos\theta\,\vec u_\theta$ avec $\vec u_y=\sin\theta\,\vec u_r+\cos\theta\,\vec u_\theta$. Pour (e), repérez les composantes cartésiennes de $\vec v$ avec $\vec u_\theta=(-\sin\theta,\cos\theta)$.


**q3.** (a) Calculer $\vec a=\dfrac{\mathrm d\vec v}{\mathrm dt}$ à partir de l'expression (d). Quelle est la loi de variation de $\|\vec a\|$ avec $r$ ? Dans quel sens la force s'exerce-t-elle ?

(b) Déterminer la vitesse aux deux apsides (périhélie $\theta=0$, aphélie $\theta=\pi$) et le rapport $v_{\max}/v_{\min}$. Vérifier avec la loi des aires.

(c) Application : pour la Terre, $e=0{,}0167$ et la vitesse orbitale moyenne vaut $29{,}8$ km/s. Estimer les vitesses au périhélie et à l'aphélie. (On pourra utiliser $v_{\max}v_{\min}=\left(\dfrac Cp\right)^2(1-e^2)$ et assimiler $\sqrt{v_{\max}v_{\min}}$ à la vitesse moyenne.)

> [!tip]- 💡 Coup de pouce
> $\vec u_y$ est fixe : seul $\vec u_\theta$ varie dans $\vec v$. Pour (g), $\cos\theta=\pm1$. Pour (h), $v_{\max}v_{\min}=\left(\dfrac Cp\right)^2(1+e)(1-e)$, puis résolvez avec $v_{\max}/v_{\min}=\dfrac{1+e}{1-e}$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]]

