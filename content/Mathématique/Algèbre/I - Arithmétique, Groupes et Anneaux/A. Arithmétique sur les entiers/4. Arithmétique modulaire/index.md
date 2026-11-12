---
title: 4. Arithmétique modulaire
tags:
  - algèbre
  - arithmétique
  - groupes
  - cours
---
[[Mathématique/Algèbre/I - Arithmétique, Groupes et Anneaux/A. Arithmétique sur les entiers/index|🏠 A. Arithmétique sur les entiers]] [[Mathématique/Algèbre/I - Arithmétique, Groupes et Anneaux/A. Arithmétique sur les entiers/3. Exercices corrigés/index| ⬅️ 3. Exercices corrigés]] [[Mathématique/Algèbre/I - Arithmétique, Groupes et Anneaux/A. Arithmétique sur les entiers/3. Exercices corrigés/index| ➡️ 3. Exercices corrigés]] 
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
