---
title: 1. Divisibilité - pgcd, ppcm
tags:
  - algèbre
  - arithmétique
  - groupes
  - cours
---
[[Mathématique/Algèbre/I - Arithmétique, Groupes et Anneaux/A. Arithmétique sur les entiers/index|🏠 A. Arithmétique sur les entiers]] [[Mathématique/Algèbre/I - Arithmétique, Groupes et Anneaux/A. Arithmétique sur les entiers/2. Nombres premiers/index|➡️ 2. Nombres premiers]] 


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
> 4. $bq+r=bq'+r'$ donc $b(q-q')=r'-r$.
> 5. Comme $0\leq r,r'<b$, on a $-b<r'-r<b$, d'où $|r'-r|<b$.
> 6. Donc $b\,|q-q'|<b$, soit $|q-q'|<1$. Or $|q-q'|\in\mathbb{N}$, donc $q=q'$ puis $r=r'$. $\square$

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
> 7. **Cas trivial.** Si $I=\{0\}$, alors $I=0\cdot A$.
> 8. **Choix du générateur.** Supposons $I\neq\{0\}$. L'ensemble $\{v(x)\mid x\in I\setminus\{0\}\}$ est une partie non vide de $\mathbb{N}$ ; elle admet un minimum. Soit $b\in I\setminus\{0\}$ qui l'atteint : $v(b)\leq v(x)$ pour tout $x\in I\setminus\{0\}$.
> 9. **Double inclusion.**
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
