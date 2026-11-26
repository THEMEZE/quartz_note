---
title: "Exercice 3 — Cardioïde"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · <a href="/pdfs/td2_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td2_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 3. Cardioïde *(facultatif)*

*Difficulté ●●●●○ · ⏱ 35 min · Type : Entraînement / Approfondissement*

Dans le plan $Oxy$, on considère le déplacement d'un mobile assimilé à un point $M$ le long d'une courbe
d'équation polaire
$$r(\theta)=a\,(1+\cos\theta),$$
appelée **cardioïde** (courbe « en forme de cœur »).


> [!question]- 🪝 Accroche
> **Où va-t-on le plus vite sur un cœur ?**
>
> *Durée de l'introduction : 3 à 5 min, avant de lire l'énoncé*
>
> *Un point parcourt une courbe en forme de cœur, en tournant autour de l'origine à vitesse angulaire constante. Va-t-il à vitesse constante ? Où va-t-il le plus vite : au creux du cœur ou à sa pointe ? Est-ce qu'il s'arrête quelque part ? Faites votre pari avant de calculer.*
>
> **Idée clé : sur une courbe polaire dont $r$ varie, la vitesse a deux composantes perpendiculaires.**
> $$\vec v=\dot r\,\vec u_r+r\dot\theta\,\vec u_\theta,\qquad\|\vec v\|=\sqrt{\dot r^2+r^2\dot\theta^2}.$$
> Si $\theta(t)$ est donné, on trouve $r(t)=r(\theta(t))$ puis $\dot r=r'(\theta)\,\dot\theta$. Une identité trigonométrique (duplication) transforme ensuite la racine en une expression simple.




> [!abstract]- 🧠 À savoir avant
> **Vitesse en base polaire**
>
> En base polaire, $\overrightarrow{OM}=r\,\vec u_r$ donne $\vec v=\dot r\,\vec u_r+r\dot\theta\,\vec u_\theta$, avec $\|\vec v\|^2=\dot r^2+r^2\dot\theta^2$. Ici $r$ varie avec le temps, donc la composante radiale $\dot r$ n'est plus nulle.
>
> **Formules trigonométriques de duplication**
>
> $\cos(2x)=2\cos^2x-1$ et $\sin(2x)=2\sin x\cos x$. En posant $x=\theta/2$ : $1+\cos\theta=2\cos^2(\theta/2)$.




> [!info]- 🎯 Ce que tu sauras faire
> **Étudier un mouvement le long d'une courbe polaire**
>
> Savoir tracer une courbe $r(\theta)$ point par point, en déduire $r(t)$ quand $\theta(t)$ est connu, calculer $\vec v$ avec ses deux composantes, simplifier la norme grâce à une identité trigonométrique et localiser le maximum de vitesse.




> [!tip]- 📖 Rappel de cours
> **Mouvement le long d'une courbe $r(	heta)$**
>
> Si $\theta(t)$ est connu, on obtient $r(t)=r(\theta(t))$ puis $\dot r=r'(\theta)\,\dot\theta$ (règle de la chaîne). Les deux composantes de la vitesse, radiale $\dot r$ et orthoradiale $r\dot\theta$, sont orthogonales : $\|\vec v\|=\sqrt{\dot r^2+r^2\dot\theta^2}$.




> [!note]- 🧮 Outils mathématiques
> **Formule de duplication : $\cos(2x)=2\cos^2x-1$**
>
> Avec $x=\theta/2$ : $1+\cos\theta=2\cos^2(\theta/2)$. Le calcul $\sin^2\theta+(1+\cos\theta)^2=2+2\cos\theta=4\cos^2(\theta/2)$ en découle.
>
> **Formule de duplication du sinus : $\sin(2x)=2\sin x\cos x$ et symétries**
>
> $\sin\theta=2\sin(\theta/2)\cos(\theta/2)$. Symétries utiles : $\cos(\pi-x)=-\cos x$ et $\sin(\pi-x)=\sin x$ (la cardioïde est symétrique par rapport à $Ox$ : $r(-\theta)=r(\theta)$ et $r(2\pi-\theta)=r(\theta)$).
>
> **Racine d'un carré et valeur absolue**
>
> $\sqrt{u^2}=|u|$. Ici $\sqrt{4\cos^2(\theta/2)}=2|\cos(\theta/2)|$, nul pour $\theta=\pi$ et maximal pour $\theta=0\ [2\pi]$.
>
> **Dérivée composée**
>
> $\dfrac{\mathrm d}{\mathrm dt}\cos(\omega t)=-\omega\sin(\omega t)$, donc $\dot r=-a\omega\sin(\omega t)$.
>
> **Tracé d'une courbe polaire par points**
>
> On dresse un tableau $\theta\mapsto r(\theta)$, on convertit chaque point en cartésien par $x=r\cos\theta$, $y=r\sin\theta$ et on relie. Une valeur $r=0$ donne l'origine.
>
> **Longueur d'une courbe par intégration**
>
> La longueur parcourue est $\displaystyle L=\int\|\vec v\|\,\mathrm dt$ : c'est l'aire sous la courbe $\|\vec v\|(t)$, comme pour une distance parcourue.



