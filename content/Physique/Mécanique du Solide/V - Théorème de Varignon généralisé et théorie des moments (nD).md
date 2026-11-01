---
title: V - Théorème de Varignon généralisé et théorie des moments (nD)
tags:
  - Physique
  - Mécanique
  - Calcul tensoriel
  - Algèbre extérieure
niveau: Doctorat
version: 1
---

# Théorème de Varignon généralisé et théorie des moments

> [!abstract]
> Ce document construit une théorie des moments valable en dimension arbitraire. Le produit vectoriel tridimensionnel est remplacé par le produit extérieur : le moment est un bivecteur de \(\Lambda^2(V)\). Le théorème de Varignon découle de la relation de Chasles et de la bilinéarité du produit extérieur. Une généralisation à toute application bilinéaire est ensuite établie.

## Objet, domaine et conventions

On travaille dans un espace affine réel \(\mathcal E\), de dimension \(n\), d'espace vectoriel directeur \(V\). Les points sont \(A,B,M,\ldots\), les vecteurs appartiennent à \(V\), et
\[
\overrightarrow{AM}=\overrightarrow{AB}+\overrightarrow{BM}.
\]
L'espace \(V\) peut être muni d'un produit scalaire \(g\), mais la définition et la preuve du théorème de Varignon n'en nécessitent pas.

### Produit extérieur

Le produit extérieur est l'application bilinéaire antisymétrique
\[
\wedge:V\times V\longrightarrow\Lambda^2(V),
\]
telle que
\[
\mathbf a\wedge\mathbf b=-\mathbf b\wedge\mathbf a,
\qquad \mathbf a\wedge\mathbf a=0.
\]
La dimension de l'espace des bivecteurs est
\[
\dim\Lambda^2(V)=\binom n2=\frac{n(n-1)}2.
\]

- En dimension 1, \(\Lambda^2(V)=\{0\}\).
- En dimension 2, \(\Lambda^2(V)\) est de dimension 1 ; après choix d'une orientation, il peut être représenté par un scalaire.
- En dimension 3, le bivecteur peut être identifié à un vecteur axial grâce à la métrique et à l'orientation.
- En dimension supérieure, le moment n'est généralement pas représentable par un vecteur ordinaire.

> [!warning]
> Le produit vectoriel est une opération particulière à la dimension trois (et à quelques structures exceptionnelles). Pour une théorie valable en dimension arbitraire, l'objet naturel est le bivecteur.

### Convention de transport (BABAR)

On adopte partout la convention
\[
\boxed{\mathcal M_B=\mathcal M_A+
\overrightarrow{BA}\wedge\mathbf R.}
\]
Elle est équivalente à
\[
\mathcal M_B=\mathcal M_A-
\overrightarrow{AB}\wedge\mathbf R.
\]
Le signe se vérifie en repartant de \(\overrightarrow{BM}=\overrightarrow{BA}+\overrightarrow{AM}\).

# 1. Définition du moment

## 1.1 Moment d'un vecteur appliqué

Soit un vecteur \(\mathbf u\in V\) appliqué en un point \(M\in\mathcal E\). Son moment au point \(A\) est défini par
\[
\boxed{\mathcal M_A(M,\mathbf u)
=\overrightarrow{AM}\wedge\mathbf u.}
\]
Cette définition est affine et ne requiert aucune dimension particulière.

Le moment s'annule lorsque \(\overrightarrow{AM}\) et \(\mathbf u\) sont linéairement dépendants. Il encode le plan orienté engendré par ces deux vecteurs.

## 1.2 Expression en composantes

Dans une base \((\mathbf e_i)\), écrivons
\[
\overrightarrow{AM}=r^i\mathbf e_i,\qquad
\mathbf u=u^i\mathbf e_i.
\]
Alors
\[
\mathcal M_A=r^iu^j\,\mathbf e_i\wedge\mathbf e_j,
\]
et les composantes antisymétriques sont
\[
\boxed{\mathcal M_A^{ij}=r^iu^j-r^ju^i
=2r^{[i}u^{j]}.}
\]
Ainsi \(\mathcal M_A^{ij}=-\mathcal M_A^{ji}\), avec \(n(n-1)/2\) composantes indépendantes.

