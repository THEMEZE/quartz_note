---
title: Moments, Varignon généralisé, théorie des torseurs
tags:
  - Physique
  - Mathematiques
lang: fr
partie: III
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Moments, Varignon généralisé, théorie des torseurs

## III.1 Moment d'un vecteur appliqué

Pour un vecteur $w$ appliqué en $M$ et un point $A$ :
$$
\mathfrak m_A(M,w)\doteq\overrightarrow{AM}\wedge w\in\Lambda^2E,\qquad \big(\mathfrak m_A\big)^{ij}=AM^i\,w^j-AM^j\,w^i .
$$
En 3D, $\mathfrak m_A=\overrightarrow{AM}\times w$ (via $M^{ij}=\varepsilon^{ijk}M_k$).

## III.2 Système de vecteurs : théorème de Varignon généralisé

Pour $(M_k,w_k)_k$ (ou une mesure) :
$$
R\doteq\sum_kw_k,\qquad M(A)\doteq\sum_k\overrightarrow{AM_k}\wedge w_k .
$$

> [!tip] Théorème (Varignon généralisé, **[nD]**)
> $$M(B)=M(A)+\overrightarrow{BA}\wedge R .$$
> *Preuve.* $\overrightarrow{BM_k}=\overrightarrow{BA}+\overrightarrow{AM_k}$, donc $M(B)=\sum_k\overrightarrow{BA}\wedge w_k+\sum_k\overrightarrow{AM_k}\wedge w_k$. $\square$
> En composantes : $M^{ij}(B)=M^{ij}(A)+BA^iR^j-BA^jR^i$.

**Composition de transports** : $M(C)=M(B)+\overrightarrow{CB}\wedge R=M(A)+\overrightarrow{CA}\wedge R$ (cocycle, compatible avec $\overrightarrow{CB}+\overrightarrow{BA}=\overrightarrow{CA}$).

**Version bilinéaire abstraite.** Soit $\beta\colon E\times W\to Z$ bilinéaire et $M_\beta(A)\doteq\sum_k\beta(\overrightarrow{AM_k},w_k)$. Alors $M_\beta(B)=M_\beta(A)+\beta(\overrightarrow{BA},R)$. Avec $\beta=\wedge$ : moments ; $\beta=\cdot$ : moment *scalaire* $\sum\overrightarrow{AM_k}\cdot w_k$ ; $\beta=\times$ en 3D.

**Dérivée d'un torseur à point de réduction mobile.** Si $A=A(t)$, la dérivée du torseur de type moment $\{R;M(A)\}$ est
$$
\dot{\mathscr T}(A)\doteq\{\dot R;\ \dot M(A)+v_A\wedge R\},\qquad \dot M(A)\doteq\textstyle\sum\overrightarrow{AM_k}\wedge\dot w_k .
$$
(Le terme $v_A\wedge R$ provient de $\frac d{dt}\overrightarrow{AM_k}=v_{M_k}-v_A$ ; il redonne $\mathscr D=\dot{\mathscr C}$ en IV.)

## III.3 Structure de torseur ; classification (**[nD]**)

- $\mathscr T(A)=\{R;M(A)\}$ est **un seul objet** : $R\in E$ et $M\in\Lambda^2E$, d'où $\dim=n+\tfrac{n(n-1)}2=\tfrac{n(n+1)}2=\dim\mathfrak e(n)$. En 3D : 6, d'où « deux vecteurs » — mais en général le moment n'est **pas** un vecteur.
- **Addition** : $\{R_1;M_1\}+\{R_2;M_2\}\doteq\{R_1+R_2;M_1+M_2\}$ (réduits au même point).
- **Résultante nulle** : $M$ est indépendant du point (**couple**), classifié par la forme normale de $\mathfrak{so}(n)$ (I.2) : $\lfloor n/2\rfloor$ invariants. Deux forces opposées $\pm w$ appliquées en $M_1,M_2$ : $M=\overrightarrow{M_2M_1}\wedge w$.
- **Invariant fondamental** : $M(B)\wedge R=M(A)\wedge R$ (car $R\wedge R=0$). Le **trivecteur** $M\wedge R\in\Lambda^3E$ est invariant. En 3D, $\star(M\wedge R)=\vec M\cdot\vec R$ (invariant scalaire classique) ; en espace-temps de dimension 4, c'est le **vecteur de Pauli–Lubański** (X).
- **Axe central généralisé.** Pour $R\neq0$ : on cherche $B$ avec $M(B)\lrcorner R=0$ (contraction $M^{ij}R_j=0$). Comme $M(B)R=M(A)R+\overrightarrow{BA}\,|R|^2-R\,(\overrightarrow{BA}\cdot R)$, la solution est
$$
\overrightarrow{AB}=\frac{M(A)\,R}{|R|^2}+\lambda R,\quad\lambda\in\mathbb R\quad(\text{droite affine}).
$$
Sur cette droite, $M_{\min}\in\Lambda^2(R^\perp)$ : forme canonique $\{R;M_{\min}\}$. En 3D, $\Lambda^2(R^\perp)=\mathbb R\,\star R$, donc $M_{\min}\parallel R$ (**torseur de Poinsot / hélicoïde**). En $n\geq4$, $M_{\min}$ reste un bivecteur de $R^\perp$ à $\lfloor(n-1)/2\rfloor$ invariants.
- **Existence d'un point où $M=0$** : possible ssi $M(A)\in\{a\wedge R\}$, i.e. ssi $M\wedge R=0$ (pour $R\neq0$) ; en 3D ssi $\vec M\cdot\vec R=0$.

## III.4 Deux types de torseurs, dualité, comoment

| | Type **vitesse** (élément de $\mathfrak e(n)$) | Type **moment** (élément de $\mathfrak e(n)^\ast$) |
|---|---|---|
| Données | $\{\Omega;v(A)\}$, $\Omega\in\mathfrak{so}(n)$ | $\{R;M(A)\}$, $R\in E$, $M\in\Lambda^2E$ |
| Transport | $v(B)=v(A)+\Omega\,\overrightarrow{AB}$ | $M(B)=M(A)+\overrightarrow{BA}\wedge R$ |
| Exemples | cinématique $\mathscr V$ | cinétique $\mathscr C$, dynamique $\mathscr D$, actions $\mathscr A$ |

**Comoment** (couplage $\mathfrak e(n)^\ast\times\mathfrak e(n)\to\mathbb R$) :
$$
\boxed{\langle\mathscr T,\mathscr V\rangle\doteq R\cdot v(A)-\tfrac12M^{ij}(A)\,\Omega_{ij}}\qquad(\text{3D : } \vec R\cdot v(A)+\vec M(A)\cdot\vec\Omega).
$$
*Indépendance de $A$* : $R\cdot\Omega\overrightarrow{AB}$ compense exactement $-\tfrac12(\overrightarrow{BA}\wedge R)^{ij}\Omega_{ij}$ (calcul direct). Conséquences :
- **Puissance** $\mathcal P=\langle\mathscr A,\mathscr V\rangle$ d'un système de forces sur un solide ;
- **Énergie cinétique** d'un solide : $2T=\langle\mathscr C,\mathscr V\rangle$ (IV.5).

## III.5 Systèmes continus et formulaire

Pour une mesure $dR(M)$ : $R=\iiint dR(M)$, $M(A)=\iiint\overrightarrow{AM}\wedge dR(M)$ ; Varignon inchangé. Les quatre torseurs de la mécanique ($\mathscr V,\mathscr C,\mathscr D,\mathscr A$) sont des instances (IV).