**q1.** Étude de la courbe.


(a) Quelle est la dimension de $a$ ?

(b) Choisir une valeur pour $a$ et représenter la cardioïde en plaçant les points correspondant à $\theta=0$, $\theta=\dfrac\pi3$, $\theta=\dfrac\pi2$, $\theta=\dfrac{2\pi}3$, $\theta=\pi$, $\theta=\dfrac{4\pi}3$, $\theta=2\pi$.

(c) Représenter la base polaire $(\vec u_r,\vec u_\theta)$ en un point $P$ de la cardioïde, correspondant à $\theta=\dfrac\pi3$.


> [!tip]- 💡 Coup de pouce
> $r$ est une distance. Pour placer un point, calculez $r(\theta)$, puis $x=r\cos\theta$ et $y=r\sin\theta$. En $P$, $\vec u_r$ est dirigé selon $\overrightarrow{OP}$ et $\vec u_\theta$ en est la rotation de $+90^\circ$.




> [!success]- ✅ Correction
> $[a]=\mathrm L$. Pour $a=2$ cm : $r=4,\ 3,\ 2,\ 1,\ 0,\ 1,\ 4$ cm pour les sept angles ; courbe symétrique par rapport à $Ox$ avec un point de rebroussement en $O$.




> [!example]- 📝 Solution détaillée
> **(a) Dimension de $a$**
>
> $r=a(1+\cos\theta)$ est une longueur et $1+\cos\theta$ est sans dimension : $[a]=\mathrm L$.
>
> **(b) Points de la cardioïde**
>
> On choisit $a=2$ cm. On calcule $r=a(1+\cos\theta)$ puis $x=r\cos\theta$, $y=r\sin\theta$ :
> $$
> \begin{array}{c|ccccccc}
> \theta & 0 & \pi/3 & \pi/2 & 2\pi/3 & \pi & 4\pi/3 & 2\pi\\
> \hline
> r~(\mathrm{cm}) & 4 & 3 & 2 & 1 & 0 & 1 & 4\\
> x~(\mathrm{cm}) & 4 & 1{,}5 & 0 & -0{,}5 & 0 & -0{,}5 & 4\\
> y~(\mathrm{cm}) & 0 & 2{,}6 & 2 & 0{,}87 & 0 & -0{,}87 & 0
> \end{array}
> $$
> La courbe est fermée, symétrique par rapport à $Ox$ ($r(2\pi-\theta)=r(\theta)$). Elle passe par $(2a,0)$ pour $\theta=0$ (point le plus éloigné de $O$) et revient à l'origine pour $\theta=\pi$, où elle présente un **point de rebroussement** (« creux » du cœur).
>
> **(c) Base polaire en $P$**
>
> Pour $\theta=\pi/3$, $P$ est à la distance $r=\tfrac32a$ de $O$, et
> $$\vec u_r=\cos\tfrac\pi3\,\vec\imath+\sin\tfrac\pi3\,\vec\jmath=\tfrac12\vec\imath+\tfrac{\sqrt3}2\vec\jmath,\qquad\vec u_\theta=-\tfrac{\sqrt3}2\vec\imath+\tfrac12\vec\jmath.$$
> On trace $\vec u_r$ le long de la droite $(OP)$, en s'éloignant de $O$, et $\vec u_\theta$ perpendiculaire, orienté dans le sens des $\theta$ croissants. Contrairement au cercle, $\vec u_\theta$ n'est pas tangent à la courbe ici (car $r$ varie avec $\theta$).



**q2.** La courbe est parcourue avec une vitesse angulaire $\dot\theta=\omega$ constante, avec $\theta(0)=0$.


(a) Déterminer l'expression de $\theta(t)$ et en déduire $r(t)$.

(b) Déterminer l'expression du vecteur vitesse $\vec v$ de $M$ dans la base $(\vec u_r,\vec u_\theta)$ et calculer sa norme.

(c) Représenter la vitesse du mobile lorsqu'il se situe au point $P$.

(d) En quel point de la trajectoire la vitesse de $M$ est-elle maximale ?


> [!tip]- 💡 Coup de pouce
> Intégrez $\dot\theta=\omega$. Pour la vitesse, utilisez $\vec v=\dot r\,\vec u_r+r\dot\theta\,\vec u_\theta$ avec $\dot r=-a\omega\sin\omega t$. Pour simplifier la norme, développez $\sin^2+(1+\cos)^2$.




> [!success]- ✅ Correction
> $\theta=\omega t$, $r=a(1+\cos\omega t)$ ; $\vec v=-a\omega\sin(\omega t)\,\vec u_r+a\omega(1+\cos\omega t)\,\vec u_\theta$ ; $\|\vec v\|=2a\omega\,|\cos(\omega t/2)|$ ; vitesse maximale ($2a\omega$) en $\theta=0$, point $(2a,0)$.




