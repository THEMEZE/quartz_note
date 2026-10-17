---
title: "Exercice 7 — Cercle d'adhérence : freiner et tourner en même temps"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/index|⬅ Retour]] · <a href="/pdfs/td3_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td3_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

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

**q2.** **2/ Freiner dans un virage.** La voiture parcourt maintenant un arc de cercle de rayon $R=50\ \mathrm m$ ($\mu=0{,}8$) en freinant.


(a) Établir la décélération maximale $b_{\max}(v)$ possible à la vitesse $v$. Calculer $b_{\max}$ pour $v=15\ \mathrm{m/s}$ et pour $v=19\ \mathrm{m/s}$. Commenter.

(b) Le conducteur freine avec une décélération constante $b=4\ \mathrm{m\,s^{-2}}$ dès l'entrée dans le virage. Quelle est la vitesse d'entrée maximale $v_0$ pour que la voiture ne sorte pas du disque d'adhérence ? Que se passe-t-il ensuite ?

(c) Représenter l'évolution de $(a_N,a_T)$ dans le plan du disque d'adhérence.

**q3.** **3/ Trajectoire de courbure variable.** Une voiture parcourt à la limite d'adhérence la parabole $y=kx^2$ avec $k=0{,}01\ \mathrm m^{-1}$ (rayon de courbure au sommet $R_0=50\ \mathrm m$), avec $\mu=0{,}8$.


(a) Exprimer la vitesse maximale $v_{\max}(x)$ qui peut être tenue en chaque point si la vitesse était constante, et la calculer au sommet ($x=0$) puis en $x=50\ \mathrm m$.

(b) En déduire où le conducteur doit freiner et où il peut accélérer.

> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex1-base-de-frenet-demonstrations-de-cours-et-applications|Exercice 1 — Base de Frenet : démonstrations de cours et applications]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex2-mouvement-curviligne-uniforme-cercle-parabole-applications|Exercice 2 — Mouvement curviligne uniforme : cercle, parabole, applications]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex3-circuit-de-monaco-courbure-et-acceleration-a-vitesse-constante|Exercice 3 — Circuit de Monaco : courbure et accélération à vitesse constante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex4-abscisse-curviligne-et-rayon-de-courbure-d-une-trajectoire-parabolique|Exercice 4 — Abscisse curviligne et rayon de courbure d'une trajectoire parabolique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex5-cycloide-point-d-une-roue-qui-roule-sans-glisser|Exercice 5 — Cycloïde : point d'une roue qui roule sans glisser]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex6-raccordement-routier-en-clothoide-courbure-variable-et-jerk|Exercice 6 — Raccordement routier en clothoïde (courbure variable et « jerk »)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex8-tir-parabolique-vu-dans-la-base-de-frenet|Exercice 8 — Tir parabolique vu dans la base de Frenet]]

