---
title: Algèbres graduées, idéaux, superalgèbres de Lie
tags:
  - Mathematiques
  - Algebres
  - Superalgebres
lang: fr
---

> Retour : [[00_Index]] · [[06_Algebres_de_Lie]] · [[02_Formes_differentielles_calcul_exterieur]] · [[01_Supersymetrie]]
> Version **corrigée et complétée** des notes *Algèbre graduée*, *Idéal*, *Super-algèbre de Lie* et *Algèbres graduées, formes différentielles et structure de superalgèbre de Lie* (corrections listées dans [[99_Errata_des_notes_importees]]).

# Algèbres graduées, idéaux, superalgèbres de Lie

## 1. Idéaux (rappels d'algèbre générale)

Soit $A$ un anneau (unitaire). Un **idéal à gauche** (resp. à droite) est un sous-groupe additif $I$ tel que $AI\subset I$ (resp. $IA\subset I$) ; un **idéal bilatère** est les deux à la fois (c'est « l'idéal » en algèbre commutative). Un sous-ensemble $I$ est un idéal bilatère **ssi** c'est le noyau d'un morphisme d'anneaux de source $A$ ; alors $A/I$ est un anneau et $A\to A/I$ un morphisme. Idéaux triviaux : $\{0\}$ et $A$ ; **propre** : $\ne A$.
Exemples : $n\mathbb Z\subset\mathbb Z$ (maximal ssi $n$ premier) ; $(x)\subset\mathbb K[x]$ ; pour un morphisme $f$, $\ker f$. Dans un anneau commutatif : $I$ maximal ⇔ $A/I$ corps ; premier ⇔ $A/I$ intègre.
**Idéaux de Lie** ([[06_Algebres_de_Lie]]) : $\mathfrak i\subset\mathfrak g$ avec $[\mathfrak g,\mathfrak i]\subset\mathfrak i$.
**Idéaux différentiels** : un idéal $I\subset\Omega^\bullet(M)$ est **différentiel** si $dI\subset I$ ; **Frobenius** : la distribution $D=\{\alpha_1=\dots=\alpha_k=0\}$ est intégrable ssi l'idéal engendré par les $\alpha_i$ est différentiel ([[01_Varietes_differentielles]]).

## 2. Algèbres graduées

**Définition.** Soit $\mathbb K$ un corps. Une **algèbre $\mathbb N$-graduée** est une $\mathbb K$-algèbre $\mathcal A$ munie d'une décomposition en sous-espaces $\mathcal A=\bigoplus_{i\in\mathbb N}\mathcal A_i$ telle que $\mathcal A_i\mathcal A_j\subset\mathcal A_{i+j}$. Éléments de $\mathcal A_i$ : **homogènes de degré $i$**. (On peut remplacer $\mathbb N$ par $\mathbb Z$, un monoïde $M$, ou $\mathbb Z_2$.)
- **Graduation triviale** : $\mathcal A_0=\mathcal A$ et $\mathcal A_i=\{0\}$ pour $i>0$ (**et non $\emptyset$** : chaque $\mathcal A_i$ est un sous-espace vectoriel, donc contient $0$).
- **Morphisme gradué** : $f(\mathcal A_i)\subset\mathcal B_i$.
- **Idéal homogène** : contient les composantes homogènes de chacun de ses éléments, ⇔ engendré par des éléments homogènes ; alors $\mathcal A/I$ est gradué : $(\mathcal A/I)_i=\mathcal A_i/(I\cap\mathcal A_i)$.
- **Exemples** : $\mathbb K[X_1,\dots,X_d]$ (degré total) ; algèbre tensorielle $T(V)$ ; algèbre symétrique $S(V)=T(V)/(v\otimes w-w\otimes v)$ ; **algèbre extérieure** $\Lambda V=T(V)/(v\otimes v)$ ; $\mathrm{Cl}(V,q)$ ($\mathbb Z_2$-graduée, [[09_Algebres_de_Clifford_spineurs]]) ; $H^\bullet(M)$ ; $\Omega^\bullet(M)$.
- **Commutativité graduée** (signe de Koszul) : $ab=(-1)^{|a||b|}ba$ pour $a,b$ homogènes. $\Lambda V$ et $\Omega^\bullet$ sont graduées-commutatives ; $S(V)$ est commutative.
- **Dérivation graduée de degré $k$** : $D\colon\mathcal A_i\to\mathcal A_{i+k}$, $D(ab)=D(a)b+(-1)^{k|a|}aD(b)$. Ex. : $d$ (degré $+1$), $\iota_X$ (degré $-1$), $\mathcal L_X$ (degré $0$).
- **Algèbre différentielle graduée (DGA)** : $(\mathcal A,d)$ avec $d$ dérivation de degré $+1$, $d^2=0$ : $(\Omega^\bullet(M),\wedge,d)$, complexe de Chevalley–Eilenberg ([[05_Cohomologie]]), complexe BRST.

