---
title: "Exercice 5 — Perle sur une tige tournante"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/index|⬅ Retour]] · <a href="/pdfs/td2_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td2_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td2_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 5. Perle sur une tige tournante *(facultatif)*

Dans un plan horizontal, une tige rectiligne $OA$ tourne autour de $O$ à vitesse angulaire **constante**
$\omega$ : l'angle $\theta$ entre $Ox$ et la tige vaut $\theta(t)=\omega t$. Une petite perle $M$ coulisse sur la
tige ; sa position est repérée par $r(t)=OM$. On étudie deux mouvements de la perle sur la tige :


- **cas A** : la perle est entraînée à vitesse radiale constante $u$ à partir de $O$, soit $r(t)=ut$ ;
- **cas B** : la perle est **libre** sur une tige lisse : la tige ne peut exercer sur elle qu'une action perpendiculaire à la tige, donc l'accélération n'a **aucune composante radiale**, $a_r=0$. La perle est lâchée à $r(0)=r_0$ avec $\dot r(0)=0$.

**q1.** **Cas A : $r(t)=ut$, $\theta(t)=\omega t$.**


(a) Déterminer l'équation polaire $r(\theta)$ de la trajectoire et la nommer. Quel est l'écart radial entre deux tours successifs ?

(b) Calculer $\vec v$ et $\vec a$ dans la base polaire, puis leurs normes. Identifier dans $\vec a$ le terme centripète et le terme de Coriolis.

> [!tip]- 💡 Coup de pouce
> Éliminez $t=\theta/\omega$ dans $r=ut$. Pour $\vec a$, utilisez $a_r=\ddot r-r\dot\theta^2$ et $a_\theta=r\ddot\theta+2\dot r\dot\theta$ avec $\ddot r=0$ et $\ddot\theta=0$.


> [!success]- ✅ Correction
> (a) $r=u\theta/\omega$, spirale d'Archimède, écart $2\pi u/\omega$. (b) $\vec v=u\,\vec u_r+u\omega t\,\vec u_\theta$, $\|\vec v\|=u\sqrt{1+\omega^2t^2}$ ; $\vec a=-u\omega^2t\,\vec u_r+2u\omega\,\vec u_\theta$, $\|\vec a\|=u\omega\sqrt{4+\omega^2t^2}$.


> [!example]- 📝 Solution détaillée
> **(a) Trajectoire**
>
> $t=\theta/\omega$ donne $\boxed{r=\dfrac u\omega\,\theta}$ : c'est une **spirale d'Archimède**. Entre $\theta$ et $\theta+2\pi$, $r$ augmente de $2\pi u/\omega$ : les spires sont **régulièrement espacées**.
>
> **(b) Vitesse**
>
> $\dot r=u$ et $r\dot\theta=ut\cdot\omega$ :
> $$\boxed{\vec v=u\,\vec u_r+u\omega t\,\vec u_\theta},\qquad\|\vec v\|=u\sqrt{1+\omega^2t^2}.$$
>
> **(b) Accélération**
>
> $a_r=\ddot r-r\dot\theta^2=-u\omega^2t$ et $a_\theta=r\ddot\theta+2\dot r\dot\theta=2u\omega$ :
> $$\boxed{\vec a=-u\omega^2t\,\vec u_r+2u\omega\,\vec u_\theta},\qquad\|\vec a\|=u\omega\sqrt{4+\omega^2t^2}.$$
> Le terme $-u\omega^2t\,\vec u_r=-r\omega^2\vec u_r$ est l'accélération **centripète** ; le terme $2u\omega\,\vec u_\theta=2\dot r\dot\theta\,\vec u_\theta$ est l'accélération **de Coriolis**. Ce dernier existe même si la vitesse radiale est constante et la rotation uniforme.


**q2.** (a) Calculer l'angle $\beta$ entre $\vec v$ et la tige. Que devient-il quand $t\to\infty$ ?

(b) Calculer le rayon de courbure $\rho(t)$ de la trajectoire. Donner sa valeur en $t=0$ et son comportement aux temps longs. Commenter.

> [!tip]- 💡 Coup de pouce
> $\tan\beta=r\dot\theta/\dot r$. Pour $\rho$, calculez $v_ra_\theta-v_\theta a_r$ avec les composantes de la question (b).


> [!success]- ✅ Correction
> $\tan\beta=\omega t\to\infty$ donc $\beta\to\pi/2$. $\rho=\dfrac u\omega\dfrac{(1+\omega^2t^2)^{3/2}}{2+\omega^2t^2}$ ; $\rho(0)=\dfrac u{2\omega}$ ; $\rho\sim ut=r$ aux temps longs (la spirale ressemble à un cercle).


