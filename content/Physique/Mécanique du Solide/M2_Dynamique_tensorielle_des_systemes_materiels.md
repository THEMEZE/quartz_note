---
title: Dynamique des systèmes matériels — formulation tensorielle et métrique
tags:
  - Physique
  - Mécanique
  - Calcul tensoriel
niveau: Doctorat
version: 1.0
---

# Dynamique des systèmes matériels : formulation tensorielle

## Objet, domaine et conventions

Ce document reprend les notions de résultante, moment, torseurs, quantité de mouvement et théorèmes généraux de la dynamique en distinguant les identités physiques des expressions coordonnées. Le cadre principal est la mécanique classique newtonienne dans un espace affine euclidien tridimensionnel, avec une formulation tensorielle qui s'étend à $n$ dimensions. La généralisation en dimension arbitraire n'autorise pas à conserver sans modification le produit vectoriel usuel : les moments angulaires et les couples sont alors représentés par des tenseurs antisymétriques ou des 2-formes.

Convention d'Einstein : les indices répétés haut/bas sont sommés. Les coordonnées sont $q^i$, la métrique $g_{ij}$ et son inverse $g^{ij}$. On distingue les composantes contravariantes $v^i$ des composantes covariantes $v_i=g_{ij}v^j$. Les lois de Newton supposent ici un espace euclidien, un temps classique absolu et un référentiel galiléen, sauf mention contraire.

# 1. Cinématique et mesure de masse

## 1.1 Position, vitesse et accélération

Soit un système matériel fermé $\mathscr S$, constitué de points matériels $M$ dont les trajectoires sont $q^i(M,t)$. Dans une carte curviligne, la vitesse est

$$
\mathbf v(M,t)=\dot q^i(M,t)\,\mathbf e_i.
$$

Les composantes de l'accélération géométrique sont

$$
a^i(M,t)=\ddot q^i+\Gamma^i{}_{jk}\dot q^j\dot q^k,
$$
avec les symboles de Christoffel de la métrique euclidienne exprimée dans la carte. Cette formule est la traduction en coordonnées de la dérivée vectorielle physique ; les termes de Christoffel encodent la variation de la base.

La mesure de masse est notée $dm$. Pour un milieu continu de densité volumique $\rho$, $dm=\rho\,dV$ avec $dV=\sqrt{g}\,dq^1\cdots dq^n$ en métrique riemannienne. Pour une densité surfacique ou linéique, on utilise la mesure géométrique adaptée à la surface ou à la courbe.

## 1.2 Masse et centre de masse

La masse totale du système est

$$
m=\int_{\mathscr S}dm.
$$

Dans un espace affine euclidien, le centre de masse $G$ est défini par

$$
\overrightarrow{OG}=\frac1m\int_{\mathscr S}\overrightarrow{OM}\,dm,
$$
pour une origine $O$ fixée. De façon indépendante de l'origine, $\int_{\mathscr S}\overrightarrow{GM}\,dm=\mathbf0$. En coordonnées cartésiennes, $x_G^i=m^{-1}\int x^i dm$. En coordonnées curvilignes, il faut intégrer les coordonnées de l'immersion dans l'espace affine, et non en général faire la moyenne directe des coordonnées $q^i$.

# 2. Quantité de mouvement et résultante dynamique

## 2.1 Quantité de mouvement

La quantité de mouvement élémentaire est $d\mathbf p=\mathbf v\,dm$. La quantité de mouvement totale est

$$
\mathbf P=\int_{\mathscr S}\mathbf v\,dm.
$$

Si la masse est constante et que l'intégration porte sur les mêmes éléments matériels,

$$
\mathbf P=m\mathbf v_G.
$$

Ses composantes contravariantes sont $P^i=\int v^i dm$, tandis que $P_i=g_{ij}P^j$. La contraction avec un covecteur donne un scalaire invariant.

## 2.2 Résultante des forces

Pour une distribution de forces, la force élémentaire exercée sur l'élément de matière en $M$ est $d\mathbf F(M)$. La résultante est

$$
\mathbf F=\int_{\mathscr S}d\mathbf F(M).
$$

En composantes, $F^i=\int dF^i$ et $F_i=g_{ij}F^j$. Les forces doivent être exprimées dans une même base avant addition de leurs composantes.

## 2.3 Principe fondamental de la dynamique

Dans un référentiel galiléen, la loi de Newton locale est

$$
d\mathbf F_{\mathrm{tot}}(M)=\mathbf a(M)\,dm(M).
$$

L'intégration sur un système fermé conduit au théorème de la résultante dynamique (TRD) :

