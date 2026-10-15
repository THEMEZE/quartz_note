---
title: "Exercice 8 — Ellipse de Kepler, loi des aires et hodographe"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td2_PhV111_corrige.pdf) · [📄 Énoncé](/pdfs/td2_PhV111_enonces.pdf) · [📄 Aides](/pdfs/td2_PhV111_aides.pdf) · [📄 Fiche enseignant](/pdfs/td2_PhV111_fiche.pdf)

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


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]]

