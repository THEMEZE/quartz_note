---
title: "Travail et énergie"
tags:
  - td
  - chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique
---

[[physique/IPSA/ipsa-mecanique-point/index|⬅ Mécanique du point — IPSA]]


> [!info] ℹ️ Chap. 3 — Travail, énergie cinétique, énergie potentielle, énergie mécanique
> Séance 5



<a href="/pdfs/td5_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td5_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>


> [!question]- 🪝 Accroche
> **Sans calculer l'accélération : la hauteur d'une montagne russe**
>
> *Durée de l'introduction : 5 min*
>
> *Un wagon est lâché sans vitesse du haut d'une descente. **Quelle est sa vitesse en bas ?** Dépend-elle de la forme de la descente ? Et de la masse ? Existe-t-il **une hauteur minimale** pour passer le looping ?*
>
> **Idée clé : $E_c+E_p=\text{cte}$ quand les seules forces qui travaillent sont conservatives.** Le travail d'une force de liaison est nul ; le travail du poids ne dépend que de la différence d'altitude. D'où $v=\sqrt{2g\,\Delta h}$ quelle que soit la forme du rail, indépendamment de la masse.



> [!abstract]- 🧠 À savoir avant
> **Les lois de Newton et la méthode du TD4**
>
> $\sum\vec F=m\vec a$, bilan de forces exhaustif, projection sur des axes adaptés (cartésiens, polaires, base de Frenet). Le TD5 donne une **seconde méthode** : au lieu de projeter la loi de Newton, on intègre une fois pour obtenir un bilan d'énergie.
>
> **Produit scalaire et intégrale**
>
> $\vec A\cdot\vec B=A_xB_x+A_yB_y+A_zB_z=\|\vec A\|\|\vec B\|\cos\varphi$ ; intégrale d'une fonction d'une variable, primitive de $x^n$ ; différentielle $\mathrm d(x^2)=2x\,\mathrm dx$.
>
> **Cinématique du TD1 et accélération dans la base de Frenet**
>
> $\vec a=\dfrac{\mathrm dv}{\mathrm dt}\,\vec t+\dfrac{v^2}{\rho}\,\vec n$ ($\rho$ rayon de courbure) ; en coordonnées polaires, $\vec v=\dot r\vec e_r+r\dot\theta\vec e_\theta$ ; $\vec v=\dfrac{\mathrm d\overrightarrow{OM}}{\mathrm dt}$, donc $\mathrm d\overrightarrow{OM}=\vec v\,\mathrm dt$.
>
> **Forces usuelles du TD4**
>
> Poids, réaction normale ($N\ge0$), tension d'un fil, rappel élastique $-k(\ell-\ell_0)\vec u$, frottement solide de Coulomb. Il faut savoir dire **lesquelles travaillent**.



> [!info]- 🎯 Ce que tu sauras faire
> **Calculer un travail**
>
> Savoir écrire $\delta W=\vec F\cdot\mathrm d\overrightarrow{OM}$, l'intégrer sur un chemin (force constante, force de rappel, force dépendant de la position), reconnaître le signe (moteur, résistant, nul) et calculer une puissance $P=\vec F\cdot\vec v$.
>
> **Utiliser le théorème de l'énergie cinétique et de l'énergie mécanique**
>
> Savoir choisir entre $\Delta E_c=\sum W$ et $\Delta E_m=W_{\rm nc}$, justifier la conservation de $E_m$ (forces conservatives ou ne travaillant pas) et obtenir une vitesse sans calculer l'accélération.
>
> **Exploiter un diagramme d'énergie potentielle**
>
> Savoir lire un graphe $E_p(x)$ : positions d'équilibre, stabilité, états liés et libres, points de rebroussement, période des petites oscillations par $k_{\rm eff}=E_p''(x_{\rm eq})$.
>
> **Articuler énergie et dynamique**
>
> Savoir utiliser l'énergie pour la vitesse, puis la loi de Newton projetée (radialement) pour la réaction, et en déduire des conditions de décollage ($N=0$), de passage ou de glissement.