# 2. Système discret de vecteurs

Considérons un système fini \((M_k,\mathbf u_k)_{1\leq k\leq N}\).

## 2.1 Résultante

La résultante est
\[
\boxed{\mathbf R=\sum_{k=1}^N\mathbf u_k.}
\]
Elle ne dépend pas du point de réduction.

## 2.2 Moment résultant

Le moment du système au point \(A\) est
\[
\boxed{\mathcal M_A
=\sum_{k=1}^N\overrightarrow{AM_k}\wedge\mathbf u_k.}
\]
En composantes,
\[
\mathcal M_A^{ij}
=\sum_k(r_k^iu_k^j-r_k^ju_k^i),
\qquad R^i=\sum_ku_k^i.
\]
La réunion de deux systèmes correspond à l'addition de leurs résultantes et de leurs moments, à condition de réduire les deux moments au même point.

# 3. Théorème de Varignon généralisé

## 3.1 Énoncé

Pour tout système fini de vecteurs et pour tous points \(A,B\in\mathcal E\),
\[
\boxed{\mathcal M_B=\mathcal M_A+
\overrightarrow{BA}\wedge\mathbf R.}
\]

## 3.2 Démonstration

Par définition,
\[
\mathcal M_B=\sum_k\overrightarrow{BM_k}\wedge\mathbf u_k.
\]
La relation de Chasles donne
\[
\overrightarrow{BM_k}=\overrightarrow{BA}+\overrightarrow{AM_k}.
\]
Par bilinéarité,
\[
\begin{aligned}
\mathcal M_B
&=\sum_k(\overrightarrow{BA}+\overrightarrow{AM_k})
                  \wedge\mathbf u_k\\
&=\sum_k\overrightarrow{BA}\wedge\mathbf u_k
  +\sum_k\overrightarrow{AM_k}\wedge\mathbf u_k\\
&=\overrightarrow{BA}\wedge\sum_k\mathbf u_k+\mathcal M_A\\
&=\boxed{\mathcal M_A+\overrightarrow{BA}\wedge\mathbf R.}
\end{aligned}
\]
La démonstration est achevée.

> [!abstract] Portée de la preuve
> Seules interviennent la relation de Chasles et la bilinéarité du produit extérieur. Ni la dimension trois, ni une métrique, ni une hypothèse dynamique ne sont nécessaires.

## 3.3 Démonstration en composantes

Posons \(b^i=(\overrightarrow{BA})^i\) et
\((\overrightarrow{BM_k})^i=b^i+r_k^i\). Alors
\[
\begin{aligned}
\mathcal M_B^{ij}
&=\sum_k[(b^i+r_k^i)u_k^j-(b^j+r_k^j)u_k^i]\\
&=b^iR^j-b^jR^i+\mathcal M_A^{ij}.
\end{aligned}
\]
Donc
\[
\boxed{\mathcal M_B^{ij}
=\mathcal M_A^{ij}+b^iR^j-b^jR^i.}
\]

## 3.4 Composition des transports

Pour trois points \(A,B,C\),
\[
\mathcal M_C=\mathcal M_B+\overrightarrow{CB}\wedge\mathbf R
=\mathcal M_A+(\overrightarrow{BA}+\overrightarrow{CB})\wedge\mathbf R.
\]
Or \(\overrightarrow{BA}+\overrightarrow{CB}=\overrightarrow{CA}\), donc
\[
\mathcal M_C=\mathcal M_A+\overrightarrow{CA}\wedge\mathbf R.
\]
Le transport est compatible avec la composition des changements de point.

# 4. Généralisation à une application bilinéaire

## 4.1 Cadre abstrait

