---
title: Géométrie : tenseurs, bivecteurs, opérateurs différentiels
tags:
  - Physique
  - Mathematiques
lang: fr
partie: I
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Géométrie : tenseurs, bivecteurs, opérateurs différentiels

## I.1 Métrique et coordonnées

Variété $(M,g)$ (pseudo-)riemannienne de dimension $n$, coordonnées $q^i$, base naturelle $e_i\doteq\partial_i$, $g_{ij}\doteq g(e_i,e_j)$, $g^{ij}$ l'inverse, $g\doteq\det(g_{ij})$.

- Musicaux : $v_i = g_{ij}v^j$ ($\flat$), $\alpha^i = g^{ij}\alpha_j$ ($\sharp$).
- Changement de coordonnées $q\mapsto q'$ : $v'^{\,i}=\dfrac{\partial q'^i}{\partial q^j}v^j$ (contravariant), $\alpha'_i=\dfrac{\partial q^j}{\partial q'^i}\alpha_j$ (covariant).
- **Connexion de Levi-Civita** : $\Gamma^k_{ij}\doteq\tfrac12 g^{kl}(\partial_i g_{jl}+\partial_j g_{il}-\partial_l g_{ij})$, $\nabla_j v^i=\partial_jv^i+\Gamma^i_{jk}v^k$.
- **Accélération en coordonnées quelconques** : $a^i=\ddot q^i+\Gamma^i_{jk}\dot q^j\dot q^k$. Le mouvement libre est donc la **géodésique** $a^i=0$ : première loi de Newton $=$ géodésique de la métrique plate (idée généralisée en relativité générale, partie XIV).

## I.2 Bivecteurs, $\mathfrak{so}(n)$, produit extérieur

- $\Lambda^kE$ : $k$-vecteurs, $\dim\Lambda^kE=\binom nk$. Pour $a,b\in E$ :
$$
a\wedge b\doteq a\,b^{\mathsf T}-b\,a^{\mathsf T},\qquad (a\wedge b)^{ij}=a^ib^j-a^jb^i,\qquad (a\wedge b)(u)=a\,(b\cdot u)-b\,(a\cdot u).
$$
- $\mathfrak{so}(n)\doteq\{\Omega\in\mathrm{End}(E):\Omega^{\mathsf T}=-\Omega\}\;\cong\;\Lambda^2E$, $\dim=\tfrac{n(n-1)}2$, crochet $[\Omega_1,\Omega_2]=\Omega_1\Omega_2-\Omega_2\Omega_1$ ; $SO(n)=\exp\mathfrak{so}(n)$.
- **Dimension 3** (*et seulement elle, avec $n=7$ par accident octonionique*) : il existe un produit vectoriel, via la dualité de Hodge $\star\colon\Lambda^2E\to E$. Identifications :
$$
M^{ij}=\varepsilon^{ijk}M_k\ \ (\text{bivecteur-moment}),\qquad \Omega^{ij}=-\varepsilon^{ijk}\Omega_k\ \ (\text{endomorphisme}: \Omega\cdot u=\vec\Omega\times u),\qquad a\wedge b\leftrightarrow a\times b.
$$
- $n=2$ : $\Lambda^2E\cong\mathbb R$ (pseudo-scalaire $\omega$, $\Omega=\omega\begin{pmatrix}0&-1\\1&0\end{pmatrix}$). $n=4$ : $\Lambda^2=\Lambda^2_+\oplus\Lambda^2_-$ (auto-dual/anti-auto-dual), $\mathfrak{so}(4)=\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ — ce sera la clé de l'hydrogène (VIII).
- **Forme normale** (Youla) : tout $\Omega\in\mathfrak{so}(n)$ s'écrit, dans une base orthonormée adaptée, $\Omega=\sum_{k=1}^{\lfloor n/2\rfloor}\omega_k\,e_{2k-1}\wedge e_{2k}$ ; les $\omega_k$ sont les $\lfloor n/2\rfloor$ invariants. Si $n$ est impair, $\ker\Omega\neq\{0\}$.
- Produit scalaire sur $\Lambda^2$ : $\langle A,B\rangle\doteq\tfrac12A^{ij}B_{ij}$.

## I.3 Opérateurs différentiels métriques

Pour $f\colon M\to\mathbb R$, $v$ champ de vecteurs :
$$
\operatorname{grad}f\doteq(df)^\sharp=g^{ij}\partial_jf\,e_i,\qquad
\operatorname{div}v\doteq\nabla_iv^i=\frac1{\sqrt{|g|}}\partial_i\!\big(\sqrt{|g|}\,v^i\big),\qquad
\Delta f\doteq\operatorname{div}\operatorname{grad}f=\frac1{\sqrt{|g|}}\partial_i\!\big(\sqrt{|g|}\,g^{ij}\partial_jf\big).
$$
- Élément de volume $dV=\sqrt{|g|}\,dq^1\cdots dq^n$ (le facteur $\sqrt{|g|}$ est une densité de volume, pas un facteur à ajouter « à la main » aux composantes physiques).
- **Théorème de la divergence** : $\displaystyle\int_\Omega\operatorname{div}v\,dV=\int_{\partial\Omega}g(v,\nu)\,dS$.
- **Rotationnel** : $\operatorname{rot}v\doteq d(v^\flat)$, 2-forme $(\partial_iv_j-\partial_jv_i)$ en toute dimension ; identifié à un vecteur par $\star$ **seulement en 3D** : $\operatorname{rot}v=\star\,d v^\flat=\nabla\times v$.

**Coordonnées orthogonales** ($g_{ii}=h_i^2$, facteurs de Lamé) :
$$
\operatorname{grad}f=\sum_i\frac1{h_i}\partial_if\,\hat e_i,\quad
\operatorname{div}v=\frac1{\prod h}\sum_i\partial_i\!\Big(\frac{\prod h}{h_i}\hat v_i\Big),\quad
\Delta f=\frac1{\prod h}\sum_i\partial_i\!\Big(\frac{\prod h}{h_i^{2}}\partial_if\Big).
$$

| Système $\mathbb R^3$ | $(h_1,h_2,h_3)$ | $dV$ | $\Delta f$ |
|---|---|---|---|
| cartésien $(x,y,z)$ | $(1,1,1)$ | $dx\,dy\,dz$ | $\partial_x^2f+\partial_y^2f+\partial_z^2f$ |
| cylindrique $(r,\theta,z)$ | $(1,r,1)$ | $r\,dr\,d\theta\,dz$ | $\frac1r\partial_r(r\partial_rf)+\frac1{r^2}\partial_\theta^2f+\partial_z^2f$ |
| sphérique $(r,\theta,\varphi)$ | $(1,r,r\sin\theta)$ | $r^2\sin\theta\,dr\,d\theta\,d\varphi$ | $\frac1{r^2}\partial_r(r^2\partial_rf)+\frac1{r^2\sin\theta}\partial_\theta(\sin\theta\,\partial_\theta f)+\frac1{r^2\sin^2\theta}\partial_\varphi^2f$ |

**Dimension $n$ en coordonnées radiales** : $dV=r^{n-1}dr\,d\Omega_{n-1}$, $|S^{n-1}|=\dfrac{2\pi^{n/2}}{\Gamma(n/2)}$, $|B^n|=\dfrac{\pi^{n/2}}{\Gamma(n/2+1)}$, et
$$
\Delta=r^{1-n}\partial_r\big(r^{n-1}\partial_r\big)+r^{-2}\Delta_{S^{n-1}}.
$$
Solution fondamentale du laplacien : $\propto r^{2-n}$ ($n\geq3$), $\ln r$ ($n=2$) — c'est pourquoi la force de gravitation/Coulomb en $1/r^{n-1}$ est la « bonne » en dimension $n$ (VIII).

## I.4 Hypersurfaces $\Sigma\subset M$ (dimension $n-1$)

Paramétrage $q^i=X^i(u)$, $\mathbf t_a=\partial_aX^i e_i$.
$$
\gamma_{ab}\doteq g_{ij}\partial_aX^i\partial_bX^j,\qquad dS=\sqrt{|\gamma|}\,du^1\cdots du^{n-1}.
$$
- Sphère $S^2_R$ : $dS=R^2\sin\theta\,d\theta\,d\varphi$. Graphe $q^n=h(q')$ : $dS=\sqrt{1+|\nabla h|^2}\,dq'$.
- Normale si $\Sigma=\{F=0\}$ : $\nu=\operatorname{grad}F/|\operatorname{grad}F|$, $dS=\iota_\nu dV|_\Sigma$.
- Projecteur tangent $P^i{}_j=\delta^i{}_j-\nu^i\nu_j$ ; $\operatorname{grad}_\Sigma f=P\operatorname{grad}f=\gamma^{ab}\partial_af\,\mathbf t_b$ ; $\operatorname{div}_\Sigma v=\nabla_iv^i-\nu_i\nu^j\nabla_jv^i$ ; $\Delta_\Sigma f=\dfrac1{\sqrt{|\gamma|}}\partial_a\big(\sqrt{|\gamma|}\gamma^{ab}\partial_bf\big)$.
- **Courbure moyenne** $H\doteq\operatorname{div}_\Sigma\nu$ (somme des courbures principales ; sphère de rayon $R$, $\nu$ sortante : $H=2/R$) et
$$
\Delta f=\Delta_\Sigma f+H\,\partial_\nu f+\partial_\nu^2f\qquad(\text{espace euclidien}).
$$
- **Divergence sur $\Sigma$ à bord** (conormale sortante $n$) : $\displaystyle\int_\Sigma\operatorname{div}_\Sigma v\,dS=\int_{\partial\Sigma}g(v,n)\,d\ell-\int_\Sigma H\,g(v,\nu)\,dS$. Si $v$ tangent, le dernier terme disparaît ; $\Sigma$ fermée et $w$ tangent : $\int_\Sigma\operatorname{div}_\Sigma w\,dS=0$.

## I.5 Sous-variétés de codimension $k$ (dimension $m=n-k$)

$$
\gamma_{ab}=g_{ij}\partial_aX^i\partial_bX^j,\qquad dS=\sqrt{\det\gamma}\,d^mu,\qquad P_T^{ij}=\gamma^{ab}t_a^it_b^j,\qquad P_N=g^{-1}-P_T .
$$
Définition implicite $S=\{F^1=\dots=F^k=0\}$, $G^{\alpha\beta}\doteq g^{ij}\partial_iF^\alpha\partial_jF^\beta$, $J\doteq\sqrt{\det G^{\alpha\beta}}$ :
$$
\int_M\varphi\,\delta^{(k)}(F)\,J\,dV=\int_S\varphi\,dS\quad(\text{Dirac}),\qquad
\int_M\varphi\,J\,dV=\int_{\mathbb R^k}\Big(\int_{\{F=c\}}\varphi\,dS\Big)d^kc\quad(\text{co-aire}).
$$
- Seconde forme fondamentale $\mathrm{II}(X,Y)=(\nabla_XY)^\perp$, **vecteur courbure moyenne** $\vec H=\gamma^{ab}\mathrm{II}(\mathbf t_a,\mathbf t_b)$ ; pour $k=1$, $\nu$ sortante : $\vec H=-H\nu$.
- $\operatorname{div}_Sv=\operatorname{div}_S(v^T)-g(v,\vec H)$ ; $\displaystyle\int_S\operatorname{div}_Sv\,dS=\int_{\partial S}g(v,n)d\sigma-\int_Sg(v,\vec H)\,dS$ ; première variation de l'aire : $\delta\,\mathrm{Aire}(S)=-\int_Sg(v,\vec H)\,dS$.
