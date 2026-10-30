---
title: VIII - Opérateurs différentiels et métrique en coordonnées curvilignes
tags:
  - Mathématiques
  - Physique
  - Géométrie différentielle
  - Analyse vectorielle
niveau: Doctorat
---

# Opérateurs différentiels, métrique et systèmes de coordonnées

## 1. Objet et conventions

L'objectif est de reconstruire les opérateurs différentiels à partir de la géométrie, plutôt que de mémoriser séparément leurs expressions en coordonnées cartésiennes, cylindriques ou sphériques.

On considère d'abord un espace euclidien de dimension $n$, muni de coordonnées locales
$$
(q^1,\ldots,q^n)\longmapsto \boldsymbol r(q^1,\ldots,q^n).
$$
Les coordonnées $q^i$ ne sont pas nécessairement des longueurs. Les indices latins $i,j,k,\ldots$ parcourent $\{1,\ldots,n\}$, et la convention de sommation d'Einstein est adoptée : un indice répété une fois en position haute et une fois en position basse est sommé.

Dans une carte, on distingue soigneusement :

- les **coordonnées** $q^i$ ;
- la **base coordonnée covariante** $(\boldsymbol e_i)$ ;
- la **base réciproque contravariante** $(\boldsymbol e^i)$ ;
- une éventuelle **base orthonormale** $(\boldsymbol u_{\hat\imath})$, dont les indices coiffés signalent les composantes physiques dans cette base.

Dans un espace euclidien, un changement de coordonnées ne change pas la géométrie : il change les composantes et la forme des expressions. Sur une variété riemannienne, la métrique peut en revanche varier d'un point à l'autre et la courbure peut être non nulle.

## 2. Base coordonnée et métrique

### 2.1 Base tangente associée aux coordonnées

Le vecteur position est $\boldsymbol r=\boldsymbol r(q^1,\ldots,q^n)$. La base coordonnée est définie par
$$
\boldsymbol e_i := \frac{\partial \boldsymbol r}{\partial q^i}.
$$
Un déplacement infinitésimal s'écrit
$$
d\boldsymbol r = \boldsymbol e_i\,dq^i.
$$
Le carré de l'élément de longueur est alors
$$
ds^2=d\boldsymbol r\cdot d\boldsymbol r
=g_{ij}\,dq^i\,dq^j,
\qquad
g_{ij}:=\boldsymbol e_i\cdot\boldsymbol e_j.
$$
La matrice $G=(g_{ij})$ est la matrice métrique covariante. Dans une carte régulière, elle est symétrique et définie positive pour une métrique riemannienne.

### 2.2 Métrique inverse et base réciproque

On note $(g^{ij})=G^{-1}$, de sorte que
$$
g^{ik}g_{kj}=\delta^i{}_j.
$$
La base réciproque est
$$
\boldsymbol e^i:=g^{ij}\boldsymbol e_j,
\qquad
\boldsymbol e^i\cdot\boldsymbol e_j=\delta^i{}_j.
$$
Un vecteur $\boldsymbol A$ peut être développé sous les deux formes équivalentes
$$
\boldsymbol A=A^i\boldsymbol e_i=A_i\boldsymbol e^i,
$$
où les composantes sont reliées par
$$
A_i=g_{ij}A^j,\qquad A^i=g^{ij}A_j.
$$
Attention : $\boldsymbol e_i$ et $\boldsymbol e^i$ sont des vecteurs de base, tandis que $A^i$ et $A_i$ sont des composantes. Il ne faut pas confondre le caractère covariant ou contravariant des composantes avec la nature géométrique du vecteur lui-même.

### 2.3 Coordonnées orthogonales et facteurs d'échelle

La base coordonnée est orthogonale si
$$
g_{ij}=0\quad\text{pour }i\ne j.
$$
On définit alors les facteurs d'échelle
$$
h_i:=\sqrt{g_{ii}}=\|\boldsymbol e_i\|,
$$
et les vecteurs unitaires
$$
\boldsymbol u_{\hat\imath}:=\frac{\boldsymbol e_i}{h_i}.
$$
La métrique et la longueur deviennent
$$
ds^2=\sum_{i=1}^n h_i^2(dq^i)^2,
\qquad
\boldsymbol e_i=h_i\boldsymbol u_{\hat\imath}.
$$
Dans une base orthonormale, les composantes physiques $A_{\hat\imath}$ sont définies par
$$
\boldsymbol A=A_{\hat\imath}\boldsymbol u_{\hat\imath}.
$$
Dans le cas orthogonal, $A_{\hat\imath}=h_i A^i$ et $A^i=A_{\hat\imath}/h_i$. Cette égalité n'est pas une règle générale pour une base non orthogonale.

