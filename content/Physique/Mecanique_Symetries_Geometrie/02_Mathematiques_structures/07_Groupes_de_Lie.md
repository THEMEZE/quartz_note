---
title: Groupes de Lie
tags:
  - Mathematiques
  - Groupes-de-Lie
lang: fr
---

> Retour : [[00_Index]] · avant : [[01_Varietes_differentielles]] · [[06_Algebres_de_Lie]] · suite : [[03_Fibres]]

# Groupes de Lie

## 1. Définition, algèbre de Lie

Un **groupe de Lie** $G$ est une variété lisse munie d'une structure de groupe pour laquelle $(g,h)\mapsto gh$ et $g\mapsto g^{-1}$ sont lisses. Translations à gauche $L_g\colon h\mapsto gh$, à droite $R_g$, conjugaison $c_g=L_gR_{g^{-1}}$.
**Algèbre de Lie** $\mathfrak g=T_eG\simeq\{$champs de vecteurs invariants à gauche$\}$ avec le crochet des champs ([[01_Varietes_differentielles]]). **Exponentielle** : $\exp\colon\mathfrak g\to G$, $\exp(tX)$ = sous-groupe à un paramètre ; pour $G\subset GL(n)$, $\exp X=\sum X^k/k!$. Difféo local en $0$.
**Baker–Campbell–Hausdorff** : $e^Xe^Y=\exp\big(X+Y+\tfrac12[X,Y]+\tfrac1{12}[X,[X,Y]]-\tfrac1{12}[Y,[X,Y]]+\cdots\big)$ : la loi de groupe est déterminée localement par $\mathfrak g$.
**Correspondance de Lie** : $\mathfrak g$ de dimension finie ⇒ il existe un unique groupe connexe simplement connexe $\tilde G$ d'algèbre $\mathfrak g$ ; tout groupe connexe d'algèbre $\mathfrak g$ est $\tilde G/\Gamma$ ($\Gamma$ discret central). Morphismes d'algèbres ⇔ morphismes de groupes si la source est simplement connexe.

## 2. Représentation adjointe, forme de Maurer–Cartan

- $\mathrm{Ad}_g=d(c_g)_e\colon\mathfrak g\to\mathfrak g$ ; $\mathrm{Ad}\,e^X=e^{\mathrm{ad}X}$ ; $d\mathrm{Ad}=\mathrm{ad}$.
- **Forme de Maurer–Cartan** $\theta\doteq g^{-1}dg\in\Omega^1(G,\mathfrak g)$ (matrices) ; équation de structure
$$d\theta+\theta\wedge\theta=0,\quad\text{i.e. } d\theta+\tfrac12[\theta,\theta]=0 .$$
C'est exactement « courbure nulle » : $\theta$ est la connexion plate canonique du fibré trivial $G\to\{pt\}$ ([[04_Connexions]]) ; $d\theta^a=-\tfrac12f_{bc}{}^a\theta^b\wedge\theta^c$.
- **Haar** : mesure invariante à gauche, unique à un scalaire près ; $G$ compact ⇒ bi-invariante ; moyennage ⇒ toute représentation d'un compact est unitarisable, complètement réductible.
- **Compact connexe** ⇒ $\mathfrak g=\mathfrak z\oplus\mathfrak g_{ss}$, forme de Killing définie négative sur $\mathfrak g_{ss}$ ⇒ métrique bi-invariante, $\pi_1(G_{ss})$ fini.

## 3. Groupes classiques

| Groupe | Définition | dim | Remarques |
|---|---|---|---|
| $GL(n,\mathbb R)$ | inversibles | $n^2$ | 2 composantes |
| $SL(n)$ | $\det=1$ | $n^2-1$ | |
| $O(n)$, $SO(n)$ | $R^{\mathsf T}R=1$ | $\tfrac{n(n-1)}2$ | $SO(n)$ connexe, $\pi_1=\mathbb Z_2$ ($n\ge3$) |
| $U(n)$, $SU(n)$ | $U^\dagger U=1$ | $n^2$, $n^2-1$ | $SU(n)$ simplement connexe |
| $Sp(n)$ | préserve $\omega$ quaternionique | $n(2n+1)$ | |
| $SO(p,q)$ | préserve $\eta_{p,q}$ | $\tfrac{(p+q)(p+q-1)}2$ | non compact |
| $E(n)=SO(n)\ltimes\mathbb R^n$ | isométries euclidiennes | $\tfrac{n(n+1)}2$ | **torseurs** ([[02_Torseurs_Varignon_generalise]]) |
| Poincaré $ISO(1,n)$ | isométries de Minkowski | $\tfrac{(n+1)(n+2)}2$ | ([[02_Relativite_restreinte_Poincare]]) |
| Galilée $\mathrm{Gal}(n)$ | boosts, rotations, translations | $\tfrac{n(n+1)}2+n+1$ | extension de Bargmann ([[05_Cohomologie]]) |

