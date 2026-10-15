---
title: "Exercice 2 — Onde stationnaire, tube de Kundt ouvert"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/index|⬅ Retour]] · [📄 Énoncé (td2_PhV212_enonce)](/pdfs/td2_PhV212_enonce.pdf) · [📄 Énoncé (td2_enonce)](/pdfs/td2_enonce.pdf)

### Exercice 2. Onde stationnaire, tube de Kundt ouvert

Un haut-parleur en $x=0$ émet une onde acoustique dans un tube d'air de
longueur $L$, ouvert aux deux extrémités ($x=0$ et $x=L$). Déplacement
incident $\Psi_I(x,t)=A_I e^{i(\omega t - kx)}$, avec $k=\omega/c$. À la
réflexion en $x=L$ (extrémité ouverte), le déplacement réfléchi s'écrit
$\Psi_R(x,t)=A_I e^{i(\omega t - k(2L-x))}$.

**q1.** Justifier cette expression du déplacement réfléchi par un schéma.

> [!tip]- 💡 Coup de pouce
> Une extrémité ouverte est un ventre de déplacement (pas de nœud) : le déplacement n'est pas inversé au retour, contrairement à une réflexion sur paroi rigide.


**q2.** Montrer que le déplacement résultant s'écrit
$\Psi(x,t)=2A_I\cos\big(k(L-x)\big)e^{i(\omega t-kL)}$. Justifier le nom d'onde stationnaire.

> [!tip]- 💡 Coup de pouce
> Sommez $\Psi_I+\Psi_R$ et factorisez ; une onde stationnaire a un profil spatial et une évolution temporelle qui se séparent (le terme $\cos(k(L-x))$ ne dépend pas de $t$).


**q3.** Exprimer la surpression acoustique (notation complexe) $\tilde p(x,t)=-\dfrac{1}{\chi_S}\dfrac{\partial\Psi}{\partial x}$.

> [!tip]- 💡 Coup de pouce
> Dérivez simplement l'expression de $\Psi(x,t)$ trouvée en 2) par rapport à $x$, puis utilisez $1/\chi_S=\rho_0 c^2$ (cf. point cours de l'exercice 1) et $k=\omega/c$ pour simplifier.


**q4.** En déduire les fréquences $f_n$ de résonance en surpression, en fonction de $n\in\mathbb{N}^*$, $c$ et $L$.

> [!tip]- 💡 Coup de pouce
> Un tube ouvert-ouvert a un ventre de déplacement (donc un nœud de surpression) à chaque extrémité : condition analogue à une corde fixée aux deux bouts mais sur la pression. La condition en $x=L$ est déjà satisfaite automatiquement par construction (cf. remarque du point cours) ; il reste à imposer la même condition en $x=0$.


**q5.** Positions des maxima/minima de surpression ; représenter graphiquement jusqu'à la 3e harmonique (n=4).

> [!tip]- 💡 Coup de pouce
> Les nœuds de pression sont aux extrémités ouvertes, les ventres au milieu des segments -- comme les nœuds/ventres de déplacement pour une corde fixée.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex3-onde-stationnaire-tube-de-kundt-ferme-a-faire-a-la-maison|Exercice 3 — Onde stationnaire, tube de Kundt fermé (à faire à la maison)]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex5-energie-intensite-acoustique-et-niveau-sonore-de-l-oreille-humaine-a-l-onde-stationnaire|Exercice 5 — Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex6-tube-d-impedance-mesurer-l-absorption-d-un-materiau-avec-une-onde-stationnaire-partielle|Exercice 6 — Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex8-transmission-a-travers-une-lame-adaptation-d-impedance-loi-de-masse-et-double-vitrage|Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage]]

