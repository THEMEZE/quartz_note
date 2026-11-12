---
title: 2. Nombres premiers
tags:
  - algèbre
  - arithmétique
  - groupes
  - cours
---
[[Mathématique/Algèbre/I - Arithmétique, Groupes et Anneaux/A. Arithmétique sur les entiers/index|🏠 A. Arithmétique sur les entiers]] [[Mathématique/Algèbre/I - Arithmétique, Groupes et Anneaux/A. Arithmétique sur les entiers/1. Divisibilité - pgcd, ppcm/index| ⬅️ 1. Divisibilité - pgcd, ppcm]] [[Mathématique/Algèbre/I - Arithmétique, Groupes et Anneaux/A. Arithmétique sur les entiers/3. Exercices corrigés/index| ➡️ 3. Exercices corrigés]] 

> [!note] <span style="font-variant: small-caps;">Définition 6 : nombre premier</span>
> On dit qu'un entier naturel $p\geq2$ est un *nombre premier* si ses seuls diviseurs sont $p,-p,1$ et $-1$.

> [!quote] <span style="font-variant: small-caps;">Remarque 4</span>
> Tout entier $n$, $|n|\geq2$, est divisible par un nombre premier.
>
> > [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> > L'ensemble des diviseurs strictement supérieurs à $1$ de $|n|$ est non vide (il contient $|n|$). Son plus petit élément $p$ est premier : un diviseur $d$ de $p$ avec $1<d<p$ diviserait aussi $n$ et contredirait la minimalité de $p$. $\square$

> [!info] <span style="font-variant: small-caps;">Théorème 3 (Théorème fondamental de l'arithmétique)</span>
> Tout entier naturel $n\geq2$ s'écrit de manière **unique**, à l'ordre près, sous la forme
> $$n=p_1^{\alpha_1}\cdots p_k^{\alpha_k}\tag{$\ast$}$$
> où les $p_i$ sont des nombres premiers distincts et les $\alpha_i$ des entiers naturels non nuls. La relation $(\ast)$ s'appelle la *décomposition de $n$ en facteurs premiers*.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> **Existence** (récurrence forte). Si $n$ est premier, c'est fini. Sinon $n=ab$ avec $1<a,b<n$, et on décompose $a$ et $b$ par hypothèse de récurrence ; en regroupant, on obtient une décomposition de $n$.
>
> **Unicité.** Supposons $p_1\cdots p_r=q_1\cdots q_s$ (premiers, répétés selon leur multiplicité). Alors $p_1$ divise $q_1\cdots q_s$ donc, d'après la proposition 7, $p_1$ divise un $q_j$ ; comme $q_j$ est premier, $p_1=q_j$. On simplifie et on recommence : par récurrence sur $r$, les deux listes coïncident à l'ordre près. $\square$

> [!quote]- <span style="font-variant: small-caps;">Conséquence : pgcd et ppcm par les décompositions</span>
> Si $n=p_1^{\alpha_1}\cdots p_k^{\alpha_k}$ et $m=p_1^{\beta_1}\cdots p_k^{\beta_k}$, où les $p_i$ sont des nombres premiers distincts et les $\alpha_i,\beta_i\in\mathbb{N}$, alors
> $$\operatorname{pgcd}(n,m)=p_1^{\gamma_1}\cdots p_k^{\gamma_k},\qquad\operatorname{ppcm}(n,m)=p_1^{\delta_1}\cdots p_k^{\delta_k},$$
> avec $\gamma_i=\inf(\alpha_i,\beta_i)$ et $\delta_i=\sup(\alpha_i,\beta_i)$.

> [!info] <span style="font-variant: small-caps;">Proposition 6</span>
> Si un nombre premier $p$ ne divise pas un entier $a$, alors $p$ et $a$ sont premiers entre eux.
>
> > [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> > $p\wedge a$ divise $p$, donc vaut $1$ ou $p$. Il ne peut valoir $p$ car $p\nmid a$. Donc $p\wedge a=1$. $\square$

> [!info] <span style="font-variant: small-caps;">Proposition 7 (Lemme d'Euclide)</span>
> Si un nombre premier divise un produit d'entiers $a_1\cdots a_n$, il divise au moins l'un des facteurs $a_i$ de ce produit.
>
> > [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> > Récurrence sur $n$. Pour $n=2$ : si $p\mid ab$ et $p\nmid a$, alors $p\wedge a=1$ (prop. 6) et Gauss donne $p\mid b$. Pour l'hérédité, $p\mid(a_1\cdots a_{n-1})\,a_n$ : soit $p\mid a_n$, soit $p\mid a_1\cdots a_{n-1}$ et on applique l'hypothèse. $\square$

> [!info] <span style="font-variant: small-caps;">Proposition 8</span>
> L'ensemble des nombres premiers est infini.
>
> > [!tip]- <span style="font-variant: small-caps;">Démonstration (Euclide)</span>
> > Raisonnons par l'absurde et supposons qu'il y ait un nombre fini de nombres premiers. Soit $N$ le plus grand d'entre eux et posons $M=N!+1\geq 2$. Soit $p$ un nombre premier divisant $M$ (remarque 4). Comme $p\leq N$, on a $p\mid N!$, donc $p\mid M-N!=1$, ce qui est absurde. $\square$

> [!info] <span style="font-variant: small-caps;">Proposition 9</span>
> Soit $p$ un nombre premier et $k$ un entier, $1\leq k\leq p-1$. Alors $p\mid\binom{p}{k}$.
>
> > [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> > On a $k\binom{p}{k}=p\binom{p-1}{k-1}$, donc $p\mid k\binom{p}{k}$. Comme $1\leq k<p$, $p\nmid k$ donc $p\wedge k=1$. Gauss donne $p\mid\binom{p}{k}$. $\square$

> [!info] <span style="font-variant: small-caps;">Proposition 10</span>
> Soit $n\geq2$ un entier. L'anneau $\mathbb{Z}/n\mathbb{Z}$ est un corps si et seulement si $n$ est premier.
>
> > [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> > $(\Leftarrow)$ Si $n$ est premier et $\overline{a}\neq\overline{0}$, alors $n\nmid a$ donc $n\wedge a=1$. Bézout : $au+nv=1$, donc $\overline{a}\,\overline{u}=\overline{1}$ : $\overline{a}$ est inversible.
> >
> > $(\Rightarrow)$ Si $n=ab$ avec $1<a,b<n$, alors $\overline{a}\,\overline{b}=\overline{0}$ avec $\overline{a},\overline{b}\neq\overline{0}$ : $\mathbb{Z}/n\mathbb{Z}$ a des diviseurs de zéro, donc n'est pas intègre, donc pas un corps. $\square$

> [!info] <span style="font-variant: small-caps;">Théorème 4 (Fermat)</span>
> Soit $p\geq 2$ un nombre premier. Alors
> $$\forall a\in\mathbb{Z},\quad a^p\equiv a\pmod p,$$
> et
> $$\forall a\in\mathbb{Z},\; p\nmid a,\quad a^{p-1}\equiv1\pmod p.$$

> [!tip]- <span style="font-variant: small-caps;">Démonstration (Fermat)</span>
> **Première relation.** Par récurrence sur $a\in\mathbb{N}$. Vrai pour $a=0$. D'après la formule du binôme,
> $$(a+1)^p=a^p+\sum_{k=1}^{p-1}\binom{p}{k}a^k+1\equiv a^p+1\pmod p$$
> car $p\mid\binom pk$ pour $1\leq k\leq p-1$ (prop. 9). Avec l'hypothèse $a^p\equiv a$, on obtient $(a+1)^p\equiv a+1$. Pour $a<0$, on se ramène à $\mathbb{N}$ en remplaçant $a$ par $a+mp$ avec $m$ assez grand.
>
> **Seconde relation.** Si $p\nmid a$, alors $p\wedge a=1$ et $p\mid a(a^{p-1}-1)$ ; Gauss donne $p\mid a^{p-1}-1$. $\square$

> [!example]- <span style="font-variant: small-caps;">Application : calcul d'un reste</span>
> *Quel est le reste de la division de $16^{(2^{1000})}$ par $7$ ?*
>
> 1. $16\equiv2\pmod 7$ donc $N=16^{2^{1000}}\equiv2^{2^{1000}}\pmod7$.
> 2. Par Fermat, $2^6\equiv1\pmod 7$ : il faut l'exposant $2^{1000}$ modulo $6$.
> 3. $4^n\equiv4\pmod 6$ pour tout $n\geq1$ (récurrence : $4\times4=16\equiv4$). Or $2^{1000}=4^{500}\equiv4\pmod 6$, donc $2^{1000}=6q+4$.
> 4. $N\equiv2^{6q+4}=(2^6)^q\cdot2^4\equiv1\cdot16\equiv2\pmod7$.
>
> **Le reste est $2$.**

> [!info] <span style="font-variant: small-caps;">Théorème 5 (Wilson)</span>
> Un entier $p\geq2$ est un nombre premier si et seulement si
> $$(p-1)!\equiv-1\pmod p.$$

> [!tip]- <span style="font-variant: small-caps;">Démonstration (Wilson)</span>
> **Condition nécessaire.** Soit $p$ premier. Si $p=2$ ou $p=3$, c'est évident. Pour $p>3$, on cherche les éléments $x$ du groupe multiplicatif $(\mathbb{Z}/p\mathbb{Z})^\ast$ égaux à leur inverse.
> - Ils vérifient $x^2=\overline1$, soit $(x-\overline1)(x+\overline1)=\overline0$. Comme $\mathbb{Z}/p\mathbb{Z}$ est un corps, $x=\overline1$ ou $x=\overline{-1}$.
> - Les autres éléments $\overline2,\overline3,\dots,\overline{p-2}$ se rangent en $\frac{p-3}{2}$ paires $\{x_i,y_i\}$ avec $x_iy_i=\overline1$. D'où
> $$\overline2\cdot\overline3\cdots\overline{p-2}=\prod_{i=1}^{(p-3)/2}x_iy_i=\overline1,\quad\text{donc}\quad(p-1)!\equiv1\cdot(-1)\equiv-1\pmod p.$$
>
> **Condition suffisante.** Supposons $p$ non premier et soit $a$ un diviseur de $p$ avec $1<a<p$. Si $(p-1)!\equiv-1$, alors $a\mid(p-1)!+1$. Mais $a\mid(p-1)!$ puisque $1<a<p$ ; donc $a\mid1$, absurde. $\square$

> [!warning] <span style="font-variant: small-caps;">Attention</span>
> Wilson est un critère de primalité **théorique** : calculer $(p-1)!$ est bien trop coûteux en pratique.

---
