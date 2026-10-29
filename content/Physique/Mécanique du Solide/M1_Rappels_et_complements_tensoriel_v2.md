---
title: Rappels et compléments — cinématique, dynamique, principes variationnels et solide en dimension $n$ (formulation tensorielle)
tags:
  - Agrégation
  - Physique
  - Mécanique
  - Calcul tensoriel
niveau: Doctorat
version: 1.0
---

---
[^1]: Physique pour l'agrégation, Jules Fillette - Julien Froustey - Hugo Roussille
[^2]: Physique Spé. PC*, PC, Cours et exercices d'application, Stéphane Olivier, Hubert Gié, Jean-Pierre Sarmant
[^3]: Formulaire MATHS, PHYSIQUE, CHIMIE, SII (2e édition), MPSI-MP, Bertrand Hauchecorne
[^4]: Formulaire MATHS, PHYSIQUE, CHIMIE, SII (3e édition), PCSI-MPSI/PTSI-PSI, Bertrand Beaufils
[^5]: Jérôme Perez, *Le théorème de Noether. Son centenaire, sa signification et sa portée*, Quadrature n°100 (2018)
[^6]: Documents associés : *Dynamique des systèmes matériels fermés*, *Dynamique tensorielle des systèmes matériels*, *Cinématique tensorielle et géométrie*, *Opérateurs différentiels et métrique en coordonnées curvilignes*
---

> [!abstract] Plan et esprit du document
> On reprend *Rappels et compléments* (cinématique du solide, éléments cinématiques d'un système fermé) en le **réécrivant en dimension $n$** avec la métrique $g$, des composantes **contravariantes** $A^i$ et **covariantes** $A_i$, la base $\vec e_i$, et une **rotation instantanée** définie comme un opérateur $g$-antisymétrique (et non comme un vecteur, qui n'existe qu'en dimension 3).
> Tout est **démontré** : composition des vitesses et des accélérations, forces d'inertie, lois de Newton, théorèmes de la résultante, du moment, de l'énergie, du viriel. On passe ensuite aux formalismes **lagrangien** et **hamiltonien** (théorème de Liouville), au **théorème de Noether** (qui redonne PFD, TEC, TEM, TMC, l'équation de Schrödinger, etc.), puis au **solide** et au calcul de **moments d'inertie**.

# 0. Conventions et outils

>[!question]- $=$, $:=$, $\doteq$, $\equiv$ : conventions d'écriture
>- $=$ : égalité (résultat, équation) ;
>- $:=$ ou $\doteq$ : **définition** (on introduit l'objet) ;
>- $\equiv$ : identité valable pour tout argument, ou identification canonique (par exemple entre un objet et ses composantes dans une base fixée).

## 0.1 Espace, base, métrique

- L'espace physique est un espace affine euclidien $\mathscr E$ de dimension $n$, de direction $V$ (espace vectoriel) muni d'un produit scalaire $g$ ; $n=3$ pour la physique usuelle, mais **rien ne l'impose** sauf mention explicite.
- Un **référentiel** $\mathscr R \doteq (O;\vec e_1,\dots,\vec e_n)$ est un repère affine : une origine et une base **constante dans $\mathscr R$**. La base n'est pas supposée orthonormée :
$$
g_{ij} := g(\vec e_i,\vec e_j) = \vec e_i\cdot\vec e_j,\qquad g^{ik}g_{kj}=\delta^i{}_j,\qquad \partial_t g_{ij}=0 \ \text{ dans } \mathscr R .
$$
- **Convention d'Einstein** : un indice répété, une fois en haut et une fois en bas, est sommé. Un vecteur s'écrit $\vec A = A^i\vec e_i$ ($A^i$ : composantes **contravariantes**) ; ses composantes **covariantes** sont $A_i = g_{ij}A^j = \vec A\cdot\vec e_i$. Le produit scalaire est $\vec A\cdot\vec B = g_{ij}A^iB^j = A_iB^i$.
- Les $(\vec e_i)$ constants donnent $\vec v^{\,i} = \dot x^i$, $a^i = \ddot x^i$ (composantes contravariantes de la dérivée = dérivée des composantes). En coordonnées curvilignes $q^i$ avec $\vec e_i(q)=\partial\vec r/\partial q^i$ et $g_{ij}(q)$ variable, la **dérivée covariante** le long de la trajectoire remplace $\dot A^i$ :
$$
\frac{D A^i}{dt} := \dot A^i + \Gamma^i{}_{jk}\,\dot q^j A^k,\qquad \Gamma^i{}_{jk}=\tfrac12 g^{i\ell}(\partial_j g_{\ell k}+\partial_k g_{\ell j}-\partial_\ell g_{jk}),
$$
et $a^i = \ddot q^i + \Gamma^i{}_{jk}\dot q^j\dot q^k$. Dans un espace euclidien décrit par un repère affine, $\Gamma\equiv 0$ ; on garde la notation $D/dt$ pour que les formules restent valables dans toute carte.
- **Compatibilité métrique** : $\dfrac{d}{dt}\,g(\vec A,\vec B)=g\!\left(\dfrac{D\vec A}{dt},\vec B\right)+g\!\left(\vec A,\dfrac{D\vec B}{dt}\right)$.

## 0.2 Tenseurs antisymétriques et produit extérieur

En dimension $n$ il n'y a pas de produit vectoriel $V\times V\to V$. Pour $\vec u,\vec w\in V$ on définit le **bivecteur** (tenseur antisymétrique contravariant)
$$
(\vec u\wedge\vec w)^{ij} := u^iw^j-u^jw^i .
$$
En dimension 3 orientée, avec $\varepsilon_{ijk}=\sqrt{g}\,[ijk]$ ($g=\det g_{ij}$, $[ijk]$ symbole de permutation) et $\varepsilon^i{}_{jk}=g^{i\ell}\varepsilon_{\ell jk}$, l'identification de Hodge est
$$
(\vec u\times\vec w)^k=\tfrac12\varepsilon^k{}_{ij}(\vec u\wedge\vec w)^{ij},\qquad (\vec u\wedge\vec w)^{ij}=\varepsilon^{ijk}(\vec u\times\vec w)_k .
$$
Un bivecteur $\mathsf M^{ij}$ est donc l'objet « moment » en dimension $n$ ; il a $n(n-1)/2$ composantes indépendantes ($3$ en dimension 3, $1$ en dimension 2, $6$ en dimension 4).

## 0.3 Groupe et algèbre des rotations

- $O(V,g)=\{f\in GL(V)\mid g(f\vec x,f\vec y)=g(\vec x,\vec y)\}$ (isométries). Pour $f\in O(V,g)$ : $f^\ast f=\mathrm{id}$, où l'adjoint $f^\ast$ est défini par $g(f\vec x,\vec y)=g(\vec x,f^\ast\vec y)$ ; donc $f^{-1}=f^\ast$.
- $SO(V,g)=\{f\in O(V,g)\mid \det f=1\}$ ; c'est un groupe de Lie connexe de dimension $n(n-1)/2$.
- Son algèbre de Lie est $\mathfrak{so}(V,g)=\{\Omega\in\mathrm{End}(V)\mid \Omega^\ast=-\Omega\}$. En composantes, $\Omega_{ij}:=g_{ik}\Omega^k{}_j$ vérifie $\Omega_{ij}=-\Omega_{ji}$ : on **identifie** $\mathfrak{so}(V,g)\equiv\Lambda^2V$ (bivecteurs). En dimension 3 : $\Omega(\vec x)=\vec\omega\times\vec x$, soit $\Omega^i{}_j=\varepsilon^i{}_{kj}\omega^k$ et $\omega^k=-\tfrac12\varepsilon^{kij}\Omega_{ij}$ (à orientation fixée).

>[!tip]- Pourquoi $\Omega^2$ est utile : un opérateur symétrique négatif
>Si $\Omega\in\mathfrak{so}(V,g)$, alors $g(\vec x,\Omega\vec x)=0$ et $g(\vec x,\Omega^2\vec x)=-g(\Omega\vec x,\Omega\vec x)\le 0$. Donc $\Omega^2$ est $g$-symétrique, négatif ; on le retrouvera dans la force centrifuge.

>[!tip]- Exponentielle et formule de Rodrigues (cas $n=3$)
>Pour $\Omega=\hat\omega$ constant ($\hat\omega\vec x=\vec\omega\times\vec x$), $\theta:=\|\vec\omega\|$, on a $\hat\omega^3=-\theta^2\hat\omega$, donc
>$$
>\exp(\hat\omega)=\mathrm{id}+\frac{\sin\theta}{\theta}\hat\omega+\frac{1-\cos\theta}{\theta^2}\hat\omega^{2}\in SO(3).
>$$
>Si maintenant $f_t=\exp(\hat v(t))$ avec $\vec v(t)$ variable, la rotation instantanée $\Omega_t=\dot f_tf_t^{-1}=\hat\omega$ est (dérivée de l'exponentielle)
>$$
>\vec\omega=\dot{\vec v}+\frac{1-\cos\theta}{\theta^2}\,\vec v\times\dot{\vec v}+\frac{\theta-\sin\theta}{\theta^3}\,\vec v\times(\vec v\times\dot{\vec v}),\qquad\theta=\|\vec v\|.
>$$
>Avec $\vec v=\theta\vec u$ : $\vec\omega=\underbrace{\dot\theta\vec u}_{\text{spin}}+\underbrace{\theta\dot{\vec u}}_{\text{transport de l'axe}}+\underbrace{(1-\cos\theta)\,\vec u\times\dot{\vec u}+(\theta-\sin\theta)\,\vec u\times(\vec u\times\dot{\vec u})}_{\text{non-commutativité de }SO(3)}$. Dans ce dernier cas $\vec v\times\dot{\vec v}=\theta^2\,\vec u\times\dot{\vec u}$, car $\vec u\times\vec u=0$.

# 1. Cinématique des référentiels

## 1.1 Deux référentiels

- $\mathscr R\doteq(O;\vec e_1,\dots,\vec e_n)$, base **constante** dans $\mathscr R$, métrique $g_{ij}$.
- $\mathscr R'\doteq(O';\vec e_{1'}(t),\dots,\vec e_{n'}(t))$, **mobile** par rapport à $\mathscr R$ et **indéformable** : sa base a, à tout instant, la même matrice de Gram, $g_{i'j'}=g(\vec e_{i'},\vec e_{j'})=\text{cste}$.
- Le temps est absolu : $t'=t$.

Le point $M$ est repéré par $\overrightarrow{OM}=x^i\vec e_i$ dans $\mathscr R$ et par $\overrightarrow{O'M}=x^{i'}\vec e_{i'}$ dans $\mathscr R'$, avec $\overrightarrow{OM}=\overrightarrow{OO'}+\overrightarrow{O'M}$. On note $\left.\vec A\right)_{\mathscr R}$ « le vecteur $\vec A$ vu depuis $\mathscr R$ » et $\left.\dfrac{d\vec A}{dt}\right)_{\mathscr R}$ la dérivée prise dans $\mathscr R$ (base fixe dans $\mathscr R$).

**Vitesse et accélération dans $\mathscr R$ et $\mathscr R'$** (la base du référentiel considéré est constante dans celui-ci) :
$$
\vec v_{\mathscr R}(M)=\left.\frac{d\overrightarrow{OM}}{dt}\right)_{\mathscr R}=\dot x^i\vec e_i,\quad \vec a_{\mathscr R}(M)=\ddot x^i\vec e_i,\qquad
\vec v_{\mathscr R'}(M)=\left.\frac{d\overrightarrow{O'M}}{dt}\right)_{\mathscr R'}=\dot x^{i'}\vec e_{i'},\quad \vec a_{\mathscr R'}(M)=\ddot x^{i'}\vec e_{i'}.
$$

## 1.2 Rotation instantanée de $\mathscr R'$ par rapport à $\mathscr R$

**Définition.** $\mathscr R'$ étant indéformable, il existe un **unique** opérateur linéaire $\Omega_{\mathscr R'/\mathscr R}(t)\in\mathrm{End}(V)$ tel que
$$
\boxed{\;\left.\frac{d\vec e_{j'}}{dt}\right)_{\mathscr R}=\Omega_{\mathscr R'/\mathscr R}(\vec e_{j'})=\Omega^{i'}{}_{j'}\,\vec e_{i'},\qquad j=1,\dots,n.\;}
$$
(Il suffit de décomposer $\dot{\vec e}_{j'}$ sur la base $(\vec e_{i'})$ : cela définit les $\Omega^{i'}{}_{j'}$, donc $\Omega$.)

>[!tip]+ **Proposition 1.** $\Omega_{\mathscr R'/\mathscr R}\in\mathfrak{so}(V,g)$, c'est-à-dire $\Omega_{ij}=-\Omega_{ji}$.
>
>*Démonstration (par la rigidité).* Les $g_{i'j'}=g(\vec e_{i'},\vec e_{j'})$ sont constants. Dérivons (compatibilité métrique, base de $\mathscr R$ constante) :
>$$
>0=\frac{d}{dt}g(\vec e_{i'},\vec e_{j'})=g(\dot{\vec e}_{i'},\vec e_{j'})+g(\vec e_{i'},\dot{\vec e}_{j'})=\Omega^{k'}{}_{i'}g_{k'j'}+g_{i'k'}\Omega^{k'}{}_{j'}=\Omega_{j'i'}+\Omega_{i'j'} .\qquad\square
>$$
>*Démonstration (par le groupe).* Comme les matrices de Gram coïncident, l'application linéaire $f_t$ qui envoie $\vec e_{i'}(0)$ sur $\vec e_{i'}(t)$ vérifie $g(f_t\vec x,f_t\vec y)=g(\vec x,\vec y)$ : $f_t\in O(V,g)$, et par continuité (à partir de $f_0=\mathrm{id}$) $f_t\in SO(V,g)$. Alors $\dot{\vec e}_{i'}(t)=\dot f_t\,\vec e_{i'}(0)=\dot f_tf_t^{-1}\vec e_{i'}(t)$, donc $\Omega=\dot f_tf_t^{-1}$. Dériver $f_tf_t^\ast=\mathrm{id}$ donne $\dot f_tf_t^\ast+f_t\dot f_t^\ast=0$, soit $\Omega+\Omega^\ast=0$ (car $f_t^{-1}=f_t^\ast$). $\square$

**Conséquences.**
- Une rotation instantanée possède $n(n-1)/2$ degrés de liberté : $1$ en dimension 2 (un scalaire $\dot\theta$ : $\Omega^i{}_j=\dot\theta\,\varepsilon^i{}_j$), $3$ en dimension 3 (un vecteur axial $\vec\omega$), $6$ en dimension 4 (deux plans de rotation indépendants). Le **vecteur-rotation** $\vec\Omega$ des cours usuels n'existe qu'en dimension 3 et vaut $\vec\omega$ avec $\Omega(\vec x)=\vec\omega\times\vec x$.
- La dérivée de $\Omega$ ne dépend pas du référentiel de dérivation : $\left.\dot\Omega\right)_{\mathscr R}=\left.\dot\Omega\right)_{\mathscr R'}+[\Omega,\Omega]=\left.\dot\Omega\right)_{\mathscr R'}$ (on le notera $\dot\Omega$). En dimension 3 : $\dot\Omega=\hat{\dot\omega}$.

