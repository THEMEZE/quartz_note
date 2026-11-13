---
title: "Exercice 5 — (*) Bille sur une sphère : angle de décollage"
tags:
  - td
  - chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/index|⬅ Retour]]

### Exercice 5. (*) Bille sur une sphère : angle de décollage *(facultatif)*

Une petite bille de masse $m$, assimilée à un point matériel, est posée au sommet $S$ d'une sphère **fixe** de rayon $R$, posée sur le sol, et légèrement écartée de la verticale : elle part avec une vitesse initiale pratiquement nulle et glisse sans frottement sur la sphère. On repère sa position par l'angle $\theta$ entre la verticale ascendante $Oz$ (axe passant par le centre $O$) et le rayon $\overrightarrow{OM}$ ($\theta=0$ au sommet). On prendra $g=9{,}81~\mathrm{m\,s^{-2}}$ et, pour les applications numériques, $R=2{,}0$ m. **Question centrale : à quel angle la bille quitte-t-elle la sphère ?**

**q1.** - [(a)] Faire un schéma, dresser le bilan des forces sur la bille et dire lesquelles travaillent. Justifier que l'énergie mécanique est conservée.
- [(b)] Établir la vitesse $v(\theta)$ de la bille en fonction de $g$, $R$ et $\theta$.

> [!tip]- 💡 Coup de pouce
> Deux forces : le poids et la réaction normale (pas de frottement). La réaction est perpendiculaire à $\vec v$. L'altitude de la bille est $z=R\cos\theta$ au-dessus de $O$.


**q2.** - [(c)] Appliquer la loi de Newton à la bille et la projeter sur $\vec e_r$. En déduire la réaction $N(\theta)$.
- [(d)] Quelle est la condition physique de décollage ? Déterminer l'angle $\theta_d$, la hauteur $z_d$ et la vitesse $v_d$ du décollage. Application numérique pour $R=2{,}0$ m. L'angle dépend-il de $m$ ? de $R$ ?

> [!tip]- 💡 Coup de pouce
> $\vec a=-R\dot\theta^2\,\vec e_r+R\ddot\theta\,\vec e_\theta$. Le poids a pour composante radiale $-mg\cos\theta$ (vers le centre) : attention au signe de $N$.


**q3.** - [(e)] La bille part maintenant du sommet avec une vitesse horizontale $v_0$ non nulle. Établir $\cos\theta_d$ en fonction de $v_0$, $g$ et $R$. À partir de quelle valeur de $v_0$ la bille décolle-t-elle immédiatement ?
- [(f)] Pour $v_0=0$, la sphère étant posée sur le sol, étudier la suite du mouvement : déterminer l'instant et le point d'impact (distance horizontale à l'axe de la sphère) et la vitesse à l'impact (application numérique). Vérifier la vitesse d'impact par l'énergie.

> [!tip]- 💡 Coup de pouce
> (e) $E_m=\tfrac12mv_0^2+mgR$. Poser $N=0$. (f) Après $\theta_d$ : projectile ; $\vec v_d$ est tangent au cercle, dirigé vers le bas. Le sol est à $z=-R$ si l'origine est en $O$.


**q4.** **Bille qui roule.** La bille est maintenant une bille pleine de rayon $r\ll R$, qui roule **sans glisser** sur la sphère (on assimile son centre à un point du cercle de rayon $R$, $J=\tfrac25mr^2$).


- [(g)] Établir par l'énergie $v^2(\theta)$, puis $N(\theta)$ et l'angle de décollage $\theta_d$ ($\cos\theta_d=10/17$ attendu). Comparer au cas du glissement.
- [(h)] Écrire le théorème du moment cinétique pour la bille et en déduire la force de frottement $f(\theta)$ (adhérence). Exprimer $f/N$.
- [(i)] Le coefficient d'adhérence est $\mu$. Montrer qu'il existe un angle $\theta_g<\theta_d$ à partir duquel la bille glisse. Calculer $\theta_g$ pour $\mu=0{,}3$ ; $0{,}5$ ; $0{,}8$. Conclure : la bille quitte-t-elle la sphère en roulant ?

> [!tip]- 💡 Coup de pouce
> (g) $E_c=\tfrac12mv^2+\tfrac12J\omega^2$ avec $\omega=v/r$. (h) $J\dot\omega=fr$ et $m\dot v=mg\sin\theta-f$ avec $\dot\omega=\dot v/r$. (i) Condition d'adhérence : $f\le\mu N$.


**q5.** **Approche de Lagrange (niveau licence/master).** On revient à la bille qui glisse sans frottement. On utilise les coordonnées polaires $(r,\theta)$ et la liaison $f(r)=r-R=0$.


- [(j)] Écrire le lagrangien $L(r,\theta,\dot r,\dot\theta)=T-V$.
- [(k)] Écrire les équations d'Euler--Lagrange avec un multiplicateur $\lambda$ pour la liaison : $\dfrac{\mathrm d}{\mathrm dt}\dfrac{\partial L}{\partial\dot q}-\dfrac{\partial L}{\partial q}=\lambda\dfrac{\partial f}{\partial q}$. Montrer que $\lambda=N$ et retrouver $N(\theta)$ et $\theta_d$.

> [!tip]- 💡 Coup de pouce
> $T=\tfrac12m(\dot r^2+r^2\dot\theta^2)$ et $V=mgr\cos\theta$. Écrire l'équation en $r$ puis imposer $r=R$, $\dot r=\ddot r=0$. L'équation en $\theta$ donne $\ddot\theta$ ; l'intégrer par $\dot\theta\ddot\theta$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex4-looping-vertical|Exercice 4 — Looping vertical]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex4-systeme-pendule-bloc|Exercice 4 — (*) Système pendule-bloc]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex5-pendule-balistique|Exercice 5 — (*) Pendule balistique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex3-vitesse-et-acceleration-en-coordonnees-polaires|Exercice 3 — Vitesse et accélération en coordonnées polaires]]