## 3. Élément de volume

On pose
$$
g:=\det(g_{ij}),\qquad \sqrt{g}:=\sqrt{\det(g_{ij})}.
$$
L'élément de volume riemannien est
$$
dV=\sqrt{g}\,dq^1\cdots dq^n.
$$
Dans un système orthogonal,
$$
\sqrt{g}=\prod_{i=1}^n h_i,
\qquad
dV=\left(\prod_{i=1}^n h_i\right)dq^1\cdots dq^n.
$$
La mesure est positive ; dans les calculs d'intégrales orientées, on distingue cette mesure de la forme volume orientée.

## 4. Gradient d'un champ scalaire

Soit $f$ un champ scalaire différentiable. Sa différentielle est la 1-forme
$$
df=(\partial_i f)\,dq^i.
$$
Le gradient est le vecteur défini par la relation métrique
$$
\langle\operatorname{grad}f,\boldsymbol X\rangle=df(\boldsymbol X)
\quad\text{pour tout vecteur }\boldsymbol X.
$$
Il en résulte
$$
\boxed{\operatorname{grad}f=g^{ij}\partial_j f\,\boldsymbol e_i
=\partial_i f\,\boldsymbol e^i.}
$$
Les composantes covariantes du gradient sont $(\operatorname{grad}f)_i=\partial_i f$, et ses composantes contravariantes sont
$$
(\operatorname{grad}f)^i=g^{ij}\partial_j f.
$$
En coordonnées orthogonales,
$$
\boxed{\operatorname{grad}f
=\sum_{i=1}^n\boldsymbol u_{\hat\imath}\frac1{h_i}\frac{\partial f}{\partial q^i}.}
$$
On écrit parfois formellement
$$
\boldsymbol\nabla=\boldsymbol u_{\hat\imath}\frac1{h_i}\partial_i
$$
dans un système orthogonal. Cette notation est un raccourci opératoire : le gradient est intrinsèquement défini par la métrique, et il faut préciser la base dans laquelle les composantes sont exprimées.

## 5. Divergence d'un champ vectoriel

La divergence est définie intrinsèquement comme la trace de la dérivée covariante :
$$
\operatorname{div}\boldsymbol A:=\nabla_i A^i.
$$
Pour la connexion de Levi-Civita,
$$
\nabla_i A^j=\partial_i A^j+\Gamma^j{}_{ik}A^k,
$$
avec
$$
\Gamma^k{}_{ij}
=\frac12g^{k\ell}
\left(\partial_i g_{\ell j}+\partial_jg_{\ell i}-\partial_\ell g_{ij}\right).
$$
La trace se simplifie en
$$
\boxed{\operatorname{div}\boldsymbol A
=\frac1{\sqrt g}\partial_i\!\left(\sqrt g\,A^i\right).}
$$
Cette formule utilise les composantes **contravariantes** $A^i$ dans la base coordonnée. Elle est valable en coordonnées générales sur une variété riemannienne.

Dans un système orthogonal, si
$$
\boldsymbol A=A_{\hat\imath}\boldsymbol u_{\hat\imath},
\qquad
H:=\prod_{i=1}^n h_i,
$$
alors $A^i=A_{\hat\imath}/h_i$ et
$$
\boxed{\operatorname{div}\boldsymbol A
=\frac1H\sum_{i=1}^n
\frac{\partial}{\partial q^i}
\left(\frac{H}{h_i}A_{\hat\imath}\right).}
$$
Les $A_{\hat\imath}$ sont ici les composantes physiques dans la base orthonormale locale.

## 6. Laplacien scalaire et opérateur de Laplace–Beltrami

Le laplacien scalaire est la divergence du gradient :
$$
\Delta f:=\operatorname{div}(\operatorname{grad}f).
$$
En coordonnées générales,
$$
\boxed{
\Delta f
=\frac1{\sqrt g}\partial_i
\left(\sqrt g\,g^{ij}\partial_j f\right).
}
$$
Il s'agit de l'opérateur de Laplace–Beltrami pour une métrique riemannienne. En coordonnées cartésiennes euclidiennes, il redonne le laplacien usuel.

