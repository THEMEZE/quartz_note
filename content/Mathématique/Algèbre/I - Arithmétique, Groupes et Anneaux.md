---
title: I - Arithmétique, Groupes et Anneaux
tags: [algèbre, arithmétique, groupes, cours]
---
---
**Brouillon**

[[Algèbre (brouillon)]] , [[I - Arithmétique, Groupes et Anneaux (brouillon)]]

---


> [!quote] <span style="font-variant: small-caps;">Introduction</span>
> Jusqu'au début du vingtième siècle, l'algèbre désignait essentiellement l'étude de la résolution d'équations algébriques (en témoigne la dénomination de *théorème fondamental de l'algèbre*). Avec la résolution des équations algébriques apparut, de manière plus ou moins confuse, la notion de nombre complexe : on utilisa le symbole $\sqrt{-1}$. Parallèlement, la théorie des congruences se développa.
>
> Ainsi, de nouveaux objets mathématiques entrèrent en scène. Bientôt, les mathématiciens y virent des analogies étroites qu'ils cherchèrent à expliquer : l'algèbre devint progressivement l'étude abstraite des **structures algébriques**, jusqu'à ce que connaît l'étudiant d'aujourd'hui.

> [!abstract]- <span style="font-variant: small-caps;">Légende des encadrés</span>
> | Encadré | Signification |
> |---|---|
> | `[!note]` bleu | **Définition** |
> | `[!info]` | **Théorème / Proposition** |
> | `[!tip]` | **Démonstration** (repliée) |
> | `[!quote]` | **Remarque** |
> | `[!example]` | **Exemple / Application** |
> | `[!warning]` | **Piège à éviter** |
>
> Les démonstrations sont repliées : clique sur la flèche pour les ouvrir.

---

# 1. Arithmétique sur les entiers

Nous supposons acquises les notions de base sur l'ensemble des entiers naturels $\mathbb{N}$ et des entiers relatifs $\mathbb{Z}$, ainsi que les calculs dans l'anneau quotient $\mathbb{Z}/n\mathbb{Z}$. Une étude plus approfondie de ce dernier fait l'objet de la section [[#1.4. Arithmétique modulaire]] de ce chapitre.

## 1.1. Divisibilité - pgcd, ppcm

> [!note] <span style="font-variant: small-caps;">Définition 1 : divisibilité $a \mid b$</span>
> Soient $a$ et $b$ deux entiers relatifs. On dit que $a$ *divise* $b$ (ou que $b$ est un *multiple* de $a$), et on note $a\mid b$, s'il existe un entier $n$ tel que $b=an$. Si $a$ ne divise pas $b$, on note $a\nmid b$.

> [!example]- <span style="font-variant: small-caps;">Propriétés immédiates</span>
> - $1 \mid a$, $a \mid a$ et $a \mid 0$ pour tout $a\in\mathbb{Z}$.
> - Si $a\mid b$ et $b\mid c$, alors $a\mid c$ (transitivité).
> - Si $a \mid b$ et $a \mid c$, alors $a \mid (ub+vc)$ pour tous $u,v\in\mathbb{Z}$.
> - Si $a\mid b$ et $b\neq 0$, alors $|a|\leq|b|$.

> [!info] <span style="font-variant: small-caps;">Proposition 1 (Division euclidienne)</span>
> Soient $a\in \mathbb{Z}$ et $b\in \mathbb{N}^\ast$. Il existe un **unique** couple $(q,r) \in \mathbb{Z}\times \mathbb{N}$ tel que
> $$ a = bq + r, \qquad \text{avec} \qquad 0 \leq r \leq b - 1. $$
> $q$ s'appelle le *quotient*, $r$ le *reste*, de la division euclidienne de $a$ par $b$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration de la proposition 1</span>
> **Existence.** Considérons $E=\{a-kb \mid k\in\mathbb{Z},\; a-kb\geq 0\}\subset \mathbb{N}$.
> 1. $E$ est non vide : pour $k=-|a|$, on a $a+|a|b\geq a+|a|\geq 0$ (car $b\geq 1$).
> 2. Par le principe du bon ordre, $E$ possède un plus petit élément $r=a-qb\geq 0$. Donc $a=bq+r$.
> 3. Montrons $r<b$ par l'absurde. Si $r\geq b$, alors $r-b=a-(q+1)b\geq 0$ appartient à $E$ et $r-b<r$ : contradiction avec la minimalité de $r$.
>
> **Unicité.** Soient $(q,r)$ et $(q',r')$ deux couples convenant.
> 1. $bq+r=bq'+r'$ donc $b(q-q')=r'-r$.
> 2. Comme $0\leq r,r'<b$, on a $-b<r'-r<b$, d'où $|r'-r|<b$.
> 3. Donc $b\,|q-q'|<b$, soit $|q-q'|<1$. Or $|q-q'|\in\mathbb{N}$, donc $q=q'$ puis $r=r'$. $\square$

> [!warning]- <span style="font-variant: small-caps;">Correction apportée</span>
> Dans ton brouillon, le reste était dans $\mathbb{N}^\ast$ : c'est faux, le reste peut valoir $0$ (c'est même le cas quand $b\mid a$). Le bon ensemble est $\mathbb{N}$.

> [!note]- <span style="font-variant: small-caps;">Définition : anneau euclidien (rappel)</span>
> Soit $A$ un anneau commutatif intègre. On dit que $A$ est **euclidien** s'il existe une application $v\colon A\setminus\{0\}\to\mathbb{N}$ (appelée *stathme*) telle que :
> pour tous $a,b\in A$ avec $b\neq 0$, il existe $(q,r)\in A\times A$ vérifiant
> $$a=bq+r \qquad \text{avec} \qquad r=0 \;\; \text{ou} \;\; v(r)<v(b).$$
>
> > [!quote]
> > L'**existence** de la division fait partie de l'axiome de la structure. En général, l'**unicité** du couple $(q,r)$ n'est *pas* garantie (elle l'est dans $\mathbb{Z}$ ou $K[X]$ avec les stathmes usuels).

> [!info] <span style="font-variant: small-caps;">Théorème : tout anneau euclidien est principal</span>
> Tout idéal $I$ d'un anneau euclidien $A$ est de la forme $bA$ pour un certain $b\in A$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> 1. **Cas trivial.** Si $I=\{0\}$, alors $I=0\cdot A$.
> 2. **Choix du générateur.** Supposons $I\neq\{0\}$. L'ensemble $\{v(x)\mid x\in I\setminus\{0\}\}$ est une partie non vide de $\mathbb{N}$ ; elle admet un minimum. Soit $b\in I\setminus\{0\}$ qui l'atteint : $v(b)\leq v(x)$ pour tout $x\in I\setminus\{0\}$.
> 3. **Double inclusion.**
>    - $bA\subset I$ : car $b\in I$ et $I$ est un idéal.
>    - $I\subset bA$ : soit $a\in I$. On écrit $a=bq+r$ avec $r=0$ ou $v(r)<v(b)$. Alors $r=a-bq\in I$. Si $r\neq0$, on aurait $r\in I\setminus\{0\}$ avec $v(r)<v(b)$, ce qui contredit la minimalité de $v(b)$. Donc $r=0$ et $a=bq\in bA$.
>
> Ainsi $I=bA$. $\square$

### 1.1.1. *Classes de congruence modulo $n$*

> [!note] <span style="font-variant: small-caps;">Définition 2 : congruence modulo $n$</span>
> Soit $n\in\mathbb{N}^\ast$. On note $n\mathbb{Z}=\{nk\mid k\in\mathbb{Z}\}$. Si $x$ et $y$ sont deux entiers, on note
> $$x\equiv y \pmod n \iff x-y\in n\mathbb{Z} \iff n\mid x-y,$$
> et on dit que $x$ et $y$ sont *congrus modulo $n$*.

> [!note] <span style="font-variant: small-caps;">Définition 3 : $\mathbb{Z}/n\mathbb{Z}=\{\overline{0},\overline{1},\dots,\overline{n-1}\}$</span>
> Soit $n\in\mathbb{N}^\ast$. L'anneau quotient de $\mathbb{Z}$ par $n\mathbb{Z}$ est noté $\mathbb{Z}/n\mathbb{Z}$. On note $\overline{x}$ (ou $\dot{x}$) la classe d'un entier $x$. Ainsi $\mathbb{Z}/n\mathbb{Z}=\{\overline{0},\overline{1},\dots,\overline{n-1}\}$, et $\overline{x}=\overline{y}\iff x\equiv y\pmod n$.

> [!quote]- <span style="font-variant: small-caps;">Remarque : lien avec la division euclidienne</span>
> D'après la proposition 1, tout entier $x$ s'écrit $x=nq+r$ avec $0\leq r<n$, donc $\overline{x}=\overline{r}$ : **chaque classe a exactement un représentant dans $\llbracket 0,n-1\rrbracket$**. C'est pourquoi $\mathbb{Z}/n\mathbb{Z}$ a exactement $n$ éléments.

### 1.1.2. *Plus Grand Commun Diviseur (PGCD)*

> [!info]- <span style="font-variant: small-caps;">Lemme : les sous-groupes de $\mathbb{Z}$</span>
> Tout sous-groupe $H$ de $(\mathbb{Z},+)$ est de la forme $d\mathbb{Z}$ avec $d\in\mathbb{N}$, et $d$ est unique.
>
> > [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> > Si $H=\{0\}$, alors $d=0$. Sinon $H$ contient un entier strictement positif (si $x\in H$ alors $-x\in H$). Soit $d$ le plus petit élément de $H\cap\mathbb{N}^\ast$.
> > - $d\mathbb{Z}\subset H$ car $H$ est stable par addition et opposé.
> > - Soit $x\in H$ ; on écrit $x=dq+r$ avec $0\leq r<d$. Alors $r=x-dq\in H$, et par minimalité de $d$, $r=0$. Donc $x\in d\mathbb{Z}$.
> >
> > L'unicité vient du fait que $d$ est le plus petit élément strictement positif de $H$. $\square$

> [!note] <span style="font-variant: small-caps;">Définition 4 : PGCD</span>
> - Soient $a_1,\dots,a_n$ des entiers. Il existe un **unique** entier naturel $d$ tel que $a_1\mathbb{Z}+\dots+a_n\mathbb{Z}=d\mathbb{Z}$. Ce $d$ s'appelle le *pgcd* de $a_1,\dots,a_n$ et on note $d=\operatorname{pgcd}(a_1,\dots,a_n)$. C'est le plus grand entier naturel divisant tous les $a_i$.
> - Lorsque $\operatorname{pgcd}(a_1,\dots,a_n)=1$, on dit que les $a_i$ sont *premiers entre eux dans leur ensemble*. Lorsque $\operatorname{pgcd}(a_i,a_j)=1$ dès que $i\neq j$, ils sont *premiers entre eux deux à deux*.

> [!tip]- <span style="font-variant: small-caps;">Justification de la définition 4</span>
> L'ensemble $a_1\mathbb{Z}+\dots+a_n\mathbb{Z}=\{u_1a_1+\dots+u_na_n\mid u_i\in\mathbb{Z}\}$ est un sous-groupe de $\mathbb{Z}$ : d'après le lemme, il vaut $d\mathbb{Z}$ pour un unique $d\in\mathbb{N}$.
> - Chaque $a_i\in d\mathbb{Z}$, donc $d\mid a_i$ : $d$ est un diviseur commun.
> - Si $c$ divise tous les $a_i$, alors $c$ divise toute combinaison $u_1a_1+\dots+u_na_n$, donc $c\mid d$ ; en particulier $c\leq d$ (si $d\neq 0$).
>
> Donc $d$ est bien le plus grand des diviseurs communs, et **les diviseurs communs sont exactement les diviseurs de $d$**. $\square$

> [!quote] <span style="font-variant: small-caps;">Remarque 1</span>
> - Des entiers premiers entre eux deux à deux sont premiers entre eux dans leur ensemble (la réciproque est fausse : $6,10,15$).
> - Les diviseurs communs à une famille d'entiers sont les diviseurs de leur pgcd.
> - Pour tout $a\in\mathbb{Z}$ : $\operatorname{pgcd}(aa_1,\dots,aa_n)=|a|\operatorname{pgcd}(a_1,\dots,a_n)$.
> - Le pgcd de deux entiers $a$ et $b$ se note aussi $a\wedge b$.

> [!info] <span style="font-variant: small-caps;">Théorème 1 (Bézout)</span>
> Des entiers $a_1,\dots,a_n$ sont premiers entre eux dans leur ensemble si et seulement s'il existe des entiers $u_1,\dots,u_n$ tels que
> $$u_1a_1+\dots+u_na_n=1.$$

> [!tip]- <span style="font-variant: small-caps;">Démonstration (Bézout)</span>
> $(\Rightarrow)$ Si $\operatorname{pgcd}(a_1,\dots,a_n)=1$, alors par définition $a_1\mathbb{Z}+\dots+a_n\mathbb{Z}=1\cdot\mathbb{Z}=\mathbb{Z}$. Comme $1\in\mathbb{Z}$, il s'écrit $1=u_1a_1+\dots+u_na_n$.
>
> $(\Leftarrow)$ Si $u_1a_1+\dots+u_na_n=1$, alors tout diviseur commun $c$ des $a_i$ divise $1$, donc $c=\pm1$. Ainsi le pgcd vaut $1$. $\square$

> [!quote] <span style="font-variant: small-caps;">Remarque 2</span>
> Pour deux entiers, Bézout assure l'existence de $(u,v)\in\mathbb{Z}^2$ tel que $au+bv=1$. Il existe un moyen pratique de le calculer : l'**algorithme d'Euclide étendu**.
>
> De façon plus générale, pour $d=a\wedge b$, il existe $(u,v)$ avec $au+bv=d$.

> [!example]- <span style="font-variant: small-caps;">Exemple : algorithme d'Euclide étendu</span>
> Trouver $u,v$ tels que $47u+111v=1$.
>
> *Descente* (divisions euclidiennes successives) :
> $$\begin{aligned} 111&=47\times2+17\\ 47&=17\times2+13\\ 17&=13\times1+4\\ 13&=4\times3+1\end{aligned}$$
> Le dernier reste non nul est $1$, donc $47\wedge111=1$.
>
> *Remontée* :
> $$\begin{aligned}1&=13-4\times3=13-(17-13)\times3=4\times13-3\times17\\&=4(47-2\times17)-3\times17=4\times47-11\times17\\&=4\times47-11(111-2\times47)=26\times47-11\times111.\end{aligned}$$
> Donc $(u,v)=(26,-11)$. *Vérification :* $47\times26=1222$ et $111\times11=1221$. ✔

> [!info] <span style="font-variant: small-caps;">Théorème 2 (Gauss)</span>
> Soient $a,b,c$ trois entiers. Si $a$ divise le produit $bc$ et si $a$ et $b$ sont premiers entre eux, alors $a$ divise $c$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration (Gauss)</span>
> Comme $a\wedge b=1$, Bézout donne $u,v\in\mathbb{Z}$ tels que $au+bv=1$. On multiplie par $c$ :
> $$c=acu+bcv.$$
> Or $a\mid acu$ trivialement, et $a\mid bc$ par hypothèse donc $a\mid bcv$. Donc $a$ divise la somme, c'est-à-dire $a\mid c$. $\square$

> [!info] <span style="font-variant: small-caps;">Proposition 2</span>
> Si un entier $a$ est premier avec chacun des entiers $b_1,\dots,b_n$, alors $a$ est premier avec le produit $b_1\cdots b_n$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> Par récurrence sur $n$ ; le cas $n=1$ est évident. Traitons $n=2$ (l'hérédité est identique).
> Si $a\wedge b_1=1$ et $a\wedge b_2=1$, Bézout donne $au+b_1v=1$ et $au'+b_2v'=1$. En multipliant :
> $$1=(au+b_1v)(au'+b_2v')=a\,(\underbrace{uau'+ub_2v'+b_1vu'}_{\in\mathbb{Z}})+b_1b_2\,vv'.$$
> D'après Bézout, $a\wedge(b_1b_2)=1$. Pour l'hérédité, on applique ceci à $b_1\cdots b_{n-1}$ et $b_n$. $\square$

> [!info] <span style="font-variant: small-caps;">Proposition 3</span>
> Soient $a_1,\dots,a_n$ des entiers premiers entre eux **deux à deux** et $b$ un entier. Le produit $a_1\cdots a_n$ divise $b$ si et seulement si, pour tout $i$, $a_i$ divise $b$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> $(\Rightarrow)$ évident.
>
> $(\Leftarrow)$ Récurrence sur $n$ ($n=1$ trivial). Supposons $a_1\cdots a_{n-1}\mid b$ : on écrit $b=a_1\cdots a_{n-1}\,c$.
> Comme $a_n\mid b$ et que $a_n$ est premier avec chaque $a_i$ ($i<n$), il l'est avec leur produit (proposition 2). Gauss donne alors $a_n\mid c$. Donc $a_1\cdots a_n\mid b$. $\square$

### 1.1.3. *Plus Petit Commun Multiple (PPCM)*

> [!note] <span style="font-variant: small-caps;">Définition 5 : PPCM</span>
> Soient $a_1,\dots,a_n$ des entiers non nuls. Il existe un unique entier naturel $d$ tel que
> $$a_1\mathbb{Z}\cap\dots\cap a_n\mathbb{Z}=d\mathbb{Z}.$$
> Ce $d$ s'appelle le *ppcm* de $a_1,\dots,a_n$, noté $d=\operatorname{ppcm}(a_1,\dots,a_n)$. C'est le plus petit entier naturel non nul multiple de tous les $a_i$.

> [!tip]- <span style="font-variant: small-caps;">Justification</span>
> Une intersection de sous-groupes de $\mathbb{Z}$ est un sous-groupe de $\mathbb{Z}$, donc de la forme $d\mathbb{Z}$. Il est non réduit à $\{0\}$ car il contient $|a_1\cdots a_n|\neq 0$. Ses éléments sont les multiples communs, et $d$ est le plus petit strictement positif. $\square$

> [!quote] <span style="font-variant: small-caps;">Remarque 3</span>
> - Les multiples communs à une famille d'entiers sont les multiples de leur ppcm.
> - $\forall a\in\mathbb{Z}^\ast,\;\operatorname{ppcm}(aa_1,\dots,aa_n)=|a|\operatorname{ppcm}(a_1,\dots,a_n)$.
> - Le ppcm de deux entiers $a$ et $b$ se note aussi $a\vee b$.

> [!info] <span style="font-variant: small-caps;">Proposition 4</span>
> Soient $a_1,\dots,a_n$ des entiers premiers entre eux deux à deux. Alors $\operatorname{ppcm}(a_1,\dots,a_n)=|a_1\cdots a_n|$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> Un entier $M$ est multiple commun des $a_i$ ssi chaque $a_i\mid M$, ssi (proposition 3) $a_1\cdots a_n\mid M$. Le plus petit multiple positif est donc $|a_1\cdots a_n|$. $\square$

> [!info] <span style="font-variant: small-caps;">Proposition 5</span>
> Pour deux entiers $a$ et $b$, on a $\operatorname{pgcd}(a,b)\times\operatorname{ppcm}(a,b)=|ab|$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> On suppose $a,b\neq0$. Soit $d=a\wedge b$ ; on écrit $a=da'$, $b=db'$ avec $a'\wedge b'=1$.
> - $m=da'b'$ est un multiple commun : $m=a\,b'=b\,a'$.
> - Soit $M$ un multiple commun : $M=ak=bl$, donc $da'k=db'l$, soit $a'k=b'l$. Ainsi $b'\mid a'k$ et, comme $b'\wedge a'=1$, Gauss donne $b'\mid k$. Donc $ab'\mid ak=M$, c'est-à-dire $m\mid M$.
>
> Donc $m=\operatorname{ppcm}(a,b)$ et $d\cdot m=d^2a'b'=|ab|$. $\square$

---

## 1.2. Nombres premiers

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

## 1.3. Exercices corrigés

---

> [!abstract]- <span style="font-variant: small-caps;">Comment utiliser ce fichier</span>
>
> - `[!question]` : énoncé, avec difficulté ★ à ★★★ (★★★ = niveau agrégation)
> - `[!todo]-` 💡 **Indice** : à n'ouvrir que si tu bloques
> - `[!success]-` **Solution** : à ouvrir en dernier
>
> Les exercices **14 à 22** sont des compléments plus difficiles. Certains utilisent la théorie des groupes (notion d'ordre, Lagrange) : ils sont signalés par 🔗.

---
### Exercices du livre


> [!question]- <span style="font-variant: small-caps;">Exercice 1 : triplets</span>
> Déterminer les triplets $(a,b,c)\in(\mathbb{N}^\ast)^3$ tels que (i) $\operatorname{ppcm}(a,b)=42$, (ii) $\operatorname{pgcd}(a,c)=3$, (iii) $a+b+c=29$.
>
> > [!success]- <span style="font-variant: small-caps;">Solution</span>
> > D'après (ii), $3\mid a$ et $3\mid c$, donc $3\mid(a+c)$. Comme $b=29-(a+c)$, $b$ n'est pas multiple de $3$, et $3\wedge b=1$. Par (i), $b\mid42=3\times14$, et par le théorème de Gauss, $b\mid14$. Donc $b\in\{1,2,7,14\}$. Mais $29-b=a+c$ est divisible par $3$, ce qui restreint $b$ à $2$ ou $14$.
> > - Si $b=2$, $a\in\{21,42\}$ d'après (i) ; avec $a\leq29$, $a=21$ puis $c=6$.
> > - Si $b=14$, $a\in\{3,6,21,42\}$ d'après (i) ; (iii) donne $a\leq15$, d'où $a\in\{3,6\}$ : $a=3,c=12$ ou $a=6,c=9$.
> >
> > Triplets : $(21,2,6)$, $(3,14,12)$, $(6,14,9)$. On vérifie qu'ils conviennent.

> [!question]- <span style="font-variant: small-caps;">Exercice 2 : unicité dans Bézout</span>
> Soient $a,b\geq2$ premiers entre eux. Montrer que $\exists!(u_0,v_0)\in\mathbb{N}^2$ avec $u_0a-v_0b=1$, $u_0<b$ et $v_0<a$, puis décrire tous les couples $(u,v)\in\mathbb{Z}^2$ solutions de $ua-vb=1$.
>
> > [!success]- <span style="font-variant: small-caps;">Solution</span>
> > **Existence.** Bézout donne $(u_1,v_1)$ avec $u_1a-v_1b=1$. On divise : $u_1=bq+u_0$ avec $0\leq u_0<b$. Alors $(bq+u_0)a-v_1b=1$ donne $u_0a-v_0b=1$ avec $v_0=v_1-aq$. Ainsi $-1\leq v_0b=u_0a-1<u_0a<ba$, et en divisant par $b\geq2$, on a $0\leq v_0<a$.
> >
> > **Description de toutes les solutions.** Si $ua-vb=1$, en retranchant : $(u-u_0)a=(v-v_0)b$. Donc $a\mid(v-v_0)b$ ; Gauss donne $a\mid v-v_0$ : $v=v_0+ka$, puis $u=u_0+kb$ ($k\in\mathbb{Z}$). Réciproquement ces couples conviennent. Le couple $(u_0,v_0)$ est le seul dans $[0,b[\times[0,a[$ (il correspond à $k=0$).

> [!question]- <span style="font-variant: small-caps;">Exercice 3 : divisibilité</span>
> a) Montrer que pour tout $n\in\mathbb{N}$, $5\mid2^{3n+5}+3^{n+1}$.
> b) Montrer que pour tout $n\in\mathbb{Z}$, $30\mid n^5-n$.
>
> > [!success]- <span style="font-variant: small-caps;">Solution</span>
> > **a)** $2^5\equiv2$ et $2^3\equiv8\equiv3\pmod5$ donc $2^{3n+5}\equiv2\cdot3^n$. Alors $2^{3n+5}+3^{n+1}\equiv2\cdot3^n+3\cdot3^n=5\cdot3^n\equiv0\pmod5$.
> >
> > **b)** Par Fermat, $n^5\equiv n\pmod5$. De plus $n^3\equiv n\pmod 3$ (Fermat avec $n^3$), donc $n^5=n^3\cdot n^2\equiv n\cdot n^2=n^3\equiv n\pmod3$. Enfin $n$ et $n^5$ ont même parité, donc $2\mid n^5-n$. Comme $2,3,5$ sont premiers entre eux deux à deux, $30=2\cdot3\cdot5$ divise $n^5-n$ (prop. 3).

> [!question]- <span style="font-variant: small-caps;">Exercice 4 : nombres de Mersenne et de Fermat</span>
> a) Si $a^n-1$ est premier ($a,n\geq2$), montrer $a=2$ et $n$ premier.
> b) Si $2^n+1$ est premier, montrer que $n$ est une puissance de $2$.
>
> > [!success]- <span style="font-variant: small-caps;">Solution</span>
> > **a)** $x^n-1=(x-1)(x^{n-1}+\dots+x+1)$ montre que $(a-1)\mid(a^n-1)$. Comme $a^n-1$ est premier, $a-1=1$, donc $a=2$. Si $n=pq$, alors $2^n-1=(2^q)^p-1$ est divisible par $2^q-1$ ; la primalité impose $q=1$ ou $q=n$. Donc $n$ est premier.
> >
> > **b)** Pour $n$ impair, $x^n+1=(x+1)(x^{n-1}-\dots-x+1)$ donc $(x+1)\mid(x^n+1)$. Si $n$ n'est pas une puissance de $2$, il a un facteur impair $p>1$ : $n=pq$ et $2^n+1=(2^q)^p+1$ est divisible par $2^q+1$, donc non premier.

> [!example]- <span style="font-variant: small-caps;">Pour aller plus loin</span>
> - Les nombres de **Mersenne** $M_p=2^p-1$ : $M_{11}=2047=23\times89$ n'est pas premier (la réciproque de a) est fausse).
> - Les nombres de **Fermat** $F_n=2^{2^n}+1$ : premiers pour $0\leq n\leq4$, mais $F_5=641\times6700417$ (Euler).
> - Les $F_n$ sont premiers entre eux deux à deux, ce qui donne une autre preuve de l'infinité des nombres premiers.

> [!question]- <span style="font-variant: small-caps;">Exercice 5 ★★ : somme des chiffres de $4444^{4444}$</span>
> Soit $A$ la somme des chiffres de $4444^{4444}$ (écrit en base 10), $B$ la somme des chiffres de $A$. Que vaut $C$, la somme des chiffres de $B$ ?
>
> > [!todo]- 💡 Indice
> > Tout entier est congru à la somme de ses chiffres modulo $9$. Puis majorer $C$.
>
> > [!success]- Solution
> > **Lemme.** $N\equiv$ (somme de ses chiffres) $\pmod 9$. En effet, $N=\sum a_i10^i$ et $10\equiv1\pmod 9$ donne $10^i\equiv1$, donc $N\equiv\sum a_i$.
> >
> > **Calcul modulo 9.** Par le lemme, $C\equiv B\equiv A\equiv4444^{4444}\pmod 9$. Or $4444\equiv4+4+4+4=16\equiv7\equiv-2\pmod 9$, donc $4444^3\equiv(-2)^3=-8\equiv1$. Comme $4444=3\times1481+1$,
> > $$4444^{4444}=(4444^3)^{1481}\cdot4444\equiv1\cdot(-2)\equiv7\pmod 9.$$
> > Donc $C\equiv7\pmod 9$.
> >
> > **Majoration.** $4444^{4444}<10000^{4444}<10^{20000}$ a au plus $20000$ chiffres, donc $A\leq9\times20000=180000$ a au plus $6$ chiffres, donc $B\leq6\times9=54$, donc $C\leq4+9=13$ (le plus grand des cas : $49$) $\leq14$.
> >
> > Les deux conditions $C\equiv7\pmod 9$ et $0<C\leq14$ donnent $\boxed{C=7}$.

> [!question]- <span style="font-variant: small-caps;">Exercice 6 ★ : racines rationnelles d'un polynôme unitaire</span>
> Soit $P=X^n+c_1X^{n-1}+\dots+c_{n-1}X+c_n$ à coefficients entiers. Montrer qu'une racine rationnelle de $P$ est nécessairement entière. En déduire que $\sqrt[n]{N}$ est entier ou irrationnel.
>
> > [!success]- Solution
> > Soit $x=a/b$ une racine rationnelle, $a\in\mathbb{Z}$, $b\in\mathbb{N}^\ast$, $a\wedge b=1$. Alors
> > $$0=b^nP\left(\tfrac ab\right)=a^n+c_1a^{n-1}b+\dots+c_nb^n,\quad\text{donc}\quad a^n=-b\,(c_1a^{n-1}+\dots+c_nb^{n-1}).$$
> > Donc $b\mid a^n$. Comme $a\wedge b=1$, $a^n\wedge b=1$ (prop. 2), donc $b=1$ : $x\in\mathbb{Z}$.
> >
> > **Conséquence.** Une racine $n$-ième de $N\in\mathbb{N}$ est racine de $X^n-N$ : si elle est rationnelle, elle est entière.

> [!question]- <span style="font-variant: small-caps;">Exercice 7 ★★ : primes de la forme $6k-1$</span>
> Montrer qu'il y a une infinité de nombres premiers de la forme $6k-1$, $k\in\mathbb{N}^\ast$.
>
> > [!todo]- 💡 Indice
> > Imiter Euclide avec $M=6\,N!-1$. Que valent les restes possibles d'un nombre premier $>3$ modulo $6$ ?
>
> > [!success]- Solution
> > Par l'absurde, soit $N$ le plus grand premier de la forme $6k-1$, et $M=6\,N!-1$. Alors $M$ est impair et $M\equiv-1\pmod 3$, donc $2\nmid M$ et $3\nmid M$.
> >
> > Un nombre premier $p\notin\{2,3\}$ est $\equiv1$ ou $5\pmod 6$ (il n'est divisible ni par $2$ ni par $3$). Si tous les facteurs premiers de $M$ étaient $\equiv1\pmod 6$, on aurait $M\equiv1\pmod 6$ ; or $M\equiv-1\pmod 6$ par construction : **absurde**. Donc $M$ a un facteur premier $p\equiv-1\pmod 6$, de la forme $6k-1$, avec $p\leq N$ (maximalité de $N$). Alors $p\mid N!$, donc $p\mid6N!-M=1$ : contradiction.
>
> > [!quote]- Remarque
> > Même méthode pour $4k-1$. Le théorème de **Dirichlet** (1837) généralise : pour $a\wedge b=1$, il y a une infinité de premiers de la forme $ak+b$. Sa preuve complète est analytique (séries $L$).

> [!question]- <span style="font-variant: small-caps;">Exercice 8 ★★ : pas de polynôme qui ne prenne que des valeurs premières</span>
> Montrer qu'il n'existe pas de polynôme $P$ non constant à coefficients entiers tel que $P(n)$ soit premier pour tout entier $n$ supérieur à un certain rang $N$.
>
> > [!todo]- 💡 Indice
> > Si $P(N)=p$ est premier, montrer que $p\mid P(N+rp)$ pour tout $r$.
>
> > [!success]- Solution
> > Supposons qu'un tel $P=\sum_{k=0}^da_kX^k$ existe. Soit $p=P(N)$ premier. Pour tout $r\in\mathbb{N}$, $N+rp\equiv N\pmod p$ donc
> > $$P(N+rp)=\sum a_k(N+rp)^k\equiv\sum a_kN^k=P(N)=p\equiv0\pmod p.$$
> > Donc $p\mid P(N+rp)$. Or $P(N+rp)$ est premier pour tout $r$ (car $N+rp\geq N$), donc $P(N+rp)=p$ pour tout $r\in\mathbb{N}$. Le polynôme $P-p$ a donc une infinité de racines : il est nul, et $P=p$ est constant : contradiction. $\square$

> [!question]- <span style="font-variant: small-caps;">Exercice 9 ★★ : nombres de Fermat premiers entre eux</span>
> Pour $n\in\mathbb{N}$ on pose $F_n=2^{2^n}+1$.
> a) Montrer que les $F_n$ sont premiers entre eux deux à deux.
> b) En déduire une autre démonstration de l'infinité des nombres premiers.
>
> > [!success]- Solution
> > **a)** Soient $n\in\mathbb{N}$, $k\in\mathbb{N}^\ast$. On a $F_{n+k}-1=2^{2^{n+k}}=\left(2^{2^n}\right)^{2^k}=(F_n-1)^{2^k}$. Modulo $F_n$ : $F_{n+k}-1\equiv(-1)^{2^k}=1$, donc $F_{n+k}\equiv2\pmod{F_n}$, i.e. $F_n\mid F_{n+k}-2$. Le pgcd $d$ de $F_n$ et $F_{n+k}$ divise donc $F_{n+k}-(F_{n+k}-2)=2$. Comme $F_n$ est impair, $d=1$.
> >
> > **b)** Pour chaque $n$, soit $p_n$ un facteur premier de $F_n$. Les $F_n$ étant premiers entre eux deux à deux, les $p_n$ sont **deux à deux distincts** : on a une infinité de nombres premiers. $\square$

