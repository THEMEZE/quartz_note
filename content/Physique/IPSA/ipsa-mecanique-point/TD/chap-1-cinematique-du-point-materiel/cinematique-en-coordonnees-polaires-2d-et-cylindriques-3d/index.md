---
title: "Cinématique en coordonnées polaires (2D) et cylindriques (3D)"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/index|⬅ Mécanique du point — IPSA]]


> [!info] ℹ️ Chap. 1 — Cinématique du point matériel
> Séance 2



<a href="/pdfs/td2_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td2_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>


> [!question]- 🪝 Accroche
> **Un radar, une planète, un faucon : un seul système de coordonnées ?**
>
> *Durée de l'introduction : 5 à 8 min, avant les exercices*
>
> *Comment décrire **simplement** un satellite sur son orbite, une perle sur une tige qui tourne, un faucon qui fond sur sa proie et trois drones qui se poursuivent ? Pourquoi $x(t)$ et $y(t)$ donnent-ils des équations lourdes alors que $r(t)$ et $\theta(t)$ les rendent presque évidentes ? Pourquoi la base polaire est-elle « mobile » et quelles en sont les conséquences sur l'accélération ?*
>
> **Idée clé : on choisit les coordonnées adaptées à la symétrie.** Pour un mouvement autour d'un point $O$, on repère $M$ par $r=OM$ et par l'angle $\theta$. La base $(\vec u_r,\vec u_\theta)$ est liée à $M$ et **tourne** avec lui : $\dfrac{\mathrm d\vec u_r}{\mathrm dt}=\dot\theta\,\vec u_\theta$ et $\dfrac{\mathrm d\vec u_\theta}{\mathrm dt}=-\dot\theta\,\vec u_r$. D'où
> $$\vec v=\dot r\,\vec u_r+r\dot\theta\,\vec u_\theta,\qquad\vec a=(\ddot r-r\dot\theta^2)\,\vec u_r+(r\ddot\theta+2\dot r\dot\theta)\,\vec u_\theta.$$
> Chaque terme a un sens physique (variation de distance, rotation, centripète, Coriolis). En 3D, on ajoute simplement l'axe fixe $\vec k$.



> [!abstract]- 🧠 À savoir avant
> **Cinématique cartésienne (TD1)**
>
> Savoir dériver une loi horaire pour obtenir $\vec v$ et $\vec a$, intégrer avec des conditions initiales, calculer une norme, éliminer le temps pour obtenir une trajectoire. Mouvement circulaire uniforme en cartésien : $x=R\cos\omega t$, $y=R\sin\omega t$, $\vec a=-\omega^2\overrightarrow{OM}$.
>
> **Dérivée d'un vecteur unitaire tournant**
>
> Pour $\vec u_r=\cos\theta\,\vec\imath+\sin\theta\,\vec\jmath$ et $\vec u_\theta=-\sin\theta\,\vec\imath+\cos\theta\,\vec\jmath$ : $\dfrac{\mathrm d\vec u_r}{\mathrm dt}=\dot\theta\,\vec u_\theta$ et $\dfrac{\mathrm d\vec u_\theta}{\mathrm dt}=-\dot\theta\,\vec u_r$ (dérivée composée). Un vecteur de base **fixe** ($\vec\imath$, $\vec\jmath$, $\vec k$) a une dérivée nulle.
>
> **Trigonométrie**
>
> Cercle trigonométrique, valeurs remarquables ($0,\ \pi/6,\ \pi/4,\ \pi/3,\ \pi/2$), $\cos^2+\sin^2=1$, formules d'addition et de duplication ($\cos2x=2\cos^2x-1$, $\sin2x=2\sin x\cos x$), angle moitié ($1+\cos\theta=2\cos^2\frac\theta2$), complément ($\cos(\frac\pi2-x)=\sin x$). Fonctions $\arctan$ et $\operatorname{atan2}$ et discussion du quadrant.
>
> **Fonctions exponentielle, logarithme et hyperboliques**
>
> $(\mathrm e^{\lambda t})'=\lambda\mathrm e^{\lambda t}$, $\ln$ comme réciproque, $\cosh$ et $\sinh$ ($\cosh^2-\sinh^2=1$, $\cosh'=\sinh$). Résolution de $\ddot r=\pm\omega^2r$ (solutions exponentielles ou sinusoïdales).
>
> **Calcul vectoriel et produits**
>
> Composantes dans une base orthonormée, norme, produit scalaire (orthogonalité), produit vectoriel dans le plan ($v_xa_y-v_ya_x$). Un vecteur se dérive composante par composante **seulement si la base est fixe** ; sinon, il faut dériver aussi les vecteurs de base.
>
> **Courbes planes, aires et longueurs**
>
> Tracé d'une courbe point par point, équation d'un cercle et d'une droite, aire d'un secteur $\tfrac12r^2\,\mathrm d\theta$, longueur $L=\int\|\vec v\|\,\mathrm dt$, séries géométriques.
>
> **Dimensions et ordres de grandeur**
>
> $[\dot\theta]=\mathrm T^{-1}$ (le radian est sans dimension), $[r\dot\theta]=\mathrm{L\,T^{-1}}$, $[\vec a]=\mathrm{L\,T^{-2}}$ ; accélération centripète d'une voiture dans un virage $\sim3$ à $5\ \mathrm{m\,s^{-2}}$, vitesse orbitale de la Terre $\simeq30$ km/s.



