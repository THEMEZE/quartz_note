---
title: I - Arithmétique, Groupes et Anneaux
tags: [algèbre, arithmétique, groupes, cours]
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

---

> [!todo] <span style="font-variant: small-caps;">Suite du cours</span>
> - [ ] 2.2. Morphismes de groupes, noyau et image
> - [ ] 2.3. Sous-groupe engendré, ordre d'un élément, groupes cycliques
> - [ ] 2.4. Théorème de Lagrange, groupes quotients
> - [ ] 3. Anneaux et corps
