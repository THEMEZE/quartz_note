## 1. Algèbre de Poisson de Kepler

Pour $H=p^2/2m-k/r$ en dimension 3, avec $\{q,p\}=1$ :
$$
\{L_i,L_j\}=\epsilon_{ijk}L_k,\quad\{L_i,A_j\}=\epsilon_{ijk}A_k,\quad\{A_i,A_j\}=-2mH\,\epsilon_{ijk}L_k .
$$
Les $L_i$ et $A_i$ commutent avec $H$ (voir [[Vecteur de Runge–Lenz–Laplace]]).

>[!tip]+ **Théorème (symétrie cachée de Kepler).** Sur la surface d'énergie $H=E$, on renormalise $D_i=A_i/\sqrt{-2mE}$ ($E<0$). Alors
>$$
>\{L_i,L_j\}=\epsilon_{ijk}L_k,\ \ \{L_i,D_j\}=\epsilon_{ijk}D_k,\ \ \{D_i,D_j\}=\epsilon_{ijk}L_k ,
>$$
>c'est l'algèbre $\mathfrak{so}(4)$. Pour $E>0$ on obtient $\mathfrak{so}(3,1)$ ($D_i=A_i/\sqrt{2mE}$, signe de $\{D,D\}$ opposé) ; pour $E=0$, l'algèbre euclidienne $\mathfrak e(3)$. En dimension $n$, $\mathfrak{so}(n+1)$.
>
>*Démonstration.* Les deux premières relations expriment que $\vec A$ est un vecteur. Pour la troisième, $\{A_i,A_j\}$ se calcule par Leibniz à partir des crochets fondamentaux et donne $-2mH\epsilon_{ijk}L_k$ ; diviser par $-2mE$. $\square$

## 2. Structure $\mathfrak{so}(3)\oplus\mathfrak{so}(3)$

Posons $\vec J_\pm=\tfrac12(\vec L\pm\vec D)$. Alors $\{J_{\pm i},J_{\pm j}\}=\epsilon_{ijk}J_{\pm k}$, $\{J_+,J_-\}=0$ (voir [[Algèbre de Lie]]), et comme $\vec L\cdot\vec D=0$ : $\vec J_+^{\,2}=\vec J_-^{\,2}=\tfrac14(L^2+D^2)=\dfrac{mk^2}{-8E}$ (classique, d'après $A^2=m^2k^2+2mEL^2$).

## 3. Conséquence quantique : le spectre de l'hydrogène

Dans la version quantique (Pauli, 1926), $[J_{\pm i},J_{\pm j}]=i\hbar\epsilon_{ijk}J_{\pm k}$ avec $\vec J_+^{\,2}=\vec J_-^{\,2}=\hbar^2j(j+1)$ et la relation $L^2+D^2+\hbar^2=\dfrac{mk^2}{-2E}$ :
$$
\hbar^2(2j+1)^2=\frac{mk^2}{-2E}\ \Longrightarrow\ \boxed{E_n=-\frac{mk^2}{2\hbar^2n^2},\quad n=2j+1.}
$$
La dégénérescence est $(2j+1)^2=n^2$ : elle est expliquée **sans calcul radial** par la symétrie cachée (le moment cinétique seul n'explique que $2\ell+1$).

## 4. Interprétation géométrique

La projection stéréographique de l'espace des impulsions sur la sphère $S^3$ (Fock, Moser) envoie le flot de Kepler à énergie fixée sur le **flot géodésique** de $S^3$, dont le groupe d'isométries est $SO(4)$. Les orbites de Kepler sont les grands cercles ; elles se ferment toutes, et $\vec A$ est le générateur des « rotations » qui les mêlent.

## 5. Fil de Noether

La symétrie n'est pas une transformation de l'espace des configurations mais du **fibré cotangent** ([[Mécanique hamiltonienne]]) : le [[Théorème de Noether]] hamiltonien relie $\vec A$ à ce flot via $\{\cdot,A\}$ ([[Crochet de Poisson]]).