> [!info]- 🎯 Ce que tu sauras faire
> **Choisir et utiliser le système de coordonnées adapté**
>
> Passer des coordonnées cartésiennes aux coordonnées polaires, cylindriques et inversement ; choisir celles qui épousent la symétrie du problème (rotation autour d'un point ou d'un axe) ; écrire sans hésiter $\overrightarrow{OM}$, $\vec v$ et $\vec a$ dans la base polaire ou cylindrique.
>
> **Maîtriser les dérivées des vecteurs de base et leurs conséquences**
>
> Savoir que la base polaire **tourne** avec $M$, retrouver à chaque fois $\dfrac{\mathrm d\vec u_r}{\mathrm dt}=\dot\theta\,\vec u_\theta$ et $\dfrac{\mathrm d\vec u_\theta}{\mathrm dt}=-\dot\theta\,\vec u_r$, et en déduire les formules $\vec v=\dot r\,\vec u_r+r\dot\theta\,\vec u_\theta$ et $\vec a=(\ddot r-r\dot\theta^2)\,\vec u_r+(r\ddot\theta+2\dot r\dot\theta)\,\vec u_\theta$.
>
> **Interpréter chaque terme de la vitesse et de l'accélération**
>
> Reconnaître la composante radiale ($\dot r$), orthoradiale ($r\dot\theta$), centripète ($-r\dot\theta^2$) et de Coriolis ($2\dot r\dot\theta$) ; savoir que $\vec a\neq\vec0$ dès qu'un mouvement est circulaire, même uniforme ; lire géométriquement un résultat (vitesse maximale, arrêt, angle constant).
>
> **Étudier une trajectoire donnée par $r(\theta)$**
>
> Tracer une courbe polaire (cardioïde, spirale, ellipse), déduire $r(t)$ de $r(\theta)$ et $\theta(t)$ par la règle de la chaîne $\dot r=\dfrac{\mathrm dr}{\mathrm d\theta}\dot\theta$, calculer longueur, rayon de courbure, accélérations tangentielle et normale.
>
> **Étendre à la 3D et exploiter des symétries et des lois de conservation**
>
> Ajouter l'axe fixe $\vec k$ (hélice), utiliser la symétrie d'un problème collectif (poursuite) pour le ramener à un seul mobile, exploiter la loi des aires $r^2\dot\theta=$ cte, reconnaître une accélération radiale ; retrouver sans forces une loi en $1/r^2$.
>
> **Compétences transversales**
>
> Faire un schéma soigné avec les bases locales, mener des calculs trigonométriques et exponentiels sans erreur de signe, **valider** (homogénéité, cas limites, ordre de grandeur), utiliser Python pour tracer trajectoires, vecteurs et hodographes.