> [!example]- 📝 Solution détaillée
> **(d) Équations horaires**
>
> $\dot\theta=\omega$ constant et $\theta(0)=0$ donnent $\boxed{\theta(t)=\omega t}$, donc
> $$\boxed{r(t)=a\,(1+\cos\omega t)}.$$
>
> **(e) Vecteur vitesse**
>
> $\dot r=-a\omega\sin\omega t$ et $r\dot\theta=a\omega(1+\cos\omega t)$ :
> $$\boxed{\vec v=-a\omega\sin(\omega t)\,\vec u_r+a\omega\,(1+\cos\omega t)\,\vec u_\theta}.$$
> Les deux composantes sont orthogonales, donc
> $$\|\vec v\|^2=a^2\omega^2\left[\sin^2\omega t+(1+\cos\omega t)^2\right]=a^2\omega^2\,(2+2\cos\omega t).$$
> Avec $1+\cos\omega t=2\cos^2(\omega t/2)$ :
> $$\boxed{\|\vec v\|=2a\omega\,\left|\cos\frac{\omega t}2\right|}.$$
>
> **(f) Vitesse au point $P$ ($\theta=\pi/3$)**
>
> Pour $\omega t=\pi/3$ : $v_r=-a\omega\sin\frac\pi3=-\frac{\sqrt3}2a\omega\approx-0{,}87\,a\omega$ et $v_\theta=a\omega\left(1+\frac12\right)=\frac32a\omega$. D'où $\|\vec v\|=a\omega\sqrt{\tfrac34+\tfrac94}=\sqrt3\,a\omega\approx1{,}73\,a\omega$, ce qui coïncide avec $2a\omega\cos\frac\pi6=\sqrt3\,a\omega$. En $P$, on trace $\vec v$ avec une composante **rentrante** ($v_r<0$ : le point se rapproche de $O$) et une grande composante orthoradiale ($v_\theta>0$ : le point tourne dans le sens trigonométrique).
>
> **(g) Vitesse maximale**
>
> $\|\vec v\|$ est maximale lorsque $|\cos(\omega t/2)|=1$, soit $\omega t=0\ [2\pi]$, c'est-à-dire $\theta=0$ : le point $(2a,0)$, le plus éloigné de $O$. La vitesse vaut alors $v_{\max}=2a\omega$, dirigée selon $\vec u_\theta=\vec\jmath$ ($v_r=0$ en ce point). À l'inverse, $\|\vec v\|=0$ pour $\omega t=\pi$ : le point passe en $O$, point de rebroussement, où il s'arrête un instant avant de repartir.




> [!note]- 🔗 Liens avec d'autres disciplines
> **Acoustique**
>
> Un **microphone cardioïde** a une sensibilité en fonction de l'angle d'incidence proportionnelle à $1+\cos\theta$ : maximale en face, nulle derrière. Son diagramme de directivité est exactement cette courbe.
>
> **Optique**
>
> La lumière d'une source ponctuelle placée sur le bord d'une tasse circulaire se réfléchit sur la paroi et forme une courbe lumineuse (caustique) qui est une cardioïde. Pour un faisceau parallèle, c'est une néphroïde.
>
> **Mathématiques**
>
> Courbes polaires (limaçons $r=a+b\cos\theta$), épicycloïdes, intégrales de longueur et d'aire. La cardioïde est aussi le contour de la partie principale de l'ensemble de Mandelbrot.
>
> **Mécanique**
>
> Un point matériel peut s'arrêter sans que le mouvement soit terminé : au point de rebroussement, $\vec v=\vec0$ puis le mobile repart en changeant de direction, comme une balle au sommet de sa trajectoire verticale.




> [!question]- 🔭 Aller plus loin — Licence : Longueur et aire de la cardioïde
> La longueur parcourue en un tour est $L=\int_0^{T}\|\vec v\|\,\mathrm dt=\int_0^{2\pi}2a|\cos(\theta/2)|\,\mathrm d\theta=8a$. L'aire intérieure est $\mathcal A=\tfrac12\int_0^{2\pi}r^2\,\mathrm d\theta=\tfrac32\pi a^2$. Refaire les deux calculs et vérifier que la longueur ne demande aucune hypothèse sur $\omega$ (elle ne dépend que de la forme de la courbe).




> [!question]- 🔭 Aller plus loin — Master : Une cardioïde comme épicycloïde
> La cardioïde est la trajectoire d'un point d'un cercle de rayon $a/2$ qui roule sans glisser à l'extérieur d'un cercle fixe de même rayon $a/2$ (épicycloïde à une seule pointe). En notation complexe, le contour de la cardioïde principale de l'ensemble de Mandelbrot s'écrit $c(t)=\tfrac12e^{it}-\tfrac14e^{2it}$. Montrer que l'on obtient la même courbe, à une similitude près (translation, rotation, homothétie), que $r=a(1+\cos\theta)$.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex5-bille-sur-une-sphere-angle-de-decollage|Exercice 5 — (*) Bille sur une sphère : angle de décollage]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex3-vitesse-et-acceleration-en-coordonnees-polaires|Exercice 3 — Vitesse et accélération en coordonnées polaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex2-seance-1-exploitation-de-la-chronophotographie-vitesses-forces-lois-de-newton|Exercice 2 — Séance 1 -- Exploitation de la chronophotographie : vitesses, forces, lois de Newton]]


