---
title: "Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · <a href="/pdfs/td1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td1_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/test.pdf" target="_blank" rel="noopener">📄 PDF</a> · <a href="/pdfs/td1_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 11. La valve du vélo : cycloïde d'une roue qui roule *(facultatif)*

*Difficulté ●●●●○ · ⏱ 55 min · Type : Approfondissement / Exercice non guidé*

Une roue de rayon $R$ roule **sans glisser** sur un sol horizontal rectiligne. Son centre $C$ se déplace à la vitesse constante $V$, parallèlement au sol.
On étudie le mouvement d'un point $M$ de la jante (la valve d'un pneu de vélo, par exemple) dans le référentiel du sol, muni d'un repère $Oxy$ : $Ox$ est horizontal, dans le sens du déplacement, $Oy$ est vertical ascendant, et l'origine $O$ est la position de $M$ à l'instant $t=0$, lorsque $M$ touche le sol. À cet instant, le centre est en $C_0=(0,R)$. On note $\theta(t)$ l'angle dont la roue a tourné depuis $t=0$ (la roue tourne dans le sens horaire, comme il se doit pour avancer vers $+Ox$), et $\omega=\dot\theta$ sa vitesse angulaire, supposée constante.

> [!question]+ 🎣 Accroche
> **La valve du vélo : quand est-elle immobile ? quand va-t-elle le plus vite ?**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *Vous roulez à 36 km/h ($=10~\mathrm{m/s}$). Est-il possible qu'un point de votre roue soit **immobile** par rapport au sol ? Y a-t-il un point qui va **plus vite que vous** ? Quelle forme prend la trajectoire de la valve vue depuis le trottoir ?*
>
> **Idée clé : composer translation et rotation.** Position de $M$ = position du centre + vecteur du centre à $M$ :
> $$\overrightarrow{OM}=\begin{pmatrix}Vt\\R\end{pmatrix}+R\begin{pmatrix}-\sin\omega t\\-\cos\omega t\end{pmatrix}\quad\text{avec }V=R\omega.$$
> La translation de $C$ à vitesse $V$ et la rotation de $M$ autour de $C$ à vitesse $R\omega=V$ s'ajoutent : elles s'**annulent** au point bas (vitesse nulle) et se **doublent** au sommet ($2V$).


> [!abstract]+ 📚 Prérequis
> **Composition de mouvements : $\vec v_M=\vec v_C+\vec v_{M/C}$**
>
> Si l'on décompose $\overrightarrow{OM}=\overrightarrow{OC}+\overrightarrow{CM}$, alors en dérivant : $\vec v_M=\vec v_C+\dfrac{\mathrm d\overrightarrow{CM}}{\mathrm dt}$. Le premier terme est la vitesse de translation du centre, le second est la vitesse due à la rotation autour du centre.
>
> **Dérivées de $\cos$ et $\sin$ composées avec $\omega t$**
>
> $\dfrac{\mathrm d}{\mathrm dt}\cos(\omega t)=-\omega\sin(\omega t)$ et $\dfrac{\mathrm d}{\mathrm dt}\sin(\omega t)=\omega\cos(\omega t)$.


> [!info]+ 🎯 Objectifs
> **Étudier une courbe paramétrée non triviale**
>
> Savoir déduire des coordonnées d'un point d'un solide en mouvement ses vecteurs vitesse et accélération, simplifier une norme à l'aide de formules trigonométriques, identifier les points particuliers de la trajectoire (vitesse nulle, vitesse maximale), calculer la longueur d'une arche par intégration et un rayon de courbure à partir de l'accélération normale.


> [!info]- 🧑‍🏫 Objectifs pédagogiques (enseignant)
> **Un exercice très riche autour d'une courbe célèbre**
>
> La cycloïde fournit des résultats **contre-intuitifs** que les étudiants peuvent vérifier : un point de la roue est instantanément **immobile** par rapport au sol, un autre va **deux fois plus vite** que le vélo, et l'accélération a un module constant. L'exercice mobilise la trigonométrie (angle moitié), le calcul d'une intégrale, l'orthogonalité de deux vecteurs et le concept de rayon de courbure : c'est le plus technique du TD. La question finale (boue qui se détache) relie la cinématique d'un point de la roue au tir de projectile des exercices précédents. Prévoir de laisser les étudiants conclure eux-mêmes que $\vec v\perp\overrightarrow{PM}$, ce qui introduit la notion de centre instantané de rotation.