> [!tip]- 📖 Rappel de cours
> **Travail d'une force**
>
> Travail élémentaire : $\delta W=\vec F\cdot\mathrm d\overrightarrow{OM}=\vec F\cdot\vec v\,\mathrm dt$. Travail le long d'un chemin $\Gamma$ de $A$ à $B$ : $W_{A\to B}=\displaystyle\int_\Gamma\vec F\cdot\mathrm d\overrightarrow{OM}$. Force constante : $W=\vec F\cdot\overrightarrow{AB}$ (le chemin ne compte pas). Signe : $W>0$ (force motrice, $\varphi<90^\circ$), $W<0$ (résistante), $W=0$ (force perpendiculaire au déplacement : réaction d'un support lisse, tension d'un pendule, force magnétique). Unité : le joule, $1~\mathrm J=1~\mathrm N\,\mathrm m=1~\mathrm{kg\,m^2\,s^{-2}}$.
>
> **Puissance**
>
> $P=\dfrac{\delta W}{\mathrm dt}=\vec F\cdot\vec v$ (en watts). Puissance moyenne : $\bar P=W/\Delta t$. Un moteur de puissance $P$ qui tire à vitesse $v$ exerce $F=P/v$ : à puissance fixée, la force diminue quand la vitesse augmente.
>
> **Théorème de l'énergie cinétique (TEC)**
>
> **Démonstration.** $m\vec a=\sum\vec F$ ; on multiplie scalairement par $\vec v\,\mathrm dt=\mathrm d\overrightarrow{OM}$ : $m\,\dfrac{\mathrm d\vec v}{\mathrm dt}\cdot\vec v\,\mathrm dt=\mathrm d\Big(\tfrac12mv^2\Big)=\sum\delta W$. D'où, avec $E_c=\tfrac12mv^2$ :
> $$\mathrm dE_c=\sum\delta W,\qquad \Delta E_c=E_c(B)-E_c(A)=\sum W_{A\to B}.$$
> Forme valable pour **toutes** les forces (conservatives ou non), dans un référentiel galiléen. Le TEC est une conséquence de la 2\textsuperscript{e} loi (projection sur la tangente) : il ne contient pas l'information normale à la trajectoire.
>
> **Force conservative et énergie potentielle**
>
> Une force est **conservative** si son travail ne dépend pas du chemin suivi, c'est-à-dire s'il existe $E_p$ telle que $\delta W=-\mathrm dE_p$, soit $\vec F=-\overrightarrow{\mathrm{grad}}\,E_p$ ; en 1D, $F_x=-\dfrac{\mathrm dE_p}{\mathrm dx}$. Critère : $\overrightarrow{\mathrm{rot}}\,\vec F=\vec0$. $E_p$ est définie à une **constante près**. Exemples : poids $E_p=mgz$ ($Oz$ vertical ascendant) ; rappel élastique $E_p=\tfrac12k(\ell-\ell_0)^2$ ; gravitation $E_p=-\dfrac{GMm}{r}$ ; force de Coulomb $E_p=\dfrac{qq'}{4\pi\varepsilon_0r}$. Non conservatives : frottement de glissement $\vec f=-\mu N\,\vec v/\|\vec v\|$, frottement fluide $-\lambda\vec v$ (travail toujours négatif).
>
> **Énergie mécanique et sa variation**
>
> $E_m=E_c+E_p$. En séparant les forces conservatives (dans $E_p$) et les autres : $\boxed{\Delta E_m=W_{\rm nc}}$. Si $W_{\rm nc}=0$ (**forces non conservatives absentes ou ne travaillant pas**), $E_m=\text{cte}$. **Attention** : la réaction normale d'un support lisse et la tension d'un fil de pendule sont non conservatives (elles ne dérivent pas d'une $E_p$) mais **ne travaillent pas**, donc $E_m$ est conservée.
>
> **Énergie et dynamique : que donne chaque méthode ?**
>
> Énergie : $v(\text{position})$ directement, pas de dépendance au temps, pas d'information sur les forces de liaison. Newton projeté : $\vec a$, donc $t$, et les forces de liaison ($N$, $T$). Stratégie classique : **énergie pour $v$, puis Newton sur la direction normale pour $N$ ou $T$**, puis étude du signe de $N$ ou $T$ (contact, tension, décollage).
>
> **Diagramme d'énergie potentielle (mouvement à 1 degré de liberté)**
>
> $E_m=\tfrac12m\dot x^2+E_p(x)$ constante : le mouvement n'est possible que dans la zone $E_p(x)\le E_m$. **Points d'équilibre** : $E_p'(x_{\rm eq})=0$ ; **stable** si $E_p''(x_{\rm eq})>0$ (minimum), instable si $<0$. **Points de rebroussement** (vitesse nulle) : $E_p(x)=E_m$. Si la zone permise est bornée par deux rebroussements : **état lié** (oscillation) ; si elle est non bornée : **état de diffusion**. Petites oscillations : $E_p(x)\approx E_p(x_{\rm eq})+\tfrac12E_p''(x_{\rm eq})(x-x_{\rm eq})^2$, soit $\omega_0=\sqrt{E_p''(x_{\rm eq})/m}$ et $T_0=2\pi\sqrt{m/E_p''(x_{\rm eq})}$ ; on retrouve $k_{\rm eff}=E_p''(x_{\rm eq})$.
>
> **Mouvement le long d'une courbe lisse : réaction normale**
>
> Pour un point sur un rail lisse ou une sphère lisse : $E_m$ conservée ; projection de $m\vec a=m\vec g+\vec N$ sur la normale $\vec n$ (vers le centre de courbure) : $m\dfrac{v^2}{\rho}=N_n+mg_n$ (composantes algébriques selon $\vec n$). Le contact est maintenu tant que $N\ge0$ : **le décollage a lieu à l'instant où $N$ s'annule**.



> [!note]- 🧮 Outils mathématiques
> **Produit scalaire et intégrale curviligne**
>
> $\displaystyle\int_A^B\vec F\cdot\mathrm d\vec\ell$ ; pour $F$ constante, $\vec F\cdot\overrightarrow{AB}$ ; pour $F(x)\vec u_x$, $\displaystyle\int F(x)\,\mathrm dx$.
>
> **Primitives usuelles**
>
> $\displaystyle\int x\,\mathrm dx=\tfrac{x^2}2$, $\displaystyle\int x^n\mathrm dx=\tfrac{x^{n+1}}{n+1}$ ; $\displaystyle\int\dfrac{\mathrm dx}{x^2}=-\dfrac1x$ ; $\displaystyle\int\dfrac{\mathrm dx}{\sqrt{x^2-a^2}}=\operatorname{arcosh}\dfrac xa$.
>
> **Dérivée de $E_p$ et gradient en 1D**
>
> $F_x=-\dfrac{\mathrm dE_p}{\mathrm dx}$ ; équilibre $\dfrac{\mathrm dE_p}{\mathrm dx}=0$ ; stabilité par le signe de $\dfrac{\mathrm d^2E_p}{\mathrm dx^2}$.
>
> **Développement de Taylor à l'ordre 2**
>
> $E_p(x)\approx E_p(x_0)+\tfrac12E_p''(x_0)(x-x_0)^2$ autour d'un minimum ; $\cos\theta\approx1-\tfrac{\theta^2}2$.
>
> **Fonctions hyperboliques**
>
> $\cosh u=\dfrac{\mathrm e^u+\mathrm e^{-u}}2$, $\sinh u=\dfrac{\mathrm e^u-\mathrm e^{-u}}2$, $\cosh^2-\sinh^2=1$ ; $\ddot x=\kappa^2x\Rightarrow x=A\cosh\kappa t+B\sinh\kappa t$.
>
> **Conversion d'unités de vitesse et d'énergie**
>
> $1~\mathrm{km/h}=\dfrac1{3{,}6}~\mathrm{m/s}$ ; $1~\mathrm{kWh}=3{,}6~\mathrm{MJ}$ ; $1~\mathrm{eV}=1{,}6\times10^{-19}~\mathrm J$.



## Exercices

- [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex1-travail-d-une-force-constante|Exercice 1 — Travail d'une force constante]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex2-theoreme-de-l-energie-cinetique|Exercice 2 — Théorème de l'énergie cinétique]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex3-travail-d-une-force-de-rappel|Exercice 3 — Travail d'une force de rappel]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex4-looping-vertical|Exercice 4 — Looping vertical]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex5-bille-sur-une-sphere-angle-de-decollage|Exercice 5 — (*) Bille sur une sphère : angle de décollage]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex6-chaine-qui-glisse-d-une-table|Exercice 6 — (*) Chaîne qui glisse d'une table]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex7-puits-de-potentiel-de-lennard-jones|Exercice 7 — (*) Puits de potentiel de Lennard-Jones]]