> [!tip]- 📖 Rappel de cours
> **Coordonnées polaires et base polaire**
>
> $$x=r\cos\theta,\quad y=r\sin\theta,\quad r=\sqrt{x^2+y^2},\quad\cos\theta=\frac xr,\quad\sin\theta=\frac yr.$$
> $\vec u_r=\cos\theta\,\vec\imath+\sin\theta\,\vec\jmath$, $\vec u_\theta=-\sin\theta\,\vec\imath+\cos\theta\,\vec\jmath$, $\overrightarrow{OM}=r\,\vec u_r$, $\dfrac{\mathrm d\vec u_r}{\mathrm dt}=\dot\theta\,\vec u_\theta$, $\dfrac{\mathrm d\vec u_\theta}{\mathrm dt}=-\dot\theta\,\vec u_r$.
>
> **Vitesse et accélération en polaire et en cylindrique**
>
> $$\vec v=\dot r\,\vec u_r+r\dot\theta\,\vec u_\theta\ (+\dot z\,\vec k),\qquad\|\vec v\|^2=\dot r^2+r^2\dot\theta^2\ (+\dot z^2),$$
> $$\vec a=\left(\ddot r-r\dot\theta^2\right)\vec u_r+\left(r\ddot\theta+2\dot r\dot\theta\right)\vec u_\theta\ (+\ddot z\,\vec k).$$
> La composante $-r\dot\theta^2$ est **centripète** ; $2\dot r\dot\theta$ est l'accélération **de Coriolis**. On a aussi $a_\theta=\dfrac1r\dfrac{\mathrm d}{\mathrm dt}\left(r^2\dot\theta\right)$.
>
> **Mouvements de référence**
>
> **Circulaire** ($r=R$) : $\vec v=R\dot\theta\,\vec u_\theta$, $\vec a=-R\dot\theta^2\,\vec u_r+R\ddot\theta\,\vec u_\theta$ ; uniforme si $\dot\theta=\omega$ : $v=R\omega$, $\vec a=-R\omega^2\,\vec u_r$.
>
> **Hélicoïdal** ($r=a$, $z=h\theta$) : $\vec v=\dot\theta\,(a\,\vec u_\theta+h\,\vec k)$, $\tan\alpha=h/a$.
>
> **Courbe $r(\theta)$ parcourue à $\dot\theta=\omega$** : $\dot r=r'(\theta)\,\omega$.
>
> **Loi des aires et accélération radiale**
>
> $\vec a\parallel\vec u_r\iff r^2\dot\theta=C=$ cte. La vitesse aréolaire est $\dfrac{\mathrm dA}{\mathrm dt}=\dfrac C2$. Une loi des aires conduit à $\dot\theta=C/r^2$ : le mobile tourne plus vite quand il est proche de $O$.
>
> **Composantes tangentielle et normale**
>
> $\vec a=a_t\,\vec\tau+a_n\,\vec n$ avec $a_t=\dfrac{\mathrm dv}{\mathrm dt}$, $a_n=\dfrac{v^2}\rho=\sqrt{a^2-a_t^2}$ et, dans le plan, $\rho=\dfrac{v^3}{|v_xa_y-v_ya_x|}=\dfrac{v^3}{|v_ra_\theta-v_\theta a_r|}$. Si $v=$ cte alors $\vec a\perp\vec v$.
>
> **Méthode d'étude d'un mouvement en polaire**
>
> (1) Schéma avec $O$, $\vec u_r$, $\vec u_\theta$ (et $\vec k$). (2) Écrire $r(t)$ et $\theta(t)$ (ou $r(\theta)$ et $\theta(t)$ et en déduire $r(t)$). (3) Dériver : $\dot r$, $\dot\theta$, $\ddot r$, $\ddot\theta$. (4) Reporter dans les formules de $\vec v$ et $\vec a$. (5) Calculer normes, angles, extrémas. (6) Valider : cas limites, homogénéité, ordre de grandeur.



