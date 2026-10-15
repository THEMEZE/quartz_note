---
title: "Exercice 1 — Mouvement à 2 dimensions"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td1_PhV111_corrige.pdf) · [📄 Énoncé](/pdfs/td1_PhV111_enonces.pdf) · [📄 Aides](/pdfs/td1_PhV111_aides.pdf) · [📄 Fiche enseignant](/pdfs/td1_PhV111_fiche.pdf)

### Exercice 1. Mouvement à 2 dimensions

Un point matériel $M$ se déplace dans le plan $xOy$. Son vecteur position $\overrightarrow{OM}$
suit la loi horaire :
$$\overrightarrow{OM}(t) = a\,t\,\vec{u}_x - b\,t^2\,\vec{u}_y \qquad \text{avec } a,\, b \text{ constantes}.$$

**q1.** Équations horaires et trajectoire de $M$.


(a) Quelles sont les dimensions des constantes $a$ et $b$ ?

(b) Donner l'expression des équations horaires $x(t)$ et $y(t)$ de $M$.

(c) Déterminer l'équation de la trajectoire $y(x)$ de $M$. De quelle courbe s'agit-il ?

(d) Représenter graphiquement la trajectoire de $M$, en prenant $a = 4\times10^{-2}$ S.I. et $b = 8\times10^{-2}$ S.I.

(e) Préciser sur le graphique la position de $M$ aux instants $t_0=0$ s, $t_1=0{,}1$ s, $t_2=0{,}2$ s, $t_3=0{,}3$ s, $t_4=0{,}4$ s, $t_5=0{,}5$ s, $t_{10}=1$ s.

(f) Que peut-on dire du mouvement de $M$ suivant $Ox$ ? suivant $Oy$ ?

> [!tip]- 💡 Coup de pouce
> Pour la trajectoire, isolez $t$ dans $x(t)$ et substituez dans $y(t)$. Pour la nature du mouvement sur chaque axe, regardez si la coordonnée est linéaire ou quadratique en $t$.


> [!success]- ✅ Correction
> $y(x) = -\dfrac{b}{a^2}x^2$ : parabole. Suivant $Ox$ : uniforme. Suivant $Oy$ : uniformément accéléré, parti du repos.


> [!example]- 📝 Solution détaillée
> **(a) Analyse dimensionnelle**
>
> $\overrightarrow{OM}$ est une longueur, donc chaque terme du membre de droite doit être une longueur. Puisque $a\,t$ est une longueur et $t$ est un temps, $a$ a la dimension d'une vitesse : $[a] = \mathrm{L}\cdot\mathrm{T}^{-1}$. De même $b\,t^2$ est une longueur, donc $b$ a la dimension d'une accélération : $[b] = \mathrm{L}\cdot\mathrm{T}^{-2}$.
>
> **(b) Équations horaires**
>
> En projetant $\overrightarrow{OM}(t)$ sur $(\vec u_x,\vec u_y)$ :
> $$\boxed{x(t) = a\,t}, \qquad \boxed{y(t) = -b\,t^2}.$$
>
> **(c) Équation de la trajectoire**
>
> De $x(t)=at$ on tire $t = x/a$. En reportant dans $y(t)=-bt^2$ :
> $$y(x) = -b\left(\frac{x}{a}\right)^2 = -\frac{b}{a^2}\,x^2.$$
> C'est l'équation d'une **parabole** passant par l'origine, d'axe de symétrie $Ox$... plus précisément d'axe vertical $Oy$ et de sommet $O$, tournée vers les $y$ négatifs (car $a,b>0$).
>
> **(d)-(e) Tracé et positions successives**
>
> Avec $a=4\times10^{-2}$ m/s et $b=8\times10^{-2}$ m/s$^2$, on a $b/a^2 = 0{,}08/(0{,}04)^2 = 50~\mathrm{m^{-1}}$, soit $y=-50\,x^2$ (en mètres). On calcule le tableau de positions :
>
> $$
> \begin{array}{c|ccccccc}
> t ~(s) &  0 & 0,1 & 0,2 & 0,3 & 0,4 & 0,5 & 1 \\
> \hline 
> x~ (m)  & 0  & 0,004  & 0,008  & 0,012  & 0,016  & 0,020  & 0,040 \\
> y~ (m)  & 0  & -0,0008  & -0,0032  & -0,0072  & -0,0128  & -0,020  & -0,080 
> \end{array}
> $$
>
> %| $t$ (s) | 0 | 0,1 | 0,2 | 0,3 | 0,4 | 0,5 | 1 |
> %|---|---|---|---|---|---|---|---|
> %| $x$ (m) | 0 | 0,004 | 0,008 | 0,012 | 0,016 | 0,020 | 0,040 |
> %| $y$ (m) | 0 | -0,0008 | -0,0032 | -0,0072 | -0,0128 | -0,020 | -0,080 |
>
> On reporte ces points sur le graphique $y(x)$ : ils s'accumulent près de l'origine puis s'écartent de plus en plus vite, la vitesse suivant $Oy$ augmentant avec $t$ (voir (f)).
>
> **(f) Nature du mouvement sur chaque axe**
>
> Suivant $Ox$ : $x(t)=at$ est **linéaire en $t$**, le mouvement est donc **rectiligne uniforme** de vitesse constante $a$.
>
> Suivant $Oy$ : $y(t)=-bt^2$ est **quadratique en $t$**, le mouvement est donc **rectiligne uniformément accéléré**, parti sans vitesse initiale ($\dot y(0)=0$) et d'accélération constante $\ddot y = -2b$.