> [!note]+ 📖 Point de cours
> **Roulement sans glissement**
>
> Une roue roule sans glisser quand le point de la roue en contact avec le sol a une **vitesse nulle** par rapport au sol. La longueur d'arc de jante qui a touché le sol est alors égale à la distance parcourue par le centre : $R\theta=Vt$, soit $V=R\omega$. Un point de la jante a une vitesse qui varie entre $0$ (au contact) et $2V$ (au sommet).
>
> **Cycloïde**
>
> La trajectoire d'un point de la jante d'une roue qui roule sans glisser est une **cycloïde**, de paramétrage $x=R(\omega t-\sin\omega t)$, $y=R(1-\cos\omega t)$. Une arche s'étend sur $2\pi R$ de large, $2R$ de haut, et mesure $8R$ de long.


> [!note]- 🧮 Outils mathématiques
> **Formules de l'angle moitié**
>
> $1-\cos\theta=2\sin^2\dfrac\theta2$ et $\sin\theta=2\sin\dfrac\theta2\cos\dfrac\theta2$. Elles simplifient $\|\vec v\|^2=R^2\omega^2(2-2\cos\omega t)=4R^2\omega^2\sin^2\dfrac{\omega t}2$ et la racine carrée.
>
> **Racine d'un carré et valeur absolue**
>
> $\sqrt{A^2}=|A|$. Sur une arche ($0\le\omega t\le2\pi$), $\sin(\omega t/2)\ge0$ : la valeur absolue disparaît.
>
> **Primitive d'un sinus de $\omega t/2$**
>
> $\displaystyle\int\sin\Big(\dfrac{\omega t}{2}\Big)\mathrm dt=-\dfrac2\omega\cos\Big(\dfrac{\omega t}2\Big)+\text{cte}$ (règle de la chaîne inversée : le facteur $\dfrac1{\omega/2}$).
>
> **Produit scalaire et orthogonalité**
>
> $\vec A\perp\vec B\iff\vec A\cdot\vec B=A_xB_x+A_yB_y=0$. Pour $\vec v=R\omega(1-\cos\omega t,\ \sin\omega t)$ et $\overrightarrow{PM}=R(-\sin\omega t,\ 1-\cos\omega t)$ : $v_xPM_x+v_yPM_y=R^2\omega[-(1-\cos\omega t)\sin\omega t+\sin\omega t(1-\cos\omega t)]=0$.
>
> **Accélération normale et rayon de courbure**
>
> Pour une trajectoire courbe, $\vec a=\dfrac{\mathrm dv}{\mathrm dt}\,\vec u_T+\dfrac{v^2}{\rho}\,\vec u_N$, où $\rho$ est le rayon de courbure. Quand $\vec a\perp\vec v$, $\vec a$ est purement normale : $\rho=\dfrac{v^2}{a}$.


**q1.** - [(a)] Justifier que la condition de non-glissement impose $V=R\omega$, puis donner la position $(x_C,y_C)$ du centre de la roue à l'instant $t$.
- [(b)] Déterminer les coordonnées $x(t)$ et $y(t)$ du point $M$.
- [(c)] Placer sur un graphique les positions de $M$ pour $\omega t=0,\ \pi/2,\ \pi,\ 3\pi/2,\ 2\pi$ et esquisser la trajectoire sur deux tours de roue.

> [!tip]- 💡 Coup de pouce
> Pour (a), la longueur d'arc de jante qui touche le sol pendant $t$ est $R\theta$ ; elle doit être égale à la distance parcourue par le centre. Pour (b), écrivez $\overrightarrow{OM}=\overrightarrow{OC}+\overrightarrow{CM}$ : au point bas, $\overrightarrow{CM}=-R\,\vec u_y$ ; après une rotation horaire de $\theta$, $\overrightarrow{CM}=R\,(-\sin\theta,\ -\cos\theta)$. Vérifiez qu'à $t=0$ on retrouve $M=O$.


> [!success]- ✅ Correction
> $V=R\omega$ ; $C=(R\omega t,\ R)$ ; $x(t)=R(\omega t-\sin\omega t)$, $y(t)=R(1-\cos\omega t)$ : cycloïde, arches de largeur $2\pi R$ et de hauteur $2R$.


