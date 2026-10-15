---
title: "Exercice 1 — Corde non homogène, jonction entre deux cordes"
tags:
  - td
  - chap-3-interfaces-entre-deux-milieux
---

[[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/index|⬅ Retour]] · [📄 Énoncé (td3_PhV212_enonce)](/pdfs/td3_PhV212_enonce.pdf) · [📄 Énoncé (td3_enonce)](/pdfs/td3_enonce.pdf)

### Exercice 1. Corde non homogène, jonction entre deux cordes

Deux cordes de longueur $L$ et de masses linéiques $\mu_1$ et $\mu_2=\alpha\mu_1$
sont attachées en un point de jonction $O$ pour former une corde tendue
horizontalement suivant l'axe $Ox$ avec une force de tension $F$. Le point
$O$ se situe en l'abscisse $x=0$.

Une onde transversale progressive se propageant dans le sens des $x$
décroissants (onde incidente) arrive au niveau de la jonction $O$. Il
s'agit d'une onde sinusoïdale d'amplitude $A_I$ et de pulsation $\omega$.
Elle donne naissance à une onde réfléchie se propageant dans le sens des
$x$ croissants ainsi qu'à une onde transmise se propageant dans le sens
des $x$ décroissants. Ces deux ondes sont aussi sinusoïdales et
progressives, de même pulsation $\omega$.

[![Suggestion : schéma de la corde double, jonction en $O$ ($x=0$) ; représenter la corde 1 (masse linéique $\mu_1$) où vivent l'onde incidente et l'onde réfléchie, et la corde 2 (masse linéique $\mu_2=\alpha\mu_1$) où se propage l'onde transmise, avec des flèches indiquant clairement les trois sens de propagation ($x$ décroissants pour l'incidente et la transmise, $x$ croissants pour la réfléchie).](/figures/td3_ex1_corde_double.svg)](/figures/td3_ex1_corde_double.svg)

**q1.** Donner l'expression de l'onde incidente $y_i(x,t)$ se déplaçant dans le sens des $x$ décroissants, d'amplitude $A_I$ et de déphasage $\phi=0$.

> [!tip]- 💡 Coup de pouce
> Une onde progressive vers les $x$ décroissants s'écrit $\cos(\omega t + kx)$ (le signe $+$ devant $kx$ est ce qui inverse le sens de propagation par rapport à la convention $\cos(\omega t-kx)$ rappelée dans les prérequis).


**q2.** Donner l'expression de l'onde réfléchie $y_r(x,t)$ se déplaçant dans le sens des $x$ croissants, d'amplitude $A_R$ et de déphasage $\phi=0$.

**q3.** Donner l'expression de l'onde transmise $y_t(x,t)$ se déplaçant dans le sens des $x$ décroissants, d'amplitude $A_T$ et de déphasage $\phi=0$.

**q4.** Pour chaque corde, donner la relation entre $k$, $\omega$ et $c$. Comment s'appelle cette relation ? Exprimer $k_1$ en fonction de $k_2$ et $\alpha$.

> [!tip]- 💡 Coup de pouce
> Relation de dispersion $\omega=kc$ avec $c=\sqrt{F/\mu}$ propre à chaque corde (cf. point cours) ; la pulsation $\omega$ est la même des deux côtés car le régime est établi et le point $O$ oscille avec une seule et même pulsation (continuité temporelle en $O$).


**q5.** Exprimer les déplacements verticaux $y_1(x,t)$ et $y_2(x,t)$ sur les cordes 1 et 2 respectivement.

**q6.** Écrire la condition de continuité sur le déplacement vertical $y(x,t)$ de la corde à la position $x=0$. Traduire cette relation en termes de $A_I$, $A_R$ et $A_T$.

> [!tip]- 💡 Coup de pouce
> $y_1(0,t)=y_2(0,t)$ à tout instant $t$ (cf.  point cours, condition 1).


**q7.** La relation de continuité de la force en $x=0$ donne $\left.\partial y_1/\partial x\right|_{x=0} = \left.\partial y_2/\partial x\right|_{x=0}$. Traduire cette relation en termes de $A_I$, $A_R$ et $A_T$.

> [!tip]- 💡 Coup de pouce
> Dérivez $y_1$ et $y_2$ par rapport à $x$, puis évaluez en $x=0$ ; les cosinus deviennent des sinus qui s'annulent sauf le terme en $x$ dérivé, attention aux signes de $k_1$ dans $y_i$ et $y_r$ (cf. remarque pédagogique sur ce point).


**q8.** En déduire les coefficients de réflexion $r$ et de transmission $t$, en amplitude, en fonction de $\alpha$. Écrire $r$ et $t$ en fonction des impédances des deux milieux après avoir défini $Z_1$ et $Z_2$, lesdites impédances.

> [!tip]- 💡 Coup de pouce
> Combinez les deux relations de continuité (questions 6 et 7) comme un système linéaire en $A_R,A_T$. Impédance mécanique d'une corde : $Z=\mu c=\sqrt{F\mu}$ (cf. point cours) ; attention, $Z$ et $k$ sont ici *directement* proportionnels (à $\omega,F$ fixés), et non inversement proportionnels.


**q9.** Commenter dans le cas où $\alpha=1$.

> [!tip]- 💡 Coup de pouce
> Si $\alpha=1$, les deux cordes sont identiques : il n'y a plus vraiment de jonction.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex3-perle-sur-une-corde-jonction-massive-filtre-passe-bas-puis-passe-bande|Exercice 3 — Perle sur une corde : jonction massive, filtre passe-bas puis passe-bande]]