**q2.** Vitesse et accélération de $M$.


(a) Rappeler l'expression du vecteur vitesse $\vec v$ et de la norme $\|\vec v\|$ en coordonnées cartésiennes, et les appliquer au cas présent.

(b) Rappeler l'expression du vecteur accélération $\vec a$ et de la norme $\|\vec a\|$ en coordonnées cartésiennes, et les appliquer au cas présent.

(c) Représenter sur le graphique la vitesse $\vec v$ et l'accélération $\vec a$ de $M$ à différents instants $t$ (choisir une échelle adéquate).

> [!tip]- 💡 Coup de pouce
> La base cartésienne étant fixe, il suffit de dériver composante par composante.


> [!success]- ✅ Correction
> $\vec v = a\,\vec u_x - 2bt\,\vec u_y$ ; $\vec a = -2b\,\vec u_y$ (constant).


> [!example]- 📝 Solution détaillée
> **(a) Vecteur vitesse**
>
> En base cartésienne fixe, $\vec v = \dot x\,\vec u_x + \dot y\,\vec u_y$, avec $\|\vec v\|=\sqrt{\dot x^2+\dot y^2}$. Ici :
> $$\boxed{\vec v(t) = a\,\vec u_x - 2b\,t\,\vec u_y}, \qquad \|\vec v(t)\| = \sqrt{a^2 + 4b^2t^2}.$$
>
> **(b) Vecteur accélération**
>
> De même $\vec a = \ddot x\,\vec u_x + \ddot y\,\vec u_y$, avec $\|\vec a\|=\sqrt{\ddot x^2+\ddot y^2}$. Ici :
> $$\boxed{\vec a(t) = -2b\,\vec u_y} \quad (\text{constant}), \qquad \|\vec a\| = 2b.$$
>
> **(c) Tracé**
>
> À chaque instant du tableau précédent, on trace en $M(t)$ le vecteur $\vec v(t)$ (composante $Ox$ constante $=a$, composante $Oy$ de plus en plus négative) et le vecteur $\vec a$ (toujours vertical, vers le bas, de norme constante $2b$). On observera que $\vec v$ devient de plus en plus incliné vers le bas au cours du temps, alors que $\vec a$ garde une direction et une norme fixes — cohérent avec un mouvement uniforme suivant $Ox$ et uniformément accéléré suivant $Oy$.


