---
title: "Exercice 7 — Courbe de poursuite : les trois drones"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td2_PhV111_corrige.pdf) · [📄 Énoncé](/pdfs/td2_PhV111_enonces.pdf) · [📄 Aides](/pdfs/td2_PhV111_aides.pdf) · [📄 Fiche enseignant](/pdfs/td2_PhV111_fiche.pdf)

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


> [!success]- ✅ Correction
> (a) La rotation de $2\pi/3$ autour de $O$ échange les mobiles et conserve la règle de mouvement : la configuration reste invariante, donc équilatérale de centre $O$. (b) L'angle vaut $30^\circ$ : $\dot r=-v\cos30^\circ=-\dfrac{\sqrt3}2v$ et $r\dot\theta=v\sin30^\circ=\dfrac v2$.


> [!example]- 📝 Solution détaillée
> **(a) Argument de symétrie**
>
> La règle « chaque mobile vise le suivant à la vitesse $v$ » est invariante par la rotation de centre $O$ et d'angle $2\pi/3$ qui envoie $A_1\to A_2\to A_3\to A_1$. Comme le mouvement est entièrement déterminé par la configuration initiale et par cette règle, l'état à tout instant est invariant par cette rotation : les trois mobiles restent aux sommets d'un triangle **équilatéral**, de centre $O$ fixe, à la distance $r(t)$ de $O$ et tournant autour de $O$. Il suffit d'étudier $A_1$, en polaire de centre $O$.
>
> **(b) Composantes de la vitesse**
>
> Dans le triangle équilatéral, l'angle en $A_1$ vaut $60^\circ$ et $A_1O$ est la bissectrice : l'angle entre $\overrightarrow{A_1A_2}$ et $\overrightarrow{A_1O}$ vaut $30^\circ$. La vitesse $\vec v$ de $A_1$, de norme $v$, est dirigée selon $\overrightarrow{A_1A_2}$. Sa projection sur $-\vec u_r$ (vers $O$) vaut $v\cos30^\circ$ et sa projection sur $\vec u_\theta$ vaut $v\sin30^\circ$ :
> $$\boxed{\dot r=-\frac{\sqrt3}2\,v},\qquad\boxed{r\dot\theta=\frac v2}.$$


**q2.** (a) Déterminer $r(t)$ et la durée $T$ au bout de laquelle les drones se rencontrent en $O$. Exprimer $T$ en fonction du côté $d$ du triangle initial.

(b) Déterminer $\theta(t)$. Combien de tours effectue chaque drone avant la rencontre ?

(c) Établir l'équation polaire $r(\theta)$ de la trajectoire et la nommer. Calculer la longueur $L$ parcourue par chaque drone.

> [!tip]- 💡 Coup de pouce
> $\dot r$ est constant : intégrez directement. Pour $\theta(t)$, reportez $r(t)$ dans $\dot\theta=\dfrac{v}{2r}$ et intégrez ; attention au comportement de $r\to0$. Pour $r(\theta)$, éliminez $t$ ou calculez $\dfrac{\mathrm dr}{\mathrm d\theta}=\dfrac{\dot r}{\dot\theta}$.


> [!success]- ✅ Correction
> $r=R-\frac{\sqrt3}2vt$ ; $T=\dfrac{2R}{\sqrt3v}=\dfrac{2d}{3v}$ (car $d=R\sqrt3$). $\theta(t)=-\dfrac1{\sqrt3}\ln\left(1-\dfrac tT\right)\to\infty$ : une infinité de tours. $r=R\,\mathrm e^{-\sqrt3\,\theta}$, spirale logarithmique ; $L=vT=\dfrac{2R}{\sqrt3}=\dfrac{2d}3$.