> [!example]- 📝 Solution détaillée
> **(a) Non-glissement et position du centre**
>
> Sans glissement, l'arc de jante de longueur $R\theta$ qui a touché le sol est déroulé sur la distance $Vt$ parcourue par le centre : $R\theta=Vt$. Comme $\theta=\omega t$, on obtient
> $$\boxed{V=R\,\omega}.$$
> Le centre reste à la hauteur $R$ et avance à vitesse constante :
> $$x_C(t)=V\,t=R\,\omega\,t,\qquad y_C(t)=R.$$
>
> **(b) Coordonnées du point $M$**
>
> À $t=0$, $M$ est sous le centre : $\overrightarrow{CM}(0)=-R\,\vec u_y$. La roue tourne dans le sens horaire de l'angle $\omega t$ ; le vecteur $\overrightarrow{CM}$ tourne avec elle :
> $$\overrightarrow{CM}(t)=R\,(-\sin\omega t)\,\vec u_x+R\,(-\cos\omega t)\,\vec u_y .$$
> (À $t$ petit, $M$ remonte et recule par rapport au centre : cohérent avec un sens horaire.) D'où
> $$\boxed{x(t)=R\,\omega\,t-R\sin\omega t=R(\omega t-\sin\omega t)},\qquad\boxed{y(t)=R-R\cos\omega t=R(1-\cos\omega t)}.$$
> Vérification : à $t=0$, $x=y=0$ ($M=O$). $\surd$
>
> **(c) Positions remarquables et allure de la trajectoire**
>
> $$\begin{array}{c|ccccc}
> \omega t&0&\pi/2&\pi&3\pi/2&2\pi\\\hline
> x/R&0&\pi/2-1\approx0{,}57&\pi\approx3{,}14&3\pi/2+1\approx5{,}71&2\pi\approx6{,}28\\
> y/R&0&1&2&1&0
> \end{array}$$
> La trajectoire est une succession d'arches identiques de **largeur** $2\pi R$ et de **hauteur** $2R$. Chaque arche commence et finit au sol par un point de **rebroussement** (tangente verticale) ; le sommet de l'arche, en $\omega t=\pi$, est à la hauteur $2R$ (diamètre de la roue).


**q2.** - [(d)] Calculer le vecteur vitesse $\vec v$ de $M$ et sa norme (la mettre sous la forme $2V\left|\sin\dfrac{\omega t}{2}\right|$).
- [(e)] Calculer le vecteur accélération $\vec a$ et sa norme. Que remarque-t-on ?
- [(f)] En quels points la vitesse est-elle nulle ? maximale ? Que vaut alors l'accélération ? Commenter.

> [!tip]- 💡 Coup de pouce
> Dérivez chaque coordonnée une fois, puis deux fois. Pour simplifier $\|\vec v\|$, utilisez $1-\cos\theta=2\sin^2(\theta/2)$.


> [!success]- ✅ Correction
> $\vec v=R\omega\,(1-\cos\omega t,\ \sin\omega t)$, $\|\vec v\|=2V|\sin(\omega t/2)|$ ; $\vec a=R\omega^2(\sin\omega t,\ \cos\omega t)$, $\|\vec a\|=R\omega^2=V^2/R$ constante ; $v=0$ au contact ($\omega t=2k\pi$), $v_{\max}=2V$ au sommet ($\omega t=(2k+1)\pi$).


> [!example]- 📝 Solution détaillée
> **(d) Vitesse**
>
> $$\vec v=\dot x\,\vec u_x+\dot y\,\vec u_y=\boxed{R\omega\,(1-\cos\omega t)\,\vec u_x+R\omega\sin\omega t\,\vec u_y}.$$
> Norme :
> $$\|\vec v\|^2=R^2\omega^2\big[(1-\cos\omega t)^2+\sin^2\omega t\big]=R^2\omega^2\,(2-2\cos\omega t)=4R^2\omega^2\sin^2\frac{\omega t}{2},$$
> d'où
> $$\boxed{\|\vec v\|=2R\omega\left|\sin\frac{\omega t}{2}\right|=2V\left|\sin\frac{\omega t}{2}\right|}.$$
>
> **(e) Accélération**
>
> $$\vec a=\ddot x\,\vec u_x+\ddot y\,\vec u_y=\boxed{R\omega^2\sin\omega t\,\vec u_x+R\omega^2\cos\omega t\,\vec u_y},\qquad\|\vec a\|=R\omega^2=\frac{V^2}{R}.$$
> La norme est **constante**. De plus, le vecteur $R\omega^2(\sin\omega t,\cos\omega t)$ est colinéaire à $\overrightarrow{MC}=R(\sin\omega t,\cos\omega t)$ : l'accélération est dirigée vers le **centre de la roue**, comme dans un mouvement circulaire uniforme (c'est normal : c'est l'accélération due à la rotation autour de $C$, celle de la translation étant nulle).
>
> **(f) Points remarquables**
>
> **Vitesse nulle** : $\sin(\omega t/2)=0$, soit $\omega t=2k\pi$ : $M$ est alors au contact du sol, en $x=2k\pi R$, $y=0$. Il est **instantanément immobile** par rapport au sol. Mais l'accélération y vaut $\vec a=R\omega^2\,\vec u_y\ne\vec0$ : le point repart verticalement vers le haut (rebroussement).
>
> **Vitesse maximale** : $|\sin(\omega t/2)|=1$, soit $\omega t=(2k+1)\pi$ : $M$ est au sommet, $y=2R$, et $\|\vec v\|=\boxed{2V}$, dirigée suivant $+\vec u_x$. L'accélération y vaut $-R\omega^2\,\vec u_y$ (vers le bas, vers le centre).
>
> Un point du haut de la roue va donc **deux fois plus vite** que le vélo ; un point du bas est **à l'arrêt** par rapport au sol.