**q3.** Application : une mouette vole à une hauteur de 20 m au-dessus de la mer, en vol horizontal, à la vitesse de 36 km/h, lorsqu'elle laisse tomber un poisson.


(a) Faire un schéma en définissant un repère adapté.

(b) Calculer le temps nécessaire au poisson pour atteindre la surface de l'eau.

(c) Déterminer l'équation de la trajectoire.

> [!tip]- 💡 Coup de pouce
> Le poisson a, à l'instant où il est lâché, la même vitesse horizontale que la mouette et une vitesse verticale nulle : c'est un cas particulier du mouvement étudié en question 1, avec $a=v_0$ et $2b=g$.


> [!success]- ✅ Correction
> $t_{chute} \approx 2{,}0$ s ; $y(x) = -\dfrac{g}{2v_0^2}x^2$.


> [!example]- 📝 Solution détaillée
> **(a) Choix du repère**
>
> On choisit l'origine $O$ au point où le poisson est lâché, avec $\vec u_x$ horizontal dans le sens du vol, et $\vec u_y$ vertical ascendant. La surface de la mer correspond alors à l'ordonnée $y=-20$ m.
>
> **(b) Temps de chute**
>
> La vitesse horizontale $v_0 = 36~\text{km/h} = 10~\text{m/s}$ reste constante (pas de force horizontale), et le poisson est en chute libre verticale à partir d'une vitesse verticale nulle. On a donc, comme en question 1 mais avec $a=v_0=10$ m/s et $b=g/2$ :
> $$x(t) = v_0\,t, \qquad y(t) = -\frac{1}{2}g\,t^2.$$
> Le poisson atteint l'eau quand $y(t)=-20$ m, soit :
> $$t_{chute} = \sqrt{\frac{2\times 20}{g}} = \sqrt{\frac{40}{9{,}81}} \approx \boxed{2{,}0~\text{s}}.$$
>
> **(c) Équation de la trajectoire**
>
> Comme à la question 1(c), en éliminant $t = x/v_0$ :
> $$\boxed{y(x) = -\frac{g}{2v_0^2}\,x^2} = -\frac{9{,}81}{2\times 10^2}\,x^2 \approx -0{,}049\,x^2 \quad (\text{en mètres}).$$
> C'est une parabole, identique en nature à celle de la question 1 : la chute du poisson est un cas particulier du mouvement étudié plus haut.


**q4.** (*) Entraînement : refaire l'exercice pour $a=0$ et commenter.

> [!tip]- 💡 Coup de pouce
> Que devient $x(t)$ si $a=0$ ? Quelle est alors la trajectoire géométrique du point ?


> [!success]- ✅ Correction
> Si $a=0$, le mouvement est purement rectiligne le long de $Oy$ (chute libre 1D), la « trajectoire parabolique » dégénère en un segment de droite.


> [!example]- 📝 Solution détaillée
> **Cas limite $a=0$**
>
> Avec $a=0$, on a $x(t)=0$ pour tout $t$ : le point reste sur l'axe $Oy$. La loi horaire devient $\overrightarrow{OM}(t) = -b\,t^2\,\vec u_y$, soit un **mouvement rectiligne** le long de $Oy$, uniformément accéléré, sans vitesse initiale.
>
> On retrouve ce résultat en particularisant la formule de la trajectoire $y(x)=-\frac{b}{a^2}x^2$ : quand $a\to 0$, la parabole devient infiniment "resserrée" autour de l'axe $Oy$, jusqu'à dégénérer en ce segment de droite lorsque $a=0$ exactement (la notion même d'équation $y(x)$ perd alors son sens, puisque $x$ ne varie plus). Physiquement, sans vitesse horizontale initiale, il n'y a plus de mouvement horizontal : on retrouve une simple chute libre verticale 1D, cas particulier (et plus simple) du mouvement à 2 dimensions étudié en question 1.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex6-parabole-de-s-rete-et-tir-sur-une-pente|Exercice 6 — Parabole de sûreté et tir sur une pente]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]]

