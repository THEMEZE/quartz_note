---
title: "Exercice 7 — Balle rebondissante et paradoxe de Zénon"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · <a href="/pdfs/td1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 7. Balle rebondissante et paradoxe de Zénon *(facultatif)*

Une balle est lâchée sans vitesse initiale d'une hauteur $h_0=1{,}00$ m au-dessus d'un sol horizontal. On néglige les frottements de l'air et on assimile la balle à un point matériel dans le champ de pesanteur $g=9{,}81~\mathrm{m\,s^{-2}}$.
Chaque choc avec le sol est supposé **instantané** : la composante verticale de la vitesse est inversée et **multipliée par** un coefficient de restitution $e$ (avec $0<e<1$) ; on prendra $e=0{,}80$. On repère la balle par son altitude $z$ (axe $Oz$ vertical ascendant, origine au sol), l'origine des temps étant l'instant du lâcher.

**q1.** - [(a)] Calculer la vitesse $v_0$ de la balle juste avant le premier choc et la durée $t_0$ de la première chute.
- [(b)] Après le $n$-ième choc ($n\ge1$), exprimer la vitesse initiale $v_n$ de la balle, la hauteur maximale $h_n$ atteinte et la durée $T_n$ qui sépare le $n$-ième du $(n+1)$-ième choc, en fonction de $e$, $v_0$, $h_0$ et $t_0$.
- [(c)] Représenter schématiquement $z(t)$ sur les premiers rebonds.

> [!tip]- 💡 Coup de pouce
> Après chaque choc, la balle repart verticalement vers le haut avec la vitesse $e$ fois celle de l'arrivée : c'est un lancer vertical. Utilisez les résultats d'un lancer vertical ($h=v^2/2g$, durée aller-retour $2v/g$).


**q2.** - [(d)] Calculer la durée totale $t_\infty$ entre le lâcher et l'immobilisation (limite), en fonction de $t_0$ et $e$. Application numérique.
- [(e)] Calculer la distance totale $D$ parcourue par la balle. Application numérique.
- [(f)] À partir de quel rebond la hauteur maximale devient-elle inférieure à $1$ mm ?
- [(g)] La balle effectue-t-elle un nombre fini ou infini de rebonds ? Commenter.

> [!tip]- 💡 Coup de pouce
> La durée totale est $t_0+\sum_{n\ge1}T_n$ : une série géométrique de raison $e$. La distance est la somme de la hauteur initiale $h_0$ et des montées-descentes ($2h_n$). Pour (f), résolvez $e^{2n}h_0<10^{-3}$ avec un logarithme.


**q3.** - [(h)] On enregistre le son des chocs d'une balle lâchée sans vitesse initiale d'une hauteur inconnue. Les quatre premiers chocs se produisent aux instants $0{,}45$ s ; $1{,}17$ s ; $1{,}75$ s ; $2{,}21$ s. En déduire le coefficient de restitution $e$ et la hauteur de lâcher $h_0$.
- [(i)] La balle est maintenant **lancée horizontalement** depuis la hauteur $h_0=1{,}00$ m avec la vitesse $v_x=2{,}0~\mathrm{m\,s^{-1}}$, sans frottement à l'impact (la composante horizontale de la vitesse est conservée). Quelle distance horizontale totale $L$ parcourt-elle ? Quelle est la longueur de la première arche ?

> [!tip]- 💡 Coup de pouce
> Pour (h), les intervalles entre chocs successifs sont $T_1,T_2,T_3$ : calculez leurs rapports. Le premier instant de choc est $t_0=\sqrt{2h_0/g}$. Pour (i), le temps est commun aux deux mouvements : la distance horizontale se déduit de la durée totale.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex3-course-automobile-rattrapage-de-deux-mobiles|Exercice 3 — Course automobile : rattrapage de deux mobiles]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex4-le-dilemme-du-feu-orange|Exercice 4 — Le dilemme du feu orange]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex6-parabole-de-s-rete-et-tir-sur-une-pente|Exercice 6 — Parabole de sûreté et tir sur une pente]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]]