**q3.** - [(g)] Soit $P(t)=(R\omega t,\,0)$ le point du sol qui est, à l'instant $t$, en contact avec la roue. Montrer que $\vec v\perp\overrightarrow{PM}$ et que $\|\vec v\|=\omega\,PM$. Interpréter.
- [(h)] Calculer la longueur $L$ d'une arche de la trajectoire et la comparer à la distance parcourue par le centre pendant le même temps.
- [(i)] Calculer le rayon de courbure $\rho_{\rm top}$ de la trajectoire au sommet.
- [(j)] Un cycliste roule à $V=36~\mathrm{km/h}$ sur des roues de rayon $R=0{,}35$ m. Au sommet de la roue, un grain de boue se détache. En supposant qu'il part avec la vitesse de ce point, où retombe-t-il (par rapport au point de détachement) ?

> [!tip]- 💡 Coup de pouce
> (g) : $\overrightarrow{PM}=R(-\sin\omega t,\ 1-\cos\omega t)$. Calculez le produit scalaire, puis la norme. (h) : $L=\int_0^{2\pi/\omega}\|\vec v\|\,\mathrm dt$. (i) : au sommet, la vitesse est horizontale et l'accélération verticale : $\vec a$ est purement normale, $a=v^2/\rho$. (j) : le grain a la vitesse de $M$ au sommet ($2V$, horizontale) à la hauteur $2R$ : c'est un tir horizontal.


> [!success]- ✅ Correction
> $\vec v\cdot\overrightarrow{PM}=0$ et $\|\vec v\|=\omega\,PM$ : rotation instantanée autour du point de contact ; $L=8R$ (contre $2\pi R\approx6{,}28R$ pour le centre) ; $\rho_{\rm top}=4R$ ; boue : $v=20~\mathrm{m/s}$, hauteur $0{,}70$ m, retombe à $\approx7{,}6$ m devant le point de détachement.