$$
\boxed{\frac{d\mathbf P}{dt}=\mathbf F^{\mathrm{ext}}}.
$$

Les forces internes se compensent dans la résultante si les interactions vérifient l'antisymétrie de Newton appropriée. Pour une masse constante,

$$
\boxed{m\mathbf a_G=\mathbf F^{\mathrm{ext}}}.
$$

En composantes dans une carte curviligne, il faut employer l'accélération covariante :

$$
\frac{dP^i}{dt}+\Gamma^i{}_{jk}\,\dot q^j P^k=F^i
$$
si la dérivée est prise le long de la trajectoire pertinente et que $P^i$ représente le vecteur transporté. Dans le cas d'un système étendu, la formule intrinsèque $D\mathbf P/Dt=\mathbf F^{\mathrm{ext}}$ doit être comprise comme la dérivée physique du vecteur dans l'espace euclidien ; une expression composante complète dépend de la manière dont les trajectoires et la base sont paramétrées.

# 3. Moments : formulation tridimensionnelle et généralisation

## 3.1 Moment d'une force en dimension trois

Dans un espace euclidien orienté de dimension trois, le moment de la force $\mathbf F$ appliquée en $M$ au point $A$ est

$$
\boldsymbol\mathfrak M_A=\overrightarrow{AM}\times\mathbf F.
$$

Pour un système de forces distribuées,

$$
\boldsymbol\mathfrak M_A=\int_{\mathscr S}\overrightarrow{AM}\times d\mathbf F(M).
$$

La résultante et le moment au point $A$ constituent le torseur des actions mécaniques :

$$
\mathscr A(A)=\left\{\begin{array}{c}\mathbf F\\\boldsymbol\mathfrak M_A\end{array}\right\}.
$$

## 3.2 Formulation tensorielle du moment en dimension arbitraire

En dimension $n$, il n'existe pas de produit vectoriel canonique $V\times V\to V$. Pour deux vecteurs $r$ et $F$, on définit le bivecteur (ou tenseur antisymétrique contravariant)

$$
\mathsf M^{ij}:=r^iF^j-r^jF^i=2r^{[i}F^{j]}.
$$

La convention $2r^{[i}F^{j]}$ signifie $r^iF^j-r^jF^i$. Pour une distribution de forces, le moment tensoriel au point $A$ est

$$
\mathsf M_A^{ij}=\int_{\mathscr S}\left(r_{AM}^i\,dF^j-r_{AM}^j\,dF^i\right).
$$

On peut abaisser les indices : $\mathsf M_{ij}=g_{ik}g_{j\ell}\mathsf M^{k\ell}$. En dimension trois, une orientation et la métrique permettent d'identifier un bivecteur à un vecteur axial via le symbole de Levi-Civita :

$$
(\mathfrak M_A)^k=\frac12\varepsilon^k{}_{ij}\mathsf M_A^{ij}.
$$

Cette identification est la raison géométrique pour laquelle le moment est usuellement noté comme un vecteur en mécanique tridimensionnelle. En dimension autre que trois, le bivecteur antisymétrique est l'objet général.

## 3.3 Relation de transport du moment — loi de Varignon

En dimension trois, si $A$ et $B$ sont deux points, la relation de Varignon est

$$
\boldsymbol\mathfrak M_B=\boldsymbol\mathfrak M_A+\overrightarrow{BA}\times\mathbf F.
$$

Le signe dépend de la convention sur le vecteur de position : avec $\mathbf r_{AM}=\overrightarrow{AM}$, on a $\mathbf r_{BM}=\mathbf r_{BA}+\mathbf r_{AM}$, d'où la formule ci-dessus. En dimension $n$, la relation correspondante est

$$
\mathsf M_B^{ij}=\mathsf M_A^{ij}+r_{BA}^iF^j-r_{BA}^jF^i.
$$

La résultante ne dépend pas du point de réduction ; le moment, lui, dépend du point choisi.

# 4. Torseurs et dynamique

## 4.1 Torseur des actions mécaniques

En trois dimensions, le torseur des actions au point $A$ est

$$
\mathscr A(A)=\left\{\begin{array}{c}\mathbf F\\\boldsymbol\mathfrak M_A\end{array}\right\},
$$
avec relation de transport de Varignon. Le torseur est une représentation compacte de la résultante et du moment ; sa signification physique ne dépend pas du choix du point de réduction, même si la valeur du moment change.

## 4.2 Torseur cinétique

La résultante cinétique est $\mathbf P=\int\mathbf v\,dm$. Le moment cinétique au point $A$ est

