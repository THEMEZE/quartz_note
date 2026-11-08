---
title: Théorie des cordes et théorie M ★★★
tags:
  - Physique
  - Mathematiques
lang: fr
partie: XV
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Théorie des cordes et théorie M ★★★

## XV.1 La corde et son torseur

Action de Nambu–Goto, puis de Polyakov ($\gamma_{ab}$ métrique auxiliaire) :
$$
S_{NG}=-T\int d^2\sigma\sqrt{-\det h_{ab}},\ \ h_{ab}\doteq\partial_aX^\mu\partial_bX_\mu,\ \ T=\frac1{2\pi\alpha'}=\frac1{2\pi\ell_s^2};\qquad S_P=-\frac T2\int d^2\sigma\sqrt{-\gamma}\,\gamma^{ab}\partial_aX\cdot\partial_bX .
$$
**Torseur de la corde** (système continu de III.5) : $P^\mu=T\int d\sigma\,\partial_\tau X^\mu$, $M^{\mu\nu}=T\int d\sigma(X^\mu\partial_\tau X^\nu-X^\nu\partial_\tau X^\mu)$, avec la même loi de transport de Varignon.
**Cohérence quantique** (annulation de l'anomalie conforme) : $D=26$ (bosonique) ; $D=10$ (superstring : RNS/Green–Schwarz). Le spectre fermé contient un **graviton** $g_{\mu\nu}$, un champ $B_{\mu\nu}$, un dilaton $\Phi$ ($g_s=e^{\langle\Phi\rangle}$) : la gravitation est incluse automatiquement ; $2\kappa_{10}^2=(2\pi)^7g_s^2\ell_s^8$.

## XV.2 Cinq théories de supercordes et dualités

| Théorie | Supercharges | Jauge |
|---|---|---|
| Type I | 16 | $SO(32)$ |
| Type IIA | 32 | — |
| Type IIB | 32 (chirale) | — |
| Hétérotique $SO(32)$ | 16 | $SO(32)$ |
| Hétérotique $E_8\times E_8$ | 16 | $E_8\times E_8$ |

Annulation d'anomalies de Green–Schwarz (1984) $\Rightarrow$ $SO(32)$ ou $E_8\times E_8$. **Dualités** : T ($R\leftrightarrow\ell_s^2/R$) ; S de IIB ($g_s\to1/g_s$, $SL(2,\mathbb Z)$) ; type I $\leftrightarrow$ hétérotique $SO(32)$ ($g_s\to1/g_s$).

## XV.3 Théorie M (Witten 1995)

À fort couplage, IIA devient une théorie à **11 dimensions** de rayon $R_{11}=g_s\ell_s$ :
$$
\ell_{11}=g_s^{1/3}\ell_s,\qquad2\kappa_{11}^2=(2\pi)^8\ell_{11}^9,\qquad\text{limite basse énergie}=\text{sugra à 11D (XIII.2)}.
$$
- Les **D0-branes** sont les modes de Kaluza–Klein ($m=1/R_{11}=1/g_s\ell_s$) : leur charge est la charge de Noether de l'isométrie $\partial_{11}$ (XIII.3).
- **Membranes** : M2 ($T_{M2}=\frac1{(2\pi)^2\ell_{11}^3}$) et M5 ($T_{M5}=\frac1{(2\pi)^5\ell_{11}^6}$), charges $Z_2,Z_5$ de la superalgèbre. M2 enroulée sur le cercle $\Rightarrow$ corde F1 de IIA : $T_{F1}=2\pi R_{11}T_{M2}=\frac1{2\pi\ell_s^2}$ ✓ ; M2 non enroulée $\Rightarrow$ D2 ; M5 enroulée $\Rightarrow$ D4, non enroulée $\Rightarrow$ NS5.
- **Hořava–Witten** : $E_8\times E_8$ hétérotique $=$ théorie M sur l'intervalle $S^1/\mathbb Z_2$, un $E_8$ sur chaque bord.
- **Théorie des matrices** (Banks–Fischler–Shenker–Susskind 1996) : M-théorie en moment infini $\simeq$ mécanique quantique supersymétrique **de $N$ D0-branes** à $N\to\infty$, $H\propto\operatorname{tr}\big(\Pi_i^2-\tfrac12[X^i,X^j]^2\big)+\text{fermions}$, avec $X^i\in\mathfrak u(N)$ (9 matrices) : les positions deviennent **non commutatives**.
- **AdS/CFT** (XIV.5) : $AdS_4\times S^7\leftrightarrow$ théorie ABJM ($N$ M2) ; $AdS_7\times S^4\leftrightarrow$ théorie $(2,0)$ en $D=6$ ($N$ M5).

## XV.4 Compactifications et statut

$4+7=11$ : théorie M sur une variété d'holonomie $G_2$ $\Rightarrow\mathcal N=1$, $D=4$ ; cordes sur Calabi–Yau $CY_3$. Flux et $\sim10^{500}$ vides estimés (paysage ; estimation heuristique) ; programme du « marais » (swampland). **Statut** : cohérence mathématique remarquable, dualités précises, AdS/CFT nonperturbatif ; **pas de confirmation expérimentale** ni de définition nonperturbative complète indépendante en espace plat. Ce qu'il faut retenir de l'ensemble XII–XV : à chaque palier, **le groupe de symétrie s'étend** (Poincaré $\to$ super-Poincaré $\to$ symétries locales $\to$ dualités), et les charges du torseur $\{P;M\}$ sont enrichies ($Q$, $Z_2$, $Z_5$, $D$-charges).
