---
title: "Exercice 8 — Pendule conique"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 8. Pendule conique *(facultatif)*

Une petite masse $m=100$ g, assimilée à un point matériel $M$, est accrochée à l'extrémité d'un fil inextensible de masse négligeable et de longueur $L=1{,}00$ m, dont l'autre extrémité est fixée en un point $O$. La masse décrit à vitesse angulaire constante $\omega$ un cercle **horizontal** autour de la verticale $Oz$ passant par $O$ ; le fil fait alors un angle constant $\theta$ avec la verticale descendante (voir schéma : fil, cône de demi-angle $\theta$). On travaille dans le référentiel terrestre galiléen, avec $g=9{,}81~\mathrm{m\,s^{-2}}$ ; $Oz$ est vertical **descendant** et on utilise les coordonnées cylindriques $(r,\varphi,z)$ d'axe $Oz$, de base $(\vec e_r,\vec e_\varphi,\vec e_z)$.

**q1.** - [(a)] Faire un schéma et le bilan des forces s'exerçant sur $M$. Exprimer le rayon $r$ du cercle en fonction de $L$ et $\theta$.
- [(b)] Donner l'expression du vecteur vitesse $\vec v$ et du vecteur accélération $\vec a$ de $M$ en coordonnées cylindriques. Exprimer $v$ en fonction de $L$, $\theta$, $\omega$.

> [!tip]- 💡 Coup de pouce
> $M$ est à distance $L$ de $O$ et à angle $\theta$ de l'axe : $r=L\sin\theta$ et $z=L\cos\theta$ constants. Dérivez : $\dot r=\dot z=0$ et $\dot\varphi=\omega$.


> [!success]- ✅ Correction
> Forces : poids $mg\,\vec e_z$ et tension $\vec T$ ; $r=L\sin\theta$ ; $\vec v=r\omega\,\vec e_\varphi$, $\vec a=-r\omega^2\,\vec e_r$, $v=\omega L\sin\theta$.