> [!question]- <span style="font-variant: small-caps;">Exercice 10 ★★★ : nombres parfaits pairs (Euclide-Euler)</span>
> On note $\sigma(n)$ la somme des diviseurs de $n$. Un entier $n$ est *parfait* si $\sigma(n)=2n$.
> a) Exprimer $\sigma(n)$ à l'aide de la décomposition en facteurs premiers, et montrer que $n\wedge m=1\Rightarrow\sigma(nm)=\sigma(n)\sigma(m)$.
> b) Si $2^p-1$ est premier, montrer que $n=2^{p-1}(2^p-1)$ est parfait.
> c) Réciproquement, montrer qu'un nombre parfait **pair** est de cette forme, avec $2^p-1$ premier.
>
> > [!todo]- 💡 Indice
> > c) Écrire $n=2^{p-1}m$ avec $m$ impair, utiliser a) puis Gauss, puis compter les diviseurs de $m$.
>
> > [!success]- Solution
> > **a)** Si $n=p_1^{\alpha_1}\cdots p_k^{\alpha_k}$, les diviseurs de $n$ sont les $p_1^{\beta_1}\cdots p_k^{\beta_k}$, $0\leq\beta_i\leq\alpha_i$, donc
> > $$\sigma(n)=\prod_{i=1}^k(1+p_i+\dots+p_i^{\alpha_i})=\prod_{i=1}^k\frac{p_i^{\alpha_i+1}-1}{p_i-1}.$$
> > Si $n\wedge m=1$, les facteurs premiers de $nm$ sont ceux de $n$ et de $m$ (disjoints), donc la formule donne $\sigma(nm)=\sigma(n)\sigma(m)$.
> >
> > **b)** $2^p-1$ premier est impair, donc premier avec $2^{p-1}$ : $\sigma(n)=\sigma(2^{p-1})\sigma(2^p-1)=(2^p-1)\cdot2^p=2n$. ✔
> >
> > **c)** Soit $n$ parfait pair : $n=2^{p-1}m$ avec $p\geq2$, $m$ impair. Alors $\sigma(n)=(2^p-1)\sigma(m)$ et $\sigma(n)=2n=2^pm$. Donc $(2^p-1)\mid2^pm$ et $(2^p-1)\wedge2^p=1$, donc (Gauss) $(2^p-1)\mid m$ : $m=(2^p-1)\ell$. L'égalité devient $\sigma(m)=2^p\ell=m+\ell$.
> > Si $\ell>1$, alors $m$ a au moins les trois diviseurs distincts $1,\ell,m$ (car $1<\ell<m$), donc $\sigma(m)\geq m+\ell+1$ : absurde. Donc $\ell=1$, $m=2^p-1$ et $\sigma(m)=m+1$ : les seuls diviseurs de $m$ sont $1$ et $m$, donc $m=2^p-1$ est **premier**. $\square$
>
> > [!quote]- Remarque
> > On ne connaît aucun nombre parfait **impair**, on ne sait même pas s'il en existe. S'il en existe un, il a au moins $300$ chiffres décimaux et au moins $9$ facteurs premiers distincts. Le théorème d'Euler dit qu'il est de la forme $p^{1+4\alpha}Q^2$ avec $p\equiv1\pmod 4$ premier.

> [!question]- <span style="font-variant: small-caps;">Exercice 11 ★★★ : théorème de Liouville</span>
> Soit $p>5$ un entier. Montrer que l'équation $(p-1)!+1=p^m$ n'a pas de solution $m\in\mathbb{N}^\ast$.
>
> > [!todo]- 💡 Indice
> > Montrer que $(p-1)^2\mid(p-1)!$, puis que $(p-1)\mid m$, puis comparer les tailles.
>
> > [!success]- Solution
> > Supposons $(p-1)!+1=p^m$. Comme $p>5$, $(p-1)!+1$ est impair, donc $p$ est impair.
> >
> > **Étape 1.** Pour $p>5$, $2<\frac{p-1}2<p-1$ : les trois entiers $2$, $\frac{p-1}2$, $p-1$ sont distincts et figurent dans le produit $(p-1)!$. Donc $2\cdot\frac{p-1}2\cdot(p-1)=(p-1)^2$ divise $(p-1)!=p^m-1$.
> >
> > **Étape 2.** $p^m-1=(p-1)(1+p+\dots+p^{m-1})$, donc $(p-1)\mid1+p+\dots+p^{m-1}$. Or $p\equiv1\pmod{p-1}$, donc cette somme est $\equiv m\pmod{p-1}$ : ainsi $(p-1)\mid m$, et $m\geq p-1$.
> >
> > **Étape 3.** $p^m\geq p^{p-1}>(p-1)^{p-1}\geq2\,(p-1)!\geq(p-1)!+2$, donc $p^m>(p-1)!+1$ : contradiction. $\square$

