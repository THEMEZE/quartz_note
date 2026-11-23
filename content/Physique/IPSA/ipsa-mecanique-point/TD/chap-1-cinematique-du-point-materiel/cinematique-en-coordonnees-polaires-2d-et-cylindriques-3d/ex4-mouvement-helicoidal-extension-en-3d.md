---
title: "Exercice 4 — Mouvement hélicoïdal (extension en 3D)"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · <a href="/pdfs/td2_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td2_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 4. Mouvement hélicoïdal (extension en 3D) *(facultatif)*

*Difficulté ●●●○○ · ⏱ 30 min · Type : Entraînement / Extension 3D*

Dans l'espace muni d'un repère cartésien $Oxyz$, un point $M$ décrit une **hélice circulaire** d'axe $Oz$,
d'équations horaires (en coordonnées cylindriques)
$$\begin{cases}r(t)=a\\\theta(t)\\z(t)=h\,\theta(t)\end{cases}$$
où $a$ et $h$ sont des paramètres constants et $\theta(t)$ est l'angle entre $Ox$ et $\overrightarrow{Om}$,
$m$ étant la projection du point $M$ sur le plan $Oxy$. On note $\dot\theta$ la vitesse angulaire.

> [!question]+ 🎣 Accroche
> **Une trajectoire qui monte en tournant**
>
> *Durée de l'introduction : 3 à 5 min, avant de lire l'énoncé*
>
> *Un ressort, une vis, un escalier en colimaçon, la molécule d'ADN : la trajectoire d'un point qui tourne autour d'un axe tout en avançant le long de cet axe est une **hélice**. Si l'on déroule le cylindre sur lequel elle est tracée, que devient-elle ? Et l'inclinaison de la vitesse, est-elle constante ?*
>
> **Idée clé : en coordonnées cylindriques, on ajoute à la base polaire un axe fixe $\vec k$.** La vitesse gagne une composante $\dot z\,\vec k$, l'accélération une composante $\ddot z\,\vec k$ :
> $$\vec v=\dot r\,\vec u_r+r\dot\theta\,\vec u_\theta+\dot z\,\vec k.$$
> Pour l'hélice ($r=a$, $z=h\theta$) : $\vec v=\dot\theta\,(a\,\vec u_\theta+h\,\vec k)$. La composante horizontale ($a\dot\theta$) et la composante verticale ($h\dot\theta$) sont proportionnelles : **l'inclinaison de la vitesse est constante**.


> [!abstract]+ 📚 Prérequis
> **Base cylindrique**
>
> La base cylindrique $(\vec u_r,\vec u_\theta,\vec k)$ est la base polaire du plan $Oxy$ complétée par l'axe fixe $\vec k$ de $Oz$. Le vecteur position est $\overrightarrow{OM}=r\,\vec u_r+z\,\vec k$, avec $\dfrac{\mathrm d\vec u_r}{\mathrm dt}=\dot\theta\,\vec u_\theta$, $\dfrac{\mathrm d\vec u_\theta}{\mathrm dt}=-\dot\theta\,\vec u_r$ et $\dfrac{\mathrm d\vec k}{\mathrm dt}=\vec0$.


> [!info]+ 🎯 Objectifs
> **Étendre la cinématique polaire à la 3D**
>
> Savoir qu'en coordonnées cylindriques on ajoute simplement une composante selon l'axe fixe $\vec k$, calculer $\vec v$ et $\vec a$ d'un mouvement hélicoïdal, et exploiter une propriété géométrique (angle constant avec le plan $Oxy$).


> [!note]+ 📖 Point de cours
> **Cinématique en coordonnées cylindriques**
>
> $$\overrightarrow{OM}=r\,\vec u_r+z\,\vec k,\qquad\vec v=\dot r\,\vec u_r+r\dot\theta\,\vec u_\theta+\dot z\,\vec k,$$
> $$\vec a=\left(\ddot r-r\dot\theta^2\right)\vec u_r+\left(r\ddot\theta+2\dot r\dot\theta\right)\vec u_\theta+\ddot z\,\vec k.$$


