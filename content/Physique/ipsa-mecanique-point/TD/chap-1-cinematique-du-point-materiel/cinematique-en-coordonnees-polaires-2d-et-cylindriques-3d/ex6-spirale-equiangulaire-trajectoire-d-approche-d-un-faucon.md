---
title: "Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td2_PhV111_corrige.pdf) · [📄 Énoncé](/pdfs/td2_PhV111_enonces.pdf) · [📄 Aides](/pdfs/td2_PhV111_aides.pdf) · [📄 Fiche enseignant](/pdfs/td2_PhV111_fiche.pdf)

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


> [!success]- ✅ Correction
> $\theta=\omega t$, $r=r_0\mathrm e^{-k\omega t}$. $\vec v=\omega r(-k\,\vec u_r+\vec u_\theta)$, $\|\vec v\|=\omega r\sqrt{1+k^2}$, $\tan\gamma=1/k$ : constant.


> [!example]- 📝 Solution détaillée
> **(a) Équations horaires**
>
> $\theta(t)=\omega t$ et $\boxed{r(t)=r_0\,\mathrm e^{-k\omega t}}$. Le rayon décroît exponentiellement, avec la constante de temps $1/(k\omega)$, et $r\to0$ seulement quand $t\to\infty$.
>
> **(b) Vitesse et angle constant**
>
> $\dot r=-k\omega r$ et $r\dot\theta=\omega r$ :
> $$\boxed{\vec v=\omega r\left(-k\,\vec u_r+\vec u_\theta\right)},\qquad\|\vec v\|=\boxed{\omega r\sqrt{1+k^2}}.$$
> La composante vers la proie est $|v_r|=k\omega r$ et la composante orthoradiale est $\omega r$ : $\tan\gamma=\dfrac{v_\theta}{|v_r|}=\boxed{\dfrac1k}$, soit $\cos\gamma=\dfrac k{\sqrt{1+k^2}}$. L'angle ne dépend ni de $t$ ni de $r$ : le faucon voit la proie sous un **angle constant**.


**q2.** (a) Calculer l'accélération $\vec a$ et sa norme. Pour quelle valeur de $k$ l'accélération est-elle purement orthoradiale ? Que devient-elle pour $k\to0$ ?

(b) Calculer l'accélération tangentielle $a_t=\dfrac{\mathrm dv}{\mathrm dt}$, l'accélération normale $a_n$ et le rayon de courbure $\rho$. Vérifier le cas $k\to0$.

> [!tip]- 💡 Coup de pouce
> $\ddot r=k^2\omega^2r$. Pour $a_n$, utilisez $a_n^2=a^2-a_t^2$.


> [!success]- ✅ Correction
> $\vec a=\omega^2r\left[(k^2-1)\,\vec u_r-2k\,\vec u_\theta\right]$, $\|\vec a\|=\omega^2r(1+k^2)$ ; $k=1$ : orthoradiale ; $a_t=-k\omega^2r\sqrt{1+k^2}$, $a_n=\omega^2r\sqrt{1+k^2}$, $\rho=r\sqrt{1+k^2}$.