$$
\mathbf L_A=\int_{\mathscr S}\overrightarrow{AM}\times\mathbf v(M)\,dm.
$$

Le torseur cinétique s'écrit

$$
\mathscr C(A)=\left\{\begin{array}{c}\mathbf P\\\mathbf L_A\end{array}\right\}.
$$

Sa relation de transport est

$$
\mathbf L_B=\mathbf L_A+\overrightarrow{BA}\times\mathbf P.
$$

En dimension $n$, le moment cinétique est le tenseur antisymétrique

$$
\mathsf L_A^{ij}=\int_{\mathscr S}\left(r_{AM}^i v^j-r_{AM}^jv^i\right)dm,
$$
qui vérifie $\mathsf L_B^{ij}=\mathsf L_A^{ij}+r_{BA}^iP^j-r_{BA}^jP^i$.

## 4.3 Torseur dynamique

La résultante dynamique est

$$
\mathbf S=\int_{\mathscr S}\mathbf a(M)\,dm=\frac{d\mathbf P}{dt}
$$
au sens de la dérivée physique dans un référentiel galiléen. Le moment dynamique en $A$ est

$$
\mathbf D_A=\int_{\mathscr S}\overrightarrow{AM}\times\mathbf a(M)\,dm,
$$
si $A$ est fixe dans le référentiel utilisé pour cette écriture. Plus généralement, si $A$ se déplace, la dérivée du moment cinétique contient les termes dus au mouvement du point de réduction.

Le torseur dynamique est

$$
\mathscr D(A)=\left\{\begin{array}{c}\mathbf S\\\mathbf D_A\end{array}\right\}.
$$

Pour un système fermé dans un référentiel galiléen, les théorèmes de la dynamique donnent $\mathscr D(A)=\mathscr A^{\mathrm{ext}}(A)$ sous les hypothèses usuelles et avec une définition cohérente du moment dynamique.

# 5. Théorèmes généraux de la dynamique

## 5.1 Théorème de la résultante dynamique (TRD)

Pour un système matériel fermé dans un référentiel galiléen,

$$
\boxed{\frac{d\mathbf P}{dt}=\mathbf F^{\mathrm{ext}}},\qquad \boxed{m\mathbf a_G=\mathbf F^{\mathrm{ext}}}.
$$

La seconde relation suppose que la masse totale est constante et que $G$ est le centre de masse. Les forces internes s'annulent dans la résultante totale lorsque les forces mutuelles vérifient l'action-réaction et que les conditions du modèle newtonien sont satisfaites.

## 5.2 Théorème du moment dynamique (TMD)

Pour un système fermé, dans un référentiel galiléen, le moment dynamique au point $A$ est égal au moment des forces extérieures au même point lorsque les définitions des dérivées et du point de réduction sont cohérentes :

$$
\boxed{\mathbf D_A=\boldsymbol\mathfrak M_A^{\mathrm{ext}}}.
$$

Si $A$ est fixe dans le référentiel galiléen, on obtient le théorème du moment cinétique

$$
\boxed{\left.\frac{d\mathbf L_A}{dt}\right|_{\mathscr R}=\boldsymbol\mathfrak M_A^{\mathrm{ext}}}.
$$

Si $A$ se déplace, la dérivée de $\mathbf L_A$ ne s'identifie pas en général au moment des forces extérieures sans terme correctif. Pour éviter toute ambiguïté, on part de la définition $\mathbf L_A=\int\overrightarrow{AM}\times\mathbf v\,dm$ et on dérive en tenant compte de $\mathbf v_A$.

## 5.3 Moment cinétique au centre de masse

Le moment cinétique barycentrique est

$$
\mathbf L_G=\int_{\mathscr S}\overrightarrow{GM}\times\mathbf v(M)\,dm.
$$

Dans un référentiel galiléen, son évolution vérifie

$$
\boxed{\frac{d\mathbf L_G}{dt}=\boldsymbol\mathfrak M_G^{\mathrm{ext}}}
$$
avec la dérivée comprise dans le référentiel galiléen et les hypothèses usuelles du système fermé. Le choix du centre de masse simplifie la séparation entre mouvement global et mouvement interne.

En dimension $n$, les équations correspondantes s'écrivent pour le tenseur antisymétrique $\mathsf L_G^{ij}$ et le moment tensoriel extérieur $\mathsf M_G^{ij}$ :

$$
\boxed{\frac{D\mathsf L_G^{ij}}{Dt}=\mathsf M_G^{ij,\mathrm{ext}}}.
$$

