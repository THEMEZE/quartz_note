---
title: "Exercice 8 — Ellipse de Kepler, loi des aires et hodographe"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · <a href="/pdfs/td2_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td2_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 8. Ellipse de Kepler, loi des aires et hodographe *(facultatif)*

*Difficulté ●●●●● · ⏱ 50 min · Type : Approfondissement / Problème de synthèse*

Une planète $M$ décrit, autour du Soleil placé en $O$ (foyer de l'orbite), une ellipse d'équation polaire
$$r(\theta)=\frac p{1+e\cos\theta},\qquad0\le e<1,$$
où $p$ (le **paramètre**) et $e$ (l'**excentricité**) sont des constantes. Le mouvement est tel que la quantité
$$C=r^2\dot\theta$$
(la **constante des aires**) est conservée. On se place dans la base polaire $(\vec u_r,\vec u_\theta)$ et on note
$\vec u_y$ le vecteur fixe de l'axe $Oy$ (perpendiculaire à l'axe focal $Ox$). Le but est de déterminer toute la
cinématique de ce mouvement **sans aucune hypothèse sur les forces** : on retrouvera la loi de la force.


> [!question]- 🪝 Accroche
> **La vitesse d'une planète dessine un cercle**
>
> *Durée de l'introduction : 3 à 5 min, avant de lire l'énoncé*
>
> *Une planète décrit une ellipse. Si l'on reporte, à partir d'un même point, les vecteurs vitesse successifs, quelle courbe trace leur extrémité ? Une ellipse comme l'orbite ? Autre chose ? Newton a retrouvé la loi de la gravitation à partir de l'ellipse de Kepler : peut-on faire de même avec de la seule cinématique ?*
>
> **Idée clé : la loi des aires $r^2\dot\theta=C$ remplace une loi de force.** Elle donne $\dot\theta=C/r^2$, donc $\dot r=\dfrac{\mathrm dr}{\mathrm d\theta}\dfrac C{r^2}$ et $r\dot\theta=\dfrac Cr$. Avec $r=p/(1+e\cos\theta)$ : $\dot r=\dfrac{Ce}p\sin\theta$ et $r\dot\theta=\dfrac Cp(1+e\cos\theta)$. Le vecteur vitesse s'écrit alors
> $$\vec v=\frac Cp\left(\vec u_\theta+e\,\vec u_y\right).$$




> [!abstract]- 🧠 À savoir avant
> **Accélération en base polaire**
>
> $\vec a=(\ddot r-r\dot\theta^2)\,\vec u_r+\dfrac1r\dfrac{\mathrm d}{\mathrm dt}\left(r^2\dot\theta\right)\vec u_\theta$, avec $\dfrac{\mathrm d\vec u_\theta}{\mathrm dt}=-\dot\theta\,\vec u_r$.
>
> **Dérivée de $1/(1+e\cos\theta)$**
>
> $\dfrac{\mathrm d}{\mathrm d\theta}\left(\dfrac p{1+e\cos\theta}\right)=\dfrac{p\,e\sin\theta}{(1+e\cos\theta)^2}$. Avec $r=\dfrac p{1+e\cos\theta}$ : $\dfrac{\mathrm dr}{\mathrm d\theta}=\dfrac{r^2}p\,e\sin\theta$.
>
> **Composantes de $\vec u_y$ dans la base polaire**
>
> $\vec u_y=\sin\theta\,\vec u_r+\cos\theta\,\vec u_\theta$ (projeter $\vec u_y$ sur $\vec u_r$ et $\vec u_\theta$).




> [!info]- 🎯 Ce que tu sauras faire
> **Retrouver les lois de Kepler par la cinématique seule**
>
> Savoir montrer que $r^2\dot\theta=$ cte équivaut à une accélération radiale, calculer $\vec v$ le long de l'ellipse, reconnaître que son extrémité décrit un **cercle** (hodographe), en déduire $\vec a$ en $1/r^2$, les vitesses extrêmes aux apsides et la période, avec une application à la Terre.




> [!tip]- 📖 Rappel de cours
> **Loi des aires**
>
> $a_\theta=\dfrac1r\dfrac{\mathrm d}{\mathrm dt}(r^2\dot\theta)$ : l'accélération est **radiale** ($a_\theta=0$) si et seulement si $C=r^2\dot\theta$ est constante. L'aire balayée par le rayon vecteur par unité de temps est $\dfrac{\mathrm dA}{\mathrm dt}=\dfrac12r^2\dot\theta=\dfrac C2$ (**vitesse aréolaire**).
>
> **Hodographe**
>
> L'**hodographe** est la courbe décrite par l'extrémité du vecteur vitesse quand on le reporte à partir d'un point fixe. Pour le mouvement circulaire uniforme, c'est un cercle ; pour une ellipse de Kepler, c'est aussi un cercle, mais **non centré** sur l'origine.




> [!note]- 🧮 Outils mathématiques
> **Dérivée composée sur une courbe polaire**
>
> $\dot r=\dfrac{\mathrm dr}{\mathrm d\theta}\,\dot\theta$ et $\ddot\theta$ se déduit de $r^2\dot\theta=C$ par $\dfrac{\mathrm d}{\mathrm dt}$.
>
> **Équation d'un cercle**
>
> L'ensemble des points $(v_x,v_y)$ tels que $v_x^2+(v_y-v_c)^2=\rho_h^2$ est un cercle de centre $(0,v_c)$ et de rayon $\rho_h$. Pour l'hodographe : $v_c=\dfrac{Ce}p$ et $\rho_h=\dfrac Cp$.
>
> **Propriétés de l'ellipse**
>
> Périhélie $r_{\min}=\dfrac p{1+e}$ ($\theta=0$), aphélie $r_{\max}=\dfrac p{1-e}$ ($\theta=\pi$), demi-grand axe $a=\dfrac p{1-e^2}$, demi-petit axe $b=\dfrac p{\sqrt{1-e^2}}$, aire $\pi ab$, et $b^2=ap$.
>
> **Norme d'un vecteur dans la base polaire**
>
> $\|\vec v\|^2=v_r^2+v_\theta^2=\left(\dfrac Cp\right)^2\left[e^2\sin^2\theta+(1+e\cos\theta)^2\right]=\left(\dfrac Cp\right)^2\left(1+2e\cos\theta+e^2\right)$.
>
> **Dérivée d'un vecteur unitaire tournant**
>
> $\dfrac{\mathrm d\vec u_\theta}{\mathrm dt}=-\dot\theta\,\vec u_r$ et $\dfrac{\mathrm d\vec u_y}{\mathrm dt}=\vec0$ (vecteur fixe).



**q1.** (a) Montrer que $a_\theta=\dfrac1r\dfrac{\mathrm d}{\mathrm dt}(r^2\dot\theta)$. En déduire que la loi des aires $r^2\dot\theta=C$ est équivalente au fait que l'accélération est **radiale** (dirigée selon $\vec u_r$).

(b) Exprimer la vitesse aréolaire $\dfrac{\mathrm dA}{\mathrm dt}$ en fonction de $C$.


> [!tip]- 💡 Coup de pouce
> Développez $\dfrac{\mathrm d}{\mathrm dt}(r^2\dot\theta)=2r\dot r\dot\theta+r^2\ddot\theta$ et comparez avec $r\,a_\theta=r^2\ddot\theta+2r\dot r\dot\theta$. L'aire élémentaire balayée est le secteur de rayon $r$ et d'angle $\mathrm d\theta$.




> [!success]- ✅ Correction
> $\dfrac1r\dfrac{\mathrm d}{\mathrm dt}(r^2\dot\theta)=2\dot r\dot\theta+r\ddot\theta=a_\theta$, donc $a_\theta=0\iff r^2\dot\theta=$ cte. $\dfrac{\mathrm dA}{\mathrm dt}=\dfrac12r^2\dot\theta=\dfrac C2$.




> [!example]- 📝 Solution détaillée
> **(a) Composante orthoradiale de l'accélération**
>
> $\dfrac1r\dfrac{\mathrm d}{\mathrm dt}\left(r^2\dot\theta\right)=\dfrac1r\left(2r\dot r\dot\theta+r^2\ddot\theta\right)=2\dot r\dot\theta+r\ddot\theta=a_\theta$. Donc
> $$a_\theta=0\iff\frac{\mathrm d}{\mathrm dt}\left(r^2\dot\theta\right)=0\iff r^2\dot\theta=C.$$
> La loi des aires équivaut à $\vec a=a_r\,\vec u_r$ : l'accélération est **radiale** (« force centrale »). Réciproquement, tout mouvement dont l'accélération est radiale vérifie la loi des aires.
>
> **(b) Vitesse aréolaire**
>
> Pendant $\mathrm dt$, le rayon vecteur balaye un secteur d'angle $\mathrm d\theta=\dot\theta\,\mathrm dt$ et d'aire $\mathrm dA=\tfrac12r^2\,\mathrm d\theta$ :
> $$\boxed{\frac{\mathrm dA}{\mathrm dt}=\frac12r^2\dot\theta=\frac C2}.$$
> Le rayon vecteur balaye des aires égales en des temps égaux (deuxième loi de Kepler).



**q2.** (a) Pour l'ellipse $r=\dfrac p{1+e\cos\theta}$ avec $r^2\dot\theta=C$, calculer $\dot r$ et $r\dot\theta$ en fonction de $C$, $p$, $e$ et $\theta$.

(b) En déduire que $\vec v=\dfrac Cp\left(\vec u_\theta+e\,\vec u_y\right)$ et calculer $\|\vec v\|^2$.

(c) Montrer que l'hodographe est un cercle dont on précisera le centre et le rayon.


> [!tip]- 💡 Coup de pouce
> $\dot r=\dfrac{\mathrm dr}{\mathrm d\theta}\dot\theta=\dfrac{r^2}pe\sin\theta\cdot\dfrac C{r^2}$. Pour (d), écrivez $e\sin\theta\,\vec u_r+e\cos\theta\,\vec u_\theta$ avec $\vec u_y=\sin\theta\,\vec u_r+\cos\theta\,\vec u_\theta$. Pour (e), repérez les composantes cartésiennes de $\vec v$ avec $\vec u_\theta=(-\sin\theta,\cos\theta)$.




> [!success]- ✅ Correction
> $\dot r=\dfrac{Ce}p\sin\theta$, $r\dot\theta=\dfrac Cp(1+e\cos\theta)$ ; $\vec v=\dfrac Cp(\vec u_\theta+e\,\vec u_y)$, $\|\vec v\|^2=\left(\dfrac Cp\right)^2(1+2e\cos\theta+e^2)$ ; hodographe : cercle de centre $\dfrac{Ce}p\vec u_y$ et de rayon $\dfrac Cp$.




> [!example]- 📝 Solution détaillée
> **(c) Composantes de la vitesse**
>
> $\dot\theta=C/r^2$ donne $r\dot\theta=\dfrac Cr=\dfrac Cp(1+e\cos\theta)$. Et $\dot r=\dfrac{\mathrm dr}{\mathrm d\theta}\dot\theta=\dfrac{r^2e\sin\theta}p\cdot\dfrac C{r^2}$, soit
> $$\boxed{\dot r=\frac{Ce}p\sin\theta},\qquad\boxed{r\dot\theta=\frac Cp\,(1+e\cos\theta)}.$$
>
> **(d) Forme compacte de $\vec v$ et norme**
>
> $$\vec v=\frac Cp\left[e\sin\theta\,\vec u_r+(1+e\cos\theta)\,\vec u_\theta\right]=\frac Cp\left[\vec u_\theta+e\left(\sin\theta\,\vec u_r+\cos\theta\,\vec u_\theta\right)\right]=\boxed{\frac Cp\left(\vec u_\theta+e\,\vec u_y\right)}.$$
> $$\|\vec v\|^2=\left(\frac Cp\right)^2\left[e^2\sin^2\theta+(1+e\cos\theta)^2\right]=\boxed{\left(\frac Cp\right)^2\left(1+2e\cos\theta+e^2\right)}.$$
>
> **(e) Hodographe circulaire**
>
> $\vec v-\dfrac{Ce}p\,\vec u_y=\dfrac Cp\,\vec u_\theta$ avec $\|\vec u_\theta\|=1$ : la distance de l'extrémité de $\vec v$ au point $\dfrac{Ce}p\,\vec u_y$ vaut $\dfrac Cp$, constante. L'hodographe est donc un **cercle de centre $\dfrac{Ce}p\,\vec u_y$ et de rayon $\dfrac Cp$**. Comme $e<1$, l'origine est **à l'intérieur** du cercle (le vecteur vitesse ne s'annule jamais) ; pour $e=0$ (orbite circulaire), le cercle est centré sur l'origine : mouvement circulaire uniforme.



**q3.** (a) Calculer $\vec a=\dfrac{\mathrm d\vec v}{\mathrm dt}$ à partir de l'expression (d). Quelle est la loi de variation de $\|\vec a\|$ avec $r$ ? Dans quel sens la force s'exerce-t-elle ?

(b) Déterminer la vitesse aux deux apsides (périhélie $\theta=0$, aphélie $\theta=\pi$) et le rapport $v_{\max}/v_{\min}$. Vérifier avec la loi des aires.

(c) Application : pour la Terre, $e=0{,}0167$ et la vitesse orbitale moyenne vaut $29{,}8$ km/s. Estimer les vitesses au périhélie et à l'aphélie. (On pourra utiliser $v_{\max}v_{\min}=\left(\dfrac Cp\right)^2(1-e^2)$ et assimiler $\sqrt{v_{\max}v_{\min}}$ à la vitesse moyenne.)


> [!tip]- 💡 Coup de pouce
> $\vec u_y$ est fixe : seul $\vec u_\theta$ varie dans $\vec v$. Pour (g), $\cos\theta=\pm1$. Pour (h), $v_{\max}v_{\min}=\left(\dfrac Cp\right)^2(1+e)(1-e)$, puis résolvez avec $v_{\max}/v_{\min}=\dfrac{1+e}{1-e}$.




> [!success]- ✅ Correction
> $\vec a=-\dfrac{C^2}{p\,r^2}\vec u_r$ : attractive, en $1/r^2$. $v_{\max}=\dfrac Cp(1+e)$, $v_{\min}=\dfrac Cp(1-e)$ ; rapport $\dfrac{1+e}{1-e}$. Terre : $v_p\approx30{,}3$ km/s, $v_a\approx29{,}3$ km/s.




> [!example]- 📝 Solution détaillée
> **(f) Accélération**
>
> $\vec u_y$ est constant et $\dfrac{\mathrm d\vec u_\theta}{\mathrm dt}=-\dot\theta\,\vec u_r$, donc
> $$\vec a=\frac Cp\,\frac{\mathrm d\vec u_\theta}{\mathrm dt}=-\frac Cp\,\dot\theta\,\vec u_r=-\frac Cp\cdot\frac C{r^2}\,\vec u_r=\boxed{-\frac{C^2}{p\,r^2}\,\vec u_r}.$$
> L'accélération est bien radiale (cohérent avec (a)), **dirigée vers $O$** (force attractive) et proportionnelle à $1/r^2$ : on retrouve, par la seule cinématique, la loi de la gravitation de Newton. Par identification, la constante $C^2/p$ est égale à $\mathcal GM$ pour le champ de gravitation du Soleil.
>
> **(g) Vitesses aux apsides**
>
> $\|\vec v\|^2=\left(\dfrac Cp\right)^2(1+2e\cos\theta+e^2)$ est maximale pour $\theta=0$ et minimale pour $\theta=\pi$ :
> $$\boxed{v_{\max}=\frac Cp(1+e)},\qquad\boxed{v_{\min}=\frac Cp(1-e)},\qquad\frac{v_{\max}}{v_{\min}}=\frac{1+e}{1-e}.$$
> Contrôle avec la loi des aires : au périhélie $r_{\min}=\dfrac p{1+e}$ et $v=r\dot\theta=\dfrac C{r}$, soit $v_{\max}=\dfrac Cp(1+e)$ $\surd$ ; à l'aphélie $r_{\max}=\dfrac p{1-e}$, $v_{\min}=\dfrac Cp(1-e)$ $\surd$. Et $r_{\min}v_{\max}=r_{\max}v_{\min}=C$.
>
> **(h) Application numérique : la Terre**
>
> $\dfrac{v_{\max}}{v_{\min}}=\dfrac{1,0167}{0,9833}\approx1{,}034$. Avec $\sqrt{v_{\max}v_{\min}}=\dfrac Cp\sqrt{1-e^2}\approx29{,}8$ km/s et $\sqrt{1-e^2}\approx0{,}99986$ : $\dfrac Cp\approx29{,}8$ km/s. D'où
> $$v_{\max}\approx29{,}8\times1{,}0167\approx30{,}3\ \text{km/s},\qquad v_{\min}\approx29{,}8\times0{,}9833\approx29{,}3\ \text{km/s}.$$
> La vitesse de la Terre ne varie que de $3\,\%$ : l'orbite est quasi circulaire. En revanche, pour la comète de Halley ($e\approx0{,}967$), $\dfrac{v_{\max}}{v_{\min}}=\dfrac{1,967}{0,033}\approx60$ : la comète file au périhélie $60$ fois plus vite qu'à l'aphélie. **Validation** : les ordres de grandeur ($\sim30$ km/s) sont ceux connus de la Terre.




> [!note]- 🔗 Liens avec d'autres disciplines
> **Astronomie**
>
> Orbites des planètes et des comètes (la comète de Halley a $e\approx0{,}967$), satellites artificiels (orbites de transfert), lois de Kepler.
>
> **Physique : mécanique analytique**
>
> Le problème de Kepler est le prototype des mouvements à force centrale, avec deux constantes : $C$ (moment cinétique par unité de masse) et l'énergie. L'hodographe circulaire est la signature de la **symétrie cachée** du problème de Kepler (vecteur de Runge--Lenz).
>
> **Histoire des sciences**
>
> Kepler obtient ses lois en 1609-1619 à partir des mesures de Tycho Brahe ; Newton les relie à la gravitation en 1687 (Principia). L'hodographe est introduit par Hamilton (1846) comme outil de démonstration élégant.




> [!question]- 🔭 Aller plus loin — Licence : Troisième loi de Kepler
> Avec $C^2=\mathcal G M\,p$ (constante de la force), l'aire de l'ellipse est $\pi ab$ avec $b^2=ap$ ; la loi des aires donne $T=\dfrac{2\pi ab}C$. En déduire $\dfrac{T^2}{a^3}=\dfrac{4\pi^2}{\mathcal GM}$.




> [!question]- 🔭 Aller plus loin — Master : Les trois types de coniques et l'énergie
> Pour $e=1$ (parabole) et $e>1$ (hyperbole), le même calcul donne $\vec v=\dfrac Cp(\vec u_\theta+e\,\vec u_y)$. Montrer que l'hodographe est alors un cercle **passant par $O$** ($e=1$) ou **entourant l'origine** ($e<1$), et que l'origine est **extérieure** au cercle ($e>1$), ce qui permet de classer les trajectoires liées ou de diffusion.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex5-bille-sur-une-sphere-angle-de-decollage|Exercice 5 — (*) Bille sur une sphère : angle de décollage]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex3-vitesse-et-acceleration-en-coordonnees-polaires|Exercice 3 — Vitesse et accélération en coordonnées polaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex2-seance-1-exploitation-de-la-chronophotographie-vitesses-forces-lois-de-newton|Exercice 2 — Séance 1 -- Exploitation de la chronophotographie : vitesses, forces, lois de Newton]]


