---
title: Supersymétrie ★★★
tags:
  - Physique
  - Mathematiques
lang: fr
partie: XII
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Supersymétrie ★★★

> [!info] Statut
> Cadre mathématique rigoureux (superalgèbres, théorème de Coleman–Mandula, HLS, indice de Witten) ; **aucune superparticule n'a été observée** à ce jour. Les formules explicites en notation à deux composantes suivent les conventions de Wess–Bagger, **au signe et au facteur de convention près**.

## XII.1 Pourquoi des symétries fermioniques

- **Coleman–Mandula (1967)** : dans une théorie quantique des champs relativiste avec matrice $S$ non triviale (et écart de masse), l'algèbre de Lie des symétries de $S$ est $\mathfrak{iso}(1,3)\oplus\mathfrak g_{\text{interne}}$ : on ne peut **pas** mélanger spin et symétrie interne avec des générateurs bosoniques.
- **Haag–Łopuszański–Sohnius (1975)** : l'unique échappatoire est d'autoriser des générateurs **fermioniques** : algèbres de Lie **graduées** (superalgèbres). La symétrie la plus générale est le **super-Poincaré**.

## XII.2 Superalgèbres de Lie

Un espace $\mathfrak g=\mathfrak g_0\oplus\mathfrak g_1$ ($\mathbb Z_2$-gradué) avec un **super-crochet** $[\cdot,\cdot\}$ : commutateur sur $\mathfrak g_0\times\mathfrak g_0$ et $\mathfrak g_0\times\mathfrak g_1$ ; **anticommutateur symétrique** sur $\mathfrak g_1\times\mathfrak g_1$ :
$$
[X,Y\}=-(-1)^{|X||Y|}[Y,X\},\qquad(-1)^{|X||Z|}[X,[Y,Z\}\}+\text{(perm. cycliques)}=0\ \ (\text{super-Jacobi}).
$$
Les paramètres de transformation fermioniques sont des **nombres de Grassmann** ($\epsilon_1\epsilon_2=-\epsilon_2\epsilon_1$).

## XII.3 Super-Poincaré ($\mathcal N=1$, $D=4$)

Générateurs : $P_\mu$, $M_{\mu\nu}$ (Poincaré, X.2) et supercharges $Q_\alpha,\bar Q_{\dot\alpha}$ (spineurs de Weyl) :
$$
\{Q_\alpha,\bar Q_{\dot\beta}\}=2\,\sigma^\mu_{\alpha\dot\beta}P_\mu,\qquad\{Q_\alpha,Q_\beta\}=0=\{\bar Q_{\dot\alpha},\bar Q_{\dot\beta}\},\qquad[P_\mu,Q_\alpha]=0,\qquad[M_{\mu\nu},Q_\alpha]\propto(\sigma_{\mu\nu})_\alpha{}^\beta Q_\beta .
$$
**Lecture « torseur »** : $Q$ est une « racine carrée » de la translation ; le *super-torseur* $\{P^\mu;M^{\mu\nu};Q\}$ se transporte par Varignon *sans* mélange de $Q$ (car $[P,Q]=0$), mais $Q$ tourne sous $M$.
**Version étendue** $\mathcal N$ : $\{Q^I_\alpha,\bar Q_{J\dot\beta}\}=2\delta^I_J\sigma^\mu_{\alpha\dot\beta}P_\mu$, $\{Q^I_\alpha,Q^J_\beta\}=\varepsilon_{\alpha\beta}Z^{IJ}$ avec **charges centrales** $Z^{IJ}$ (antisymétriques, commutant avec tout) ; **symétrie R** $U(\mathcal N)$ des $Q$.

**Conséquences immédiates** :
1. $\sum_\alpha\{Q_\alpha,Q_\alpha^\dagger\}=4P^0=4H$ ⟹ $\boxed{H\geq0}$ ; l'énergie du vide est nulle ssi la supersymétrie n'est pas brisée.
2. $[P^2,Q]=0$ ⟹ les membres d'un supermultiplet ont **même masse** ; $(-1)^F$ anticommute avec $Q$ ⟹ autant de degrés de liberté bosoniques que fermioniques (hors vide).
3. Représentations : massless $\mathcal N=1$ : hélicités $(\lambda,\lambda+\tfrac12)$ ; multiplet chiral $(\phi,\psi)$ spin $(0,\tfrac12)$ ; vectoriel $(A_\mu,\lambda)$ spin $(1,\tfrac12)$.

## XII.4 Noether et superespace

