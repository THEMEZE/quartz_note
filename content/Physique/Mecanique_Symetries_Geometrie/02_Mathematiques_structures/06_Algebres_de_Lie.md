---
title: Algèbres de Lie
tags:
  - Mathematiques
  - Algebres
lang: fr
---

> Retour : [[00_Index]] · [[07_Groupes_de_Lie]] · [[08_Algebres_graduees_ideaux_superalgebres]] · [[09_Algebres_de_Clifford_spineurs]]

# Algèbres de Lie

## 1. Définitions

Une **algèbre de Lie** sur $\mathbb K$ est un $\mathbb K$-espace vectoriel $\mathfrak g$ muni d'un crochet bilinéaire $[\cdot,\cdot]\colon\mathfrak g\times\mathfrak g\to\mathfrak g$ **antisymétrique** ($[x,y]=-[y,x]$, donc $[x,x]=0$) et vérifiant **Jacobi** : $[x,[y,z]]+[y,[z,x]]+[z,[x,y]]=0$. Constantes de structure : $[T_a,T_b]=f_{ab}{}^cT_c$.
Exemples : $\mathfrak{gl}(n)$ ($[A,B]=AB-BA$) ; $\mathfrak{so}(n)=\{A^{\mathsf T}=-A\}$ ; $\mathfrak{su}(n)$ ; $\mathfrak{sl}(n)$ ; $\mathfrak X(M)$ (champs, [[01_Varietes_differentielles]]) ; $(C^\infty(T^\ast Q),\{\,,\})$ (Poisson) ; $\mathfrak{e}(n)=\mathfrak{so}(n)\ltimes\mathbb R^n$ ([[05_Lagrange_Hamilton_Noether]]) ; Heisenberg $[x,p]=c$.
**Représentation adjointe** : $\mathrm{ad}_x(y)=[x,y]$ ; **Jacobi ⇔ $\mathrm{ad}_x$ est une dérivation** : $\mathrm{ad}_x[y,z]=[\mathrm{ad}_xy,z]+[y,\mathrm{ad}_xz]$ et $\mathrm{ad}_{[x,y]}=[\mathrm{ad}_x,\mathrm{ad}_y]$.

## 2. Idéaux, quotient, extensions

