---
title: "Exercice 4 — Le dilemme du feu orange"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · <a href="/pdfs/td1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 4. Le dilemme du feu orange *(facultatif)*

Une voiture roule en ligne droite à la vitesse constante $v_0=50~\mathrm{km/h}$ (limitation en ville) lorsque le feu
situé devant elle passe à l'orange. On choisit l'axe $Ox$ le long de la route, orienté dans le sens de la marche, l'origine $O$ à
la position de la voiture à cet instant, qui est aussi l'origine des temps. La ligne d'arrêt du feu est à l'abscisse $x=D$. Le feu reste orange pendant $\tau=3{,}0~\mathrm{s}$,
puis passe au rouge.

Le conducteur a deux options :


- **freiner** : pendant un temps de réaction $t_r=1{,}0~\mathrm{s}$ la vitesse reste égale à $v_0$, puis la voiture décélère de manière uniforme, avec une décélération $a=3{,}0~\mathrm{m\,s^{-2}}$ (freinage confortable), jusqu'à l'arrêt. Il doit s'immobiliser **avant** la ligne d'arrêt ($x\le D$) ;
- **passer** : maintenir sa vitesse $v_0$ et franchir la ligne d'arrêt **avant** le passage au rouge, c'est-à-dire à un instant $t\le\tau$.


On modélise la voiture par un point matériel.

**q1.** - [(a)] Écrire, pour chacune des deux phases du freinage (réaction puis décélération), la vitesse $v(t)$ et l'abscisse $x(t)$ de la voiture.
- [(b)] Déterminer l'instant $t_s$ de l'arrêt et la distance totale $d_f$ parcourue depuis l'apparition de l'orange. Faire l'application numérique et distinguer distance de réaction et distance de freinage.
- [(c)] Tracer $v(t)$ et retrouver $d_f$ comme l'aire sous la courbe.

> [!tip]- 💡 Coup de pouce
> Il y a deux lois horaires, à raccorder en $t=t_r$. La seconde est une loi à accélération constante $-a$ dont les conditions initiales sont la position et la vitesse atteintes à la fin de la phase de réaction. Convertissez $v_0$ en m/s avant tout calcul.


**q2.** - [(d)] Exprimer, en fonction de $d_f$, $v_0$ et $\tau$, la condition sur $D$ pour que le conducteur puisse s'arrêter, puis la condition pour qu'il puisse passer.
- [(e)] En déduire l'existence d'une « zone de dilemme », donner sa largeur $\Delta$ en fonction de $v_0$, $t_r$, $a$ et $\tau$, et la calculer numériquement.
- [(f)] Pour quelles vitesses $v_0$ la zone de dilemme existe-t-elle ? Donner le seuil littéral et numérique (en km/h).

> [!tip]- 💡 Coup de pouce
> Pour passer, il faut atteindre la ligne $x=D$ au plus tard à $t=\tau$ : à vitesse constante, $x(\tau)=v_0\tau$ doit être au moins égal à $D$. Une zone de dilemme est un intervalle de $D$ qui ne vérifie aucune des deux conditions.


**q3.** - [(g)] Quelle durée minimale $\tau_{\min}$ l'orange doit-il avoir pour qu'il n'existe aucune zone de dilemme ? Calculer $\tau_{\min}$ pour des vitesses de $30$, $50$, $70$ et $90$ km/h.
- [(h)] Commenter : pourquoi la durée de l'orange est-elle plus longue sur les routes rapides ? Que dire de la valeur $\tau=3$ s à 50 km/h ?

> [!tip]- 💡 Coup de pouce
> Il n'y a pas de dilemme si $d_f\le v_0\tau$. Isolez $\tau$.


**q4.** (*) Entraînement : un conducteur qui décide de passer **accélère** avec $a_{\rm acc}=2{,}0~\mathrm{m\,s^{-2}}$ pendant tout l'orange. Quelle est la nouvelle condition de passage ? La zone de dilemme subsiste-t-elle ? À quelle vitesse franchit-il alors la ligne au plus tard, et qu'en penser ?

> [!tip]- 💡 Coup de pouce
> Entre $0$ et $\tau$, la voiture suit un MRUA de vitesse initiale $v_0$ : $x(\tau)=v_0\tau+\tfrac12a_{\rm acc}\tau^2$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex3-course-automobile-rattrapage-de-deux-mobiles|Exercice 3 — Course automobile : rattrapage de deux mobiles]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex7-balle-rebondissante-et-paradoxe-de-zenon|Exercice 7 — Balle rebondissante et paradoxe de Zénon]]