> [!example]- 📝 Solution détaillée
> **(g) Rotation autour du point de contact**
>
> $\overrightarrow{PM}=\overrightarrow{OM}-\overrightarrow{OP}=R(-\sin\omega t)\,\vec u_x+R(1-\cos\omega t)\,\vec u_y$. Produit scalaire :
> $$\vec v\cdot\overrightarrow{PM}=R^2\omega\big[-(1-\cos\omega t)\sin\omega t+\sin\omega t\,(1-\cos\omega t)\big]=0 .$$
> Donc $\vec v\perp\overrightarrow{PM}$. Norme : $PM=R\sqrt{\sin^2\omega t+(1-\cos\omega t)^2}=R\sqrt{2-2\cos\omega t}=2R\left|\sin\dfrac{\omega t}2\right|$, d'où $\|\vec v\|=\omega\,PM$.
>
> Interprétation : à chaque instant, le mouvement de la roue est une **rotation de vitesse angulaire $\omega$ autour du point de contact $P$** (vitesse nulle). Ce point s'appelle le **centre instantané de rotation**. Au sommet, $PM=2R$ et $v=2R\omega=2V$ : on retrouve le résultat de (f).
>
> **(h) Longueur d'une arche**
>
> Une arche correspond à $0\le\omega t\le2\pi$, soit $0\le t\le T=2\pi/\omega$ (où $\sin(\omega t/2)\ge0$) :
> $$L=\int_0^{T}2R\omega\sin\frac{\omega t}{2}\,\mathrm dt=2R\omega\left[-\frac2\omega\cos\frac{\omega t}{2}\right]_0^{T}=4R\,\big[-\cos\pi+\cos0\big]=\boxed{8R}.$$
> Pendant le même temps, le centre parcourt $VT=2\pi R\approx6{,}28\,R$. Le point $M$ parcourt donc une distance $\dfrac{8}{2\pi}=\dfrac4\pi\approx1{,}27$ fois plus grande : le chemin de la valve est plus long que celui du centre.
>
> **(i) Rayon de courbure au sommet**
>
> En $\omega t=\pi$ : $\vec v=2R\omega\,\vec u_x$ (horizontale) et $\vec a=-R\omega^2\,\vec u_y$ (verticale) : $\vec a\perp\vec v$, donc l'accélération est **purement normale** et $a=\dfrac{v^2}{\rho}$ :
> $$\rho_{\rm top}=\frac{v^2}{a}=\frac{4R^2\omega^2}{R\omega^2}=\boxed{4R}.$$
> Le sommet de la cycloïde est donc beaucoup moins courbé que la roue elle-même (qui a un rayon $R$).
>
> **(j) Grain de boue détaché au sommet**
>
> Conversion : $V=36/3{,}6=10~\mathrm{m/s}$. Au sommet, le grain part avec la vitesse de $M$ : $v_0=2V=20~\mathrm{m/s}$ horizontale, à la hauteur $h=2R=0{,}70$ m. C'est un tir horizontal :
> $$t_c=\sqrt{\frac{2h}{g}}=\sqrt{\frac{2\times0{,}70}{9{,}81}}\approx0{,}378~\text{s},\qquad d=v_0\,t_c\approx20\times0{,}378\approx\boxed{7{,}6~\text{m}}.$$
> Le grain retombe à environ $7{,}6$ m devant le point de détachement. Pendant ce temps le vélo a avancé de $V\,t_c\approx3{,}8$ m : le grain atterrit donc $\approx3{,}8$ m **devant la roue**, comme on s'y attend puisque, dans le référentiel du vélo, il part à la vitesse $V$ vers l'avant.


