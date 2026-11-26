---
title: "Exercice 1 — Exercices élémentaires"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td4_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 1. Exercices élémentaires

*⭐ Indispensable · Difficulté ●○○○○ · ⏱ 40 min · Type : Cours actif / Application directe*

On se place dans le référentiel terrestre, supposé galiléen, muni d'un repère cartésien $Oxyz$ ($Oz$ vertical ascendant). On prendra $g=9{,}81~\mathrm{m\,s^{-2}}$. Six petits problèmes indépendants, qui servent à installer la méthode : **système, référentiel, bilan des forces, schéma, loi de Newton, projection**.


> [!question]- 🪝 Accroche
> **Quand un ascenseur monte, le câble tire-t-il plus fort ?**
>
> *Durée de l'introduction : 3 min*
>
> *Un ascenseur monte à vitesse constante : la tension du câble est-elle **plus grande, égale ou plus petite** que le poids de la cabine ? Et au démarrage ? Et quand la cabine s'arrête ?*
>
> **Idée clé : c'est l'accélération qui compte, pas la vitesse.** $\sum\vec F=m\vec a$. À vitesse constante, $\vec a=\vec0$ et la tension égale le poids ; au démarrage $T=m(g+a)$, à l'arrêt $T=m(g-|a|)$.




> [!abstract]- 🧠 À savoir avant
> **Les trois lois de Newton**
>
> 1\textsuperscript{re} loi : dans un référentiel galiléen, un point matériel isolé ou pseudo-isolé ($\sum\vec F=\vec0$) est au repos ou en mouvement rectiligne uniforme. 2\textsuperscript{e} loi : $\sum\vec F=m\,\vec a$ (masse constante). 3\textsuperscript{e} loi : $\vec F_{A\to B}=-\vec F_{B\to A}$.
>
> **Forces usuelles**
>
> Poids $\vec P=m\vec g$ ; tension d'un fil idéal (dirigée le long du fil, vers le fil) ; force de rappel d'un ressort $\vec F=-k(\ell-\ell_0)\,\vec u$ avec $\vec u$ dirigé du point fixe vers la masse ; réaction du support.




> [!info]- 🎯 Ce que tu sauras faire
> **Appliquer la méthode générale de la dynamique**
>
> Savoir définir le système, choisir le référentiel et le repère, faire le bilan des forces, projeter la loi de Newton, résoudre, puis commenter l'ordre de grandeur du résultat.




> [!info]- 🧑‍🏫 Objectifs pédagogiques
> **Six cas pour installer les réflexes**
>
> Équilibre (1, 2), somme vectorielle (3), accélération non nulle (4, 6), chute libre (5). La question 4(b) est un classique : **vitesse constante $\Rightarrow$ $\vec a=\vec0$ $\Rightarrow$ tension égale au poids**, contre l'intuition « il monte donc la tension est plus grande ». Les questions 1 et 3 dépendent d'une figure ou d'un angle : adapter les données au sujet distribué.




> [!tip]- 📖 Rappel de cours
> **Méthode en cinq étapes**
>
> (1) Système et référentiel. (2) Repère et schéma. (3) Bilan des forces, toutes représentées. (4) $\sum\vec F=m\vec a$ puis projection sur chaque axe. (5) Résolution littérale, application numérique, vérification.




> [!note]- 🧮 Outils mathématiques
> **Projection d'un vecteur**
>
> Un vecteur de norme $F$ faisant l'angle $\varphi$ avec $Ox$ a pour composantes $(F\cos\varphi,\ F\sin\varphi)$ ; pour la pente $\alpha$ d'un plan incliné, le poids se projette en $mg\sin\alpha$ le long du plan et $mg\cos\alpha$ perpendiculairement.
>
> **Résolution d'un système de deux équations**
>
> Pour deux cordes : deux équations (horizontale, verticale), deux inconnues $T_1,T_2$ ; on élimine l'une par substitution ou par combinaison.
>
> **Chute libre depuis le repos**
>
> $h=\tfrac12gt^2\Rightarrow t=\sqrt{2h/g}$.



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




> [!note]- 🔗 Liens avec d'autres disciplines
> **Génie civil**
>
> Dimensionnement de câbles (tension $=$ poids $\times$ facteur dynamique $1+a/g$), haubans et ponts suspendus.
>
> **Sport**
>
> Ski : l'accélération sur une pente sans frottement ne dépend que de l'angle ; les frottements limitent la vitesse en pratique.




> [!warning]- 🪤 Écueils classiques
> **Ajouter une « force de mouvement »**
>
> Il n'existe pas de force « dans le sens du mouvement » : à vitesse constante, la somme des forces est nulle. Seules des forces exercées par des objets identifiables figurent sur le bilan.
>
> **Masse en grammes**
>
> $630$ g $=0{,}630$ kg, $370$ g $=0{,}370$ kg, $5{,}4$ cm $=0{,}054$ m : convertir avant tout calcul.
>
> **Mélanger masse et poids**
>
> Le poids $mg$ est une force (N), la masse $m$ une quantité de matière (kg). La cabine de $1300$ kg a un poids de $12{,}8$ kN.




> [!tip]- 🎙️ Conseils d'animation
> **Un schéma avant toute équation**
>
> Exiger un schéma avec repère et forces pour chaque question, même triviale. Faire vérifier le bilan par le voisin avant de projeter.




> [!success]- 🏁 Bilan pédagogique
> **Ce qu'on retient**
>
> Équilibre $\Rightarrow\sum\vec F=\vec0$ ; mouvement uniforme $\Rightarrow\sum\vec F=\vec0$ aussi ; accélération $\Rightarrow\sum\vec F=m\vec a$. Dans un ascenseur qui accélère vers le haut, $T=m(g+a)>mg$ ; à vitesse constante, $T=mg$. Sur un plan incliné sans frottement, $a=g\sin\alpha$, indépendante de la masse.




> [!question]- 🔭 Aller plus loin — CPGE : Poids apparent dans l'ascenseur
> Une personne de $70$ kg est sur une balance dans l'ascenseur de la question 4. Quelle valeur lit-on au démarrage, à vitesse constante, puis au freinage ($a=-1{,}5~\mathrm{m\,s^{-2}}$) ? Que lit-on si le câble casse ?




> [!question]- 🔭 Aller plus loin — Licence : Référentiel non galiléen
> Refaire 4(a) dans le référentiel de la cabine (non galiléen) en introduisant la force d'inertie $-m\vec a_e$, et retrouver la même tension.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex3-machine-d-atwood|Exercice 3 — Machine d'Atwood]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex7-chute-avec-frottement-fluide-vitesse-limite|Exercice 7 — Chute avec frottement fluide : vitesse limite]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex4-systeme-pendule-bloc|Exercice 4 — (*) Système pendule-bloc]]