> [!example]- 📝 Solution détaillée
> **(c) Rayon et durée**
>
> $\dot r=-\frac{\sqrt3}2v$ constant et $r(0)=R$ donnent $\boxed{r(t)=R-\frac{\sqrt3}2\,vt}$. La rencontre a lieu quand $r=0$ :
> $$\boxed{T=\frac{2R}{\sqrt3\,v}}.$$
> Le côté du triangle est $d=R\sqrt3$ : $T=\dfrac{2d}{3v}$. Interprétation : si la cible était fixe, il faudrait $d/v$. Ici la cible avance elle aussi, avec une composante $v\cos60^\circ=v/2$ dirigée vers son poursuivant : le côté $d$ du triangle diminue au rythme $v+v/2=\frac32v$, d'où $T=d/(\frac32v)=\frac{2d}{3v}<\frac dv$.
>
> **(d) Angle $\theta(t)$ et nombre de tours**
>
> $\dot\theta=\dfrac v{2r}=\dfrac v{2R\,(1-t/T)}$. Avec $R=\dfrac{\sqrt3}2vT$ : $\dot\theta=\dfrac1{\sqrt3\,T\,(1-t/T)}=\dfrac1{\sqrt3\,(T-t)}$. D'où
> $$\boxed{\theta(t)=-\frac1{\sqrt3}\ln\left(1-\frac tT\right)}.$$
> $\theta\to+\infty$ quand $t\to T^-$ : chaque drone fait une **infinité de tours** avant la rencontre, qui a pourtant lieu en un temps **fini**. Les derniers tours sont parcourus de plus en plus vite ($\dot\theta=v/(2r)\to\infty$).
>
> **(e) Trajectoire et longueur**
>
> $\dfrac{\mathrm dr}{\mathrm d\theta}=\dfrac{\dot r}{\dot\theta}=\dfrac{-\frac{\sqrt3}2v}{v/(2r)}=-\sqrt3\,r$, d'où
> $$\boxed{r(\theta)=R\,\mathrm e^{-\sqrt3\,\theta}}$$
> (vérification : $\theta=-\frac1{\sqrt3}\ln(1-t/T)$ donne $\mathrm e^{-\sqrt3\theta}=1-t/T=r/R$ $\surd$). C'est une **spirale logarithmique** ($k=\sqrt3=\tan60^\circ$). La longueur parcourue est simplement $L=vT=\dfrac{2R}{\sqrt3}=\dfrac{2d}3$, car la vitesse est constante. Comparaison avec l'exercice 6 : même courbe, mais ici $\|\vec v\|=$ cte (et $\dot\theta$ variable), ce qui donne une durée **finie**.


**q3.** (a) Calculer l'accélération $\vec a$ d'un drone dans la base polaire, sa norme et vérifier $\vec a\perp\vec v$. En déduire le rayon de courbure $\rho(r)$.

(b) **Généralisation à $n$ mobiles** (polygone régulier à $n$ côtés). Établir $\dot r$, $r\dot\theta$, $T$, $L$ et $\rho$ en fonction de $n$, $R$ et $v$. Vérifier les cas limites $n=2$ et $n\to\infty$.

(c) Application numérique : trois drones aux sommets d'un triangle équilatéral de côté $d=60$ m, $v=10$ m/s. Calculer $R$, $T$, $L$, le rayon de courbure initial et l'accélération initiale.

> [!tip]- 💡 Coup de pouce
> Dérivez $\dot r=-v\sin(\pi/n)$ et $r\dot\theta=v\cos(\pi/n)$ : $\ddot r=0$, $\dot\theta=\dfrac{v\cos(\pi/n)}r$ puis $\ddot\theta=-\dfrac{v\cos(\pi/n)\,\dot r}{r^2}$. Pour $n$ quelconque, l'angle entre $\vec v$ et $\vec u_r$ vaut $\pi-\left(\dfrac\pi2-\dfrac\pi n\right)$ (vitesse vers $O$).


> [!success]- ✅ Correction
> $\vec a=-\dfrac{v^2\cos(\pi/n)}{r}\left[\cos\dfrac\pi n\,\vec u_r+\sin\dfrac\pi n\,\vec u_\theta\right]$, $\|\vec a\|=\dfrac{v^2\cos(\pi/n)}r$, $\rho=\dfrac r{\cos(\pi/n)}$ ($=2r$ pour $n=3$). $T=\dfrac R{v\sin(\pi/n)}$, $L=\dfrac R{\sin(\pi/n)}$. AN : $R\approx34{,}6$ m, $T=4{,}0$ s, $L=40$ m, $\rho_0\approx69$ m, $a_0\approx1{,}4\ \mathrm{m\,s^{-2}}$.