Soient \(V,U,W\) des espaces vectoriels et
\[
\beta:V\times U\longrightarrow W
\]
une application bilinéaire. Pour un système \((M_k,\mathbf u_k)\), avec \(\mathbf u_k\in U\), posons
\[
\mathbf R_U=\sum_k\mathbf u_k,\qquad
\mathcal M_A^\beta=\sum_k
\beta(\overrightarrow{AM_k},\mathbf u_k).
\]

## 4.2 Théorème de transport bilinéaire

On a
\[
\boxed{\mathcal M_B^\beta
=\mathcal M_A^\beta+\beta(\overrightarrow{BA},\mathbf R_U).}
\]

En effet,
\[
\begin{aligned}
\mathcal M_B^\beta
&=\sum_k\beta(\overrightarrow{BM_k},\mathbf u_k)\\
&=\sum_k\beta(\overrightarrow{BA}+\overrightarrow{AM_k},\mathbf u_k)\\
&=\beta(\overrightarrow{BA},\sum_k\mathbf u_k)
+\mathcal M_A^\beta.
\end{aligned}
\]

> [!warning]
> Cette généralisation est algébrique. Elle ne signifie pas que toute grandeur vectorielle possède automatiquement un moment ayant une interprétation physique. Cette interprétation doit être justifiée dans le problème considéré.

Exemples de constructions utilisant le produit extérieur :
- force : \(\overrightarrow{AM}\wedge\mathbf F\) ;
- quantité de mouvement : \(\overrightarrow{AM}\wedge\mathbf p\) ;
- vitesse : \(\overrightarrow{AM}\wedge\mathbf v\) ;
- accélération : \(\overrightarrow{AM}\wedge\mathbf a\).

# 5. Structure de torseur en dimension arbitraire

## 5.1 Couple résultante-moment

À un point de réduction \(A\), le système est décrit par
\[
\mathcal T_A=(\mathbf R,\mathcal M_A),
\]
avec \(\mathbf R\in V\) et \(\mathcal M_A\in\Lambda^2(V)\). Lorsqu'on change de point,
\[
\mathcal M_B=\mathcal M_A+\overrightarrow{BA}\wedge\mathbf R,
\]
tandis que \(\mathbf R\) reste inchangée. C'est la loi de transformation d'un torseur généralisé.

## 5.2 Addition

Pour deux systèmes réduits au même point,
\[
\mathbf R=\mathbf R_1+\mathbf R_2,\qquad
\mathcal M_A=\mathcal M_{A,1}+\mathcal M_{A,2}.
\]
La loi de transport est conservée par addition.

## 5.3 Résultante nulle

Si \(\mathbf R=0\), alors
\[
\boxed{\mathcal M_B=\mathcal M_A\quad\text{pour tous }A,B.}
\]
Le moment est indépendant du point de réduction. Il peut néanmoins être non nul : un système peut avoir une résultante nulle et un moment non nul.

## 5.4 Existence d'un point où le moment s'annule

On cherche \(B\) tel que
\[
0=\mathcal M_A+\overrightarrow{BA}\wedge\mathbf R.
\]
Pour \(\mathbf R\neq0\), considérons
\[
\varphi_{\mathbf R}:V\to\Lambda^2(V),\qquad
\mathbf x\mapsto\mathbf x\wedge\mathbf R.
\]
Son noyau est
\[
\ker\varphi_{\mathbf R}=\operatorname{Vect}(\mathbf R),
\]
donc son rang vaut \(n-1\). L'équation admet une solution si et seulement si
\(-\mathcal M_A\) appartient à l'image de \(\varphi_{\mathbf R}\). Si une solution existe, toutes les solutions diffèrent d'un multiple de \(\mathbf R\) : le lieu des points de réduction où le moment est nul est une droite affine parallèle à la résultante.

> [!warning]
> Les propriétés usuelles des torseurs tridimensionnels exprimées avec un produit scalaire entre résultante et moment axial doivent être reformulées en dimension arbitraire. Le moment est alors un bivecteur.

