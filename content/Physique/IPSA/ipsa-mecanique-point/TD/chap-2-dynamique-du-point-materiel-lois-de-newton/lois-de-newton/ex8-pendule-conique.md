---
title: "Exercice 8 — Pendule conique"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td4_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 8. Pendule conique *(facultatif)*

*Difficulté ●●●●○ · ⏱ 50 min · Type : Synthèse / Exercice non guidé*

Une petite masse $m=100$ g, assimilée à un point matériel $M$, est accrochée à l'extrémité d'un fil inextensible de masse négligeable et de longueur $L=1{,}00$ m, dont l'autre extrémité est fixée en un point $O$. La masse décrit à vitesse angulaire constante $\omega$ un cercle **horizontal** autour de la verticale $Oz$ passant par $O$ ; le fil fait alors un angle constant $\theta$ avec la verticale descendante (voir schéma : fil, cône de demi-angle $\theta$). On travaille dans le référentiel terrestre galiléen, avec $g=9{,}81~\mathrm{m\,s^{-2}}$ ; $Oz$ est vertical **descendant** et on utilise les coordonnées cylindriques $(r,\varphi,z)$ d'axe $Oz$, de base $(\vec e_r,\vec e_\varphi,\vec e_z)$.


> [!question]- 🪝 Accroche
> **Pourquoi une balle au bout d'une ficelle ne tourne-t-elle jamais à l'horizontale ?**
>
> *Durée de l'introduction : 4 min*
>
> *Vous faites tourner une balle au bout d'une ficelle de plus en plus vite. La ficelle se **soulève** mais ne devient **jamais** horizontale, même à très grande vitesse. Pourquoi ? Et à partir de quelle vitesse de rotation la balle quitte-t-elle la verticale ?*
>
> **Idée clé : deux projections de la 2\textsuperscript{e} loi.** Verticale : $T\cos\theta=mg$ (pas de mouvement vertical). Horizontale : $T\sin\theta=m\,r\omega^2=m\omega^2L\sin\theta$. D'où $T=m\omega^2L$ et $\cos\theta=\dfrac g{\omega^2L}$, qui n'a de solution que si $\omega^2L>g$.




> [!abstract]- 🧠 À savoir avant
> **Cinématique en coordonnées cylindriques**
>
> $\overrightarrow{OM}=r\,\vec e_r+z\,\vec e_z$, $\vec v=\dot r\,\vec e_r+r\dot\varphi\,\vec e_\varphi+\dot z\,\vec e_z$, $\vec a=(\ddot r-r\dot\varphi^2)\,\vec e_r+(r\ddot\varphi+2\dot r\dot\varphi)\,\vec e_\varphi+\ddot z\,\vec e_z$. Pour un cercle de rayon $r$ parcouru à $\omega$ constante : $\vec a=-r\omega^2\,\vec e_r$.




> [!info]- 🎯 Ce que tu sauras faire
> **Mouvement circulaire uniforme sous tension et pesanteur**
>
> Savoir identifier les forces (poids, tension), écrire l'accélération en cylindriques, projeter sur $\vec e_r$ et $\vec e_z$, résoudre pour la tension et l'angle, discuter l'existence d'une solution ($\omega$ minimale), et exploiter une limite de rupture du fil.




> [!info]- 🧑‍🏫 Objectifs pédagogiques
> **Un problème à deux projections et un seuil**
>
> La verticale ($a_z=0$) donne la composante verticale de la tension ; l'horizontale (centripète) donne la composante radiale. En divisant on obtient $\tan\theta$, et en reportant, $\cos\theta=g/(\omega^2L)$ : il n'existe de solution inclinée que si $\omega>\sqrt{g/L}$. En dessous, la masse reste suspendue verticalement. C'est un résultat de **seuil** remarquable : à discuter avec les étudiants. La tension $T=m\omega^2L$ ne dépend pas de $\theta$ explicitement.




> [!tip]- 📖 Rappel de cours
> **Mouvement circulaire uniforme**
>
> Cercle de rayon $r$ parcouru à vitesse angulaire $\omega$ constante : $v=r\omega$, $\vec a=-r\omega^2\,\vec e_r$ (accélération centripète), période $T_0=2\pi/\omega$. La somme des forces est dirigée vers le centre du cercle : $\sum\vec F=-mr\omega^2\,\vec e_r$.




> [!note]- 🧮 Outils mathématiques
> **Projection d'une force oblique**
>
> Fil faisant l'angle $\theta$ avec la verticale : la tension se décompose en $T\cos\theta$ (verticale) et $T\sin\theta$ (horizontale, radiale).
>
> **Fonction arccosinus**
>
> $\theta=\arccos\Big(\dfrac g{\omega^2L}\Big)$ défini si $\dfrac g{\omega^2L}\le1$ ; $\arccos(0{,}613)\approx52{,}2^\circ$.
>
> **Développement limité de $\cos\theta$**
>
> $\cos\theta\approx1-\dfrac{\theta^2}2$ : $\dfrac g{\omega^2L}\approx1-\dfrac{\theta^2}2$ donne $\omega^2\approx\dfrac gL\Big(1+\dfrac{\theta^2}2\Big)$.
>
> **Division membre à membre**
>
> Diviser $T\sin\theta=m\omega^2L\sin\theta$ par $T\cos\theta=mg$ pour éliminer $T$ : $\tan\theta=\dfrac{\omega^2L\sin\theta}g$, soit $\cos\theta=\dfrac g{\omega^2L}$ pour $\theta\ne0$.



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




