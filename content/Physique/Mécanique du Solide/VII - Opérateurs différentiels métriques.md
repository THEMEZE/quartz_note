---
title: VII - Opérateurs différentiels métriques
lang: fr
tags:
  - géométrie-différentielle
  - calcul-tensoriel
  - sous-variétés
format:
  html:
    toc: true
    number-sections: false
---

# 3. Opérateurs différentiels métriques

Notations : $(M,g)$ variété (pseudo-)riemannienne de dimension $n$, coordonnées $q^i$, $g_{ij}$ la métrique, $g^{ij}$ son inverse, $g=\det(g_{ij})$.

## 3.1 Gradient

Le différentiel $df=(\partial_i f)\,dq^i$ est un covecteur. Le gradient est son image par $\sharp$ :

$$
\operatorname{grad} f=(df)^\sharp=g^{ij}\,\partial_j f\;\mathbf e_i .
$$

Il satisfait $g(\operatorname{grad} f,v)=df(v)$ pour tout $v$. Cette définition est valable en toute dimension.

## 3.2 Divergence et élément de volume

L'élément de volume riemannien est

$$
dV=\sqrt{|g|}\;dq^1\cdots dq^n ,
$$

avec $|g|=g$ pour une métrique riemannienne. La divergence d'un champ vectoriel est

$$
\operatorname{div} v=\nabla_i v^i=\frac{1}{\sqrt{|g|}}\,\partial_i\!\left(\sqrt{|g|}\,v^i\right).
$$

> **Remarque.** Le facteur $\sqrt{|g|}$ est la densité de volume, et non un facteur à ajouter arbitrairement aux composantes physiques.

## 3.3 Laplacien (Laplace–Beltrami)

$$
\Delta f=\operatorname{div}\operatorname{grad} f=\frac{1}{\sqrt{|g|}}\,\partial_i\!\left(\sqrt{|g|}\,g^{ij}\,\partial_j f\right).
$$

## 3.4 Théorème de la divergence

Pour un domaine $\Omega\subset M$ de bord $\partial\Omega$, de normale unitaire sortante $\nu$ :

$$
\int_\Omega \operatorname{div} v\;dV=\int_{\partial\Omega} g(v,\nu)\;dS .
$$

Le élément de surface $dS$ est défini en 4.2.

---

# 4. Hypersurfaces (dimension $n-1$)

## 4.1 Paramétrage et métrique induite

Une hypersurface $\Sigma\subset M$ est paramétrée par $u=(u^1,\dots,u^{n-1})$ :

$$
q^i=X^i(u).
$$

Les vecteurs tangents sont $\mathbf t_a=\partial_a X^i\,\mathbf e_i$ ($a=1,\dots,n-1$). La **métrique induite** est

$$
\gamma_{ab}=g(\mathbf t_a,\mathbf t_b)=g_{ij}\,\partial_a X^i\,\partial_b X^j .
$$

## 4.2 Élément de surface

$$
dS=\sqrt{|\gamma|}\;du^1\cdots du^{n-1},\qquad \gamma=\det(\gamma_{ab}).
$$

> **Exemple.** Sphère $S^2_R\subset\mathbb R^3$, $u=(\theta,\varphi)$ :
> $\gamma=\operatorname{diag}(R^2,\,R^2\sin^2\theta)$, donc $dS=R^2\sin\theta\,d\theta\,d\varphi$.

> **Exemple.** Graphe $q^n=h(q^1,\dots,q^{n-1})$ dans $\mathbb R^n$ :
> $dS=\sqrt{1+|\nabla h|^2}\;dq^1\cdots dq^{n-1}$.

## 4.3 Normale

Si $\Sigma=\{F=0\}$ avec $dF\neq0$, la normale unitaire est

$$
\nu=\frac{\operatorname{grad}F}{|\operatorname{grad}F|},\qquad |\operatorname{grad}F|=\sqrt{g^{ij}\partial_iF\,\partial_jF}.
$$

On a alors $dS=\iota_\nu\,dV$ restreint à $\Sigma$ (la $(n-1)$-forme obtenue en contractant $dV$ avec $\nu$).

## 4.4 Gradient et divergence de surface

Projecteur tangent (cas riemannien) :

$$
P^i{}_j=\delta^i{}_j-\nu^i\nu_j .
$$

