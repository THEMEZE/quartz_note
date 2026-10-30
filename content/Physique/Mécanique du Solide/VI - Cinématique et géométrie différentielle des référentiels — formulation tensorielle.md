---
title: VI - Cinématique et géométrie différentielle des référentiels — formulation tensorielle
tags:
  - Physique
  - Mécanique
  - Géométrie différentielle
  - Calcul tensoriel
niveau: Doctorat
version: 1
---

# Cinématique et géométrie différentielle des référentiels

## Objet et conventions

Ce document reformule la cinématique du point et du solide dans un langage valable en dimension arbitraire, pour des coordonnées cartésiennes ou curvilignes, des bases orthonormales ou non orthonormales, et des espaces munis d'une métrique. Il distingue soigneusement les identités géométriques, indépendantes des coordonnées, de leurs expressions composantes.

On adopte la convention d'Einstein : un indice répété une fois en position haute et une fois en position basse est sommé. Les indices latins $i,j,k,\ldots$ parcourent $1,\ldots,n$. Les indices grecs peuvent être réservés à des sous-espaces ou à des coordonnées angulaires lorsque cela est précisé. Les composantes sont écrites dans une base explicitement indiquée lorsqu'une ambiguïté est possible.

Une égalité entre vecteurs est intrinsèque ; une égalité entre leurs composantes dépend du repère choisi. Les dérivées ordinaires des composantes ne sont pas, en général, les composantes de la dérivée géométrique d'un vecteur dans une base mobile.

# 1. Espace, coordonnées et métrique

## 1.1 Variété et carte locale

Soit $M$ une variété différentiable de dimension $n$. Une carte locale est une application $q=(q^1,\ldots,q^n):U\to\mathbb R^n$ définie sur un ouvert $U\subset M$. Les $q^i$ sont les coordonnées locales. Un point géométrique $P\in U$ ne dépend pas de la carte ; son tuple de coordonnées $q(P)$, lui, en dépend.

Pour la mécanique classique euclidienne, l'espace physique est un espace affine euclidien $E$ de dimension $n$, dont l'espace vectoriel directeur est $V$. Un choix d'origine $O$ identifie chaque point $P$ à un vecteur-position $\mathbf r(P)=\overrightarrow{OP}\in V$. Cette identification affine ne doit pas être confondue avec le choix des coordonnées.

Dans une carte curviligne d'un espace euclidien, l'application de position s'écrit localement $\mathbf r=\mathbf r(q^1,\ldots,q^n)$. Les vecteurs de base coordonnée sont

$$
\mathbf e_i:=\frac{\partial\mathbf r}{\partial q^i},\qquad i=1,\ldots,n.
$$

Ils sont tangents aux lignes coordonnées. Ils ne sont pas nécessairement unitaires ni orthogonaux. On suppose la carte régulière, donc $(\mathbf e_1,\ldots,\mathbf e_n)$ forme une base de l'espace tangent considéré.

## 1.2 Métrique et abaissement des indices

La métrique riemannienne (ou, en relativité, pseudo-riemannienne) est un champ de formes bilinéaires symétriques non dégénérées $g_p:T_pM\times T_pM\to\mathbb R$. En coordonnées,

$$
g_{ij}:=g(\mathbf e_i,\mathbf e_j),\qquad g=g_{ij}\,dq^i\otimes dq^j.
$$

Pour une métrique riemannienne, la matrice $(g_{ij})$ est définie positive. On note $(g^{ij})$ sa matrice inverse :

$$
g^{ik}g_{kj}=\delta^i{}_j.
$$

La métrique identifie l'espace tangent et son dual, ce qui définit les applications musicales

$$
\flat:V\to V^*,\quad v^\flat=g(v,\cdot),\qquad \sharp:V^*\to V,
$$
qui sont inverses. En composantes, si $v=v^i\mathbf e_i$ et $\alpha=\alpha_i\,dq^i$, alors

$$
v_i=g_{ij}v^j,\qquad v^i=g^{ij}v_j.
$$

