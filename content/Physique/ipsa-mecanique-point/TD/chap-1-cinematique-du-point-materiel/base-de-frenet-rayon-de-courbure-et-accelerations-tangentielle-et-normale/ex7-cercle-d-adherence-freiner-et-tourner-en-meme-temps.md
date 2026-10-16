---
title: "Exercice 7 — Cercle d'adhérence : freiner et tourner en même temps"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/index|⬅ Retour]] · <a href="/pdfs/td3_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td3_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td3_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td3_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 7. Cercle d'adhérence : freiner et tourner en même temps *(facultatif)*

Une voiture roule sur une route horizontale. Les seules forces horizontales qu'elle subit sont les forces de
frottement des pneus sur le sol, dont la norme est bornée par l'**adhérence** : $F\le\mu\,mg$ où $\mu$ est le
coefficient d'adhérence (admis ici ; sa justification relève de la dynamique). D'après la deuxième loi de Newton, la
norme de l'accélération est donc limitée :
$$\|\vec a\|=\sqrt{a_T^2+a_N^2}\le\mu g.$$
Dans le plan $(a_N,a_T)$, les accélérations réalisables sont donc à l'intérieur du **cercle d'adhérence** de rayon
$\mu g$ : tout ce qu'on utilise pour tourner ($a_N=v^2/R$) n'est plus disponible pour freiner ($a_T<0$) ou accélérer
($a_T>0$). On prendra $g=9{,}81\ \mathrm{m\,s^{-2}}$ et $\mu=0{,}8$ (route sèche), sauf mention contraire.

**q1.** **1/ Virage stationnaire et freinage droit.**


(a) Une voiture roule à vitesse constante sur un arc de cercle de rayon $R$. Établir la vitesse maximale $v_{\max}$ en fonction de $\mu$, $g$ et $R$. Application numérique pour $R=50\ \mathrm m$ et $\mu=0{,}8\ ;\ 0{,}5\ ;\ 0{,}1$.

(b) En ligne droite, établir la distance de freinage $d$ en fonction de $v_0$, $\mu$ et $g$. Calculer $d$ pour $v_0=90\ \mathrm{km/h}$ sur route sèche ($\mu=0{,}8$) et sur verglas ($\mu=0{,}1$).

> [!tip]- 💡 Coup de pouce
> (a) $a_T=0$ : $a_N=v^2/R\le\mu g$. (b) $a_N=0$ : $|a_T|\le\mu g$ ; utiliser le mouvement uniformément décéléré.


> [!success]- ✅ Correction
> (a) $v_{\max}=\sqrt{\mu gR}$ : $19{,}8\ \mathrm{m/s}\ (71\ \mathrm{km/h})$, $15{,}7\ \mathrm{m/s}\ (56\ \mathrm{km/h})$, $7{,}0\ \mathrm{m/s}\ (25\ \mathrm{km/h})$. (b) $d=\dfrac{v_0^2}{2\mu g}$ : $39{,}8\ \mathrm m$ et $318\ \mathrm m$.


> [!example]- 📝 Solution détaillée
> **(a) Virage stationnaire**
>
> $v=$ cte donc $a_T=0$ et $\|\vec a\|=a_N=\dfrac{v^2}R\le\mu g$, soit
> $$\boxed{v_{\max}=\sqrt{\mu gR}}.$$
> $R=50\ \mathrm m$ : $\mu=0{,}8$ : $\sqrt{392{,}4}=19{,}8\ \mathrm{m/s}=71\ \mathrm{km/h}$ ; $\mu=0{,}5$ : $15{,}7\ \mathrm{m/s}=56\ \mathrm{km/h}$ ; $\mu=0{,}1$ : $7{,}0\ \mathrm{m/s}=25\ \mathrm{km/h}$. La vitesse limite varie en $\sqrt{\mu}$ et en $\sqrt R$ : quadrupler le rayon double la vitesse limite.
>
> **(b) Freinage en ligne droite**
>
> $R=\infty$ : $a_N=0$ et $a_T\ge-\mu g$. Décélération maximale constante $b=\mu g$ : $v^2=v_0^2-2bd$ donne $v=0$ pour
> $$\boxed{d=\frac{v_0^2}{2\mu g}}.$$
> $v_0=25\ \mathrm{m/s}$ : $\mu=0{,}8$ : $d=\dfrac{625}{15{,}7}\approx39{,}8\ \mathrm m$ ; $\mu=0{,}1$ : $d=\dfrac{625}{1{,}96}\approx318\ \mathrm m$. Résultat à rapprocher des distances de sécurité sur verglas.