> [!warning]- 🪤 Écueils classiques
> **Oublier la translation du centre**
>
> Écrire $x=-R\sin\omega t$, $y=R-R\cos\omega t$ (seule la rotation autour du centre) donne un **cercle**, pas une cycloïde. La translation de $C$ ajoute $Vt=R\omega t$ à l'abscisse.
>
> **Se tromper dans le signe de la rotation**
>
> Pour une roue qui avance vers $+Ox$, la rotation est horaire. Au point bas, un point de la roue recule par rapport au centre (composante $-R\sin\omega t$), ce qui permet de vérifier que $v_x=0$ au contact. Un signe $+R\sin\omega t$ donnerait $v_x=2V$ au contact : absurde.
>
> **Croire que la vitesse est nulle ET l'accélération nulle au contact**
>
> Au contact, $\vec v=\vec0$ mais $\vec a=R\omega^2\,\vec u_y\neq\vec0$ : la valve accélère vers le haut et repart verticalement (c'est le **point de rebroussement** de la cycloïde).
>
> **Simplifier $\sqrt{2-2\cos\omega t}$ sans valeur absolue**
>
> $\sqrt{2-2\cos\omega t}=2\left|\sin\dfrac{\omega t}{2}\right|$ : la valeur absolue est indispensable pour que la norme reste positive sur toute l'arche (et au-delà).


> [!tip]- 🎙️ Conseils d'animation
> **Manipulation en classe**
>
> Coller un point lumineux sur le bord d'un disque et filmer en pose longue le roulement du disque : la cycloïde apparaît. Comparer la photographie avec le tracé théorique. Un pot de peinture roulé sur le sol avec un point marqué fonctionne aussi.
>
> **Faire deviner avant de calculer**
>
> Demander : « À quel instant la valve est-elle immobile par rapport au sol ? Et quand va-t-elle le plus vite ? » Les étudiants répondent souvent « jamais immobile » et « toujours à $V$ ». La réponse $0$ et $2V$ crée la surprise.


> [!note]- 🔗 Liens avec d'autres disciplines
> **Mathématiques**
>
> Courbes paramétrées, cycloïde, longueur d'arc $\displaystyle\int\|\vec v\|\,\mathrm dt$, rayon de courbure ; la cycloïde est aussi solution des problèmes de la brachistochrone et de la tautochrone.
>
> **Transports ferroviaires**
>
> Le boudin d'une roue de train a une trajectoire de trochoïde allongée : il **recule** un instant par rapport au sol à chaque tour, ce qui explique en partie l'usure du rail.
>
> **Horlogerie et mécanique**
>
> Huygens a proposé un pendule dont la masse suit une cycloïde pour obtenir une période indépendante de l'amplitude (isochronisme). Les engrenages utilisent des profils de dents en épicycloïdes et en développantes de cercle.
>
> **Architecture**
>
> Les voûtes en arc de cycloïde du musée Kimbell (Fort Worth) de Louis Kahn.
>
> **Sport**
>
> Eau projetée par les roues d'un vélo ou d'une voiture : les gouttes quittent la roue avec une vitesse tangente, qui peut atteindre $2V$ dans le référentiel du sol.


> [!success]- 🏁 Bilan
> **Roue qui roule : cycloïde, $v\in[0,2V]$, $a=\text{cte}$**
>
> Pour une roue de rayon $R$ roulant sans glisser à vitesse $V=R\omega$ : $x=R(\omega t-\sin\omega t)$, $y=R(1-\cos\omega t)$ ; $\vec v=R\omega\,(1-\cos\omega t,\ \sin\omega t)$, $\|\vec v\|=2V|\sin(\omega t/2)|$ ; $\vec a=R\omega^2(\sin\omega t,\ \cos\omega t)$, $\|\vec a\|=R\omega^2$ constante, dirigée vers le centre de la roue. La vitesse est nulle au contact, maximale ($2V$) au sommet ; la longueur d'une arche vaut $8R$ ; le rayon de courbure au sommet vaut $4R$.


> [!question]- 🔭 Aller plus loin — CPGE : Retrouver les résultats par la composition des vitesses
> Vérifier que $\vec v_M=\vec v_C+\vec\Omega\wedge\overrightarrow{CM}$ avec $\vec\Omega=-\omega\,\vec u_z$ redonne l'expression de $\vec v$. En déduire que la vitesse est nulle au point de contact et vaut $2V$ au sommet sans calculer de dérivées de $\sin$ et $\cos$.


> [!question]- 🔭 Aller plus loin — Licence : Rayon de courbure en tout point de la cycloïde
> Le rayon de courbure s'écrit $\rho=\dfrac{\|\vec v\|^3}{\|\vec v\wedge\vec a\|}$. Calculer $\vec v\wedge\vec a$ pour la cycloïde et montrer que $\rho(t)=4R\left|\sin\dfrac{\omega t}{2}\right|$. Vérifier $\rho=4R$ au sommet et $\rho=0$ au point de rebroussement.


> [!question]- 🔭 Aller plus loin — Master : Trochoïdes : un point qui n'est pas sur la jante
> Un point à la distance $b$ du centre a pour coordonnées $x=R\omega t-b\sin\omega t$, $y=R-b\cos\omega t$ : c'est une **trochoïde**. Pour $b>R$ (boudin d'une roue de train, qui dépasse la roue), la trajectoire présente des **boucles** : au point bas, la vitesse horizontale est $R\omega-b\omega<0$, le boudin **recule** par rapport au sol. Pour $b<R$ (point à l'intérieur de la roue), la trochoïde est « raccourcie » et ne comporte pas de rebroussement.


> [!question]- 🔭 Aller plus loin — Doctorat : Brachistochrone et tautochrone
> La cycloïde (retournée) est à la fois la courbe de plus rapide descente (brachistochrone : Jean Bernoulli, 1696) et la courbe pour laquelle le temps de chute ne dépend pas du point de départ (tautochrone : Huygens, 1659). Retrouver la brachistochrone par le calcul des variations : minimiser $\displaystyle\int\dfrac{\sqrt{1+y'^2}}{\sqrt{2gy}}\,\mathrm dx$ avec $y$ mesuré vers le bas.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex2-seance-1-exploitation-de-la-chronophotographie-vitesses-forces-lois-de-newton|Exercice 2 — Séance 1 -- Exploitation de la chronophotographie : vitesses, forces, lois de Newton]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex6-parabole-de-s-rete-et-tir-sur-une-pente|Exercice 6 — Parabole de sûreté et tir sur une pente]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]]