Si les coordonnées sont orthogonales, $g^{ij}=0$ pour $i\ne j$, $g^{ii}=h_i^{-2}$ et $H=\prod_i h_i$. Ainsi,
$$
\boxed{
\Delta f=\frac1{\prod_i h_i}
\sum_{i=1}^n
\frac{\partial}{\partial q^i}
\left[
\frac{\prod_j h_j}{h_i^2}
\frac{\partial f}{\partial q^i}
\right].
}
$$
C'est la formule générale à retenir pour retrouver le laplacien scalaire dans un système de coordonnées orthogonales. Elle est obtenue en combinant la métrique, le gradient et la divergence ; elle n'est pas une formule indépendante à mémoriser.

## 7. Rotationnel : particularité de la dimension trois

En dimension trois, le rotationnel peut être défini à l'aide de la métrique et de l'orientation. En langage des formes différentielles,
$$
(\operatorname{rot}\boldsymbol A)^\flat
=*\,d(\boldsymbol A^\flat),
$$
où $\flat$ désigne l'identification métrique vecteur–1-forme et $*$ l'opérateur de Hodge. Cette identification produit un vecteur parce qu'en dimension trois une 2-forme peut être identifiée à un vecteur via la forme volume.

En dimension $n$ quelconque, l'objet $d(\boldsymbol A^\flat)$ est une 2-forme, pas en général un vecteur. Il est donc incorrect de supposer que le rotationnel vectoriel usuel se généralise tel quel à toute dimension. La formulation naturelle en dimension arbitraire utilise les formes différentielles et la dérivée extérieure.

## 8. Applications en dimension trois

Les expressions suivantes utilisent les composantes physiques $A_{\hat\imath}$ dans la base orthonormale locale. En coordonnées curvilignes, ces composantes ne sont pas les mêmes que les composantes contravariantes $A^i$ dans la base coordonnée.

### 8.1 Coordonnées cartésiennes $(x,y,z)$

La paramétrisation est
$$
\boldsymbol r=x\boldsymbol e_x+y\boldsymbol e_y+z\boldsymbol e_z.
$$
La métrique est
$$
ds^2=dx^2+dy^2+dz^2,\qquad
(g_{ij})=I_3,\qquad (h_x,h_y,h_z)=(1,1,1).
$$
Gradient :
$$
\operatorname{grad}f
=(\partial_xf)\boldsymbol e_x
+(\partial_yf)\boldsymbol e_y
+(\partial_zf)\boldsymbol e_z.
$$
Pour $\boldsymbol A=A_x\boldsymbol e_x+A_y\boldsymbol e_y+A_z\boldsymbol e_z$,
$$
\operatorname{div}\boldsymbol A
=\partial_xA_x+\partial_yA_y+\partial_zA_z.
$$
Rotationnel :
$$
\operatorname{rot}\boldsymbol A=
\begin{pmatrix}
\partial_yA_z-\partial_zA_y\\
\partial_zA_x-\partial_xA_z\\
\partial_xA_y-\partial_yA_x
\end{pmatrix}_{(\boldsymbol e_x,\boldsymbol e_y,\boldsymbol e_z)}.
$$
Laplacien scalaire :
$$
\Delta f=\partial_x^2f+\partial_y^2f+\partial_z^2f.
$$

### 8.2 Coordonnées cylindriques $(r,\theta,z)$

On prend $r\geq0$, $\theta$ l'angle azimutal et $z$ la coordonnée axiale :
$$
\boldsymbol r=r\cos\theta\,\boldsymbol e_x
+r\sin\theta\,\boldsymbol e_y+z\,\boldsymbol e_z.
$$
La base orthonormale locale est $(\boldsymbol e_r,\boldsymbol e_\theta,\boldsymbol e_z)$ et
$$
d\boldsymbol r=dr\,\boldsymbol e_r
+r\,d\theta\,\boldsymbol e_\theta+dz\,\boldsymbol e_z.
$$
Donc
$$
ds^2=dr^2+r^2d\theta^2+dz^2,
\quad
(g_{ij})=\operatorname{diag}(1,r^2,1),
\quad
(h_r,h_\theta,h_z)=(1,r,1).
$$
Le déterminant métrique vaut $g=r^2$ et $dV=r\,dr\,d\theta\,dz$ pour $r>0$.

