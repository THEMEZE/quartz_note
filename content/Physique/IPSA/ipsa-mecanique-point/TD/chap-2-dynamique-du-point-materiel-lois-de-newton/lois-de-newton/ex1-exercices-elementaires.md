---
title: "Exercice 1 — Exercices élémentaires"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 1. Exercices élémentaires

On se place dans le référentiel terrestre, supposé galiléen, muni d'un repère cartésien $Oxyz$ ($Oz$ vertical ascendant). On prendra $g=9{,}81~\mathrm{m\,s^{-2}}$. Six petits problèmes indépendants, qui servent à installer la méthode : **système, référentiel, bilan des forces, schéma, loi de Newton, projection**.

**q1.** - [1/] Un bloc de $630$ g est suspendu au plafond par deux cordes inclinées d'angles $\theta_1$ et $\theta_2$ avec l'horizontale (voir figure). Déterminer littéralement, puis numériquement, le module de la tension dans chaque corde.
- [2/] On suspend un objet au bout d'un ressort vertical de raideur $k=16$ S.I. L'allongement est $\Delta\ell=5{,}4$ cm. Déterminer la masse $m$ de l'objet.

> [!tip]- 💡 Coup de pouce
> À l'équilibre, $\sum\vec F=\vec0$ : projetez sur l'horizontale puis sur la verticale. Pour le ressort, la force de rappel équilibre le poids.


> [!success]- ✅ Correction
> 1/ $T_1=\dfrac{mg\cos\theta_2}{\sin(\theta_1+\theta_2)}$, $T_2=\dfrac{mg\cos\theta_1}{\sin(\theta_1+\theta_2)}$ ; pour $\theta_1=\theta_2=30^\circ$ : $T_1=T_2=mg\approx6{,}18$ N. 2/ $m=k\Delta\ell/g\approx0{,}088$ kg $=88$ g.


