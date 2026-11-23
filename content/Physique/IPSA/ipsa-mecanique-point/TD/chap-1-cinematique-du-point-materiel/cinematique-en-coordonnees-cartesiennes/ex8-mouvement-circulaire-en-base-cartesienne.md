---
title: "Exercice 8 — Mouvement circulaire en base cartésienne"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · <a href="/pdfs/td1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td1_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/test.pdf" target="_blank" rel="noopener">📄 PDF</a> · <a href="/pdfs/td1_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 8. Mouvement circulaire en base cartésienne

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 35 min · Type : Application*

Un point matériel $M$ se déplace dans un plan muni d'un repère cartésien $(O,\vec\imath,\vec\jmath)$.
Son rayon vecteur $\vec r$ s'écrit en fonction du temps :
$$\vec r(t) = R\cos(\omega t)\,\vec\imath + R\sin(\omega t)\,\vec\jmath \qquad \text{avec } R,\,\omega \text{ constantes}.$$

> [!question]+ 🎣 Accroche
> **Accélérer sans aller plus vite**
>
> *Durée de l'introduction : 3 à 5 min, avant de lire l'énoncé*
>
> *Un manège tourne à vitesse constante. Vous sentez pourtant une « force » qui vous plaque vers l'extérieur. **Peut-on accélérer sans jamais aller plus vite ?** Et la Lune, qui tourne autour de la Terre à vitesse constante : est-elle ou non accélérée ?*
>
> **Idée clé : l'accélération change le vecteur vitesse, pas forcément sa norme.** La vitesse est un vecteur : si sa **direction** change, il y a accélération, même à norme constante. Pour un mouvement circulaire uniforme de rayon $R$ et de vitesse angulaire $\omega$ :
> $$\|\vec v\|=R\omega,\qquad \vec a=-\omega^2\,\vec r,\qquad \|\vec a\|=R\omega^2=\frac{v^2}{R}.$$
> L'accélération est **centripète** (dirigée vers le centre), perpendiculaire à $\vec v$ : elle ne fait que **courber** la trajectoire. Seule une composante **tangentielle** de l'accélération modifie la norme de la vitesse.


> [!abstract]+ 📚 Prérequis
> **Dérivation en base cartésienne fixe**
>
> La base $(\vec\imath,\vec\jmath)$ étant fixe (indépendante du temps), la dérivation d'un vecteur exprimé dans cette base se fait composante par composante, sans terme supplémentaire lié à la rotation de la base elle-même — contrairement à ce qui se passera en base polaire, étudiée plus tard dans le cours.


> [!info]+ 🎯 Objectifs
> **Retrouver le mouvement circulaire uniforme par le calcul cartésien**
>
> Savoir montrer, à partir des seules équations horaires cartésiennes, qu'un mouvement est circulaire et uniforme, et interpréter physiquement le fait que l'accélération puisse être non nulle alors que la norme de la vitesse est constante (accélération purement centripète).


> [!info]- 🧑‍🏫 Objectifs pédagogiques (enseignant)
> **Préparer la base polaire**
>
> Cet exercice, mené intégralement en coordonnées cartésiennes, est volontairement plus lourd en calcul qu'un traitement en base polaire (qui sera vu plus tard). L'objectif pédagogique est de faire ressentir cette lourdeur relative, pour motiver l'introduction des coordonnées polaires : ici, $\|\vec v\|$ et $\|\vec a\|$ constants n'apparaissent qu'après simplification trigonométrique, alors qu'ils seraient immédiats en base $(\vec u_r,\vec u_\theta)$.


> [!note]+ 📖 Point de cours
> **Identité trigonométrique fondamentale**
>
> Pour tout $\theta$, $\cos^2\theta + \sin^2\theta = 1$. C'est cette identité qui permet de retrouver l'équation d'un cercle à partir des équations horaires paramétriques, et de simplifier les normes de $\vec v$ et $\vec a$ dans cet exercice.


