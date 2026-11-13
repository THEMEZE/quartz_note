---
title: "Exercice 7 — Chute avec frottement fluide : vitesse limite"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 7. Chute avec frottement fluide : vitesse limite *(facultatif)*

Une bille de masse $m=50$ g est lâchée sans vitesse initiale dans un fluide visqueux (huile). En plus de son poids, elle subit une force de frottement fluide $\vec f=-\lambda\,\vec v$ avec $\lambda=0{,}50~\mathrm{kg\,s^{-1}}$. On néglige la poussée d'Archimède. On prendra $g=9{,}81~\mathrm{m\,s^{-2}}$. L'axe $Oz$ est vertical **descendant**, l'origine $O$ est le point de lâcher, et $t=0$ est l'instant du lâcher.

**q1.** - [(a)] Établir l'équation différentielle vérifiée par la vitesse $v(t)=\dot z$ de la bille.
- [(b)] Sans résoudre l'équation, déterminer la vitesse limite $v_\ell$ et le temps caractéristique $\tau$. Applications numériques.
- [(c)] Résoudre l'équation avec la condition initiale. Tracer $v(t)$.

> [!tip]- 💡 Coup de pouce
> Avec $Oz$ descendant : poids $+mg$, frottement $-\lambda v$. La vitesse limite correspond à $\mathrm dv/\mathrm dt=0$. Solution de la forme $v=v_\ell+C\mathrm e^{-t/\tau}$.


**q2.** - [(d)] Déterminer $z(t)$. Quelle distance la bille a-t-elle parcourue au bout de $0{,}50$ s ?
- [(e)] À quel instant la vitesse atteint-elle $99\%$ de $v_\ell$ ? Quelle distance a été parcourue alors ?
- [(f)] Montrer que pour $t\ll\tau$ on retrouve la chute libre.

> [!tip]- 💡 Coup de pouce
> Intégrez $v(t)$ avec $z(0)=0$. Pour (e), résolvez $\mathrm e^{-t/\tau}=0{,}01$. Pour (f), développez l'exponentielle à l'ordre $2$.


**q3.** - [(g)] La bille est maintenant lancée **vers le haut** avec la vitesse $v_0=2{,}0~\mathrm{m/s}$ dans le même fluide (axe $Oz$ désormais ascendant). Établir la vitesse $v_z(t)$, l'instant $t_s$ du sommet et la hauteur maximale $h$. Application numérique.
- [(h)] Vérifier que le résultat redonne $h=v_0^2/(2g)$ quand le frottement tend vers $0$ ($\lambda\to0$). Comparer à la valeur numérique sans frottement.

> [!tip]- 💡 Coup de pouce
> Avec $Oz$ ascendant : $m\dot v_z=-mg-\lambda v_z$. Posez $v_\ell=mg/\lambda$ : la solution est $v_z=-v_\ell+(v_0+v_\ell)\mathrm e^{-t/\tau}$. Le sommet est atteint quand $v_z=0$. Pour (h), développez $\ln(1+x)$ à l'ordre $2$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex1-exercices-elementaires|Exercice 1 — Exercices élémentaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex3-machine-d-atwood|Exercice 3 — Machine d'Atwood]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex4-systeme-pendule-bloc|Exercice 4 — (*) Système pendule-bloc]]