> [!example]- 📝 Solution détaillée
> **(a) Forces et rayon**
>
> Système : la masse. Forces : le poids $\vec P=mg\,\vec e_z$ ($Oz$ descendant) et la tension du fil $\vec T$, dirigée de $M$ vers $O$, de composantes $\vec T=-T\sin\theta\,\vec e_r-T\cos\theta\,\vec e_z$. Le triangle $OMH$ ($H$ projection de $M$ sur l'axe) donne $\boxed{r=L\sin\theta}$ et $z=L\cos\theta$.
>
> **(b) Vitesse et accélération**
>
> $\overrightarrow{OM}=r\,\vec e_r+z\,\vec e_z$ avec $r,z$ constants et $\dot\varphi=\omega$ : $\boxed{\vec v=r\omega\,\vec e_\varphi}$, $v=\omega L\sin\theta$ ; et
> $$\boxed{\vec a=-r\omega^2\,\vec e_r=-\omega^2L\sin\theta\,\vec e_r}$$
> (accélération centripète, dirigée vers l'axe $Oz$).


**q2.** - [(c)] Appliquer la 2\textsuperscript{e} loi de Newton et la projeter sur $\vec e_r$ et $\vec e_z$.
- [(d)] En déduire la tension $T$ du fil et la relation entre $\theta$, $\omega$, $L$ et $g$.
- [(e)] À quelle condition sur $\omega$ le mouvement avec $\theta\ne0$ est-il possible ? Calculer cette vitesse angulaire critique.
- [(f)] Application numérique pour $\omega=4{,}0~\mathrm{rad/s}$ : calculer $\theta$, $T$, $r$, $v$ et la période de révolution.

> [!tip]- 💡 Coup de pouce
> Selon $\vec e_z$ : $a_z=0$. Selon $\vec e_r$ : $a_r=-r\omega^2$. Éliminez $T$ entre les deux projections, ou utilisez la projection radiale pour avoir $T$ directement.


> [!success]- ✅ Correction
> $T\cos\theta=mg$ ; $T\sin\theta=m\omega^2L\sin\theta$ ; $T=m\omega^2L$ ; $\cos\theta=\dfrac g{\omega^2L}$ ; $\omega>\sqrt{g/L}\approx3{,}13~\mathrm{rad/s}$ ; $\theta\approx52{,}2^\circ$, $T=1{,}6$ N, $r\approx0{,}79$ m, $v\approx3{,}2~\mathrm{m/s}$, période $1{,}57$ s.


> [!example]- 📝 Solution détaillée
> **(c) Deuxième loi et projections**
>
> $m\vec a=\vec P+\vec T$ se projette en
> $$(\vec e_r):\ -m\,r\omega^2=-T\sin\theta,\qquad(\vec e_z):\ 0=mg-T\cos\theta .$$
>
> **(d) Tension et angle**
>
> Avec $r=L\sin\theta$, la première équation donne, pour $\theta\ne0$, $T\sin\theta=m\omega^2L\sin\theta$ soit $\boxed{T=m\,\omega^2L}$. La seconde donne $T\cos\theta=mg$. En égalant :
> $$m\omega^2L\cos\theta=mg\ \Rightarrow\ \boxed{\cos\theta=\frac{g}{\omega^2L}}.$$
> La masse $m$ disparaît de la relation entre l'angle et la vitesse de rotation.
>
> **(e) Condition d'existence**
>
> $\cos\theta<1$ exige $\omega^2L>g$, soit
> $$\boxed{\omega>\omega_c=\sqrt{\frac gL}}\approx3{,}13~\mathrm{rad/s}\quad(\text{soit }\approx0{,}50~\text{tour/s}).$$
> Pour $\omega\le\omega_c$, seule la solution $\theta=0$ (masse suspendue verticalement au repos, ou en rotation sur place) existe. Quand $\omega\to\infty$, $\cos\theta\to0$ : $\theta\to90^\circ$ mais n'est jamais atteint.
>
> **(f) Application numérique**
>
> $\cos\theta=\dfrac{9{,}81}{16\times1{,}00}=0{,}613\Rightarrow\boxed{\theta\approx52{,}2^\circ}$ ; $T=0{,}100\times16\times1{,}00=\boxed{1{,}6~\text{N}}$ (soit $\approx1{,}6$ fois le poids $0{,}98$ N) ; $r=L\sin\theta\approx\boxed{0{,}79~\text{m}}$ ; $v=\omega r\approx\boxed{3{,}2~\mathrm{m/s}}$ ; période $\dfrac{2\pi}\omega=\boxed{1{,}57~\text{s}}$.


**q3.** - [(g)] Le fil se rompt si la tension dépasse $T_{\max}=5{,}0$ N. Quelle est la vitesse de rotation maximale (en rad/s et en tours par minute) ? Quel est alors l'angle $\theta$ ?
- [(h)] Le fil casse. Décrire qualitativement le mouvement ultérieur de la masse, à partir de ses conditions initiales juste après la rupture.

> [!tip]- 💡 Coup de pouce
> $T=m\omega^2L$ : la rupture se produit quand $T=T_{\max}$. Après rupture, il ne reste que le poids : quel type de mouvement ?


> [!success]- ✅ Correction
> $\omega_{\max}=\sqrt{T_{\max}/(mL)}\approx7{,}07~\mathrm{rad/s}\approx67{,}5$ tr/min ; $\theta\approx78{,}7^\circ$. Après rupture : tir parabolique à vitesse initiale horizontale tangente au cercle.


> [!example]- 📝 Solution détaillée
> **(g) Vitesse limite de rotation**
>
> $T=m\omega^2L\le T_{\max}\Rightarrow\omega_{\max}=\sqrt{\dfrac{T_{\max}}{mL}}=\sqrt{\dfrac{5{,}0}{0{,}100\times1{,}00}}\approx\boxed{7{,}07~\mathrm{rad/s}}\approx67{,}5$ tours/min. L'angle correspondant : $\cos\theta=\dfrac{9{,}81}{50}=0{,}196\Rightarrow\boxed{\theta\approx78{,}7^\circ}$ : le fil est presque horizontal sans jamais l'être.
>
> **(h) Après la rupture**
>
> Seul le poids agit ensuite : mouvement de **projectile**. Conditions initiales : position sur le cercle de rayon $r\approx0{,}98$ m, hauteur $z=L\cos\theta$ sous $O$, vitesse $v=\omega r\approx6{,}9~\mathrm{m/s}$ **horizontale et tangente au cercle**. La masse quitte le cercle suivant la tangente (et non radialement) et décrit une parabole dans le plan vertical contenant cette tangente ; à la verticale, c'est une chute libre sans vitesse initiale verticale.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex1-exercices-elementaires|Exercice 1 — Exercices élémentaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex3-machine-d-atwood|Exercice 3 — Machine d'Atwood]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex7-chute-avec-frottement-fluide-vitesse-limite|Exercice 7 — Chute avec frottement fluide : vitesse limite]]

