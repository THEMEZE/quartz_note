---
title: "Exercice 9 — Virage relevé et frottement solide"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 9. Virage relevé et frottement solide *(facultatif)*

Une voiture, assimilée à un point matériel $M$ de masse $m$, prend un virage circulaire de rayon $R=100$ m dont la chaussée est **relevée** d'un angle $\beta=10^\circ$ vers l'intérieur du virage (la route est inclinée comme un plan incliné, le bord intérieur étant plus bas). La voiture roule à vitesse constante $v$ sur un cercle horizontal de rayon $R$ et centre $C$ sur l'axe vertical du virage. Le contact route--pneus est modélisé par la loi de Coulomb du frottement solide : la réaction $\vec R=\vec N+\vec f$ avec $\vec N$ normale à la route et $\vec f$ tangentielle (dans le plan incliné, perpendiculaire à la vitesse donc dirigée dans la **pente**), $\|\vec f\|\le\mu\|\vec N\|$ où $\mu$ est le coefficient d'adhérence. On prendra $g=9{,}81~\mathrm{m\,s^{-2}}$. On travaille dans le référentiel terrestre galiléen, avec un repère $(\vec e_r,\vec e_\varphi,\vec u_z)$ cylindrique d'axe vertical passant par $C$.

**q1.** - [(a)] Faire le schéma en coupe du virage (plan vertical contenant l'axe) et le bilan des forces s'exerçant sur $M$ dans le cas **sans frottement**.
- [(b)] Écrire la 2\textsuperscript{e} loi de Newton et la projeter horizontalement (sur $-\vec e_r$, vers le centre) et verticalement. En déduire l'expression de la vitesse $v_0$ pour laquelle la voiture reste sur la trajectoire sans aucun frottement. Application numérique.

> [!tip]- 💡 Coup de pouce
> Sans frottement, il ne reste que le poids et la réaction normale, inclinée de $\beta$ par rapport à la verticale. L'accélération est horizontale, dirigée vers l'axe.


**q2.** On tient maintenant compte de l'adhérence de coefficient $\mu$.


- [(c)] Pour $v>v_0$, dans quel sens la voiture a-t-elle tendance à glisser ? Quel est le sens de la force de frottement $\vec f$ ? Écrire les projections de la 2\textsuperscript{e} loi.
- [(d)] Exprimer la condition de non-glissement $\|\vec f\|\le\mu N$ et en déduire la vitesse maximale $v_{\max}$ en fonction de $g$, $R$, $\beta$, $\mu$.
- [(e)] Application numérique pour $\mu=0{,}1$ (route mouillée) et $\mu=0{,}7$ (route sèche).

> [!tip]- 💡 Coup de pouce
> À vitesse élevée, la voiture « part vers l'extérieur » : elle tend à remonter la pente. Le frottement s'y oppose, donc il est dirigé vers le bas de la pente. Au seuil, $f=\mu N$. Divisez les deux projections pour éliminer $N$.


**q3.** - [(f)] Pour $v<v_0$, dans quel sens la voiture a-t-elle tendance à glisser ? En déduire la vitesse minimale $v_{\min}$ en dessous de laquelle elle glisse vers l'intérieur du virage.
- [(g)] Quelle condition sur $\mu$ et $\beta$ assure qu'il n'existe aucune vitesse minimale ? Discuter pour $\mu=0{,}1$ et $\mu=0{,}7$.
- [(h)] Écrire $v_{\min}$ et $v_{\max}$ à l'aide de l'angle de frottement $\varphi$ défini par $\tan\varphi=\mu$. Commenter.

> [!tip]- 💡 Coup de pouce
> À basse vitesse, la voiture « tombe vers l'intérieur » : elle tend à descendre la pente. Le frottement est alors dirigé vers le haut de la pente : changez le signe de $\mu$ dans les formules précédentes. Pour (h), utilisez la formule d'addition de la tangente.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex1-exercices-elementaires|Exercice 1 — Exercices élémentaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex3-machine-d-atwood|Exercice 3 — Machine d'Atwood]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex7-chute-avec-frottement-fluide-vitesse-limite|Exercice 7 — Chute avec frottement fluide : vitesse limite]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex4-systeme-pendule-bloc|Exercice 4 — (*) Système pendule-bloc]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex6-chaine-qui-glisse-d-une-table|Exercice 6 — (*) Chaîne qui glisse d'une table]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]]