> [!note]- 🧮 Outils mathématiques
> **Identité fondamentale : $\cos^2\theta+\sin^2\theta=1$**
>
> Elle permet d'éliminer $t$ : $x^2+y^2=R^2$ (cercle), et de simplifier les normes : $\|\vec v\|^2=R^2\omega^2(\sin^2+\cos^2)=R^2\omega^2$.
>
> **Dérivées de $\cos(\omega t)$ et $\sin(\omega t)$ (dérivée composée)**
>
> $\dfrac{\mathrm d}{\mathrm dt}\cos(\omega t)=-\omega\sin(\omega t)$ et $\dfrac{\mathrm d}{\mathrm dt}\sin(\omega t)=\omega\cos(\omega t)$. Chaque dérivation multiplie par $\omega$ et fait « avancer » la phase de $\pi/2$ : $-\sin(\omega t)=\cos(\omega t+\tfrac\pi2)$.
>
> **Décalage de $\pi/2$ : $\cos(x+\tfrac\pi2)=-\sin x$ et $\sin(x+\tfrac\pi2)=\cos x$**
>
> Le vecteur $\vec v$ est le vecteur $\vec r$ tourné de $+90^\circ$ et multiplié par $\omega$ ; $\vec a$ est $\vec r$ tourné de $180^\circ$ (donc opposé) et multiplié par $\omega^2$.
>
> **Radian, période et vitesse angulaire**
>
> Un angle en radians vaut $\theta=\text{arc}/R$ ; un tour complet fait $2\pi$. D'où $\omega=2\pi/T=2\pi f$ et $v=R\omega$. Le radian est sans dimension, ce qui impose $[\omega]=\mathrm T^{-1}$.
>
> **Produit scalaire et orthogonalité**
>
> $\vec v\cdot\vec r=-R^2\omega\sin\cos+R^2\omega\sin\cos=0$ : la vitesse est perpendiculaire au rayon. Plus généralement, si $\|\vec v\|$ est constante, $\vec v\cdot\vec a=\tfrac12\dfrac{\mathrm d}{\mathrm dt}\|\vec v\|^2=0$.
>
> **Notation complexe (ouverture)**
>
> On peut écrire $x+iy=R\,e^{i\omega t}$. Dériver revient à multiplier par $i\omega$ (rotation de $90^\circ$ et facteur $\omega$) : on retrouve $\vec v$ et $\vec a=-\omega^2\vec r$ en une ligne.


**q1.** Équations horaires et trajectoire de $M$.


(a) Donner la dimension des constantes $R$ et $\omega$.

(b) Donner l'expression des équations horaires $x(t)$ et $y(t)$ de $M$.

(c) Déterminer l'équation de la trajectoire de $M$ (indication : calculer puis relier $x^2$ et $y^2$). De quelle courbe s'agit-il ?

(d) Représenter graphiquement la trajectoire de $M$, en prenant $R=4\times10^{-2}$ S.I. et $\omega=\pi/6$ S.I.

(e) Préciser sur le graphique la position de $M$ aux instants $t_0=0$ s, $t_1=1$ s, ..., $t_6=6$ s.

(f) Que peut-on dire du mouvement de $M$ ?

> [!tip]- 💡 Coup de pouce
> Utilisez $\cos^2+\sin^2=1$ pour éliminer $t$ entre $x(t)$ et $y(t)$.


> [!success]- ✅ Correction
> $x^2+y^2=R^2$ : cercle de rayon $R$ centré en $O$, parcouru à vitesse angulaire constante $\omega$ (mouvement circulaire uniforme).