> [!note]- 🧮 Outils mathématiques
> **Dérivée composée et dérivée d'un produit**
>
> $z=h\theta(t)$ donne $\dot z=h\dot\theta$ et $\ddot z=h\ddot\theta$ ($h$ constant). Même règle que pour toute fonction d'une fonction du temps.
>
> **Pythagore dans l'espace**
>
> $\vec u_\theta$ et $\vec k$ sont orthogonaux et unitaires : $\|a\dot\theta\,\vec u_\theta+h\dot\theta\,\vec k\|=|\dot\theta|\sqrt{a^2+h^2}$.
>
> **Angle entre un vecteur et un plan**
>
> L'angle $\alpha$ entre $\vec v$ et le plan $Oxy$ est celui entre $\vec v$ et sa projection horizontale : $\tan\alpha=\dfrac{v_z}{\|\vec v_{\text{horizontale}}\|}=\dfrac{h\dot\theta}{a\dot\theta}=\dfrac ha$. On retrouve l'idée de pente : $\alpha=\arctan(h/a)$.
>
> **Hélice et cylindre déroulé**
>
> Si l'on déroule le cylindre en un rectangle, $\theta$ devient l'abscisse curviligne $a\theta$, et l'hélice devient la droite $z=\dfrac ha\,(a\theta)$ : une droite de pente $h/a$. La longueur de l'hélice entre deux tours est $2\pi\sqrt{a^2+h^2}$ (Pythagore sur le triangle $2\pi a$, $2\pi h$).
>
> **Produit scalaire et orthogonalité**
>
> $\vec a\cdot\vec v=0$ si $\|\vec v\|$ est constante : $\tfrac12\dfrac{\mathrm d}{\mathrm dt}\|\vec v\|^2=\vec a\cdot\vec v$. En 3D comme en 2D, un mouvement uniforme a une accélération normale à la trajectoire.


**q1.** (a) Compléter la figure avec les données du problème : représenter l'axe $Oz$, le point $M$, sa projection $m$ sur $Oxy$, les coordonnées cylindriques $(r,\theta,z)$ et la base $(\vec u_r,\vec u_\theta,\vec k)$.

> [!tip]- 💡 Coup de pouce
> $\overrightarrow{OM}=\overrightarrow{Om}+\overrightarrow{mM}$ avec $\overrightarrow{Om}=a\,\vec u_r$ et $\overrightarrow{mM}=z\,\vec k$.


> [!success]- ✅ Correction
> $\overrightarrow{OM}=a\,\vec u_r+h\theta\,\vec k$ ; $\vec u_r$ dirigé de $O$ vers $m$, $\vec u_\theta$ perpendiculaire à $\vec u_r$ dans le plan horizontal, $\vec k$ vertical ascendant.


> [!example]- 📝 Solution détaillée
> **(a) Construction de la figure**
>
> On trace le cylindre d'axe $Oz$ et de rayon $a$. Le point $m$ est la projection de $M$ sur $Oxy$, à la distance $a$ de $O$, à l'angle $\theta$ de $Ox$. On trace alors :
>
>
> - $\vec u_r$ : horizontal, de $O$ vers $m$ (direction radiale) ;
> - $\vec u_\theta$ : horizontal, perpendiculaire à $\vec u_r$, dans le sens des $\theta$ croissants ;
> - $\vec k$ : vertical, vers le haut ; $\overrightarrow{mM}=z\,\vec k$ avec $z=h\theta$.
>
>
> Le vecteur position est $\overrightarrow{OM}=a\,\vec u_r+h\theta\,\vec k$. Quand $\theta$ augmente de $2\pi$, le point revient à la même position $m$ mais à l'altitude $2\pi h$ plus haute : c'est le **pas** de l'hélice.


**q2.** (b) Établir l'expression du vecteur vitesse $\vec v$ et du vecteur accélération $\vec a$ de $M$ et leur norme.

> [!tip]- 💡 Coup de pouce
> Dérivez $\overrightarrow{OM}=a\,\vec u_r+h\theta\,\vec k$ par rapport au temps. $a$, $h$ et $\vec k$ sont constants ; seuls $\vec u_r$ et $\theta$ varient.