Dans un espace euclidien fixe, le membre de gauche peut être interprété dans une base cartésienne constante par la dérivée ordinaire des composantes. Dans une base mobile ou une carte générale, il faut utiliser la dérivée covariante / la dérivée physique adaptée.

# 6. Action-réaction et annulation des actions internes

Soient deux éléments matériels $M$ et $M'$. Pour une interaction newtonienne centrale, les forces mutuelles sont opposées et colinéaires à la droite qui joint les deux points :

$$
d\mathbf F_{M'\to M}=-d\mathbf F_{M\to M'},\qquad \overrightarrow{MM'}\times d\mathbf F_{M'\to M}=\mathbf0.
$$

La première relation entraîne l'annulation des forces internes dans la résultante. La seconde garantit aussi l'annulation de leur moment total. L'antisymétrie seule suffit à la résultante, mais pas, dans le cas général, au moment : il faut la centralité des interactions ou une hypothèse équivalente. Cette distinction est importante lorsque l'on généralise le principe d'action-réaction à des modèles plus riches.

En notation tensorielle, le moment élémentaire d'une interaction centrale est nul parce que $r^iF^j-r^jF^i=0$ lorsque $F^i$ est proportionnel à $r^i$.

# 7. Solide rigide et inertie

## 7.1 Vitesse d'un solide

Pour un solide rigide tridimensionnel, le champ des vitesses vérifie

$$
\mathbf v(M)=\mathbf v(A)+\boldsymbol\Omega\times\overrightarrow{AM}.
$$

Cette relation permet de calculer le moment cinétique à partir de la vitesse d'un point et de la rotation instantanée. En dimension $n$, la formulation correcte utilise un endomorphisme antisymétrique $W^i{}_j$ :

$$
v^i(M)=v^i(A)+W^i{}_j r_{AM}^j,\qquad W_{ij}=-W_{ji}
$$

pour une base orthonormale (ou $W$ antisymétrique au sens de la métrique dans une base quelconque).

## 7.2 Tenseur d'inertie en trois dimensions

Pour un point $A$, le tenseur d'inertie est l'endomorphisme symétrique

$$
I_A^{ij}=\int_{\mathscr S}\left(\|\mathbf r\|^2g^{ij}-r^ir^j\right)dm
$$
(en base cartésienne orthonormale, $I_{ij}=\int(r^2\delta_{ij}-r_ir_j)dm$). Il relie le moment cinétique à la vitesse angulaire par

$$
L_A^i=I_A{}^i{}_j\,\Omega^j
$$
si $A$ est fixe et que la vitesse du solide est une rotation pure autour de $A$. Dans le cas général, le moment cinétique contient aussi la contribution de translation.

Le tenseur d'inertie est symétrique et peut être diagonalisé dans une base orthonormale. Ses vecteurs propres définissent les axes principaux d'inertie. Les moments principaux sont les valeurs propres correspondantes.

## 7.3 Formulation en dimension n

Le tenseur d'inertie d'ordre deux ne suffit pas toujours à identifier une rotation arbitraire en dimension $n$ à un vecteur $\boldsymbol\Omega$, car la vitesse angulaire généralisée possède $n(n-1)/2$ composantes indépendantes. La relation naturelle entre rotation et moment cinétique est alors un opérateur linéaire entre les espaces des bivecteurs / tenseurs antisymétriques :

$$
\mathsf L^{ij}=\int(r^iv^j-r^jv^i)dm,
$$
avec $v^i=W^i{}_k r^k$ pour une rotation autour de l'origine. On obtient une application linéaire $\mathsf L=\mathcal I(W)$ dépendant de la distribution de masse. En trois dimensions, la dualité de Hodge ramène cette relation à la forme usuelle $\mathbf L=I\boldsymbol\Omega$.

# 8. Intégrales dans les coordonnées curvilignes

La géométrie intervient dans les mesures d'intégration, non dans la définition physique des résultantes. Pour une densité volumique $\rho$,

$$
\int_{\mathscr S} f\,dm=\int_{\mathcal U}f(q)\rho(q)\sqrt{g(q)}\,dq^1\cdots dq^n.
$$

En coordonnées cylindriques tridimensionnelles, $dV=r\,dr\,d\theta\,dz$. En coordonnées sphériques avec angle polaire $\theta$ et azimut $\varphi$, $dV=r^2\sin\theta\,dr\,d\theta\,d\varphi$. Ces facteurs viennent de $\sqrt{\det(g_{ij})}$ et ne doivent pas être ajoutés une seconde fois si l'on intègre déjà avec la mesure géométrique $dV$.