> [!example]- 📝 Solution détaillée
> **(c) Accélération**
>
> $a_r=\ddot r-r\dot\theta^2=(k^2-1)\,\omega^2r$ et $a_\theta=2\dot r\dot\theta=-2k\omega^2r$ :
> $$\boxed{\vec a=\omega^2r\left[(k^2-1)\,\vec u_r-2k\,\vec u_\theta\right]},\qquad\|\vec a\|=\omega^2r\sqrt{(k^2-1)^2+4k^2}=\boxed{\omega^2r\,(1+k^2)}.$$
> Pour $k=1$ : $a_r=0$, l'accélération est **orthoradiale**. Pour $k\to0$ : $\vec a\to-\omega^2r\,\vec u_r$, l'accélération centripète du cercle.
>
> **(d) Composantes tangentielle et normale**
>
> $v=\omega\sqrt{1+k^2}\,r$ et $\dot r=-k\omega r$ donnent
> $$a_t=\frac{\mathrm dv}{\mathrm dt}=\boxed{-k\omega^2r\sqrt{1+k^2}}\quad(\text{le faucon ralentit}).$$
> $a_n^2=a^2-a_t^2=\omega^4r^2(1+k^2)\left[(1+k^2)-k^2\right]=\omega^4r^2(1+k^2)$, soit $a_n=\omega^2r\sqrt{1+k^2}$ et
> $$\rho=\frac{v^2}{a_n}=\boxed{r\sqrt{1+k^2}}.$$
> Pour $k\to0$ : $\rho\to r$ (cercle de rayon $r$), $a_t\to0$ (vitesse constante) : on retrouve le mouvement circulaire uniforme.


**q3.** (a) Combien de temps le faucon met-il pour atteindre $O$ ? Combien de tours fait-il ? Calculer la longueur totale $L$ de la trajectoire de $\theta=0$ à $+\infty$ et l'exprimer en fonction de $r_0$ et de l'angle $\gamma$.

(b) Application numérique : $r_0=100$ m, $\gamma=40^\circ$, $\omega=0{,}5$ rad/s. Calculer $k$, $L$, la vitesse initiale, et le rapport $L/r_0$. Commenter.

> [!tip]- 💡 Coup de pouce
> $r\to0$ seulement si $t\to\infty$. Pour $L$, intégrez $\|\vec v\|=\omega r_0\sqrt{1+k^2}\,\mathrm e^{-k\omega t}$ de $0$ à $\infty$. Utilisez $\cos\gamma=k/\sqrt{1+k^2}$.


> [!success]- ✅ Correction
> Durée infinie, nombre de tours infini ; $L=\dfrac{r_0\sqrt{1+k^2}}k=\dfrac{r_0}{\cos\gamma}$. AN : $k\approx1{,}19$, $L\approx131$ m, $v_0\approx78$ m/s, $L/r_0\approx1{,}31$.


> [!example]- 📝 Solution détaillée
> **(e) Durée, nombre de tours et longueur**
>
> $r(t)=r_0\mathrm e^{-k\omega t}$ ne s'annule jamais : le faucon n'atteint $O$ qu'au bout d'un temps **infini**, après un nombre **infini** de tours ($\theta=\omega t\to\infty$). Pourtant
> $$L=\int_0^\infty\omega r_0\sqrt{1+k^2}\,\mathrm e^{-k\omega t}\,\mathrm dt=\frac{r_0\sqrt{1+k^2}}{k}=\boxed{\frac{r_0}{\cos\gamma}}.$$
> $L$ est **finie**. En dessous, $L\geq r_0$ (distance en ligne droite), avec égalité pour $\gamma=0$ (approche droite, $k\to\infty$). Résultat remarquable : plus l'angle d'approche $\gamma$ est grand, plus le trajet est long, mais rien ne diverge tant que $\gamma<90^\circ$ ($k>0$).
>
> **(f) Application numérique**
>
> $k=\dfrac1{\tan\gamma}=\dfrac1{\tan40^\circ}\approx1{,}19$. $L=\dfrac{100}{\cos40^\circ}\approx131$ m, soit $L/r_0\approx1{,}31$ : le trajet en spirale n'est que $31\,\%$ plus long que la ligne droite, alors que le faucon fait une infinité de tours. La vitesse initiale vaut $v_0=\omega r_0\sqrt{1+k^2}\approx0{,}5\times100\times1{,}55\approx78$ m/s : ordre de grandeur réaliste pour un piqué de faucon pèlerin ($\sim80$ m/s). Le faucon ralentit ensuite exponentiellement ($v\propto r$) : le modèle n'est valable que jusqu'à une distance minimale de la proie, où commence la capture.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]]