**Gradient tangentiel** :

$$
\operatorname{grad}_\Sigma f=P\,\operatorname{grad}f=\gamma^{ab}\,\partial_a f\;\mathbf t_b .
$$

**Divergence de surface** d'un champ $v$ défini sur $M$ :

$$
\operatorname{div}_\Sigma v=\nabla_i v^i-\nu_i\,\nu^j\,\nabla_j v^i .
$$

Pour un champ **tangent** $w=w^a\mathbf t_a$, c'est la formule intrinsèque :

$$
\operatorname{div}_\Sigma w=\frac{1}{\sqrt{|\gamma|}}\,\partial_a\!\left(\sqrt{|\gamma|}\,w^a\right).
$$

**Laplacien de surface** (Laplace–Beltrami sur $\Sigma$) :

$$
\Delta_\Sigma f=\operatorname{div}_\Sigma\operatorname{grad}_\Sigma f=\frac{1}{\sqrt{|\gamma|}}\,\partial_a\!\left(\sqrt{|\gamma|}\,\gamma^{ab}\,\partial_b f\right).
$$

## 4.5 Courbure moyenne

$$
H=\operatorname{div}_\Sigma\nu=\text{somme des courbures principales}.
$$

> **Exemple.** Sphère de rayon $R$, $\nu$ sortante : $H=2/R$.

Relation entre le laplacien ambiant (espace euclidien) et celui de surface :

$$
\Delta f=\Delta_\Sigma f+H\,\partial_\nu f+\partial_\nu^2 f .
$$

## 4.6 Théorème de la divergence sur $\Sigma$

Pour $v$ défini sur $\Sigma$ et $\Sigma$ à bord $\partial\Sigma$, de conormale sortante $n$ (tangente à $\Sigma$, normale à $\partial\Sigma$) :

$$
\int_\Sigma \operatorname{div}_\Sigma v\;dS=\int_{\partial\Sigma} g(v,n)\;d\ell-\int_\Sigma H\,g(v,\nu)\;dS .
$$

Si $v$ est tangent à $\Sigma$, le second terme disparaît. Si $\Sigma$ est fermée, il reste $\int_\Sigma\operatorname{div}_\Sigma w\,dS=0$ pour tout $w$ tangent.

---

# 5. Codimension $k$ (dimension $m=n-k$)

## 5.1 Métrique induite et élément de volume

Sous-variété $S\subset M$ de dimension $m=n-k$, paramétrée par $u=(u^1,\dots,u^m)$, $q^i=X^i(u)$ :

$$
\gamma_{ab}=g_{ij}\,\partial_aX^i\,\partial_bX^j,\qquad
dS=\sqrt{\det(\gamma_{ab})}\;du^1\cdots du^m .
$$

Les cas particuliers sont $k=1$ (hypersurface, section 4), $k=n-1$ (courbe, $dS=d\ell=\sqrt{g_{ij}\dot X^i\dot X^j}\,du$) et $k=n$ (points, mesure de comptage).

## 5.2 Décomposition tangent / normal

En chaque point, $T_pM=T_pS\oplus N_pS$ avec $\dim N_pS=k$. Projecteurs :

$$
P_T^{ij}=\gamma^{ab}\,t_a^{\,i}\,t_b^{\,j},\qquad P_N=g^{-1}-P_T .
$$

Si $(\nu_1,\dots,\nu_k)$ est un repère normal orthonormé : $P_N^{ij}=\sum_\alpha\nu_\alpha^i\nu_\alpha^j$.

## 5.3 Cas d'une sous-variété définie implicitement

Soit $S=\{F^1=\dots=F^k=0\}$ avec $dF^1,\dots,dF^k$ indépendants. Posons

$$
G^{\alpha\beta}=g^{ij}\,\partial_iF^\alpha\,\partial_jF^\beta,\qquad J=\sqrt{\det G^{\alpha\beta}} .
$$

**Distribution de Dirac de $S$** :

$$
\int_M \varphi\;\delta^{(k)}(F)\,J\;dV=\int_S\varphi\;dS .
$$

**Formule de la co-aire** :

$$
\int_M \varphi\,J\;dV=\int_{\mathbb R^k}\left(\int_{\{F=c\}}\varphi\;dS\right)d^kc .
$$

