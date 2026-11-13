---
title: "Exercice 6 — (*) Balle rebondissante et coefficient de restitution"
tags:
  - td
  - chap-4-quantite-de-mouvement-systemes-de-points-collisions
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/index|⬅ Retour]]

### Exercice 6. (*) Balle rebondissante et coefficient de restitution *(facultatif)*

Une balle est lâchée sans vitesse initiale d'une hauteur $h_0=1{,}00$ m au-dessus d'un sol dur et horizontal. À chaque rebond, la composante normale de la vitesse est multipliée par $-e$ ($0<e<1$ : coefficient de restitution), la composante tangentielle étant conservée (pas de frottement). On prendra $e=0{,}80$ et $g=9{,}81~\mathrm{m\,s^{-2}}$ ; les frottements de l'air sont négligés et les chocs sont supposés instantanés.

**q1.** - [(a)] Calculer la durée $t_0$ de la première chute et la vitesse $v_1$ juste avant le premier rebond.
- [(b)] Établir la hauteur $h_n$ atteinte après le $n$-ième rebond. Application numérique pour $n=1$, $2$, $5$. Combien de rebonds jusqu'à une hauteur $<1$ cm ?
- [(c)] Quelle fraction de l'énergie mécanique est dissipée à chaque rebond ?

> [!tip]- 💡 Coup de pouce
> Après le rebond $n$, la vitesse vaut $v_n'=ev_n$ ; la hauteur atteinte est $h_n=v_n'^2/(2g)$ et la vitesse de retour au sol est $\sqrt{2gh_n}$.


**q2.** - [(d)] Montrer que l'intervalle de temps entre le $n$-ième et le $(n+1)$-ième rebond vaut $\tau_n=2t_0e^n$. En déduire la durée totale $t_{\rm tot}$ jusqu'à l'arrêt ; AN. La balle s'arrête-t-elle en un temps fini ?
- [(e)] Calculer la distance verticale totale parcourue. AN.
- [(f)] **Rebond oblique** : la balle arrive sur le sol avec un angle $\theta=30^\circ$ par rapport à la normale (vitesse $v$). Quelle est la direction après le rebond ? Quel est le rapport $v'/v$ ? Application numérique.

> [!tip]- 💡 Coup de pouce
> (d) Durée d'un aller-retour : $2v_n'/g$ avec $v_n'=ev_n=e^nv_1$. (e) $h_0+2\sum_{n\ge1}h_n$. (f) Composante tangentielle conservée, composante normale multipliée par $-e$.


**q3.** - [(g)] **Rebond sur une raquette.** Une balle de tennis de vitesse $v=20~\mathrm{m/s}$ (vers la droite) est frappée par une raquette de masse très grande devant celle de la balle, animée d'une vitesse $V=30~\mathrm{m/s}$ (vers la gauche). Le coefficient de restitution est $e=0{,}75$. Calculer la vitesse de la balle après le choc, par un raisonnement dans le référentiel de la raquette. Quelle fraction de l'énergie fournie par la raquette est transmise ? Pourquoi une balle ne repart-elle pas à $2V$ ?

> [!tip]- 💡 Coup de pouce
> Se placer dans le référentiel de la raquette (immobile) : la balle arrive à $v+V$ et repart à $e(v+V)$. Revenir au référentiel du laboratoire.

