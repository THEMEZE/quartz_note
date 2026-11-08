---
title: Formes différentielles et calcul extérieur
tags:
  - Mathematiques
  - Formes-differentielles
lang: fr
---

> Retour : [[00_Index]] · avant : [[01_Varietes_differentielles]] · suite : [[05_Cohomologie]] · [[04_Connexions]]
> Reprend et corrige les notes *Calcul différentiel extérieur et géométrie* (d'après F. Hélein) et *Forme-différentielle* (voir [[99_Errata_des_notes_importees]]).

# Formes différentielles et calcul extérieur

## 1. Algèbre extérieure d'un espace vectoriel

Soit $V$ un $\mathbb R$-espace vectoriel de dimension $m$, $V^\ast$ son dual.

**Définition.** Une **$p$-forme** sur $V$ est une application $\alpha\colon V^p\to\mathbb R$, **$p$-linéaire alternée** : linéaire en chaque variable et $\alpha(\dots,v_i,\dots,v_j,\dots)=-\alpha(\dots,v_j,\dots,v_i,\dots)$. On note $\Lambda^pV^\ast$ cet espace ; $\Lambda^0V^\ast=\mathbb R$, $\Lambda^1V^\ast=V^\ast$, $\Lambda^pV^\ast=\{0\}$ si $p>m$, $\dim\Lambda^pV^\ast=\binom mp$.

**Produit extérieur** $\Lambda^pV^\ast\times\Lambda^qV^\ast\to\Lambda^{p+q}V^\ast$ :
$$
(\alpha\wedge\beta)(v_1,\dots,v_{p+q})\doteq\frac1{p!\,q!}\sum_{\sigma\in\mathfrak S_{p+q}}(-1)^{|\sigma|}\alpha(v_{\sigma(1)},\dots,v_{\sigma(p)})\,\beta(v_{\sigma(p+1)},\dots,v_{\sigma(p+q)}) .
$$
- bilinéaire, **associatif** : $(\alpha\wedge\beta)\wedge\gamma=\alpha\wedge(\beta\wedge\gamma)$ ;
- **commutatif gradué** : $\beta\wedge\alpha=(-1)^{pq}\alpha\wedge\beta$ ; en particulier $\alpha\wedge\alpha=0$ si $p$ impair ;
- $\Lambda^\bullet V^\ast\doteq\bigoplus_{p=0}^m\Lambda^pV^\ast$ est une **algèbre graduée** de dimension $2^m$ (cf. [[08_Algebres_graduees_ideaux_superalgebres]]).

**Exemples.** (i) $\alpha,\beta\in V^\ast$ : $(\alpha\wedge\beta)(v,w)=\alpha(v)\beta(w)-\beta(v)\alpha(w)=\begin{vmatrix}\alpha(v)&\alpha(w)\\ \beta(v)&\beta(w)\end{vmatrix}$. Si $\alpha=a_1\theta_1+a_2\theta_2$, $\beta=b_1\theta_1+b_2\theta_2$ en dimension 2 : $\alpha\wedge\beta=(a_1b_2-a_2b_1)\,\theta_1\wedge\theta_2$.
(ii) $\alpha_1\wedge\dots\wedge\alpha_p(v_1,\dots,v_p)=\det\big(\alpha_i(v_j)\big)_{ij}$.
(iii) $\alpha\in V^\ast$, $\beta\in\Lambda^2V^\ast$ : $(\alpha\wedge\beta)(u,v,w)=\alpha(u)\beta(v,w)+\alpha(v)\beta(w,u)+\alpha(w)\beta(u,v)$.

**Produit intérieur** $\iota_\xi\alpha(v_2,\dots,v_p)\doteq\alpha(\xi,v_2,\dots,v_p)$ ($\iota_\xi f=0$ pour $p=0$). Propriétés : $\iota_\xi\iota_\eta=-\iota_\eta\iota_\xi$ (donc $\iota_\xi^2=0$) et **Leibniz gradué** $\iota_\xi(\alpha\wedge\beta)=\iota_\xi\alpha\wedge\beta+(-1)^p\alpha\wedge\iota_\xi\beta$ : $\iota_\xi$ est une **antidérivation** de degré $-1$.

## 2. Formes différentielles

Sur un ouvert $U\subset\mathbb R^m$ (ou une variété, [[01_Varietes_differentielles]]) une **$p$-forme différentielle** est une application lisse $\alpha\colon U\to\Lambda^p(\mathbb R^m)^\ast$ ; en coordonnées $\alpha=\tfrac1{p!}\alpha_{i_1\dots i_p}dx^{i_1}\wedge\dots\wedge dx^{i_p}$ ($\alpha_{i_1\dots i_p}$ antisymétrique). $\Omega^p(M)$ : l'espace ; $\Omega^\bullet=\bigoplus_p\Omega^p$.

**Deux exemples fondateurs** : une 0-forme est une fonction ; pour $\varphi\in C^1(U)$, $d\varphi=\partial_i\varphi\,dx^i$ est une 1-forme.

## 3. Différentielle extérieure

> **Théorème–définition.** Il existe une unique application $\mathbb R$-linéaire $d\colon\Omega^p\to\Omega^{p+1}$ telle que (a) $d f$ est la différentielle usuelle pour $f\in\Omega^0$ ; (b) $d(\alpha\wedge\beta)=d\alpha\wedge\beta+(-1)^p\alpha\wedge d\beta$ (Leibniz gradué) ; (c) $d\circ d=0$.
> En coordonnées : $d\alpha=\tfrac1{p!}\partial_j\alpha_{i_1\dots i_p}dx^j\wedge dx^{i_1}\wedge\cdots$ ; pour $A=A_\mu dx^\mu$ : $dA=\partial_\mu A_\nu\,dx^\mu\wedge dx^\nu=\tfrac12(\partial_\mu A_\nu-\partial_\nu A_\mu)\,dx^\mu\wedge dx^\nu$.

*Preuve de $d^2=0$* : $d^2f=\partial_j\partial_if\,dx^j\wedge dx^i=0$ (Schwarz + antisymétrie), puis Leibniz. $\square$

**Formule invariante.** Pour une 1-forme $A$ et des champs $X,Y$ :
$$
dA(X,Y)=X\big(A(Y)\big)-Y\big(A(X)\big)-A\big([X,Y]\big).
$$
(Conséquence : $d$ mesure le défaut de commutation des flots ; cf. torsion, [[04_Connexions]].) Générale : $d\alpha(X_0,\dots,X_p)=\sum_i(-1)^iX_i\alpha(\dots\widehat{X_i}\dots)+\sum_{i<j}(-1)^{i+j}\alpha([X_i,X_j],\dots\widehat{X_i}\dots\widehat{X_j}\dots)$.

**Naturalité** : $f^\ast d=d f^\ast$.

## 4. Calcul de Cartan : trois opérateurs, une superalgèbre

Sur $\Omega^\bullet(M)$ : $d$ (degré $+1$, antidérivation), $\iota_X$ (degré $-1$, antidérivation), $\mathcal L_X$ (degré $0$, dérivation).

> **Formule magique de Cartan** : $\ \mathcal L_X=d\,\iota_X+\iota_X\,d=\{d,\iota_X\}.$
> Relations complètes : $\{d,d\}=2d^2=0$, $\{\iota_X,\iota_Y\}=0$, $[\mathcal L_X,d]=0$, $[\mathcal L_X,\iota_Y]=\iota_{[X,Y]}$, $[\mathcal L_X,\mathcal L_Y]=\mathcal L_{[X,Y]}$.

C'est la structure d'une **superalgèbre de Lie** ($d,\iota_X$ impairs, $\mathcal L_X$ pair) agissant sur l'algèbre différentielle graduée $(\Omega^\bullet,\wedge,d)$ : voir [[08_Algebres_graduees_ideaux_superalgebres]].

## 5. Lemme de Poincaré, Stokes, Hodge

- **Poincaré** : sur un ouvert étoilé, toute forme fermée ($d\alpha=0$) est exacte ($\alpha=d\beta$). Opérateur d'homotopie $K$ avec $dK+Kd=\mathrm{id}$ ; l'obstruction globale est la cohomologie de de Rham ([[05_Cohomologie]]).
- **Stokes** : $\int_Md\alpha=\int_{\partial M}\alpha$.
- **Dualité de Hodge** (variété riemannienne orientée) : $\star\colon\Omega^p\to\Omega^{n-p}$, $\alpha\wedge\star\beta=\langle\alpha,\beta\rangle\mathrm{vol}$ ; $\star\star=(-1)^{p(n-p)}s$ ($s$ = signe de $\det g$). Codifférentielle $\delta=(-1)^{\dots}\star d\star$, laplacien de Hodge $\Delta=d\delta+\delta d$ (égal à $-\nabla^2$ sur les fonctions et c'est le $H$ de la SUSY-QM, [[01_Supersymetrie]]).

## 6. Dictionnaire en dimension 3 et Maxwell

| Opération vectorielle | Forme |
|---|---|
| $\operatorname{grad}f$ | $d f$ (via $\sharp$) |
| $\operatorname{rot}\vec v$ | $\star d(v^\flat)$ |
| $\operatorname{div}\vec v$ | $\star d\star(v^\flat)$ |
| $\operatorname{rot}\operatorname{grad}=0$, $\operatorname{div}\operatorname{rot}=0$ | $d^2=0$ |

**Maxwell** (espace-temps $\mathbb R^{1,3}$) : $F=dA$, donc $dF=0$ (pas de monopôle, Faraday) ; équation dynamique $d{\star F}={\star J}$ (courants), d'où $d{\star J}=0$ (conservation de la charge). Action $S=-\tfrac12\int F\wedge\star F+\int A\wedge\star J$.

## 7. Intégration sur des sous-variétés (lien avec la mécanique)

Pour $\Sigma\subset M$ de dimension $k$ : $\int_\Sigma\alpha$ ; flux, circulation, aire. L'**invariant intégral de Poincaré–Cartan** $\oint p\,dq$ est conservé par le flot hamiltonien ; $\omega=d\theta$ ([[01_Varietes_differentielles]], [[05_Lagrange_Hamilton_Noether]]). Le **moment d'une force** est un élément de $\Lambda^2E$, bivecteur ([[02_Torseurs_Varignon_generalise]]) : la 2-forme duale.