> [!success]- ✅ Correction
> $\vec v=a\dot\theta\,\vec u_\theta+h\dot\theta\,\vec k$, $\|\vec v\|=|\dot\theta|\sqrt{a^2+h^2}$ ; $\vec a=-a\dot\theta^2\,\vec u_r+a\ddot\theta\,\vec u_\theta+h\ddot\theta\,\vec k$, $\|\vec a\|=\sqrt{a^2\dot\theta^4+(a^2+h^2)\ddot\theta^2}$.


> [!example]- 📝 Solution détaillée
> **(b) Vecteur vitesse**
>
> $$\vec v=a\,\frac{\mathrm d\vec u_r}{\mathrm dt}+h\dot\theta\,\vec k=\boxed{a\dot\theta\,\vec u_\theta+h\dot\theta\,\vec k}.$$
> Les vecteurs $\vec u_\theta$ et $\vec k$ sont orthogonaux et unitaires :
> $$\|\vec v\|=\boxed{|\dot\theta|\sqrt{a^2+h^2}}.$$
>
> **(b) Vecteur accélération**
>
> $$\vec a=a\ddot\theta\,\vec u_\theta+a\dot\theta\,\frac{\mathrm d\vec u_\theta}{\mathrm dt}+h\ddot\theta\,\vec k=\boxed{-a\dot\theta^2\,\vec u_r+a\ddot\theta\,\vec u_\theta+h\ddot\theta\,\vec k}.$$
> Les trois composantes étant orthogonales,
> $$\|\vec a\|=\sqrt{a^2\dot\theta^4+a^2\ddot\theta^2+h^2\ddot\theta^2}=\boxed{\sqrt{a^2\dot\theta^4+(a^2+h^2)\,\ddot\theta^2}}.$$
> On retrouve la formule générale du point de cours avec $\dot r=\ddot r=0$ et $\ddot z=h\ddot\theta$.


**q3.** (c) Montrer que le vecteur vitesse $\vec v$ fait avec le plan $Oxy$ un angle constant.

> [!tip]- 💡 Coup de pouce
> Décomposez $\vec v$ en une partie horizontale (dans $Oxy$) et une partie verticale (selon $\vec k$). L'angle avec le plan est celui entre $\vec v$ et sa partie horizontale.


> [!success]- ✅ Correction
> $\tan\alpha=\dfrac{v_z}{\|\vec v_{\text{hor}}\|}=\dfrac ha$ : indépendant du temps et de $\theta(t)$.


> [!example]- 📝 Solution détaillée
> **(c) Angle avec le plan $Oxy$**
>
> La partie horizontale de $\vec v$ est $a\dot\theta\,\vec u_\theta$, de norme $a|\dot\theta|$ ; la partie verticale est $h\dot\theta\,\vec k$. L'angle $\alpha$ que fait $\vec v$ avec le plan $Oxy$ vérifie
> $$\tan\alpha=\frac{|h\dot\theta|}{a|\dot\theta|}=\boxed{\frac ha}\qquad\Longleftrightarrow\qquad\sin\alpha=\frac{h}{\sqrt{a^2+h^2}}.$$
> Cette valeur ne dépend ni de $t$, ni de $\theta$, ni de la loi $\theta(t)$ choisie (tant que $\dot\theta\neq0$) : l'angle est constant, ce qui est la propriété caractéristique de l'hélice (pente constante).


**q4.** (d) Montrer que, si le mouvement est uniforme, la norme du vecteur vitesse $\|\vec v\|$ est constante et que le vecteur accélération passe par l'axe du cylindre et est parallèle au plan $Oxy$.

> [!tip]- 💡 Coup de pouce
> Mouvement uniforme signifie $\|\vec v\|=$ cte. Que cela impose-t-il à $\dot\theta$, puis à $\ddot\theta$ ? Reportez dans $\vec a$.


> [!success]- ✅ Correction
> $\|\vec v\|=|\dot\theta|\sqrt{a^2+h^2}$ constante $\Rightarrow\dot\theta$ constant $\Rightarrow\ddot\theta=0$ et $\vec a=-a\dot\theta^2\,\vec u_r$ : horizontal, dirigé vers l'axe $Oz$.