> [!question]- <span style="font-variant: small-caps;">Exercice 12 ★★★ : critère de factorisabilité des nombres de Mersenne</span>
> a) Soit $p$ un nombre premier de la forme $4k+3$, $k\in\mathbb{N}^\ast$. Montrer que $2^{(p-1)/2}\equiv(-1)^{k+1}\pmod p$.
> b) Si $p$ est un premier de la forme $4k+3$ et si $2p+1$ est premier, montrer que $M_p=2^p-1$ n'est pas premier.
>
> > [!todo]- 💡 Indice
> > a) Calculer de deux façons $N=2\cdot4\cdot6\cdots(p-1)$. Remplacer les facteurs $>\frac p2$ par leurs opposés modulo $p$.
>
> > [!success]- Solution
> > **a)** Ici $p-1=4k+2$ et $\frac{p-1}2=2k+1$. On pose
> > $$N=2\cdot4\cdots(4k+2)=2^{2k+1}(2k+1)!=2^{(p-1)/2}(2k+1)!.$$
> > Séparons les facteurs pairs $\leq2k$ et ceux $\geq2k+2$. Modulo $p=4k+3$ :
> > $$2k+2\equiv-(2k+1),\quad2k+4\equiv-(2k-1),\;\dots,\quad4k+2\equiv-1.$$
> > Il y a $k+1$ de ces facteurs, donc
> > $$N\equiv(2\cdot4\cdots2k)\cdot(-1)^{k+1}(2k+1)(2k-1)\cdots3\cdot1=(-1)^{k+1}(2k+1)!\pmod p.$$
> > Ainsi $2^{(p-1)/2}(2k+1)!\equiv(-1)^{k+1}(2k+1)!$. Comme $2k+1<p$ et $p$ est premier, $(2k+1)!\not\equiv0\pmod p$ : on simplifie. $\square$
> >
> > **b)** Soit $q=2p+1=8k+7=4(2k+1)+3$, premier. Le résultat a) appliqué à $q$ (avec $k'=2k+1$) donne
> > $$2^{(q-1)/2}=2^p\equiv(-1)^{k'+1}=(-1)^{2k+2}=1\pmod q.$$
> > Donc $q\mid2^p-1=M_p$. Comme $M_p>q$, $M_p$ n'est pas premier.
>
> > [!example]- Application
> > $p=11$ ($2p+1=23$), $23$ ($47$), $83$ ($167$), $131$, $179$, $191$, $239$, $251$ : pour tous ces $p$, $M_p$ n'est pas premier. Par exemple $M_{11}=2047=23\times89$.

> [!question]- <span style="font-variant: small-caps;">Exercice 13 ★★ : triplets pythagoriciens</span>
> Résoudre $x^2+y^2=z^2$ avec $(x,y,z)\in(\mathbb{N}^\ast)^3$.
>
> > [!todo]- 💡 Indice
> > Se ramener à $x,y,z$ premiers entre eux, étudier la parité (modulo $4$), puis factoriser $(x/2)^2=\frac{z-y}2\cdot\frac{z+y}2$.
>
> > [!success]- Solution
> > Quitte à diviser par $\operatorname{pgcd}(x,y,z)$, supposons $x,y,z$ premiers entre eux dans leur ensemble. Alors ils le sont **deux à deux** (un premier divisant deux d'entre eux diviserait le carré du troisième, donc le troisième).
> >
> > **Parité.** Un impair $N=2n+1$ vérifie $N^2=4n^2+4n+1\equiv1\pmod4$. Si $x,y$ étaient impairs, $z^2=x^2+y^2\equiv2\pmod4$, impossible (un carré est $\equiv0$ ou $1$). Donc l'un d'eux est pair, disons $x$ ; alors $y$ et $z$ sont impairs (premiers avec $x$, donc avec $2$).
> >
> > **Factorisation.** On écrit $\left(\frac x2\right)^2=\frac{z-y}2\cdot\frac{z+y}2$ (entiers, car $z,y$ impairs). Ces deux facteurs sont **premiers entre eux** : un premier $p$ les divisant diviserait leur somme $z$ et leur différence $y$, ce qui contredit $y\wedge z=1$. Un produit de deux entiers premiers entre eux étant un carré, chacun est un carré (décomposition en facteurs premiers) :
> > $$\tfrac{z-y}2=n^2,\quad\tfrac{z+y}2=m^2,\quad\text{d'où}\quad z=m^2+n^2,\;y=m^2-n^2,\;x=2mn.$$
> > Réciproquement, ces triplets sont solutions. **Solution générale :**
> > $$(x,y)\text{ ou }(y,x)=\bigl(2kmn,\;k(m^2-n^2)\bigr),\quad z=k(m^2+n^2),\quad k\in\mathbb{N}^\ast,\;m>n\geq1.$$
>
> > [!quote]- Remarque
> > Pour $x^n+y^n=z^n$ avec $n\geq3$, Fermat (1637) affirma qu'il n'y a pas de solution en entiers non nuls. La démonstration complète est due à Andrew Wiles (1993-1994).

---

### Compléments de niveau agrégation

> [!question]- <span style="font-variant: small-caps;">Exercice 14 ★★★ : théorème de Fermat sur les sommes de deux carrés</span>
> Soit $p\equiv1\pmod 4$ un nombre premier. Montrer qu'il existe $a,b\in\mathbb{N}^\ast$ tels que $p=a^2+b^2$.
>
> > [!todo]- 💡 Indice
> > Étape 1 : Wilson donne $x$ avec $x^2\equiv-1\pmod p$. Étape 2 (lemme de Thue) : principe des tiroirs sur les nombres $u-xv\bmod p$ avec $0\leq u,v\leq\lfloor\sqrt p\rfloor$.
>
> > [!success]- Solution
> > **Étape 1 : $-1$ est un carré modulo $p$.** Par Wilson, $(p-1)!\equiv-1$. Regroupons chaque $k\in\left[1,\frac{p-1}2\right]$ avec $p-k\equiv-k$ :
> > $$(p-1)!=\prod_{k=1}^{(p-1)/2}k(p-k)\equiv(-1)^{(p-1)/2}\left(\left(\tfrac{p-1}2\right)!\right)^2\pmod p.$$
> > Comme $p\equiv1\pmod 4$, $(p-1)/2$ est pair, donc $\left(\left(\frac{p-1}2\right)!\right)^2\equiv-1$. Posons $x=\left(\frac{p-1}2\right)!$ : $x^2\equiv-1\pmod p$.
> >
> > **Étape 2 : lemme de Thue.** Soit $m=\lfloor\sqrt p\rfloor$ (on a $m<\sqrt p<m+1$ car $p$ n'est pas un carré). Les $(m+1)^2>p$ couples $(u,v)$ avec $0\leq u,v\leq m$ donnent $(m+1)^2$ valeurs de $u-xv$ pour seulement $p$ classes modulo $p$ : par les tiroirs, deux couples distincts $(u,v)\neq(u',v')$ donnent $u-xv\equiv u'-xv'$. Posons $a=u-u'$, $b=v-v'$ : $(a,b)\neq(0,0)$, $|a|,|b|\leq m<\sqrt p$ et $a\equiv xb\pmod p$.
> >
> > **Conclusion.** $a^2\equiv x^2b^2\equiv-b^2\pmod p$, donc $p\mid a^2+b^2$ avec $0<a^2+b^2<2p$ : $a^2+b^2=p$. Et $a,b\neq0$ car $p$ n'est pas un carré. $\square$

> [!question]- <span style="font-variant: small-caps;">Exercice 15 ★★ : premiers $\equiv3\pmod 4$ et sommes de deux carrés</span>
> Soit $p\equiv3\pmod 4$ premier. Montrer que si $p\mid a^2+b^2$, alors $p\mid a$ et $p\mid b$. En déduire qu'un entier $n$ somme de deux carrés a tous ses facteurs premiers $\equiv3\pmod 4$ avec un exposant pair.
>
> > [!todo]- 💡 Indice
> > Si $p\nmid b$, $b$ est inversible modulo $p$. Appliquer Fermat à $(ab^{-1})$.
>
> > [!success]- Solution
> > Si $p\nmid b$, soit $c$ un inverse de $b$ modulo $p$. De $a^2\equiv-b^2$ on tire $(ac)^2\equiv-1$. Par Fermat, $(ac)^{p-1}\equiv1$. Or $(ac)^{p-1}=((ac)^2)^{(p-1)/2}\equiv(-1)^{(p-1)/2}=-1$ car $(p-1)/2$ est **impair**. Donc $1\equiv-1\pmod p$, $p\mid2$ : absurde. Donc $p\mid b$, puis $p\mid a^2$ donc $p\mid a$.
> >
> > **Conséquence.** Si $n=a^2+b^2$ et $p\equiv3\pmod 4$ divise $n$, alors $p\mid a,b$ donc $n=p^2n'$ avec $n'=a'^2+b'^2$. Par récurrence descendante sur $n$, l'exposant de $p$ dans $n$ est pair. $\square$
>
> > [!quote]- Théorème des deux carrés (énoncé complet)
> > $n$ est somme de deux carrés $\iff$ tout facteur premier $\equiv3\pmod 4$ de $n$ a un exposant pair. La réciproque se déduit de l'exercice 14 et de l'identité de Brahmagupta : $(a^2+b^2)(c^2+d^2)=(ac-bd)^2+(ad+bc)^2$.

> [!question]- <span style="font-variant: small-caps;">Exercice 16 ★★ : infinité des premiers $\equiv1\pmod 4$</span>
> Montrer qu'il y a une infinité de nombres premiers de la forme $4k+1$.
>
> > [!todo]- 💡 Indice
> > Considérer $(n!)^2+1$ et utiliser l'exercice 15.
>
> > [!success]- Solution
> > Soit $n\geq2$ et $M=(n!)^2+1$, impair. Soit $p$ un facteur premier de $M$. Alors $p>n$ (sinon $p\mid n!$ et $p\mid1$) et $p\mid(n!)^2+1^2$. Si $p\equiv3\pmod 4$, l'exercice 15 donnerait $p\mid1$ : absurde. Comme $p\neq2$, $p\equiv1\pmod 4$. Ainsi pour tout $n$, il existe un premier $\equiv1\pmod 4$ supérieur à $n$. $\square$

> [!question]- <span style="font-variant: small-caps;">Exercice 17 ★★★ 🔗 : diviseurs premiers des nombres de Fermat</span>
> Montrer que tout facteur premier $p$ de $F_n=2^{2^n}+1$ est de la forme $p=k\cdot2^{n+1}+1$. Retrouver que $641\mid F_5$ est plausible.
>
> > [!todo]- 💡 Indice
> > Calculer l'ordre de $\overline2$ dans le groupe $(\mathbb{Z}/p\mathbb{Z})^\ast$ (d'ordre $p-1$).
>
> > [!success]- Solution
> > Soit $p$ premier divisant $F_n$ ($p$ impair). Alors $2^{2^n}\equiv-1\pmod p$ et $2^{2^{n+1}}\equiv1$. L'ordre $d$ de $\overline2$ dans $(\mathbb{Z}/p\mathbb{Z})^\ast$ divise donc $2^{n+1}$ (théorème 3 du fichier II). C'est donc une puissance de $2$. Si $d\mid2^n$, on aurait $2^{2^n}\equiv1$, donc $-1\equiv1$, $p=2$ : absurde. Donc $d=2^{n+1}$ exactement. Par Lagrange ($\operatorname{Card}((\mathbb{Z}/p\mathbb{Z})^\ast)=p-1$), $2^{n+1}\mid p-1$. $\square$
> >
> > **Application à $F_5$.** Les facteurs premiers de $F_5=4294967297$ sont de la forme $64k+1$ : $193$, $257$, $449$, $577$, $641$, … On trouve $641=64\times10+1$, et $F_5=641\times6700417$ (c'est le résultat d'Euler : $F_5$ n'est pas premier).

> [!question]- <span style="font-variant: small-caps;">Exercice 18 ★★ : pgcd de $a^m-1$ et $a^n-1$</span>
> Soient $a\geq2$ et $m,n\in\mathbb{N}^\ast$. Montrer que $\operatorname{pgcd}(a^m-1,a^n-1)=a^{\operatorname{pgcd}(m,n)}-1$.
>
> > [!todo]- 💡 Indice
> > Pour $m>n$ : $a^m-1=a^{m-n}(a^n-1)+(a^{m-n}-1)$. Suivre l'algorithme d'Euclide sur les exposants.
>
> > [!success]- Solution
> > Notons $g(m,n)=\operatorname{pgcd}(a^m-1,a^n-1)$. Pour $m>n$, l'identité $a^m-1=a^{m-n}(a^n-1)+(a^{m-n}-1)$ montre que les diviseurs communs de $a^m-1$ et $a^n-1$ sont ceux de $a^n-1$ et $a^{m-n}-1$ : $g(m,n)=g(n,m-n)$. En répétant (algorithme d'Euclide par soustractions, ou par divisions : $g(m,n)=g(n,r)$ où $r$ est le reste de $m$ par $n$ — avec la convention $a^0-1=0$ et $\operatorname{pgcd}(x,0)=x$), on arrive à $g(d,0)=a^d-1$ où $d=\operatorname{pgcd}(m,n)$, puisque la suite des exposants suit **exactement** l'algorithme d'Euclide sur $(m,n)$. $\square$
>
> > [!quote]- Corollaire
> > Les nombres de Mersenne $M_p$, $M_q$ avec $p\neq q$ premiers sont premiers entre eux ($\operatorname{pgcd}(p,q)=1$ donne $2^1-1=1$).

> [!question]- <span style="font-variant: small-caps;">Exercice 19 ★★★ 🔗 : $n\mid2^n-1\Rightarrow n=1$</span>
> Montrer que si $n\in\mathbb{N}^\ast$ divise $2^n-1$, alors $n=1$.
>
> > [!todo]- 💡 Indice
> > Par l'absurde, considérer le **plus petit** facteur premier $p$ de $n$ et l'ordre de $\overline2$ dans $(\mathbb{Z}/p\mathbb{Z})^\ast$.
>
> > [!success]- Solution
> > Supposons $n>1$ et soit $p$ son plus petit facteur premier. Alors $p\mid n\mid2^n-1$, donc $p$ est impair et $2^n\equiv1\pmod p$. L'ordre $d$ de $\overline2$ dans $(\mathbb{Z}/p\mathbb{Z})^\ast$ divise $n$ (thm 3 du fichier II) et divise $p-1$ (Fermat/Lagrange). Donc $d\mid\operatorname{pgcd}(n,p-1)$.
> > Or tout diviseur premier de $p-1$ est $<p$, donc ne divise pas $n$ (minimalité de $p$) : $\operatorname{pgcd}(n,p-1)=1$. Donc $d=1$, i.e. $2\equiv1\pmod p$, soit $p\mid1$ : absurde. $\square$

> [!question]- <span style="font-variant: small-caps;">Exercice 20 ★★ 🔗 : théorème d'Euler et multiplicativité de $\varphi$</span>
> a) Montrer que si $a\wedge n=1$, alors $a^{\varphi(n)}\equiv1\pmod n$.
> b) Montrer que si $m\wedge n=1$, alors $\varphi(mn)=\varphi(m)\varphi(n)$. En déduire $\varphi(n)=n\prod_{p\mid n}\left(1-\frac1p\right)$.
>
> > [!todo]- 💡 Indice
> > a) $\overline a$ est un élément du groupe $(\mathbb{Z}/n\mathbb{Z})^\ast$ d'ordre $\varphi(n)$. b) Théorème chinois.
>
> > [!success]- Solution
> > **a)** $(\mathbb{Z}/n\mathbb{Z})^\ast$ est un groupe de cardinal $\varphi(n)$ (prop. 12). Si $a\wedge n=1$, $\overline a$ y est inversible, et le théorème 2 du fichier II donne $\overline a^{\varphi(n)}=\overline1$. $\square$
> >
> > **b)** Par le théorème chinois, $\Phi\colon\mathbb{Z}/mn\mathbb{Z}\to\mathbb{Z}/m\mathbb{Z}\times\mathbb{Z}/n\mathbb{Z}$, $\overline x\mapsto(\overline x,\overline x)$ est bijective. Or $x\wedge mn=1\iff x\wedge m=1$ et $x\wedge n=1$ (prop. 2). Donc $\Phi$ induit une bijection des inversibles de $\mathbb{Z}/mn\mathbb{Z}$ sur le produit des inversibles : $\varphi(mn)=\varphi(m)\varphi(n)$.
> > Avec $\varphi(p^k)=p^k-p^{k-1}=p^k(1-\frac1p)$ et la décomposition en facteurs premiers, on obtient la formule. $\square$

> [!question]- <span style="font-variant: small-caps;">Exercice 21 ★★ : formule de Legendre</span>
> Soit $p$ premier et $v_p(n!)$ l'exposant de $p$ dans $n!$. Montrer que $v_p(n!)=\sum_{k\geq1}\left\lfloor\frac n{p^k}\right\rfloor$. Combien de zéros termine l'écriture décimale de $2026!$ ?
>
> > [!todo]- 💡 Indice
> > $v_p(j)=\#\{k\geq1\mid p^k\mid j\}$. Sommer sur $j\leq n$ en échangeant les sommes.
>
> > [!success]- Solution
> > On a $v_p(n!)=\sum_{j=1}^nv_p(j)=\sum_{j=1}^n\sum_{k\geq1}\mathbf{1}_{p^k\mid j}=\sum_{k\geq1}\#\{j\leq n\mid p^k\mid j\}=\sum_{k\geq1}\left\lfloor\frac n{p^k}\right\rfloor$ (il y a $\lfloor n/p^k\rfloor$ multiples de $p^k$ entre $1$ et $n$). $\square$
> >
> > **Zéros de $2026!$.** Le nombre de zéros terminaux est $\min(v_2,v_5)=v_5(2026!)$ (il y a bien plus de facteurs $2$ que de facteurs $5$) :
> > $$\left\lfloor\tfrac{2026}5\right\rfloor+\left\lfloor\tfrac{2026}{25}\right\rfloor+\left\lfloor\tfrac{2026}{125}\right\rfloor+\left\lfloor\tfrac{2026}{625}\right\rfloor=405+81+16+3=\boxed{505}.$$

> [!question]- <span style="font-variant: small-caps;">Exercice 22 ★★★ : $H_n=1+\frac12+\dots+\frac1n$ n'est jamais entier ($n\geq2$)</span>
> Montrer que pour tout $n\geq2$, $H_n$ n'est pas un entier.
>
> > [!todo]- 💡 Indice
> > Soit $2^k$ la plus grande puissance de $2$ avec $2^k\leq n$. Multiplier $H_n$ par $2^{k-1}\times$ (produit des impairs $\leq n$). Un seul terme n'est alors pas entier.
>
> > [!success]- Solution
> > Soit $k\geq1$ tel que $2^k\leq n<2^{k+1}$, $P$ le produit des **entiers impairs** $\leq n$, et $M=2^{k-1}P$. Alors $M\,H_n=\sum_{j=1}^n\frac Mj$.
> > - Si $j\neq2^k$, $j=2^aq$ avec $q$ impair, $q\leq n$ donc $q\mid P$, et $a\leq k-1$ (le seul entier $\leq n<2^{k+1}$ de valuation $2$-adique $\geq k$ est $2^k$ lui-même, car $3\cdot2^k>2^{k+1}>n$). Donc $\frac Mj$ est un entier.
> > - Si $j=2^k$ : $\frac M{2^k}=\frac P2$, qui **n'est pas** un entier ($P$ impair).
> >
> > Donc $M\,H_n=(\text{entier})+\frac P2\notin\mathbb{Z}$. Si $H_n$ était entier, $MH_n$ le serait : contradiction. $\square$

---

> [!tip] <span style="font-variant: small-caps;">Pistes pour continuer</span>
> Idées d'exercices supplémentaires, que je peux rédiger sur demande : loi de réciprocité quadratique (preuve par Gauss ou par les sommes de Gauss), théorème de Wilson généralisé, pseudo-premiers et nombres de Carmichael, critère de Lucas-Lehmer pour les nombres de Mersenne, équation de Pell, équations diophantiennes $x^2+y^2=z^n$.