**Algèbre de Grassmann** $\Lambda_N=\Lambda(\mathbb R^N)=\mathbb R[\theta^1,\dots,\theta^N]$, $\theta^i\theta^j=-\theta^j\theta^i$, $(\theta^i)^2=0$ ; $\dim=2^N$ ; développement $f(\theta)=f_0+f_i\theta^i+\tfrac12f_{ij}\theta^i\theta^j+\cdots$. **Intégrale de Berezin** : $\int d\theta\,1=0$, $\int d\theta\,\theta=1$ (l'intégration est la dérivation). C'est l'algèbre des paramètres/coordonnées de supersymétrie ([[01_Supersymetrie]]).

## 3. Espace vectoriel $\mathbb Z_2$-gradué, super-algèbres

Un **superespace** $V=V_0\oplus V_1$ ($V_0$ pair/bosonique, $V_1$ impair/fermionique), $|x|\in\{0,1\}$ le degré (ou **parité**). $\dim V=(p|q)$. Un **produit** est gradué si $V_iV_j\subset V_{i+j\bmod2}$ ; une **superalgèbre** est une algèbre $\mathbb Z_2$-graduée (super-anneau = superalgèbre sur $\mathbb Z$). Pour $x,y$ homogènes : $|xy|=|x|+|y|\bmod2$.
**Exemple fondamental** $\mathrm{End}(V)=\mathfrak{gl}(p|q)$, matrices par blocs $\begin{pmatrix}A&B\\C&D\end{pmatrix}$ : pair si $B=C=0$, impair si $A=D=0$.

## 4. Superalgèbres de Lie

> **Définition.** Une **superalgèbre de Lie** est une superalgèbre $\mathfrak g=\mathfrak g_0\oplus\mathfrak g_1$ avec un **super-crochet** bilinéaire $[\cdot,\cdot\}\colon\mathfrak g\times\mathfrak g\to\mathfrak g$, $[\mathfrak g_i,\mathfrak g_j\}\subset\mathfrak g_{i+j}$, tel que pour $x,y,z$ homogènes :
> 1. **super-antisymétrie** : $[x,y\}=-(-1)^{|x||y|}[y,x\}$ ;
> 2. **super-Jacobi** : $(-1)^{|x||z|}[x,[y,z\}\}+(-1)^{|y||x|}[y,[z,x\}\}+(-1)^{|z||y|}[z,[x,y\}\}=0$.

Conséquences : sur $\mathfrak g_0\times\mathfrak g_0$ et $\mathfrak g_0\times\mathfrak g_1$ c'est un **commutateur** antisymétrique ; sur $\mathfrak g_1\times\mathfrak g_1$ c'est un **anticommutateur symétrique** $\{Q,Q'\}$. Donc $\mathfrak g_0$ est une algèbre de Lie et $\mathfrak g_1$ une représentation de $\mathfrak g_0$, avec une application symétrique $S^2\mathfrak g_1\to\mathfrak g_0$ équivariante. Propriétés : $[x,x\}=0$ pour $x$ pair ; $[[x,x\},x\}=0$ pour $x$ impair (**Jacobi impair**, c'est une condition en soi si on ne suppose pas $\mathrm{char}\ne3$).
**Réalisation associative** : dans $\mathrm{End}(V)$ ou une algèbre associative graduée : $[x,y\}\doteq xy-(-1)^{|x||y|}yx$. (Cette formule n'est **valable que dans une algèbre associative graduée**, pas dans une superalgèbre de Lie abstraite.)
**Idéaux** : $\mathfrak i$ est un idéal si $[\mathfrak g,\mathfrak i\}\subset\mathfrak i$ et $\mathfrak i=\mathfrak i_0\oplus\mathfrak i_1$ (homogène) ; **simple** : pas d'idéal propre.

### Exemples

| Superalgèbre | $\mathfrak g_0$ | $\mathfrak g_1$ | Rôle |
|---|---|---|---|
| $\mathfrak{gl}(m|n)$, $\mathfrak{sl}(m|n)$ ($\mathrm{str}=0$) | $\mathfrak{gl}_m\oplus\mathfrak{gl}_n$ | $m n$ paires | modèle de base |
| $\mathfrak{osp}(M|2n)$ | $\mathfrak{so}(M)\oplus\mathfrak{sp}(2n)$ | $M\times2n$ | sugra AdS ($\mathfrak{osp}(\mathcal N|4)$) |
| super-Poincaré | $\mathfrak{iso}(1,3)\,[\oplus R]$ | $Q_\alpha,\bar Q_{\dot\alpha}$ | SUSY ([[01_Supersymetrie]]) |
| algèbre de Cartan $\langle d,\iota_X,\mathcal L_X\rangle$ | $\mathcal L_X$ | $d,\iota_X$ | calcul extérieur |
| $\mathfrak{psu}(2,2|4)$ | $\mathfrak{su}(2,2)\oplus\mathfrak{su}(4)$ | | AdS$_5$/CFT$_4$ ([[04_Cordes_et_theorie_M]]) |

**Correction de l'exemple $\mathfrak{osp}(1|2)$ des notes importées.** Ce n'est **pas** l'algèbre à 3 générateurs $\{J_0,J_+,J_-\}$ avec $J_0$ pair et $J_\pm$ impairs, $[J_0,J_\pm]=\pm J_\pm$, $\{J_+,J_-\}=2J_0$ : le super-Jacobi avec $x=y=J_+$, $z=J_-$ donne $4[J_+,J_0]=-4J_+\ne0$ ; elle ne ferme pas. $\mathfrak{osp}(1|2)$ est de dimension $(3|2)$ : partie paire $\mathfrak{sl}_2=\langle H,E,F\rangle$ et deux générateurs impairs $Q_\pm$ :
$$[H,Q_\pm]=\pm Q_\pm,\quad[E,Q_-]=Q_+,\quad[F,Q_+]=Q_-,\quad\{Q_+,Q_+\}=-2E,\ \ \{Q_-,Q_-\}=2F,\ \ \{Q_+,Q_-\}=H$$
(avec $[H,E]=2E$, $[H,F]=-2F$, $[E,F]=H$). *Vérification* : Jacobi $(Q_+,Q_+,Q_-)$ : $2[Q_+,\{Q_+,Q_-\}]+[Q_-,\{Q_+,Q_+\}]=-2Q_+-2\,[Q_-,E]$ et $[Q_-,E]=-[E,Q_-]=-Q_+$, d'où $-2Q_++2Q_+=0$ ✓. (Les signes sont ceux de la convention choisie.) Son $\mathfrak g_1$ est la représentation $\mathbf2$ de $\mathfrak{sl}_2$ ; c'est la plus petite superalgèbre de Lie simple classique ; elle contient $\mathfrak{sl}_2$ comme racine carrée : « $Q^2\sim$ générateur ».

## 5. Cartan, calcul extérieur = superalgèbre de Lie

Sur $\Omega^\bullet(M)$ (voir [[02_Formes_differentielles_calcul_exterieur]]) la famille $\{d\}\cup\{\iota_X\}\cup\{\mathcal L_X\}$ est stable par super-crochets (commutateur gradué d'opérateurs) :
$$[d,d\}=2d^2=0,\ \ [d,\iota_X\}=\mathcal L_X,\ \ [\iota_X,\iota_Y\}=0,\ \ [\mathcal L_X,\iota_Y]=\iota_{[X,Y]},\ \ [\mathcal L_X,d]=0,\ \ [\mathcal L_X,\mathcal L_Y]=\mathcal L_{[X,Y]} .$$
C'est la superalgèbre de Lie $\mathfrak{X}(M)\ltimes\Pi\mathfrak X(M)\oplus\langle d\rangle$ ($\Pi$ = changement de parité) : **$d$ joue le rôle d'un générateur supersymétrique** : $d^2=0$ et $\{d,\iota_X\}=\mathcal L_X$ est l'analogue de $\{Q,\bar Q\}=2P$ (c'est la SUSY-QM de Witten, [[01_Supersymetrie]]).
**Dérivée extérieure covariante.** Pour $\Omega^\bullet(M,\mathfrak g)$ avec connexion $A$ : $D=d+[A,\cdot\,]$ (avec signes de Koszul), $D^2=[F,\cdot\,]$ ([[04_Connexions]]).
**Algèbre de Lie graduée différentielle** (dgLa) $\Omega^\bullet(M,\mathfrak g)$ : crochet $[\alpha\otimes x,\beta\otimes y]=\alpha\wedge\beta\otimes[x,y]$ ; équation de Maurer–Cartan $dA+\tfrac12[A,A]=F$ ; équation de courbure nulle ⇔ $A$ est un élément de Maurer–Cartan.

## 6. Super-trace, Berezinien, supergroupes

$\mathrm{str}\begin{pmatrix}A&B\\C&D\end{pmatrix}=\operatorname{tr}A-\operatorname{tr}D$ (invariante : $\mathrm{str}[x,y\}=0$) ; $\mathrm{Ber}=\det(A-BD^{-1}C)/\det D$ ; $\mathfrak{sl}(m|n)=\ker\mathrm{str}$. Le **supergroupe** associé a pour faisceau de fonctions $\mathcal O(G)\otimes\Lambda(\mathfrak g_1^\ast)$ ; les **supervariétés** ont pour coordonnées $(x^\mu|\theta^\alpha)$ ([[03_Fibres]], [[01_Supersymetrie]]).
