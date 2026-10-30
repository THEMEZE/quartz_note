---
title: V - Problème de Kepler, vecteur de Runge–Lenz–Laplace, symétrie $SO(n+1)$, version quantique, précession de Mercure, exercices corrigés
tags:
  - Agrégation
  - Physique
  - Mécanique
  - Mécanique quantique
  - Relativité générale
niveau: Doctorat
version: 1
---

---
[^1]: Jérôme Perez, *Le théorème de Noether. Son centenaire, sa signification et sa portée*, Quadrature n°100 (2018)
[^2]: J. Moser, *Regularization of Kepler's problem and the averaging method on a manifold*, Comm. Pure Appl. Math. 23 (1970), 609–636
[^3]: V. Fock, *Zur Theorie des Wasserstoffatoms*, Z. Phys. 98 (1935), 145–154 ; W. Pauli, Z. Phys. 36 (1926), 336–363
[^4]: A. Einstein, *Erklärung der Perihelbewegung des Merkur aus der allgemeinen Relativitätstheorie*, Sitzungsber. Preuss. Akad. Wiss. (1915)
[^5]: C. D. Murray & S. F. Dermott, *Solar System Dynamics*, Cambridge UP (1999), chap. 6–7
---

> [!abstract] Suite de *M1 Rappels et compléments (tensoriel)*
> On reprend §8.7 de M1 (symétrie cachée de Kepler) et on la développe : (1) vecteur de Runge–Lenz–Laplace (RLL) et trajectoire $r(\theta)$ **déduite de la seule conservation de $\vec A$** ; (2) algèbre de Lie $\mathfrak{so}(n+1)$, preuve détaillée, transformation de Noether engendrée par $\vec A$, projection de Fock–Moser ; (3) **version quantique** (Pauli) : spectre de l'atome d'hydrogène en dimension $n$ ; (4) perturbations : $\dot{\vec A}=\{\vec A,\delta H\}$ ; (5) **avance du périhélie de Mercure**, de façon complète (relativité générale, post-newtonien, perturbations planétaires, bilan chiffré) ; (6) exercices corrigés : pendule de Foucault, toupie, cerceau.
>
> Conventions de M1 : base de $\mathscr E$ orthonormée pour simplifier ($g_{ij}=\delta_{ij}$, indices haut/bas confondus quand c'est sans ambiguïté), $\mathsf L^{ij}=x^ip^j-x^jp^i$, $\{x^i,p_j\}=\delta^i{}_j$.

# 1. Kepler classique : vecteur de Runge–Lenz–Laplace et trajectoire

## 1.1 Le problème

Point $M$ de masse $m$ dans $\mathscr E=\mathbb R^n$, $V(r)=-k/r$ ($k>0$ : attraction ; gravitation $k=GMm$, coulomb $k=e^2/4\pi\varepsilon_0$) :
$$
H=\frac{p^2}{2m}-\frac kr,\qquad \dot x^i=\frac{p^i}{m},\quad \dot p^i=-\frac{k\,x^i}{r^3}.
$$
Invariant par $SO(n)$ : $\mathsf L^{ij}$ conservés (§8.4 de M1). Notons $s:=\vec x\cdot\vec p$, $L^2:=\tfrac12\mathsf L_{ij}\mathsf L^{ij}=r^2p^2-s^2$ (carré du moment cinétique, indépendant de $n$) ; $\ \dot r=s/(mr)$.

Le mouvement reste dans le **plan** engendré par $(\vec x,\vec p)$ (qui est le plan de $\mathsf L=\vec x\wedge\vec p$, fixe) : on se ramène à la dimension 2 dans ce plan. Ce plan est aussi le plan de $\vec A$ (ci-dessous).

## 1.2 Définition du vecteur RLL

$$
\boxed{A^i:=\mathsf L^{ij}p_j-mk\,\frac{x^i}{r}=x^i\left(p^2-\frac{mk}{r}\right)-s\,p^i}\qquad(\text{dim. 3 : }\vec A=\vec p\times\vec L-mk\,\hat r).
$$
(Le calcul $\mathsf L^{ij}p_j=x^ip^2-sp^i$ est immédiat ; en dimension 3, $(\vec p\times\vec L)^i=\mathsf L^{ij}p_j$ par $\varepsilon\varepsilon=\delta\delta-\delta\delta$.)

>[!tip]+ **Proposition 1 (conservation).** $\dot A^i=0$.
>
>*Démonstration.* $\dot{\mathsf L}=0$ ; $\dot p_j=-kx_j/r^3$ donne $\mathsf L^{ij}\dot p_j=-\dfrac{k}{r^3}\left(x^is-r^2p^i\right)$ (car $\mathsf L^{ij}x_j=x^is-r^2p^i$). D'autre part $\dfrac{d}{dt}\dfrac{x^i}{r}=\dfrac{p^i}{mr}-\dfrac{x^is}{mr^3}$. Donc
>$$
>\dot A^i=-\frac{k}{r^3}\left(x^is-r^2p^i\right)-\frac{kp^i}{r}+\frac{k\,x^is}{r^3}=\frac{kp^i}{r}-\frac{kp^i}{r}=0.\qquad\square
>$$
>*Variante par les crochets de Poisson* : $\{A^i,H\}=0$ (même calcul).

## 1.3 Propriétés algébriques

1. **$\vec A$ est dans le plan de l'orbite** : $\vec A=\alpha\vec x+\beta\vec p$ avec $\alpha=p^2-mk/r$, $\beta=-s$ ; donc $A^{[i}\mathsf L^{jk]}=0$ (en dimension 3 : $\vec A\cdot\vec L=0$).
2. **Norme.** $\ \boxed{A^2=m^2k^2+2mE\,L^2}$ où $E=H$.

>*Démonstration.* Avec $W=p^2-mk/r$ : $A^2=r^2W^2-2s^2W+s^2p^2=r^2p^4-2mkrp^2+m^2k^2-s^2p^2+\frac{2mks^2}{r}$. En regroupant : $=m^2k^2+p^2\left(r^2p^2-s^2\right)-\frac{2mk}{r}\left(r^2p^2-s^2\right)=m^2k^2+L^2\left(p^2-\frac{2mk}{r}\right)=m^2k^2+2mE\,L^2$. $\square$

3. **Excentricité.** On pose $\boxed{e:=\dfrac{\|\vec A\|}{mk}=\sqrt{1+\dfrac{2EL^2}{mk^2}}}$ : $e<1$ si $E<0$ (ellipse), $e=1$ si $E=0$ (parabole), $e>1$ si $E>0$ (hyperbole).

## 1.4 Trajectoire $r(\theta)$ obtenue par la conservation de $\vec A$

>[!tip]+ **Proposition 2.** Soit $\theta$ l'angle entre $\vec x$ et $\vec A$ (dans le plan de l'orbite). Alors
>$$
>\boxed{r(\theta)=\frac{p}{1+e\cos\theta},\qquad p=\frac{L^2}{mk}}\qquad(\text{conique de foyer l'origine}).
>$$
>*Démonstration.* Calculons $\vec A\cdot\vec x$ de deux façons. D'une part $\vec A\cdot\vec x=\|\vec A\|\,r\cos\theta=mk\,e\,r\cos\theta$. D'autre part
>$$
>\vec A\cdot\vec x=\mathsf L^{ij}p_jx_i-mkr=\left(x^ip^j-x^jp^i\right)x_ip_j-mkr=r^2p^2-s^2-mkr=L^2-mkr .
>$$
>L'égalité $mke\,r\cos\theta=L^2-mkr$ donne $r\,(1+e\cos\theta)=L^2/(mk)$. $\square$

*Remarque.* Aucune équation différentielle n'a été intégrée : la conservation de $\vec A$ est une **intégrale première supplémentaire** qui équivaut à l'équation de la conique ; elle fixe l'**orientation de l'orbite** ($\vec A$ pointe vers le **périhélie**, $\theta=0$) et explique pourquoi l'orbite est **fermée**. Toute perturbation qui brise la conservation de $\vec A$ produit une **précession** (§4–5).

**Grandeurs de l'ellipse** ($E<0$) : $a=\dfrac{p}{1-e^2}=-\dfrac{k}{2E}$, $b=a\sqrt{1-e^2}$, $r_{\min}=a(1-e)$, $r_{\max}=a(1+e)$, $E=-\dfrac{k}{2a}$. **Loi des aires** : $\dot\theta=L/(mr^2)$, aire balayée $\dfrac{L}{2m}\,dt$ ; en une période $\pi ab=\dfrac{L}{2m}T$, d'où avec $L^2=mkp=mka(1-e^2)$ et $b=a\sqrt{1-e^2}$ : $\ \boxed{T=2\pi\sqrt{\dfrac{ma^3}{k}}}$ (3e loi de Kepler).

## 1.5 Hodographe

Pour $n=3$ avec $\vec L\perp\vec p$, $\vec L\times(\vec p\times\vec L)=L^2\vec p$ ; en appliquant $\vec L\times$ à $\vec p\times\vec L=\vec A+mk\,\hat r$ :
$$
\vec p=\frac{1}{L^2}\,\vec L\times\vec A+\frac{mk}{L^2}\,\vec L\times\hat r .
$$
Comme $\hat r$ décrit le cercle unité du plan, l'**hodographe** (lieu de $\vec p$) est un **cercle** de rayon $\rho=mk/L$ et de centre $\vec C=\vec L\times\vec A/L^2$, $\|\vec C\|=\|\vec A\|/L=e\rho$. Pour $E<0$ : $\rho^2-\|\vec C\|^2=\rho^2(1-e^2)=-2mE=:p_0^2>0$ ; l'origine est à l'intérieur du cercle. (On retrouve le cercle de centre $\overrightarrow{OC}=\sqrt{\frac{2e^2(-E)}{m(1-e^2)}}\hat u_y$ de [^1].)

# 2. La symétrie cachée $SO(n+1)$ : démonstration détaillée

## 2.1 Crochets de Poisson fondamentaux

Posons $\mathsf L^{ij}=x^ip^j-x^jp^i$. Pour tout vecteur $V^k\in\{x^k,p^k,A^k\}$ (fonction vectorielle de $x,p$) :
$$
\boxed{\{\mathsf L^{ij},V^k\}=\delta^{ik}V^j-\delta^{jk}V^i}
$$
(rotation de $V$ : on a $\{\mathsf L^{ij},x^k\}=-x^i\delta^{jk}+x^j\delta^{ik}$, et de même pour $p$). De plus (§7.2 de M1) $\{\mathsf L^{ij},\mathsf L^{kl}\}=\delta^{ik}\mathsf L^{jl}-\delta^{il}\mathsf L^{jk}-\delta^{jk}\mathsf L^{il}+\delta^{jl}\mathsf L^{ik}$ et $\{\mathsf L^{ij},H\}=\{A^i,H\}=0$.

>[!tip]+ **Proposition 3.** $\ \boxed{\{A^i,A^j\}=-2mH\,\mathsf L^{ij}}$.
>
>*Démonstration.* On écrit $A^i=x^iW-s\,p^i$, $W=p^2-mk/r$, $s=\vec x\cdot\vec p$. Briques élémentaires (convention $\{f,g\}=\partial_xf\partial_pg-\partial_pf\partial_xg$) :
>$$
>\{x^i,W\}=2p^i,\ \ \{W,p^j\}=\frac{mk\,x^j}{r^3},\ \ \{s,W\}=2p^2-\frac{mk}{r}\ (\text{car }s\text{ engendre les dilatations}),\ \ \{x^i,s\}=x^i,\ \ \{p^i,s\}=-p^i .
>$$
>(i) $\{x^iW,x^jW\}=x^iW\{W,x^j\}+Wx^j\{x^i,W\}=2W\left(x^jp^i-x^ip^j\right)=-2W\mathsf L^{ij}$.
>(ii) $B^{ij}:=\{x^iW,sp^j\}=\dfrac{mk\,s\,x^ix^j}{r^3}-x^ip^j\left(2p^2-\dfrac{mk}{r}\right)+Ws\,\delta^{ij}+Wx^ip^j$, et $\{sp^i,x^jW\}=-B^{ji}$. Donc $-B^{ij}+B^{ji}=\left(2p^2-\frac{mk}{r}-W\right)\mathsf L^{ij}=p^2\mathsf L^{ij}$.
>(iii) $\{sp^i,sp^j\}=sp^j\{p^i,s\}+p^is\{s,p^j\}=-sp^ip^j+sp^ip^j=0$.
>Au total $\{A^i,A^j\}=\left(p^2-2W\right)\mathsf L^{ij}=\left(-p^2+\frac{2mk}{r}\right)\mathsf L^{ij}=-2mH\,\mathsf L^{ij}$. $\square$

## 2.2 Les trois algèbres selon le signe de $E$

Sur l'hypersurface d'énergie $H=E\ne0$, on pose
$$
K^i:=\frac{A^i}{\sqrt{|{-2mE}|}}\quad\text{et}\quad \mathsf L^{i,n+1}:=K^i\ (E<0),\qquad\mathsf L^{i,n+1}:=\frac{A^i}{\sqrt{2mE}}\ (E>0).
$$
**$E<0$ :** $\{K^i,K^j\}=\mathsf L^{ij}$ et $\{\mathsf L^{ij},K^k\}=\delta^{ik}K^j-\delta^{jk}K^i$ : ce sont **exactement** les relations de $\mathfrak{so}(n+1)$ pour les $\mathsf L^{ab}$, $a,b\in\{1,\dots,n+1\}$ (on vérifie $\{\mathsf L^{i,n+1},\mathsf L^{j,n+1}\}=\mathsf L^{ij}$ avec la formule générale et $\delta^{n+1,n+1}=1$). **$E>0$ :** $\{K^i,K^j\}=-\mathsf L^{ij}$, algèbre de Lorentz $\mathfrak{so}(n,1)$ (orbites hyperboliques). **$E=0$ :** les $A^i$ commutent entre eux, algèbre euclidienne $\mathfrak e(n)=\mathfrak{so}(n)\ltimes\mathbb R^n$ (orbites paraboliques).

Les charges conservées engendrent donc, pour $E<0$, le groupe $SO(n+1)$ ($SO(4)$ pour $n=3$, $SO(3)$ pour $n=2$) agissant sur l'ensemble des orbites **de même énergie**. Le nombre de charges est $\frac{n(n+1)}{2}=\frac{n(n-1)}{2}+n$ ($\mathsf L^{ij}$ plus $A^i$), mais seules $2n-1$ sont indépendantes (relations $A^{[i}\mathsf L^{jk]}=0$, $A^2=m^2k^2+2mEL^2$, $E$ fonction de $a$) : le système est **maximalement superintégrable**.

*Casimirs.* Pour $E<0$, $\ \tfrac12\mathsf L_{ij}\mathsf L^{ij}+K^2=L^2+\dfrac{A^2}{-2mE}=L^2+\dfrac{m^2k^2+2mEL^2}{-2mE}=-\dfrac{mk^2}{2E}$. C'est le **Casimir quadratique** de $\mathfrak{so}(n+1)$ (norme au carré du « vecteur moment cinétique en $n+1$ dimensions ») ; il détermine $E$.

## 2.3 Transformation de Noether engendrée par $\vec A$

Le théorème de Noether hamiltonien (§8.1 de M1) : la charge $\mathscr Q_{\vec a}=\vec a\cdot\vec A$ engendre $\delta x^i=\{x^i,\mathscr Q_{\vec a}\}=\partial\mathscr Q_{\vec a}/\partial p_i$ et $\delta p_i=-\partial\mathscr Q_{\vec a}/\partial x^i$ :
$$
\boxed{\delta x=2(\vec a\cdot\vec x)\,\vec p-(\vec a\cdot\vec p)\,\vec x-(\vec x\cdot\vec p)\,\vec a}\ ,\qquad
\delta\vec p=-p^2\vec a+(\vec a\cdot\vec p)\vec p+mk\left(\frac{\vec a}{r}-\frac{(\vec a\cdot\vec x)\vec x}{r^3}\right).
$$
C'est une symétrie **non ponctuelle** (elle mélange $x$ et $p$) : $\delta H=\{H,\mathscr Q_{\vec a}\}\!=0$. Elle change **la forme** de l'orbite (excentricité, orientation) à $E$ **fixée**, c'est elle qui fait passer d'une ellipse à une autre de même $a$ : cf. la rotation de vitesse au point $K$ dans [^1].

## 2.4 Projection de Fock–Moser : le flot de Kepler est un flot géodésique sur $S^n$ [^2][^3]

**Idée.** Pour $E<0$ on pose $p_0=\sqrt{-2mE}$ et on projette stéréographiquement l'espace des impulsions $\mathbb R^n\ni\vec p$ sur la sphère unité $S^n\subset\mathbb R^{n+1}$ :
$$
\boldsymbol\xi=\left(\frac{2p_0\,\vec p}{p^2+p_0^2},\ \frac{p^2-p_0^2}{p^2+p_0^2}\right),\qquad\|\boldsymbol\xi\|=1,\qquad|\boldsymbol\xi-\boldsymbol\xi'|^2=\frac{4p_0^2\,|\vec p-\vec p'|^2}{(p^2+p_0^2)(p'^2+p_0^2)}.
$$
L'équateur $\xi_{n+1}=0$ correspond à la sphère $|\vec p|=p_0$.

>[!tip]+ **Proposition 4.** Pour $E$ fixé, les hodographes de toutes les orbites képlériennes sont envoyés par la projection sur les **grands cercles** de $S^n$.
>
>*Démonstration.* D'après §1.5, l'hodographe d'une orbite est un cercle de rayon $\rho$, de centre $\vec C$ avec $\rho^2-\|\vec C\|^2=p_0^2$. Un cercle du plan coupe la sphère $|\vec p|=p_0$ (qui est l'image de l'équateur) en deux points **diamétralement opposés** $\pm\,p_0\hat u$, $\hat u\perp\vec C$ (par la puissance d'un point : le point $O$ a pour puissance $-(\rho^2-C^2)=-p_0^2$, et les cordes issues de $O$ perpendiculaires à $\vec C$ ont pour demi-longueur $p_0$). Inversement, la projection stéréographique transforme les cercles en cercles, et un cercle de $S^n$ qui coupe l'équateur en deux points antipodaux est un grand cercle. $\square$

*Conséquences.* (i) Les orbites képlériennes d'énergie $E$ sont paramétrées par l'ensemble des **grands cercles** de $S^n$, c'est-à-dire par le fibré unitaire tangent $T^1S^n$ : l'espace des orbites est un espace homogène de $SO(n+1)$. (ii) Moser montre qu'après le changement de temps $d\tau=dt/r$ (équivalent à l'**anomalie excentrique** comme paramètre), le flot de Kepler devient le **flot géodésique** de $S^n$ : tous les mouvements sont des rotations uniformes le long de grands cercles ; l'orbite est fermée (périodique en $\tau$) parce que **toutes les géodésiques de $S^n$ sont fermées de même longueur**. (iii) Les générateurs de $SO(n+1)$ sont $\mathsf L^{ij}$ (rotations des $n$ premières coordonnées) et $K^i$ (rotations dans les plans $(i,n+1)$).

# 3. Version quantique : Pauli, spectre de l'atome d'hydrogène

## 3.1 Opérateurs

$H=\dfrac{\hat p^2}{2m}-\dfrac{k}{\hat r}$, $\ \hat{\mathsf L}^{ij}=\hat x^i\hat p^j-\hat x^j\hat p^i$ (hermitiens), $[\hat x^i,\hat p_j]=i\hbar\delta^i{}_j$ ; en dimension 3, $\hat L_i=\tfrac12\varepsilon_{ijk}\hat{\mathsf L}^{jk}$ et le **RLL hermitien** (symétrisé, car $\vec p\times\vec L\neq-\vec L\times\vec p$ en quantique) est
$$
\boxed{\hat A^i=\tfrac12\left(\hat{\mathsf L}^{ij}\hat p_j-\hat p_j\hat{\mathsf L}^{ij}\right)-mk\,\frac{\hat x^i}{\hat r}\ \ \Big(\text{dim. 3 : }\hat{\vec A}=\tfrac12(\hat{\vec p}\times\hat{\vec L}-\hat{\vec L}\times\hat{\vec p})-mk\,\hat r\Big).}
$$
On admet (calcul direct, analogue quantique du §2.1) les relations de Pauli :
$$
[H,\hat A^i]=0,\quad[\hat L_i,\hat A_j]=i\hbar\,\varepsilon_{ijk}\hat A_k,\quad[\hat A_i,\hat A_j]=-2i\hbar\,mH\,\varepsilon_{ijk}\hat L_k,\quad\hat{\vec A}\cdot\hat{\vec L}=\hat{\vec L}\cdot\hat{\vec A}=0,
$$
$$
\hat A^2=m^2k^2+2mH\left(\hat L^2+\hbar^2\right).
$$
(Le terme en $\hbar^2$ dans $\hat A^2$ est un effet quantique de l'ordre des opérateurs : il remplace $L^2$ par $L^2+\hbar^2$ ; c'est lui qui donne, au §3.2, le spectre de Bohr exact.)

## 3.2 Spectre par l'algèbre $\mathfrak{so}(4)=\mathfrak{su}(2)\oplus\mathfrak{su}(2)$

Sur le sous-espace propre $H=E<0$, on pose $\hat{\vec K}=\hat{\vec A}/\sqrt{-2mE}$. Alors $[\hat K_i,\hat K_j]=i\hbar\varepsilon_{ijk}\hat L_k$, et les opérateurs
$$
\hat{\vec J}_\pm:=\tfrac12\left(\hat{\vec L}\pm\hat{\vec K}\right)\quad\text{vérifient}\quad[\hat J_{\pm i},\hat J_{\pm j}]=i\hbar\varepsilon_{ijk}\hat J_{\pm k},\quad[\hat J_{+i},\hat J_{-j}]=0 .
$$
Deux copies **commutantes** de $\mathfrak{su}(2)$. De $\hat L\cdot\hat K=0$ on déduit $\hat J_+^2=\hat J_-^2$, donc $j_+=j_-=j\in\{0,\tfrac12,1,\dots\}$, $J_\pm^2=\hbar^2j(j+1)$. Alors
$$
\hat L^2+\hat K^2=2\left(\hat J_+^2+\hat J_-^2\right)=4\hbar^2j(j+1).
$$
D'autre part $\hat L^2+\hat K^2=\hat L^2+\dfrac{m^2k^2+2mE(\hat L^2+\hbar^2)}{-2mE}=-\dfrac{mk^2}{2E}-\hbar^2$. Donc $-\dfrac{mk^2}{2E}=\hbar^2(4j(j+1)+1)=\hbar^2(2j+1)^2$ et, avec $N:=2j+1\in\{1,2,3,\dots\}$,
$$
\boxed{E_N=-\frac{mk^2}{2\hbar^2N^2}}\qquad(\text{niveaux de Bohr, } -13{,}6\ \mathrm{eV}/N^2\text{ pour l'hydrogène}).
$$
**Dégénérescence** : la représentation est $(j,j)$ de dimension $(2j+1)^2=N^2$ ; elle se décompose sous $\hat{\vec L}=\hat{\vec J}_++\hat{\vec J}_-$ en $\ell=0,1,\dots,2j=N-1$ : on retrouve les $N^2=\sum_{\ell=0}^{N-1}(2\ell+1)$ états. La dégénérescence en $\ell$ (« accidentelle » en apparence) est **la dégénérescence de la représentation de $SO(4)$**.

## 3.3 Dimension $n$ quelconque

L'algèbre est $\mathfrak{so}(n+1)$ et les niveaux sont des représentations symétriques traceless de rang $\ell$ (harmoniques sphériques de degré $\ell$ sur $S^n$). Le Casimir de $\mathfrak{so}(n+1)$ vaut $\hbar^2\ell(\ell+n-1)$ ; la relation $\hat L^2+\hat K^2=-\dfrac{mk^2}{2E}-\hbar^2\left(\dfrac{n-1}{2}\right)^2$ (généralisation de §3.2 ; pour $n=3$ on retrouve $-\hbar^2$) donne
$$
-\frac{mk^2}{2E}=\hbar^2\left(\ell+\frac{n-1}{2}\right)^2\ \Longrightarrow\ \boxed{E_N=-\frac{mk^2}{2\hbar^2\left(N+\frac{n-3}{2}\right)^2},\quad N=\ell+1\ge1},
$$
de dégénérescence $d_\ell=\dfrac{(2\ell+n-1)(\ell+n-2)!}{\ell!\,(n-1)!}$ (nombre d'harmoniques de degré $\ell$ sur $S^n$). Vérifications : $n=3$ : $d=(\ell+1)^2=N^2$ ; $n=2$ : $E_N=-\dfrac{mk^2}{2\hbar^2(N-\frac12)^2}$, $d=2N-1$ (atome d'hydrogène plan).

## 3.4 Preuve de Fock (espace des impulsions, $n=3$, $\hbar=1$)

La transformée de Fourier de $-k/r$ est $-4\pi k/q^2$. L'équation de Schrödinger en impulsion s'écrit
$$
\left(p^2+p_0^2\right)\phi(\vec p)=\frac{mk}{\pi^2}\int\frac{\phi(\vec p')}{|\vec p-\vec p'|^2}\,d^3p',\qquad p_0^2=-2mE .
$$
Avec $d^3p'=\left(\frac{p'^2+p_0^2}{2p_0}\right)^3d\Omega'$, la formule de distance de §2.4 et $\phi=c\,(p^2+p_0^2)^{-2}\,\Psi(\boldsymbol\xi)$, il vient
$$
\Psi(\boldsymbol\xi)=\frac{mk}{2\pi^2p_0}\int_{S^3}\frac{\Psi(\boldsymbol\xi')}{|\boldsymbol\xi-\boldsymbol\xi'|^2}\,d\Omega'
$$
(équation de valeur propre pour un **noyau invariant par $SO(4)$**). Ses vecteurs propres sont les harmoniques hypersphériques de degré $N-1$, de valeur propre $2\pi^2/N$ (par exemple pour $N=1$ : $\int_{S^3}\frac{d\Omega'}{4\sin^2(\chi/2)}=\pi\int_0^\pi\frac{\sin^2\chi}{\sin^2(\chi/2)}d\chi=2\pi^2$). La condition de valeur propre $\dfrac{mk}{2\pi^2p_0}\cdot\dfrac{2\pi^2}{N}=1$ donne $p_0=mk/N$, soit $E_N=-mk^2/(2N^2)$ : spectre retrouvé **sans aucune équation radiale**.

## 3.5 Rupture de la symétrie

Une perturbation qui n'est pas $SO(4)$-invariante lève la dégénérescence en $\ell$ : correction relativiste (terme $-\hat p^4/8m^3c^2$, **structure fine**), effet Lamb, polarisabilité d'un cœur, etc. La perturbation de **relativité générale** $\propto1/r^3$ en mécanique céleste est son analogue classique : elle fait précesser $\vec A$ (§4–5).

# 4. Perturbations : précession de $\vec A$

## 4.1 Équation du mouvement du RLL

Soit $H=H_0+\delta H$, avec $\delta H$ petit. Alors $\dot A^i=\{A^i,H\}=\{A^i,\delta H\}$ puisque $\{A^i,H_0\}=0$. Pour $\delta H=f(r)$ (perturbation centrale) :
$$
\{A^i,f(r)\}=-\frac{\partial A^i}{\partial p_j}\frac{\partial f}{\partial x^j}=-\frac{f'(r)}{r}\left(2x^is-r^2p^i-sx^i\right)=-\frac{f'(r)}{r}\,\mathsf L^{ij}x_j\ ,
$$
(utiliser $\partial A^i/\partial p_j=2x^ip^j-p^ix^j-s\delta^{ij}$). Donc
$$
\boxed{\dot A^i=-\frac{f'(r)}{r}\,\mathsf L^{ij}x_j\qquad(\text{dim. 3 : }\dot{\vec A}=\frac{f'(r)}{r}\,\vec L\times\vec x)} .
$$
$\vec L$ est conservé (perturbation centrale) et $\dot{\vec A}\perp\vec A$ n'est pas nécessairement vrai instantanément, mais **en moyenne** $\langle\dot{\vec A}\rangle\perp\vec A$ : $\vec A$ **tourne** dans le plan de l'orbite (précession du périhélie) avec une variation séculaire de sa norme nulle au premier ordre.

## 4.2 Moyenne sur une période

Pour une fonction de l'orbite képlérienne $F$ : $\langle F\rangle=\dfrac1T\oint F\,dt=\dfrac{m}{TL}\oint F\,r^2\,d\theta$ (loi des aires). En posant les axes de sorte que $\vec A\parallel\hat x$ (périhélie en $\theta=0$), $\vec L=L\hat z$ : $\ \langle\dot{\vec A}\rangle=\left\langle\frac{f'}{r}(\vec L\times\vec x)\right\rangle=L\,\hat z\times\left\langle\frac{f'}{r}\vec x\right\rangle$, et si $\left\langle\frac{f'}{r}\vec x\right\rangle=\mathcal C\,\hat x$ (la composante en $\hat y$ s'annule par la symétrie $\theta\to-\theta$), alors $\langle\dot{\vec A}\rangle=L\,\mathcal C\,\hat y$ : $\vec A$ tourne **dans le sens du mouvement** si $\mathcal C>0$, à la vitesse angulaire $\dot\varpi=L\,\mathcal C/\|\vec A\|$.

**Équivalent par les éléments de Delaunay.** Avec $G=L$ (moment cinétique) et $a$ fixé, $\ \dot\varpi=\dfrac{\partial\langle\delta H\rangle}{\partial G}$ (moyenne sur l'orbite képlérienne) : les deux méthodes concordent (§5.4).

# 5. L'avance du périhélie de Mercure

## 5.1 Données d'observation

Le périhélie de Mercure (demi-grand axe $a=5{,}791\times10^{10}$ m, $e=0{,}2056$, $T=87{,}969$ j, soit environ $415{,}2$ révolutions par siècle) avance, par rapport aux étoiles fixes (repère de l'équinoxe précessant), de $\approx5600''$ par siècle (« siècle julien »). Le bilan classique (valeurs arrondies, à vérifier dans les éphémérides récentes) :

| Cause | Précession $(''/\text{siècle})$ |
| --- | --- |
| Précession générale des équinoxes (changement de repère) | $\approx5025{,}6$ |
| Perturbations newtoniennes des planètes (Vénus $\approx278$, Jupiter $\approx154$, Terre $\approx90$, Saturne $\approx7{,}3$, Mars $\approx2{,}5$, autres $\lesssim0{,}2$) | $\approx531{,}6$ |
| Relativité générale (Schwarzschild) | $\approx42{,}98$ |
| Aplatissement solaire $J_2$ (négligeable) | $\approx0{,}03$ |
| Total prédit | $\approx5600{,}2$ |
| Observé | $\approx5599{,}7\pm0{,}4$ |

Le **résidu inexpliqué** découvert par Le Verrier (1859, environ $38''$) puis précisé par Newcomb ($43''$ en 1882) est expliqué par la relativité générale en 1915 [^4] : c'est la grande confirmation initiale de la théorie.

## 5.2 Dérivation par la métrique de Schwarzschild (planète test dans le plan équatorial)

**Métrique** (rayon de Schwarzschild $r_s=2GM/c^2$, coordonnées $(t,r,\varphi)$) :
$$
ds^2=-\left(1-\frac{r_s}{r}\right)c^2dt^2+\frac{dr^2}{1-r_s/r}+r^2d\varphi^2 .
$$
Le lagrangien géodésique est indépendant de $t$ et de $\varphi$ : **Noether** donne deux intégrales premières (temps propre $\tau$, $\dot{}=d/d\tau$)
$$
\left(1-\frac{r_s}{r}\right)\dot t=\varepsilon\ (\text{énergie par unité de }mc^2),\qquad r^2\dot\varphi=h\ (\text{moment cinétique par unité de masse}).
$$
La normalisation $g_{\mu\nu}\dot x^\mu\dot x^\nu=-c^2$ s'écrit $-\dfrac{c^2\varepsilon^2}{1-r_s/r}+\dfrac{\dot r^2}{1-r_s/r}+\dfrac{h^2}{r^2}=-c^2$, soit
$$
\dot r^2=c^2\varepsilon^2-\left(1-\frac{r_s}{r}\right)\left(c^2+\frac{h^2}{r^2}\right).
$$
Avec $u=1/r$ et $\dot r=-h\,u'$ ($'=d/d\varphi$) :
$$
h^2u'^2=c^2(\varepsilon^2-1)+c^2r_su-h^2u^2+r_sh^2u^3 .
$$
**Équation de Binet relativiste** : on dérive par rapport à $\varphi$ et on divise par $2h^2u'$ :
$$
\boxed{u''+u=\frac{GM}{h^2}+\frac{3GM}{c^2}\,u^2}\qquad\left(\text{Newton : }u''+u=\frac{GM}{h^2}\right).
$$
Le terme $3GMu^2/c^2$ (rapport $\sim3GM/(c^2p)\sim5\times10^{-8}$ pour Mercure) est la correction relativiste.

## 5.3 Résolution perturbative

Posons $p=h^2/GM$, $\delta=3GM/c^2$ et $\epsilon:=\delta/p$ ($\ll1$). À l'ordre 0, $u_0=\dfrac{1+e\cos\varphi}{p}$. À l'ordre 1, $u=u_0+u_1$ avec
$$
u_1''+u_1=\delta\,u_0^2=\frac{\delta}{p^2}\left[1+\frac{e^2}{2}+2e\cos\varphi+\frac{e^2}{2}\cos2\varphi\right].
$$
Les termes constant et en $\cos2\varphi$ donnent des corrections périodiques bornées (de l'ordre $\delta/p^2$), négligeables en moyenne. Le terme **résonant** $2e\cos\varphi$ (même fréquence que l'oscillateur homogène) donne la solution séculaire $\dfrac{\delta e}{p^2}\,\varphi\sin\varphi$ (on vérifie $(\varphi\sin\varphi)''+\varphi\sin\varphi=2\cos\varphi$). Donc
$$
u\simeq\frac1p\left[1+e\cos\varphi+\epsilon\,e\,\varphi\sin\varphi\right]\simeq\frac1p\left[1+e\cos\big((1-\epsilon)\varphi\big)\right],\qquad\epsilon=\frac{3GM}{c^2p}.
$$
(on a utilisé $\cos(\varphi-\epsilon\varphi)\simeq\cos\varphi+\epsilon\varphi\sin\varphi$, valable pour $\epsilon\varphi\ll1$, c'est-à-dire sur quelques révolutions). L'orbite n'est plus fermée : $r$ revient à sa valeur minimale quand $(1-\epsilon)\varphi=2\pi$, soit après $\varphi=2\pi/(1-\epsilon)\simeq2\pi(1+\epsilon)$. D'où l'**avance du périhélie par révolution**
$$
\boxed{\Delta\varpi=2\pi\epsilon=\frac{6\pi GM}{c^2\,p}=\frac{6\pi GM}{c^2a(1-e^2)}=\frac{24\pi^3a^2}{c^2T^2(1-e^2)}=\frac{3\pi r_s}{p}}
$$
(forme d'Einstein [^4], avec $GM=4\pi^2a^3/T^2$). **Sens** : dans le sens du mouvement (prograde).

## 5.4 Dérivation par le RLL : perturbation en $-\beta/r^3$

Reécrivons l'équation de Binet comme une équation de force centrale newtonienne : $\ddot r-\dfrac{h^2}{r^3}=-\dfrac{GM}{r^2}-\dfrac{3GMh^2}{c^2r^4}$, c'est-à-dire **mouvement newtonien dans** $V(r)=-\dfrac{GM}{r}+\delta V(r)$, $\delta V=-\dfrac{\beta}{r^3}$, avec $\beta=\dfrac{GM\,h^2}{c^2}$ (par unité de masse). $h$ est une constante du mouvement de ce problème central : on peut donc traiter $\beta$ comme une **constante** pendant l'évolution. Par unité de masse, $\mu=GM$, $L\to h$, $\|\vec A\|=\mu e$.

D'après §4.1 avec $f=-\beta/r^3$, $f'=3\beta/r^4$ : $\ \dot{\vec A}=\dfrac{3\beta}{r^5}\,\vec h\times\vec x$. Moyenne ($\vec A\parallel\hat x$, périhélie en $\theta=0$, $\vec h=h\hat z$, loi des aires $dt=r^2d\theta/h$) :
$$
\left\langle\frac{\vec x}{r^5}\right\rangle=\frac{1}{Th}\oint\frac{(\cos\theta,\sin\theta)}{r^2}\,d\theta=\frac{1}{Thp^2}\oint(1+e\cos\theta)^2\cos\theta\,d\theta\,\hat x=\frac{2\pi e}{Th\,p^2}\,\hat x ,
$$
car $\oint\cos\theta\,(1+2e\cos\theta+e^2\cos^2\theta)\,d\theta=2\pi e$ et la composante en $\sin\theta$ s'annule. Donc
$$
\langle\dot{\vec A}\rangle=3\beta\,h\,\hat z\times\frac{2\pi e}{Thp^2}\hat x=\frac{6\pi\beta\,e}{Tp^2}\,\hat y,\qquad\dot\varpi=\frac{\|\langle\dot{\vec A}\rangle\|}{\|\vec A\|}=\frac{6\pi\beta}{T\mu p^2}.
$$
Par révolution : $\Delta\varpi=\dot\varpi\,T=\dfrac{6\pi\beta}{\mu p^2}=\dfrac{6\pi\mu h^2}{c^2\,\mu\,p^2}\ \Big(\text{avec }h^2=\mu p\Big)=\dfrac{6\pi\mu}{c^2p}$. ✓ **Identique** à la valeur trouvée par la méthode de Binet. De plus $\langle\dot{\vec A}\rangle\propto\hat y$ est **perpendiculaire à $\vec A$** : la norme de $\vec A$ (donc $e$) n'a pas de variation séculaire ; seule l'**orientation** change.

*Variante par Delaunay.* $\langle1/r^3\rangle=\dfrac{1}{a^3(1-e^2)^{3/2}}$ et $\sqrt{1-e^2}=G/\sqrt{\mu a}$ donnent $\langle\delta H\rangle=-\dfrac{\beta\mu^{3/2}}{a^{3/2}G^3}$ ; alors $\dot\varpi=\partial\langle\delta H\rangle/\partial G=\dfrac{3\beta\mu^{3/2}}{a^{3/2}G^4}$ et $\Delta\varpi=\dot\varpi\cdot2\pi\sqrt{a^3/\mu}=\dfrac{6\pi\beta\mu}{G^4}=\dfrac{6\pi\mu}{c^2p}$ ✓.

## 5.5 Vérification post-newtonienne (1PN)

Pour une planète test dans le champ de masse $M$ (coordonnées harmoniques, par unité de masse), le lagrangien 1PN est $L=\frac{v^2}{2}+\frac\mu r+\frac1{c^2}\left[\frac{v^4}{8}+\frac{3\mu v^2}{2r}-\frac{\mu^2}{2r^2}\right]$, d'où $H=\frac{p^2}{2}-\frac\mu r+\frac1{c^2}\left[-\frac{p^4}{8}-\frac{3\mu p^2}{2r}+\frac{\mu^2}{2r^2}\right]$. En remplaçant $p^2=2(E+\mu/r)$ dans la correction :
$$
H_1=\frac1{c^2}\left[-\frac{E^2}{2}-\frac{4E\mu}{r}-\frac{3\mu^2}{r^2}\right].
$$
À $E=-\mu/2a$ **fixée**, seul le terme $-3\mu^2/(c^2r^2)$ dépend de $G$ après moyenne ; $\langle1/r^2\rangle=\dfrac{\sqrt\mu}{a^{3/2}G}$ donne $\langle H_1\rangle\ni-\dfrac{3\mu^{5/2}}{c^2a^{3/2}G}$, $\ \dot\varpi=\dfrac{\partial\langle H_1\rangle}{\partial G}=\dfrac{3\mu^{5/2}}{c^2a^{3/2}G^2}$ et $\Delta\varpi=\dfrac{6\pi\mu^2}{c^2G^2}=\dfrac{6\pi\mu}{c^2p}$. ✓ Même résultat dans un **autre système de coordonnées** (le résultat physique, un angle entre deux passages au périhélie, est indépendant de la jauge).

## 5.6 Application numérique à Mercure

$GM_\odot=1{,}327\times10^{20}\ \mathrm{m^3\,s^{-2}}$, $c=2{,}998\times10^8$ m/s ⇒ $GM_\odot/c^2=1{,}477$ km, $p=a(1-e^2)=5{,}791\times10^{10}\times0{,}9577=5{,}545\times10^{10}$ m.
$$
\Delta\varpi=\frac{6\pi\times1{,}477\times10^3}{5{,}545\times10^{10}}=5{,}02\times10^{-7}\ \text{rad par révolution}.
$$
Par siècle : $415{,}2\times5{,}02\times10^{-7}=2{,}084\times10^{-4}$ rad $=\ \mathbf{43{,}0''}$, soit $0{,}1''$ par révolution environ (qui expliquait l'impossibilité d'une mesure directe en une seule orbite). **Hors Mercure** (même formule) : Vénus $8{,}6''$, Terre $3{,}8''$, Mars $1{,}35''$ par siècle.

## 5.7 Les 532″ newtoniennes : théorie séculaire (ordre de grandeur et méthode)

Un perturbateur extérieur (masse $m'$, orbite circulaire coplanaire de rayon $a'$) agit sur Mercure ($a<a'$, $\alpha=a/a'$). La fonction perturbatrice moyennée sur les deux orbites (développée en $\alpha$) est $\langle\mathscr R\rangle=\dfrac{Gm'}{a'}\left[\dfrac{\alpha^2}{4}\left(1+\dfrac32e^2\right)+O(\alpha^4)\right]$ ; l'équation de Lagrange coplanaire $\dot\varpi=\dfrac{\sqrt{1-e^2}}{na^2e}\dfrac{\partial\langle\mathscr R\rangle}{\partial e}$ donne, avec $n^2a^3=GM$,
$$
\dot\varpi\simeq\frac34\,n\,\frac{m'}{M}\,\alpha^3\sqrt{1-e^2}\qquad(\text{plus généralement }\dot\varpi=\tfrac14n\tfrac{m'}{M}\alpha^2b^{(1)}_{3/2}(\alpha)\sqrt{1-e^2}\ \text{à }e\to0),
$$
avec le coefficient de Laplace $b^{(1)}_{3/2}(\alpha)=3\alpha\left[1+\tfrac{15}{8}\alpha^2+\tfrac{175}{64}\alpha^4+\tfrac{3675}{1024}\alpha^6+\cdots\right]$ [^5].
**Jupiter** ($\alpha=0{,}0744$, $m'/M=9{,}55\times10^{-4}$, $n=2609$ rad/siècle) : $\dot\varpi\simeq0{,}75\times2609\times9{,}55\times10^{-4}\times4{,}12\times10^{-4}\times0{,}979=7{,}5\times10^{-4}$ rad/siècle $\approx156''$ (valeur de référence $153{,}6''$ ✓). **Vénus** ($\alpha=0{,}535$, $m'/M=2{,}45\times10^{-6}$) : le terme dominant seul vaut $\approx148''$ ; avec la série (facteur $\approx1{,}9$) on obtient $\approx280''$ ($\approx278''$ de référence). **Terre** ($\alpha=0{,}387$) : $\approx95''$ (réf. $90''$). Le **total** newtonien $\approx532''$ est dominé par Vénus, la Terre et Jupiter.

## 5.8 Lecture en termes de symétrie

- Le potentiel $-k/r$ possède la symétrie $SO(n+1)$ ($SO(4)$) : $\vec A$ fixe, orbites fermées.
- Toute perturbation qui n'a pas cette symétrie (terme en $1/r^3$ de la relativité générale, quadrupôle d'un perturbateur, aplatissement solaire $J_2$) **brise** la symétrie cachée et fait précesser $\vec A$ : $\mathfrak{so}(4)\to\mathfrak{so}(3)$ (le moment cinétique reste conservé tant que la perturbation est centrale).
- En quantique, c'est la **levée de dégénérescence en $\ell$** : au premier ordre $\Delta E_{N\ell}=\langle\delta H\rangle_{N\ell}$, et la précession classique de $\vec A$ est la fréquence $\dot\varpi=\dfrac1\hbar\dfrac{\partial\Delta E}{\partial\ell}$ (correspondance de Bohr, $L\leftrightarrow\hbar\ell$). Pour $\delta H\propto1/r^3$ on utilise $\langle r^{-3}\rangle_{N\ell}=\dfrac{1}{a_0^3N^3\,\ell(\ell+\frac12)(\ell+1)}$ (pour l'hydrogène, rayon de Bohr $a_0$), ce qui produit la structure fine ; le détail relève de la physique atomique.

# 6. Exercices corrigés

## Exercice 1 — Pendule de Foucault

**Énoncé.** Un pendule sphérique simple (longueur $\ell$, masse $m$) oscille à petite amplitude à la latitude $\lambda$ sur la Terre, de vitesse angulaire $\Omega$ ($\Omega=2\pi/T_{\rm sid}$, $T_{\rm sid}=23{,}934$ h). Déterminer le mouvement dans le référentiel terrestre, la période de rotation du plan d'oscillation, et la valeur à Paris ($\lambda=48{,}85^\circ$).

**Solution.** Référentiel terrestre $\mathscr R'=(\text{Est},\text{Nord},\text{Haut})\equiv(x,y,z)$ ; $\vec\Omega=\Omega(\cos\lambda\,\hat y+\sin\lambda\,\hat z)$. D'après §2.3 de M1, on néglige la centrifuge (absorbée dans $\vec g$) et on garde Coriolis :
$$
m\vec a'=\vec T+m\vec g-2m\,\vec\Omega\times\vec v',\qquad\omega_0^2=g/\ell .
$$
Pour de petites oscillations, $z\approx0$, $v_z\approx0$, et la tension projetée sur l'horizontale vaut $-m\omega_0^2(x,y)$. Avec $\vec v'=(\dot x,\dot y,0)$ :
$$
\vec\Omega\times\vec v'=(-\Omega\sin\lambda\,\dot y,\ \Omega\sin\lambda\,\dot x,\ -\Omega\cos\lambda\,\dot x)\ \Rightarrow\ 
\ddot x=2\Omega_z\dot y-\omega_0^2x,\quad\ddot y=-2\Omega_z\dot x-\omega_0^2y,\quad\Omega_z=\Omega\sin\lambda .
$$
Seule la composante verticale $\Omega_z$ de la rotation intervient dans le plan horizontal (la composante $\Omega\cos\lambda$ donne une force verticale d'ordre supérieur). Avec $\zeta=x+iy$ :
$$
\ddot\zeta+2i\Omega_z\dot\zeta+\omega_0^2\zeta=0\ \Rightarrow\ \zeta(t)=e^{-i\Omega_zt}\left(\mathcal Ae^{i\omega t}+\mathcal Be^{-i\omega t}\right),\qquad\omega=\sqrt{\omega_0^2+\Omega_z^2}\simeq\omega_0 .
$$
L'oscillation (dans le plan tournant) est périodique de pulsation $\omega\simeq\omega_0$ et le plan d'oscillation **tourne à la vitesse $-\Omega\sin\lambda$** (sens horaire dans l'hémisphère nord, vu de dessus), de période
$$
\boxed{T_F=\frac{T_{\rm sid}}{\sin\lambda}}\ .
$$
À Paris : $\sin48{,}85^\circ=0{,}7527$, $T_F=31{,}8$ h, soit une rotation de $\approx11{,}3^\circ/$h (pôle : $T_F=T_{\rm sid}$ ; équateur : $T_F=\infty$ ; hémisphère sud : sens inverse).

*Lecture géométrique.* Le plan d'oscillation est transporté **parallèlement** le long d'un cercle de latitude : l'angle de rotation sur un tour est $2\pi\sin\lambda$ (aire solide du cône tangent, $\Omega_{\rm sol}=2\pi(1-\cos\vartheta)$ avec $\vartheta=\pi/2-\lambda$ : la holonomie de la sphère $S^2$). *Version $n$ dimensions* : la rotation d'une base orthonormée mobile est portée par $\Omega\in\mathfrak{so}(n)$ ; seule la projection de $\Omega$ sur le plan du mouvement (ici $\Omega_z$) agit sur ce plan.

## Exercice 2 — Toupie symétrique (toupie de Lagrange)

**Énoncé.** Solide de révolution (moments d'inertie $I_1=I_2$ et $I_3$ par rapport à un point fixe $O$ de l'axe de symétrie), masse $m$, centre de masse à la distance $\ell$ de $O$ sur l'axe, dans le champ de pesanteur. Utiliser les angles d'Euler $(\varphi,\theta,\psi)$ (précession, nutation, rotation propre). Déterminer les intégrales premières, la précession régulière à grande vitesse de rotation propre, et la condition de la « toupie endormie ».

**Solution.** $T=\tfrac12I_1\left(\dot\theta^2+\dot\varphi^2\sin^2\theta\right)+\tfrac12I_3\left(\dot\psi+\dot\varphi\cos\theta\right)^2$, $V=mg\ell\cos\theta$, $L=T-V$ ($\theta$ angle de l'axe avec la verticale ascendante).

*Intégrales premières (Noether).* $\varphi$ et $\psi$ sont cycliques (invariance par rotation autour de la verticale et autour de l'axe de la toupie), et $\partial_tL=0$ :
$$
p_\psi=I_3\omega_3,\quad\omega_3:=\dot\psi+\dot\varphi\cos\theta;\qquad p_\varphi=\left(I_1\sin^2\theta+I_3\cos^2\theta\right)\dot\varphi+I_3\cos\theta\,\dot\psi=I_1\dot\varphi\sin^2\theta+p_\psi\cos\theta;\qquad E=T+V .
$$
($p_\varphi=L_z$ et $p_\psi=L_{z'}$ : composantes de $\vec L$ sur les deux axes.) L'énergie réduite devient $E'=E-\frac{p_\psi^2}{2I_3}=\tfrac12I_1\dot\theta^2+U_{\rm eff}(\theta)$, avec
$$
U_{\rm eff}(\theta)=\frac{(p_\varphi-p_\psi\cos\theta)^2}{2I_1\sin^2\theta}+mg\ell\cos\theta :
$$
**problème à un degré de liberté** (intégrable ; avec $u=\cos\theta$ : $\dot u^2=f(u)$ cubique, fonctions elliptiques).

*Précession régulière.* L'équation en $\theta$ vaut $I_1\ddot\theta=I_1\dot\varphi^2\sin\theta\cos\theta-I_3\omega_3\dot\varphi\sin\theta+mg\ell\sin\theta$. Pour $\theta=\theta_0$ constant (précession pure, $\dot\varphi=\Omega_p$) :
$$
I_1\cos\theta_0\,\Omega_p^2-I_3\omega_3\Omega_p+mg\ell=0\ \Rightarrow\ \Omega_p=\frac{I_3\omega_3\pm\sqrt{I_3^2\omega_3^2-4I_1mg\ell\cos\theta_0}}{2I_1\cos\theta_0}.
$$
Racine **lente** quand $I_3^2\omega_3^2\gg4I_1mg\ell$ (toupie rapide) : $\ \boxed{\Omega_p\simeq\dfrac{mg\ell}{I_3\omega_3}}$ ; c'est la **loi gyroscopique** $\dot{\vec L}=\vec\Gamma$ : $\vec L\simeq I_3\omega_3\hat u$ ($\hat u$ = axe de la toupie, orienté du pivot vers $G$) et le couple du poids en $O$ est $\vec\Gamma=\ell\hat u\times(-mg\hat z)=mg\ell\,\hat z\times\hat u$, donc $I_3\omega_3\dot{\hat u}=mg\ell\,\hat z\times\hat u$, soit $\dot{\hat u}=\dfrac{mg\ell}{I_3\omega_3}\,\hat z\times\hat u$ : l'axe précesse à la vitesse $mg\ell/(I_3\omega_3)$ autour de la verticale, **dans le sens de la rotation propre** si l'axe est au-dessus du pivot. La racine rapide $\Omega_p\simeq I_3\omega_3/(I_1\cos\theta_0)$ correspond à un autre régime.
*Nutation.* Les petites oscillations de $\theta$ autour de $\theta_0$ pour une toupie rapide ont pour pulsation $\omega_n\simeq I_3\omega_3/I_1$ (rapide, de faible amplitude).

*Toupie endormie ($\theta=0$).* Linéarisation de l'équation en $\theta$ avec $p_\varphi=p_\psi$ : $\ I_1\ddot\theta=\left(mg\ell-\frac{I_3^2\omega_3^2}{4I_1}\right)\theta$ ; la position verticale est **stable** si
$$
\boxed{\omega_3^2>\frac{4I_1mg\ell}{I_3^2}}\ .
$$
Quand les frottements ralentissent $\omega_3$ jusqu'à cette valeur, la toupie se réveille et s'écarte de la verticale.

## Exercice 3 — Cerceau

### (a) Cerceau qui roule sans glisser sur un plan incliné

**Énoncé.** Un cerceau (anneau mince, masse $m$, rayon $R$, $I_G=mR^2$) descend un plan incliné d'angle $\alpha$ en roulant sans glisser. Accélération et condition de non-glissement.

**Solution.** Soit $x$ l'abscisse de $G$ le long de la pente, $\dot x=R\omega$ (roulement sans glissement : la vitesse du point de contact est nulle, $\vec v_G+\vec\omega\times\overrightarrow{GI}=0$). Koenig : $T=\tfrac12m\dot x^2+\tfrac12I_G\omega^2=\tfrac12\left(m+\dfrac{I_G}{R^2}\right)\dot x^2=m\dot x^2$ ; $V=-mgx\sin\alpha$. Lagrange (liaison holonome, la force de frottement ne travaille pas) :
$$
2m\ddot x=mg\sin\alpha\ \Rightarrow\ \boxed{a=\tfrac12g\sin\alpha}\qquad(\text{plein disque : }\tfrac23g\sin\alpha;\ \text{bille : }\tfrac57g\sin\alpha).
$$
Frottement (TRD + TMC\* en $G$) : $ma=mg\sin\alpha-f$ donne $f=\tfrac12mg\sin\alpha$ ; la réaction normale est $N=mg\cos\alpha$. Pas de glissement si $f\le\mu N$ :
$$
\boxed{\mu\ge\tfrac12\tan\alpha}.
$$
*Remarque.* Cette accélération est **indépendante de $m$ et de $R$** ; plus la masse est près de la périphérie ($I_G$ grand), plus la descente est lente.

### (b) Perle sur un cerceau tournant (système à liaison dépendant du temps)

**Énoncé.** Un cerceau vertical de rayon $R$ tourne à vitesse angulaire constante $\omega$ autour de son diamètre vertical. Une perle (masse $m$) coulisse sans frottement ; $\theta$ est l'angle avec la verticale descendante. Étudier l'équilibre, la stabilité, et discuter les intégrales premières.

**Solution.** Position : $x_{\perp}=R\sin\theta$ (distance à l'axe), $z=-R\cos\theta$. $T=\tfrac12mR^2\left(\dot\theta^2+\omega^2\sin^2\theta\right)$, $V=-mgR\cos\theta$ :
$$
L=\tfrac12mR^2\dot\theta^2+\tfrac12mR^2\omega^2\sin^2\theta+mgR\cos\theta\ \Rightarrow\ \ddot\theta=\sin\theta\left(\omega^2\cos\theta-\frac gR\right).
$$
*Intégrale première.* $L$ ne dépend pas explicitement du temps : $H=p_\theta\dot\theta-L=\tfrac12mR^2\dot\theta^2-\tfrac12mR^2\omega^2\sin^2\theta-mgR\cos\theta$ est **conservée** (Noether, translation en temps), mais $H\ne T+V$ : l'**énergie mécanique $T+V$ n'est pas conservée** (l'axe tournant fournit de l'énergie par la liaison), c'est $H=T+V-mR^2\omega^2\sin^2\theta$ qui l'est ; $H$ s'interprète en référentiel tournant comme énergie avec le potentiel centrifuge $-\frac12mR^2\omega^2\sin^2\theta$.
*Équilibres.* $\theta=0$ (bas) toujours ; $\theta=\pi$ (haut) ; et, **si $\omega^2>g/R$**, $\cos\theta_0=\dfrac{g}{R\omega^2}$.
*Stabilité.* Linéarisation autour de $\theta_*$ : $\ddot{\delta\theta}=\left[\omega^2\cos(2\theta_*)-\dfrac gR\cos\theta_*\right]\delta\theta$.
- $\theta_*=0$ : $\omega_{\rm osc}^2=\dfrac gR-\omega^2$ : stable si $\omega<\sqrt{g/R}$, **instable** au-delà.
- $\theta_*=\pi$ : $\omega_{\rm osc}^2=-\left(\dfrac gR+\omega^2\right)<0$ : toujours instable.
- $\theta_0$ (pour $\omega^2>g/R$) : $\omega_{\rm osc}^2=\omega^2\sin^2\theta_0=\omega^2-\dfrac{g^2}{R^2\omega^2}>0$ : **stable**.
Il s'agit d'une **bifurcation en fourche** (brisure de symétrie $\theta\to-\theta$) au seuil $\omega_c=\sqrt{g/R}$ : au-dessus du seuil, le point bas devient instable et deux positions stables symétriques $\pm\theta_0$ apparaissent.

# 7. Contrôles de cohérence

>[!question]- Vérifications utiles
>1. $A^2=m^2k^2+2mEL^2$ donne $e=\|\vec A\|/(mk)$ ; $\vec A$ pointe vers le périhélie.
>2. Classique $\{A^i,A^j\}=-2mH\mathsf L^{ij}$ ↔ quantique $[\hat A_i,\hat A_j]=-2i\hbar mH\varepsilon_{ijk}\hat L_k$ (règle $\{\,,\}\to-\tfrac{i}{\hbar}[\,,]$).
>3. $E<0$ : $\mathfrak{so}(n+1)$ ; $E=0$ : $\mathfrak e(n)$ ; $E>0$ : $\mathfrak{so}(n,1)$.
>4. Mercure : $\Delta\varpi=6\pi GM/(c^2p)$ **par révolution**, $\approx43''$ par siècle ; sens prograde.
>5. Foucault : $T_F=T_{\rm sid}/\sin\lambda$ ; toupie rapide : $\Omega_p=mg\ell/(I_3\omega_3)$ ; cerceau incliné : $a=\tfrac12g\sin\alpha$, $\mu\ge\tfrac12\tan\alpha$.
>6. Les valeurs numériques des éphémérides (contributions planétaires, précession générale) sont **données de mémoire à titre indicatif** et doivent être vérifiées dans une référence récente avant d'être citées.