---
## 1.4. Arithmétique modulaire

### 1.4.1. *Calculs dans $\mathbb{Z}/n\mathbb{Z}$*

> [!info] <span style="font-variant: small-caps;">Proposition 11 : compatibilité avec les opérations</span>
> Soient $n\in\mathbb{N}^\ast$ et $a\equiv a'$, $b\equiv b'\pmod n$. Alors
> $$a+b\equiv a'+b'\pmod n,\qquad ab\equiv a'b'\pmod n,\qquad a^k\equiv a'^k\pmod n\;(k\in\mathbb{N}).$$

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> Écrivons $a'=a+nk$, $b'=b+nl$. Alors $a'+b'=a+b+n(k+l)$ et $a'b'=ab+n(al+bk+nkl)$. La puissance découle de la récurrence sur $k$. $\square$

> [!warning] <span style="font-variant: small-caps;">Pièges</span>
> - On **ne peut pas** simplifier librement : $2\times3\equiv2\times0\pmod 6$ mais $3\not\equiv0$.
> - On **ne réduit pas** les exposants modulo $n$ : $2^{5}\not\equiv2^{5\bmod 3}\pmod 3$ en général. L'exposant se réduit modulo l'ordre (voir Fermat, Euler).

> [!info] <span style="font-variant: small-caps;">Proposition 12 : éléments inversibles</span>
> Dans $\mathbb{Z}/n\mathbb{Z}$, $\overline{a}$ est inversible si et seulement si $a\wedge n=1$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> $\overline a$ inversible $\iff\exists u,\;au\equiv1\pmod n\iff\exists u,v,\;au+nv=1\iff a\wedge n=1$ (Bézout). $\square$

> [!note] <span style="font-variant: small-caps;">Définition 7 : indicatrice d'Euler</span>
> On note $\varphi(n)$ le nombre d'entiers de $\llbracket1,n\rrbracket$ premiers avec $n$. C'est le cardinal du groupe $(\mathbb{Z}/n\mathbb{Z})^\ast$ des inversibles.
>
> - Si $p$ est premier, $\varphi(p)=p-1$ et $\varphi(p^k)=p^k-p^{k-1}$.
> - Si $m\wedge n=1$, $\varphi(mn)=\varphi(m)\varphi(n)$ (conséquence du théorème chinois).

> [!example]- <span style="font-variant: small-caps;">Exemple : résoudre $ax\equiv b\pmod n$</span>
> Résoudre $47x\equiv5\pmod{111}$. On a vu $47\times26\equiv1\pmod{111}$ : on multiplie par $26$ :
> $$x\equiv5\times26=130\equiv19\pmod{111}.$$

### 1.4.2. *Théorème chinois*

> [!info] <span style="font-variant: small-caps;">Théorème 6 (Restes chinois)</span>
> Soient $m,n$ deux entiers premiers entre eux. Pour tout $(a,b)\in\mathbb{Z}^2$, le système
> $$\begin{cases}x\equiv a\pmod m\\x\equiv b\pmod n\end{cases}$$
> admet des solutions, et elles forment une unique classe modulo $mn$. Autrement dit :
> $$\mathbb{Z}/mn\mathbb{Z}\;\cong\;\mathbb{Z}/m\mathbb{Z}\times\mathbb{Z}/n\mathbb{Z}.$$

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> **Existence.** Bézout : $mu+nv=1$. Posons $x_0=a\,nv+b\,mu$. Alors $x_0\equiv a\cdot nv\equiv a(1-mu)\equiv a\pmod m$ et de même $x_0\equiv b\pmod n$.
>
> **Unicité modulo $mn$.** Si $x$ et $x'$ sont deux solutions, $m\mid x-x'$ et $n\mid x-x'$. Comme $m\wedge n=1$, la proposition 3 donne $mn\mid x-x'$. Réciproquement, toute classe $x_0+mn\mathbb{Z}$ convient. $\square$

> [!example]- <span style="font-variant: small-caps;">Exemple</span>
> Résoudre $x\equiv2\pmod3$ et $x\equiv3\pmod5$. On a $3\cdot2-5\cdot1=1$, donc $m=3,n=5,u=2,v=-1$ :
> $$x_0=2\cdot5\cdot(-1)+3\cdot3\cdot2=-10+18=8.$$
> Vérification : $8\equiv2\pmod 3$, $8\equiv3\pmod 5$ ✔. Solution : $x\equiv8\pmod{15}$.


---

> [!todo] <span style="font-variant: small-caps;">Suite du cours (à construire)</span>
> - [x] Anneaux et corps (idéaux, anneaux quotients, anneaux principaux, polynômes)
> - [x] Théorèmes de Sylow (utiliser Cauchy, exercice 12, et la section 2.6)
> - [x] Simplicité de $\mathfrak{A}_n$ ($n\geq5$)

---

# 2. Groupes

## 2.1. Généralités

> [!note] <span style="font-variant: small-caps;">Définition 1 : groupe</span>
> On appelle *groupe* un ensemble $G$ muni d'une loi interne $\ast$ telle que :
> 1. **(i)** La loi $\ast$ est *associative* : $\forall x,y,z\in G,\;(x\ast y)\ast z=x\ast(y\ast z)$.
> 2. **(ii)** Il existe un *élément neutre* $e$ : $\forall x\in G,\;x\ast e=e\ast x=x$.
> 3. **(iii)** Tout élément a un *symétrique* : $\forall x\in G,\;\exists y\in G,\;x\ast y=y\ast x=e$.
>
> Si la loi $\ast$ est commutative, on parle de groupe *commutatif* (ou *abélien*).

> [!quote] <span style="font-variant: small-caps;">Remarque 1</span>
> - L'élément neutre $e$ de $(G,\ast)$ est unique.
> - Pour tout $x\in G$, $x$ a un unique symétrique, souvent noté $x^{-1}$.
>
> > [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> > *Neutre.* Si $e$ et $e'$ sont neutres, $e=e\ast e'=e'$.
> > *Symétrique.* Si $y$ et $y'$ sont symétriques de $x$, alors $y=y\ast e=y\ast(x\ast y')=(y\ast x)\ast y'=e\ast y'=y'$. $\square$

> [!note] <span style="font-variant: small-caps;">Définition 2 : sous-groupe</span>
> Soit $(G,\ast)$ un groupe. On dit que $H\subset G$ est un *sous-groupe* de $G$ si la restriction de la loi $\ast$ à $H$ lui confère une structure de groupe.

