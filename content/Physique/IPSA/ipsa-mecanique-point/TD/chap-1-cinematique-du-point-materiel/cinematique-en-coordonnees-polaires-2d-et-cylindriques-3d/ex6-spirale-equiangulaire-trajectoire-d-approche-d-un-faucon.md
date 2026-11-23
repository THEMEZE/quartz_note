---
title: "Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · <a href="/pdfs/td2_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td2_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 6. Spirale équiangulaire (trajectoire d'approche d'un faucon) *(facultatif)*

*Difficulté ●●●●○ · ⏱ 40 min · Type : Entraînement / Approfondissement*

Un faucon vole dans un plan horizontal vers sa proie, immobile en $O$. Il garde la proie dans une direction
qui fait un **angle constant** avec sa vitesse. En coordonnées polaires centrées en $O$, sa trajectoire a pour
équation
$$r(\theta)=r_0\,\mathrm e^{-k\theta},\qquad k>0\ \text{constante},$$
(spirale **logarithmique** ou **équiangulaire**) et il la parcourt avec une vitesse angulaire constante
$\dot\theta=\omega>0$, $\theta(0)=0$.

> [!question]+ 🎣 Accroche
> **Pourquoi un faucon ne fonce-t-il pas en ligne droite ?**
>
> *Durée de l'introduction : 3 à 5 min, avant de lire l'énoncé*
>
> *Un faucon pèlerin s'approche de sa proie en spirale plutôt qu'en ligne droite : on explique cela par le fait qu'il garde la tête droite (pour une meilleure vision) et regarde la proie sous un angle constant. Quelle courbe obtient-on ? Combien de tours fait-il ? Le trajet est-il beaucoup plus long qu'une ligne droite ?*
>
> **Idée clé : trajectoire équiangulaire.** Une courbe polaire $r=r_0\mathrm e^{-k\theta}$ coupe tous les rayons issus de $O$ sous le même angle, et le rapport $\dot r/(r\dot\theta)=-k$ est constant. Si $\theta(t)$ est connu, $\dot r=-kr\dot\theta$ et
> $$\vec v=r\dot\theta\,(-k\,\vec u_r+\vec u_\theta).$$


> [!abstract]+ 📚 Prérequis
> **Accélération en base polaire**
>
> $a_r=\ddot r-r\dot\theta^2$ et $a_\theta=r\ddot\theta+2\dot r\dot\theta$.
>
> **Composantes tangentielle et normale**
>
> $a_t=\dfrac{\mathrm dv}{\mathrm dt}$ (variation de la norme de la vitesse) et $a_n=\sqrt{a^2-a_t^2}=\dfrac{v^2}{\rho}$ (changement de direction), $\rho$ étant le rayon de courbure.
>
> **Intégrale d'une exponentielle**
>
> $\displaystyle\int_0^\infty\mathrm e^{-\lambda t}\,\mathrm dt=\frac1\lambda$ pour $\lambda>0$.


> [!info]+ 🎯 Objectifs
> **Exploiter une trajectoire donnée en $r(\theta)$ et une loi horaire $\theta(t)$**
>
> Obtenir $r(t)$ à partir de $r(\theta)$, calculer $\vec v$ et $\vec a$, mesurer l'angle entre la vitesse et le rayon vecteur, décomposer l'accélération en parties tangentielle et normale, et calculer une longueur parcourue **finie** en un temps infini.


> [!note]+ 📖 Point de cours
> **Spirale logarithmique**
>
> Pour $r=r_0\mathrm e^{-k\theta}$ : $\dfrac{\mathrm dr}{\mathrm d\theta}=-kr$, donc la pente $\dfrac{\mathrm dr}{r\,\mathrm d\theta}=-k$ est **constante** : la tangente fait un angle constant avec le rayon vecteur en tout point (d'où « équiangulaire »). La courbe est invariante par similitude (rotation + homothétie).


> [!note]- 🧮 Outils mathématiques
> **Dérivation d'une exponentielle composée**
>
> $\dfrac{\mathrm d}{\mathrm dt}\mathrm e^{-k\omega t}=-k\omega\,\mathrm e^{-k\omega t}$, donc $\dot r=-k\omega r$ et $\ddot r=k^2\omega^2r$.
>
> **Angle entre deux vecteurs**
>
> $\cos\varphi=\dfrac{\vec A\cdot\vec B}{\|\vec A\|\,\|\vec B\|}$. Pour $\vec v=\omega r(-k,1)$ et $-\vec u_r=(-1,0)$ dans la base polaire : $\cos\gamma=\dfrac{k}{\sqrt{1+k^2}}$.
>
> **Accélération tangentielle**
>
> $a_t=\dfrac{\mathrm dv}{\mathrm dt}$ avec $v=\omega\sqrt{1+k^2}\,r$ : $a_t=\omega\sqrt{1+k^2}\,\dot r=-k\omega^2\sqrt{1+k^2}\,r$.
>
> **Longueur parcourue**
>
> $L=\displaystyle\int_0^\infty\|\vec v\|\,\mathrm dt$ : intégrale d'une exponentielle décroissante, qui converge.


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


> [!note]- 🔗 Liens avec d'autres disciplines
> **Biologie et éthologie**
>
> Approche en spirale des faucons pèlerins et des insectes vers une source lumineuse (mouvement à angle constant avec la direction de la source) ; coquilles de mollusques (nautile), tournesol.
>
> **Astronomie**
>
> Bras de galaxies spirales (spirales logarithmiques approchées) ; trajectoire d'un satellite qui perd lentement de l'altitude par frottements (spirale de décroissance quasi circulaire).
>
> **Mathématiques**
>
> Courbe de Bernoulli (« spira mirabilis »), invariance par similitude, nombres complexes : $z=r_0\mathrm e^{(-k+i)\theta}$.


> [!question]- 🔭 Aller plus loin — Licence : Choisir la loi horaire pour atteindre la proie en temps fini
> Avec la même trajectoire, quelle loi $\theta(t)$ faut-il imposer pour que la vitesse $\|\vec v\|$ soit **constante** ? Montrer qu'alors $r=r_0-v\sin\gamma\,t$ et que la proie est atteinte en un temps fini $T=r_0/(v\sin\gamma)$ (où $\gamma$ est l'angle de l'énoncé). C'est exactement le mouvement de l'exercice 7.


> [!question]- 🔭 Aller plus loin — Master : Similitudes et invariance d'échelle
> Montrer que la spirale logarithmique est invariante par la similitude $(r,\theta)\mapsto(\lambda r,\theta+\ln\lambda/k')$ avec $k'=-k$ choisi convenablement, et expliquer pourquoi cette propriété la rend « auto-similaire » (coquille de nautile, bras de galaxies spirales, cyclones).


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex5-bille-sur-une-sphere-angle-de-decollage|Exercice 5 — (*) Bille sur une sphère : angle de décollage]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex3-vitesse-et-acceleration-en-coordonnees-polaires|Exercice 3 — Vitesse et accélération en coordonnées polaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex2-seance-1-exploitation-de-la-chronophotographie-vitesses-forces-lois-de-newton|Exercice 2 — Séance 1 -- Exploitation de la chronophotographie : vitesses, forces, lois de Newton]]