Un **idéal** $\mathfrak i\subset\mathfrak g$ : sous-espace avec $[\mathfrak g,\mathfrak i]\subset\mathfrak i$ (toujours bilatère par antisymétrie) ; $\mathfrak g/\mathfrak i$ est une algèbre de Lie ; noyau d'un morphisme = idéal ([[08_Algebres_graduees_ideaux_superalgebres]]).
- **Centre** $\mathfrak z=\{x:[x,\mathfrak g]=0\}$ ; **dérivée** $[\mathfrak g,\mathfrak g]$ ; série dérivée $\mathfrak g^{(k+1)}=[\mathfrak g^{(k)},\mathfrak g^{(k)}]$ ; série centrale descendante $\mathfrak g^k=[\mathfrak g,\mathfrak g^{k-1}]$.
- **Résoluble** : $\mathfrak g^{(k)}=0$ pour un $k$ ; **nilpotente** : $\mathfrak g^k=0$ ; **simple** : non abélienne sans idéal propre ; **semi-simple** : somme directe d'algèbres simples (⇔ radical résoluble nul).
- **Somme semi-directe** $\mathfrak h\ltimes_\rho\mathfrak n$ : $[(h,n),(h',n')]=([h,h'],\rho(h)n'-\rho(h')n+[n,n'])$ ; ex. $\mathfrak{iso}(n)=\mathfrak{so}(n)\ltimes\mathbb R^n$, Poincaré $\mathfrak{so}(1,n)\ltimes\mathbb R^{1,n}$ : $[P,P]=0$.
- **Extension centrale** par $\mathbb R$ : $0\to\mathbb R\to\hat{\mathfrak g}\to\mathfrak g\to0$, classée par $H^2(\mathfrak g,\mathbb R)$ ([[05_Cohomologie]]).
- **Théorème de Levi** : $\mathfrak g=\mathfrak s\ltimes\mathfrak r$ ($\mathfrak s$ semi-simple, $\mathfrak r$ radical).
- **Théorème de Lie** (résoluble complexe) : représentation triangularisable ; **Engel** : nilpotente ⇔ $\mathrm{ad}_x$ nilpotent $\forall x$.

## 3. Forme de Killing, critères de Cartan

$B(x,y)\doteq\operatorname{tr}(\mathrm{ad}_x\mathrm{ad}_y)$ : symétrique, **invariante** ($B([z,x],y)+B(x,[z,y])=0$). **Cartan** : $\mathfrak g$ semi-simple ⇔ $B$ non dégénérée ; $\mathfrak g$ compacte semi-simple ⇔ $B$ définie négative. Alors $B$ sert de métrique bi-invariante sur $G$, et d'action de Yang–Mills $\langle F,F\rangle$ ([[04_Connexions]]).

## 4. Racines, classification

Pour $\mathfrak g$ semi-simple complexe, une sous-algèbre de Cartan $\mathfrak h$ (maximale abélienne ad-diagonalisable, $\dim=\mathrm{rang}$) donne $\mathfrak g=\mathfrak h\oplus\bigoplus_{\alpha\in\Phi}\mathfrak g_\alpha$ (**racines** $\alpha\in\mathfrak h^\ast$), $[H,E_\alpha]=\alpha(H)E_\alpha$, $[E_\alpha,E_{-\alpha}]=H_\alpha$ : chaque racine engendre un $\mathfrak{sl}_2$. Les systèmes de racines sont classés par les **diagrammes de Dynkin** :

| Type | Algèbre compacte | dim |
|---|---|---|
| $A_n$ | $\mathfrak{su}(n+1)$ | $n(n+2)$ |
| $B_n$ | $\mathfrak{so}(2n+1)$ | $n(2n+1)$ |
| $C_n$ | $\mathfrak{sp}(n)$ | $n(2n+1)$ |
| $D_n$ | $\mathfrak{so}(2n)$ | $n(2n-1)$ |
| $G_2,F_4,E_6,E_7,E_8$ | exceptionnelles | $14,52,78,133,248$ |

Isomorphismes en bas rang : $\mathfrak{so}(3)\simeq\mathfrak{su}(2)$, $\mathfrak{so}(4)\simeq\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ (clé de Kepler, [[06_Kepler_Runge_Lenz_SO_n+1]]), $\mathfrak{so}(5)\simeq\mathfrak{sp}(2)$, $\mathfrak{so}(6)\simeq\mathfrak{su}(4)$, $\mathfrak{so}(1,3)_{\mathbb C}\simeq\mathfrak{sl}_2\oplus\mathfrak{sl}_2$. Physique : $E_8\times E_8$ et $SO(32)$ en théorie des cordes ([[04_Cordes_et_theorie_M]]), $E_{7(7)}$ en sugra $\mathcal N=8$ ([[02_Supergravite_resume]]).

## 5. Algèbre enveloppante, Casimir

$U(\mathfrak g)=T(\mathfrak g)/\langle x\otimes y-y\otimes x-[x,y]\rangle$ ; **PBW** : base ordonnée de monômes $T_{a_1}^{n_1}\cdots T_{a_k}^{n_k}$. Les représentations de $\mathfrak g$ = modules sur $U(\mathfrak g)$. **Casimir** $C=B^{ab}T_aT_b\in Z(U\mathfrak g)$ : scalaire sur chaque irrep (spin $j(j+1)$ pour $\mathfrak{su}(2)$, masse² et $W^2$ pour Poincaré, [[02_Relativite_restreinte_Poincare]]).
**Poids** : $\mathfrak{su}(2)$ : irreps de dimension $2j+1$, $H|m\rangle=2m|m\rangle$, $J_\pm$ ; règle de Clebsch–Gordan $j_1\otimes j_2=\bigoplus_{|j_1-j_2|}^{j_1+j_2}j$.

## 6. Dualité, structures de Lie–Poisson

Le dual $\mathfrak g^\ast$ porte le **crochet de Lie–Poisson** $\{f,g\}(\mu)=\langle\mu,[df,dg]\rangle$ ; ses feuilles symplectiques sont les **orbites coadjointes** (Kirillov–Kostant–Souriau, [[07_Groupes_de_Lie]]). Les **torseurs de type moment** sont des éléments de $\mathfrak e(n)^\ast$ ([[02_Torseurs_Varignon_generalise]]).