> [!example] <span style="font-variant: small-caps;">Exemple 1</span>
> L'ensemble $\mathbb{Z}$ des entiers, muni de l'addition, est un groupe. Pour tout $n\in\mathbb{N}$, $n\mathbb{Z}$ est un sous-groupe de $(\mathbb{Z},+)$. Réciproquement, on peut démontrer que **tous** les sous-groupes de $(\mathbb{Z},+)$ sont de la forme $n\mathbb{Z}$, avec $n\in\mathbb{N}$ (c'est le lemme de la section 1.1.2).

> [!quote] <span style="font-variant: small-caps;">Convention</span>
> Dorénavant, la loi $\ast$ d'un groupe sera notée multiplicativement (la notation additive est réservée aux groupes abéliens). On écrit $xy$ pour $x\ast y$ et $x^{-1}$ pour le symétrique.

> [!info] <span style="font-variant: small-caps;">Proposition 1 (Caractérisation des sous-groupes)</span>
> Soit $G$ un groupe et $H\subset G$. L'ensemble $H$ est un sous-groupe de $G$ si et seulement si $H\neq\varnothing$ et pour tout couple $(x,y)\in H^2$, on a $xy^{-1}\in H$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> $(\Rightarrow)$ Un sous-groupe contient $e$ (donc non vide) et est stable par inverse et produit : $xy^{-1}\in H$.
>
> $(\Leftarrow)$ Soit $x\in H$ (possible car $H\neq\varnothing$).
> - Avec $y=x$ : $xx^{-1}=e\in H$.
> - Avec $(e,x)$ : $ex^{-1}=x^{-1}\in H$.
> - Pour $x,y\in H$ : $y^{-1}\in H$ donc $x(y^{-1})^{-1}=xy\in H$.
>
> La loi est donc interne sur $H$, associative (héritée de $G$), $e\in H$ et tout élément a son inverse dans $H$. $\square$

> [!info] <span style="font-variant: small-caps;">Proposition 2</span>
> Une intersection de sous-groupes d'un groupe $G$ est un sous-groupe de $G$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> Soit $(H_i)_{i\in I}$ une famille de sous-groupes et $H=\bigcap_iH_i$. Alors $e\in H$ donc $H\neq\varnothing$. Si $x,y\in H$, pour tout $i$, $x,y\in H_i$ donc $xy^{-1}\in H_i$ ; ainsi $xy^{-1}\in H$. On conclut par la proposition 1. $\square$

> [!quote] <span style="font-variant: small-caps;">Remarque 2</span>
> Le résultat est **faux** dans le cas d'une réunion.
>
> > [!example]- <span style="font-variant: small-caps;">Contre-exemple</span>
> > Dans $(\mathbb{Z},+)$, $2\mathbb{Z}$ et $3\mathbb{Z}$ sont des sous-groupes, mais $2\mathbb{Z}\cup3\mathbb{Z}$ n'en est pas un : $2$ et $3$ y sont, mais $2+3=5$ n'y est pas.
> >
> > Plus généralement, $H_1\cup H_2$ est un sous-groupe si et seulement si $H_1\subset H_2$ ou $H_2\subset H_1$.

> [!note] <span style="font-variant: small-caps;">Définition 3 : centre</span>
> Soit $(G,\cdot)$ un groupe. On appelle *centre* de $G$, noté $Z(G)$, l'ensemble des éléments de $G$ commutant avec tous les éléments de $G$ :
> $$Z(G)=\{z\in G\mid\forall g\in G,\;zg=gz\}.$$
> L'ensemble $Z(G)$ est un sous-groupe de $G$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> $e\in Z(G)$ donc $Z(G)\neq\varnothing$. Soient $z,z'\in Z(G)$ et $g\in G$. Alors $zg=gz$ et $z'g=gz'$, donc $g z'^{-1}=z'^{-1}g$ (on multiplie $z'g=gz'$ à gauche et à droite par $z'^{-1}$). Donc
> $$(zz'^{-1})g=z\,g\,z'^{-1}=g\,zz'^{-1}.$$
> Ainsi $zz'^{-1}\in Z(G)$ et Proposition 1 conclut. $\square$

> [!quote]- <span style="font-variant: small-caps;">Remarque 3</span>
> $G$ est abélien $\iff Z(G)=G$. Le centre de $\mathbb{Z}/n\mathbb{Z}$ est lui-même, tandis que celui du groupe symétrique $\mathfrak{S}_n$ ($n\geq3$) est trivial.


> [!abstract]- <span style="font-variant: small-caps;">Comment utiliser ce fichier</span>
> 
>
> Convention : pour une action, j'écris $\operatorname{Orb}(x)$ pour l'orbite et $\operatorname{Stab}(x)$ pour le stabilisateur (le livre note $G_x$ et $S_x$, ce qui prête à confusion).


> [!note] <span style="font-variant: small-caps;">Définition 4 : ordre d'un groupe</span>
> Si $G$ est un groupe fini, $\operatorname{Card}(G)$ s'appelle l'*ordre* de $G$.

> [!info] <span style="font-variant: small-caps;">Théorème 1 (Lagrange)</span>
> Soit $G$ un groupe fini. L'ordre de tout sous-groupe $H$ de $G$ divise l'ordre de $G$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration (Lagrange)</span>
> 1. La relation $x\mathcal{R}y\iff xy^{-1}\in H$ est une relation d'équivalence : réflexive ($xx^{-1}=e\in H$), symétrique ($(xy^{-1})^{-1}=yx^{-1}$), transitive ($xz^{-1}=(xy^{-1})(yz^{-1})$).
> 2. La classe de $x$ est $\dot x=Hx=\{hx\mid h\in H\}$. En effet $y\in\dot x\iff yx^{-1}\in H\iff y\in Hx$.
> 3. Pour tout $x$, l'application $H\to Hx,\;h\mapsto hx$ est bijective (inverse $y\mapsto yx^{-1}$) : toutes les classes ont $\operatorname{Card}(H)$ éléments.
> 4. Les classes forment une partition de $G$. Si $n$ est leur nombre, $\operatorname{Card}(G)=n\operatorname{Card}(H)$. $\square$

> [!quote] <span style="font-variant: small-caps;">Remarque 3</span>
> - Les classes $Hx$ sont les *classes à droite* suivant $H$. En utilisant $x\mathcal{R}'y\iff x^{-1}y\in H$ on obtient les *classes à gauche* $xH$.
> - L'entier $\operatorname{Card}(G/\mathcal{R})$ est l'*indice* de $H$ dans $G$, noté $[G:H]$. On a
> $$\operatorname{Card}(G)=[G:H]\times\operatorname{Card}(H).$$

> [!warning] <span style="font-variant: small-caps;">Attention</span>
> La réciproque de Lagrange est **fausse** : $\mathfrak{A}_4$ est d'ordre $12$ mais n'a aucun sous-groupe d'ordre $6$. (Voir aussi l'exercice 8 pour $\mathfrak{S}_5$.)

### Sous-groupes distingués

> [!note] <span style="font-variant: small-caps;">Définition 5 : sous-groupe distingué (ou normal, invariant)</span>
> Soit $G$ un groupe. Un sous-groupe $H$ de $G$ est dit *distingué* dans $G$, noté $H\lhd G$, si pour tout $x\in G$, $xH=Hx$.

> [!example] <span style="font-variant: small-caps;">Exemple 2</span>
> - Tout sous-groupe d'un groupe **abélien** $G$ est distingué dans $G$.
> - Le centre $Z(G)$ est distingué dans $G$. Plus généralement, tout sous-groupe de $Z(G)$ l'est.
> - Un sous-groupe d'**indice $2$** est toujours distingué (voir exercice 9).

> [!quote] <span style="font-variant: small-caps;">Remarque 4 : la relation « distingué dans » n'est pas transitive</span>
> Si $L\lhd H$ et $H\lhd G$, il est faux en général que $L\lhd G$.
>
> > [!example]- <span style="font-variant: small-caps;">Contre-exemple</span>
> > Dans $\mathfrak{A}_4$, $V=\{\mathrm{id},(12)(34),(13)(24),(14)(23)\}$ est distingué, et $K=\{\mathrm{id},(12)(34)\}\lhd V$ car $V$ est abélien. Mais $K$ n'est pas distingué dans $\mathfrak{A}_4$ : en conjuguant $(12)(34)$ par le 3-cycle $(123)$, on obtient $(23)(14)\notin K$.

> [!info] <span style="font-variant: small-caps;">Proposition 3 (caractérisation)</span>
> Soit $G$ un groupe. Un sous-groupe $H$ de $G$ est distingué dans $G$ si et seulement si pour tout $x\in G$, $xHx^{-1}\subset H$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> $(\Rightarrow)$ Si $xH=Hx$, pour $h\in H$ on a $xh\in Hx$, donc $xhx^{-1}\in H$.
>
> $(\Leftarrow)$ L'hypothèse donne $xH\subset Hx$ pour tout $x$. Appliquée à $x^{-1}$ : $x^{-1}H\subset Hx^{-1}$, soit en multipliant à gauche et à droite par $x$ : $Hx\subset xH$. D'où $xH=Hx$. $\square$

### Groupes quotients

> [!info] <span style="font-variant: small-caps;">Théorème (groupe quotient)</span>
> Soit $H\lhd G$. L'ensemble quotient $G/H=\{xH\mid x\in G\}$ est un groupe pour la loi
> $$\overline x\cdot\overline y=\overline{xy},$$
> appelé *groupe quotient* de $G$ par $H$. Si $G$ est fini, $\operatorname{Card}(G)=\operatorname{Card}(G/H)\cdot\operatorname{Card}(H)$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> **La loi est bien définie** (c'est le point crucial : $\overline{xy}$ ne doit pas dépendre des représentants). Si $\overline{x'}=\overline x$ et $\overline{y'}=\overline y$, on écrit $x'=xh$ et $y'=yh'$ avec $h,h'\in H$. Alors
> $$x'y'=xhyh'=xy\,(y^{-1}hy)\,h'\in xyH,$$
> car $y^{-1}hy\in H$ ($H$ distingué, proposition 3). Donc $\overline{x'y'}=\overline{xy}$.
>
> **Structure de groupe.** L'associativité vient de celle de $G$, l'élément neutre est $\overline e=H$, l'inverse de $\overline x$ est $\overline{x^{-1}}$. $\square$

> [!quote] <span style="font-variant: small-caps;">Pourquoi « distingué » ?</span>
> On peut montrer que les relations d'équivalence compatibles avec la loi de $G$ sont exactement les $x\mathcal{R}y\iff xy^{-1}\in H$ avec $H$ distingué. **Distingué** = **noyau possible d'un morphisme** = **quotient possible**. C'est le fil rouge du chapitre.

> [!example] <span style="font-variant: small-caps;">Exemple 3</span>
> $n\mathbb{Z}$ est un sous-groupe du groupe additif $(\mathbb{Z},+)$, commutatif donc distingué. On définit ainsi le groupe quotient $\mathbb{Z}/n\mathbb{Z}$ (la structure d'anneau sera introduite avec les anneaux quotients).

### Morphismes de groupes

> [!note] <span style="font-variant: small-caps;">Définition 6 : morphisme</span>
> Soient $G,G'$ deux groupes, d'éléments neutres $e,e'$. Une application $\varphi\colon G\to G'$ est un *morphisme de groupes* si $\forall x,y\in G,\;\varphi(xy)=\varphi(x)\varphi(y)$.
> - Si $\varphi$ est bijective, c'est un *isomorphisme* ; si de plus $G'=G$, un *automorphisme*.
> - L'ensemble $\varphi^{-1}(\{e'\})$ est le *noyau* de $\varphi$, noté $\operatorname{Ker}\varphi$. L'*image* est $\varphi(G)$.
> - $\varphi$ est injectif $\iff\operatorname{Ker}\varphi=\{e\}$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration : $\varphi$ injectif $\iff\operatorname{Ker}\varphi=\{e\}$</span>
> On a toujours $\varphi(e)=e'$ (car $\varphi(e)=\varphi(e)\varphi(e)$) et $\varphi(x^{-1})=\varphi(x)^{-1}$.
> $(\Rightarrow)$ Si $\varphi(x)=e'=\varphi(e)$, l'injectivité donne $x=e$.
> $(\Leftarrow)$ Si $\varphi(x)=\varphi(y)$, alors $\varphi(xy^{-1})=e'$, donc $xy^{-1}=e$, $x=y$. $\square$

> [!info] <span style="font-variant: small-caps;">Proposition 4</span>
> Soit $\varphi\colon G\to G'$ un morphisme, $H$ et $H'$ deux sous-groupes de $G$, $G'$ respectivement.
> - $\varphi(H)$ est un sous-groupe de $G'$, distingué si $H\lhd G$ **et** $\varphi$ est surjectif.
> - $\varphi^{-1}(H')$ est un sous-groupe de $G$, distingué dans $G$ si $H'\lhd G'$.
> - En particulier $\operatorname{Ker}\varphi=\varphi^{-1}(\{e'\})$ est distingué dans $G$, et **$G/\operatorname{Ker}\varphi$ est isomorphe à $\varphi(G)$**.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> *Sous-groupes.* $\varphi(x)\varphi(y)^{-1}=\varphi(xy^{-1})$ donne la stabilité de $\varphi(H)$ ; de même $\varphi(x)\varphi(y)^{-1}\in H'\Rightarrow\varphi(xy^{-1})\in H'$ donne celle de $\varphi^{-1}(H')$ (proposition 1 du fichier I).
>
> *Distinction.* Si $H'\lhd G'$, $x\in G$, $h\in\varphi^{-1}(H')$ : $\varphi(xhx^{-1})=\varphi(x)\varphi(h)\varphi(x)^{-1}\in H'$. Si $H\lhd G$ et $\varphi$ surjectif, tout élément de $G'$ est de la forme $\varphi(x)$ et $\varphi(x)\varphi(h)\varphi(x)^{-1}=\varphi(xhx^{-1})\in\varphi(H)$.
>
> *Premier théorème d'isomorphisme.* Posons $K=\operatorname{Ker}\varphi$. L'application $\overline\varphi\colon G/K\to\varphi(G)$, $xK\mapsto\varphi(x)$ est :
> - **bien définie et injective** : $xK=yK\iff x^{-1}y\in K\iff\varphi(x)=\varphi(y)$ ;
> - **surjective** par définition ;
> - **un morphisme** : $\overline\varphi(xK\cdot yK)=\varphi(xy)=\varphi(x)\varphi(y)$. $\square$

> [!quote] <span style="font-variant: small-caps;">Remarque 5</span>
> Si $\varphi\colon G\to G'$ est un morphisme **surjectif**, alors $G'\simeq G/\operatorname{Ker}\varphi$. Cet isomorphisme est constamment utilisé dans les exercices et problèmes.

### Automorphismes intérieurs

> [!note] <span style="font-variant: small-caps;">Définition 7 : automorphisme intérieur</span>
> Soit $G$ un groupe. Pour tout $a\in G$, l'application $\varphi_a\colon G\to G,\;x\mapsto axa^{-1}$ est un automorphisme. L'ensemble $\mathcal{A}=\{\varphi_a\mid a\in G\}$, muni de la composition, est un groupe appelé *groupe des automorphismes intérieurs* de $G$, noté $\operatorname{Int}(G)$. On a $\varphi_a\circ\varphi_b=\varphi_{ab}$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> $\varphi_a(xy)=axya^{-1}=(axa^{-1})(aya^{-1})$ : morphisme. $\varphi_a\circ\varphi_b(x)=abxb^{-1}a^{-1}=\varphi_{ab}(x)$, et $\varphi_e=\mathrm{id}$, donc $\varphi_a\circ\varphi_{a^{-1}}=\mathrm{id}$ : $\varphi_a$ est bijectif. $\square$

> [!example]- <span style="font-variant: small-caps;">À retenir : $\operatorname{Int}(G)\simeq G/Z(G)$</span>
> L'application $a\mapsto\varphi_a$ est un morphisme **surjectif** de $G$ dans $\operatorname{Int}(G)$. Son noyau est $\{a\mid\forall x,\;axa^{-1}=x\}=Z(G)$. Le premier théorème d'isomorphisme donne $\operatorname{Int}(G)\simeq G/Z(G)$.

---

## 2.2. Génération d'un groupe

Dans toute cette partie, $G$ désigne un groupe dont l'élément neutre est noté $e$.

> [!note] <span style="font-variant: small-caps;">Définition 8 : sous-groupe engendré</span>
> Soit $A\subset G$. Il existe un plus petit sous-groupe $H$ de $G$ contenant $A$ (c'est l'intersection de tous les sous-groupes contenant $A$, cf. proposition 2). C'est l'ensemble des éléments de $G$ qui s'écrivent comme **produit d'éléments de $A$ et d'inverses d'éléments de $A$**. On l'appelle le sous-groupe *engendré par $A$* et on note $H=\langle A\rangle$. Si $A=\{x_1,\dots,x_n\}$, on note $H=\langle x_1,\dots,x_n\rangle$.

> [!example] <span style="font-variant: small-caps;">Exemple 4</span>
> Pour tout $a\in G$, $\langle a\rangle=\{a^m\mid m\in\mathbb{Z}\}$. Si deux éléments $a$ et $b$ **commutent**, alors $\langle a,b\rangle=\{a^mb^n\mid(m,n)\in\mathbb{Z}^2\}$.

> [!note] <span style="font-variant: small-caps;">Définition 9 : groupes monogènes, cycliques, de type fini</span>
> - $G$ est *monogène* s'il existe $a\in G$ tel que $G=\langle a\rangle$. Si de plus $G$ est fini, on dit que $G$ est *cyclique*.
> - $G$ est de *type fini* s'il existe un nombre fini d'éléments $a_1,\dots,a_n$ tels que $G=\langle a_1,\dots,a_n\rangle$. Un tel $n$-uplet est un *système de générateurs* de $G$.

> [!quote] <span style="font-variant: small-caps;">Remarque 6</span>
> - Tout groupe monogène est abélien.
> - Pour tout $n\in\mathbb{N}^\ast$, $(\mathbb{Z}/n\mathbb{Z},+)$ est cyclique (engendré par $\overline1$). De plus, **tout groupe cyclique à $n$ éléments est isomorphe à $(\mathbb{Z}/n\mathbb{Z},+)$**.
>
> > [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> > $a^ma^k=a^{m+k}=a^ka^m$ : abélien. Si $G=\langle a\rangle$ est d'ordre $n$, on a $a^n=e$ (théorème 2 ci-dessous), donc $m\mapsto a^m$ passe au quotient en $\overline m\mapsto a^m$ de $\mathbb{Z}/n\mathbb{Z}$ dans $G$ : c'est un morphisme, surjectif, entre ensembles de même cardinal $n$ : un isomorphisme. $\square$

> [!note] <span style="font-variant: small-caps;">Définition 10 : ordre d'un élément</span>
> Un élément $a$ de $G$ est dit d'**ordre $p\in\mathbb{N}^\ast$** si $\langle a\rangle$ est fini d'ordre $p$. L'ordre de $a$ est aussi **le plus petit entier naturel non nul $p$ tel que $a^p=e$**, et alors
> $$\langle a\rangle=\{e,a,\dots,a^{p-1}\}.$$

> [!tip]- <span style="font-variant: small-caps;">Pourquoi ces deux définitions coïncident</span>
> Si $\langle a\rangle$ est fini, les puissances $a^0,a^1,a^2,\dots$ ne peuvent pas toutes être distinctes : $a^i=a^j$ pour certains $i<j$, d'où $a^{j-i}=e$. Soit $p\geq1$ le plus petit entier tel que $a^p=e$. Pour $m\in\mathbb{Z}$, la division $m=pq+r$ donne $a^m=(a^p)^qa^r=a^r$ avec $0\leq r<p$, donc $\langle a\rangle=\{e,\dots,a^{p-1}\}$. Ces $p$ éléments sont deux à deux distincts (sinon $a^k=e$ avec $0<k<p$). $\square$

> [!info] <span style="font-variant: small-caps;">Théorème 2</span>
> Si $G$ est fini d'ordre $n$, alors l'ordre de tout élément de $G$ divise $n$. En particulier, tout élément $a$ de $G$ vérifie $a^n=e$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> L'ordre $p$ de $a$ est le cardinal du sous-groupe $\langle a\rangle$, qui divise $n$ par Lagrange. Si $n=pk$, $a^n=(a^p)^k=e$. $\square$

> [!info] <span style="font-variant: small-caps;">Théorème 3</span>
> Soit $a$ un élément de $G$ d'ordre $p$. On a l'équivalence $(a^q=e)\iff(p\mid q)$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> $(\Leftarrow)$ clair. $(\Rightarrow)$ On écrit $q=pk+r$, $0\leq r<p$. Alors $a^r=a^q(a^p)^{-k}=e$ et par minimalité de $p$, $r=0$. $\square$

> [!info] <span style="font-variant: small-caps;">Théorème 4</span>
> Si l'ordre de $G$ est un nombre **premier**, le groupe $G$ est cyclique, engendré par tout élément différent de l'élément neutre.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> Soit $a\neq e$. L'ordre de $a$ divise $\operatorname{Card}(G)=p$ premier et est $>1$ : il vaut $p$. Donc $\langle a\rangle$ a $p$ éléments, c'est $G$. $\square$

> [!info] <span style="font-variant: small-caps;">Proposition 5 (générateurs d'un groupe cyclique)</span>
> Si $G$ est cyclique d'ordre $n$, $G=\langle a\rangle$, alors
> $$\langle a^k\rangle=G\iff k\wedge n=1.$$
> En particulier $G$ possède exactement $\varphi(n)$ générateurs.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> $\langle a^k\rangle=G\iff a\in\langle a^k\rangle\iff\exists v\in\mathbb{Z},\;a^{kv}=a\iff\exists v,\;a^{kv-1}=e\iff\exists v,\;n\mid kv-1$ (théorème 3) $\iff\exists u,v\in\mathbb{Z},\;kv-1=un\iff k\wedge n=1$ (Bézout). $\square$

> [!info] <span style="font-variant: small-caps;">Proposition (sous-groupes d'un groupe cyclique)</span>
> Tout sous-groupe d'un groupe cyclique $G$ d'ordre $n$ est cyclique, et pour tout diviseur $d$ de $n$, $G$ a **un et un seul** sous-groupe d'ordre $d$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> On peut supposer $G=\mathbb{Z}/n\mathbb{Z}$. Un sous-groupe $H$ s'écrit $H=\pi(H')$ avec $H'=\pi^{-1}(H)$ sous-groupe de $\mathbb{Z}$ contenant $n\mathbb{Z}$ ($\pi$ : projection). D'après le lemme du fichier I, $H'=d'\mathbb{Z}$, et $n\in d'\mathbb{Z}$ force $d'\mid n$. Donc $H=\langle\overline{d'}\rangle$ est cyclique, d'ordre $n/d'$. Réciproquement à chaque diviseur $d'$ de $n$ correspond un unique sous-groupe, d'ordre $n/d'$. $\square$

---

## 2.3. Groupe symétrique

> [!note] <span style="font-variant: small-caps;">Définition 11 : groupe symétrique</span>
> Pour tout $n\in\mathbb{N}^\ast$, on note $\mathfrak{S}_n$ le groupe des permutations de $\{1,\dots,n\}$ (muni de la composition). C'est le *groupe symétrique d'indice $n$*. Si $s\in\mathfrak{S}_n$, on note $s=\begin{pmatrix}1&2&\cdots&n\\s(1)&s(2)&\cdots&s(n)\end{pmatrix}$.

> [!quote] <span style="font-variant: small-caps;">Remarque 7</span>
> $\operatorname{Card}(\mathfrak{S}_n)=n!$. (On choisit $s(1)$ de $n$ façons, $s(2)$ de $n-1$ façons, etc.) Pour $n\geq3$, $\mathfrak{S}_n$ n'est pas abélien.

> [!note] <span style="font-variant: small-caps;">Définition 12 : transposition</span>
> Pour $i\neq j$, la *transposition* $\tau_{i,j}=(i,j)$ est la permutation qui échange $i$ et $j$ et fixe tous les autres éléments.

> [!info] <span style="font-variant: small-caps;">Théorème 5</span>
> Tout élément de $\mathfrak{S}_n$ se décompose en produit de transpositions.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> Récurrence sur le nombre $m(s)$ de points **non fixés** par $s$. Si $m(s)=0$, $s=\mathrm{id}$ (produit vide). Sinon, soit $a$ avec $b=s(a)\neq a$, et $t=(a,b)$. Alors $(t\circ s)(a)=a$, et tout point fixé par $s$ l'est encore par $t\circ s$ (un point fixé par $s$ n'est ni $a$ ni $b$). Donc $m(t\circ s)<m(s)$, d'où $t\circ s=t_1\cdots t_r$ et $s=t\,t_1\cdots t_r$ (car $t^2=\mathrm{id}$). $\square$

> [!note] <span style="font-variant: small-caps;">Définition 13 : orbite</span>
> Si $s\in\mathfrak{S}_n$ et $a\in\{1,\dots,n\}$, on appelle *orbite* de $a$ suivant $s$ l'ensemble $\mathcal{O}_s(a)=\{s^k(a),\;k\in\mathbb{Z}\}$.

> [!note] <span style="font-variant: small-caps;">Définition 14 : cycle</span>
> Soit $\gamma\in\mathfrak{S}_n$. On dit que $\gamma$ est un *cycle* si, parmi les orbites $\mathcal{O}_\gamma(a)$, $1\leq a\leq n$, il n'y a **qu'une seule** orbite non réduite à un élément. Autrement dit, il existe $p\geq2$ et $a$ tels que
> $$\mathcal{O}_\gamma(a)=\{a,\gamma(a),\dots,\gamma^{p-1}(a)\}\quad\text{et}\quad\forall x\notin\mathcal{O}_\gamma(a),\;\gamma(x)=x.$$
> L'orbite $\mathcal{O}_\gamma(a)$ est le *support* du cycle, son cardinal $p$ sa *longueur*, et on note $\gamma=(a,\gamma(a),\dots,\gamma^{p-1}(a))$.

> [!example] <span style="font-variant: small-caps;">Exemple 5</span>
> - Une transposition est un cycle de longueur $2$.
> - Dans $\mathfrak{S}_5$, $s=(1,3,5)=\begin{pmatrix}1&2&3&4&5\\3&2&5&4&1\end{pmatrix}$ est un cycle de support $\{1,3,5\}$ et de longueur $3$.
> - $s=\begin{pmatrix}1&2&3&4\\2&1&4&3\end{pmatrix}$ de $\mathfrak{S}_4$ **n'est pas** un cycle (deux orbites $\{1,2\}$ et $\{3,4\}$).

> [!quote] <span style="font-variant: small-caps;">Remarque 8</span>
> - Des cycles à supports **disjoints commutent**.
> - L'ordre d'un cycle dans $\mathfrak{S}_n$ est sa longueur.
> - L'ordre d'une permutation est le **ppcm des longueurs** des cycles de sa décomposition.

> [!info] <span style="font-variant: small-caps;">Théorème 6 (décomposition en cycles disjoints)</span>
> Toute permutation $s\neq\mathrm{Id}$ se décompose de manière **unique**, à l'ordre près, en un produit de cycles dont les supports sont deux à deux disjoints.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> **Existence.** Les orbites de $s$ forment une partition de $\{1,\dots,n\}$ (relation $x\sim y\iff y=s^k(x)$). Sur une orbite $O$ de cardinal $p\geq2$, si $a\in O$, soit $p'$ le plus petit entier $\geq1$ avec $s^{p'}(a)=a$ ; alors $O=\{a,s(a),\dots,s^{p'-1}(a)\}$ donc $p'=p$ et $s$ agit sur $O$ comme le cycle $\gamma_O=(a,s(a),\dots,s^{p-1}(a))$. Alors $s=\prod_O\gamma_O$ sur les orbites non triviales.
>
> **Unicité.** Dans une décomposition $s=\gamma_1\cdots\gamma_r$ en cycles à supports disjoints, les supports des $\gamma_i$ sont exactement les orbites non triviales de $s$, et $\gamma_i$ coïncide avec $s$ sur son support. $\square$

> [!example] <span style="font-variant: small-caps;">Exemple 6</span>
> - $\begin{pmatrix}1&2&3&4\\2&1&4&3\end{pmatrix}=(1,2)(3,4)=(3,4)(1,2)$.
> - $\begin{pmatrix}1&2&3&4&5&6&7\\2&6&5&1&3&4&7\end{pmatrix}=(1,2,6,4)(3,5)=(3,5)(1,2,6,4)$.
> - Ordre de ce dernier : $\operatorname{ppcm}(4,2)=4$.

### Signature d'une permutation

> [!note] <span style="font-variant: small-caps;">Définition 15 : signature</span>
> Soit $s\in\mathfrak{S}_n$. On appelle *signature* de $s$ le nombre
> $$\varepsilon(s)=\prod_{1\leq i<j\leq n}\frac{s(j)-s(i)}{j-i}\in\{-1,1\}.$$
> Si $\varepsilon(s)=1$ (resp. $-1$), $s$ est dite *paire* (resp. *impaire*).

> [!tip]- <span style="font-variant: small-caps;">Pourquoi $\varepsilon(s)=\pm1$</span>
> Le facteur $\frac{s(j)-s(i)}{j-i}$ est inchangé par l'échange de $i$ et $j$ : le produit porte donc sur l'ensemble des **paires** $\{i,j\}$. Comme $s$ est une bijection, $\{s(i),s(j)\}$ parcourt toutes les paires une fois chacune : numérateur et dénominateur ont les mêmes valeurs absolues. Donc $|\varepsilon(s)|=1$. $\square$

> [!info] <span style="font-variant: small-caps;">Proposition 6</span>
> Si $s$ et $t$ sont deux éléments de $\mathfrak{S}_n$, alors $\varepsilon(st)=\varepsilon(s)\varepsilon(t)$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> $$\varepsilon(st)=\prod_{\{i,j\}}\frac{s(t(j))-s(t(i))}{t(j)-t(i)}\cdot\prod_{\{i,j\}}\frac{t(j)-t(i)}{j-i}.$$
> Le second produit vaut $\varepsilon(t)$. Dans le premier, $\{t(i),t(j)\}$ parcourt toutes les paires de $\{1,\dots,n\}$ une fois chacune (car $t$ est bijective), donc il vaut $\varepsilon(s)$. $\square$

> [!quote] <span style="font-variant: small-caps;">Remarque 9</span>
> - Une transposition est de signature $-1$. *(Pour $(i,j)$, $i<j$, les seuls facteurs négatifs sont $(i,j)$ et, pour $i<k<j$, $(i,k)$ et $(k,j)$ : au total $2(j-i-1)+1$, nombre impair.)*
> - $\varepsilon\colon\mathfrak{S}_n\to\{-1,1\}$ est un **morphisme de groupes**. Son noyau $\mathfrak{A}_n=\varepsilon^{-1}(\{1\})$ est un sous-groupe distingué de $\mathfrak{S}_n$, d'indice $2$ : on a $\operatorname{Card}(\mathfrak{A}_n)=n!/2$ ; c'est le *groupe alterné d'indice $n$*.

> [!info] <span style="font-variant: small-caps;">Proposition 7</span>
> La signature d'un cycle de longueur $p$ est $(-1)^{p-1}$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> $(a_1,\dots,a_p)=(a_1,a_p)(a_1,a_{p-1})\cdots(a_1,a_3)(a_1,a_2)$ est un produit de $p-1$ transpositions, chacune de signature $-1$. $\square$

> [!example]- <span style="font-variant: small-caps;">Calculer une signature en pratique</span>
> Pour $s=(1,2,6,4)(3,5)$ : $\varepsilon(s)=(-1)^{3}\cdot(-1)^{1}=+1$ : $s$ est paire.
> Règle : $\varepsilon(s)=(-1)^{n-\#\text{orbites de }s}$.

---

## 2.4. Groupe opérant sur un ensemble

Dans cette partie, $G$ désigne un groupe d'élément neutre $e$ et $X$ un ensemble quelconque.

> [!note] <span style="font-variant: small-caps;">Définition 16 : action de groupe</span>
> On dit que $G$ **opère** sur $X$ s'il existe une application $G\times X\to X,\;(s,x)\mapsto s\cdot x$ telle que
> 1. $\forall(s,t)\in G^2,\;\forall x\in X,\;s\cdot(t\cdot x)=(st)\cdot x$,
> 2. $\forall x\in X,\;e\cdot x=x$.
>
> (Analogie avec un espace vectoriel sur un corps $\mathbb{K}$.)

> [!example] <span style="font-variant: small-caps;">Exemple 7</span>
> - $G$ opère sur lui-même par translation $(s,x)\mapsto sx$.
> - $G$ opère sur lui-même par **conjugaison** $(s,x)\mapsto sxs^{-1}$ (action par automorphismes intérieurs).
> - Le groupe des permutations $S$ d'un ensemble $X$ opère sur $X$ par $(s,x)\mapsto s(x)$.

### Équivalence d'intransitivité

> [!note] <span style="font-variant: small-caps;">Définition 17 : orbite</span>
> La relation sur $X$ définie par $x\mathcal{T}y\iff\exists s\in G,\;y=s\cdot x$ est une relation d'équivalence. La classe d'un élément $x$ est son **orbite** (ou trajectoire) $\operatorname{Orb}(x)=\{s\cdot x\mid s\in G\}$.

> [!note] <span style="font-variant: small-caps;">Définition 18 : stabilisateur</span>
> Le *stabilisateur* d'un élément $x$ de $X$ est $\operatorname{Stab}(x)=\{s\in G\mid s\cdot x=x\}$.

> [!info] <span style="font-variant: small-caps;">Proposition 8</span>
> Pour tout $x\in X$, $\operatorname{Stab}(x)$ est un sous-groupe de $G$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> $e\in\operatorname{Stab}(x)$. Soient $s,t\in\operatorname{Stab}(x)$ : $t\cdot x=x$ donc $x=t^{-1}\cdot(t\cdot x)=t^{-1}\cdot x$. Alors $(st^{-1})\cdot x=s\cdot(t^{-1}\cdot x)=s\cdot x=x$, d'où $st^{-1}\in\operatorname{Stab}(x)$. $\square$

> [!info] <span style="font-variant: small-caps;">Théorème 7 (formule orbite-stabilisateur)</span>
> Si $G$ est fini, pour tout $x\in X$ on a
> $$\operatorname{Card}(G)=\operatorname{Card}(\operatorname{Orb}(x))\cdot\operatorname{Card}(\operatorname{Stab}(x)).$$

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> Posons $S=\operatorname{Stab}(x)$. L'application $\Phi\colon G/S\to\operatorname{Orb}(x)$, $tS\mapsto t\cdot x$ est :
> - **bien définie et injective** : $t\cdot x=t'\cdot x\iff t'^{-1}t\cdot x=x\iff t'^{-1}t\in S\iff tS=t'S$ ;
> - **surjective** par définition de l'orbite.
>
> Donc $\operatorname{Card}(\operatorname{Orb}(x))=[G:S]=\operatorname{Card}(G)/\operatorname{Card}(S)$ (Lagrange). $\square$

> [!info] <span style="font-variant: small-caps;">Corollaire 1 (équation aux classes)</span>
> Si $X$ et $G$ sont finis, en désignant par $\Theta$ une partie de $X$ contenant exactement un représentant de chacune des orbites, on a
> $$\operatorname{Card}(X)=\sum_{x\in\Theta}\operatorname{Card}(\operatorname{Orb}(x))=\sum_{x\in\Theta}\frac{\operatorname{Card}(G)}{\operatorname{Card}(\operatorname{Stab}(x))}.$$

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> Les orbites partitionnent $X$, et on applique le théorème 7 à chacune. $\square$

### Application aux automorphismes intérieurs

> [!info] <span style="font-variant: small-caps;">Théorème 8</span>
> Soit $G$ un groupe fini. Il existe une famille finie de sous-groupes **stricts** de $G$ (i.e. $\neq\{e\}$ et $\neq G$) $(H_i)_{i\in I}$ telle que
> $$\operatorname{Card}(G)=\operatorname{Card}(Z(G))+\sum_{i\in I}\frac{\operatorname{Card}(G)}{\operatorname{Card}(H_i)},$$
> où $Z(G)$ désigne le centre de $G$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> On fait opérer $G$ sur lui-même par conjugaison : $s\cdot x=sxs^{-1}$. Le stabilisateur de $x$ est $\operatorname{Stab}(x)=\{s\mid sx=xs\}$ (le *centralisateur* de $x$). Soit $\Theta$ un système de représentants des orbites (classes de conjugaison).
>
> Or $\operatorname{Stab}(x)=G\iff\forall s,\;sx=xs\iff x\in Z(G)$, et alors l'orbite de $x$ est $\{x\}$ (taille $1$). Notons $\Theta'=\Theta\setminus Z(G)$. L'équation aux classes devient
> $$\operatorname{Card}(G)=\sum_{x\in\Theta\cap Z(G)}1+\sum_{x\in\Theta'}\frac{\operatorname{Card}(G)}{\operatorname{Card}(\operatorname{Stab}(x))}=\operatorname{Card}(Z(G))+\sum_{x\in\Theta'}\frac{\operatorname{Card}(G)}{\operatorname{Card}(\operatorname{Stab}(x))}.$$
> Pour $x\in\Theta'$, $\operatorname{Stab}(x)$ est un sous-groupe de $G$ (prop. 8), $\neq G$ car $x\notin Z(G)$, et $\neq\{e\}$ car il contient $\{e,x\}$ avec $x\neq e$ ($e\in Z(G)$). $\square$

> [!quote] <span style="font-variant: small-caps;">Remarque 10</span>
> Ce résultat est très puissant : il donne des renseignements sur $\operatorname{Card}(Z(G))$ en connaissant *a priori* la forme des ordres des sous-groupes de $G$ (exercice 11, par exemple). Cette formule n'est pas au programme de mathématiques spéciales : il faut savoir la redémontrer.

---

## 2.5. Exercices

### Exercices du cours (avec solutions)

> [!question]- <span style="font-variant: small-caps;">Exercice 1 ★ : $xy$ et $yx$ ont même ordre</span>
> Soient $x,y\in G$. On suppose $xy$ d'ordre fini $p$. Montrer que $yx$ est également d'ordre fini $p$.
>
> > [!todo]- 💡 Indice
> > Calculer $y(xy)^ny^{-1}$.
>
> > [!success]- Solution
> > Pour tout $n\in\mathbb{N}^\ast$, $(yx)^n=y(xy)^ny^{-1}$ (on développe : $y\,xy\,xy\cdots xy\,y^{-1}=yx\,yx\cdots yx$). Donc $(yx)^n=e\iff(xy)^n=e$ (la conjugaison est bijective et fixe $e$). Les deux éléments ont donc le même plus petit exposant $n$ : le même ordre.

> [!question]- <span style="font-variant: small-caps;">Exercice 2 ★ : réunion de sous-groupes</span>
> Soient $H_1,H_2$ deux sous-groupes de $G$.
> a) On suppose que $H_1\cup H_2$ est un sous-groupe. Montrer que $H_1\subset H_2$ ou $H_2\subset H_1$.
> b) Si les ordres de $H_1$ et $H_2$ sont finis et premiers entre eux, que dire de $H_1\cap H_2$ ?
>
> > [!success]- Solution
> > **a)** Par l'absurde : il existe $x_1\in H_1\setminus H_2$ et $x_2\in H_2\setminus H_1$. Comme $H_1\cup H_2$ est un sous-groupe, $x_1x_2\in H_1\cup H_2$. Si $x_1x_2\in H_1$, alors $x_2=x_1^{-1}(x_1x_2)\in H_1$, absurde. Si $x_1x_2\in H_2$, alors $x_1=(x_1x_2)x_2^{-1}\in H_2$, absurde.
> >
> > **b)** $H_1\cap H_2$ est un sous-groupe de $H_1$ et de $H_2$ : par Lagrange, son ordre divise $\operatorname{Card}(H_1)$ et $\operatorname{Card}(H_2)$, donc divise leur pgcd $1$. Donc $H_1\cap H_2=\{e\}$.

> [!question]- <span style="font-variant: small-caps;">Exercice 3 ★★ : produit de sous-groupes</span>
> Soient $H_1,H_2$ deux sous-groupes de $G$. On pose $H_1H_2=\{xy\mid x\in H_1,y\in H_2\}$.
> a) À quelle condition nécessaire et suffisante $H_1H_2$ est-il un sous-groupe de $G$ ?
> b) Si $H_1$ et $H_2$ sont finis et $H_1\cap H_2=\{e\}$, montrer que $\operatorname{Card}(H_1H_2)=\operatorname{Card}(H_1)\operatorname{Card}(H_2)$.
> c) On suppose $G$ abélien, $H_1,H_2$ d'ordres finis $p$ et $q$, deux nombres premiers distincts. Montrer que $H_1H_2$ est cyclique.
>
> > [!todo]- 💡 Indice
> > a) Une partie $S$ non vide est un sous-groupe ssi $S=S^{-1}$ et $SS\subset S$. Que vaut $(H_1H_2)^{-1}$ ?
> > c) Considérer $xy$ avec $x$ d'ordre $p$, $y$ d'ordre $q$.
>
> > [!success]- Solution
> > **a)** *Réponse : $H_1H_2$ est un sous-groupe $\iff H_1H_2=H_2H_1$.*
> > *Nécessaire.* Supposons $H_1H_2$ sous-groupe. Si $a\in H_1H_2$, alors $a^{-1}\in H_1H_2$, donc $a^{-1}=xy$ avec $x\in H_1,y\in H_2$, d'où $a=y^{-1}x^{-1}\in H_2H_1$ : $H_1H_2\subset H_2H_1$. Réciproquement si $a=yx\in H_2H_1$, alors $a^{-1}=x^{-1}y^{-1}\in H_1H_2$, donc $a\in H_1H_2$ (stable par inverse) : $H_2H_1\subset H_1H_2$. D'où l'égalité.
> > *Suffisante.* $H_1H_2\neq\varnothing$. Soient $a=a_1a_2$, $b=b_1b_2$. Alors $ab^{-1}=a_1(a_2b_2^{-1})b_1^{-1}$, avec $a_2b_2^{-1}b_1^{-1}\in H_2H_1=H_1H_2$ : il s'écrit $x'y'$, $(x',y')\in H_1\times H_2$. Donc $ab^{-1}=(a_1x')y'\in H_1H_2$.
> >
> > **b)** $\varphi\colon H_1\times H_2\to H_1H_2$, $(x_1,x_2)\mapsto x_1x_2$ est surjective. Elle est injective : si $x_1x_2=y_1y_2$ alors $y_1^{-1}x_1=y_2x_2^{-1}\in H_1\cap H_2=\{e\}$, donc $x_1=y_1$, $x_2=y_2$. D'où le résultat (cardinal d'un produit cartésien).
> >
> > **c)** $G$ étant abélien, $H_1H_2=H_2H_1$ est un sous-groupe, d'ordre $pq$ (b, car $H_1\cap H_2=\{e\}$ par l'exercice 2). Ils sont cycliques d'ordre premier : $H_1=\langle x\rangle$, $H_2=\langle y\rangle$. Soit $n$ avec $(xy)^n=e$. Alors $x^n=(y^{-1})^n\in H_1\cap H_2=\{e\}$, donc $p\mid n$ et $q\mid n$, donc $pq\mid n$ ($p\wedge q=1$). Ainsi $xy$ est d'ordre $\geq pq$ et au plus $\operatorname{Card}(H_1H_2)=pq$ : il engendre $H_1H_2$.