Gradient :
$$
\operatorname{grad}f
=(\partial_rf)\boldsymbol e_r
+\frac1r(\partial_\theta f)\boldsymbol e_\theta
+(\partial_zf)\boldsymbol e_z.
$$
Divergence :
$$
\operatorname{div}\boldsymbol A
=\frac1r\partial_r(rA_r)
+\frac1r\partial_\theta A_\theta
+\partial_zA_z.
$$
Rotationnel :
$$
\begin{aligned}
(\operatorname{rot}\boldsymbol A)_r
&=\frac1r\partial_\theta A_z-\partial_zA_\theta,\\
(\operatorname{rot}\boldsymbol A)_\theta
&=\partial_zA_r-\partial_rA_z,\\
(\operatorname{rot}\boldsymbol A)_z
&=\frac1r\left[\partial_r(rA_\theta)-\partial_\theta A_r\right].
\end{aligned}
$$
Laplacien scalaire :
$$
\boxed{
\Delta f=\frac1r\partial_r(r\partial_rf)
+\frac1{r^2}\partial_\theta^2f+\partial_z^2f.
}
$$

### 8.3 Coordonnées sphériques $(r,\theta,\varphi)$

Convention : $r\geq0$, $\theta\in[0,\pi]$ est l'angle polaire mesuré depuis l'axe $z$, et $\varphi\in[0,2\pi)$ est l'angle azimutal dans le plan $xy$. La paramétrisation est
$$
\boldsymbol r=
r\sin\theta\cos\varphi\,\boldsymbol e_x
+r\sin\theta\sin\varphi\,\boldsymbol e_y
+r\cos\theta\,\boldsymbol e_z.
$$
La base orthonormale locale est $(\boldsymbol e_r,\boldsymbol e_\theta,\boldsymbol e_\varphi)$ et
$$
d\boldsymbol r=dr\,\boldsymbol e_r
+r\,d\theta\,\boldsymbol e_\theta
+r\sin\theta\,d\varphi\,\boldsymbol e_\varphi.
$$
Ainsi,
$$
ds^2=dr^2+r^2d\theta^2+r^2\sin^2\theta\,d\varphi^2,
$$
$$
(g_{ij})=\operatorname{diag}(1,r^2,r^2\sin^2\theta),
\qquad
(h_r,h_\theta,h_\varphi)=(1,r,r\sin\theta).
$$
Le déterminant est $g=r^4\sin^2\theta$, d'où
$$
dV=r^2\sin\theta\,dr\,d\theta\,d\varphi.
$$
Gradient :
$$
\operatorname{grad}f
=(\partial_rf)\boldsymbol e_r
+\frac1r(\partial_\theta f)\boldsymbol e_\theta
+\frac1{r\sin\theta}(\partial_\varphi f)\boldsymbol e_\varphi.
$$
Divergence :
$$
\operatorname{div}\boldsymbol A
=\frac1{r^2}\partial_r(r^2A_r)
+\frac1{r\sin\theta}\partial_\theta(\sin\theta A_\theta)
+\frac1{r\sin\theta}\partial_\varphi A_\varphi.
$$
Rotationnel :
$$
\begin{aligned}
(\operatorname{rot}\boldsymbol A)_r
&=\frac1{r\sin\theta}
\left[\partial_\theta(\sin\theta A_\varphi)-\partial_\varphi A_\theta\right],\\
(\operatorname{rot}\boldsymbol A)_\theta
&=\frac1r\left[\frac1{\sin\theta}\partial_\varphi A_r-\partial_r(rA_\varphi)\right],\\
(\operatorname{rot}\boldsymbol A)_\varphi
&=\frac1r\left[\partial_r(rA_\theta)-\partial_\theta A_r\right].
\end{aligned}
$$
Laplacien scalaire :
$$
\boxed{
\begin{aligned}
\Delta f={}&\frac1{r^2}\partial_r(r^2\partial_rf)\\
&+\frac1{r^2\sin\theta}\partial_\theta(\sin\theta\,\partial_\theta f)\\
&+\frac1{r^2\sin^2\theta}\partial_\varphi^2f.
\end{aligned}
}
$$

Les coordonnées sphériques sont singulières en $r=0$ et sur l'axe polaire où $\sin\theta=0$. Les facteurs $1/r$ et $1/\sin\theta$ dans les formules sont donc à interpréter dans une carte où les coordonnées sont régulières ; une singularité de coordonnées n'implique pas nécessairement une singularité du champ géométrique.

## 9. Exemple de calcul : retrouver le laplacien cylindrique

