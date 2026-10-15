---
title: "Exercice 2 — Mouvement circulaire en base polaire"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td2_PhV111_corrige.pdf) · [📄 Énoncé](/pdfs/td2_PhV111_enonces.pdf) · [📄 Aides](/pdfs/td2_PhV111_aides.pdf) · [📄 Fiche enseignant](/pdfs/td2_PhV111_fiche.pdf)

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


> [!success]- ✅ Correction
> $[R]=\mathrm L$, $[\omega]=\mathrm T^{-1}$ ; cercle de centre $O$ et de rayon $R$ ; points $(0{,}04\ \mathrm m;\ 0,\ \pi/6,\ \pi/3,\ \pi/2)$.


> [!example]- 📝 Solution détaillée
> **(a) Dimensions**
>
> $R$ est la norme de $\overrightarrow{OM}$ : une longueur, $[R]=\mathrm L$. L'argument $\omega t$ est un angle (sans dimension), donc $[\omega]=\mathrm T^{-1}$ (vitesse angulaire, en rad/s).
>
> **(b) Trajectoire**
>
> $OM=\|R\,\vec u_r\|=R$ est constant : $M$ décrit le **cercle de centre $O$ et de rayon $R$**. L'angle $\theta=\omega t$ varie linéairement : le mouvement est circulaire **uniforme**, dans le sens trigonométrique si $\omega>0$.
>
> **(c)-(e) Tracé, coordonnées polaires et base**
>
> Avec $R=0{,}04$ m et $\omega=\pi/6$ rad/s (période $T=2\pi/\omega=12$ s) :
> $$
> \begin{array}{c|cccc}
> t~(\mathrm s) & 0 & 1 & 2 & 3\\
> \hline
> r~(\mathrm m) & 0{,}04 & 0{,}04 & 0{,}04 & 0{,}04\\
> \theta & 0 & \pi/6\ (30^\circ) & \pi/3\ (60^\circ) & \pi/2\ (90^\circ)
> \end{array}
> $$
> Pour placer les points on peut passer en cartésien : $(0{,}04;\,0)$, $(0{,}035;\,0{,}020)$, $(0{,}020;\,0{,}035)$, $(0;\,0{,}04)$ (en mètres). En chaque point, on trace $\vec u_r$ (radial, de $O$ vers $M$) et $\vec u_\theta$ (tangent, obtenu en tournant $\vec u_r$ de $+90^\circ$) : cette base **change d'orientation** d'un point à l'autre, contrairement à la base cartésienne.


**q2.** Vitesse et accélération de $M$ en base polaire.


(a) Déterminer l'expression du vecteur vitesse $\vec v$ de $M$ dans la base polaire $(\vec u_r,\vec u_\theta)$. En déduire sa norme $\|\vec v\|$.

(b) Déterminer l'expression du vecteur accélération $\vec a$ de $M$ dans la base polaire. En déduire sa norme $\|\vec a\|$.

(c) Représenter sur le graphique la vitesse $\vec v$ et l'accélération $\vec a$ de $M$ à différents instants $t$ (choisir une échelle adéquate pour la vitesse et pour l'accélération).

(d) En un point de la trajectoire, représenter la base polaire $(\vec u_r,\vec u_\theta)$ et faire apparaître les composantes des vecteurs vitesse $\vec v$ et accélération $\vec a$.

> [!tip]- 💡 Coup de pouce
> Dérivez $R\,\vec u_r$ par rapport au temps. $R$ est constant, mais $\vec u_r$ ne l'est pas : utilisez $\dfrac{\mathrm d\vec u_r}{\mathrm dt}=\dot\theta\,\vec u_\theta$, puis recommencez avec $\vec u_\theta$.


> [!success]- ✅ Correction
> $\vec v=R\omega\,\vec u_\theta$, $\|\vec v\|=R\omega\approx2{,}1\times10^{-2}$ m/s ; $\vec a=-R\omega^2\,\vec u_r$, $\|\vec a\|=R\omega^2\approx1{,}1\times10^{-2}$ m/s$^2$.


