---
title: "Exercice 4 — Le dilemme du feu orange"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · <a href="/pdfs/td1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td1_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

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


> [!success]- ✅ Correction
> $d_f=v_0t_r+\dfrac{v_0^2}{2a}\approx13{,}9+32{,}2\approx46{,}0$ m ; $t_s=t_r+\dfrac{v_0}{a}\approx5{,}63$ s.


> [!example]- 📝 Solution détaillée
> **(a) Lois horaires par phase**
>
> Conversion : $v_0=50/3{,}6\approx13{,}89~\mathrm{m\,s^{-1}}$.
>
> **Phase 1** ($0\le t\le t_r$), mouvement uniforme :
> $$v(t)=v_0,\qquad x(t)=v_0\,t .$$
> À la fin de la phase 1 : $x_1=v_0t_r\approx13{,}9$ m et $v_1=v_0$.
>
> **Phase 2** ($t\ge t_r$), accélération constante $-a$ :
> $$v(t)=v_0-a\,(t-t_r),\qquad x(t)=v_0t_r+v_0\,(t-t_r)-\tfrac12\,a\,(t-t_r)^2=v_0\,t-\tfrac12\,a\,(t-t_r)^2 .$$
>
> **(b) Instant et distance d'arrêt**
>
> La voiture s'arrête quand $v(t_s)=0$ :
> $$v_0-a\,(t_s-t_r)=0\;\Longrightarrow\;\boxed{t_s=t_r+\frac{v_0}{a}}\approx1+4{,}63=5{,}63~\text{s}.$$
> En reportant dans $x(t)$ :
> $$d_f=x(t_s)=v_0t_r+\frac{v_0^2}{2a}=\boxed{v_0t_r+\frac{v_0^2}{2a}}.$$
> Application numérique : $d_f\approx13{,}9+\dfrac{13{,}89^2}{2\times3}\approx13{,}9+32{,}2\approx\boxed{46{,}0~\text{m}}$. La distance de réaction (13,9 m) représente près d'un tiers du total.
>
> **(c) Graphe de $v(t)$ et aire**
>
> Le graphe de $v(t)$ est un palier horizontal $v=v_0$ de $t=0$ à $t_r$, puis une droite de pente $-a$ qui rejoint l'axe des temps en $t_s=t_r+v_0/a$.
>
> L'aire sous la courbe est la somme d'un **rectangle** de base $t_r$ et de hauteur $v_0$ (aire $v_0t_r$) et d'un **triangle** de base $v_0/a$ et de hauteur $v_0$ (aire $\tfrac12v_0\cdot v_0/a=v_0^2/(2a)$). On retrouve $d_f=v_0t_r+v_0^2/(2a)$ sans intégrer.


**q2.** - [(d)] Exprimer, en fonction de $d_f$, $v_0$ et $\tau$, la condition sur $D$ pour que le conducteur puisse s'arrêter, puis la condition pour qu'il puisse passer.
- [(e)] En déduire l'existence d'une « zone de dilemme », donner sa largeur $\Delta$ en fonction de $v_0$, $t_r$, $a$ et $\tau$, et la calculer numériquement.
- [(f)] Pour quelles vitesses $v_0$ la zone de dilemme existe-t-elle ? Donner le seuil littéral et numérique (en km/h).

> [!tip]- 💡 Coup de pouce
> Pour passer, il faut atteindre la ligne $x=D$ au plus tard à $t=\tau$ : à vitesse constante, $x(\tau)=v_0\tau$ doit être au moins égal à $D$. Une zone de dilemme est un intervalle de $D$ qui ne vérifie aucune des deux conditions.


> [!success]- ✅ Correction
> Arrêt possible : $D\ge d_f\approx46{,}0$ m. Passage possible : $D\le v_0\tau\approx41{,}7$ m. Zone de dilemme : $41{,}7~\text{m}<D<46{,}0~\text{m}$, largeur $\Delta=v_0\Big(\dfrac{v_0}{2a}-(\tau-t_r)\Big)\approx4{,}4$ m, qui existe pour $v_0>2a(\tau-t_r)=12~\mathrm{m/s}=43{,}2$ km/h.


> [!example]- 📝 Solution détaillée
> **(d) Les deux conditions**
>
> **Arrêt possible** : la voiture doit s'immobiliser avant la ligne, donc la distance d'arrêt doit être inférieure ou égale à $D$ :
> $$D\ge d_f .$$
> **Passage possible** : à vitesse constante, la position à l'instant $\tau$ est $x(\tau)=v_0\tau$. La ligne est franchie avant le rouge si
> $$D\le v_0\,\tau .$$
>
> **(e) Zone de dilemme**
>
> Un $D$ est « dilemme » s'il ne vérifie aucune des deux conditions : $v_0\tau<D<d_f$. Cet intervalle est non vide si $d_f>v_0\tau$, et sa largeur est
> $$\Delta=d_f-v_0\tau=v_0t_r+\frac{v_0^2}{2a}-v_0\tau=\boxed{v_0\left(\frac{v_0}{2a}-(\tau-t_r)\right)}.$$
> Application numérique : $v_0\tau\approx41{,}7$ m et $d_f\approx46{,}0$ m, donc
> $$\boxed{41{,}7~\text{m}<D<46{,}0~\text{m}},\qquad\Delta\approx4{,}4~\text{m}.$$
> Entre ces deux valeurs, freiner conduit à franchir la ligne (rouge) et passer à la franchir trop tard : les deux manœuvres sont fautives, ou nécessitent un freinage plus fort que $a=3~\mathrm{m\,s^{-2}}$.
>
> **(f) Vitesse seuil**
>
> $\Delta>0\iff\dfrac{v_0}{2a}>\tau-t_r\iff v_0>v^\star=2a\,(\tau-t_r)$. Numériquement :
> $$v^\star=2\times3\times(3-1)=12~\mathrm{m\,s^{-1}}=\boxed{43{,}2~\text{km/h}}.$$
> À 50 km/h on est au-dessus du seuil : un dilemme existe. À 30 km/h, il n'y a plus de zone de dilemme : il existe toujours une manœuvre valable.