**Revêtements** : $SU(2)\to SO(3)$ (2:1), $SU(2)\simeq S^3$ ; $Spin(n)\to SO(n)$ (2:1) ; $SL(2,\mathbb C)\to SO_0(1,3)$ (2:1, la forme spinorielle du groupe de Lorentz, [[09_Algebres_de_Clifford_spineurs]]) ; $\mathbb{RP}^3\simeq SO(3)$. Les spineurs sont des représentations de $Spin$ qui ne descendent pas à $SO$.
**Exemple $SU(2)\to SO(3)$** : $q=e^{-i\theta\hat n\cdot\vec\sigma/2}$ agit sur $\vec v\cdot\vec\sigma\mapsto q(\vec v\cdot\vec\sigma)q^{-1}$ comme la rotation d'angle $\theta$ ; $q$ et $-q$ donnent la même rotation ; la formule de Rodrigues $R=\mathbb 1+\sin\theta[\hat n]_\times+(1-\cos\theta)[\hat n]_\times^2$.

## 4. Actions, espaces homogènes

Action $G\times M\to M$ ; **champ fondamental** $\xi_M(m)=\tfrac d{dt}|_0e^{t\xi}\cdot m$ avec $[\xi_M,\eta_M]=-[\xi,\eta]_M$ ; orbite $G\cdot m\simeq G/G_m$. **Espace homogène** $G/H$ : $G\to G/H$ est un $H$-fibré principal ([[03_Fibres]]). Exemples : $S^n=SO(n+1)/SO(n)$, $\mathbb{RP}^n$, $AdS_n=SO(2,n-1)/SO(1,n-1)$, $dS_n$, espace de Minkowski $=ISO(1,3)/SO(1,3)$.
La **symétrie du problème de Kepler** est $SO(n+1)$ (compacte), $E(n)$ à $E=0$, $SO(n,1)$ à $E>0$ ([[06_Kepler_Runge_Lenz_SO_n+1]]).

## 5. Application moment, orbites coadjointes, Noether

$G$ agit symplectiquement sur $(M,\omega)$ ; **application moment** $\mu\colon M\to\mathfrak g^\ast$, $\iota_{\xi_M}\omega=-d\langle\mu,\xi\rangle$, **équivariante** : $\mu(g\cdot m)=\mathrm{Ad}^\ast_g\mu(m)$ (à cocycle près). Les composantes $\langle\mu,\xi\rangle$ sont les **charges de Noether** ([[05_Lagrange_Hamilton_Noether]]). **Orbites coadjointes** $\mathcal O_\mu=\{\mathrm{Ad}^\ast_g\mu\}$ : variétés symplectiques canoniques (**Kirillov–Kostant–Souriau**) ; pour $E(3)$ : sphère de rayon $|\vec R|$ fibrée en hélicité $\to$ « spin » ; pour Poincaré : masse et spin → classification de Wigner.
**Hamiltonien de réduction** (Marsden–Weinstein) : $M/\!/G=\mu^{-1}(0)/G$ ; élimination de la rotation globale.

## 6. Représentations

- **Schur** : un opérateur d'entrelacement entre irreps est scalaire ; **Peter–Weyl** : $L^2(G)=\bigoplus_{\rho}V_\rho\otimes V_\rho^\ast$ (harmoniques sphériques pour $SO(3)$).
- Poids dominants, Weyl dimension formula ($\dim V_{(j)}=2j+1$ pour $SU(2)$) ; **Casimirs** ([[06_Algebres_de_Lie]]).
- **Groupes non compacts** : irreps unitaires de dimension infinie ; Lorentz : $(j_1,j_2)$ de $SL(2,\mathbb C)$ ; Poincaré : méthode des petites orbites de Wigner.

## 7. Supergroupes (renvoi)

Un **supergroupe de Lie** est un groupe dont l'algèbre est une superalgèbre ([[08_Algebres_graduees_ideaux_superalgebres]]) ; **super-Poincaré** : extension de $ISO(1,3)$ par des générateurs fermioniques $Q_\alpha$ ([[01_Supersymetrie]]).