# 6. Applications mécaniques

## 6.1 Système de forces

Pour des forces \(\mathbf F_k\) appliquées en \(M_k\),
\[
\mathbf R_F=\sum_k\mathbf F_k,\qquad
\mathcal M_A^F=\sum_k\overrightarrow{AM_k}\wedge\mathbf F_k.
\]
Le transport s'écrit
\[
\boxed{\mathcal M_B^F=\mathcal M_A^F+
\overrightarrow{BA}\wedge\mathbf R_F.}
\]

## 6.2 Quantité de mouvement et moment cinétique

Pour un point matériel de masse \(m\),
\[
\mathbf p=m\mathbf v,\qquad
\mathcal L_A=\overrightarrow{AM}\wedge\mathbf p.
\]
Pour un système,
\[
\mathbf P=\sum_k\mathbf p_k,\qquad
\mathcal L_A=\sum_k\overrightarrow{AM_k}\wedge\mathbf p_k,
\]
et
\[
\boxed{\mathcal L_B=\mathcal L_A+
\overrightarrow{BA}\wedge\mathbf P.}
\]

## 6.3 Moments cinématiques

On peut également définir
\[
\mathcal V_A=\sum_k\overrightarrow{AM_k}\wedge\mathbf v_k,
\qquad
\mathcal A_A=\sum_k\overrightarrow{AM_k}\wedge\mathbf a_k.
\]
Ils vérifient
\[
\mathcal V_B=\mathcal V_A+\overrightarrow{BA}\wedge\sum_k\mathbf v_k,
\]
\[
\mathcal A_B=\mathcal A_A+\overrightarrow{BA}\wedge\sum_k\mathbf a_k.
\]
Ce sont des constructions algébriques ; leur intérêt physique dépend du contexte.

## 6.4 Résultante et moment dynamiques

Pour des masses \(m_k\),
\[
\mathbf R_d=\sum_km_k\mathbf a_k,\qquad
\mathcal D_A=\sum_k\overrightarrow{AM_k}\wedge m_k\mathbf a_k.
\]
Alors
\[
\boxed{\mathcal D_B=\mathcal D_A+
\overrightarrow{BA}\wedge\mathbf R_d.}
\]
Dans un référentiel galiléen, le principe fondamental de la dynamique permet de relier les termes \(m_k\mathbf a_k\) aux résultantes des forces appliquées.

## 6.5 Impulsion

Pour une force \(\mathbf F(t)\), l'impulsion entre \(t_0\) et \(t_1\) est
\[
\mathbf J=\int_{t_0}^{t_1}\mathbf F(t)\,\mathrm dt.
\]
Si le point d'application \(M\) est fixe,
\[
\mathcal J_A=\overrightarrow{AM}\wedge\mathbf J.
\]
Pour un point d'application mobile, il faut écrire
\[
\mathcal J_A=\int_{t_0}^{t_1}
\overrightarrow{AM(t)}\wedge\mathbf F(t)\,\mathrm dt.
\]

# 7. Systèmes continus

Soit un domaine \(\Omega\), muni d'une mesure \(d\mu\), sur lequel est défini un champ vectoriel \(\mathbf u(M)\). On pose
\[
\mathbf R=\int_\Omega\mathbf u(M)\,\mathrm d\mu(M),
\]
\[
\mathcal M_A=\int_\Omega
\overrightarrow{AM}\wedge\mathbf u(M)\,\mathrm d\mu(M).
\]
Avec Chasles,
\[
\begin{aligned}
\mathcal M_B
&=\int_\Omega(\overrightarrow{BA}+\overrightarrow{AM})
                 \wedge\mathbf u(M)\,\mathrm d\mu(M)\\
&=\overrightarrow{BA}\wedge\int_\Omega\mathbf u(M)\,\mathrm d\mu(M)
+\int_\Omega\overrightarrow{AM}\wedge\mathbf u(M)\,\mathrm d\mu(M).
\end{aligned}
\]
Donc
\[
\boxed{\mathcal M_B=\mathcal M_A+
\overrightarrow{BA}\wedge\mathbf R.}
\]
La preuve est la même que dans le cas discret, la somme étant remplacée par une intégrale.