> [!example]- 📝 Solution détaillée
> **(a) Vecteur vitesse**
>
> $$\vec v=\frac{\mathrm d\overrightarrow{OM}}{\mathrm dt}=R\,\frac{\mathrm d\vec u_r}{\mathrm dt}=R\dot\theta\,\vec u_\theta=\boxed{R\omega\,\vec u_\theta}.$$
> $\vec v$ est **tangent** au cercle, dans le sens des $\theta$ croissants. La base $(\vec u_r,\vec u_\theta)$ étant orthonormée :
> $$\|\vec v\|=\boxed{R\omega}=0{,}04\times\frac\pi6\approx2{,}1\times10^{-2}~\mathrm{m/s}.$$
>
> **(b) Vecteur accélération**
>
> $$\vec a=\frac{\mathrm d\vec v}{\mathrm dt}=R\omega\,\frac{\mathrm d\vec u_\theta}{\mathrm dt}=R\omega\,(-\dot\theta\,\vec u_r)=\boxed{-R\omega^2\,\vec u_r}.$$
> $$\|\vec a\|=\boxed{R\omega^2}=0{,}04\times\left(\frac\pi6\right)^2\approx1{,}1\times10^{-2}~\mathrm{m/s^2}.$$
> L'accélération est **radiale et centripète** : elle pointe vers $O$. On vérifie que $\vec v\cdot\vec a=0$ et que $\|\vec a\|=v^2/R$.
>
> **(c)-(d) Représentation**
>
> En chaque point, $\vec v$ est tracé tangent au cercle (suivant $\vec u_\theta$), de longueur constante, et $\vec a$ est tracé vers le centre (suivant $-\vec u_r$), de longueur constante aussi. Avec une échelle, par exemple, de $1$ cm pour $0{,}01$ m/s pour $\vec v$ et de $1$ cm pour $0{,}005$ m/s$^2$ pour $\vec a$, on obtient une flèche d'environ $2$ cm pour $\vec v$ et $2$ cm pour $\vec a$. Les composantes sont directement lisibles : $v_r=0$, $v_\theta=R\omega$ ; $a_r=-R\omega^2$, $a_\theta=0$.


**q3.** Retour sur le mouvement circulaire en base cartésienne. Comparer vos résultats à ceux obtenus dans le TD1 sur le mouvement circulaire.


(a) Le mouvement de $M$ dépend-il du repère choisi ?

(b) Les composantes des vecteurs vitesse et accélération dépendent-elles de la base choisie ?

(c) Le tracé des vecteurs vitesse et accélération dépend-il de la base choisie ?

(d) La norme des vecteurs vitesse et accélération dépend-elle de la base choisie ?

> [!tip]- 💡 Coup de pouce
> Exprimez $\vec u_\theta$ et $\vec u_r$ dans la base cartésienne et comparez avec $\vec v=-R\omega\sin(\omega t)\,\vec\imath+R\omega\cos(\omega t)\,\vec\jmath$ trouvé au TD1.


> [!success]- ✅ Correction
> (a) Non. (b) Oui. (c) Non. (d) Non.


> [!example]- 📝 Solution détaillée
> **Vérification du lien entre les deux écritures**
>
> Comme $\vec u_\theta=-\sin\theta\,\vec\imath+\cos\theta\,\vec\jmath$ et $\vec u_r=\cos\theta\,\vec\imath+\sin\theta\,\vec\jmath$, on retrouve
> $$R\omega\,\vec u_\theta=-R\omega\sin(\omega t)\,\vec\imath+R\omega\cos(\omega t)\,\vec\jmath,\qquad-R\omega^2\,\vec u_r=-R\omega^2\cos(\omega t)\,\vec\imath-R\omega^2\sin(\omega t)\,\vec\jmath,$$
> c'est-à-dire exactement les résultats cartésiens du TD1 : les deux écritures décrivent **le même vecteur**.
>
> **(a) Le mouvement dépend-il du repère ?**
>
> **Non.** Choisir des coordonnées cartésiennes ou polaires n'est qu'un choix d'**écriture** dans le même référentiel : la trajectoire, la position à chaque instant et la loi du mouvement sont les mêmes. Il ne faut pas confondre avec un changement de référentiel, qui modifie le mouvement.
>
> **(b) Les composantes dépendent-elles de la base ?**
>
> **Oui.** Les composantes sont les « coordonnées » du vecteur dans une base donnée : $\vec v=(-R\omega\sin\theta,\ R\omega\cos\theta)$ en cartésien, mais $\vec v=(0,\ R\omega)$ en polaire. Les nombres changent, l'objet qu'ils décrivent non.
>
> **(c) Le tracé dépend-il de la base ?**
>
> **Non.** La flèche représentant $\vec v$ (ou $\vec a$) en un point donné a la même direction, le même sens et la même longueur, quelle que soit la base utilisée pour calculer ses composantes.
>
> **(d) Les normes dépendent-elles de la base ?**
>
> **Non.** $\|\vec v\|=\sqrt{v_x^2+v_y^2}=\sqrt{v_r^2+v_\theta^2}=R\omega$ et $\|\vec a\|=R\omega^2$ dans les deux bases : le passage d'une base orthonormée à l'autre est une rotation, qui conserve les normes. En revanche, en polaire, ce résultat est immédiat alors qu'en cartésien il demande d'utiliser $\cos^2+\sin^2=1$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]]