**q2.** **2/ Freiner dans un virage.** La voiture parcourt maintenant un arc de cercle de rayon $R=50\ \mathrm m$ ($\mu=0{,}8$) en freinant.


(a) Établir la décélération maximale $b_{\max}(v)$ possible à la vitesse $v$. Calculer $b_{\max}$ pour $v=15\ \mathrm{m/s}$ et pour $v=19\ \mathrm{m/s}$. Commenter.

(b) Le conducteur freine avec une décélération constante $b=4\ \mathrm{m\,s^{-2}}$ dès l'entrée dans le virage. Quelle est la vitesse d'entrée maximale $v_0$ pour que la voiture ne sorte pas du disque d'adhérence ? Que se passe-t-il ensuite ?

(c) Représenter l'évolution de $(a_N,a_T)$ dans le plan du disque d'adhérence.

> [!tip]- 💡 Coup de pouce
> $b^2+a_N^2\le(\mu g)^2$ avec $a_N=v^2/R$. Pour (d), c'est à $t=0$ que $a_N$ est maximale (la vitesse décroît), donc la condition la plus contraignante est à l'entrée.


> [!success]- ✅ Correction
> (c) $b_{\max}=\sqrt{(\mu g)^2-v^4/R^2}$ : $6{,}43\ \mathrm{m\,s^{-2}}$ à $15\ \mathrm{m/s}$ ; $3{,}08\ \mathrm{m\,s^{-2}}$ à $19\ \mathrm{m/s}$. (d) $v_0^4\le R^2\left[(\mu g)^2-b^2\right]$ : $v_0\le18{,}4\ \mathrm{m/s}=66\ \mathrm{km/h}$.


> [!example]- 📝 Solution détaillée
> **(c) Décélération maximale en virage**
>
> $a_T=-b$, $a_N=\dfrac{v^2}R$ : $b^2+\dfrac{v^4}{R^2}\le(\mu g)^2$ donc
> $$\boxed{b_{\max}(v)=\sqrt{(\mu g)^2-\frac{v^4}{R^2}}}.$$
> $\mu g=7{,}85\ \mathrm{m\,s^{-2}}$. $v=15$ : $a_N=4{,}5$, $b_{\max}=\sqrt{61{,}6-20{,}3}=6{,}43\ \mathrm{m\,s^{-2}}$ ($82\ \%$ de $\mu g$). $v=19$ : $a_N=7{,}22$, $b_{\max}=\sqrt{61{,}6-52{,}1}=3{,}08\ \mathrm{m\,s^{-2}}$ ($39\ \%$ de $\mu g$) : à $19\ \mathrm{m/s}$, quasiment toute l'adhérence est consommée pour tenir le virage ; il ne reste presque rien pour freiner. À $19{,}8\ \mathrm{m/s}$ ($=v_{\max}$), $b_{\max}=0$ : impossible de freiner sans sortir de la trajectoire.
>
> **(d) Freinage constant à l'entrée**
>
> Avec $v=v_0-bt$, $a_N=v^2/R$ décroît au cours du temps : la condition la plus sévère est à $t=0$ :
> $$b^2+\frac{v_0^4}{R^2}\le(\mu g)^2\ \Longrightarrow\ v_0\le\left(R^2\left[(\mu g)^2-b^2\right]\right)^{1/4}=\left(2\,500\times(61{,}6-16)\right)^{1/4}\approx\boxed{18{,}4\ \mathrm{m/s}\approx66\ \mathrm{km/h}}.$$
> (à comparer à $v_{\max}=71\ \mathrm{km/h}$ sans freinage). Si $v_0$ est inférieur à cette valeur, la voiture reste dans le disque ensuite, car $a_N$ diminue.
>
> **(e) Trajet dans le plan $(a_N,a_T)$**
>
> Au point d'entrée : $(a_N,a_T)=(v_0^2/R,-b)$ = $(6{,}75\ ;\ -4)$ avec $v_0=18{,}4$, point situé **sur le bord** du disque ($\|\vec a\|=\sqrt{6{,}75^2+4^2}\approx7{,}85\ \mathrm{m\,s^{-2}}=\mu g$) : c'est le cas limite. Ensuite $a_N$ décroît (la voiture ralentit) tandis que $a_T=-4$ reste constant : le point se déplace horizontalement vers la gauche à l'intérieur du disque. À la fin du freinage, la voiture est à l'arrêt : le point arrive sur l'axe $a_N=0$.