> [!note]- 🧮 Outils mathématiques
> **Dérivée d'un vecteur de base et dérivée composée**
>
> Si $\vec u(\theta(t))$ : $\dfrac{\mathrm d\vec u}{\mathrm dt}=\dot\theta\,\dfrac{\mathrm d\vec u}{\mathrm d\theta}$. Pour $r(\theta(t))$ : $\dot r=\dfrac{\mathrm dr}{\mathrm d\theta}\dot\theta$ ; $\ddot r=\dfrac{\mathrm d^2r}{\mathrm d\theta^2}\dot\theta^2+\dfrac{\mathrm dr}{\mathrm d\theta}\ddot\theta$.
>
> **Formules trigonométriques et duplication**
>
> $\cos2x=2\cos^2x-1$, $\sin2x=2\sin x\cos x$, $1+\cos\theta=2\cos^2\tfrac\theta2$, $1-\cos\theta=2\sin^2\tfrac\theta2$, $\sin^2\theta+(1+\cos\theta)^2=2+2\cos\theta$.
>
> **Exponentielles, logarithmes et fonctions hyperboliques**
>
> $\cosh x=\dfrac{\mathrm e^x+\mathrm e^{-x}}2$, $\sinh x=\dfrac{\mathrm e^x-\mathrm e^{-x}}2$, $\cosh^2x-\sinh^2x=1$, $\cosh2x=\cosh^2x+\sinh^2x$, $\operatorname{arcosh}y=\ln\left(y+\sqrt{y^2-1}\right)$. Équation $\ddot r=\omega^2r$ : $r=A\cosh\omega t+B\sinh\omega t$.
>
> **Séparation des variables**
>
> $\dfrac{\mathrm dr}{\mathrm d\theta}=-\lambda r\iff r=r_0\mathrm e^{-\lambda\theta}$ (spirale logarithmique). Pour $\dot\theta=\dfrac\mu r$ avec $r=R-\lambda t$ : $\theta=-\dfrac\mu\lambda\ln\left(1-\dfrac t T\right)$ avec $T=R/\lambda$.
>
> **Intégrales de longueur et d'aire**
>
> $L=\int\|\vec v\|\,\mathrm dt$ ; aire d'un secteur polaire $A=\tfrac12\int r^2\,\mathrm d\theta$ ; $\displaystyle\int_0^\infty\mathrm e^{-\lambda t}\,\mathrm dt=\dfrac1\lambda$ ; $\displaystyle\int_0^{2\pi}|\cos\tfrac\theta2|\,\mathrm d\theta=4$.
>
> **Rayon de courbure**
>
> Dans le plan : $\rho=\dfrac{v^3}{|v_ra_\theta-v_\theta a_r|}$. Si $v=$ cte : $\rho=v^2/\|\vec a\|$. Pour un cercle $\rho=R$, une droite $\rho=\infty$.
>
> **Équations de coniques et hodographe**
>
> Ellipse de foyer $O$ : $r=\dfrac p{1+e\cos\theta}$, $a=\dfrac p{1-e^2}$, $b^2=ap$. L'hodographe est le lieu de l'extrémité de $\vec v$ ; pour Kepler c'est un cercle de rayon $C/p$ centré en $\dfrac{Ce}p\,\vec u_y$.
>
> **Produit scalaire et orthogonalité**
>
> $\vec a\cdot\vec v=\tfrac12\dfrac{\mathrm d\|\vec v\|^2}{\mathrm dt}$ : $\|\vec v\|=$ cte $\iff\vec a\perp\vec v$. L'angle entre deux vecteurs se lit sur $\cos\varphi=\dfrac{\vec A\cdot\vec B}{\|\vec A\|\|\vec B\|}$.



## Exercices

- [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]]