> [!question]- <span style="font-variant: small-caps;">Exercice 4 ★★ : produit de groupes cycliques</span>
> Soient $G_1,\dots,G_n$ des groupes cycliques d'ordres $\alpha_1,\dots,\alpha_n$. Donner une condition nécessaire et suffisante sur les $\alpha_i$ pour que $G_1\times\cdots\times G_n$ soit cyclique.
>
> > [!todo]- 💡 Indice
> > Calculer l'ordre de $(x_1,\dots,x_n)$ en fonction des ordres des $x_i$.
>
> > [!success]- Solution
> > **Lemme.** Si $x_i\in G_i$ est d'ordre $\beta_i$, alors $x=(x_1,\dots,x_n)$ est d'ordre $\operatorname{ppcm}(\beta_1,\dots,\beta_n)$. *Preuve :* $x^p=e\iff\forall i,\;x_i^p=e_i\iff\forall i,\;\beta_i\mid p$ : le plus petit $p$ est le ppcm.
> >
> > **Résultat :** $G=\prod G_i$ est cyclique $\iff$ **les $\alpha_i$ sont premiers entre eux deux à deux**.
> > $(\Rightarrow)$ Soit $x$ un générateur de $G$. Chaque $x_i$ engendre $G_i$ donc est d'ordre $\alpha_i$. Alors l'ordre de $x$ est $\operatorname{ppcm}(\alpha_i)$, et c'est aussi $\operatorname{Card}(G)=\prod\alpha_i$. Or $\operatorname{ppcm}=\prod$ ssi les $\alpha_i$ sont premiers deux à deux.
> > $(\Leftarrow)$ Prenons $x_i$ générateur de $G_i$. Alors $x$ est d'ordre $\operatorname{ppcm}(\alpha_i)=\prod\alpha_i=\operatorname{Card}(G)$ : $G=\langle x\rangle$.

> [!question]- <span style="font-variant: small-caps;">Exercice 5 ★★ : groupes d'exposant 2</span>
> Soit $G$ un groupe tel que tout élément vérifie $x^2=e$.
> a) Montrer que $G$ est abélien.
> b) Si $G$ est fini et $G\neq\{e\}$, montrer qu'il existe $n$ tel que $G\simeq((\mathbb{Z}/2\mathbb{Z})^n,+)$.
>
> > [!success]- Solution
> > **a)** $x^2=e\Rightarrow x=x^{-1}$. Donc $xy=(xy)^{-1}=y^{-1}x^{-1}=yx$.
> >
> > **b)** *Version rapide :* $G$ abélien noté additivement avec $2x=0$ est un $\mathbb{F}_2$-espace vectoriel de dimension finie $n$, donc $\simeq\mathbb{F}_2^n$.
> > *Version élémentaire :* soit $(x_1,\dots,x_n)$ un système générateur **minimal**. Comme $x_i^2=e$, $\alpha\mapsto x_1^{\alpha_1}\cdots x_n^{\alpha_n}$ est bien défini sur $(\mathbb{Z}/2\mathbb{Z})^n$ ; c'est un morphisme (car $G$ abélien), surjectif. Injectif : si le noyau contenait un $(\dot\alpha_i)\neq0$, par exemple avec $\dot\alpha_n=\dot1$, on aurait $x_n=x_1^{-\alpha_1}\cdots x_{n-1}^{-\alpha_{n-1}}$, donc $(x_1,\dots,x_{n-1})$ engendrerait $G$, contredisant la minimalité.

> [!question]- <span style="font-variant: small-caps;">Exercice 6 ★★ : transpositions $(i,i+1)$</span>
> Soit $n\geq2$. Montrer que tout élément de $\mathfrak{S}_n$ s'écrit comme produit de transpositions de la forme $(i,i+1)$, $1\leq i\leq n-1$.
>
> > [!todo]- 💡 Indice
> > Conjuguer $(i,j-1)$ par $(j-1,j)$.
>
> > [!success]- Solution
> > D'après le théorème 5, il suffit de montrer que toute transposition $(i,j)$, $i<j$, est produit de transpositions adjacentes. On procède par récurrence sur $j-i$. Si $j-i=1$, c'est évident. Si $j-i\geq2$,
> > $$(i,j)=(j-1,j)\,(i,j-1)\,(j-1,j),$$
> > (conjuguer par $(j-1,j)$ échange les « étiquettes » $j-1$ et $j$ dans $(i,j-1)$). Par hypothèse de récurrence, $(i,j-1)$ est un produit de transpositions adjacentes. $\square$

> [!question]- <span style="font-variant: small-caps;">Exercice 7 ★★ : les 3-cycles engendrent $\mathfrak{A}_n$</span>
> Pour $n\geq3$, montrer que les cycles de longueur $3$ engendrent $\mathfrak{A}_n$.
>
> > [!success]- Solution
> > Soit $\mathfrak{A}'_n$ le sous-groupe engendré par les 3-cycles. Un 3-cycle est de signature $+1$ (prop. 7) : $\mathfrak{A}'_n\subset\mathfrak{A}_n$.
> > Réciproquement, un élément de $\mathfrak{A}_n$ est un produit d'un nombre **pair** de transpositions (thm 5 et signature) : il suffit de montrer que le produit de deux transpositions est dans $\mathfrak{A}'_n$.
> > - $i,j,k,l$ distincts : $(i,j)(k,l)=(i,j,k)(j,k,l)$.
> > - $i,j,k$ distincts : $(i,j)(i,k)=(i,k,j)$.
> > - $(i,j)(i,j)=\mathrm{id}$.

> [!question]- <span style="font-variant: small-caps;">Exercice 8 ★★★ : sous-groupes de $\mathfrak{S}_p$ de petit indice</span>
> Soit $p\geq5$ premier et $H$ un sous-groupe de $\mathfrak{S}_p$ tel que $[\mathfrak{S}_p:H]\leq p-1$. Montrer que $[\mathfrak{S}_p:H]\in\{1,2\}$.
>
> > [!todo]- 💡 Indice
> > Montrer d'abord que $H$ contient tous les $p$-cycles (principe des tiroirs sur les classes $\gamma^iH$), puis tous les 3-cycles, puis utiliser l'exercice 7.
>
> > [!success]- Solution
> > **Étape 1 : $H$ contient tous les $p$-cycles.** Soit $\gamma$ un $p$-cycle. Les $p$ ensembles $H,\gamma H,\dots,\gamma^{p-1}H$ sont des classes à gauche, et il y a au plus $p-1$ classes distinctes : deux coïncident, $\gamma^iH=\gamma^jH$ avec $0\leq i<j\leq p-1$, d'où $\gamma^{j-i}\in H$. Comme $p$ est premier et $0<j-i<p$, $\gamma^{j-i}$ est aussi un $p$-cycle qui engendre $\langle\gamma\rangle$ (théorème 4) : $\gamma\in H$.
> >
> > **Étape 2 : $H$ contient les 3-cycles.** Pour $i,j,k,a_1,\dots,a_{p-3}$ distincts, on vérifie
> > $$(i,j,k)=(k,j,i,a_1,\dots,a_{p-3})\;(i,k,j,a_{p-3},\dots,a_1),$$
> > produit de deux $p$-cycles, donc dans $H$.
> >
> > **Conclusion.** $H\supset\mathfrak{A}_p$ (exercice 7), donc $[\mathfrak{S}_p:H]$ divise $[\mathfrak{S}_p:\mathfrak{A}_p]=2$. $\square$
>
> > [!quote]- Remarque
> > Pour $p=5$, il n'existe donc aucun sous-groupe de $\mathfrak{S}_5$ d'ordre $30$ ou $40$ (indices $4$ et $3$), bien que $30$ et $40$ divisent $120$. La réciproque de Lagrange est fausse.