> [!example]- 📝 Solution détaillée
> **(f) Accélération pour $n=3$**
>
> Avec $\dot r=-\frac{\sqrt3}2v$ ($\ddot r=0$) et $r\dot\theta=\frac v2$ : $\dot\theta=\dfrac v{2r}$ et $\ddot\theta=-\dfrac v{2r^2}\dot r=\dfrac{\sqrt3v^2}{4r^2}$.
> $$a_r=-r\dot\theta^2=-\frac{v^2}{4r},\qquad a_\theta=r\ddot\theta+2\dot r\dot\theta=\frac{\sqrt3v^2}{4r}-\frac{\sqrt3v^2}{2r}=-\frac{\sqrt3v^2}{4r}.$$
> $$\boxed{\vec a=-\frac{v^2}{4r}\left(\vec u_r+\sqrt3\,\vec u_\theta\right)},\qquad\|\vec a\|=\boxed{\frac{v^2}{2r}}.$$
> Avec $\vec v=v\left(-\frac{\sqrt3}2\vec u_r+\frac12\vec u_\theta\right)$ : $\vec a\cdot\vec v=-\frac{v^3}{4r}\left(-\frac{\sqrt3}2+\frac{\sqrt3}2\right)=0$ $\surd$ ($\|\vec v\|=$ cte). Comme $\vec a\perp\vec v$, $\rho=\dfrac{v^2}{\|\vec a\|}=\boxed{2r}$.
>
> **(g) Généralisation à $n$ mobiles**
>
> L'angle entre le côté et le rayon vaut $\dfrac\pi2-\dfrac\pi n$. Donc
> $$\boxed{\dot r=-v\sin\frac\pi n},\qquad\boxed{r\dot\theta=v\cos\frac\pi n}\qquad(n=3:\ \sin60^\circ=\tfrac{\sqrt3}2,\ \cos60^\circ=\tfrac12\ ~\surd).$$
> Alors $r=R-v\sin\frac\pi n\,t$, $\boxed{T=\dfrac R{v\sin(\pi/n)}}$, $\dfrac{\mathrm dr}{\mathrm d\theta}=-r\tan\dfrac\pi n$ soit $\boxed{r=R\,\mathrm e^{-\theta\tan(\pi/n)}}$ et $\boxed{L=vT=\dfrac R{\sin(\pi/n)}}$. En reprenant le calcul de (f) : $a_r=-\dfrac{v^2\cos^2(\pi/n)}r$, $a_\theta=-\dfrac{v^2\sin(\pi/n)\cos(\pi/n)}r$, donc
> $$\|\vec a\|=\frac{v^2\cos(\pi/n)}r,\qquad\rho=\frac r{\cos(\pi/n)}.$$
> **Cas limites.** $n=2$ : $\cos\frac\pi2=0$, $\vec a=\vec0$, $\rho=\infty$, $r=R-vt$, $T=R/v$ : deux mobiles qui se visent vont en ligne droite l'un vers l'autre $\surd$. $n\to\infty$ : $\sin\frac\pi n\to0$, $T\to\infty$, $r\to R$, $\rho\to r$ : on retrouve le mouvement circulaire uniforme de rayon $R$ (chaque mobile vise quasiment son voisin tangent) $\surd$.
>
> **(h) Application numérique**
>
> $R=\dfrac d{\sqrt3}\approx34{,}6$ m. $T=\dfrac{2R}{\sqrt3v}=\dfrac{2d}{3v}=4{,}0$ s. $L=vT=40$ m (à comparer avec la distance $R=34{,}6$ m : seulement $16\,\%$ de plus). $\rho_0=2R\approx69$ m et $a_0=\dfrac{v^2}{2R}=\dfrac{100}{69}\approx1{,}4\ \mathrm{m\,s^{-2}}$ (environ $0{,}15\,g$) en début de mouvement. En fin de mouvement, $a\propto1/r\to\infty$ : le modèle perd son sens quand les drones sont à quelques mètres l'un de l'autre (limite physique d'accélération des drones, collision). **Validation** : les unités sont cohérentes ($\mathrm{m^2\,s^{-2}/m}=\mathrm{m\,s^{-2}}$).


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]]