> [!example]- 📝 Solution détaillée
> **(c) Angle avec la tige**
>
> $\tan\beta=\dfrac{u\omega t}{u}=\omega t$. En $t=0$ la vitesse est radiale ($\beta=0$). Quand $t\to\infty$, $\beta\to\pi/2$ : la vitesse devient presque orthoradiale, la perle tourne de plus en plus comme sur un cercle.
>
> **(d) Rayon de courbure**
>
> $v_ra_\theta-v_\theta a_r=u\cdot2u\omega-u\omega t\cdot(-u\omega^2t)=u^2\omega\,(2+\omega^2t^2)$. Donc
> $$\rho=\frac{v^3}{|v_ra_\theta-v_\theta a_r|}=\boxed{\frac u\omega\,\frac{(1+\omega^2t^2)^{3/2}}{2+\omega^2t^2}}.$$
> En $t=0$ : $\rho=\dfrac u{2\omega}$ (la perle quitte $O$ avec une trajectoire déjà courbée). Pour $\omega t\gg1$ : $\rho\simeq\dfrac u\omega\,\omega t=ut=r$ : localement, la spirale se confond avec un cercle de rayon $r$.


**q3.** **Cas B : perle libre, $a_r=0$, $r(0)=r_0$, $\dot r(0)=0$.**


(a) Montrer que la condition $a_r=0$ conduit à $\ddot r=\omega^2r$ et en déduire $r(t)$.

(b) Déterminer $\vec v$ et $\vec a$ et calculer $\|\vec v\|$. Vérifier que $\vec a\ne\vec0$.

(c) Donner l'équation polaire $r(\theta)$ de la trajectoire et la limite de l'angle $\beta$ entre $\vec v$ et la tige quand $t\to\infty$.

(d) Application numérique : $r_0=10$ cm, tige de longueur $1{,}00$ m tournant à $1$ tour par seconde. À quel instant la perle quitte-t-elle la tige ? Avec quelle vitesse ?

> [!tip]- 💡 Coup de pouce
> $a_r=\ddot r-r\omega^2$ car $\dot\theta=\omega$. L'équation $\ddot r=\omega^2r$ a pour solutions $\cosh\omega t$ et $\sinh\omega t$ : lesquelles vérifient $\dot r(0)=0$ ?


> [!success]- ✅ Correction
> $r(t)=r_0\cosh\omega t$ ; $\vec v=r_0\omega(\sinh\omega t\,\vec u_r+\cosh\omega t\,\vec u_\theta)$, $\|\vec v\|=r_0\omega\sqrt{\cosh2\omega t}$ ; $\vec a=2r_0\omega^2\sinh\omega t\,\vec u_\theta$ ; $r=r_0\cosh\theta$, $\beta\to45^\circ$ ; $t\approx0{,}48$ s, $v\approx8{,}9$ m/s.


> [!example]- 📝 Solution détaillée
> **(e) Équation et solution**
>
> $a_r=\ddot r-r\omega^2=0$ donne $\ddot r=\omega^2r$. Solution générale $r=A\cosh\omega t+B\sinh\omega t$ ; $r(0)=r_0$ fixe $A=r_0$ et $\dot r(0)=B\omega=0$ fixe $B=0$ :
> $$\boxed{r(t)=r_0\cosh\omega t}.$$
>
> **(f) Vitesse et accélération**
>
> $\dot r=r_0\omega\sinh\omega t$, $r\dot\theta=r_0\omega\cosh\omega t$ :
> $$\boxed{\vec v=r_0\omega\left(\sinh\omega t\,\vec u_r+\cosh\omega t\,\vec u_\theta\right)},\qquad\|\vec v\|=r_0\omega\sqrt{\sinh^2\omega t+\cosh^2\omega t}=\boxed{r_0\omega\sqrt{\cosh2\omega t}}.$$
> $a_\theta=2\dot r\dot\theta=2r_0\omega^2\sinh\omega t$ et $a_r=0$ :
> $$\boxed{\vec a=2r_0\omega^2\sinh\omega t\,\vec u_\theta}\neq\vec0\ \text{pour }t>0.$$
> L'accélération est **perpendiculaire à la tige** : c'est cohérent avec une action de la tige qui ne peut être que normale à la tige.
>
> **(g) Trajectoire et angle limite**
>
> Avec $\theta=\omega t$ : $\boxed{r=r_0\cosh\theta}$. L'angle $\beta$ vérifie $\tan\beta=\dfrac{r\dot\theta}{\dot r}=\coth\omega t\to1$ : $\beta\to45^\circ$ aux temps longs, la vitesse radiale devient égale à la vitesse orthoradiale ($\mathrm e^{\omega t}$ domine dans $\cosh$ et $\sinh$), et $r$ croît exponentiellement.
>
> **(h) Application numérique**
>
> $\omega=2\pi$ rad/s. La perle quitte la tige quand $r_0\cosh\omega t=1{,}00$ m, soit $\cosh\omega t=10$ et $\omega t=\ln(10+\sqrt{99})\approx2{,}99$ rad : $t\approx0{,}48$ s (la tige a tourné de $\approx0{,}48$ tour). On a alors $v_r=r_0\omega\sinh\omega t\approx6{,}25$ m/s et $v_\theta=r_0\omega\cosh\omega t\approx6{,}28$ m/s, soit $\|\vec v\|=r_0\omega\sqrt{2\cdot100-1}\approx8{,}9$ m/s. Ordre de grandeur plausible : la perle, partie quasiment du repos, atteint $9$ m/s en une demi-seconde, car l'éjection est exponentielle.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]]