Pour le centre de masse, la quantité de mouvement, le moment cinétique et le tenseur d'inertie, intégrer chaque composante dans une base commune, ou formuler l'intégrale directement comme intégrale d'un champ vectoriel/tensoriel. Les bases unitaires curvilignes dépendent du point : on ne peut pas sortir de l'intégrale un vecteur de base variable sans justification.

# 9. Référentiels non galiléens

Dans un référentiel en translation accélérée et en rotation, les équations de Newton font apparaître des forces d'inertie. En trois dimensions, avec une origine $O'$ d'accélération $\mathbf a_{O'}$, une vitesse relative $\mathbf v'$ et un vecteur rotation $\boldsymbol\Omega$, l'accélération absolue vaut

$$
\mathbf a=\mathbf a_{O'}+\mathbf a'+2\boldsymbol\Omega\times\mathbf v'+\dot{\boldsymbol\Omega}\times\mathbf r'+\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r').
$$

Ainsi l'équation relative s'écrit

$$
m\mathbf a'=\mathbf F^{\mathrm{réelles}}-m\mathbf a_{O'}-2m\boldsymbol\Omega\times\mathbf v'-m\dot{\boldsymbol\Omega}\times\mathbf r'-m\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r').
$$

Les termes du membre de droite supplémentaires sont la force d'inertie de translation, la force de Coriolis, la force d'Euler et la force centrifuge selon cette convention. En dimension $n$, les produits vectoriels sont remplacés par l'action de l'endomorphisme antisymétrique $W$ et ses dérivées : $2Wv'$, $\dot W r'$ et $W^2r'$, avec les signes fixés par le choix du référentiel et de la définition de $W$.

# 10. Exemple : rotation autour d'un axe fixe

Considérons un solide tournant autour de l'axe $Oz$ avec $\boldsymbol\Omega=\Omega\mathbf e_z$. Pour un point $M$ de coordonnées cylindriques $(r,\theta,z)$, la vitesse de rotation est

$$
\mathbf v(M)=\boldsymbol\Omega\times\overrightarrow{OM}=\Omega r\,\mathbf u_\theta.
$$

La composante du moment cinétique sur l'axe vaut

$$
L_z=\int_{\mathscr S}(\overrightarrow{OM}\times\mathbf v)\cdot\mathbf e_z\,dm
=\Omega\int_{\mathscr S}r^2dm.
$$

On définit le moment d'inertie autour de l'axe par

$$
J_z:=\int_{\mathscr S}r^2dm,
$$
ce qui donne $L_z=J_z\Omega$. Cette simplification concerne la composante axiale ; le vecteur moment cinétique n'est pas nécessairement parallèle à $\boldsymbol\Omega$ si l'axe choisi n'est pas un axe principal d'inertie.

# 11. Checklist de cohérence tensorielle

- Les indices sont-ils cohérents ? Un vecteur s'écrit $v^i\mathbf e_i$ ; un covecteur s'écrit $\alpha_i dq^i$.
- Les contractions se font-elles entre un indice haut et un indice bas ?
- La métrique est-elle utilisée pour abaisser/élever les indices ?
- Les composantes sont-elles exprimées dans la même base avant sommation ?
- L'intégrale utilise-t-elle la mesure $dm$ appropriée, sans double compter le facteur $\sqrt g$ ?
- Le point de réduction du moment est-il explicite ?
- Le point $A$ est-il fixe ou mobile lors de la dérivation temporelle ?
- L'emploi du produit vectoriel est-il limité au cas tridimensionnel euclidien orienté ?
- L'annulation des moments internes repose-t-elle sur une hypothèse de centralité, et pas uniquement sur l'action-réaction ?
- Le référentiel est-il galiléen pour l'application directe des théorèmes de Newton ?

# 12. Formulaire général

$$
\boxed{P^i=\int v^i\,dm},\qquad \boxed{\frac{d\mathbf P}{dt}=\mathbf F^{\mathrm{ext}}},\qquad \boxed{\mathfrak M_A^{ij}=\int(r_{AM}^i\,dF^j-r_{AM}^j\,dF^i)}
$$
$$
\boxed{L_A^{ij}=\int(r_{AM}^iv^j-r_{AM}^jv^i)\,dm},\qquad \boxed{L_B^{ij}=L_A^{ij}+r_{BA}^iP^j-r_{BA}^jP^i}
$$
$$
\boxed{\frac{D L_A^{ij}}{Dt}=\mathfrak M_A^{ij,\mathrm{ext}}}\quad\text{(avec point de réduction et dérivée définis de manière cohérente).}
$$

