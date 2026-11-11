---
draft: true
---


> [!abstract]- <span style="font-variant: small-caps;">Comment utiliser ce fichier</span>
> À coller dans `I - Arithmétique, Groupes et Anneaux.md`, **juste après la remarque 3 de la section 2.1** (supprime alors le callout `[!todo]` final). La numérotation reprend celle du livre.
>
> **Code des encadrés** (en plus de ceux du fichier I) :
> - `[!question]` : énoncé d'un exercice, avec sa difficulté (★ à ★★★ ; ★★★ = niveau agrégation)
> - `[!todo]-` **Indice** : à ouvrir seulement si tu bloques
> - `[!success]-` **Solution** : à ouvrir en dernier
>
> Convention : pour une action, j'écris $\operatorname{Orb}(x)$ pour l'orbite et $\operatorname{Stab}(x)$ pour le stabilisateur (le livre note $G_x$ et $S_x$, ce qui prête à confusion).

---

## 2.1 (suite). Ordre, Lagrange, sous-groupes distingués

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

> [!todo] <span style="font-variant: small-caps;">Suite du cours (à construire)</span>
> - [ ] 3. Anneaux et corps (idéaux, anneaux quotients, anneaux principaux, polynômes)
> - [ ] Théorèmes de Sylow (utiliser Cauchy, exercice 12, et la section 2.6)
> - [ ] Simplicité de $\mathfrak{A}_n$ ($n\geq5$)