# 8. Formulation tensorielle et cas tridimensionnel

## 8.1 Tenseur antisymétrique

Les composantes du moment sont
\[
\mathcal M_A^{ij}=r^iu^j-r^ju^i.
\]
Avec une métrique \(g\), on peut abaisser les indices :
\[
\mathcal M_{A,ij}=g_{ik}g_{j\ell}\mathcal M_A^{k\ell}.
\]
La loi de transport en composantes est
\[
\boxed{\mathcal M_B^{ij}
=\mathcal M_A^{ij}+b^iR^j-b^jR^i,}
\qquad b^i=(\overrightarrow{BA})^i.
\]

## 8.2 Identification en dimension trois

Dans un espace euclidien orienté de dimension trois, l'opérateur de Hodge donne
\[
\star:\Lambda^2(V)\longrightarrow\Lambda^1(V).
\]
Après identification des formes et des vecteurs par la métrique,
\[
\star(\mathbf a\wedge\mathbf b)=\mathbf a\times\mathbf b
\]
avec les conventions usuelles. La loi de transport devient
\[
\mathbf M_B=\mathbf M_A+\overrightarrow{BA}\times\mathbf R.
\]

En dimension arbitraire, \(\dim\Lambda^2(V)=n(n-1)/2\), qui n'est généralement pas égale à \(n\). Le bivecteur est donc l'objet naturel, sans identification canonique à un vecteur.

# 9. Dérivation temporelle et point de réduction mobile

Pour un système de masses constantes \(m_k\), posons
\[
\mathbf p_k=m_k\mathbf v_k,\quad
\mathbf P=\sum_k\mathbf p_k,\quad
\mathcal L_A=\sum_k\overrightarrow{AM_k}\wedge\mathbf p_k.
\]
Si le point de réduction \(A(t)\) a pour vitesse \(\mathbf v_A\), alors
\[
\frac{\mathrm d}{\mathrm dt}\mathcal L_A
=\sum_k\left[
(\mathbf v_k-\mathbf v_A)\wedge\mathbf p_k
+\overrightarrow{AM_k}\wedge\dot{\mathbf p}_k
\right].
\]
Or \(\mathbf v_k\wedge\mathbf p_k=m_k\mathbf v_k\wedge\mathbf v_k=0\). En posant
\[
\mathcal D_A=\sum_k\overrightarrow{AM_k}\wedge\dot{\mathbf p}_k,
\]
on obtient
\[
\boxed{\frac{\mathrm d}{\mathrm dt}\mathcal L_A
=\mathcal D_A-\mathbf v_A\wedge\mathbf P.}
\]

- Si \(A\) est fixe dans le référentiel, \(\mathbf v_A=0\), donc \(\dot{\mathcal L}_A=\mathcal D_A\).
- Au centre de masse \(G\), \(\mathbf P=M\mathbf v_G\), donc \(\mathbf v_G\wedge\mathbf P=0\) et \(\dot{\mathcal L}_G=\mathcal D_G\).

> [!warning]
> La dérivée temporelle du moment dépend du mouvement du point de réduction. Il ne faut pas traiter \(A\) comme fixe lorsqu'il est mobile.

# 10. Exemples

## 10.1 Deux forces opposées : couple pur

Soient \(\mathbf F_1=\mathbf F\) appliquée en \(M_1\), et
\(\mathbf F_2=-\mathbf F\) appliquée en \(M_2\). La résultante est nulle :
\[
\mathbf R=\mathbf F-\mathbf F=0.
\]
Le moment vaut
\[
\begin{aligned}
\mathcal M_A
&=\overrightarrow{AM_1}\wedge\mathbf F
-\overrightarrow{AM_2}\wedge\mathbf F\\
&=(\overrightarrow{AM_1}-\overrightarrow{AM_2})\wedge\mathbf F\\
&=\overrightarrow{M_2M_1}\wedge\mathbf F.
\end{aligned}
\]
Il est indépendant de \(A\), et peut être non nul.