Dans les coordonnées $(r,\theta,z)$,
$$
(g_{ij})=\operatorname{diag}(1,r^2,1),
\quad \sqrt g=r,
\quad (g^{ij})=\operatorname{diag}(1,r^{-2},1).
$$
On part exclusivement de la formule générale :
$$
\Delta f=\frac1{\sqrt g}\partial_i
\left(\sqrt g\,g^{ij}\partial_jf\right).
$$
En séparant les trois coordonnées,
$$
\begin{aligned}
\Delta f
&=\frac1r\partial_r(r\,\partial_rf)
+\frac1r\partial_\theta\left(\frac1r\partial_\theta f\right)
+\frac1r\partial_z(r\,\partial_zf)\\
&=\frac1r\partial_r(r\,\partial_rf)
+\frac1{r^2}\partial_\theta^2f+\partial_z^2f.
\end{aligned}
$$
Le facteur $r^{-2}$ du terme angulaire vient de la métrique inverse, et le facteur $r^{-1}$ devant la dérivée radiale vient du déterminant métrique.

## 10. Procédure générale à appliquer à un nouveau système

Pour établir les opérateurs dans un système de coordonnées donné :

1. **Paramétrer la géométrie** : écrire $\boldsymbol r(q^1,\ldots,q^n)$.
2. **Calculer la base coordonnée** : $\boldsymbol e_i=\partial_i\boldsymbol r$.
3. **Construire la métrique** : $g_{ij}=\boldsymbol e_i\cdot\boldsymbol e_j$, puis calculer son inverse $g^{ij}$ et son déterminant $g$.
4. **Identifier la base utilisée** : composantes $A^i$ dans la base coordonnée ou composantes physiques $A_{\hat\imath}$ dans une base orthonormale.
5. **Calculer l'élément de volume** : $dV=\sqrt g\,d^nq$.
6. **Appliquer les formules générales** :
   $$
   \operatorname{grad}f=g^{ij}\partial_jf\,\boldsymbol e_i,\qquad
   \operatorname{div}\boldsymbol A=\frac1{\sqrt g}\partial_i(\sqrt g A^i),
   $$
   $$
   \Delta f=\frac1{\sqrt g}\partial_i(\sqrt g\,g^{ij}\partial_jf).
   $$
7. **Pour le rotationnel**, vérifier que l'on travaille en dimension trois et préciser l'orientation et la base des composantes.

## 11. Distinctions et erreurs fréquentes

- **Métrique et facteurs d'échelle.** Les facteurs $h_i$ ne sont définis comme ci-dessus que lorsque la base coordonnée est orthogonale. Pour une métrique non diagonale, il faut conserver $g_{ij}$ et $g^{ij}$.
- **Composantes physiques et composantes coordonnées.** Les formules orthogonales de divergence et de rotationnel présentées ici utilisent les composantes physiques $A_{\hat\imath}$. La formule générale de divergence utilise les composantes contravariantes $A^i$.
- **Laplacien scalaire et laplacien vectoriel.** $\Delta f$ est un scalaire. Le laplacien d'un champ vectoriel nécessite la dérivée covariante et tient compte de la variation de la base ; on ne l'obtient pas en appliquant naïvement le laplacien scalaire à chacune des composantes physiques curvilignes.
- **Dimension.** Le gradient, la divergence et le laplacien scalaire ont une définition en dimension $n$. Le rotationnel vectoriel usuel est une construction particulière à trois dimensions.
- **Coordonnées et courbure.** Des coefficients métriques variables ne signifient pas à eux seuls que l'espace est courbe : les coordonnées cylindriques et sphériques décrivent un espace euclidien plat avec une métrique non constante dans ces coordonnées.

## 12. Résumé des formules générales

Pour une métrique riemannienne $g_{ij}$, $g=\det(g_{ij})$, et un champ scalaire $f$ :
$$
\boxed{
\begin{aligned}
ds^2&=g_{ij}\,dq^i\,dq^j,\\
dV&=\sqrt g\,d^nq,\\
(\operatorname{grad}f)^i&=g^{ij}\partial_jf,\\
\operatorname{div}\boldsymbol A&=\frac1{\sqrt g}\partial_i(\sqrt g\,A^i),\\
\Delta f&=\frac1{\sqrt g}\partial_i(\sqrt g\,g^{ij}\partial_jf).
\end{aligned}
}
$$
Ces relations constituent le point de départ universel. Les formules cartésiennes, cylindriques et sphériques en découlent par le calcul de la métrique et de son déterminant.
'''
path = Path("/mnt/data/Operateurs_differentiels_et_metrique_coordonnees_curvilignes.md")
path.write_text(content, encoding="utf-8")
print(f"Fichier créé : {path} ({len(content)} caractères)")
