---
title: Cohomologie
tags:
  - Mathematiques
  - Cohomologie
lang: fr
---

> Retour : [[00_Index]] · [[02_Formes_differentielles_calcul_exterieur]] · [[03_Fibres]] · [[04_Connexions]] · [[06_Algebres_de_Lie]]

# Cohomologie

**Principe** : une suite de $d$ avec $d^2=0$ ⇒ $\ker d\supset\operatorname{im}d$ ; le quotient mesure l'obstruction « fermée mais non exacte ». C'est l'invariant qui sait distinguer le trou d'un tore.

## 1. Complexes et cohomologie

Un **complexe de cochaînes** $(C^\bullet,d)$ : $\cdots\to C^{k-1}\xrightarrow{d}C^k\xrightarrow{d}C^{k+1}\to\cdots$, $d^2=0$. $Z^k=\ker d$ (cocycles), $B^k=\operatorname{im}d$ (cobords), $H^k=Z^k/B^k$. Une suite exacte courte de complexes ⇒ **suite exacte longue** $\cdots\to H^k(A)\to H^k(B)\to H^k(C)\xrightarrow{\delta}H^{k+1}(A)\to\cdots$.

## 2. Cohomologie de de Rham

$H^k_{dR}(M)\doteq\{\alpha\in\Omega^k:d\alpha=0\}/\,d\Omega^{k-1}$.
- **Invariance par homotopie** (lemme de Poincaré) : $H^k(\mathbb R^n)=0$ ($k>0$), $H^0=\mathbb R$.
- **Exemples** : $H^k(S^1)=\mathbb R,\mathbb R$ ($k=0,1$) — générateur $d\theta/2\pi$ ; $H^k(S^n)=\mathbb R$ pour $k=0,n$, sinon $0$ ; $H^k(T^n)=\mathbb R^{\binom nk}$ ; $H^\ast(\mathbb{CP}^n)=\mathbb R[x]/x^{n+1}$, $\deg x=2$ ; $\mathbb R^3\setminus\{0\}\simeq S^2$ : $H^2=\mathbb R$ (flux magnétique d'un monopôle).
- **Mayer–Vietoris** : $M=U\cup V$ ⇒ $\cdots\to H^k(M)\to H^k(U)\oplus H^k(V)\to H^k(U\cap V)\xrightarrow{\delta}H^{k+1}(M)\to\cdots$.
- **Nombres de Betti** $b_k=\dim H^k$ ; **caractéristique d'Euler** $\chi(M)=\sum_k(-1)^kb_k$ ($\chi(S^2)=2$, $\chi(T^2)=0$) ; **Gauss–Bonnet–Chern** : $\chi(M)=\int_M e(R)$ (classe d'Euler de la courbure).
- **Dualité de Poincaré** ($M$ compacte orientée) : $H^k\simeq(H^{n-k})^\ast$ via $\int\alpha\wedge\beta$ ; $b_k=b_{n-k}$.
- **Théorème de Hodge** : sur compacte riemannienne orientée, chaque classe de $H^k_{dR}$ contient une unique forme **harmonique** ($\Delta\alpha=0$) : $H^k\simeq\mathcal H^k$ ([[02_Formes_differentielles_calcul_exterieur]]). Donc $\operatorname{Tr}(-1)^Fe^{-\beta H}=\chi(M)$ pour la SUSY-QM de Witten ([[01_Supersymetrie]]).
- **de Rham** : $H^k_{dR}(M)\simeq H^k_{\text{sing}}(M;\mathbb R)\simeq\check H^k(M;\mathbb R)$ (singulière, Čech).

## 3. Cohomologie de Čech et classification des fibrés

Pour un recouvrement $\mathcal U$, un fibré en droites ⇔ cocycle $g_{\alpha\beta}\in\check C^1(\mathcal U,\mathcal O^\ast)$ ; $\mathrm{Pic}(M)\simeq H^1(M,\mathcal C^\infty(M,U(1)))\simeq H^2(M,\mathbb Z)$ (suite exponentielle) : **classe de Chern** $c_1$. Pour $G$ non abélien : $\check H^1(M,G)$ (ensemble pointé) classe les $G$-fibrés principaux ([[03_Fibres]]).
**Dirac** : un monopôle de charge $g$ sur $S^2$ est un fibré en droites de $c_1=\tfrac{eg}{2\pi\hbar}\in\mathbb Z$ : $\ eg=2\pi\hbar n$ (quantification de la charge).