- **Supercourant** $S^\mu_\alpha$, $\partial_\mu S^\mu_\alpha=0$, $Q_\alpha=\int S^0_\alpha\,d^3x$ : charge de Noether d'une symétrie à paramètre de Grassmann ; $[\epsilon Q+\bar\epsilon\bar Q,\phi]=\delta_\epsilon\phi$ (crochets gradués).
- **Algèbre sur les champs** : $[\delta_{\epsilon_1},\delta_{\epsilon_2}]\phi=-2i\,(\epsilon_1\sigma^\mu\bar\epsilon_2-\epsilon_2\sigma^\mu\bar\epsilon_1)\,\partial_\mu\phi$ : deux supersymétries successives *font une translation*.
- **Superespace** $(x^\mu,\theta^\alpha,\bar\theta^{\dot\alpha})$, $\theta$ de Grassmann. La super-translation $(\xi,\epsilon)$ agit par
$$
\theta\mapsto\theta+\epsilon,\qquad x^\mu\mapsto x^\mu+\xi^\mu+i(\theta\sigma^\mu\bar\epsilon-\epsilon\sigma^\mu\bar\theta),\qquad Q_\alpha=\partial_{\theta^\alpha}-i\sigma^\mu_{\alpha\dot\alpha}\bar\theta^{\dot\alpha}\partial_\mu .
$$
Un superchamp chiral : $\Phi=\phi+\sqrt2\theta\psi+\theta\theta F$.

## XII.5 Modèle de Wess–Zumino

Multiplet chiral $(\phi,\psi,F)$ avec superpotentiel holomorphe $W(\phi)$ :
$$
\mathcal L=-\partial_\mu\phi^\ast\partial^\mu\phi-i\bar\psi\bar\sigma^\mu\partial_\mu\psi+F^\ast F+\Big[W'(\phi)F-\tfrac12W''(\phi)\psi\psi+\text{h.c.}\Big].
$$
$F$ est auxiliaire : $F=-W'^\ast$, d'où $V(\phi)=|W'(\phi)|^2\ge0$. **Brisure spontanée** $\Leftrightarrow$ $W'(\phi)=0$ sans solution (O'Raifeartaigh) $\Rightarrow V_{\min}>0$, apparition d'un **goldstino**. **Théorèmes de non-renormalisation** (Grisaru–Siegel–Roček) : $W$ n'est pas corrigé perturbativement ; les divergences quadratiques se compensent boson/fermion (motivation : problème de hiérarchie).

## XII.6 Mécanique quantique supersymétrique et indice de Witten

$\mathcal H=\mathcal H_B\oplus\mathcal H_F$, $Q$ nilpotent ($Q^2=0$), $H\doteq\{Q,Q^\dagger\}\ge0$. Exemple $\mathcal N=2$ : $H=\tfrac12\big(p^2+W'(x)^2\big)+\tfrac\hbar2W''(x)\,\sigma_3$.
> [!tip] **Indice de Witten** $\ \operatorname{Tr}(-1)^Fe^{-\beta H}=n_B^{E=0}-n_F^{E=0}$, indépendant de $\beta$ et des déformations continues.
> *Preuve.* Les états $E>0$ sont appariés par $Q$ (bosons $\leftrightarrow$ fermions) et se compensent.

**Réalisation géométrique** (Witten 1982) : sur une variété riemannienne compacte $(M,g)$, $\mathcal H=\Omega^\bullet(M)$ (formes différentielles, $(-1)^F=(-1)^{\deg}$), $Q=d$, $Q^\dagger=\delta$, $H=\{d,\delta\}=\Delta_{\text{Hodge}}$. Alors $E=0\Leftrightarrow$ forme harmonique, et $\operatorname{Tr}(-1)^F=\sum(-1)^kb_k=\chi(M)$ (**caractéristique d'Euler**). Retour aux opérateurs de la partie I : le laplacien de Laplace–Beltrami est le $H$ de la SUSY-QM.

## XII.7 États BPS et classification

- Avec charges centrales : $M\ge|Z|$ (borne de **Bogomolny–Prasad–Sommerfield**) ; les états saturant la borne préservent une fraction de la SUSY, forment des multiplets courts, et leur masse est exacte (protégée).
- **Nahm (1978)** : une théorie avec particules de spin $\le2$ a au plus **32 supercharges réelles**, donc $D\le11$.

| $D$ | spineur minimal | supercharges max | théorie |
|---|---|---|---|
| 4 | Majorana (4 réelles) | 32 ($\mathcal N=8$) | sugra $\mathcal N=8$ |
| 10 | Majorana–Weyl (16) | 32 | IIA, IIB (32) ; I, hétérotique (16) |
| 11 | Majorana (32) | 32 | supergravité à 11 dimensions |

## XII.8 Phénoménologie (statut)

MSSM : un superpartenaire par particule du Modèle Standard, symétrie $R$-parité $\Rightarrow$ particule stable (neutralino, candidat matière noire) ; unification des constantes de couplage vers $\sim2\times10^{16}$ GeV. **Aucun signal au LHC** à ce jour : des limites de l'ordre du TeV pèsent sur gluinos/squarks (modèles dépendants). La supersymétrie reste surtout un outil mathématique central (sugra, cordes, QFT exactes).