## 1.3 Dérivation d'un vecteur dans deux référentiels (théorème de transport)

>[!tip]+ **Théorème de transport.** Pour tout vecteur $\vec A(t)$,
>$$
>\boxed{\left.\frac{d\vec A}{dt}\right)_{\mathscr R}=\left.\frac{d\vec A}{dt}\right)_{\mathscr R'}+\Omega_{\mathscr R'/\mathscr R}(\vec A)},\qquad\text{soit en composantes}\quad \left(\dot A^{i'}+\Omega^{i'}{}_{j'}A^{j'}\right)\vec e_{i'}.
>$$
>*Démonstration.* Écrivons $\vec A=A^{i'}\vec e_{i'}$. Dans $\mathscr R'$, la base est constante : $\left.\frac{d\vec A}{dt}\right)_{\mathscr R'}=\dot A^{i'}\vec e_{i'}$. Dans $\mathscr R$ : $\left.\frac{d\vec A}{dt}\right)_{\mathscr R}=\dot A^{i'}\vec e_{i'}+A^{j'}\left.\frac{d\vec e_{j'}}{dt}\right)_{\mathscr R}=\dot A^{i'}\vec e_{i'}+A^{j'}\Omega^{i'}{}_{j'}\vec e_{i'}$. $\square$

*En dimension 3* : $\left.\frac{d\vec A}{dt}\right)_{\mathscr R}=\left.\frac{d\vec A}{dt}\right)_{\mathscr R'}+\vec\omega\times\vec A$. *Cas d'un tenseur* : pour $T^{ij}$ à deux indices contravariants, $\left.\dot T^{ij}\right)_{\mathscr R}=\left.\dot T^{ij}\right)_{\mathscr R'}+\Omega^i{}_kT^{kj}+\Omega^j{}_kT^{ik}$, soit $\dot T+[\Omega,T]$ si $T$ est antisymétrique ou si on écrit matriciellement en base orthonormée ($\Omega^T=-\Omega$).

## 1.4 Loi de composition des vitesses

$$
\vec v_{\mathscr R}(M)=\left.\frac{d\overrightarrow{OO'}}{dt}\right)_{\mathscr R}+\left.\frac{d\overrightarrow{O'M}}{dt}\right)_{\mathscr R}
=\vec v_{\mathscr R}(O')+\underbrace{\left.\frac{d\overrightarrow{O'M}}{dt}\right)_{\mathscr R'}}_{\vec v_{\mathscr R'}(M)}+\Omega(\overrightarrow{O'M}),
$$
d'après le théorème de transport. Donc
$$
\boxed{\vec v_{\mathscr R}(M)=\vec v_{\mathscr R'}(M)+\vec v^{\,ie}_{\mathscr R'/\mathscr R}(M),\qquad \vec v^{\,ie}_{\mathscr R'/\mathscr R}(M)=\vec v_{\mathscr R}(O')+\Omega(\overrightarrow{O'M})}
$$
$$
\text{soit}\qquad v^i=v^{i}_{\prime}+v^i(O')+\Omega^i{}_jx^{j'}.
$$
La **vitesse d'entraînement** $\vec v^{\,ie}$ est la vitesse dans $\mathscr R$ du point **fixe de $\mathscr R'$** qui coïncide avec $M$ à l'instant $t$ (prendre $\vec v_{\mathscr R'}(M)=0$).

## 1.5 Loi de composition des accélérations

On dérive la loi précédente dans $\mathscr R$, terme à terme.

1. $\left.\dfrac{d\vec v_{\mathscr R}(O')}{dt}\right)_{\mathscr R}=\vec a_{\mathscr R}(O')$.
2. $\left.\dfrac{d\vec v_{\mathscr R'}(M)}{dt}\right)_{\mathscr R}=\underbrace{\left.\dfrac{d\vec v_{\mathscr R'}(M)}{dt}\right)_{\mathscr R'}}_{\vec a_{\mathscr R'}(M)}+\Omega(\vec v_{\mathscr R'}(M))$.
3. $\left.\dfrac{d}{dt}\Omega(\overrightarrow{O'M})\right)_{\mathscr R}=\dot\Omega(\overrightarrow{O'M})+\Omega\!\left(\left.\dfrac{d\overrightarrow{O'M}}{dt}\right)_{\mathscr R}\right)=\dot\Omega(\overrightarrow{O'M})+\Omega\!\left(\vec v_{\mathscr R'}(M)+\Omega(\overrightarrow{O'M})\right)$.

En additionnant :
$$
\boxed{\vec a_{\mathscr R}(M)=\vec a_{\mathscr R'}(M)+\vec a^{\,ie}_{\mathscr R'/\mathscr R}(M)+\vec a^{\,ic}_{\mathscr R'/\mathscr R}(M)}
$$
$$
\vec a^{\,ie}=\vec a_{\mathscr R}(O')+\dot\Omega(\overrightarrow{O'M})+\Omega^2(\overrightarrow{O'M}),\qquad \vec a^{\,ic}=2\,\Omega(\vec v_{\mathscr R'}(M)).
$$
En composantes : $a^i=a^{i}_{\prime}+a^i(O')+2\Omega^i{}_jv^{j}_{\prime}+\left(\dot\Omega^i{}_j+\Omega^i{}_k\Omega^k{}_j\right)x^{j'}$. En dimension 3 :
$$
\vec a_{\mathscr R}(M)=\vec a_{\mathscr R'}(M)+\vec a_{\mathscr R}(O')+\underbrace{\dot{\vec\omega}\times\overrightarrow{O'M}}_{\text{Euler}}+\underbrace{\vec\omega\times(\vec\omega\times\overrightarrow{O'M})}_{\text{centripète}}+\underbrace{2\vec\omega\times\vec v_{\mathscr R'}(M)}_{\text{Coriolis}}.
$$

>[!warning]- Correction par rapport à la version d'origine
>Le terme « centripète » est $\Omega^2(\overrightarrow{O'M})=\vec\omega\times(\vec\omega\times\overrightarrow{O'M})$, **et non** $\vec\omega\times(\vec\omega\times\vec v_{\mathscr R'}(M))$ comme écrit par erreur dans l'ancienne version ; le terme d'Euler $\dot{\vec\omega}\times\overrightarrow{O'M}$ doit aussi figurer dans $\vec a^{\,ie}$.

**Cas particulier — $\mathscr R'$ en translation** ($\Omega=0$) : $\vec v_{\mathscr R}(M)=\vec v_{\mathscr R'}(M)+\vec v_{\mathscr R}(O')$, $\ \vec a_{\mathscr R}(M)=\vec a_{\mathscr R'}(M)+\vec a_{\mathscr R}(O')$.

# 2. Dynamique du point : lois de Newton et forces d'inertie

## 2.1 Les lois de Newton

On postule, pour la mécanique newtonienne (espace euclidien $\mathscr E$, temps absolu) :

1. **Principe d'inertie (1re loi).** Il existe des référentiels, dits **galiléens**, dans lesquels tout point matériel isolé (soumis à aucune force) a une accélération nulle : $\vec a_{\mathscr R}(M)=\vec 0$.
2. **Principe fondamental de la dynamique (2e loi).** Dans un référentiel galiléen, pour un point matériel de masse $m$ soumis à la résultante $\vec F$ des forces : $m\,\vec a_{\mathscr R}(M)=\vec F$, soit $m\,a^i=F^i$, ou $m\,g_{ij}a^j=F_i$.
3. **Principe des actions réciproques (3e loi).** $\vec F_{A\to B}=-\vec F_{B\to A}$ (forme faible). **Forme forte** : de plus, ces forces sont portées par la droite $AB$ (forces centrales) : $\overrightarrow{AB}\wedge\vec F_{A\to B}=0$.

Les forces d'interaction sont **invariantes par changement de référentiel** (elles ne dépendent que des positions et vitesses relatives).

## 2.2 Caractérisation des référentiels galiléens

>[!tip]+ **Proposition 2.** Soit $\mathscr R$ galiléen. Alors $\mathscr R'$ est galiléen $\iff$ $\mathscr R'$ est en **translation rectiligne uniforme** par rapport à $\mathscr R$ ($\Omega_{\mathscr R'/\mathscr R}=0$ et $\vec a_{\mathscr R}(O')=\vec 0$).
>
>*Démonstration.* ($\Leftarrow$) Avec $\Omega=0$, $\vec a_{\mathscr R'}(M)=\vec a_{\mathscr R}(M)-\vec a_{\mathscr R}(O')=\vec a_{\mathscr R}(M)$ : l'accélération d'un point isolé est nulle dans $\mathscr R'$ aussi, et la 2e loi garde la même forme (les forces sont invariantes).
>($\Rightarrow$) Un point isolé a $\vec a_{\mathscr R}=\vec a_{\mathscr R'}=\vec 0$ ; d'après 1.5, pour toutes conditions initiales $(\overrightarrow{O'M},\vec v_{\mathscr R'}(M))$ :
>$$
>\vec 0=\vec a_{\mathscr R}(O')+\left(\dot\Omega+\Omega^2\right)\overrightarrow{O'M}+2\,\Omega\,\vec v_{\mathscr R'}(M).
>$$
>En $\overrightarrow{O'M}=\vec 0$, la vitesse $\vec v_{\mathscr R'}$ étant arbitraire, $\Omega=0$ ; il reste $\vec a_{\mathscr R}(O')=\vec 0$. $\square$

*Corollaire (relativité galiléenne).* Le groupe de Galilée $\{\vec x\to R\vec x+\vec ut+\vec c,\ t\to t+s\}$ avec $R\in O(V,g)$ laisse invariante la 2e loi.

## 2.3 Forces d'inertie

Dans $\mathscr R$ galiléen, $m\vec a_{\mathscr R}(M)=\vec F$. En utilisant 1.5 :
$$
\boxed{m\,\vec a_{\mathscr R'}(M)=\vec F\underbrace{-m\,\vec a_{\mathscr R}(O')}_{\vec F^{ie}_{\text{transl.}}}\ \underbrace{-m\,\dot\Omega(\overrightarrow{O'M})}_{\vec F_{\text{Euler}}}\ \underbrace{-m\,\Omega^2(\overrightarrow{O'M})}_{\vec F_{\text{centrifuge}}}\ \underbrace{-2m\,\Omega(\vec v_{\mathscr R'}(M))}_{\vec F^{ic}_{\text{Coriolis}}}}
$$
- $\vec F^{ie}=-m\,\vec a^{\,ie}$ (force d'inertie d'entraînement), $\vec F^{ic}=-m\,\vec a^{\,ic}$ (force d'inertie de Coriolis).
- **Centrifuge** : $\vec F=-m\Omega^2\vec r'$ ; son produit scalaire avec $\vec r'$ vaut $-m\,g(\vec r',\Omega^2\vec r')=m\,\|\Omega\vec r'\|^2\ge 0$ : elle écarte de l'axe de rotation (dimension 3 : $+m\omega^2\vec r'_\perp$).
- **Coriolis** : $g(\vec v',\Omega\vec v')=0$ ; **elle ne travaille pas**.
- Si $\mathscr R'$ est en rotation uniforme autour d'un point fixe : $\vec F^{ie}=-m\Omega^2\vec r'$.

# 3. Éléments cinématiques d'un système fermé

## 3.1 Centre d'inertie, référentiel barycentrique

Soit $\mathscr S$ un système matériel fermé, de mesure de masse $dm(M)$ et de masse totale $m=\int_{\mathscr S}dm$ (conservée).

**Centre d'inertie** $G$ : $\displaystyle\int_{M\in\mathscr S}\overrightarrow{GM}\,dm(M)=\vec 0$ ; pour toute origine $O$, $\ m\,\overrightarrow{OG}=\int_{\mathscr S}\overrightarrow{OM}\,dm(M)$. (Cette définition est affine : en coordonnées curvilignes on intègre les composantes cartésiennes d'immersion, pas la moyenne des $q^i$.)

**Référentiel barycentrique** $\mathscr R^\ast\doteq(G;\vec e_1,\dots,\vec e_n)$ : en **translation** par rapport à $\mathscr R$ ($\Omega_{\mathscr R^\ast/\mathscr R}=0$) et d'origine $G$. Les compositions de 1.4 et 1.5 donnent
$$
\boxed{\vec v_{\mathscr R}(M)=\vec v_{\mathscr R^\ast}(M)+\vec v_{\mathscr R}(G),\qquad \vec a_{\mathscr R}(M)=\vec a_{\mathscr R^\ast}(M)+\vec a_{\mathscr R}(G).}
$$
Remarque : $\mathscr R^\ast$ n'est galiléen que si $\vec a_{\mathscr R}(G)=\vec 0$.

## 3.2 Torseur cinétique

**Définition.**
$$
\vec P_{\mathscr S/\mathscr R}:=\int_{\mathscr S}\vec v_{\mathscr R}(M)\,dm(M),\qquad
\mathsf L^{ij}_{\mathscr S/\mathscr R}(A):=\int_{\mathscr S}\left(\overrightarrow{AM}\wedge\vec v_{\mathscr R}(M)\right)^{ij}dm(M)=\int_{\mathscr S}\left(r^i_{AM}v^j-r^j_{AM}v^i\right)dm .
$$
Composantes de $\vec P$ : $P^i=\int v^i\,dm$, $P_i=g_{ij}P^j$. Le **moment cinétique** $\mathsf L(A)$ est un bivecteur ; en dimension 3, $\vec L(A)=\int\overrightarrow{AM}\times\vec v\,dm$, $L^k=\tfrac12\varepsilon^k{}_{ij}\mathsf L^{ij}$.

>[!tip]- Remarque
>$\vec P$ est une grandeur intrinsèque au système ; $\mathsf L$ **dépend du point $A$** choisi.

**Expression opérationnelle de $\vec P$.** En dérivant $m\overrightarrow{OG}=\int\overrightarrow{OM}dm$ :
$$
m\,\vec v_{\mathscr R}(G)=\int\vec v_{\mathscr R}(M)\,dm=\vec P_{\mathscr S/\mathscr R}\quad\Longrightarrow\quad \boxed{\vec P_{\mathscr S/\mathscr R}=m\,\vec v_{\mathscr R}(G),\quad \vec P_{\mathscr S/\mathscr R^\ast}=\vec 0,\quad m\,\vec a_{\mathscr R}(G)=\left.\frac{d\vec P}{dt}\right)_{\mathscr R}.}
$$

**Changement de point (BABAR).** Pour $A,B$ quelconques, avec $\overrightarrow{BM}=\overrightarrow{BA}+\overrightarrow{AM}$ :
$$
\boxed{\mathsf L(B)=\mathsf L(A)+\overrightarrow{BA}\wedge\vec P,\qquad \mathsf L^{ij}(B)=\mathsf L^{ij}(A)+BA^iP^j-BA^jP^i.}
$$

>[!tip]- **Torseur** (structure générale) : $\{\,\vec R\,;\,\mathsf M(A)\,\}$
>Un **torseur** est un couple (résultante $\vec R\in V$, champ de moments $A\mapsto\mathsf M(A)\in\Lambda^2V$) vérifiant la relation de changement de point $\mathsf M(B)=\mathsf M(A)+\overrightarrow{BA}\wedge\vec R$ (« **BABAR** »). En dimension 3, avec $\vec M=\tfrac12\varepsilon\,\mathsf M$ : $\vec M(B)=\vec M(A)+\overrightarrow{BA}\times\vec R$. Exemples :
>- cinétique $\mathscr C(A)=\{\vec P;\mathsf L(A)\}$ ; dynamique $\mathscr D(A)=\{\vec S;\mathsf D(A)\}$ ; des actions $\mathscr A(A)=\{\vec F;\mathsf M(A)\}$.
>- **Torseur cinématique** (rôles inversés) : $\mathscr V(A)=\{\Omega\ ;\ \vec v(A)\}$ avec $\vec v(B)=\vec v(A)+\Omega(\overrightarrow{AB})=\vec v(A)-\Omega(\overrightarrow{BA})$ ; en dimension 3, $\vec v(B)=\vec v(A)+\overrightarrow{BA}\times\vec\omega$.
>- **Comoment** (pairing) : $\langle\mathscr A,\mathscr V\rangle:=\vec F\cdot\vec v(A)+\tfrac12\mathsf M^{ij}(A)\,\Omega_{ji}$, indépendant de $A$ ; il représente la **puissance** de $\mathscr A$ sur un solide animé de $\mathscr V$ ; en dimension 3 : $\vec F\cdot\vec v_A+\vec M_A\cdot\vec\omega$.

## 3.3 Moment cinétique barycentrique, théorème de Koenig

Dans $\mathscr R^\ast$, $\vec P_{\mathscr S/\mathscr R^\ast}=\vec 0$, donc d'après BABAR $\mathsf L_{\mathscr S/\mathscr R^\ast}(B)=\mathsf L_{\mathscr S/\mathscr R^\ast}(A)=:\mathsf L^\ast$ : le **moment cinétique barycentrique** est **indépendant du point**.

>[!tip]+ **Théorème de Koenig (moment cinétique).** $\ \boxed{\mathsf L_{\mathscr S/\mathscr R}(A)=\mathsf L^\ast+m\,\overrightarrow{AG}\wedge\vec v_{\mathscr R}(G)}$.
>
>*Démonstration.* $\vec v_{\mathscr R}(M)=\vec v_{\mathscr R^\ast}(M)+\vec v_{\mathscr R}(G)$ donne $\mathsf L(A)=\int\overrightarrow{AM}\wedge\vec v_{\mathscr R^\ast}\,dm+\left(\int\overrightarrow{AM}\,dm\right)\wedge\vec v_{\mathscr R}(G)$. Or $\int\overrightarrow{AM}dm=m\overrightarrow{AG}$ et $\int\overrightarrow{AM}\wedge\vec v_{\mathscr R^\ast}dm=\int\left(\overrightarrow{AG}+\overrightarrow{GM}\right)\wedge\vec v_{\mathscr R^\ast}dm=\overrightarrow{AG}\wedge\vec P_{\mathscr S/\mathscr R^\ast}+\mathsf L^\ast=\mathsf L^\ast$. $\square$

*Interprétation* : moment cinétique = « mouvement propre » ($\mathscr S/\mathscr R^\ast$) + « mouvement d'ensemble » ($G$ affecté de la masse $m$).

## 3.4 Torseur dynamique et moment dynamique

On définit la **quantité d'accélération** et le **moment dynamique** :
$$
\vec S_{\mathscr S/\mathscr R}:=\int\vec a_{\mathscr R}(M)\,dm,\qquad \mathsf D^{ij}_{\mathscr S/\mathscr R}(A):=\int\left(r^i_{AM}a^j-r^j_{AM}a^i\right)dm .
$$
Avec $\vec S=m\vec a_{\mathscr R}(G)=\dfrac{d\vec P}{dt}$, et le torseur $\mathscr D(A)=\{\vec S;\mathsf D(A)\}$ (BABAR : $\mathsf D(B)=\mathsf D(A)+\overrightarrow{BA}\wedge\vec S$).

>[!tip]+ **Lien avec $\dot{\mathsf L}$.** $\ \boxed{\mathsf D(A)=\left.\frac{d\mathsf L(A)}{dt}\right)_{\mathscr R}+\vec v_{\mathscr R}(A)\wedge\vec P}$ , soit $\ \mathsf D^{ij}=\dot{\mathsf L}^{ij}+v_A^iP^j-v_A^jP^i$ , et $\ \vec v_{\mathscr R}(A)\wedge\vec P=m\,\vec v_{\mathscr R}(A)\wedge\vec v_{\mathscr R}(G)$.
>
>*Démonstration.* $\dfrac{d}{dt}\left(r^i_{AM}v^j-r^j_{AM}v^i\right)$ avec $\dot r_{AM}^i=v^i-v_A^i$ vaut $(v^i-v^i_A)v^j-(v^j-v^j_A)v^i+r^ia^j-r^ja^i=-(v^i_Av^j-v^j_Av^i)+(r^ia^j-r^ja^i)$. En intégrant : $\dot{\mathsf L}^{ij}=-(v^i_AP^j-v^j_AP^i)+\mathsf D^{ij}$. $\square$
>
>Si $A$ est **fixe**, ou si $A=G$, ou si $\vec v(A)\parallel\vec v(G)$ : $\mathsf D(A)=\dot{\mathsf L}(A)$.

## 3.5 Énergie cinétique, théorème de Koenig

$$
\mathcal E_{c,\mathscr S/\mathscr R}:=\int_{\mathscr S}\tfrac12\,g\!\left(\vec v_{\mathscr R}(M),\vec v_{\mathscr R}(M)\right)dm=\int\tfrac12\,g_{ij}v^iv^j\,dm.
$$
>[!tip]+ **Théorème de Koenig (énergie cinétique).** $\ \boxed{\mathcal E_{c,\mathscr S/\mathscr R}=\mathcal E_{c,\mathscr S/\mathscr R^\ast}+\tfrac12m\,\|\vec v_{\mathscr R}(G)\|^2}$.
>
>*Démonstration.* $\|\vec v\|^2=\|\vec v^\ast\|^2+2\,g(\vec v^\ast,\vec v_G)+\|\vec v_G\|^2$ ; le terme croisé donne $g(\int\vec v^\ast dm,\vec v_G)=g(\vec P_{\mathscr S/\mathscr R^\ast},\vec v_G)=0$ ; le dernier donne $\tfrac12m\|\vec v_G\|^2$. $\square$

# 4. Théorèmes généraux de la dynamique des systèmes fermés

## 4.1 Forces intérieures et extérieures

Pour $M\in\mathscr S$ on décompose la force reçue par l'élément $dm(M)$ :
$$
d\vec F(M)=d\vec F^{\,\mathrm{ext}}(M)+\int_{M'\in\mathscr S}d\vec F_{M'\to M}.
$$
La **3e loi faible** donne $d\vec F_{M'\to M}=-d\vec F_{M\to M'}$ ; la **forme forte** ajoute $\overrightarrow{MM'}\wedge d\vec F_{M'\to M}=0$.

**Résultante et moment des forces** : $\vec F=\int d\vec F$, $\ \mathsf M^{ij}(A)=\int\left(r^i_{AM}dF^j-r^j_{AM}dF^i\right)$ ; torseur $\mathscr A(A)=\{\vec F;\mathsf M(A)\}$ (BABAR : $\mathsf M(B)=\mathsf M(A)+\overrightarrow{BA}\wedge\vec F$).

## 4.2 Théorème de la résultante dynamique (TRD)

>[!tip]+ **TRD.** Dans $\mathscr R$ galiléen, pour un système fermé : $\ \boxed{\left.\frac{d\vec P}{dt}\right)_{\mathscr R}=\vec F^{\,\mathrm{ext}},\qquad m\,\vec a_{\mathscr R}(G)=\vec F^{\,\mathrm{ext}}}$.
>
>*Démonstration.* La 2e loi appliquée à $dm(M)$ s'écrit $\vec a(M)dm=d\vec F^{\,\mathrm{ext}}(M)+\int_{M'}d\vec F_{M'\to M}$. On intègre sur $M$ ; la double intégrale vaut $\tfrac12\iint\left(d\vec F_{M'\to M}+d\vec F_{M\to M'}\right)=\vec 0$ par antisymétrie. D'où $\vec S=\vec F^{\,\mathrm{ext}}$, et $\vec S=m\vec a(G)=d\vec P/dt$. $\square$

*Conséquences.* **Système isolé** : $\vec P$ constante, $G$ en mouvement rectiligne uniforme (retrouve la 1re loi pour $\mathscr S$). Projection : $g(\vec n,\vec P)$ est conservée si $\vec n\cdot\vec F^{\,\mathrm{ext}}=0$.

## 4.3 Théorème du moment dynamique (TMD) et théorèmes du moment cinétique

>[!tip]+ **TMD.** Dans $\mathscr R$ galiléen, pour tout point $A$ : $\ \boxed{\mathsf D_{\mathscr S/\mathscr R}(A)=\mathsf M^{\,\mathrm{ext}}(A)}$, soit $\mathscr D(A)=\mathscr A^{\mathrm{ext}}(A)$.
>
>*Démonstration.* $\mathsf D(A)=\int\overrightarrow{AM}\wedge\left(d\vec F^{\,\mathrm{ext}}+\int_{M'}d\vec F_{M'\to M}\right)=\mathsf M^{\,\mathrm{ext}}(A)+\tfrac12\iint\left(\overrightarrow{AM}\wedge d\vec F_{M'\to M}+\overrightarrow{AM'}\wedge d\vec F_{M\to M'}\right)$. Avec $d\vec F_{M\to M'}=-d\vec F_{M'\to M}$, le crochet vaut $\overrightarrow{M'M}\wedge d\vec F_{M'\to M}$, **nul pour des forces centrales** (3e loi forte). $\square$

>[!warning]- L'antisymétrie seule ne suffit pas pour les moments
>Pour la résultante, la 3e loi faible suffit ; pour le **moment**, il faut la **centralité** des interactions internes (ou une hypothèse équivalente). On verra au §8 que la centralité découle de l'invariance par rotation de l'énergie potentielle interne.

**Théorème du moment cinétique en un point fixe (TMC).** Si $A$ est fixe dans $\mathscr R$ galiléen : $\ \displaystyle\left.\frac{d\mathsf L(A)}{dt}\right)_{\mathscr R}=\mathsf M^{\,\mathrm{ext}}(A)$ (car $\vec v(A)=0$ dans §3.4).

**Théorème du moment cinétique barycentrique (TMC\*).** $\ \displaystyle\boxed{\left.\frac{d\mathsf L^\ast}{dt}\right)_{\mathscr R^\ast}=\mathsf M^{\,\mathrm{ext}}(G)}$, **même si $\mathscr R^\ast$ n'est pas galiléen**.

*Démonstration.* En $A=G$, Koenig donne $\mathsf L_{\mathscr S/\mathscr R}(G)=\mathsf L^\ast$ et §3.4 donne $\mathsf D(G)=\dot{\mathsf L}^\ast+\vec v(G)\wedge m\vec v(G)=\dot{\mathsf L}^\ast$ ; le TMD en $G$ conclut. De façon équivalente : dans $\mathscr R^\ast$ (non galiléen, en translation), chaque élément subit en plus la force d'inertie $-dm\,\vec a_{\mathscr R}(G)$ dont le moment en $G$ est $\left(\int\overrightarrow{GM}dm\right)\wedge(-\vec a_G)=\vec 0$. $\square$

Pour un point $A$ quelconque mais dans $\mathscr R^\ast$ : $\dot{\mathsf L}^\ast=\mathsf M^{\,\mathrm{ext}}(A)+\overrightarrow{AG}\wedge(-m\vec a_{\mathscr R}(G))$ (moment de la force d'inertie d'entraînement).

# 5. Énergie

## 5.1 Théorème de l'énergie cinétique (TEC)

Pour un point : $m\,g_{ij}a^j=F_i$ ; la compatibilité métrique donne $\dfrac{d}{dt}\left(\tfrac12m\,g_{ij}v^iv^j\right)=m\,g_{ij}a^iv^j=F_iv^i$. D'où
$$
\boxed{\frac{d\mathcal E_c}{dt}=\mathscr P(\vec F)=\vec F\cdot\vec v,\qquad \Delta\mathcal E_c=\int_A^BF_i\,dx^i=W_{A\to B}(\vec F).}
$$
Pour un système fermé :
$$
\frac{d\mathcal E_{c,\mathscr S/\mathscr R}}{dt}=\mathscr P^{\,\mathrm{ext}}+\mathscr P^{\,\mathrm{int}},\qquad \mathscr P^{\,\mathrm{int}}=\tfrac12\iint d\vec F_{M'\to M}\cdot\left(\vec v(M)-\vec v(M')\right).
$$
$\mathscr P^{\,\mathrm{int}}$ n'est **pas nulle** en général (système déformable), mais **s'annule pour un solide** (le champ de vitesses est un torseur : $\vec v(M)-\vec v(M')=\Omega(\overrightarrow{M'M})$, et $\overrightarrow{M'M}\cdot\Omega(\cdots)$ avec force centrale donne 0).

Dans un référentiel non galiléen $\mathscr R'$ : $\dfrac{d\mathcal E_{c,\mathscr R'}}{dt}=\mathscr P(\vec F)+\mathscr P(\vec F^{ie})$, car $\mathscr P(\vec F^{ic})=-2m\,g(\vec v',\Omega\vec v')=0$.

## 5.2 Énergie potentielle et théorème de l'énergie mécanique (TEM)

Une force est **conservative** si $F_i=-\partial_iU$ ($F_idx^i=-dU$ est exacte). Alors $\mathcal E_m=\mathcal E_c+U$ vérifie
$$
\boxed{\frac{d\mathcal E_m}{dt}=\mathscr P(\vec F^{\,\mathrm{nc}}),\qquad \Delta\mathcal E_m=W(\vec F^{\,\mathrm{nc}}).}
$$
*Démonstration.* $\dfrac{d\mathcal E_c}{dt}=\left(F^{\mathrm{c}}_i+F^{\mathrm{nc}}_i\right)v^i=-\dfrac{dU}{dt}+F^{\mathrm{nc}}_iv^i$ si $U$ ne dépend pas explicitement de $t$. $\square$ (Si $\partial_tU\ne0$ : $\dot{\mathcal E}_m=\mathscr P^{\mathrm{nc}}+\partial_tU$.)

## 5.3 Théorème du viriel en dimension $n$

Soit $\mathscr G:=\sum_a g(\vec p_a,\vec r_a)=\sum_am_a\,g(\vec v_a,\vec r_a)$ (« viriel de Clausius » avant moyenne). Pour des positions prises depuis $O$ :
$$
\frac{d\mathscr G}{dt}=\sum_am_a\|\vec v_a\|^2+\sum_a\vec F_a\cdot\vec r_a=2\mathcal E_c+\sum_a\vec F_a\cdot\vec r_a .
$$
Si le mouvement est **borné** (positions et vitesses bornées), la moyenne temporelle $\langle\dot{\mathscr G}\rangle=\lim\frac{\mathscr G(T)-\mathscr G(0)}{T}=0$ : $\ \boxed{2\langle\mathcal E_c\rangle=-\Big\langle\sum_a\vec F_a\cdot\vec r_a\Big\rangle}$.
Pour une énergie potentielle **homogène de degré $k$** (champ central $U=\alpha r^k$, $\vec F\cdot\vec r=-kU$ par Euler) : $\ 2\langle\mathcal E_c\rangle=k\langle U\rangle$. Exemples : oscillateur ($k=2$) : $\langle\mathcal E_c\rangle=\langle U\rangle$ ; potentiel coulombien ou gravitationnel en $r^{-1}$ ($k=-1$) : $2\langle\mathcal E_c\rangle=-\langle U\rangle$, $\langle\mathcal E_m\rangle=-\langle\mathcal E_c\rangle$ ; potentiel de Green en dimension $n$ (force $\propto r^{1-n}$, $U\propto r^{2-n}$) : $2\langle\mathcal E_c\rangle=(2-n)\langle U\rangle$.

# 6. Formalisme lagrangien

## 6.1 Espace des configurations et métrique cinétique

Un système de $N$ points $(M_a,m_a)$ dans $\mathscr E$ a pour **configuration** $x=(\vec r_1,\dots,\vec r_N)\in\mathscr E^N$ ; avec des liaisons holonomes il vit sur une sous-variété $Q$ de dimension $\ell$ (nombre de degrés de liberté) de coordonnées $q^\alpha$, $\alpha=1,\dots,\ell$ : $\vec r_a=\vec r_a(q,t)$. L'énergie cinétique est
$$
T=\tfrac12\sum_am_a\,g(\vec v_a,\vec v_a)=\tfrac12\,m_{\alpha\beta}(q)\,\dot q^\alpha\dot q^\beta,\qquad m_{\alpha\beta}=\sum_am_a\,g_{ij}\frac{\partial r_a^i}{\partial q^\alpha}\frac{\partial r_a^j}{\partial q^\beta}
$$
(on suppose les liaisons indépendantes du temps ; sinon $T=T_2+T_1+T_0$). $m_{\alpha\beta}$ est la **métrique cinétique** (riemannienne) sur $Q$, d'inverse $m^{\alpha\beta}$. Les coordonnées $q^\alpha$ et les vitesses $\dot q^\alpha$ sont traitées comme **indépendantes**.

## 6.2 Principe de moindre action et équations d'Euler–Lagrange

**Lagrangien** $L(q,\dot q,t)=T-V$, **action** $S[q]=\int_{t_1}^{t_2}L\,dt$. Le mouvement réel rend $S$ stationnaire pour les variations $\delta q^\alpha$ à extrémités fixées, $\delta q(t_1)=\delta q(t_2)=0$ :
$$
0=\delta S=\int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q^\alpha}\delta q^\alpha+\frac{\partial L}{\partial\dot q^\alpha}\delta\dot q^\alpha\right)dt=\underbrace{\left[\frac{\partial L}{\partial\dot q^\alpha}\delta q^\alpha\right]_{t_1}^{t_2}}_{=0}+\int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q^\alpha}-\frac{d}{dt}\frac{\partial L}{\partial\dot q^\alpha}\right)\delta q^\alpha\,dt,
$$
en intégrant par parties avec $\delta\dot q=\frac{d}{dt}\delta q$. Les $\delta q^\alpha$ étant arbitraires :
$$
\boxed{\frac{d}{dt}\frac{\partial L}{\partial\dot q^\alpha}-\frac{\partial L}{\partial q^\alpha}=0,\qquad\alpha=1,\dots,\ell.}
$$
Le **moment conjugué** est $p_\alpha:=\partial L/\partial\dot q^\alpha$ (**covariant**) ; ici $p_\alpha=m_{\alpha\beta}\dot q^\beta$.

>[!tip]+ **Équivalence avec le PFD (démonstration).** Avec $L=\tfrac12m_{\alpha\beta}\dot q^\alpha\dot q^\beta-V(q)$ :
>$$
>\frac{d}{dt}\left(m_{\alpha\beta}\dot q^\beta\right)=m_{\alpha\beta}\ddot q^\beta+\partial_\gamma m_{\alpha\beta}\,\dot q^\gamma\dot q^\beta,\qquad\frac{\partial L}{\partial q^\alpha}=\tfrac12\partial_\alpha m_{\beta\gamma}\dot q^\beta\dot q^\gamma-\partial_\alpha V .
>$$
>En symétrisant $\partial_\gamma m_{\alpha\beta}\dot q^\gamma\dot q^\beta=\tfrac12\left(\partial_\gamma m_{\alpha\beta}+\partial_\beta m_{\alpha\gamma}\right)\dot q^\beta\dot q^\gamma$, l'équation devient
>$$
>m_{\alpha\beta}\left(\ddot q^\beta+\Gamma^\beta{}_{\gamma\delta}\dot q^\gamma\dot q^\delta\right)=-\partial_\alpha V,\quad\text{i.e.}\quad m_{\alpha\beta}\,a^\beta=Q_\alpha ,
>$$
>avec $\Gamma$ les symboles de Christoffel de $m_{\alpha\beta}$ et $Q_\alpha=-\partial_\alpha V$ la **force généralisée** : c'est le **PFD sur $Q$**, covariant. Sans force : équation des géodésiques de $m_{\alpha\beta}$ (1re loi). Dans les coordonnées cartésiennes d'un point, $m_{ij}=m\,g_{ij}$ et $m\,\ddot x_i=-\partial_iV$.

**Forces non conservatives.** Les équations deviennent $\frac{d}{dt}\partial_{\dot q^\alpha}L-\partial_{q^\alpha}L=Q^{\mathrm{nc}}_\alpha$ avec $Q^{\mathrm{nc}}_\alpha=\vec F^{\mathrm{nc}}\cdot\partial\vec r/\partial q^\alpha$ (principe de d'Alembert).

**Liberté de jauge.** $L\to L'=L+\dfrac{d\phi}{dt}(q,t)$ change $S$ de $\phi|_{t_2}-\phi|_{t_1}$ (terme de bord fixé) : mêmes équations du mouvement (transformation de jauge).

>[!example]- Particule chargée dans un champ électromagnétique ($n$ quelconque)
>$L=\tfrac12m\,g_{ij}v^iv^j-q\varphi+qA_iv^i$. Alors $p_i=m v_i+qA_i$ et l'équation d'Euler–Lagrange donne
>$$
>m\,a_i=q\left(E_i+F_{ij}v^j\right),\qquad E_i=-\partial_i\varphi-\partial_tA_i,\quad F_{ij}=\partial_iA_j-\partial_jA_i ,
>$$
>(force de Lorentz). En dimension 3, $F_{ij}v^j=(\vec v\times\vec B)_i$ avec $B^k=\tfrac12\varepsilon^{kij}F_{ij}$ : le champ magnétique est en réalité la **2-forme** $F=dA$.
>
>*Preuve.* $\frac{d}{dt}(mv_i+qA_i)=ma_i+q(\partial_tA_i+v^j\partial_jA_i)$ et $\frac{\partial L}{\partial x^i}=-q\partial_i\varphi+qv^j\partial_iA_j$ ; d'où $ma_i=-q\partial_i\varphi-q\partial_tA_i+qv^j(\partial_iA_j-\partial_jA_i)$.

## 6.3 Dérivée de $H$ et théorème de l'énergie

Définissons l'**énergie** (fonction de Jacobi) $H:=p_\alpha\dot q^\alpha-L$. Sur les solutions des équations d'Euler–Lagrange :
$$
\frac{dH}{dt}=\dot p_\alpha\dot q^\alpha+p_\alpha\ddot q^\alpha-\frac{\partial L}{\partial q^\alpha}\dot q^\alpha-\frac{\partial L}{\partial\dot q^\alpha}\ddot q^\alpha-\frac{\partial L}{\partial t}=-\frac{\partial L}{\partial t}.
$$
Pour $L=T-V$ (liaisons indépendantes du temps), $H=2T-(T-V)=T+V=\mathcal E_m$ : $\ \boxed{\dot{\mathcal E}_m=-\partial_tL=\partial_tV}$ : l'énergie est conservée si $L$ ne dépend pas explicitement du temps.

# 7. Formalisme hamiltonien et théorème de Liouville

## 7.1 Transformée de Legendre

Si la métrique cinétique est non dégénérée (Hessienne $\partial^2L/\partial\dot q\partial\dot q=m_{\alpha\beta}$ inversible), on peut inverser $p_\alpha=\partial L/\partial\dot q^\alpha$ en $\dot q^\alpha=m^{\alpha\beta}p_\beta$, et on définit
$$
\boxed{H(q,p,t)=p_\alpha\dot q^\alpha-L=\tfrac12m^{\alpha\beta}(q)\,p_\alpha p_\beta+V(q,t).}
$$
Dans le cas électromagnétique : $H=\dfrac{1}{2m}g^{ij}(p_i-qA_i)(p_j-qA_j)+q\varphi$.

**Équations de Hamilton.** Différentions $H$ :
$dH=\dot q^\alpha dp_\alpha+p_\alpha d\dot q^\alpha-\dfrac{\partial L}{\partial q^\alpha}dq^\alpha-p_\alpha d\dot q^\alpha-\dfrac{\partial L}{\partial t}dt=\dot q^\alpha dp_\alpha-\dot p_\alpha dq^\alpha-\dfrac{\partial L}{\partial t}dt$ (EL : $\partial L/\partial q^\alpha=\dot p_\alpha$). Par identification :
$$
\boxed{\dot q^\alpha=\frac{\partial H}{\partial p_\alpha},\qquad \dot p_\alpha=-\frac{\partial H}{\partial q^\alpha},\qquad \frac{\partial H}{\partial t}=-\frac{\partial L}{\partial t}.}
$$
L'**espace des phases** $\Gamma=T^\ast Q$ (dimension $2\ell$, coordonnées $z=(q,p)$) porte la 2-forme symplectique $\omega=dq^\alpha\wedge dp_\alpha$. En notant $J=\begin{pmatrix}0&\mathbb 1\\-\mathbb 1&0\end{pmatrix}$ : $\ \dot z=J\,\nabla_zH$.

## 7.2 Crochets de Poisson

$$
\{f,g\}:=\frac{\partial f}{\partial q^\alpha}\frac{\partial g}{\partial p_\alpha}-\frac{\partial f}{\partial p_\alpha}\frac{\partial g}{\partial q^\alpha},\qquad\boxed{\frac{df}{dt}=\{f,H\}+\frac{\partial f}{\partial t}}
$$
(antisymétrique, bilinéaire, règle de Leibniz, **identité de Jacobi** $\{f,\{g,h\}\}+\text{perm. cycl.}=0$). On a $\{q^\alpha,p_\beta\}=\delta^\alpha{}_\beta$. **Théorème de Poisson** : si $f$ et $g$ sont des intégrales premières, $\{f,g\}$ en est une (Jacobi). Exemple d'algèbre de Lie : pour $\mathsf L^{ij}=x^ip^j-x^jp^i$ (coordonnées cartésiennes orthonormées)
$$
\{\mathsf L^{ij},\mathsf L^{kl}\}=g^{ik}\mathsf L^{jl}-g^{il}\mathsf L^{jk}-g^{jk}\mathsf L^{il}+g^{jl}\mathsf L^{ik}\qquad(\text{algèbre }\mathfrak{so}(n)),
$$
qui redonne $\{L_x,L_y\}=L_z$ en dimension 3.

## 7.3 Théorème de Liouville

>[!tip]+ **Théorème de Liouville.** Le flot hamiltonien $\Phi_t:\Gamma\to\Gamma$ **conserve le volume** de l'espace des phases : $\ \mathrm{Vol}(\Phi_t(D))=\mathrm{Vol}(D)$ pour tout domaine $D$ (mesure $d^\ell q\,d^\ell p$). En fait $\Phi_t$ est **symplectique** : $\Phi_t^\ast\omega=\omega$.
>
>*Démonstration (divergence).* Le champ de phase $X_H=(\partial H/\partial p_\alpha,-\partial H/\partial q^\alpha)$ vérifie
>$$
>\operatorname{div}X_H=\frac{\partial}{\partial q^\alpha}\frac{\partial H}{\partial p_\alpha}-\frac{\partial}{\partial p_\alpha}\frac{\partial H}{\partial q^\alpha}=0\quad\text{(théorème de Schwarz).}
>$$
>Pour $\mathcal J(t)=\det\left(\partial\Phi_t(z_0)/\partial z_0\right)$, on a $\dot{\mathcal J}=(\operatorname{div}X_H)\circ\Phi_t\;\mathcal J=0$ et $\mathcal J(0)=1$, donc $\mathcal J\equiv1$.
>
>*Démonstration (symplectique).* La matrice jacobienne $M_t=\partial\Phi_t/\partial z_0$ vérifie $\dot M=J\,S\,M$ avec $S=\mathrm{Hess}\,H$ symétrique. Alors, avec $J^T=-J$, $J^TJ=\mathbb 1$, $J^2=-\mathbb 1$ :
>$$
>\frac{d}{dt}\left(M^TJM\right)=M^TS J^T J M+M^T J J SM=M^TSM-M^TSM=0 ,
>$$
>donc $M_t^TJM_t=J$ ; et $\det M_t=\pm1$, $=+1$ par continuité. $\square$

**Équation de Liouville.** Pour une densité de probabilité $\rho(z,t)$ sur $\Gamma$ transportée par le flot : $\ \partial_t\rho+\operatorname{div}(\rho X_H)=0\iff\boxed{\partial_t\rho+\{\rho,H\}=0\iff\dfrac{d\rho}{dt}\Big)_{\text{le long du flot}}=0}$ : le fluide des points de phase est **incompressible**. Un état d'équilibre est $\rho=\rho(H)$ (par exemple microcanonique ou canonique). Conséquence : **récurrence de Poincaré** (flot conservant un volume fini). *Invariance par transformation ponctuelle* : si $Q^{\alpha}=Q^{\alpha}(q)$, alors $P_\alpha=\frac{\partial q^\beta}{\partial Q^\alpha}p_\beta$ et la matrice jacobienne est triangulaire par blocs de déterminant $1$ ; la mesure $d^\ell q\,d^\ell p$ est donc intrinsèque (mais attention à la mesure $\sqrt{m}\,d^\ell q$ sur $Q$ seul).

>[!tip]- Intégrabilité de Liouville–Arnold (pour mémoire)
>Si un système à $\ell$ degrés de liberté possède $\ell$ intégrales premières $f_1=H,\dots,f_\ell$ indépendantes et en involution ($\{f_i,f_j\}=0$), alors les niveaux compacts et connexes sont des **tores** $T^\ell$ et il existe des variables angle-action $(\theta,I)$ avec $H=H(I)$, $\dot\theta=\partial H/\partial I$, $\dot I=0$.

# 8. Théorème de Noether en mécanique

## 8.1 Énoncé et démonstration

**Famille de transformations.** On considère une famille à un paramètre $q^\alpha\to q^\alpha_\sigma(t)$, $\sigma\in\mathbb R$, avec $q_{\sigma=0}=q$ et la **variation infinitésimale** $\delta q^\alpha:=\left.\partial_\sigma q^\alpha_\sigma\right|_{\sigma=0}=\zeta^\alpha(q,t)$ (on la prend « verticale », à $t$ fixé).

>[!tip]+ **Théorème de Noether (version verticale).** Soit $\delta L:=\dfrac{\partial L}{\partial q^\alpha}\zeta^\alpha+\dfrac{\partial L}{\partial\dot q^\alpha}\dot\zeta^\alpha$ la variation de $L$.
>
>**(i) Identité de Noether.** Sur toute solution des équations d'Euler–Lagrange,
>$$
>\boxed{\frac{d}{dt}\left(p_\alpha\zeta^\alpha\right)=\delta L .}
>$$
>**(ii) Théorème.** Si $\delta L=\dfrac{dK}{dt}$ (symétrie « à une jauge $K(q,t)$ près »), alors $\ \boxed{\mathscr Q:=p_\alpha\zeta^\alpha-K}$ est une **intégrale première**. Si $\delta L=0$, $\mathscr Q=p_\alpha\zeta^\alpha$.
>
>*Démonstration.* Avec EL, $\partial L/\partial q^\alpha=\dot p_\alpha$, donc $\delta L=\dot p_\alpha\zeta^\alpha+p_\alpha\dot\zeta^\alpha=\dfrac{d}{dt}(p_\alpha\zeta^\alpha)$. $\square$

**(iii) Version temporelle.** Si $\partial_tL=0$ (invariance par translation $t\to t+\sigma$), $H$ est conservée (§6.3). C'est le cas $\delta t=\sigma$, $\delta q=0$ du formalisme étendu : en posant $\xi^0=t$ et un paramètre d'évolution $\lambda$, avec $L^{(e)}=\xi^{0\prime}L\!\left(\xi,\frac{\xi'}{\xi^{0\prime}}\right)$ [^5], la grandeur conservée $\partial L^{(e)}/\partial\xi^{0\prime}=L-\dot q^\alpha\partial L/\partial\dot q^\alpha=-H$ est l'opposée de l'énergie ; le signe est une convention.

>[!tip]- Lien avec le formalisme hamiltonien
>$\mathscr Q=p_\alpha\zeta^\alpha$ **engendre** la transformation par crochet de Poisson : $\ \delta q^\alpha=\{q^\alpha,\mathscr Q\}=\partial\mathscr Q/\partial p_\alpha=\zeta^\alpha$. $\ \mathscr Q$ est conservé $\iff\{\mathscr Q,H\}=0$ ; l'algèbre des symétries est l'algèbre de Lie des charges conservées (Poisson).

## 8.2 Un système de $N$ points : Lagrangien général

$$
L=\sum_a\tfrac12m_a\,g_{ij}v_a^iv_a^j-U^{\mathrm{int}}\!\left(\{\|\vec r_a-\vec r_b\|\}\right)-U^{\mathrm{ext}}(\vec r_1,\dots,\vec r_N,t).
$$
L'énergie interne est supposée fonction des **distances mutuelles** : elle est invariante par le groupe euclidien. Ses forces sont $\vec F_{b\to a}=-\partial_{\vec r_a}U^{\mathrm{int}}$ ; on déduit de l'invariance par translations que $\sum_a\vec F^{\mathrm{int}}_a=\vec 0$ (3e loi faible) et par rotation que les forces internes sont **centrales** (3e loi forte), voir 8.3, 8.4.

## 8.3 Invariance par translation $\Rightarrow$ TRD

$\zeta_a^i=n^i$ (même vecteur $\vec n$ pour tous les points). Alors $\delta L=-n^i\sum_a\partial_{a,i}U^{\mathrm{ext}}=\vec n\cdot\vec F^{\mathrm{ext}}$ (l'énergie cinétique et $U^{\mathrm{int}}$ sont invariantes). La charge est $\mathscr Q=\sum_ap_{a,i}n^i=g(\vec n,\vec P)$ et l'identité de Noether donne
$$
\frac{d}{dt}g(\vec n,\vec P)=g(\vec n,\vec F^{\mathrm{ext}})\quad\forall\vec n\ \Longrightarrow\ \boxed{\frac{d\vec P}{dt}=\vec F^{\mathrm{ext}}}\quad(\mathrm{TRD}).
$$
Si $U^{\mathrm{ext}}$ est aussi invariant dans la direction $\vec n$ : $g(\vec n,\vec P)$ conservée (**impulsion**) ; système isolé : $\vec P$ conservée, c'est la 1re loi pour $\mathscr S$. L'invariance de $U^{\mathrm{int}}$ par translation donne $\sum_a\vec F^{\mathrm{int}}_a=0$ : **3e loi faible**.

## 8.4 Invariance par rotation $\Rightarrow$ TMC, centralité des forces

$\zeta_a^i=\Omega^i{}_jx_a^j$, $\Omega\in\mathfrak{so}(V,g)$ quelconque. L'énergie cinétique est invariante ($g(\Omega\vec v,\vec v)=0$). La charge est
$$
\mathscr Q=\sum_ap_{a,i}\Omega^i{}_jx^j_a=\Omega_{ij}\sum_ap^ix^j=-\tfrac12\Omega_{ij}\mathsf L^{ij},\qquad\mathsf L^{ij}=\sum_a\left(x_a^ip_a^j-x_a^jp_a^i\right).
$$
Variation externe : $\delta L=\sum_aF^{\mathrm{ext}}_{a,i}\Omega^i{}_jx_a^j=-\tfrac12\Omega_{ij}\mathsf M^{ij}_{\mathrm{ext}}$. L'identité de Noether, valable $\forall\Omega$ antisymétrique, donne
$$
\boxed{\frac{d\mathsf L^{ij}}{dt}=\mathsf M^{ij}_{\mathrm{ext}}}\quad(\mathrm{TMC})\ ;\qquad \text{si le système est invariant par rotation : }\mathsf L^{ij}\text{ conservés ($\tfrac{n(n-1)}{2}$ charges).}
$$
En dimension 3 : $\vec L$ conservé (3 composantes) $\iff$ symétrie $SO(3)$. *Pour un seul point* ($U=U(\vec r)$ invariant par $SO(n)$) : $U=U(\|\vec r\|)$, force **radiale** (centrale), obtenue **sans** invoquer le PFD [^5]. De même l'invariance de $U^{\mathrm{int}}$ par rotation implique $\partial U^{\mathrm{int}}/\partial\vec r_a$ combinaison de $\vec r_a-\vec r_b$ : forces internes centrales (3e loi forte).

## 8.5 Invariance par translation dans le temps $\Rightarrow$ TEM, TEC

Si $\partial_tL=0$, $H=\sum_a\tfrac12m_a\|\vec v_a\|^2+U=\mathcal E_m$ est conservée. Si $U=U(x,t)$ dépend de $t$ : $\dot H=-\partial_tL=\partial_tU$. Pour des forces non conservatives, l'identité $q^\alpha_{\ \cdot}\,\mathrm{EL}_\alpha=0$ donne $\dot T=Q_\alpha\dot q^\alpha$ : c'est le **TEC** :
$$
\frac{dT}{dt}=\sum_a\vec F_a\cdot\vec v_a\quad\text{(contracter EL avec }\dot q^\alpha\text{ : }\dot q^\alpha\left(\tfrac{d}{dt}\partial_{\dot q^\alpha}L-\partial_{q^\alpha}L\right)=\dot T+\dot V-\partial_tV-\dot q^\alpha Q_\alpha^{nc}\ ),
$$
et la combinaison $\dot{\mathcal E}_m=\mathscr P^{\mathrm{nc}}+\partial_tV$ est le **TEM**.

## 8.6 Boost galiléen $\Rightarrow$ mouvement uniforme du centre d'inertie

$\zeta_a^i=t\,n^i$ (changement de vitesse $\vec n$). Alors $\delta L=\sum_am_a\,g(\vec n,\vec v_a)=\dfrac{d}{dt}\left(m\,g(\vec n,\overrightarrow{OG})\right)=:\dfrac{dK}{dt}$ (pour un système isolé). La charge est
$$
\mathscr Q=\sum_ap_{a,i}\,t\,n^i-K=g\!\left(\vec n,\ t\vec P-m\overrightarrow{OG}\right)\ \Longrightarrow\ m\overrightarrow{OG}-t\vec P=\overrightarrow{\text{cste}}\ ,
$$
d'où $\overrightarrow{OG}=\overrightarrow{OG_0}+\dfrac{\vec P}{m}t$ : on retrouve **la 1re loi de Newton** à partir de l'invariance galiléenne.

## 8.7 Problème de Kepler : la symétrie cachée $SO(n+1)$ [^5]

Pour $U=-k/r$ (force $-k\,\vec r/r^3$), outre $\mathscr E=\mathcal E_m$ et $\mathsf L^{ij}$, le **vecteur de Runge–Lenz–Laplace** (ou *excentricité*)
$$
A^i=\mathsf L^{ij}p_j-mk\,\frac{x^i}{r}\qquad\left(\text{en dimension 3 : }\vec A=\vec p\times\vec L-mk\,\hat r\right)
$$
est conservé : en effet $\dot{\mathsf L}=0$, $\dot p_j=-kx_j/r^3$, $\dot r=\vec x\cdot\vec p/(mr)$ donnent $\dot A^i=-\frac{k}{r^3}\left(x^i(\vec x\cdot\vec p)-r^2p^i\right)-\frac{k}{r}p^i+\frac{k\,x^i(\vec x\cdot\vec p)}{r^3}=0$. Il engendre une symétrie **non ponctuelle** (dans l'espace des vitesses) de Noether. Pour $E<0$ les $\mathsf L^{ij}$ et $A^i/\sqrt{-2mE}$ forment l'algèbre $\mathfrak{so}(n+1)$ (en dimension 3 : $\mathfrak{so}(4)$ ; résultat de Moser [^5] : l'hodographe est la projection stéréographique de la sphère $S^n$). En dimension 3, $\vec A\cdot\vec L=0$ (orbite plane) et $\|\vec A\|=mk\,e$ (excentricité).

## 8.8 Tableau récapitulatif des invariances et grandeurs conservées

| Symétrie du lagrangien | Générateur $\zeta$ | Grandeur conservée (ou loi de bilan si non invariant) |
| --- | --- | --- |
| Translation d'espace | $\zeta^i=n^i$ | $g(\vec n,\vec P)$ ; sinon TRD |
| Rotation $SO(n,g)$ | $\zeta^i=\Omega^i{}_jx^j$ | $\mathsf L^{ij}$ ; sinon TMC |
| Translation de temps | $t\to t+\sigma$ | $H=\mathcal E_m$ ; sinon TEM, TEC |
| Boost galiléen | $\zeta^i=tn^i$ | $m\overrightarrow{OG}-t\vec P$ (1re loi) |
| Jauge globale $U(1)$ (champ complexe) | $\delta\psi=i\sigma\psi$ | $\int\lvert\psi\rvert^2$ (charge, probabilité) |
| Dilatation (potentiel $\propto r^{-2}$) | $\zeta=x$, $t\to\lambda^2t$ | $D=\vec x\cdot\vec p-2tH$ |
| Kepler ($-k/r$) | non ponctuelle | $\vec A$ (RLL) |

# 9. Noether pour les champs : Schrödinger, électrodynamique quantique

## 9.1 Noether pour un champ

Soient des champs $\phi_A(x^\mu)$, $\mu=0,\dots,n$ ($x^0=t$), de **densité lagrangienne** $\mathscr L(\phi,\partial_\mu\phi,x)$, $S=\int\mathscr L\,\sqrt{g}\,d^nx\,dt$. L'équation d'Euler–Lagrange de champ est
$$
\partial_\mu\left(\frac{\partial\mathscr L}{\partial(\partial_\mu\phi_A)}\right)=\frac{\partial\mathscr L}{\partial\phi_A}.
$$
>[!tip]+ **Théorème de Noether (champs).** Si $\phi_A\to\phi_A+\sigma\,\delta\phi_A$ laisse $\mathscr L$ invariant à une divergence près, $\delta\mathscr L=\partial_\mu K^\mu$, alors le **courant de Noether**
>$$
>J^\mu=\frac{\partial\mathscr L}{\partial(\partial_\mu\phi_A)}\,\delta\phi_A-K^\mu\quad\text{vérifie}\quad\partial_\mu J^\mu=0\ \ (\text{sur les solutions}),
>$$
>et si les champs décroissent à l'infini, la **charge** $\mathscr Q=\int J^0\,d^nx$ est conservée.
>
>*Démonstration.* $\delta\mathscr L=\frac{\partial\mathscr L}{\partial\phi_A}\delta\phi_A+\frac{\partial\mathscr L}{\partial(\partial_\mu\phi_A)}\partial_\mu\delta\phi_A=\partial_\mu\left(\frac{\partial\mathscr L}{\partial(\partial_\mu\phi_A)}\delta\phi_A\right)$ (EL), qu'on égale à $\partial_\mu K^\mu$. $\square$

*Tenseur énergie-impulsion.* Pour les translations d'espace-temps $x^\nu\to x^\nu+\sigma a^\nu$, $\delta\phi=-a^\nu\partial_\nu\phi$ et $K^\mu=-a^\mu\mathscr L$ : $\ T^\mu{}_\nu=\dfrac{\partial\mathscr L}{\partial(\partial_\mu\phi_A)}\partial_\nu\phi_A-\delta^\mu_\nu\mathscr L$, $\partial_\mu T^\mu{}_\nu=0$ ($\nu=0$ : énergie ; $\nu=i$ : impulsion).

## 9.2 Équation de Schrödinger

Sur $(\mathscr E,g)$ de dimension $n$, avec $\psi$ complexe, $\psi^\ast$ son conjugué (traités comme champs indépendants) :
$$
\mathscr L=\sqrt{g}\left[\frac{i\hbar}{2}\left(\psi^\ast\dot\psi-\dot\psi^\ast\psi\right)-\frac{\hbar^2}{2m}g^{ij}\partial_i\psi^\ast\partial_j\psi-V\psi^\ast\psi\right].
$$
(Elle diffère de $i\hbar\psi^\ast\dot\psi-\cdots$ par une jauge $\tfrac{i\hbar}{2}\partial_t(\psi^\ast\psi)$.) **EL pour $\phi=\psi^\ast$** : $\ \partial_t\frac{\partial\mathscr L}{\partial\dot\psi^\ast}+\partial_i\frac{\partial\mathscr L}{\partial(\partial_i\psi^\ast)}=\frac{\partial\mathscr L}{\partial\psi^\ast}$, avec $\frac{\partial\mathscr L}{\partial\dot\psi^\ast}=-\frac{i\hbar}{2}\sqrt g\,\psi$, $\frac{\partial\mathscr L}{\partial(\partial_i\psi^\ast)}=-\frac{\hbar^2}{2m}\sqrt g\,g^{ij}\partial_j\psi$, $\frac{\partial\mathscr L}{\partial\psi^\ast}=\sqrt g\left(\frac{i\hbar}{2}\dot\psi-V\psi\right)$ :
$$
-\frac{i\hbar}{2}\sqrt g\,\dot\psi-\frac{\hbar^2}{2m}\partial_i\!\left(\sqrt g\,g^{ij}\partial_j\psi\right)=\sqrt g\left(\frac{i\hbar}{2}\dot\psi-V\psi\right)\ \Longrightarrow\ \boxed{i\hbar\,\partial_t\psi=-\frac{\hbar^2}{2m}\Delta_g\psi+V\psi}
$$
avec le **laplacien de Laplace–Beltrami** $\Delta_g\psi=\frac{1}{\sqrt g}\partial_i(\sqrt g\,g^{ij}\partial_j\psi)$. (EL pour $\psi$ donne l'équation conjuguée.)

**Symétrie $U(1)$ et charge.** $\psi\to e^{i\sigma}\psi$, $\psi^\ast\to e^{-i\sigma}\psi^\ast$ : $\delta\psi=i\psi$, $\delta\psi^\ast=-i\psi^\ast$, $\delta\mathscr L=0$. Le courant de Noether est
$$
J^0=\frac{\partial\mathscr L}{\partial\dot\psi}\delta\psi+\frac{\partial\mathscr L}{\partial\dot\psi^\ast}\delta\psi^\ast=-\hbar\sqrt g\,|\psi|^2,\qquad J^i=-\hbar\sqrt g\ \frac{\hbar}{2im}\,g^{ij}\left(\psi^\ast\partial_j\psi-\psi\partial_j\psi^\ast\right).
$$
En posant $\rho=|\psi|^2$ et $j^i=\frac{\hbar}{2im}g^{ij}(\psi^\ast\partial_j\psi-\psi\partial_j\psi^\ast)$, $\partial_\mu J^\mu=0$ devient l'**équation de continuité**
$$
\partial_t(\sqrt g\,\rho)+\partial_i(\sqrt g\,j^i)=0,\qquad\frac{d}{dt}\int|\psi|^2\sqrt g\,d^nx=0,
$$
qui fonde l'interprétation probabiliste (et la conservation de la norme). *Sens physique :* $\int|\psi|^2$ constante $\iff$ évolution **unitaire**.

## 9.3 Invariance de jauge locale et couplage électromagnétique

Si l'on exige l'invariance sous $\psi\to e^{iq\chi(x,t)/\hbar}\psi$ avec $\chi$ **dépendant du point**, on remplace les dérivées par des **dérivées covariantes de jauge**
$$
D_t=\partial_t+\frac{iq}{\hbar}\varphi,\qquad D_i=\partial_i-\frac{iq}{\hbar}A_i,\qquad A_i\to A_i+\partial_i\chi,\quad\varphi\to\varphi-\partial_t\chi,
$$
(on vérifie $D\psi\to e^{iq\chi/\hbar}D\psi$). L'équation devient $i\hbar D_t\psi=-\frac{\hbar^2}{2m}g^{ij}D_iD_j\psi\ (+\text{terme de connexion})$, soit
$$
i\hbar\,\partial_t\psi=\frac{1}{2m}\left(-i\hbar\nabla-q\vec A\right)^2\psi+q\varphi\,\psi\qquad(\text{Pauli–Schrödinger sans spin}).
$$
Le champ de jauge a pour courbure $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ et, en ajoutant $-\tfrac14F_{\mu\nu}F^{\mu\nu}$ (unités $\mu_0=1$), l'équation d'Euler–Lagrange en $A_\nu$ donne $\ \partial_\mu F^{\mu\nu}=j^\nu$, **compatible** avec $\partial_\nu j^\nu=0$ car $\partial_\nu\partial_\mu F^{\mu\nu}=0$ (identité de Noether du 2e type).

**Notations de l'électrodynamique quantique** ($\hbar=c=1$, signature $(+,-,\dots)$) : champ de Dirac $\psi$, $\bar\psi=\psi^\dagger\gamma^0$, $D_\mu=\partial_\mu+ieA_\mu$,
$$
\mathscr L_{\mathrm{QED}}=\bar\psi\left(i\gamma^\mu D_\mu-m\right)\psi-\tfrac14F_{\mu\nu}F^{\mu\nu},\qquad J^\mu_{U(1)}=\bar\psi\gamma^\mu\psi,\quad\partial_\mu J^\mu=0,
$$
$\partial_\mu F^{\mu\nu}=e\,\bar\psi\gamma^\nu\psi$. Le groupe de jauge est $U(1)$, la charge de Noether est la **charge électrique** (nombre de fermions moins antifermions), et l'invariance de Lorentz donne les 10 charges d'énergie-impulsion et de moment angulaire. Cas scalaire (Klein–Gordon complexe) : $\mathscr L=\partial_\mu\phi^\ast\partial^\mu\phi-m^2\phi^\ast\phi$, $J^\mu=i(\phi^\ast\partial^\mu\phi-\phi\partial^\mu\phi^\ast)$.

# 10. Du système fermé au solide indéformable

## 10.1 Cinématique du solide : formule de Varignon

Un **solide** $\mathscr S$ est un système dont les distances mutuelles sont constantes : $\|\overrightarrow{MN}\|=\text{cste}$ pour tout couple de points. On lui attache un référentiel $\mathscr R_{\mathscr S}=(A;\vec e_{i'}(t))$ **indéformable** (si $\mathscr S$ contient $n+1$ points affinement indépendants). Alors, dans $\mathscr R_{\mathscr S}$, $\ \vec v_{\mathscr R_{\mathscr S}}(M)=\vec 0$ pour tout $M\in\mathscr S$, et §1.4 donne :
$$
\boxed{\vec v_{\mathscr S/\mathscr R}(B)=\vec v_{\mathscr S/\mathscr R}(A)+\Omega_{\mathscr S/\mathscr R}(\overrightarrow{AB})=\vec v_{\mathscr S/\mathscr R}(A)-\Omega_{\mathscr S/\mathscr R}(\overrightarrow{BA}),}\qquad \Omega_{\mathscr S/\mathscr R}\in\mathfrak{so}(V,g).
$$
En dimension 3, $\vec v(B)=\vec v(A)+\vec\omega\times\overrightarrow{AB}$, soit $\vec v(B)=\vec v(A)+\overrightarrow{BA}\wedge\vec\omega$ (« **BABAR** »). Le champ des vitesses est donc **entièrement déterminé** par $(\vec v(A),\Omega)$ : un solide a au plus
$$
n+\frac{n(n-1)}{2}=\frac{n(n+1)}{2}\ \text{degrés de liberté}\quad(6\text{ en dim. 3, }3\text{ en dim. 2}),
$$
égal à la dimension du groupe euclidien $SE(n)=\mathbb R^n\rtimes SO(n)$. Ce champ vérifie aussi la relation de **rigidité** $g\!\left(\vec v(B)-\vec v(A),\overrightarrow{AB}\right)=0$ (équiprojectivité), conséquence de $\Omega_{ij}=-\Omega_{ji}$. Le **centre instantané de rotation** (point de vitesse nulle) existe en dimension 2 si $\Omega\ne0$.

**Accélération d'un solide.** $\vec a(B)=\vec a(A)+\dot\Omega(\overrightarrow{AB})+\Omega^2(\overrightarrow{AB})$ (ce n'est **pas** un torseur).

## 10.2 Tenseur d'inertie : généralités en dimension $n$

Soit $A$ un point fixe du solide (ou on se place dans $\mathscr R^\ast$ et $A=G$). Alors $\vec v(M)=\Omega(\overrightarrow{AM})$ et
$$
\mathsf L^{ij}(A)=\int\left(r^i\,\Omega^j{}_kr^k-r^j\,\Omega^i{}_kr^k\right)dm=J^{ik}\Omega^j{}_k-J^{jk}\Omega^i{}_k,\qquad J^{ij}:=\int r^ir^j\,dm\ \ (\text{tenseur des moments d'ordre 2}).
$$
$J^{ij}$ est **symétrique défini positif** (pour un corps non contenu dans un hyperplan). En base **orthonormale** et en notation matricielle : $\ \mathsf L=-(\Omega J+J\Omega)$. L'application $\Omega\mapsto\mathsf L=\mathcal I(\Omega)$ est linéaire de $\mathfrak{so}(n)$ dans lui-même : c'est l'**opérateur d'inertie généralisé**. On a $\mathrm{tr}\,J=g_{ij}J^{ij}=\int r^2dm$.

>[!tip]+ **Énergie cinétique de rotation.** $\ \mathcal E_c=\tfrac12\int\|\Omega\vec r\|^2dm=\tfrac12\,J^{kl}\,\Omega^i{}_k\Omega_{il}=\tfrac12\langle\mathsf L,\Omega\rangle$ avec $\langle\mathsf L,\Omega\rangle:=\tfrac12\mathsf L^{ij}\Omega_{ji}$.
>
>*Démonstration.* $\|\Omega\vec r\|^2=\Omega^i{}_k\Omega_{il}r^kr^l$, on intègre ; puis $\tfrac12\mathsf L^{ij}\Omega_{ji}=\tfrac12\left(J^{ik}\Omega^j{}_k-J^{jk}\Omega^i{}_k\right)\Omega_{ji}=J^{ik}\Omega^j{}_k\Omega_{ji}$, qui est la même quantité (renommage d'indices, $J$ symétrique). $\square$

**Dimension 3.** Avec $\Omega=\hat\omega$ : $\vec L=\int\vec r\times(\vec\omega\times\vec r)dm=\int\left(r^2\vec\omega-(\vec r\cdot\vec\omega)\vec r\right)dm$, soit
$$
\boxed{L^i=I^i{}_j\,\omega^j,\qquad I^{ij}=\int\left(r^2g^{ij}-r^ir^j\right)dm=(\mathrm{tr}\,J)\,g^{ij}-J^{ij},\qquad\mathcal E_c=\tfrac12I_{ij}\omega^i\omega^j.}
$$
$I$ est symétrique, **diagonalisable en base orthonormale** : $I=\mathrm{diag}(I_1,I_2,I_3)$ (axes principaux, moments principaux $I_k>0$, $I_k\le I_l+I_m$) ; inversement $J^{ii}=\tfrac12(I_j+I_k-I_i)$. Le **moment d'inertie par rapport à l'axe** $\Delta=(A,\vec u)$, $\|\vec u\|=1$, est $\ J_\Delta=\vec u\cdot I\cdot\vec u=\int d_\perp^2\,dm$. **Dimension 2** : $\mathsf L^{12}=(\mathrm{tr}\,J)\,\omega=J_z\,\omega$ ($J_z=\int r^2dm$), un scalaire.

*Rotation autour d'un axe fixe (cas du document d'origine).* Pour $\vec\omega=\Omega\vec e_z$, $\vec v=\Omega r\vec e_\theta$ et $\vec L(O)\cdot\vec e_z=\Omega\int r^2dm=J_\Delta\Omega$ ; la composante transverse $-\Omega\int rz\,dm\,\vec e_r$ s'annule si $\Delta$ est un **axe de révolution** ou si le plan $\perp\Delta$ passant par $O$ est un plan de symétrie ($I$ diagonale dans la base cylindrique).

## 10.3 Théorème de Huygens–Steiner

>[!tip]+ **Huygens–Steiner.** Soit $\vec a=\overrightarrow{AG}$. Alors $\ \boxed{J^{ij}_A=J^{ij}_G+m\,a^ia^j}$, et en dimension 3 : $I_A^{ij}=I_G^{ij}+m\left(a^2g^{ij}-a^ia^j\right)$ ; pour un axe $\Delta_A\parallel\Delta_G$ à distance $d$ : $\ J_{\Delta_A}=J_{\Delta_G}+md^2$.
>
>*Démonstration.* $\overrightarrow{AM}=\overrightarrow{AG}+\overrightarrow{GM}$ ; $J_A=\int(a+r_G)^i(a+r_G)^jdm=m\,a^ia^j+a^i\!\int r_G^jdm+a^j\!\int r_G^idm+J_G$, et $\int r_G\,dm=0$. $\square$

## 10.4 Dynamique du solide

**Torseurs.** $\mathscr C(A)=\{m\vec v_G;\mathsf L(A)\}$ ; Koenig : $\mathsf L(A)=\mathsf L^\ast+m\overrightarrow{AG}\wedge\vec v_G$, avec $\mathsf L^\ast=\mathcal I_G(\Omega)$ (inertie en $G$). **Énergie cinétique** (Koenig) : $\mathcal E_c=\tfrac12m\|\vec v_G\|^2+\tfrac12\langle\mathsf L^\ast,\Omega\rangle$.

**Équations du mouvement.** TRD : $m\vec a_G=\vec F^{\mathrm{ext}}$ ; TMC\* : $\dfrac{d\mathsf L^\ast}{dt}\Big)_{\mathscr R}=\mathsf M^{\mathrm{ext}}(G)$ (et TMC en un point fixe $O$ : $\dot{\mathsf L}(O)=\mathsf M^{\mathrm{ext}}(O)$). **Puissance des forces extérieures** : $\mathscr P=\langle\mathscr A,\mathscr V\rangle=\vec F\cdot\vec v_A+\tfrac12\mathsf M^{ij}(A)\Omega_{ji}$ (dim. 3 : $\vec F\cdot\vec v_A+\vec M_A\cdot\vec\omega$), et **TEC** : $\dot{\mathcal E}_c=\mathscr P^{\mathrm{ext}}$ ($\mathscr P^{\mathrm{int}}=0$ pour un solide).

**Équations d'Euler (dans le repère du corps).** Dans la base $(\vec e_{i'})$ liée au solide $J^{ij}$ est **constant**. D'après §1.3 (tenseur antisymétrique), $\ \dot{\mathsf L}\big)_{\mathscr R}=\dot{\mathsf L}\big)_{\mathscr S}+[\Omega,\mathsf L]$, d'où
$$
\boxed{\ \dot{\mathsf L}\big)_{\mathscr S}+[\Omega,\mathsf L]=\mathsf M^{\mathrm{ext}}(G),\qquad \mathsf L=-(\Omega J+J\Omega)\ }\quad(\text{équation d'Euler–Arnold sur }\mathfrak{so}(n)).
$$
**Dimension 3, axes principaux** : $\dot{\vec L}+\vec\omega\times\vec L=\vec M$ avec $L_k=I_k\omega_k$ donne
$$
I_1\dot\omega_1+(I_3-I_2)\,\omega_2\omega_3=M_1,\qquad I_2\dot\omega_2+(I_1-I_3)\,\omega_3\omega_1=M_2,\qquad I_3\dot\omega_3+(I_2-I_1)\,\omega_1\omega_2=M_3 .
$$
*Toupie libre* ($\vec M=0$) : $\|\vec L\|^2$ et $\mathcal E_c$ sont conservés ; $\vec L$ de norme fixe dans le solide, sur l'ellipsoïde $\sum\frac{L_k^2}{I_k}=2\mathcal E_c$ (**Poinsot**) ; les rotations autour des axes de plus grand et de plus petit moments sont stables, celle autour de l'axe intermédiaire est **instable** (théorème de l'axe intermédiaire).

**Le solide en Noether.** Le lagrangien d'un solide de centre $G$ est $L=\tfrac12m\|\vec v_G\|^2+\tfrac12\langle\mathcal I_G(\Omega),\Omega\rangle-V$ ; l'invariance par translation donne $\vec P$, par rotation donne $\mathsf L$, et l'ensemble s'identifie à un système hamiltonien sur $T^\ast SE(n)$ dont les symétries sont celles de $SE(n)$.

**Exemple — pendule pesant.** Solide mobile autour d'un axe horizontal fixe $\Delta$, distance $d=OG$ : $J_\Delta\ddot\theta=-mgd\sin\theta$ ; petites oscillations : $\omega_0=\sqrt{mgd/J_\Delta}$, avec $J_\Delta=J_{\Delta_G}+md^2$ (Huygens).

## 10.5 Moments d'inertie de quelques corps symétriques

*Méthode.* On calcule le tenseur $J^{ij}=\int x^ix^j\,dm$ (diagonal pour un corps à symétries), puis $I^{ii}=\mathrm{tr}J-J^{ii}$ en dimension 3.

>[!tip]+ **Boule pleine de rayon $R$ en dimension $n$** (densité uniforme, masse $m$)
>Avec $\int_0^R r^{n+1}dr\Big/\int_0^Rr^{n-1}dr=\dfrac{nR^2}{n+2}$ : $\ \int r^2dm=\dfrac{n}{n+2}mR^2$ et, par isotropie, $\ \boxed{J^{ij}=\dfrac{mR^2}{n+2}\,g^{ij}}$. Le moment d'inertie pour une rotation dans un plan est $\mathrm{tr}$-partielle : $J_{12}=J^{11}+J^{22}=\dfrac{2mR^2}{n+2}$. Cas $n=3$ : $\dfrac25mR^2$ ; $n=2$ (disque) : $\dfrac12mR^2$.
>**Sphère creuse** $S^{n-1}$ : $J^{ij}=\dfrac{mR^2}{n}g^{ij}$, d'où en dimension 3 : $\dfrac23mR^2$, en dimension 2 (cercle) : $mR^2$.
>**Ellipsoïde plein** (demi-axes $a_i$) : $J^{ii}=\dfrac{ma_i^2}{n+2}$ ; en dimension 3, $I_1=\dfrac m5(a_2^2+a_3^2)$.

**Résultats en dimension 3 (axes principaux en $G$), masse $m$ :**

| Corps | $J^{xx},J^{yy},J^{zz}$ | $I_x$ | $I_y$ | $I_z$ |
| --- | --- | --- | --- | --- |
| Tige mince, longueur $\ell$ (axe $x$) | $\frac{m\ell^2}{12},0,0$ | $0$ | $\frac{m\ell^2}{12}$ | $\frac{m\ell^2}{12}$ |
| Anneau (rayon $R$, axe $z$) | $\frac{mR^2}{2},\frac{mR^2}{2},0$ | $\frac{mR^2}{2}$ | $\frac{mR^2}{2}$ | $mR^2$ |
| Disque plein (axe $z$) | $\frac{mR^2}{4},\frac{mR^2}{4},0$ | $\frac{mR^2}{4}$ | $\frac{mR^2}{4}$ | $\frac{mR^2}{2}$ |
| Cylindre plein ($R$, hauteur $h$, axe $z$) | $\frac{mR^2}{4},\frac{mR^2}{4},\frac{mh^2}{12}$ | $\frac{mR^2}{4}+\frac{mh^2}{12}$ | idem | $\frac{mR^2}{2}$ |
| Parallélépipède $a\times b\times c$ | $\frac{ma^2}{12},\frac{mb^2}{12},\frac{mc^2}{12}$ | $\frac{m(b^2+c^2)}{12}$ | $\frac{m(a^2+c^2)}{12}$ | $\frac{m(a^2+b^2)}{12}$ |
| Sphère pleine | $\frac{mR^2}{5}$ (×3) | $\frac25mR^2$ | idem | idem |
| Sphère creuse | $\frac{mR^2}{3}$ (×3) | $\frac23mR^2$ | idem | idem |
| Cône plein ($R$, axe $z$) | $\frac{3mR^2}{20},\frac{3mR^2}{20},\cdot$ | | | $\frac{3}{10}mR^2$ |
| Tore (rayon $R$, tube $r$) | | | | $m\left(R^2+\frac34r^2\right)$ |

*Vérifications.* Pour le cylindre : $I_z=J^{xx}+J^{yy}=\frac12mR^2$, $I_x=J^{yy}+J^{zz}=\frac{mR^2}{4}+\frac{mh^2}{12}$ ; pour la tige $\frac{m\ell^2}{12}$ puis, au bout de la tige, Huygens $J=\frac{m\ell^2}{12}+m\left(\frac{\ell}{2}\right)^2=\frac{m\ell^2}{3}$. Pour un corps **plan** ($z=0$), $J^{zz}=0$ et $I_z=I_x+I_y$ (théorème des axes perpendiculaires).

# 11. Contrôles de cohérence et corrections

>[!question]- Liste de vérifications
>1. Chaque contraction se fait entre un indice haut et un indice bas ; on abaisse/élève avec $g$.
>2. $\Omega^i{}_j$ est $g$-antisymétrique ($\Omega_{ij}=-\Omega_{ji}$) ; un **vecteur** rotation n'existe qu'en $n=3$.
>3. Le produit $\vec u\wedge\vec w$ est un tenseur antisymétrique ; $\times$ n'a de sens qu'en dimension 3 orientée.
>4. Les moments dépendent du point (BABAR) ; les résultantes n'en dépendent pas.
>5. Le TMD/TMC avec point mobile : $\mathsf D=\dot{\mathsf L}+\vec v_A\wedge\vec P$.
>6. L'annulation des moments internes demande des forces **centrales** ; l'annulation de la résultante, seulement l'antisymétrie.
>7. Les forces d'inertie ne sont **pas** des forces d'interaction : elles n'obéissent pas à la 3e loi.
>8. $\mathscr R^\ast$ est en translation mais pas forcément galiléen ; TMC\* reste vrai.

>[!warning]- Corrections apportées au document de départ
>- Dans la loi de composition des accélérations, le terme centripète est $\Omega^2(\overrightarrow{O'M})$ (et non appliqué à $\vec v_{\mathscr R'}$), et le terme d'Euler $\dot\Omega(\overrightarrow{O'M})$ appartient à l'accélération d'entraînement.
>- Dans la démonstration de la rotation instantanée, l'antisymétrie de $\Omega=\dot f_tf_t^{-1}$ suit de $f_tf_t^\ast=\mathrm{id}$ ; le lien $\vec\omega$–$\vec v$ passe par la dérivée de l'exponentielle (formule de la §0.3 avec $1-\cos\theta$ et $\theta-\sin\theta$), et non par une formule de Rodrigues sur la rotation elle-même.
>- Le « moment dynamique » est écrit avec la bonne identité $\mathsf D(A)=\dot{\mathsf L}(A)+\vec v(A)\wedge\vec P$.
>- Dans « $\mathrm{ad}_{\hat v}^3=-\|v\|^2\mathrm{ad}_{\hat v}$ », la relation est vraie pour l'action adjointe sur $\mathfrak{so}(3)\simeq\mathbb R^3$ ; l'espace engendré par $\{\dot v,v\times\dot v,v\times(v\times\dot v)\}$ est de dimension $\le3$ (et non 2).
