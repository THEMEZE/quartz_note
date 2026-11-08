---
title: Problème de Kepler, vecteur de Runge–Lenz–Laplace, $SO(n+1)$
tags:
  - Physique
  - Mathematiques
lang: fr
partie: VIII
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Problème de Kepler, vecteur de Runge–Lenz–Laplace, $SO(n+1)$

## VIII.1 Classique, dimension $n$

$H=\dfrac{p^2}{2m}-\dfrac kr$ ($k>0$). Charges : $E$, $L_{ij}=x_ip_j-x_jp_i$ (donc mouvement plan), et le **vecteur RLL**
$$
A^i\doteq L^{ij}p_j-mk\,\frac{x^i}r\qquad\Big(\text{3D : }\vec A=\vec p\times\vec L-mk\,\hat r\Big).
$$
Propriétés : $\{A_i,H\}=0$ ; $A\cdot L=0$ ; $A^2=m^2k^2+2mE\,L^2$ (où $L^2\doteq\tfrac12L_{ij}L^{ij}$).
**Trajectoire** : $\vec A\cdot\vec r=Ar\cos\theta=L^2-mkr\Rightarrow$
$$
r(\theta)=\frac{p}{1+e\cos\theta},\quad p=\frac{L^2}{mk},\ e=\frac{|A|}{mk}=\sqrt{1+\frac{2EL^2}{mk^2}} .
$$
**Hodographe** : $p$ décrit un cercle de rayon $mk/L$ de centre déporté de $A/L$ (cercle de vitesses : cf. IX).

> [!note] Dans $\mathbb R^n$, le potentiel « de Kepler » naturel est $1/r^{n-2}$ (solution fondamentale du laplacien, I.3) ; le résultat $SO(n+1)$ ci-dessous vaut pour le potentiel en $1/r$ **en dimension $n$** (cas de Bertrand), pas pour $1/r^{n-2}$.

## VIII.2 Algèbre hamiltonienne et trois régimes

$\{L_{ij},A_k\}=\delta_{ik}A_j-\delta_{jk}A_i$ (vecteur), et
$$
\{A_i,A_j\}=-2mH\,L_{ij}\quad(\text{à la convention de signe près selon }L_{ij}).
$$
En posant, pour $E<0$, $D_i\doteq A_i/\sqrt{-2mE}$, on obtient $\{D_i,D_j\}=L_{ij}$ : $\mathfrak{so}(n+1)$ ; $E>0$ : $\mathfrak{so}(n,1)$ ; $E=0$ : $\mathfrak e(n)$. **Compte** : $\tfrac{n(n-1)}2+n=\tfrac{n(n+1)}2=\dim\mathfrak{so}(n+1)=\dim\mathfrak e(n)$ : le couple $(L,A)$ a autant de composantes qu'un torseur de $\mathbb R^n$.
- **Fock–Moser** : la projection stéréographique de l'espace des impulsions $\mathbb R^n$ sur $S^n$ transforme le flot de Kepler à $E<0$ en flot géodésique sur $S^n$ (grands cercles) ; $SO(n+1)$ est la symétrie isométrique de $S^n$.
- $n=3$ : $\mathfrak{so}(4)=\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ via $J^\pm=\tfrac12(L\pm D)$.

## VIII.3 Version quantique (Pauli)

$\hat A=\frac1{2m}(\hat p\times\hat L-\hat L\times\hat p)-k\hat r/r$, $[\hat A_i,\hat A_j]=-\tfrac{2i\hbar}m\hat H\varepsilon_{ijk}\hat L_k$. Pour $H<0$, $\hat D=\sqrt{-m/2\hat H}\,\hat A$, $[\hat D_i,\hat D_j]=i\hbar\varepsilon_{ijk}\hat L_k$ ; $j^+=j^-=j$ (car $L\cdot D=0$), $N=2j+1$ :
$$
E_N=-\frac{mk^2}{2\hbar^2N^2},\qquad\text{dégénérescence }N^2=\sum_{\ell=0}^{N-1}(2\ell+1).
$$
**Dimension $n$** : représentation de $\mathfrak{so}(n+1)$ à $\ell$ **symétrique sans trace** de $\mathfrak{so}(n+1)$ (harmoniques sphériques sur $S^n$) :
$$
E_\ell=-\frac{mk^2}{2\hbar^2\big(\ell+\tfrac{n-1}2\big)^2},\qquad g_\ell=\binom{\ell+n}{n}-\binom{\ell+n-2}{n}\quad(\ell\in\mathbb N).
$$
Contrôle : $n=3$, $\ell=N-1$ : $g=N^2$ ; $n=2$ : $E=-\frac{2mk^2}{\hbar^2(2\ell+1)^2}$, $g=2\ell+1$.
**Brisure** : tout écart à $1/r$ ($1/r^3$ relativiste, effet Lamb, potentiel écranté) brise $SO(n+1)\to SO(n)$ et lève la dégénérescence en $\ell$.

## VIII.4 Perturbation : précession de $A$ et périhélie de Mercure

Pour $H=H_0+\delta H$ : $\dot A_i=\{A_i,\delta H\}$ ; moyenne sur l'orbite $\Rightarrow$ rotation de $\vec A$ dans le plan. Pour $\delta V=-\beta/r^3$ :
$$
\Delta\varphi_{\text{orbite}}=\frac{6\pi m\beta}{L^2\,p}\qquad\Big(p=\frac{L^2}{mk}\Big).
$$
**Relativité générale (Schwarzschild)** : le terme post-newtonien $\beta=GML^2/(mc^2)$ ($\beta$ est alors proportionnelle à $L^2$) donne
$$
\boxed{\Delta\varphi=\frac{6\pi GM}{c^2\,a(1-e^2)}\ \text{rad par révolution}}\ \Longrightarrow\ \text{Mercure : }0{,}1038''\text{ par orbite}\simeq43''\text{ par siècle}.
$$
Décomposition du total observé ($\simeq5600''$/siècle) : $\simeq5025''$ (précession des équinoxes, repère) $+\ \simeq532''$ (perturbations newtoniennes des autres planètes) $+\ 43''$ (relativité). Lecture en termes de symétrie : la précession mesure la brisure de $SO(4)$ par le $1/r^3$.
Dérivation par Schwarzschild : $u=1/r$, $u''+u=\frac{GM}{\ell^2}+\frac{3GM}{c^2}u^2$ ; solution perturbative $u=\frac1p\big[1+e\cos((1-\varepsilon)\varphi)\big]$, $\varepsilon=\frac{3GM}{c^2p}$, $\Delta\varphi\simeq2\pi\varepsilon=6\pi GM/(c^2p)$.