**q3.** - [(g)] Quelle durée minimale $\tau_{\min}$ l'orange doit-il avoir pour qu'il n'existe aucune zone de dilemme ? Calculer $\tau_{\min}$ pour des vitesses de $30$, $50$, $70$ et $90$ km/h.
- [(h)] Commenter : pourquoi la durée de l'orange est-elle plus longue sur les routes rapides ? Que dire de la valeur $\tau=3$ s à 50 km/h ?

> [!tip]- 💡 Coup de pouce
> Il n'y a pas de dilemme si $d_f\le v_0\tau$. Isolez $\tau$.


> [!success]- ✅ Correction
> $\tau_{\min}=t_r+\dfrac{v_0}{2a}$ : $2{,}39$ s (30 km/h), $3{,}31$ s (50 km/h), $4{,}24$ s (70 km/h), $5{,}17$ s (90 km/h).


> [!example]- 📝 Solution détaillée
> **(g) Durée minimale de l'orange**
>
> Pas de dilemme $\iff d_f\le v_0\tau$, soit $v_0t_r+\dfrac{v_0^2}{2a}\le v_0\tau$. En divisant par $v_0>0$ :
> $$\boxed{\tau\ge\tau_{\min}=t_r+\frac{v_0}{2a}}.$$
> Application numérique ($t_r=1$ s, $a=3~\mathrm{m\,s^{-2}}$) :
> $$\begin{array}{c|cccc}
> v_0~(\text{km/h})&30&50&70&90\\\hline
> v_0~(\mathrm{m/s})&8{,}33&13{,}89&19{,}44&25{,}0\\
> \tau_{\min}~(\text{s})&2{,}39&3{,}31&4{,}24&5{,}17
> \end{array}$$
>
> **(h) Commentaires**
>
> $\tau_{\min}$ est une fonction **affine** de $v_0$ : plus on roule vite, plus il faut laisser du temps. C'est pourquoi les orange sont plus longs sur les axes rapides.
>
> À 50 km/h, $\tau_{\min}\approx3{,}3$ s est légèrement supérieur à $\tau=3$ s : le dilemme de 4,4 m trouvé en (e) est cohérent. Mais ce résultat est **sensible aux paramètres** : avec $a=4~\mathrm{m\,s^{-2}}$, on trouverait $\tau_{\min}=1+13{,}9/8\approx2{,}74$ s $<3$ s, plus de dilemme. Le modèle n'a donc de sens que si l'on précise le conducteur et l'état de la route.


**q4.** (*) Entraînement : un conducteur qui décide de passer **accélère** avec $a_{\rm acc}=2{,}0~\mathrm{m\,s^{-2}}$ pendant tout l'orange. Quelle est la nouvelle condition de passage ? La zone de dilemme subsiste-t-elle ? À quelle vitesse franchit-il alors la ligne au plus tard, et qu'en penser ?

> [!tip]- 💡 Coup de pouce
> Entre $0$ et $\tau$, la voiture suit un MRUA de vitesse initiale $v_0$ : $x(\tau)=v_0\tau+\tfrac12a_{\rm acc}\tau^2$.


> [!success]- ✅ Correction
> Passage possible si $D\le v_0\tau+\tfrac12a_{\rm acc}\tau^2\approx50{,}7$ m $>d_f\approx46{,}0$ m : plus de zone de dilemme, mais la vitesse atteint $v_0+a_{\rm acc}\tau\approx19{,}9~\mathrm{m/s}\approx72$ km/h : infraction de vitesse.


> [!example]- 📝 Solution détaillée
> **Passage en accélérant**
>
> $$x(\tau)=v_0\tau+\tfrac12a_{\rm acc}\tau^2\approx41{,}7+\tfrac12\times2\times9=\boxed{50{,}7~\text{m}}.$$
> La condition de passage devient $D\le50{,}7$ m, tandis que l'arrêt reste possible pour $D\ge46{,}0$ m. Les deux intervalles **se recouvrent** entre $46{,}0$ et $50{,}7$ m : il n'y a plus de zone interdite, le conducteur a même le choix.
>
> Mais la vitesse au moment de franchir la ligne (au plus tard à $\tau$) vaut $v_0+a_{\rm acc}\tau\approx13{,}9+6=19{,}9~\mathrm{m/s}\approx72$ km/h, bien au-dessus de la limite de 50 km/h : on a « résolu » le dilemme au prix d'une infraction de vitesse, ce qui n'est pas une solution acceptable. Le dilemme se résout par la signalisation (orange plus long) et non par l'accélération.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex3-course-automobile-rattrapage-de-deux-mobiles|Exercice 3 — Course automobile : rattrapage de deux mobiles]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex7-balle-rebondissante-et-paradoxe-de-zenon|Exercice 7 — Balle rebondissante et paradoxe de Zénon]]