Pour $k=1$ : $J=|\operatorname{grad}F|$, et l'on retrouve $dV=\dfrac{dS\,dc}{|\operatorname{grad}F|}$.

## 5.4 Gradient et divergence de $S$

**Gradient tangentiel** :

$$
\operatorname{grad}_S f=P_T\operatorname{grad}f=\gamma^{ab}\,\partial_af\;\mathbf t_b .
$$

**Divergence de $S$** :

$$
\operatorname{div}_S v=P_T^{ij}\,\nabla_i v_j .
$$

**Laplacien de $S$** :

$$
\Delta_S f=\operatorname{div}_S\operatorname{grad}_S f=\frac{1}{\sqrt{\det\gamma}}\,\partial_a\!\left(\sqrt{\det\gamma}\;\gamma^{ab}\,\partial_bf\right).
$$

## 5.5 Seconde forme fondamentale et courbure moyenne

$$
\mathrm{II}(X,Y)=(\nabla_XY)^\perp,\qquad
\vec H=\gamma^{ab}\,\mathrm{II}(\mathbf t_a,\mathbf t_b)=\gamma^{ab}\,(\nabla_{\mathbf t_a}\mathbf t_b)^\perp .
$$

$\vec H$ est le **vecteur courbure moyenne** ; il est normal à $S$. Pour $k=1$ avec $\nu$ sortante : $\vec H=-H\,\nu$.

La divergence d'un champ se décompose selon :

$$
\operatorname{div}_S v=\operatorname{div}_S(v^T)-g(v,\vec H).
$$

> **Vérification.** Pour $v=\nu$ (normal) sur la sphère $S^2_R\subset\mathbb R^3$ : $\vec H=-\frac2R\nu$, donc $\operatorname{div}_S\nu=\frac2R$. ✔

## 5.6 Théorème de la divergence sur $S$

$$
\int_S\operatorname{div}_S v\;dS=\int_{\partial S}g(v,n)\;d\sigma-\int_S g(v,\vec H)\;dS ,
$$

où $n$ est la conormale sortante, tangente à $S$ et normale à $\partial S$, et $d\sigma$ l'élément de volume de dimension $m-1$ sur $\partial S$. Pour $S$ fermée et $v$ normal, on obtient la formule de la première variation de l'aire :

$$
\delta\,\mathrm{Aire}(S)=-\int_S g(v,\vec H)\;dS .
$$

---

# 6. Récapitulatif

| Objet | Variété $M$ ($n$) | Hypersurface $\Sigma$ ($n-1$) | Sous-variété $S$ ($n-k$) |
|---|---|---|---|
| Métrique | $g_{ij}$ | $\gamma_{ab}=g_{ij}\partial_aX^i\partial_bX^j$ | idem |
| Mesure | $\sqrt{\lvert g\rvert}\,d^nq$ | $\sqrt{\lvert\gamma\rvert}\,d^{n-1}u$ | $\sqrt{\det\gamma}\,d^{n-k}u$ |
| Gradient | $g^{ij}\partial_jf\,\mathbf e_i$ | $\gamma^{ab}\partial_af\,\mathbf t_b$ | idem |
| Divergence | $\frac1{\sqrt{\lvert g\rvert}}\partial_i(\sqrt{\lvert g\rvert}v^i)$ | $\frac1{\sqrt{\lvert\gamma\rvert}}\partial_a(\sqrt{\lvert\gamma\rvert}w^a)$ | idem |
| Courbure | — | $H=\operatorname{div}_\Sigma\nu$ | $\vec H=\gamma^{ab}(\nabla_{t_a}t_b)^\perp$ |
| Normale | — | $\nu=\operatorname{grad}F/\lvert\operatorname{grad}F\rvert$ | $\operatorname{span}(\operatorname{grad}F^\alpha)$ |

> **Note de compatibilité.** Ce fichier n'utilise que du Markdown standard, du LaTeX en `$…$` / `$$…$$` et des citations (`>`) : il s'affiche à l'identique dans Obsidian et dans Quarto (`quarto render operateurs_differentiels_metriques.md`). Pour des callouts natifs, remplacer les `>` par `> [!note]` (Obsidian) ou `::: {.callout-note}` (Quarto).