> [!example]- 📝 Solution détaillée
> **(a) Dimensions**
>
> $\vec r(t)$ est une longueur, donc $R$ est une longueur : $[R]=\mathrm L$. L'argument $\omega t$ d'un cosinus/sinus doit être sans dimension (un angle, en radian), donc $\omega$ est l'inverse d'un temps : $[\omega]=\mathrm T^{-1}$ (homogène à une vitesse angulaire, en rad/s).
>
> **(b) Équations horaires**
>
> En projetant $\vec r(t)$ sur $(\vec\imath,\vec\jmath)$ :
> $$\boxed{x(t) = R\cos(\omega t)}, \qquad \boxed{y(t) = R\sin(\omega t)}.$$
>
> **(c) Équation de la trajectoire**
>
> On calcule $x^2(t) + y^2(t) = R^2\cos^2(\omega t) + R^2\sin^2(\omega t) = R^2\big(\cos^2(\omega t)+\sin^2(\omega t)\big) = R^2$, indépendamment de $t$. La trajectoire vérifie donc :
> $$\boxed{x^2+y^2=R^2},$$
> c'est l'équation d'un **cercle de rayon $R$ centré en $O$**.
>
> **(d)-(e) Tracé et positions successives**
>
> Avec $R=0{,}04$ m et $\omega=\pi/6$ rad/s (période $T=2\pi/\omega=12$ s), on calcule $\theta(t)=\omega t$ puis $x=R\cos\theta$, $y=R\sin\theta$ :
>
> $$
> \begin{array}{c|ccccccc}
>   t~ (s) & 0 & 1 & 2 & 3 & 4 & 5 & 6 \\
>   \hline 
>   \theta~ (^\circ) & 0 & 30 & 60 & 90 & 120 & 150 & 180 \\
>   x ~ (m) & 0,040 & 0,035 & 0,020 & 0 & -0,020 & -0,035 & -0,040 \\
>   y ~ (m) & 0 & 0,020 & 0,035 & 0,040 & 0,035 & 0,020 & 0
> \end{array}
> $$
>
> %| $t$ (s) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
> %|---|---|---|---|---|---|---|---|
> %| $\theta$ (°) | 0 | 30 | 60 | 90 | 120 | 150 | 180 |
> %| $x$ (m) | 0,040 | 0,035 | 0,020 | 0 | -0,020 | -0,035 | -0,040 |
> %| $y$ (m) | 0 | 0,020 | 0,035 | 0,040 | 0,035 | 0,020 | 0 |
>
> On place ces 7 points sur le cercle de rayon 0,04 m : ils sont **régulièrement espacés angulairement** (30° entre chaque, puisque $\Delta t=1$ s est constant et $\omega$ est constant), ce qui illustre visuellement le caractère uniforme du mouvement.
>
> **(f) Nature du mouvement**
>
> Le point $M$ décrit un **mouvement circulaire uniforme** : trajectoire circulaire de rayon $R$, parcourue à vitesse angulaire constante $\omega$ (le paramètre $\theta(t)=\omega t$ croît linéairement avec le temps).


**q2.** Vitesse et accélération de $M$.


(a) Déterminer l'expression du vecteur vitesse $\vec v$ de $M$ et de sa norme $\vert \vec v\vert$.

(b) Déterminer l'expression du vecteur accélération $\vec a$ de $M$ et de sa norme $\vert\vec a\vert$.

(c) Représenter sur le graphique la vitesse $\vec v$ et l'accélération $\vec a$ de $M$ aux instants $t_1$ et $t_3$ (échelle adéquate).

(d) En un point de la trajectoire, représenter la base cartésienne $(\vec u_x,\vec u_y)$ et faire apparaître les composantes de $\vec v$ et $\vec a$.

(e) Donner la définition d'un mouvement uniforme. Le mouvement de $M$ peut-il être uniforme si son accélération est non nulle ?

> [!tip]- 💡 Coup de pouce
> Dérivez composante par composante ; pour la norme, ressortez le facteur commun $R\omega$ (ou $R\omega^2$) avant d'utiliser $\cos^2+\sin^2=1$.


> [!success]- ✅ Correction
> $\vec v = -R\omega\sin(\omega t)\vec\imath + R\omega\cos(\omega t)\vec\jmath$, $\|\vec v\|=R\omega$ (constant). $\vec a = -\omega^2\vec r$, $\|\vec a\|=R\omega^2$ (constant). Oui, le mouvement est uniforme malgré $\vec a\neq\vec 0$ : l'accélération est purement centripète.