Les composantes $v^i$ sont dites **contravariantes** ; les composantes $v_i$ sont dites **covariantes**. Il s'agit de deux descriptions du même vecteur après identification par la métrique, et non de deux vecteurs physiques distincts. Pour un covecteur $\alpha=\alpha_i dq^i$, les composantes naturelles sont covariantes.

Le produit scalaire et la norme sont

$$
\langle u,v\rangle=g_{ij}u^iv^j=u_iv^i=u^iv_i,\qquad \|v\|^2=g_{ij}v^iv^j.
$$

La distance infinitésimale vérifie

$$
ds^2=g_{ij}\,dq^i dq^j.
$$

La métrique n'est pas nécessairement constante en coordonnées. Un $g_{ij}(q)$ variable peut simplement résulter d'une carte curviligne dans l'espace euclidien : cela ne signifie pas que l'espace physique est courbe. La courbure est une propriété intrinsèque de la métrique, et non de la seule variation des coefficients $g_{ij}$.

## 1.3 Base duale, base réciproque et base orthonormale

La base duale $(\boldsymbol\theta^i)$ est définie par $\boldsymbol\theta^i(\mathbf e_j)=\delta^i{}_j$. Dans une carte de coordonnées, $\boldsymbol\theta^i=dq^i$. La base réciproque vectorielle est

$$
\mathbf e^i:=g^{ij}\mathbf e_j,\qquad g(\mathbf e^i,\mathbf e_j)=\delta^i{}_j.
$$

Ainsi, un vecteur peut s'écrire sous deux formes équivalentes :

$$
\mathbf v=v^i\mathbf e_i=v_i\mathbf e^i.
$$

Attention : $\mathbf e^i$ est un vecteur de la base réciproque, tandis que $dq^i$ est un covecteur de la base duale. La notation est proche mais les objets sont de nature différente.

Une base $(\mathbf u_a)$ est orthonormale si $g(\mathbf u_a,\mathbf u_b)=\delta_{ab}$. Pour une base coordonnée orthogonale, $g_{ij}=h_i^2\delta_{ij}$, où

$$
h_i=\sqrt{g_{ii}},\qquad \mathbf u_i=\frac{\mathbf e_i}{h_i},\qquad ds^2=\sum_i h_i^2(dq^i)^2.
$$

Les composantes physiques dans la base orthonormale sont $v_{(i)}=g(\mathbf v,\mathbf u_i)=h_i v^i$ (pas de somme sur $i$). Elles ne sont généralement pas égales aux composantes contravariantes $v^i$ dans la base coordonnée.

## 1.4 Transformation des coordonnées et des composantes

Soient deux cartes reliées par $q'^a=q'^a(q^1,\ldots,q^n)$. On a

$$
\frac{\partial}{\partial q'^a}=\frac{\partial q^i}{\partial q'^a}\frac{\partial}{\partial q^i},\qquad dq'^a=\frac{\partial q'^a}{\partial q^i}dq^i.
$$

Les composantes d'un vecteur et d'un covecteur se transforment respectivement selon

$$
v'^a=\frac{\partial q'^a}{\partial q^i}v^i,\qquad \alpha'_a=\frac{\partial q^i}{\partial q'^a}\alpha_i.
$$

Les coefficients métriques obéissent à

