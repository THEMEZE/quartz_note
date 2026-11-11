---
draft: true
---


> [!abstract]- <span style="font-variant: small-caps;">Comment utiliser ce fichier</span>
> À coller dans `I - Arithmétique, Groupes et Anneaux.md`, **à la fin de la section 1.3 (Exercices)**, juste avant la section 1.4. La numérotation continue celle du fichier I (exercices 1 à 4).
>
> - `[!question]` : énoncé, avec difficulté ★ à ★★★ (★★★ = niveau agrégation)
> - `[!todo]-` 💡 **Indice** : à n'ouvrir que si tu bloques
> - `[!success]-` **Solution** : à ouvrir en dernier
>
> Les exercices **5 à 13** sont ceux de ton livre (corrigés proprement). Les exercices **14 à 22** sont des compléments plus difficiles. Certains utilisent la théorie des groupes (notion d'ordre, Lagrange) : ils sont signalés par 🔗.

---


### Exercices du livre

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