**q3.** **3/ Trajectoire de courbure variable.** Une voiture parcourt à la limite d'adhérence la parabole $y=kx^2$ avec $k=0{,}01\ \mathrm m^{-1}$ (rayon de courbure au sommet $R_0=50\ \mathrm m$), avec $\mu=0{,}8$.


(a) Exprimer la vitesse maximale $v_{\max}(x)$ qui peut être tenue en chaque point si la vitesse était constante, et la calculer au sommet ($x=0$) puis en $x=50\ \mathrm m$.

(b) En déduire où le conducteur doit freiner et où il peut accélérer.

> [!tip]- 💡 Coup de pouce
> $R(x)=\dfrac{(1+4k^2x^2)^{3/2}}{2k}$ ; $v_{\max}(x)=\sqrt{\mu gR(x)}$.


> [!success]- ✅ Correction
> $v_{\max}(x)=\sqrt{\mu g\,R(x)}$ ; $19{,}8\ \mathrm{m/s}\ (71\ \mathrm{km/h})$ en $x=0$ ($R=50$ m), $33{,}3\ \mathrm{m/s}\ (120\ \mathrm{km/h})$ en $x=50\ \mathrm m$ ($R=141\ \mathrm m$).


> [!example]- 📝 Solution détaillée
> **(f) Profil de vitesse limite**
>
> $$v_{\max}(x)=\sqrt{\mu g\,\frac{(1+4k^2x^2)^{3/2}}{2k}}.$$
> Sommet : $R=\dfrac1{2k}=50\ \mathrm m$, $v_{\max}=\sqrt{0{,}8\times9{,}81\times50}=19{,}8\ \mathrm{m/s}=71\ \mathrm{km/h}$. En $x=50\ \mathrm m$ : $4k^2x^2=4\times10^{-4}\times2\,500=1$, $R=\dfrac{2^{3/2}}{0{,}02}=141\ \mathrm m$, $v_{\max}=\sqrt{0{,}8\times9{,}81\times141}=33{,}3\ \mathrm{m/s}=120\ \mathrm{km/h}$.
>
> **(g) Stratégie**
>
> $v_{\max}$ est minimale au sommet (virage le plus serré) et croît quand on s'en éloigne. La voiture doit donc **freiner avant** le sommet (de manière à y arriver à moins de $71\ \mathrm{km/h}$) et peut **accélérer après** le sommet (puisque $R$ augmente). Le freinage doit être terminé **avant** la zone la plus courbée : dans la zone serrée, la voiture ne peut plus décélérer (disque presque saturé par $a_N$). Une stratégie « freiner tard puis tourner » est dangereuse.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex1-base-de-frenet-demonstrations-de-cours-et-applications|Exercice 1 — Base de Frenet : démonstrations de cours et applications]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex2-mouvement-curviligne-uniforme-cercle-parabole-applications|Exercice 2 — Mouvement curviligne uniforme : cercle, parabole, applications]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex3-circuit-de-monaco-courbure-et-acceleration-a-vitesse-constante|Exercice 3 — Circuit de Monaco : courbure et accélération à vitesse constante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex4-abscisse-curviligne-et-rayon-de-courbure-d-une-trajectoire-parabolique|Exercice 4 — Abscisse curviligne et rayon de courbure d'une trajectoire parabolique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex5-cycloide-point-d-une-roue-qui-roule-sans-glisser|Exercice 5 — Cycloïde : point d'une roue qui roule sans glisser]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex6-raccordement-routier-en-clothoide-courbure-variable-et-jerk|Exercice 6 — Raccordement routier en clothoïde (courbure variable et « jerk »)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex8-tir-parabolique-vu-dans-la-base-de-frenet|Exercice 8 — Tir parabolique vu dans la base de Frenet]]