> [!example]- 📝 Solution détaillée
> **(d) Norme constante**
>
> Le mouvement est uniforme lorsque $\|\vec v\|$ est constante. Comme $\|\vec v\|=|\dot\theta|\sqrt{a^2+h^2}$ avec $a^2+h^2$ constant et non nul, cela équivaut à $|\dot\theta|=$ cte, donc à $\dot\theta=\omega$ constant et $\ddot\theta=0$. Réciproquement, $\dot\theta$ constant donne $\|\vec v\|$ constante : on a l'équivalence.
>
> **(d) Accélération**
>
> Avec $\ddot\theta=0$, l'expression de la question (b) se réduit à
> $$\boxed{\vec a=-a\omega^2\,\vec u_r},\qquad\|\vec a\|=a\omega^2.$$
> $\vec a$ n'a pas de composante selon $\vec k$ : il est **parallèle au plan $Oxy$**. Il est dirigé selon $-\vec u_r$, c'est-à-dire de $M$ vers le point $(0,0,z)$ de l'axe $Oz$ situé à la même altitude : la droite d'action de $\vec a$ **coupe l'axe du cylindre**, perpendiculairement à celui-ci. On retrouve l'accélération centripète du mouvement circulaire de rayon $a$ : monter à vitesse verticale constante ($\dot z=h\omega$) n'ajoute aucune accélération.


> [!note]- 🔗 Liens avec d'autres disciplines
> **Mathématiques (géométrie différentielle)**
>
> L'hélice est la courbe de l'espace de courbure et de torsion constantes. Elle se déroule en une droite sur le cylindre : on utilise la notion de longueur d'arc et de développable.
>
> **Électromagnétisme**
>
> Une particule chargée dans un champ magnétique uniforme décrit une hélice autour des lignes de champ (aurores polaires, cyclotron, tokamak) : $a$ est le rayon de Larmor et le pas dépend de la vitesse parallèle à $\vec B$.
>
> **Biologie et chimie**
>
> La double hélice de l'ADN a un rayon d'environ $1$ nm et un pas d'environ $3{,}4$ nm : $h=\dfrac{3{,}4}{2\pi}\approx0{,}54$ nm, soit $\tan\alpha=h/a\approx0{,}54$ et $\alpha\approx28^\circ$.
>
> **Mécanique et technologie**
>
> Une vis ou un tire-bouchon transforme une rotation en translation avec le **pas** $2\pi h$. L'angle d'hélice d'un filetage ou d'un engrenage hélicoïdal est défini par $\tan\alpha=h/a$.


> [!question]- 🔭 Aller plus loin — Licence : Courbure et torsion de l'hélice
> Pour un mouvement uniforme, l'accélération est normale : $\|\vec a\|=v^2/\rho$ donne le **rayon de courbure** $\rho=\dfrac{a^2+h^2}{a}$ (qui vaut $a$ pour $h=0$, le cercle, et tend vers l'infini quand $a\to0$ ou $h\to\infty$, la droite). La **torsion** de l'hélice, mesurant son écart au plan, vaut $\dfrac{h}{a^2+h^2}$. Une hélice a donc une courbure et une torsion constantes.


> [!question]- 🔭 Aller plus loin — Master : Particule chargée dans un champ magnétique uniforme
> Une particule de charge $q$ et de masse $m$ dans un champ $\vec B=B\,\vec k$ avec une vitesse $v_\perp$ perpendiculaire et $v_\parallel$ parallèle à $\vec B$ décrit une hélice d'axe $\vec B$, de rayon $a=\dfrac{mv_\perp}{|q|B}$, de pulsation $\omega_c=\dfrac{|q|B}m$ et de pas $2\pi\dfrac{v_\parallel}{\omega_c}$. Identifier les paramètres $a$ et $h=v_\parallel/\omega_c$ de l'exercice, et expliquer le guidage des particules chargées le long des lignes de champ (aurores polaires, confinement magnétique).


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex2-seance-1-exploitation-de-la-chronophotographie-vitesses-forces-lois-de-newton|Exercice 2 — Séance 1 -- Exploitation de la chronophotographie : vitesses, forces, lois de Newton]]