> [!question]- <span style="font-variant: small-caps;">Exercice 9 ★★★ : groupes d'ordre $2n$</span>
> Soit $G$ un groupe fini d'ordre pair $2n$.
> a) Soit $H$ un sous-groupe d'ordre $n$. Montrer que $H\lhd G$.
> b) Soient $H_1,H_2$ deux sous-groupes d'ordre $n$ avec $H_1\cap H_2=\{e\}$. Montrer que $n=1$ ou $n=2$.
> c) Soient $H_1\neq H_2$ deux sous-groupes d'ordre $n$. Montrer que $H=H_1\cap H_2\lhd G$ et que $4\mid\operatorname{Card}(G)$.
>
> > [!todo]- 💡 Indice
> > a) Il y a deux classes à gauche. b) $\operatorname{Card}(H_1\cup H_2)=2n-1$ : il reste un unique élément $\alpha$. Montrer que $xy=\alpha$ pour tout $(x,y)\in(H_1\setminus\{e\})\times(H_2\setminus\{e\})$. c) Passer au quotient $G/H$.
>
> > [!success]- Solution
> > **a)** $H$ est d'indice $2$ : les classes à gauche sont $H$ et $G\setminus H$, de même les classes à droite. Pour $x\in H$, $xH=H=Hx$. Pour $x\notin H$, $xH\neq H$ (sinon $x\in H$), donc $xH=G\setminus H=Hx$.
> >
> > **b)** $\operatorname{Card}(H_1\cup H_2)=2n-1$, donc il existe $\alpha\notin H_1\cup H_2$ et $G=H_1\cup H_2\cup\{\alpha\}$. Soit $(x,y)\in(H_1\setminus\{e\})\times(H_2\setminus\{e\})$. Si $xy\in H_1$, alors $y\in H_1\cap H_2=\{e\}$ : absurde. Si $xy\in H_2$, alors $x=e$ : absurde. Donc $xy=\alpha$. Mais l'application $(x,y)\mapsto xy$ est injective (si $xy=x'y'$, $x'^{-1}x=y'y^{-1}\in H_1\cap H_2=\{e\}$). Donc $(n-1)^2\leq1$, d'où $n\leq2$.
> >
> > **c)** Par a), $H_1,H_2\lhd G$, donc $H=H_1\cap H_2\lhd G$. Dans $G/H$ (d'ordre $2n/h$ avec $h=\operatorname{Card}(H)$), les sous-groupes $H_1/H$ et $H_2/H$ sont distincts, d'ordre $n/h$ (donc de moitié de $\operatorname{Card}(G/H)$), d'intersection $(H_1\cap H_2)/H$ triviale. Par b), $n/h\in\{1,2\}$. Comme $H_1\neq H_2$, $h<n$, donc $n/h=2$ et $\operatorname{Card}(G)=2n=4h$.

> [!question]- <span style="font-variant: small-caps;">Exercice 10 ★★★ : exposant d'un groupe abélien fini</span>
> Soit $G$ un groupe abélien fini.
> a) Si $x,y\in G$ sont d'ordres respectifs $m,n$ avec $m\wedge n=1$, quel est l'ordre de $xy$ ?
> b) On appelle *exposant* de $G$ le plus grand $r$ des ordres des éléments de $G$. Montrer que $r$ divise $\operatorname{Card}(G)$ et que l'ordre de tout $x\in G$ divise $r$.
> c) Montrer que $r$ a les mêmes facteurs premiers que $\operatorname{Card}(G)$. En déduire que pour tout facteur premier $p$ de $\operatorname{Card}(G)$, il existe un élément de $G$ d'ordre $p$.
>
> > [!todo]- 💡 Indice
> > b) Si l'ordre $q$ de $y$ ne divise pas $r$, trouver un nombre premier $p$ avec $v_p(q)>v_p(r)$ et fabriquer, avec a), un élément d'ordre $>r$.
>
> > [!success]- Solution
> > **a)** L'ordre de $xy$ est $mn$. En effet, si $(xy)^p=e$, alors $x^p=(y^{-1})^p\in\langle x\rangle\cap\langle y\rangle=\{e\}$ (ordres premiers entre eux), donc $m\mid p$ et $n\mid p$, donc $mn\mid p$. Et $(xy)^{mn}=e$.
> >
> > **b)** $r$ est l'ordre d'un élément, donc divise $\operatorname{Card}(G)$ (thm 2). Soient $x$ d'ordre $r$ et $y$ d'ordre $q$. Si $q\nmid r$, il existe un premier $p$ avec $q=p^\alpha q'$, $r=p^\beta r'$, $\alpha>\beta\geq0$, $p\nmid q'r'$. Alors $a=x^{p^\beta}$ est d'ordre $r'$ et $b=y^{q'}$ est d'ordre $p^\alpha$, premiers entre eux. Par a), $ab$ est d'ordre $r'p^\alpha>r'p^\beta=r$ : contradiction avec la maximalité de $r$. Donc $q\mid r$.
> >
> > **c)** Soit $(x_1,\dots,x_n)$ un système de générateurs, d'ordres $r_1,\dots,r_n$. L'application $\varphi\colon\langle x_1\rangle\times\cdots\times\langle x_n\rangle\to G$, $(y_i)\mapsto y_1\cdots y_n$ est un morphisme (car $G$ abélien), surjectif. Donc $G\simeq(\prod\langle x_i\rangle)/\operatorname{Ker}\varphi$ et $\operatorname{Card}(G)$ divise $r_1\cdots r_n$, qui divise $r^n$ d'après b). Tout facteur premier de $\operatorname{Card}(G)$ divise donc $r$ ; réciproquement $r\mid\operatorname{Card}(G)$. Si $p\mid\operatorname{Card}(G)$, alors $p\mid r$, $r=pr'$, et si $x$ est d'ordre $r$, $x^{r'}$ est d'ordre $p$.
>
> > [!quote]- Conséquence importante
> > Si $\mathbb{K}$ est un corps commutatif et $G$ un sous-groupe **fini** de $(\mathbb{K}^\ast,\times)$, alors $G$ est cyclique (voir exercice 17). En particulier $(\mathbb{Z}/p\mathbb{Z})^\ast$ est cyclique pour $p$ premier : résultat non évident *a priori*.

> [!question]- <span style="font-variant: small-caps;">Exercice 11 ★★★ : les $p$-groupes</span>
> Soit $p$ premier et $G$ un groupe fini d'ordre $p^\alpha$, $\alpha\in\mathbb{N}^\ast$ (on dit que $G$ est un $p$-groupe).
> a) Montrer que $Z(G)\neq\{e\}$.
> b) Que dire si $\alpha=1$ ? si $\alpha=2$ ?
> c) Montrer que pour tout entier $m$, $0\leq m\leq\alpha$, il existe un sous-groupe de $G$ d'ordre $p^m$.
>
> > [!todo]- 💡 Indice
> > a) Équation aux classes. b) Pour $\alpha=2$ : si $Z(G)$ est d'ordre $p$, prendre $x\notin Z(G)$ et considérer $\operatorname{Stab}(x)=\{u\mid ux=xu\}$. c) Récurrence en quotientant par un sous-groupe d'ordre $p$ du centre.
>
> > [!success]- Solution
> > **a)** Théorème 8 : $\operatorname{Card}(G)=\operatorname{Card}(Z(G))+\sum_i\operatorname{Card}(G)/\operatorname{Card}(H_i)$, où $H_i$ est un sous-groupe strict, donc d'ordre $p^{\beta_i}$ avec $1\leq\beta_i<\alpha$ (Lagrange). Chaque $\operatorname{Card}(G)/\operatorname{Card}(H_i)=p^{\alpha-\beta_i}$ est divisible par $p$, ainsi que $\operatorname{Card}(G)$. Donc $p\mid\operatorname{Card}(Z(G))$ ; comme $e\in Z(G)$, on a $\operatorname{Card}(Z(G))\geq p$.
> >
> > **b)** Si $\alpha=1$, $G$ est cyclique (thm 4). Si $\alpha=2$, $Z(G)$ est d'ordre $p$ ou $p^2$. Supposons $\operatorname{Card}(Z(G))=p$ : soit $x\notin Z(G)$ et $S_x=\{u\mid ux=xu\}$, sous-groupe contenant $x$ et $Z(G)$, donc $\operatorname{Card}(S_x)\geq p+1$ ; comme il divise $p^2$, $S_x=G$, d'où $x\in Z(G)$ : contradiction. Donc $Z(G)=G$ : **tout groupe d'ordre $p^2$ est abélien.**
> >
> > **c)** Récurrence sur $\alpha$ ($\alpha=1$ évident). Pour $\alpha\geq2$ : $Z(G)\neq\{e\}$, soit $z\neq e$ dans $Z(G)$ d'ordre $p^k$ ; $z_1=z^{p^{k-1}}$ est d'ordre $p$. Le sous-groupe $N=\langle z_1\rangle$ est **distingué** (il est dans le centre) d'ordre $p$. $G/N$ est d'ordre $p^{\alpha-1}$ : par hypothèse de récurrence il a des sous-groupes d'ordre $p^{m'}$, $0\leq m'\leq\alpha-1$. Leurs images réciproques par la projection $G\to G/N$ sont des sous-groupes de $G$ d'ordre $p^{m'+1}$. Avec $\{e\}$ ($m=0$), on obtient tous les ordres $p^m$.

### Exercices de niveau agrégation

> [!tip] <span style="font-variant: small-caps;">Mode d'emploi</span>
> Essaie chaque exercice sur papier **avant** d'ouvrir l'indice. Ces exercices sont des classiques des leçons d'agrégation (leçons sur les groupes, actions de groupe, groupe symétrique).

> [!question]- <span style="font-variant: small-caps;">Exercice 12 ★★★ : théorème de Cauchy</span>
> Soit $G$ un groupe fini et $p$ un nombre premier divisant $\operatorname{Card}(G)$. Montrer que $G$ possède un élément d'ordre $p$.
>
> > [!todo]- 💡 Indice (preuve de McKay)
> > Considérer $X=\{(x_1,\dots,x_p)\in G^p\mid x_1x_2\cdots x_p=e\}$ et l'action de $\mathbb{Z}/p\mathbb{Z}$ par décalage circulaire. Compter $\operatorname{Card}(X)$ modulo $p$ en utilisant la taille des orbites.
>
> > [!success]- Solution
> > 1. $\operatorname{Card}(X)=\operatorname{Card}(G)^{p-1}$ : on choisit librement $x_1,\dots,x_{p-1}$, puis $x_p=(x_1\cdots x_{p-1})^{-1}$ est imposé. Donc $p\mid\operatorname{Card}(X)$.
> > 2. $\mathbb{Z}/p\mathbb{Z}$ opère sur $X$ par $\overline1\cdot(x_1,\dots,x_p)=(x_2,\dots,x_p,x_1)$. C'est bien à valeurs dans $X$ : $x_2\cdots x_px_1=x_1^{-1}(x_1x_2\cdots x_p)x_1=e$.
> > 3. Par la formule orbite-stabilisateur, chaque orbite a pour cardinal un diviseur de $p$ : $1$ ou $p$. Soit $F$ l'ensemble des points fixes (orbites de taille 1). Alors $\operatorname{Card}(X)\equiv\operatorname{Card}(F)\pmod p$, donc $p\mid\operatorname{Card}(F)$.
> > 4. Un point fixe est un $p$-uplet constant $(x,\dots,x)$ avec $x^p=e$. Or $(e,\dots,e)\in F$ donc $\operatorname{Card}(F)\geq1$, et étant multiple de $p$, $\operatorname{Card}(F)\geq p\geq2$. Il existe donc $x\neq e$ avec $x^p=e$ : $x$ est d'ordre $p$ (car $p$ premier). $\square$

> [!question]- <span style="font-variant: small-caps;">Exercice 13 ★★★ : groupes d'ordre $2p$</span>
> Soit $p\geq3$ premier et $G$ un groupe d'ordre $2p$. Montrer que $G$ est cyclique, ou bien qu'il existe $a,b\in G$ avec $a$ d'ordre $p$, $b$ d'ordre $2$ et $bab^{-1}=a^{-1}$ (groupe diédral $D_p$).
>
> > [!todo]- 💡 Indice
> > Cauchy donne $a$ et $b$. Utiliser l'exercice 9 a) pour $\langle a\rangle$, puis calculer $bab^{-1}=a^k$ et élever au carré.
>
> > [!success]- Solution
> > Par Cauchy (ex. 12), il existe $a$ d'ordre $p$ et $b$ d'ordre $2$. Le sous-groupe $\langle a\rangle$ est d'indice $2$, donc distingué (ex. 9a), et $b\notin\langle a\rangle$ (car $2\nmid p$). Ainsi $G=\langle a\rangle\cup\langle a\rangle b$.
> > Comme $\langle a\rangle\lhd G$, $bab^{-1}=a^k$ pour un $k$. En répétant l'opération, $a=b^2ab^{-2}=b(a^k)b^{-1}=(bab^{-1})^k=a^{k^2}$, d'où $p\mid k^2-1=(k-1)(k+1)$, donc $k\equiv\pm1\pmod p$ ($p$ premier).
> > - Si $k\equiv1$ : $a$ et $b$ commutent, donc $ab$ est d'ordre $\operatorname{ppcm}(p,2)=2p$ : $G$ est cyclique.
> > - Si $k\equiv-1$ : $bab^{-1}=a^{-1}$ : $G\simeq D_p$.

> [!question]- <span style="font-variant: small-caps;">Exercice 14 ★★ : $(1\,2)$ et $(1\,2\cdots n)$ engendrent $\mathfrak{S}_n$</span>
> Montrer que $\mathfrak{S}_n$ est engendré par $\tau=(1,2)$ et $c=(1,2,\dots,n)$.
>
> > [!todo]- 💡 Indice
> > Calculer $c^k\tau c^{-k}$ et utiliser l'exercice 6.
>
> > [!success]- Solution
> > Pour $\sigma\in\mathfrak{S}_n$, $\sigma(a_1,\dots,a_r)\sigma^{-1}=(\sigma(a_1),\dots,\sigma(a_r))$. Donc $c^k\tau c^{-k}=(c^k(1),c^k(2))=(k+1,k+2)$ pour $0\leq k\leq n-2$. Le sous-groupe $\langle\tau,c\rangle$ contient donc toutes les transpositions adjacentes, donc $\mathfrak{S}_n$ tout entier (ex. 6).

> [!question]- <span style="font-variant: small-caps;">Exercice 15 ★★ : centre de $\mathfrak{S}_n$</span>
> Montrer que $Z(\mathfrak{S}_n)=\{\mathrm{id}\}$ pour $n\geq3$.
>
> > [!todo]- 💡 Indice
> > Si $s\neq\mathrm{id}$, trouver une transposition qui ne commute pas avec $s$.
>
> > [!success]- Solution
> > Soit $s\neq\mathrm{id}$ : il existe $i$ avec $j=s(i)\neq i$. Comme $n\geq3$, choisissons $k\notin\{i,j\}$ et $t=(i,k)$. Si $s$ commutait avec $t$, on aurait $s=tst^{-1}$, donc $s(k)=tst^{-1}(k)=t(s(i))=t(j)=j=s(i)$ (car $j\notin\{i,k\}$), et l'injectivité de $s$ donnerait $k=i$ : absurde. Donc $s\notin Z(\mathfrak{S}_n)$.

> [!question]- <span style="font-variant: small-caps;">Exercice 16 ★★★ : lemme de Burnside</span>
> Soit $G$ un groupe fini opérant sur un ensemble fini $X$. Pour $g\in G$, on note $\operatorname{Fix}(g)=\{x\in X\mid g\cdot x=x\}$. Montrer que le nombre d'orbites vaut
> $$N=\frac1{\operatorname{Card}(G)}\sum_{g\in G}\operatorname{Card}(\operatorname{Fix}(g)).$$
> *Application :* combien y a-t-il de colliers distincts de $6$ perles, chacune blanche ou noire, à rotation près ?
>
> > [!todo]- 💡 Indice
> > Compter de deux façons l'ensemble $\{(g,x)\in G\times X\mid g\cdot x=x\}$. Utiliser la formule orbite-stabilisateur.
>
> > [!success]- Solution
> > **Preuve.** Soit $E=\{(g,x)\mid g\cdot x=x\}$. En sommant d'abord sur $g$ : $\operatorname{Card}(E)=\sum_g\operatorname{Card}(\operatorname{Fix}(g))$. En sommant d'abord sur $x$ : $\operatorname{Card}(E)=\sum_x\operatorname{Card}(\operatorname{Stab}(x))=\sum_x\frac{\operatorname{Card}(G)}{\operatorname{Card}(\operatorname{Orb}(x))}$ (thm 7). Or sur une orbite $O$, $\sum_{x\in O}\frac1{\operatorname{Card}(O)}=1$ : donc $\sum_{x\in X}\frac1{\operatorname{Card}(\operatorname{Orb}(x))}=N$. D'où $\operatorname{Card}(E)=N\operatorname{Card}(G)$. $\square$
> >
> > **Application.** $G=\mathbb{Z}/6\mathbb{Z}$ opère par rotation sur $X=\{\text{blanc},\text{noir}\}^6$ (64 éléments). La rotation de $k$ crans a $\gcd(k,6)$ cycles sur les positions, donc $2^{\gcd(k,6)}$ points fixes :
> > $$N=\frac{2^6+2^1+2^2+2^3+2^2+2^1}{6}=\frac{64+2+4+8+4+2}{6}=\frac{84}{6}=14.$$
> > Il y a **14 colliers**.

> [!question]- <span style="font-variant: small-caps;">Exercice 17 ★★★ : sous-groupes finis de $\mathbb{K}^\ast$</span>
> Soit $\mathbb{K}$ un corps commutatif et $G$ un sous-groupe **fini** de $(\mathbb{K}^\ast,\times)$. Montrer que $G$ est cyclique. En déduire que $(\mathbb{Z}/p\mathbb{Z})^\ast$ est cyclique pour $p$ premier.
>
> > [!todo]- 💡 Indice
> > Appliquer l'exercice 10 : soit $r$ l'exposant de $G$. Que dire du polynôme $X^r-1$ ?
>
> > [!success]- Solution
> > $G$ est abélien fini ; soit $r$ son exposant. Pour tout $x\in G$, l'ordre de $x$ divise $r$ (ex. 10b), donc $x^r=1$ : les $\operatorname{Card}(G)$ éléments de $G$ sont des racines de $X^r-1\in\mathbb{K}[X]$, qui a **au plus $r$ racines** (corps). Donc $\operatorname{Card}(G)\leq r$. Comme $r\mid\operatorname{Card}(G)$, $r=\operatorname{Card}(G)$. Mais $r$ est l'ordre d'un élément $x$ : $\langle x\rangle$ est d'ordre $\operatorname{Card}(G)$, donc $G=\langle x\rangle$ est cyclique. L'application à $\mathbb{K}=\mathbb{Z}/p\mathbb{Z}$ (corps, prop. 10 du fichier I) donne le résultat. $\square$

> [!question]- <span style="font-variant: small-caps;">Exercice 18 ★★ : automorphismes de $\mathbb{Z}/n\mathbb{Z}$</span>
> Montrer que $\operatorname{Aut}(\mathbb{Z}/n\mathbb{Z},+)\simeq((\mathbb{Z}/n\mathbb{Z})^\ast,\times)$. En déduire le nombre de générateurs de $\mathbb{Z}/n\mathbb{Z}$.
>
> > [!success]- Solution
> > Un endomorphisme $f$ de $\mathbb{Z}/n\mathbb{Z}$ est déterminé par $f(\overline1)=\overline k$ : $f(\overline m)=m\overline k=\overline k\,\overline m$. Il est **bijectif** ssi $f(\overline1)$ engendre $\mathbb{Z}/n\mathbb{Z}$, ssi $k\wedge n=1$ (prop. 5), ssi $\overline k$ est inversible. L'application $f\mapsto f(\overline1)$ est un morphisme de $(\operatorname{Aut},\circ)$ dans $((\mathbb{Z}/n\mathbb{Z})^\ast,\times)$ : $f_k\circ f_l=f_{kl}$. C'est un isomorphisme. Le nombre de générateurs est $\operatorname{Card}((\mathbb{Z}/n\mathbb{Z})^\ast)=\varphi(n)$.

> [!question]- <span style="font-variant: small-caps;">Exercice 19 ★★ : si $G/Z(G)$ est monogène</span>
> Montrer que si $G/Z(G)$ est cyclique, alors $G$ est abélien.
>
> > [!todo]- 💡 Indice
> > Écrire un élément de $G$ comme $g^kz$ avec $z\in Z(G)$.
>
> > [!success]- Solution
> > Soit $gZ(G)$ un générateur de $G/Z(G)$. Tout $x\in G$ s'écrit $x=g^kz$ avec $z\in Z(G)$, $k\in\mathbb{Z}$. Pour $x=g^kz$ et $y=g^lz'$ : $xy=g^kzg^lz'=g^{k+l}zz'$ et $yx=g^lz'g^kz=g^{k+l}z'z$. Comme $zz'=z'z$ (ils sont centraux), $xy=yx$. $\square$
>
> > [!quote]- Conséquence
> > Un groupe d'ordre $p^2$ est abélien (retrouve l'exercice 11b) : $\operatorname{Card}(Z(G))\in\{p,p^2\}$, et si c'était $p$, $G/Z(G)$ serait d'ordre $p$ donc cyclique, donc $G$ abélien, donc $Z(G)=G$ : contradiction.