## 4. Chern–Weil

Pour une connexion $A$ de courbure $F$ sur $P$ et $P$ polynôme $\mathrm{Ad}$-invariant : $P(F)$ est fermée et sa classe est indépendante de $A$ ([[04_Connexions]]). Exemples : classes de Chern $c_k$ ($\det(1+\tfrac i{2\pi}F)$), de Pontryagin $p_k$, classe d'Euler. Descente : $P(F)=d\,\mathrm{CS}$ (formes de transgression), anomalies de jauge/gravité (Green–Schwarz, [[04_Cordes_et_theorie_M]]).

## 5. Cohomologie des algèbres de Lie (Chevalley–Eilenberg)

Pour $\mathfrak g$ et un $\mathfrak g$-module $V$ : cochaînes $C^k(\mathfrak g,V)=\mathrm{Hom}(\Lambda^k\mathfrak g,V)$ et
$$(d\omega)(x_0,\dots,x_k)=\sum_i(-1)^ix_i\cdot\omega(\dots\hat x_i\dots)+\sum_{i<j}(-1)^{i+j}\omega([x_i,x_j],\dots\hat x_i\dots\hat x_j\dots).$$
- $H^1(\mathfrak g,\mathbb R)=(\mathfrak g/[\mathfrak g,\mathfrak g])^\ast$.
- **$H^2(\mathfrak g,\mathbb R)$ classe les extensions centrales** $0\to\mathbb R\to\hat{\mathfrak g}\to\mathfrak g\to0$ : un 2-cocycle $c$ donne $[x,y]_{\hat{}}=[x,y]+c(x,y)\,z$. **Exemples physiques** : (i) algèbre de Galilée : $c(K_i,P_j)=m\,\delta_{ij}$ ⇒ **extension de Bargmann** ($m$ = charge centrale, [[05_Lagrange_Hamilton_Noether]]) ; (ii) lacet de $\mathfrak{su}(N)$ ⇒ Kac–Moody ; (iii) $\mathrm{Vect}(S^1)$ ⇒ **Virasoro** (charge centrale $c$) ; (iv) super-Poincaré : charges centrales $Z$ ([[01_Supersymetrie]]).
- **Whitehead** : si $\mathfrak g$ est semi-simple de dimension finie, $H^1(\mathfrak g,V)=H^2(\mathfrak g,V)=0$ ($V$ de dim. finie) ; $H^3(\mathfrak g,\mathbb R)\ne0$ (3-cocycle de Cartan $\langle x,[y,z]\rangle$ ⇒ terme de Wess–Zumino–Witten).
- **Théorème de Chevalley–Eilenberg** : pour $G$ compact connexe, $H^\ast_{dR}(G)\simeq H^\ast(\mathfrak g,\mathbb R)$ (formes invariantes à gauche ; $\theta=g^{-1}dg$, [[07_Groupes_de_Lie]]).

## 6. BRST et cohomologie en physique

Quantification des théories de jauge : on introduit des fantômes $c$ (degré $+1$) et l'opérateur de Becchi–Rouet–Stora–Tyutin $s$ avec $s^2=0$ : $sA=Dc$, $sc=-\tfrac12[c,c]$ ; les observables physiques sont la **cohomologie BRST** $H^0(s)$. L'algèbre de Chevalley–Eilenberg de l'algèbre de jauge en est la version classique. Cohomologie de $Q$ en SUSY ($Q^2=0$ pour $Q=d$ ou $Q_\alpha$ chiral).

## 7. Autres cohomologies utiles

| Théorie | Complexe | Sert à |
|---|---|---|
| de Rham | $(\Omega^\bullet,d)$ | topologie, flux, charges |
| Čech | cochaînes d'un recouvrement | fibrés, anneaux de faisceaux |
| Dolbeault | $(\Omega^{p,q},\bar\partial)$ | variétés complexes, Calabi–Yau |
| Lie (C–E) | $(\Lambda^\bullet\mathfrak g^\ast,d)$ | extensions centrales, anomalies |
| équivariante | $(\Omega^\bullet(M)\otimes S\mathfrak g^\ast)^G$ | localisation (Duistermaat–Heckman), moment map |
| de Hochschild/cyclique | algèbres non commutatives | géométrie non commutative |
| K-théorie | classes de fibrés | charges de D-branes |