## 10.2 Vecteur unique

Pour un vecteur \(\mathbf F\) appliqué en \(M\),
\[
\mathbf R=\mathbf F,\qquad
\mathcal M_A=\overrightarrow{AM}\wedge\mathbf F.
\]
Le moment s'annule lorsque \(A\) appartient à la droite passant par \(M\) et de direction \(\mathbf F\).

## 10.3 Torseur nul

Si \(\mathbf R=0\) et \(\mathcal M_A=0\) en un point, alors le transport implique \(\mathcal M_B=0\) pour tout point \(B\).

# 11. Niveaux de généralité

Il convient de distinguer :
1. **Le résultat affine et extérieur :** le moment est \(\overrightarrow{AM}\wedge\mathbf u\), et Varignon est valable en toute dimension.
2. **La généralisation bilinéaire :** toute application bilinéaire \(\beta:V\times U\to W\) fournit une loi de transport analogue.
3. **L'interprétation mécanique :** elle dépend de la grandeur considérée et des hypothèses physiques du problème.

# 12. Checklist de cohérence

- [ ] Distinguer espace affine et espace vectoriel directeur.
- [ ] Écrire les vecteurs de position comme des différences de points.
- [ ] Utiliser \(\Lambda^2(V)\) pour le moment en dimension arbitraire.
- [ ] Fixer la convention de signe avant le transport.
- [ ] Employer \(\mathcal M_B=\mathcal M_A+\overrightarrow{BA}\wedge\mathbf R\).
- [ ] Vérifier que la résultante est indépendante du point.
- [ ] Justifier l'utilisation de la bilinéarité.
- [ ] Distinguer construction algébrique et interprétation physique.
- [ ] N'utiliser l'identification bivecteur-vecteur qu'en dimension trois avec métrique et orientation.
- [ ] Tenir compte de la vitesse du point de réduction lors d'une dérivation temporelle.

# 13. Formulaire général

**Moment élémentaire**
\[
\boxed{\mathcal M_A(M,\mathbf u)=\overrightarrow{AM}\wedge\mathbf u}
\]

**Résultante et moment d'un système**
\[
\boxed{\mathbf R=\sum_k\mathbf u_k,\qquad
\mathcal M_A=\sum_k\overrightarrow{AM_k}\wedge\mathbf u_k}
\]

**Théorème de Varignon**
\[
\boxed{\mathcal M_B=\mathcal M_A+\overrightarrow{BA}\wedge\mathbf R}
\]

**Forme équivalente**
\[
\boxed{\mathcal M_B=\mathcal M_A-\overrightarrow{AB}\wedge\mathbf R}
\]

**Composantes**
\[
\boxed{\mathcal M_A^{ij}=\sum_k(r_k^iu_k^j-r_k^ju_k^i)}
\]

**Généralisation bilinéaire**
\[
\boxed{\mathcal M_B^\beta=\mathcal M_A^\beta+
\beta(\overrightarrow{BA},\mathbf R_U)}
\]

**Système continu**
\[
\boxed{\mathbf R=\int_\Omega\mathbf u\,\mathrm d\mu,\qquad
\mathcal M_A=\int_\Omega\overrightarrow{AM}\wedge\mathbf u\,\mathrm d\mu}
\]

**Moment cinétique**
\[
\boxed{\mathcal L_A=\sum_k\overrightarrow{AM_k}\wedge\mathbf p_k}
\]

**Point de réduction mobile**
\[
\boxed{\frac{\mathrm d}{\mathrm dt}\mathcal L_A
=\mathcal D_A-\mathbf v_A\wedge\mathbf P}
\]

**Dimension de l'espace des moments**
\[
\boxed{\dim\Lambda^2(V)=\frac{n(n-1)}2}
\]
