---
title: "Exercice 5 — Voiture sur une bosse"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 5. Voiture sur une bosse

Une automobile s'engage sur une portion de route en forme de bosse. Le véhicule est assimilé à un point matériel $M$ de masse $m$, et la norme $v>0$ de sa vitesse est constante tout au long du mouvement. La bosse est modélisée par deux portions rectilignes raccordées par un arc de cercle de centre $O$, de rayon $R$ et d'ouverture angulaire $2\alpha$ (le centre $O$ est sous la route). On repère $M$ sur l'arc par l'angle $\theta$ entre la verticale ascendante passant par $O$ et le rayon $\overrightarrow{OM}$ ; $\theta$ est compté positivement dans le sens trigonométrique, de sorte que la voiture, qui avance vers la droite, parcourt l'arc de $\theta=+\alpha$ à $\theta=-\alpha$. On prendra $g=9{,}81~\mathrm{m\,s^{-2}}$.

On cherche à quelle condition sur $v$ l'automobile garde le contact avec le sol tout au long de son chemin.

**q1.** **1/ Cinématique**


- [(a)] Représenter sur la figure les vecteurs $(\vec e_r,\vec e_\theta)$ de la base polaire associée au point $M$.
- [(b)] Rappeler l'expression des dérivées de ces deux vecteurs par rapport à $\theta(t)$. (Si vous avez oublié, refaire le calcul.)
- [(c)] Donner, dans le cas général, l'expression du vecteur vitesse $\vec v$ en coordonnées polaires. Que devient-elle pour la voiture sur la partie courbe ?

> [!tip]- 💡 Coup de pouce
> $\vec e_r$ pointe de $O$ vers $M$ et $\vec e_\theta$ s'en déduit par une rotation de $+90^\circ$. Sur l'arc, $r=R$ est constant.


**q2.** - [(d)] Déterminer l'expression reliant $v$, $R$ et $\mathrm d\theta/\mathrm dt$ en analysant soigneusement le signe de $\mathrm d\theta/\mathrm dt$.
- [(e)] Donner, dans le cas général, l'expression du vecteur accélération $\vec a$ en polaires. Que devient-elle pour la voiture sur la partie courbe ?

> [!tip]- 💡 Coup de pouce
> La voiture va vers la droite au sommet ; que fait $\theta$ ? $v$ est la norme de $\vec v$, donc positive. Dérivez $\vec v$ en utilisant les dérivées de $\vec e_r$ et $\vec e_\theta$.


**q3.** **2/ Dynamique**


- [(a)] Faire le bilan des forces sur l'automobile : la route exerce une réaction $\vec R=\vec N+\vec T$, avec $\vec N$ la composante normale et $\vec T$ la composante tangentielle (frottements solides). Les représenter sur le schéma.
- [(b)] Comment exprimer au moyen d'une inégalité sur $\vec N$ que la voiture est ou non en contact avec la route ?
- [(c)] En appliquant la relation fondamentale de la dynamique projetée sur $\vec e_r$, donner l'expression reliant $\|\vec N\|$, $m$, $v$, $R$, $g$ et $\theta$.

> [!tip]- 💡 Coup de pouce
> Le poids est vertical vers le bas ; $\vec N$ est perpendiculaire à la route, donc selon $\vec e_r$ ; $\vec T$ est tangent, donc selon $\vec e_\theta$. Le contact exige que la route « pousse ».


**q4.** - [(d)] Quelle inégalité relie $v$, $R$, $g$ et $\theta$ pour que la voiture reste sur la route quel que soit l'angle $\theta$ ?
- [(e)] En déduire la relation liant $v$, $R$, $g$ et $\alpha$ pour que la voiture reste sur la route tout le long du trajet.
- [(f)] Application numérique : calculer $v_{\max}$ pour $\alpha=10^\circ$ et $R=6{,}0$ m.

> [!tip]- 💡 Coup de pouce
> $N\ge0$ s'écrit $v^2\le gR\cos\theta$. Cette inégalité doit être vraie pour tous les $\theta\in[-\alpha,\alpha]$ : cherchez la valeur de $\theta$ qui rend le second membre minimal.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex1-exercices-elementaires|Exercice 1 — Exercices élémentaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex3-machine-d-atwood|Exercice 3 — Machine d'Atwood]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex7-chute-avec-frottement-fluide-vitesse-limite|Exercice 7 — Chute avec frottement fluide : vitesse limite]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex4-systeme-pendule-bloc|Exercice 4 — (*) Système pendule-bloc]]