> [!note]- 🔗 Liens avec d'autres disciplines
> **Mathématiques**
>
> Nombres complexes (module et argument), courbes polaires (cardioïde, spirales, coniques), changement de variables dans les intégrales doubles ($\mathrm dA=r\,\mathrm dr\,\mathrm d\theta$), courbes de poursuite, géométrie différentielle (courbure, torsion de l'hélice).
>
> **Astronomie et planétologie**
>
> Lois de Kepler, mouvements des planètes, comètes, satellites, trajectoires de transfert, spirales de galaxies, orbites autour d'un trou noir.
>
> **Électromagnétisme**
>
> Particule chargée dans un champ magnétique uniforme (cercle, hélice, rayon de Larmor, aurores polaires, cyclotron, tokamak) ; champs à symétrie cylindrique (fil, solénoïde) ; microphones cardioïdes, diagrammes de rayonnement d'antennes.
>
> **Mécanique, référentiels tournants et technologie**
>
> Force de Coriolis, plateau tournant, centrifugeuse, essoreuse, turbines, vis et engrenages hélicoïdaux (pas $2\pi h$), came et bielle-manivelle en polaire.
>
> **Navigation, radar et robotique**
>
> Un radar, un sonar ou un lidar mesure une distance et un angle : mesures polaires converties en cartésien. Guidage et navigation proportionnelle, algorithmes de rendez-vous de drones et de robots en formation.
>
> **Biologie et éthologie**
>
> Approche en spirale du faucon pèlerin, poursuite d'une proie, vol des insectes autour d'une lumière, géométrie de l'ADN (double hélice, rayon $\sim1$ nm, pas $3{,}4$ nm), coquilles en spirale (nautile).
>
> **Informatique et simulation**
>
> Représentation de trajectoires par intégration numérique (Euler, Runge--Kutta), moteurs physiques de jeux vidéo, animation d'orbites, algorithmes de poursuite et de flocage.



> [!question]- 🔭 Aller plus loin — CPGE : Simulation numérique de mouvements polaires
> Intégrer par la méthode d'Euler (puis \texttt{solve\_ivp}) les équations $\ddot r=r\dot\theta^2+f_r$ et $r\ddot\theta=-2\dot r\dot\theta+f_\theta$ pour la poursuite à $n$ drones ou pour une perle sur tige ; comparer à la solution analytique ($r=r_0\cosh\omega t$) et étudier l'erreur en fonction du pas.



> [!question]- 🔭 Aller plus loin — Licence : Repère de Frenet et rayon de courbure en polaire
> Établir, pour une courbe $r(\theta)$, la formule $\rho=\dfrac{(r^2+r'^2)^{3/2}}{r^2+2r'^2-rr''}$ et la comparer aux rayons de courbure obtenus dans le TD : cardioïde, spirale équiangulaire ($\rho=r\sqrt{1+k^2}$), ellipse. Vérifier $a_n=v^2/\rho$.



> [!question]- 🔭 Aller plus loin — Licence : Coordonnées sphériques
> Écrire $\overrightarrow{OM}=r\,\vec u_r$ en base sphérique $(\vec u_r,\vec u_\theta,\vec u_\varphi)$ et établir $\vec v=\dot r\,\vec u_r+r\dot\theta\,\vec u_\theta+r\sin\theta\,\dot\varphi\,\vec u_\varphi$. Traiter le mouvement d'un point à la surface d'une sphère ($r=R$) et la trajectoire d'un satellite en orbite polaire.



> [!question]- 🔭 Aller plus loin — Master : Mécanique lagrangienne et coordonnées généralisées
> Les coordonnées $(r,\theta)$ sont des exemples de **coordonnées généralisées**. Écrire l'énergie cinétique $\tfrac12m(\dot r^2+r^2\dot\theta^2)$, les équations d'Euler--Lagrange et retrouver $a_\theta=\dfrac1r\dfrac{\mathrm d}{\mathrm dt}(r^2\dot\theta)$ (conservation de $r^2\dot\theta$ pour un potentiel central) et l'équation radiale de l'exercice 5.



> [!question]- 🔭 Aller plus loin — Doctorat : Symétrie cachée du problème de Kepler
> L'hodographe circulaire (exercice 8) est la manifestation de la conservation du vecteur de Runge--Lenz. Montrer que le groupe de symétrie du problème de Kepler est $SO(4)$ (ou $SO(3,1)$ pour les orbites non liées) et que l'hodographe devient un grand cercle de la sphère $S^3$ (projection de Fock).