> [!example]- 📝 Solution détaillée
> **(a) Vecteur vitesse et sa norme**
>
> En dérivant $x(t)$ et $y(t)$ par rapport à $t$ (la base $(\vec\imath,\vec\jmath)$ étant fixe) :
> $$\boxed{\vec v(t) = -R\omega\sin(\omega t)\,\vec\imath + R\omega\cos(\omega t)\,\vec\jmath}.$$
> $$\|\vec v\|^2 = R^2\omega^2\sin^2(\omega t) + R^2\omega^2\cos^2(\omega t) = R^2\omega^2 \quad\Longrightarrow\quad \boxed{\|\vec v\| = R\omega} \ (\text{constant}).$$
>
> **(b) Vecteur accélération et sa norme**
>
> En dérivant à nouveau :
> $$\vec a(t) = -R\omega^2\cos(\omega t)\,\vec\imath - R\omega^2\sin(\omega t)\,\vec\jmath = -\omega^2\big(R\cos(\omega t)\,\vec\imath + R\sin(\omega t)\,\vec\jmath\big),$$
> soit :
> $$\boxed{\vec a(t) = -\omega^2\,\vec r(t)}.$$
> L'accélération est donc en permanence **colinéaire à $\vec r$ et de sens opposé** : elle pointe toujours vers le centre $O$ (accélération centripète). Sa norme :
> $$\boxed{\|\vec a\| = R\omega^2} \ (\text{constante}).$$
>
> **(c)-(d) Représentation graphique**
>
> Aux instants $t_1=1$ s ($\theta=30°$) et $t_3=3$ s ($\theta=90°$), on place $M$ sur le cercle, puis on trace $\vec v$ **tangent au cercle** (perpendiculaire à $\vec r$, dans le sens du mouvement, c'est-à-dire dans le sens trigonométrique ici car $\theta$ croît), et $\vec a$ **radial, pointant vers $O$**. En décomposant sur $(\vec u_x,\vec u_y)$ en un point quelconque, les composantes sont directement celles calculées en (a) et (b) : $v_x=-R\omega\sin\theta$, $v_y=R\omega\cos\theta$, $a_x=-R\omega^2\cos\theta$, $a_y=-R\omega^2\sin\theta$.
>
> **(e) Mouvement uniforme et accélération non nulle**
>
> Un mouvement est dit **uniforme** lorsque la norme du vecteur vitesse (la vitesse "scalaire", ou célérité) est **constante au cours du temps** — ce qui ne préjuge en rien de la direction de $\vec v$, ni de l'accélération.
>
> Ici, on a montré en (a) que $\|\vec v\|=R\omega$ est bien constant : le mouvement circulaire est donc **uniforme**, bien que $\vec a\neq\vec 0$ (question (b)). Ceci est possible car l'accélération est ici **purement radiale (centripète)**, donc perpendiculaire à $\vec v$ à chaque instant : elle ne fait que courber la trajectoire (faire tourner la direction de $\vec v$) sans jamais modifier sa norme. On retiendra que : **accélération non nulle n'implique pas mouvement non uniforme** — seule une composante d'accélération tangentielle (colinéaire à $\vec v$) modifie la norme de la vitesse.


**q3.** Application : le mouvement de révolution de la Lune autour de la Terre s'accomplit en 28 jours sur une trajectoire assimilée à un cercle, parcourue de façon uniforme.


(a) Quelle est la vitesse angulaire du mouvement de révolution de la Lune ?

(b) Quelle serait la vitesse angulaire si soudainement la vitesse (linéaire) était réduite de moitié et si le rayon de l'orbite quadruplait ?

> [!tip]- 💡 Coup de pouce
> Utilisez $\omega = v/R$ (issu de $v=R\omega$, question 2a) pour la question (b).


> [!success]- ✅ Correction
> $\omega \approx 2{,}6\times10^{-6}$ rad/s ; $\omega' = \omega/8$.


> [!example]- 📝 Solution détaillée
> **(a) Vitesse angulaire de la Lune**
>
> La période de révolution est $T = 28$ jours $= 28\times 24\times3600 = 2\,419\,200$ s. Comme le mouvement est circulaire uniforme, $\omega = 2\pi/T$ (l'angle balayé pendant une période complète est $2\pi$) :
> $$\omega = \frac{2\pi}{2\,419\,200} \approx \boxed{2{,}60\times10^{-6}~\text{rad/s}}.$$
>
> **(b) Nouvelle vitesse angulaire après modification de $v$ et $R$**
>
> D'après la question 2(a), $v = R\omega$, donc $\omega = v/R$. Si la vitesse est divisée par 2 ($v' = v/2$) et le rayon multiplié par 4 ($R' = 4R$), la nouvelle vitesse angulaire vaut :
> $$\omega' = \frac{v'}{R'} = \frac{v/2}{4R} = \frac{1}{8}\cdot\frac{v}{R} = \boxed{\frac{\omega}{8}} \approx 3{,}25\times10^{-7}~\text{rad/s}.$$
> La vitesse angulaire est donc divisée par 8 : elle est affectée à la fois par la réduction de la vitesse linéaire (facteur $1/2$) et par l'augmentation du rayon (facteur $1/4$ supplémentaire), les deux effets se cumulant pour ralentir la rotation.


> [!warning]- 🪤 Écueils classiques
> **Croire qu'accélération non nulle implique mouvement non uniforme**
>
> Erreur fréquente : penser que si $\vec a \neq \vec 0$, la vitesse (en norme) doit varier. Il est essentiel de bien distinguer variation de la **direction** du vecteur vitesse (qui nécessite une accélération, même à norme constante) et variation de sa **norme** (qui nécessite spécifiquement une composante d'accélération tangentielle à la trajectoire). Ici $\vec a$ est purement radiale (centripète), donc ne modifie que la direction de $\vec v$, jamais sa norme.


> [!tip]- 🎙️ Conseils d'animation
> **Faire deviner la nature du mouvement avant de calculer**
>
> Avant de faire calculer $x^2+y^2$, demander aux étudiants ce que suggère la forme de $\vec r(t)$ (avec $\cos$ et $\sin$ du même argument $\omega t$) : beaucoup reconnaîtront intuitivement un mouvement circulaire, ce qui rend le calcul de vérification plus motivé.


> [!note]- 🔗 Liens avec d'autres disciplines
> **Mathématiques**
>
> Cercle trigonométrique, nombres complexes $e^{i\theta}$, équation $x^2+y^2=R^2$.
>
> **Oscillateurs et ondes**
>
> Projeter un mouvement circulaire uniforme sur un axe donne $x=R\cos\omega t$ : un **mouvement sinusoïdal**, qui vérifie $\ddot x=-\omega^2x$, l'équation de l'oscillateur harmonique (ressort, pendule, circuit LC).
>
> **Électricité**
>
> Une tension alternative $u=U_m\cos\omega t$ est la projection d'un vecteur tournant (diagramme de Fresnel / phaseur) : c'est la même mathématique.
>
> **Astronomie**
>
> Orbites quasi circulaires de la Lune et des satellites, troisième loi de Kepler $T^2\propto R^3$.


> [!success]- 🏁 Bilan
> **Signature du mouvement circulaire uniforme**
>
> Le mouvement circulaire uniforme est caractérisé par une vitesse angulaire $\omega$ constante, une vitesse (en norme) constante $v=R\omega$, et une accélération purement centripète de norme constante $a=R\omega^2=v^2/R$, dirigée en permanence vers le centre $O$. Cette structure ($\vec a = -\omega^2\vec r$) reviendra très souvent en physique (oscillateur harmonique, force centrale, etc.).


> [!question]- 🔭 Aller plus loin — CPGE : Passage en coordonnées polaires
> On pourra reprendre entièrement cet exercice en base polaire $(\vec u_r,\vec u_\theta)$, avec $\theta(t)=\omega t$, et comparer la longueur des calculs : $\vec v = R\dot\theta\,\vec u_\theta$ et $\vec a = -R\dot\theta^2\,\vec u_r$ s'obtiennent alors directement, sans développement trigonométrique, ce qui illustre l'intérêt de choisir un système de coordonnées adapté à la symétrie du problème.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex2-seance-1-exploitation-de-la-chronophotographie-vitesses-forces-lois-de-newton|Exercice 2 — Séance 1 -- Exploitation de la chronophotographie : vitesses, forces, lois de Newton]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]]

