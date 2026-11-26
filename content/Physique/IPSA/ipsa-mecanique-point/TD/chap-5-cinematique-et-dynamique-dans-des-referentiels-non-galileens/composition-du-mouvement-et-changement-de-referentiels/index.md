---
title: "Composition du mouvement et changement de référentiels"
tags:
  - td
  - chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens
---

[[physique/IPSA/ipsa-mecanique-point/index|⬅ Mécanique du point — IPSA]]


> [!info] ℹ️ Chap. 5 — Cinématique et dynamique dans des référentiels non galiléens
> Séance 7



<a href="/pdfs/td7_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td7_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>


> [!question]- 🪝 Accroche
> **Pourquoi une balle lancée droit sur un manège semble-t-elle courber ?**
>
> *Durée de l'introduction : 5 min*
>
> *Un enfant sur un manège lance une balle droit vers un ami situé en face de lui. La balle atteint-elle l'ami ? Qu'en dit un observateur au sol ? Et un astronaute qui lance une balle vers l'équateur depuis le pôle Nord ?*
>
> **Idée clé : le mouvement est relatif ; les forces d'inertie sont le prix à payer pour décrire le monde dans un référentiel non galiléen.** Pour l'observateur au sol, la trajectoire est droite ; pour l'enfant, elle est courbée par la force de Coriolis $-2m\vec\Omega\wedge\vec v_r$.