$$
g'_{ab}=\frac{\partial q^i}{\partial q'^a}\frac{\partial q^j}{\partial q'^b}g_{ij},\qquad
 g'^{ab}=\frac{\partial q'^a}{\partial q^i}\frac{\partial q'^b}{\partial q^j}g^{ij}.
$$

Le scalaire $g_{ij}v^iw^j$ est invariant. La règle de transformation est le critère pratique qui distingue une quantité tensorielle de simples composantes.

# 2. Tenseurs et dérivation

## 2.1 Tenseurs de type $(r,s)$

Un tenseur de type $(r,s)$ est un élément de $T_pM^{\otimes r}\otimes T_p^*M^{\otimes s}$. En coordonnées, ses composantes sont $T^{i_1\cdots i_r}{}_{j_1\cdots j_s}$. Les indices supérieurs se transforment comme ceux d'un vecteur et les indices inférieurs comme ceux d'un covecteur. La contraction d'un indice supérieur avec un indice inférieur est intrinsèque.

Exemples : un scalaire est de type $(0,0)$ ; un vecteur est de type $(1,0)$ ; un covecteur est de type $(0,1)$ ; une forme bilinéaire comme la métrique est de type $(0,2)$ ; un endomorphisme est de type $(1,1)$.

## 2.2 Pourquoi la dérivée ordinaire ne suffit pas

Pour un champ vectoriel $\mathbf v=v^i\mathbf e_i$, la dérivée le long d'une courbe dépend de la variation des composantes et de celle de la base :

$$
\frac{d\mathbf v}{dt}=\frac{dv^i}{dt}\mathbf e_i+v^i\frac{d\mathbf e_i}{dt}.
$$

Dans une base coordonnée mobile, le second terme n'est généralement pas nul. La dérivée covariante $\nabla$ formalise cette variation de la base tout en produisant un objet tensoriel.

Les symboles de Christoffel sont définis par

$$
\nabla_{\partial_j}\mathbf e_k=\Gamma^i{}_{jk}\mathbf e_i.
$$

Pour la connexion de Levi-Civita (unique connexion sans torsion compatible avec la métrique),

$$
\Gamma^i{}_{jk}=\frac12g^{i\ell}\left(\partial_jg_{\ell k}+\partial_kg_{\ell j}-\partial_\ell g_{jk}\right).
$$

La dérivée covariante d'un vecteur, d'un covecteur et d'un tenseur mixte s'écrit

$$
\nabla_jv^i=\partial_jv^i+\Gamma^i{}_{jk}v^k,
$$
$$
\nabla_jv_i=\partial_jv_i-\Gamma^k{}_{ji}v_k,
$$
$$
\nabla_kT^{i}{}_{j}=\partial_kT^i{}_j+\Gamma^i{}_{k\ell}T^\ell{}_j-\Gamma^\ell{}_{kj}T^i{}_\ell.
$$

Chaque indice supérieur apporte un terme $+\Gamma$ et chaque indice inférieur un terme $-\Gamma$. Pour un scalaire $f$, $\nabla_i f=\partial_i f$.

## 2.3 Dérivée le long d'une courbe

Pour une courbe $q^i(t)$, la vitesse est le vecteur tangent

$$
\mathbf v=\dot q^i\mathbf e_i.
$$

L'accélération covariante est

$$
\mathbf a=\frac{D\mathbf v}{Dt}=\left(\ddot q^i+\Gamma^i{}_{jk}\dot q^j\dot q^k\right)\mathbf e_i.
$$

Le terme en Christoffel est précisément la contribution liée à la variation de la base. Dans des coordonnées cartésiennes euclidiennes, $g_{ij}=\delta_{ij}$ et $\Gamma^i{}_{jk}=0$ ; en coordonnées polaires ou sphériques, les coefficients de Christoffel ne sont généralement pas nuls.

L'équation géodésique (courbe dont l'accélération covariante s'annule) est

$$
\ddot q^i+\Gamma^i{}_{jk}\dot q^j\dot q^k=0.
$$

Elle exprime une loi géométrique, pas nécessairement une force physique.

## 2.4 Connexion et dérivée dans une base mobile générale

Pour une base mobile quelconque $\mathbf b_a(t)$, orthonormale ou non, on peut écrire

$$
\frac{d\mathbf b_a}{dt}=C^b{}_a(t)\mathbf b_b.
$$

Alors $\mathbf v=v^a\mathbf b_a$ implique

$$
\frac{d\mathbf v}{dt}=\left(\dot v^b+C^b{}_a v^a\right)\mathbf b_b.
$$

Si la base est orthonormale et que la métrique est indépendante du temps dans le référentiel considéré, les coefficients de rotation sont antisymétriques en indices orthonormaux : $C_{ab}=-C_{ba}$. En dimension trois, cette matrice antisymétrique peut être représentée par un vecteur $\boldsymbol\Omega$ et le produit vectoriel. En dimension $n$ générale, l'objet naturel est une matrice antisymétrique (ou une 2-forme), pas un vecteur rotation unique.

# 3. Opérateurs différentiels métriques

## 3.1 Gradient

Le différentiel $df=(\partial_i f)dq^i$ est un covecteur. Le gradient est son image par $\sharp$ :

$$
\operatorname{grad}f=(df)^\sharp=g^{ij}\partial_jf\,\mathbf e_i.
$$

Il satisfait $g(\operatorname{grad}f,\mathbf v)=df(\mathbf v)$ pour tout $\mathbf v$. Cette définition est valable en toute dimension.

## 3.2 Divergence et élément de volume

Posons $g=\det(g_{ij})$. L'élément de volume riemannien est

$$
dV=\sqrt{|g|}\,dq^1\cdots dq^n,
$$
avec $|g|=g$ pour une métrique riemannienne. La divergence d'un champ vectoriel est

$$
\operatorname{div}\mathbf v=\nabla_i v^i=\frac{1}{\sqrt{|g|}}\partial_i\left(\sqrt{|g|}\,v^i\right).
$$

Cette formule est particulièrement utile dans les coordonnées curvilignes. Le facteur $\sqrt{|g|}$ est la densité de volume, et non un facteur à ajouter arbitrairement aux composantes physiques.

## 3.3 Laplacien de Laplace–Beltrami

Pour un scalaire $f$, le Laplacien métrique est la divergence du gradient :

$$
\Delta_g f:=\operatorname{div}(\operatorname{grad}f)
=\frac{1}{\sqrt{|g|}}\partial_i\left(\sqrt{|g|}\,g^{ij}\partial_jf\right).
$$

Dans l'espace euclidien, cet opérateur est le Laplacien usuel exprimé dans la carte choisie. Sur une variété courbe, c'est le Laplace–Beltrami.

## 3.4 Rotationnel : particularité de la dimension trois

Le rotationnel vectoriel classique est une opération propre à un espace euclidien orienté de dimension trois : il utilise l'identification entre vecteurs et 2-formes fournie par la métrique et la forme volume (opérateur de Hodge $\star$). En dimension $n$ arbitraire, l'objet général est la dérivée extérieure $d$ des formes différentielles, et non un vecteur $\operatorname{rot}\mathbf v$.

En dimension trois, on peut écrire $ (\operatorname{curl}\mathbf v)^\flat=\star d(\mathbf v^\flat)$, à convention d'orientation fixée. Cette relation précise pourquoi une formule de rotationnel en coordonnées suppose une métrique et une orientation.

# 4. Coordonnées usuelles dans l'espace euclidien

## 4.1 Cartésiennes

Dans $\mathbb R^n$, $q^i=x^i$, $\mathbf e_i$ est une base orthonormale constante et

$$
g_{ij}=\delta_{ij},\quad g^{ij}=\delta^{ij},\quad \Gamma^i{}_{jk}=0,\quad dV=dx^1\cdots dx^n.
$$

Donc $\operatorname{grad}f=(\partial_i f)\mathbf e_i$, $\operatorname{div}\mathbf v=\partial_i v^i$ et $\Delta f=\sum_i\partial_i^2f$.

## 4.2 Polaires dans le plan

Avec $x=r\cos\theta$, $y=r\sin\theta$, la base coordonnée est

$$
\mathbf e_r=\partial_r\mathbf r=\mathbf u_r,\qquad \mathbf e_\theta=\partial_\theta\mathbf r=r\mathbf u_\theta.
$$

Ainsi $g_{ij}=\operatorname{diag}(1,r^2)$, $g^{ij}=\operatorname{diag}(1,r^{-2})$, $\sqrt g=r$ et $dA=r\,dr\,d\theta$. Pour $\mathbf v=v^r\mathbf e_r+v^\theta\mathbf e_\theta$, les composantes physiques dans la base orthonormale sont $v_{(r)}=v^r$ et $v_{(\theta)}=rv^\theta$.

$$
\operatorname{grad}f=\partial_r f\,\mathbf u_r+\frac1r\partial_\theta f\,\mathbf u_\theta,
$$
$$
\operatorname{div}\mathbf v=\frac1r\partial_r(rv^r)+\partial_\theta v^\theta
=\frac1r\partial_r(rv_{(r)})+\frac1r\partial_\theta v_{(\theta)},
$$
$$
\Delta f=\frac1r\partial_r(r\partial_r f)+\frac1{r^2}\partial_\theta^2 f.
$$

## 4.3 Cylindriques dans l'espace tridimensionnel

Pour $(r,\theta,z)$, $ds^2=dr^2+r^2d\theta^2+dz^2$, donc $g=\operatorname{diag}(1,r^2,1)$ et $dV=r\,dr\,d\theta\,dz$. Les formules métriques donnent

$$
\operatorname{grad}f=\partial_r f\,\mathbf u_r+\frac1r\partial_\theta f\,\mathbf u_\theta+\partial_z f\,\mathbf u_z,
$$
$$
\operatorname{div}\mathbf v=\frac1r\partial_r(rv^r)+\partial_\theta v^\theta+\partial_zv^z,
$$
$$
\Delta f=\frac1r\partial_r(r\partial_r f)+\frac1{r^2}\partial_\theta^2f+\partial_z^2f.
$$

## 4.4 Sphériques en trois dimensions

On choisit ici la convention physique : $(r,\theta,\varphi)$, où $\theta$ est l'angle polaire depuis l'axe $z$ et $\varphi$ l'azimut. Alors

$$
ds^2=dr^2+r^2d\theta^2+r^2\sin^2\theta\,d\varphi^2,
$$
$$
g_{ij}=\operatorname{diag}(1,r^2,r^2\sin^2\theta),\quad \sqrt g=r^2\sin\theta,\quad dV=r^2\sin\theta\,dr\,d\theta\,d\varphi.
$$

Les vecteurs unitaires sont $\mathbf u_r=\mathbf e_r$, $\mathbf u_\theta=\mathbf e_\theta/r$, $\mathbf u_\varphi=\mathbf e_\varphi/(r\sin\theta)$. Il en résulte

$$
\operatorname{grad}f=\partial_r f\,\mathbf u_r+\frac1r\partial_\theta f\,\mathbf u_\theta+\frac1{r\sin\theta}\partial_\varphi f\,\mathbf u_\varphi,
$$
$$
\operatorname{div}\mathbf v=\frac1{r^2}\partial_r(r^2v^r)+\frac1{\sin\theta}\partial_\theta(\sin\theta\,v^\theta)+\partial_\varphi v^\varphi,
$$
$$
\Delta f=\frac1{r^2}\partial_r(r^2\partial_r f)+\frac1{r^2\sin\theta}\partial_\theta(\sin\theta\,\partial_\theta f)+\frac1{r^2\sin^2\theta}\partial_\varphi^2f.
$$

Dans la formule de divergence, $v^i$ désigne les composantes contravariantes dans la base coordonnée. Si l'on emploie les composantes physiques $v_{(r)},v_{(\theta)},v_{(\varphi)}$ dans la base orthonormale, alors

$$
\operatorname{div}\mathbf v=\frac1{r^2}\partial_r(r^2v_{(r)})+\frac1{r\sin\theta}\partial_\theta(\sin\theta\,v_{(\theta)})+\frac1{r\sin\theta}\partial_\varphi v_{(\varphi)}.
$$

Les coordonnées sphériques sont singulières en $r=0$ et sur l'axe polaire ; la singularité de ces expressions n'implique pas à elle seule une singularité géométrique.

# 5. Cinématique du point et changement de référentiel

## 5.1 Position et dérivation temporelle

Dans un espace affine euclidien, $\mathbf r(t)=\overrightarrow{OM(t)}$ dépend du choix de l'origine $O$ mais sa dérivée temporelle, dans un référentiel donné, définit la vitesse. Pour un référentiel fixe $\mathscr R$ et une base cartésienne constante,

$$
\mathbf v_{M/\mathscr R}=\left.\frac{d\mathbf r}{dt}\right|_{\mathscr R}=\dot x^i\mathbf e_i,\qquad
\mathbf a_{M/\mathscr R}=\left.\frac{d^2\mathbf r}{dt^2}\right|_{\mathscr R}=\ddot x^i\mathbf e_i.
$$

En coordonnées curvilignes $q^i(t)$, les composantes de la vitesse sont $v^i=\dot q^i$, tandis que l'accélération physique possède les composantes

$$
a^i=\ddot q^i+\Gamma^i{}_{jk}\dot q^j\dot q^k.
$$

Dans un espace euclidien décrit par des coordonnées curvilignes, cette expression équivaut à la dérivée vectorielle usuelle de $\mathbf r(t)$ ; elle ne signifie pas que l'accélération newtonienne est définie différemment.

## 5.2 Référentiels et théorème de transport

Soient $\mathscr R$ et $\mathscr R'$ deux référentiels classiques, avec même temps $t$. Pour un vecteur géométrique $\mathbf A(t)$, la dérivée observée dans un référentiel tournant vérifie, en dimension trois,

$$
\left.\frac{d\mathbf A}{dt}\right|_{\mathscr R}=\left.\frac{d\mathbf A}{dt}\right|_{\mathscr R'}+\boldsymbol\Omega_{\mathscr R'/\mathscr R}\times\mathbf A.
$$

Cette formule suppose une base orthonormale directe et une rotation rigide entre les référentiels. Elle ne se généralise pas à un espace vectoriel de dimension arbitraire par un vecteur $\boldsymbol\Omega$ unique : on utilise alors le générateur antisymétrique $\boldsymbol\Omega^a{}_b$ de la rotation,

$$
\left.\frac{d A^a}{dt}\right|_{\mathscr R}=\left.\frac{d A^a}{dt}\right|_{\mathscr R'}+\Omega^a{}_b A^b,
$$
avec $\Omega_{ab}=-\Omega_{ba}$ dans une base orthonormale.

## 5.3 Composition des vitesses et accélérations

Pour deux référentiels classiques dont l'origine mobile est $O'$, la relation de position est $\overrightarrow{OM}=\overrightarrow{OO'}+\overrightarrow{O'M}$. En dimension trois, pour un solide ou une base rigidement liée à $\mathscr R'$, le théorème de transport donne

$$
\mathbf v_{M/\mathscr R}=\mathbf v_{O'/\mathscr R}+\mathbf v_{M/\mathscr R'}+\boldsymbol\Omega\times\overrightarrow{O'M}.
$$

L'accélération s'écrit

$$
\mathbf a_{M/\mathscr R}=\mathbf a_{O'/\mathscr R}+\mathbf a_{M/\mathscr R'}+2\boldsymbol\Omega\times\mathbf v_{M/\mathscr R'}+\dot{\boldsymbol\Omega}\times\overrightarrow{O'M}+\boldsymbol\Omega\times(\boldsymbol\Omega\times\overrightarrow{O'M}).
$$

Les termes supplémentaires sont respectivement l'accélération de Coriolis, l'accélération d'Euler et l'accélération centrifuge (avec le signe de la formule de composition indiqué). En dimension $n$, on remplace les produits vectoriels par l'action du générateur antisymétrique de rotation sur les vecteurs.

# 6. Cinématique d'un solide rigide

## 6.1 Condition de rigidité

Un mouvement rigide préserve la distance entre tout couple de points matériels :

$$
\|\mathbf r_B(t)-\mathbf r_A(t)\|^2=\text{constante}.
$$

En dérivant,

$$
(\mathbf v_B-\mathbf v_A)\cdot\overrightarrow{AB}=0.
$$

En dimension trois, il existe un vecteur rotation instantanée $\boldsymbol\Omega$ tel que

$$
\mathbf v_B=\mathbf v_A+\boldsymbol\Omega\times\overrightarrow{AB}.
$$

La relation de Varignon cinématique s'écrit donc $\mathbf v_B=\mathbf v_A+\overrightarrow{AB}\times\boldsymbol\Omega$ si l'ordre des facteurs est inversé avec le signe correspondant ; les conventions doivent être gardées constantes. Avec la convention usuelle $\mathbf v_B=\mathbf v_A+\boldsymbol\Omega\times\overrightarrow{AB}$, la formule est directement cohérente avec $\mathbf v=\boldsymbol\Omega\times\mathbf r$ pour une rotation autour de l'origine.

En dimension $n$, la formulation intrinsèque est

$$
\mathbf v_B-\mathbf v_A=\mathsf W\,\overrightarrow{AB},\qquad \mathsf W^T g+g\mathsf W=0,
$$
soit un endomorphisme antisymétrique pour la métrique. En base orthonormale, $W_{ab}=-W_{ba}$. En dimension trois seulement, l'isomorphisme entre les 2-formes et les vecteurs axiaux permet de représenter $\mathsf W$ par $\boldsymbol\Omega$.

## 6.2 Torseur cinématique en dimension trois

Le champ de vitesse d'un solide rigide est déterminé par $\boldsymbol\Omega$ et la vitesse d'un point $A$ :

$$
\mathscr V_{S/\mathscr R}(A)=\left\{\begin{array}{c}\boldsymbol\Omega_{S/\mathscr R}\\\mathbf v_{A,S/\mathscr R}\end{array}\right\}.
$$

Pour tout point $B$ du solide,

$$
\mathbf v_B=\mathbf v_A+\boldsymbol\Omega\times\overrightarrow{AB}.
$$

Cette notation de torseur est intrinsèquement tridimensionnelle dans sa forme vectorielle habituelle. En dimension arbitraire, conserver la paire $(\mathsf W,\mathbf v_A)$, avec $\mathsf W$ antisymétrique pour $g$, constitue la généralisation correcte.

## 6.3 Dérivées de bases et angles

Pour une base orthonormale mobile $(\mathbf u_a(t))$, on peut écrire $\dot{\mathbf u}_a=\Omega^b{}_a\mathbf u_b$, avec $\Omega_{ab}=-\Omega_{ba}$. En trois dimensions, cette relation équivaut à $\dot{\mathbf u}_a=\boldsymbol\Omega\times\mathbf u_a$. Les angles d'Euler constituent un paramétrage possible de $SO(3)$, mais ils sont locaux, non uniques et singuliers pour certaines configurations ; ils ne remplacent pas la description tensorielle.

# 7. Contrôles et erreurs fréquentes

1. **Ne pas confondre** $v^i$ et $v_i$ : $v_i=g_{ij}v^j$.
2. **Ne pas confondre** la base coordonnée $\mathbf e_i$ avec la base unitaire $\mathbf u_i$.
3. **Ne pas dériver uniquement les composantes** lorsque la base dépend de la position ou du temps.
4. **Ne pas conclure à une courbure physique** parce que $g_{ij}(q)$ dépend des coordonnées.
5. Le produit vectoriel de deux vecteurs n'est pas une opération canonique en dimension $n$ quelconque ; employer des tenseurs antisymétriques ou des formes différentielles.
6. Les formules polaires et sphériques ont des domaines de validité locaux ; leurs singularités de coordonnées ne sont pas nécessairement des singularités de l'espace.
7. Les composantes de la divergence dans la formule $\nabla_i v^i$ sont les composantes contravariantes de la base coordonnée, et non automatiquement les composantes physiques de la base orthonormale.

# 8. Synthèse des formules générales

$$
\boxed{ds^2=g_{ij}\,dq^i dq^j},\qquad \boxed{v_i=g_{ij}v^j},\qquad \boxed{\Gamma^i{}_{jk}=\frac12g^{i\ell}(\partial_jg_{\ell k}+\partial_kg_{\ell j}-\partial_\ell g_{jk})}
$$
$$
\boxed{a^i=\ddot q^i+\Gamma^i{}_{jk}\dot q^j\dot q^k},\qquad \boxed{\operatorname{grad}f=g^{ij}\partial_jf\,\mathbf e_i}
$$
$$
\boxed{\operatorname{div}\mathbf v=\frac1{\sqrt{|g|}}\partial_i(\sqrt{|g|}v^i)},\qquad \boxed{\Delta_gf=\frac1{\sqrt{|g|}}\partial_i(\sqrt{|g|}g^{ij}\partial_jf)}.
$$