> [!note]- 🔗 Liens avec d'autres disciplines
> **Histoire de la technique**
>
> Le régulateur à boules de Watt (1788) : l'angle des boules contrôle la vanne d'arrivée de vapeur et stabilise la vitesse des machines.
>
> **Manèges et loisirs**
>
> Les « chaises volantes » : les sièges s'écartent d'un angle qui augmente avec la vitesse de rotation, sans jamais atteindre l'horizontale.
>
> **Astronomie**
>
> Un satellite en orbite circulaire est un « pendule conique sans fil » : la gravité joue le rôle de la tension, et l'accélération centripète est $v^2/r$.




> [!warning]- 🪤 Écueils classiques
> **Chercher un équilibre dans le référentiel du laboratoire**
>
> La masse est en mouvement accéléré : $\sum\vec F\ne\vec0$. La force qui « tient » la masse sur sa trajectoire est la composante horizontale de la tension.
>
> **Projeter la tension avec le mauvais angle**
>
> Si $\theta$ est l'angle avec la verticale : composante verticale $T\cos\theta$, composante horizontale (radiale) $T\sin\theta$. L'inversion est fréquente.
>
> **Utiliser le rayon $L$ au lieu de $r=L\sin\theta$**
>
> Le rayon du cercle est $r=L\sin\theta$ ; l'accélération centripète est $r\omega^2=L\omega^2\sin\theta$ (et non $L\omega^2$).
>
> **Croire qu'un fil peut devenir horizontal**
>
> $\theta\to90^\circ$ nécessiterait $\omega\to\infty$ : un fil réel ne peut jamais être horizontal car la composante verticale de la tension doit porter le poids.




> [!tip]- 🎙️ Conseils d'animation
> **Manipulation**
>
> Faire tourner une balle au bout d'une ficelle dans un plan horizontal : on observe que l'angle augmente avec la vitesse de rotation et qu'on ne peut jamais atteindre l'horizontale. Chronométrer $10$ tours pour mesurer $\omega$ et comparer avec $\cos\theta=g/(\omega^2L)$.
>
> **Lien avec un régulateur**
>
> Le régulateur de Watt (machine à vapeur) est un double pendule conique : l'angle des boules mesure la vitesse de rotation de la machine et commande la vanne.




> [!success]- 🏁 Bilan pédagogique
> **Pendule conique**
>
> $T=m\omega^2L$ ; $\cos\theta=\dfrac{g}{\omega^2L}$ (solution inclinée si $\omega>\sqrt{g/L}\approx3{,}13~\mathrm{rad/s}$) ; rayon $r=L\sin\theta$ ; $v=\omega r$ ; période $T_0=2\pi\sqrt{L\cos\theta/g}$. Avec $\omega=4~\mathrm{rad/s}$ : $\theta\approx52{,}2^\circ$, $T=1{,}6$ N. Fil de rupture $5$ N : $\omega_{\max}\approx7{,}07~\mathrm{rad/s}$ et $\theta\approx78{,}7^\circ$.




> [!question]- 🔭 Aller plus loin — CPGE : Petits angles : retrouver le pendule simple
> Pour $\omega\to\sqrt{g/L}^{+}$, $\theta\to0$ : montrer que $\omega^2\approx\dfrac gL\Big(1+\dfrac{\theta^2}2\Big)$. Interpréter : le pendule conique de petit angle a la même période que le pendule simple de petites oscillations.




> [!question]- 🔭 Aller plus loin — Licence : Stabilité de la solution
> Écrire l'équation du mouvement dans le plan vertical contenant le fil ($\ddot\theta=\omega^2\sin\theta\cos\theta-\dfrac gL\sin\theta$) et étudier la stabilité des solutions $\theta=0$ et $\cos\theta=g/(\omega^2L)$ par linéarisation : la branche inclinée est stable pour $\omega>\sqrt{g/L}$, tandis que $\theta=0$ devient instable.




> [!question]- 🔭 Aller plus loin — Master : Régulateur de Watt
> Deux boules identiques sur deux bras articulés au même point, montés sur un axe en rotation. Établir la relation entre $\omega$ et l'angle des bras, et la hauteur du manchon $h=g/\omega^2$ (indépendante de la longueur des bras si le manchon est relié au bas du parallélogramme).




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex1-exercices-elementaires|Exercice 1 — Exercices élémentaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex3-machine-d-atwood|Exercice 3 — Machine d'Atwood]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex7-chute-avec-frottement-fluide-vitesse-limite|Exercice 7 — Chute avec frottement fluide : vitesse limite]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex4-systeme-pendule-bloc|Exercice 4 — (*) Système pendule-bloc]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex5-pendule-balistique|Exercice 5 — (*) Pendule balistique]]


