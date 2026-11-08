---
title: Algèbres de Clifford et spineurs
tags:
  - Mathematiques
  - Clifford
  - Spineurs
lang: fr
---

> Retour : [[00_Index]] · [[06_Algebres_de_Lie]] · [[07_Groupes_de_Lie]] · [[03_Fibres]] · [[04_Connexions]]

# Algèbres de Clifford et spineurs

## 1. Algèbre de Clifford

$(V,q)$ espace quadratique réel de dimension $n$ (forme $q$ ou métrique $g$). L'**algèbre de Clifford** est le quotient de l'algèbre tensorielle par $v\otimes v=q(v)$ (convention $v^2=+q(v)$ ; l'autre est $-q(v)$) :
$$\mathrm{Cl}(V,q)=T(V)/\langle v\otimes v-q(v)\mathbb 1\rangle,\qquad vw+wv=2g(v,w)\mathbb 1 .$$
- $\dim\mathrm{Cl}=2^n$ ; **isomorphe à $\Lambda V$ comme espace vectoriel** (base $e_{i_1}\cdots e_{i_k}$, $i_1<\dots<i_k$) : déformation quantique de l'algèbre extérieure ($q=0$ donne $\Lambda V$) ; produit de Clifford $v\cdot\alpha=v\wedge\alpha+\iota_v\alpha$ ([[02_Formes_differentielles_calcul_exterieur]]).
- **$\mathbb Z_2$-graduée** : $\mathrm{Cl}=\mathrm{Cl}^0\oplus\mathrm{Cl}^1$ (produit d'un nombre pair/impair de vecteurs) ; $\mathrm{Cl}^0$ est une sous-algèbre ([[08_Algebres_graduees_ideaux_superalgebres]]).
- **Classification** $\mathrm{Cl}_{p,q}$ ($p$ carrés $+1$, $q$ carrés $-1$) : $\mathrm{Cl}_{0,1}=\mathbb C$, $\mathrm{Cl}_{0,2}=\mathbb H$, $\mathrm{Cl}_{1,0}=\mathbb R\oplus\mathbb R$, $\mathrm{Cl}_{2,0}=M_2(\mathbb R)$, $\mathrm{Cl}_{3,0}=M_2(\mathbb C)$, $\mathrm{Cl}_{1,3}=M_2(\mathbb H)$, $\mathrm{Cl}_{3,1}=M_4(\mathbb R)$. **Périodicité de Bott** : $\mathrm{Cl}_{p+8,q}\simeq\mathrm{Cl}_{p,q}\otimes M_{16}(\mathbb R)$ (période 8 réelle, 2 complexe).
- **Matrices gamma** : $\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}$ ; en $D=2k$ ou $2k+1$ complexes, de taille $2^k$ ($D=4$ : $4\times4$ ; $D=10$ : $32\times32$ ; $D=11$ : $32\times32$). Chiralité $\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$ ($D=4$).

## 2. Groupes Pin et Spin, algèbre $\mathfrak{so}$

Le **groupe de Clifford** $\mathrm{Pin}(V)$ : produits de vecteurs unitaires ; $\mathrm{Spin}(V)=\mathrm{Pin}\cap\mathrm{Cl}^0$. Action **tordue** $x\mapsto\pm uxu^{-1}$ : $\mathrm{Pin}\to O(V)$, $\mathrm{Spin}\to SO(V)$, **revêtement double** ([[07_Groupes_de_Lie]]). Pour $n\ge3$ : $Spin(n)$ simplement connexe.
**Générateurs** : les **bivecteurs** $\Sigma_{ab}=\tfrac14[\gamma_a,\gamma_b]=\tfrac12\gamma_{ab}$ engendrent $\mathfrak{spin}(n)\simeq\mathfrak{so}(n)$ :
$$[\Sigma_{ab},\Sigma_{cd}]=\eta_{bc}\Sigma_{ad}-\eta_{ac}\Sigma_{bd}-\eta_{bd}\Sigma_{ac}+\eta_{ad}\Sigma_{bc},\qquad[\Sigma_{ab},\gamma_c]=\eta_{bc}\gamma_a-\eta_{ac}\gamma_b .$$
**Lien avec la mécanique** : le moment cinétique $L=x\wedge p\in\Lambda^2E\simeq\mathfrak{so}(E)$ et le moment d'un torseur ([[02_Torseurs_Varignon_generalise]]) sont des **bivecteurs** ; le spin quantique est la représentation de $\mathfrak{spin}$ qui les « exponentie » dans $\mathrm{Cl}$ : $\hat L_{ab}=\tfrac1{i\hbar}\ldots+\hbar\Sigma_{ab}$ (moment total $=$ orbital $+$ spin).

## 3. Spineurs

Un **module de spineurs** est une représentation irréductible de $\mathrm{Cl}$ (ou de $Spin$) : $\mathbb C^{2^{\lfloor n/2\rfloor}}$ pour $\mathrm{Cl}_n(\mathbb C)$. Tableaux utiles (dimension de l'espace-temps $D$) :

| $D$ | spineur de Dirac (complexe) | Majorana(–Weyl) réel | Remarque |
|---|---|---|---|
| 4 | 4 | Majorana : 4 réels | $\mathcal N=1$ : 4 supercharges |
| 10 | 32 | Majorana–Weyl : 16 | supercordes |
| 11 | 32 | Majorana : 32 | théorie M, sugra 11D |
| 2, 6, 10 (mod 8) | | Majorana–Weyl possible | conditions de réalité |

**Spineur de Weyl** : $\gamma_5\psi=\pm\psi$ ($(\tfrac12,0)$ ou $(0,\tfrac12)$ de $SL(2,\mathbb C)$) ; **Majorana** : $\psi=\psi^c=C\bar\psi^{\mathsf T}$. **Équation de Dirac** $(i\gamma^\mu\partial_\mu-m)\psi=0$ : racine carrée de Klein–Gordon car $(i\gamma^\mu\partial_\mu)^2=-\Box$ ($\eta=(+---)$) ; $\bar\psi\gamma^\mu\psi$ est un courant conservé ($U(1)$).
**Spin-statistique** : représentations de spin demi-entier ↔ fermions (antisymétrie), d'où l'importance de Grassmann pour la SUSY ([[08_Algebres_graduees_ideaux_superalgebres]]).

## 4. Fibré des spineurs, structure de spin, opérateur de Dirac

Une **structure de spin** sur $(M,g)$ orientée : relèvement $\mathrm{Spin}(M)\to\mathrm{Fr}_{SO}(M)$ d'un $Spin(n)$-fibré principal ; obstruction $w_2(M)\in H^2(M;\mathbb Z_2)$ ([[05_Cohomologie]]) ; ensemble des structures $\simeq H^1(M;\mathbb Z_2)$. Fibré des spineurs $S=\mathrm{Spin}(M)\times_\rho\Delta$ ; connexion induite de Levi-Civita $\nabla_\mu\psi=\partial_\mu\psi+\tfrac14\omega_\mu{}^{ab}\gamma_{ab}\psi$ ([[04_Connexions]]). **Opérateur de Dirac** $\slashed D=\gamma^\mu\nabla_\mu$ ; **Lichnerowicz** $\slashed D^2=\nabla^\ast\nabla+\tfrac R4$ (obstruction aux courbures scalaires positives) ; **Atiyah–Singer** : $\mathrm{ind}\,\slashed D=\int\hat A(M)$.
Les **spineurs de Killing** $\nabla_\mu\epsilon=\tfrac12\gamma_\mu\epsilon$ paramètrent les supersymétries préservées par un fond (sphères, $AdS$, Calabi–Yau : $\nabla\epsilon=0$, holonomie spéciale $SU(3)$, $G_2$ : [[04_Cordes_et_theorie_M]]).

## 5. Triade : Grassmann–Clifford–Lie

| Algèbre | Relation | Rôle |
|---|---|---|
| Grassmann $\Lambda V$ | $\theta^i\theta^j+\theta^j\theta^i=0$ | coordonnées de superespace, formes |
| Clifford $\mathrm{Cl}(V,g)$ | $\gamma^a\gamma^b+\gamma^b\gamma^a=2g^{ab}$ | spineurs, $\mathfrak{spin}$ |
| Weyl–Heisenberg | $[x,p]=i\hbar$ | quantification |
| Lie $\mathfrak g$ | $[T_a,T_b]=f_{ab}{}^cT_c$ | symétries |
| **Super-Poincaré** | $\{Q,\bar Q\}=2\sigma^\mu P_\mu$ | SUSY, « racine carrée » de la translation |