> [!example]- 📝 Solution détaillée
> **1/ Bloc suspendu par deux cordes**
>
> Système : le bloc. Forces : poids $-mg\,\vec u_z$, tensions $\vec T_1,\vec T_2$ de normes $T_1,T_2$, la corde 1 à gauche, la corde 2 à droite. À l'équilibre :
> $$\text{(Ox)}:\ -T_1\cos\theta_1+T_2\cos\theta_2=0,\qquad\text{(Oz)}:\ T_1\sin\theta_1+T_2\sin\theta_2-mg=0.$$
> De la première, $T_2=T_1\cos\theta_1/\cos\theta_2$. En reportant :
> $$T_1\,\frac{\sin\theta_1\cos\theta_2+\cos\theta_1\sin\theta_2}{\cos\theta_2}=mg\ \Rightarrow\ \boxed{T_1=\frac{mg\cos\theta_2}{\sin(\theta_1+\theta_2)}},\quad\boxed{T_2=\frac{mg\cos\theta_1}{\sin(\theta_1+\theta_2)}}.$$
> **Application** (la figure n'étant pas reproduite ici, on prend $\theta_1=\theta_2=30^\circ$ ; remplacer par les angles du sujet) : $mg=0{,}630\times9{,}81\approx6{,}18$ N et $T_1=T_2=\dfrac{mg}{2\sin30^\circ}=\boxed{6{,}18~\text{N}}$. Contrôle : si $\theta\to0$, $T\to\infty$ (une corde horizontale ne peut jamais porter le poids).
>
> **2/ Masse au bout du ressort**
>
> À l'équilibre, la force de rappel $k\Delta\ell$ (vers le haut) compense le poids : $k\Delta\ell=mg$, donc
> $$m=\frac{k\,\Delta\ell}{g}=\frac{16\times0{,}054}{9{,}81}\approx\boxed{0{,}088~\text{kg}\approx88~\text{g}}.$$


**q2.** - [3/] Dans le plan $Oxy$, une particule de masse $m=370$ g est soumise à deux forces : $\vec F_1=3\,\vec u_x-\vec u_y$ (en N) et $\vec F_2$ de norme $3$ N formant l'angle de $60^\circ$ avec l'axe $Ox$ (dirigée vers les $y$ positifs). Quelle est l'accélération de la particule ?
- [4/] Un ascenseur dont la cabine pèse $1300$ kg monte du rez-de-chaussée au premier étage. Il démarre avec une accélération de $1{,}5~\mathrm{m\,s^{-2}}$. (a) Avec la 2\textsuperscript{e} loi de Newton, déterminer la tension du câble au démarrage. (b) Que devient-elle lorsque la vitesse est constante ?

> [!tip]- 💡 Coup de pouce
> Pour 3/, additionnez les composantes des forces puis divisez par $m$. Pour 4/, projetez sur $Oz$ ascendant : $T-mg=ma$.


> [!success]- ✅ Correction
> 3/ $\vec a\approx(12{,}2\,\vec u_x+4{,}32\,\vec u_y)~\mathrm{m\,s^{-2}}$, $a\approx12{,}9~\mathrm{m\,s^{-2}}$, à $19{,}6^\circ$ de $Ox$. 4/ (a) $T=m(g+a)\approx14{,}7$ kN ; (b) $T=mg\approx12{,}8$ kN.


> [!example]- 📝 Solution détaillée
> **3/ Somme de deux forces**
>
> $\vec F_2=3\cos60^\circ\,\vec u_x+3\sin60^\circ\,\vec u_y=1{,}5\,\vec u_x+2{,}60\,\vec u_y$. Somme : $\sum\vec F=4{,}5\,\vec u_x+1{,}60\,\vec u_y$ N. Avec $m=0{,}370$ kg :
> $$\vec a=\frac{\sum\vec F}{m}\approx\boxed{12{,}2\,\vec u_x+4{,}32\,\vec u_y~\mathrm{m\,s^{-2}}},\qquad\|\vec a\|\approx12{,}9~\mathrm{m\,s^{-2}},$$
> dirigée à $\arctan(4{,}32/12{,}2)\approx19{,}6^\circ$ de $Ox$ (dans le sens de la force résultante).
>
> **4/ (a) Ascenseur au démarrage**
>
> Système : cabine. Forces : poids $-mg\,\vec u_z$ et tension $T\,\vec u_z$. Projection de $\sum\vec F=m\vec a$ sur $Oz$ : $T-mg=ma$, donc
> $$T=m(g+a)=1300\times(9{,}81+1{,}5)\approx\boxed{1{,}47\times10^4~\text{N}}.$$
> Le poids vaut $mg\approx1{,}28\times10^4$ N : la tension est $\approx15\%$ plus grande.
>
> **4/ (b) Vitesse constante**
>
> Vitesse constante $\Rightarrow\vec a=\vec0$ $\Rightarrow T=mg\approx\boxed{1{,}28\times10^4~\text{N}}$. La tension ne dépend pas de la vitesse, seulement de l'accélération.


**q3.** - [5/] Estimer le temps de chute d'une pomme qui se détache d'un arbre, sans vitesse initiale, d'une hauteur de $10$ m.
- [6/] Un skieur part sans vitesse initiale et descend une pente inclinée de $30^\circ$. Quelle est son accélération et sa vitesse après $5$ s ? On néglige les frottements.

> [!tip]- 💡 Coup de pouce
> 5/ : seule la pesanteur agit, donc $a=g$ vers le bas. 6/ : projetez le poids le long de la pente ; la réaction du sol est perpendiculaire à la pente.


> [!success]- ✅ Correction
> 5/ $t=\sqrt{2h/g}\approx1{,}4$ s. 6/ $a=g\sin30^\circ\approx4{,}9~\mathrm{m\,s^{-2}}$, $v(5~\mathrm s)\approx24{,}5~\mathrm{m/s}\approx88$ km/h.


> [!example]- 📝 Solution détaillée
> **5/ Chute de la pomme**
>
> Poids seul : $\ddot z=-g$, $z(t)=h-\tfrac12gt^2$, d'où $z(t)=0$ pour
> $$t=\sqrt{\frac{2h}{g}}=\sqrt{\frac{20}{9{,}81}}\approx\boxed{1{,}4~\text{s}}.$$
>
> **6/ Skieur sur la pente**
>
> Axe $Ox$ le long de la pente, vers le bas. Forces : poids, réaction normale $\vec N$ (perpendiculaire à la pente). Projection sur $Ox$ : $ma=mg\sin\alpha$, d'où
> $$a=g\sin\alpha=9{,}81\times\tfrac12\approx\boxed{4{,}9~\mathrm{m\,s^{-2}}},\qquad v(t)=at\Rightarrow v(5~\text{s})\approx\boxed{24{,}5~\mathrm{m/s}}\ (\approx88~\text{km/h}).$$
> La masse n'intervient pas. La valeur est surestimée : les frottements de l'air et de la neige limitent la vitesse réelle.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex3-machine-d-atwood|Exercice 3 — Machine d'Atwood]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex7-chute-avec-frottement-fluide-vitesse-limite|Exercice 7 — Chute avec frottement fluide : vitesse limite]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]]