---

## 2.6. Point de vue structurel (Bourbaki) et catégorique

> [!abstract]- <span style="font-variant: small-caps;">Idée directrice</span>
> Un groupe est un ensemble muni de **structure** ; les bons objets d'étude sont les **morphismes**, c'est-à-dire les applications qui respectent la structure. Presque tout le chapitre se relit ainsi :
>
> | Notion « élémentaire » | Lecture structurelle |
> |---|---|
> | sous-groupe $H\subset G$ | sous-objet : inclusion $i\colon H\hookrightarrow G$ morphisme injectif |
> | noyau $\operatorname{Ker}\varphi$ | ce qui est envoyé sur le neutre |
> | groupe quotient $G/H$ | objet universel pour les morphismes qui tuent $H$ |
> | $G/\operatorname{Ker}\varphi\simeq\varphi(G)$ | factorisation canonique d'un morphisme |
> | action de $G$ sur $X$ | morphisme $G\to\operatorname{Sym}(X)$ |

> [!warning]- <span style="font-variant: small-caps;">Notation abusive</span>
> On dit souvent « le groupe $G$ » au lieu de « le groupe $(G,\ast)$ », sous-entendant que *l'ensemble $G$ muni d'une loi interne notée $\ast$ est un groupe*. Rigoureusement, un groupe est un **quadruplet** $(G,\ast,e,(\cdot)^{-1})$ : la loi, le neutre et l'inversion font partie de la donnée (on montre que $e$ et l'inversion sont déterminés par $\ast$, mais les inclure rend les sous-groupes plus faciles à décrire).

### Le critère à retenir

> [!done]- <span style="font-variant: small-caps;">Critère standard de sous-groupe</span>
> Soit $(G,\ast)$ un groupe et $H\subset G$. Alors
> $$H\text{ sous-groupe de }G\iff H\neq\varnothing\;\text{ et }\;\forall(x,y)\in H^2,\;x\ast y^{-1}\in H.$$
> Ce critère garantit automatiquement que $e\in H$, que $x^{-1}\in H$ pour tout $x\in H$ et que $x\ast y\in H$ : $H$ est donc un groupe pour la loi induite. (Démonstration : proposition 1 de la section 2.1.)

> [!quote]- <span style="font-variant: small-caps;">Remarque : une coquille classique</span>
> L'énoncé s'écrit avec $(x,y)\in H^2$ (couple d'éléments de $H$), **pas** $H^{-1}$. Et c'est bien $x\ast y^{-1}$ (et non $x\ast y$) : avec $xy$ seul, on n'obtiendrait pas l'inverse. *Contre-exemple : $H=\mathbb{N}\subset(\mathbb{Z},+)$ est stable par $+$ mais n'est pas un sous-groupe.*

### Sous-groupe = sous-objet

> [!note] <span style="font-variant: small-caps;">Définition (sous-groupe, version structurelle)</span>
> Soit $H\subset G$ et $i\colon H\hookrightarrow G$ l'inclusion. On dit que $H$ est un **sous-groupe** de $G$ s'il existe une loi $\ast_H$ sur $H$ (nécessairement $\ast_H=\ast|_{H\times H}$) telle que $(H,\ast_H)$ soit un groupe et $i$ un **morphisme de groupes** : $i(x\ast_Hy)=i(x)\ast i(y)$.

> [!success]- <span style="font-variant: small-caps;">Traduction explicite</span>
> Cela revient à dire que $H$ est **stable par les opérations qui définissent la structure** :
> $$\begin{cases}e\in H\\\forall x,y\in H,\;x\ast y\in H\\\forall x\in H,\;x^{-1}\in H\end{cases}$$
> Autrement dit, $H$ est un *sous-objet* de $G$ dans la catégorie $\mathbf{Grp}$.

> [!info] <span style="font-variant: small-caps;">Dictionnaire catégorique</span>
> Dans la catégorie $\mathbf{Grp}$ (objets : groupes ; flèches : morphismes de groupes) :
> - un sous-groupe de $G$ est un couple $(H,i)$ où $i\colon H\to G$ est un **monomorphisme** ;
> - **monomorphisme $\iff$ morphisme injectif** (exercice 20) ;
> - **épimorphisme $\Leftarrow$ morphisme surjectif** (la réciproque est vraie dans $\mathbf{Grp}$ mais plus délicate) : les quotients $G\to G/H$ sont les épimorphismes « typiques ».

> [!tip]- <span style="font-variant: small-caps;">Pourquoi ce point de vue est utile</span>
> Le schéma « **être stable par les opérations de la structure** $\iff$ **sous-objet** » est universel :
> - anneaux $\to$ sous-anneaux ; espaces vectoriels $\to$ sous-espaces ; algèbres $\to$ sous-algèbres ;
> - dans chaque cas, on prouve qu'une partie est un sous-objet en vérifiant la stabilité par les opérations.
>
> Il explique aussi la remarque suivante : dire « $(H,\ast)$ est un groupe, $H\subset G$ et la loi de $H$ est celle de $G$ » est **déjà** dire que l'inclusion est un morphisme. L'implication $\{(G,\ast),(H,\ast)\text{ groupes},H\subset G\}\Rightarrow H\text{ sous-groupe}$ est donc une *tautologie* une fois la loi induite fixée : tout le contenu est dans la **vérification de la stabilité**.

### Propriété universelle du quotient

> [!info] <span style="font-variant: small-caps;">Théorème (factorisation par le quotient)</span>
> Soit $H\lhd G$ et $\pi\colon G\to G/H$ la projection canonique. Pour tout morphisme $\varphi\colon G\to G'$ tel que $H\subset\operatorname{Ker}\varphi$, il existe **un unique morphisme** $\overline\varphi\colon G/H\to G'$ tel que
> $$\varphi=\overline\varphi\circ\pi.$$
> De plus $\operatorname{Ker}\overline\varphi=\operatorname{Ker}\varphi/H$, et $\overline\varphi$ est surjectif ssi $\varphi$ l'est.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> **Existence.** On pose $\overline\varphi(xH)=\varphi(x)$. C'est bien défini : si $xH=yH$, alors $x^{-1}y\in H\subset\operatorname{Ker}\varphi$, donc $\varphi(x)=\varphi(y)$. C'est un morphisme : $\overline\varphi(xH\cdot yH)=\varphi(xy)=\varphi(x)\varphi(y)$.
> **Unicité.** Une telle $\overline\varphi$ vérifie $\overline\varphi(xH)=\overline\varphi(\pi(x))=\varphi(x)$ : elle est imposée sur tout $G/H$ car $\pi$ est surjective.
> **Noyau.** $\overline\varphi(xH)=e'\iff x\in\operatorname{Ker}\varphi$. $\square$

> [!quote]- <span style="font-variant: small-caps;">Conséquence : le premier théorème d'isomorphisme</span>
> Pour $H=\operatorname{Ker}\varphi$, on a $\operatorname{Ker}\overline\varphi=\{\overline e\}$ : $\overline\varphi$ est injectif et induit un isomorphisme $G/\operatorname{Ker}\varphi\simeq\varphi(G)$. Tout morphisme se factorise donc en
> $$G\xrightarrow{\;\text{surjection}\;}G/\operatorname{Ker}\varphi\xrightarrow{\;\simeq\;}\varphi(G)\xrightarrow{\;\text{inclusion}\;}G'.$$

> [!info] <span style="font-variant: small-caps;">Deuxième et troisième théorèmes d'isomorphisme</span>
> 1. Si $H\leq G$ et $N\lhd G$, alors $HN$ est un sous-groupe de $G$, $N\lhd HN$, $H\cap N\lhd H$ et
> $$HN/N\;\simeq\;H/(H\cap N).$$
> 2. Si $N\subset K$ sont deux sous-groupes distingués de $G$, alors $K/N\lhd G/N$ et
> $$(G/N)\big/(K/N)\;\simeq\;G/K.$$

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> **(1)** $HN=NH$ car $N$ est distingué, donc $HN$ est un sous-groupe (exercice 3a). L'application $f\colon H\to HN/N$, $h\mapsto hN$ est un morphisme, surjectif (car $hnN=hN$), de noyau $H\cap N$. Le premier théorème conclut.
> **(2)** La projection $\pi_K\colon G\to G/K$ est surjective de noyau $K\supset N$ : elle se factorise en $\overline{\pi_K}\colon G/N\to G/K$ surjective, de noyau $K/N$ (théorème de factorisation). Donc $K/N\lhd G/N$, et le premier théorème donne $(G/N)/(K/N)\simeq G/K$. $\square$

### Actions et morphismes vers le groupe symétrique

> [!info] <span style="font-variant: small-caps;">Proposition (une action = un morphisme)</span>
> Se donner une action de $G$ sur $X$ revient à se donner un **morphisme de groupes** $\rho\colon G\to\operatorname{Sym}(X)$ (groupe des bijections de $X$). Le noyau de $\rho$ est l'ensemble des éléments qui agissent trivialement.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> *Action $\Rightarrow$ morphisme.* On pose $\rho(g)(x)=g\cdot x$. Chaque $\rho(g)$ est bijective, d'inverse $\rho(g^{-1})$ (car $g^{-1}\cdot(g\cdot x)=(g^{-1}g)\cdot x=x$), et $\rho(gh)=\rho(g)\circ\rho(h)$ par l'axiome (i) d'action.
> *Morphisme $\Rightarrow$ action.* On pose $g\cdot x=\rho(g)(x)$ : $e\cdot x=x$ car $\rho(e)=\mathrm{id}$, et $g\cdot(h\cdot x)=(\rho(g)\circ\rho(h))(x)=\rho(gh)(x)$. $\square$

> [!info] <span style="font-variant: small-caps;">Théorème de Cayley</span>
> Tout groupe $G$ est isomorphe à un sous-groupe de $\operatorname{Sym}(G)$. En particulier, tout groupe d'ordre $n$ s'injecte dans $\mathfrak{S}_n$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> $G$ opère sur lui-même par translation à gauche $g\cdot x=gx$. Le morphisme associé $\lambda\colon G\to\operatorname{Sym}(G)$ est injectif : si $\lambda(g)=\mathrm{id}$, alors $g=g\cdot e=e$. Donc $G\simeq\lambda(G)\leq\operatorname{Sym}(G)$. $\square$

> [!quote]- <span style="font-variant: small-caps;">Pourquoi c'est important</span>
> Cayley dit que **les groupes de permutations sont « tous les groupes »**. Mais $\operatorname{Sym}(G)$ est énorme ($n!$ éléments) : en pratique on cherche des actions sur des ensembles *plus petits* (par exemple $G/H$, voir exercice 22).

### Produit direct

> [!info] <span style="font-variant: small-caps;">Propriété universelle du produit</span>
> Soient $G_1,G_2$ des groupes. Le produit $G_1\times G_2$ (loi composante par composante) muni des projections $p_1,p_2$ vérifie : pour tout groupe $K$ et tous morphismes $f_i\colon K\to G_i$, il existe un **unique** morphisme $f\colon K\to G_1\times G_2$ tel que $p_i\circ f=f_i$, à savoir $f(k)=(f_1(k),f_2(k))$.

> [!tip]- <span style="font-variant: small-caps;">Démonstration</span>
> L'application $k\mapsto(f_1(k),f_2(k))$ est un morphisme car les lois sont composante par composante. Si $f$ vérifie $p_i\circ f=f_i$, alors ses deux composantes sont imposées. $\square$

---

### Exercices complémentaires

> [!question]- <span style="font-variant: small-caps;">Exercice 20 ★★ : monomorphismes dans $\mathbf{Grp}$</span>
> Montrer qu'un morphisme de groupes $\varphi\colon G\to G'$ est un *monomorphisme* (i.e. pour tous morphismes $u,v\colon K\to G$, $\varphi\circ u=\varphi\circ v\Rightarrow u=v$) si et seulement si il est **injectif**.
>
> > [!todo]- 💡 Indice
> > Pour $(\Rightarrow)$, prendre $K=\operatorname{Ker}\varphi$, $u$ l'inclusion et $v$ le morphisme trivial.
>
> > [!success]- Solution
> > $(\Leftarrow)$ Si $\varphi$ est injectif et $\varphi(u(k))=\varphi(v(k))$, alors $u(k)=v(k)$ : donc $u=v$.
> > $(\Rightarrow)$ Soit $K=\operatorname{Ker}\varphi$, $u\colon K\hookrightarrow G$ l'inclusion et $v\colon K\to G$, $k\mapsto e$. Alors $\varphi\circ u=\varphi\circ v$ (les deux valent $e'$), donc $u=v$ : tout élément de $K$ est envoyé sur $e$ par $u$, c'est-à-dire vaut $e$. Donc $K=\{e\}$ et $\varphi$ est injectif.

> [!question]- <span style="font-variant: small-caps;">Exercice 21 ★★ : quotients par des intersections</span>
> Soient $N_1,N_2\lhd G$ avec $N_1\cap N_2=\{e\}$. Montrer que l'application $G\to G/N_1\times G/N_2$, $x\mapsto(xN_1,xN_2)$ est un morphisme **injectif**. Si de plus $G=N_1N_2$, montrer qu'elle est un isomorphisme.
>
> > [!todo]- 💡 Indice
> > Utiliser la propriété universelle du produit, puis calculer le noyau. Pour la surjectivité : $G=N_1N_2$.
>
> > [!success]- Solution
> > C'est $(\pi_1,\pi_2)$, morphisme par la propriété universelle du produit. Son noyau est $N_1\cap N_2=\{e\}$ : injectif.
> > Si $G=N_1N_2$, soit $(xN_1,yN_2)$ ; on écrit $x=a_1a_2$ et $y=b_1b_2$ ($a_i,b_i\in N_i$). Comme $N_1,N_2$ sont distingués et $N_1\cap N_2=\{e\}$, ils commutent élément par élément (le commutateur $[a_1,a_2]$ est dans $N_1\cap N_2$). Posons $z=b_1a_2$ : $zN_1=a_2N_1=a_1a_2N_1=xN_1$ et $zN_2=b_1N_2=b_1b_2N_2=yN_2$. Donc l'application est surjective, d'où un isomorphisme.

> [!question]- <span style="font-variant: small-caps;">Exercice 22 ★★★ : sous-groupe de plus petit indice premier</span>
> Soit $G$ un groupe fini, $p$ le plus petit nombre premier divisant $\operatorname{Card}(G)$, et $H$ un sous-groupe d'indice $p$. Montrer que $H\lhd G$.
>
> > [!todo]- 💡 Indice
> > Faire opérer $G$ sur $G/H$ par translation. Le morphisme $\rho\colon G\to\mathfrak{S}_p$ a un noyau $K\subset H$. Comparer $\operatorname{Card}(G/K)$ avec $p!$ et utiliser la minimalité de $p$.
>
> > [!success]- Solution
> > $G$ opère sur $X=G/H$ (ensemble à $p$ éléments) par $g\cdot xH=gxH$. Soit $\rho\colon G\to\operatorname{Sym}(X)\simeq\mathfrak{S}_p$ le morphisme associé et $K=\operatorname{Ker}\rho\lhd G$.
> > - $K\subset H$ : si $g\in K$, $g\cdot H=H$, donc $g\in H$.
> > - $G/K\simeq\rho(G)\leq\mathfrak{S}_p$, donc $\operatorname{Card}(G/K)\mid p!$.
> > - Or $\operatorname{Card}(G/K)=[G:H][H:K]=p\cdot[H:K]$ divise $\operatorname{Card}(G)$. Donc $[H:K]$ divise $\operatorname{Card}(G)$ et, puisque $p\cdot[H:K]\mid p!$, $[H:K]\mid(p-1)!$.
> > - Tout facteur premier de $[H:K]$ est donc $\leq p-1$ (diviseur de $(p-1)!$) **et** divise $\operatorname{Card}(G)$ : impossible par minimalité de $p$, sauf si $[H:K]=1$.
> >
> > Donc $H=K\lhd G$. $\square$
>
> > [!quote]- Corollaires célèbres
> > - Un sous-groupe d'indice $2$ est distingué (cas $p=2$ : c'est alors le plus petit premier possible, mais l'énoncé de l'exercice 9a le prouve sans hypothèse).
> > - Si $|G|=pq$ avec $p<q$ premiers, tout sous-groupe d'ordre $q$ (donc d'indice $p$) est distingué dans $G$.

> [!question]- <span style="font-variant: small-caps;">Exercice 23 ★★ : un groupe ne peut pas être union de deux sous-groupes propres</span>
> Montrer qu'un groupe $G$ ne peut pas être la réunion de deux sous-groupes **stricts**. Que dire de trois sous-groupes ?
>
> > [!success]- Solution
> > Si $G=H_1\cup H_2$ avec $H_1,H_2\neq G$, alors $H_1\cup H_2$ est un sous-groupe, donc (exercice 2a) $H_1\subset H_2$ ou $H_2\subset H_1$, d'où $G=H_2$ ou $G=H_1$ : absurde.
> > Avec trois sous-groupes, c'est possible : le groupe de Klein $V=(\mathbb{Z}/2\mathbb{Z})^2$ est la réunion de ses trois sous-groupes d'ordre $2$.

---

> [!todo] <span style="font-variant: small-caps;">Suite du cours</span>
> - [ ] 2.2. Morphismes de groupes, noyau et image
> - [ ] 2.3. Sous-groupe engendré, ordre d'un élément, groupes cycliques
> - [ ] 2.4. Théorème de Lagrange, groupes quotients
> - [ ] 3. Anneaux et corps