> [!abstract]- 🧠 À savoir avant
> **Dérivée d'un vecteur dans une base mobile**
>
> Pour un vecteur $\vec A$ : $\left(\dfrac{\mathrm d\vec A}{\mathrm dt}\right)_{\mathcal R}=\left(\dfrac{\mathrm d\vec A}{\mathrm dt}\right)_{\mathcal R'}+\vec\Omega\wedge\vec A$. Pour une base tournant autour de $Oz$ avec $\dot\theta=\omega$ : $\dot{\vec e}_x{}'=\omega\,\vec e_y{}'$ et $\dot{\vec e}_y{}'=-\omega\,\vec e_x{}'$.
>
> **Cinématique du point dans une base cartésienne et polaire**
>
> $\vec v=\dot x\,\vec e_x+\dot y\,\vec e_y$ ; en polaire $\vec v=\dot r\,\vec e_r+r\dot\theta\,\vec e_\theta$ et $\vec a=(\ddot r-r\dot\theta^2)\,\vec e_r+(r\ddot\theta+2\dot r\dot\theta)\,\vec e_\theta$.
>
> **Les trois lois de Newton**
>
> Dans un référentiel galiléen, $m\vec a=\sum\vec F$ ; le principe d'inertie définit les référentiels galiléens.
>
> **Produit vectoriel**
>
> Règle de la main droite, double produit vectoriel $\vec a\wedge(\vec b\wedge\vec c)=\vec b(\vec a\cdot\vec c)-\vec c(\vec a\cdot\vec b)$, norme $\|\vec a\wedge\vec b\|=ab\sin\alpha$.



> [!info]- 🎯 Ce que tu sauras faire
> **Composer vitesses et accélérations**
>
> Savoir écrire et appliquer $\vec v_a=\vec v_r+\vec v_e$ et $\vec a_a=\vec a_r+\vec a_e+\vec a_c$, identifier à chaque fois le mouvement relatif, d'entraînement, et savoir calculer $\vec a_e$ et $\vec a_c=2\vec\Omega\wedge\vec v_r$.
>
> **Reconnaître un référentiel galiléen**
>
> Savoir qu'un référentiel en **translation rectiligne uniforme** par rapport à un galiléen est galiléen (exercice 1) et que les accélérations y sont identiques.
>
> **Faire de la dynamique en référentiel non galiléen**
>
> Savoir écrire le principe fondamental $m\vec a_r=\sum\vec F+\vec F_{ie}+\vec F_{ic}$ avec $\vec F_{ie}=-m\vec a_e$ et $\vec F_{ic}=-m\vec a_c$, et en déduire équilibres relatifs et petites oscillations (exercices 5 à 7).



> [!tip]- 📖 Rappel de cours
> **Mouvement absolu, relatif, d'entraînement**
>
> Le mouvement de $M$ dans $\mathcal R$ est le **mouvement absolu**, dans $\mathcal R'$ le **mouvement relatif**. Le **mouvement d'entraînement** est celui du point $M'$ **fixe dans $\mathcal R'$** qui coïncide à l'instant $t$ avec $M$, vu depuis $\mathcal R$ : c'est le mouvement que $M$ aurait s'il était fixé à $\mathcal R'$.
>
> **Composition des vitesses**
>
> $$\vec v_a=\vec v_r+\vec v_e,\qquad\vec v_e=\vec v_{O'/\mathcal R}+\vec\Omega\wedge\overrightarrow{O'M}.$$
> Cas particuliers : translation ($\vec\Omega=\vec0$) $\Rightarrow\vec v_e=\vec v_{O'}$ ; rotation autour d'un axe fixe ($O'=O$) $\Rightarrow\vec v_e=\vec\Omega\wedge\overrightarrow{OM}$.
>
> **Composition des accélérations**
>
> $$\vec a_a=\vec a_r+\vec a_e+\vec a_c,\qquad\vec a_c=2\vec\Omega\wedge\vec v_r,$$
> $$\vec a_e=\vec a_{O'/\mathcal R}+\frac{\mathrm d\vec\Omega}{\mathrm dt}\wedge\overrightarrow{O'M}+\vec\Omega\wedge(\vec\Omega\wedge\overrightarrow{O'M}).$$
> Pour une rotation uniforme autour de $Oz$ : $\vec a_e=-\Omega^2\,\overrightarrow{HM}$ où $H$ est le projeté orthogonal de $M$ sur l'axe (accélération **centripète**).
>
> **Démonstration de la composition des vitesses**
>
> $\overrightarrow{OM}=\overrightarrow{OO'}+\overrightarrow{O'M}$ avec $\overrightarrow{O'M}=x'\vec e_x{}'+y'\vec e_y{}'+z'\vec e_z{}'$. On dérive dans $\mathcal R$ : les composantes donnent $\vec v_r$ ; les dérivées des vecteurs de base donnent $\vec\Omega\wedge\overrightarrow{O'M}$ ; il reste $\vec v_{O'}$. D'où $\vec v_a=\vec v_r+\vec v_{O'}+\vec\Omega\wedge\overrightarrow{O'M}$.
>
> **Référentiels galiléens**
>
> Si $\mathcal R$ est galiléen, $\mathcal R'$ l'est ssi $\vec a_e=\vec0$ et $\vec a_c=\vec0$ pour tout $M$ : $\mathcal R'$ est en **translation rectiligne uniforme** par rapport à $\mathcal R$. Le référentiel terrestre est « galiléen » pour des durées courtes devant un jour ; le référentiel de Copernic est un meilleur galiléen.
>
> **Dynamique en référentiel non galiléen**
>
> Le principe fondamental s'écrit $m\vec a_r=\vec F_{\rm vraies}-m\vec a_e-m\vec a_c$. On pose $\vec F_{ie}=-m\vec a_e$ (inertie d'entraînement, pour une rotation : force **centrifuge** $m\Omega^2\overrightarrow{HM}$) et $\vec F_{ic}=-2m\,\vec\Omega\wedge\vec v_r$ (Coriolis). La force de Coriolis **ne travaille pas** ($\perp\vec v_r$) ; la force d'inertie d'entraînement dérive d'une énergie potentielle dans une rotation uniforme : $E_{p,ie}=-\tfrac12m\Omega^2HM^2$.
>
> **Théorème de l'énergie dans $\mathcal R'$**
>
> $\dfrac{\mathrm d}{\mathrm dt}E_{c,r}=\sum P(\vec F_{\rm vraies})+P(\vec F_{ie})$ (Coriolis ne contribue pas). Pour une rotation uniforme et des forces conservatives : $E_{m}'=\tfrac12mv_r^2+E_p-\tfrac12m\Omega^2HM^2=\text{cte}$.
>
> **Équilibre relatif et stabilité**
>
> À l'équilibre relatif ($\vec v_r=\vec0$ et $\vec a_r=\vec0$), les forces d'inertie d'entraînement s'ajoutent aux forces vraies : $\sum\vec F+\vec F_{ie}=\vec0$. La stabilité s'étudie sur le potentiel effectif $E_{p,\rm eff}=E_p+E_{p,ie}$ (minimum $\Rightarrow$ stable).
>
> **Le référentiel terrestre**
>
> Rotation à $\Omega=\dfrac{2\pi}{23\,{\rm h}\,56\,{\rm min}\,4\,{\rm s}}=7{,}292\times10^{-5}\ {\rm rad\cdot s^{-1}}$. Pesanteur effective $\vec g=\vec g_0+\Omega^2\overrightarrow{HM}$ (correction $\le3{,}4\times10^{-2}\ {\rm m\cdot s^{-2}}$ à l'équateur, soit 0,35 \%). Coriolis : déviation vers la droite dans l'hémisphère Nord ; composante verticale de $\vec\Omega$ à la latitude $\lambda$ : $\Omega\sin\lambda$.



> [!note]- 🧮 Outils mathématiques
> **Dérivation de vecteurs**
>
> Règle de dérivation de $\vec A=A_x'\vec e_x{}'+A_y'\vec e_y{}'$ dans $\mathcal R$ : $\dot{\vec A}=\dot A_x'\vec e_x{}'+\dot A_y'\vec e_y{}'+\vec\Omega\wedge\vec A$.
>
> **Produit vectoriel en composantes**
>
> $\vec e_z\wedge\vec e_x=\vec e_y$, $\vec e_z\wedge\vec e_y=-\vec e_x$ ; $\vec\Omega=\Omega\vec e_z$ : $\vec\Omega\wedge(x\vec e_x+y\vec e_y)=\Omega(-y\vec e_x+x\vec e_y)$.
>
> **Petites oscillations**
>
> $\ddot\theta=f(\theta)$, équilibre $f(\theta_0)=0$ stable si $f'(\theta_0)<0$ ; pulsation $\omega_0^2=-f'(\theta_0)$.
>
> **Développement limité à l'ordre 1**
>
> $\sin\varphi\approx\varphi$, $\cos\varphi\approx1-\varphi^2/2$, $\cosh\varphi\approx1+\varphi^2/2$ (pour le cas Coriolis et le pendule dans le train).



## Exercices

- [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex1-vitesse-d-entrainement|Exercice 1 — Vitesse d'entraînement]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex2-traversee-d-une-riviere|Exercice 2 — Traversée d'une rivière]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex3-vitesse-et-acceleration-en-coordonnees-polaires|Exercice 3 — Vitesse et accélération en coordonnées polaires]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex4-mouvement-sur-un-manege|Exercice 4 — Mouvement sur un manège]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex5-pendule-dans-un-wagon-accelere|Exercice 5 — Pendule dans un wagon accéléré]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex6-perle-sur-un-cerceau-tournant|Exercice 6 — Perle sur un cerceau tournant]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex7-effet-coriolis-terrestre-chute-libre-et-pendule-de-foucault|Exercice 7 — Effet Coriolis terrestre : chute libre et pendule de Foucault]]
