---
title: "Solide rigide : tenseur d'inertie, dynamique"
tags:
  - Physique
  - Mathematiques
lang: fr
partie: V
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Solide rigide : tenseur d'inertie, dynamique

## V.1 Tenseur d'inertie en dimension $n$

Soit $x=\overrightarrow{AM}$ et le tenseur de **second moment** $K_A\doteq\int x\,x^{\mathsf T}dm$ (symétrique, $\geq0$). Pour une rotation $\Omega$ : $v=\Omega x$,
$$
L(A)=\int x\wedge(\Omega x)\,dm=-(K_A\Omega+\Omega K_A)\ \ \Longrightarrow\ \ \mathbb I_A(\Omega)\doteq K_A\Omega+\Omega K_A,\quad L(A)=-\mathbb I_A(\Omega)
$$
($\mathbb I_A\colon\mathfrak{so}(n)\to\mathfrak{so}(n)$ linéaire symétrique). Énergie de rotation : $T_{\text{rot}}=\tfrac12\int|\Omega x|^2dm=\tfrac12\operatorname{tr}(\Omega K\Omega^{\mathsf T})$, et $2T_{\text{rot}}=\langle\mathscr C,\mathscr V\rangle_{\text{rot}}$.

**Cas $n=3$** : avec $K\,[\vec a]_\times+[\vec a]_\times K=[(\operatorname{tr}K\,\mathbb 1-K)\vec a]_\times$ on retrouve $\vec L=I\vec\Omega$, $I=\operatorname{tr}K\,\mathbb 1-K=\int(|x|^2\mathbb 1-xx^{\mathsf T})dm$ (matrice d'inertie classique, moments $I_{ij}=\int(r^2\delta_{ij}-x_ix_j)dm$). **Cas $n=2$** : $I=\int r^2dm$ scalaire, $L=I\omega$.

**Axes principaux.** On diagonalise $K=\operatorname{diag}(k_1,\dots,k_n)$ : les bivecteurs de base $e_i\wedge e_j$ sont propres, de valeur propre $k_i+k_j$ (**moments d'inertie de plan** $I_{ij}=k_i+k_j$). En 3D : $I_1=k_2+k_3$, etc.

**Boule homogène** (rayon $R$, masse $m$, dim $n$) : $K=\dfrac{mR^2}{n+2}\mathbb 1$, donc $\mathbb I=\dfrac{2mR^2}{n+2}\ \ (\kappa_n\doteq\tfrac2{n+2}$ : $\kappa_2=\tfrac12,\ \kappa_3=\tfrac25)$.

## V.2 Théorème de Huygens–Steiner (**[nD]**)

$$
K_A=K_G+m\,\overrightarrow{GA}\,\overrightarrow{GA}^{\mathsf T}\ \ \Longrightarrow\ \ \mathbb I_A(\Omega)=\mathbb I_G(\Omega)+m\big(\overrightarrow{GA}\,\overrightarrow{GA}^{\mathsf T}\Omega+\Omega\,\overrightarrow{GA}\,\overrightarrow{GA}^{\mathsf T}\big).
$$
En 3D, axe parallèle à $\Delta_G$ à distance $d$ : $I_\Delta=I_{\Delta_G}+md^2$.

## V.3 Dynamique du solide

Rotation + translation : $m\,a_G=\vec F^{\text{ext}}$ ; $\dfrac{dL^\ast}{dt}\Big)_{\mathscr R}=\mathfrak M^{\text{ext}}(G)$ avec $L^\ast=-\mathbb I_G(\Omega)$ et $T=\tfrac12mv_G^2+\tfrac12\langle\mathscr C^\ast,\mathscr V^\ast\rangle$.

**Équation d'Euler–Arnold.** Dans le repère propre du solide (où $\mathbb I$ est constant) :
$$
\dot L_b=[L_b,\Omega_b]+M_b,\qquad L_b=-\mathbb I(\Omega_b)\qquad\Big(\text{3D : }I\dot{\vec\Omega}+\vec\Omega\times I\vec\Omega=\vec M\Big).
$$
Géodésique de $SO(n)$ muni de la métrique invariante à gauche $\mathbb I$ en l'absence de couple. Pour $n=3$ : solide symétrique $\Rightarrow$ précession libre à la fréquence $|\Omega_p|=\big|\frac{I_3-I_1}{I_1}\big||\Omega_3|$ dans le repère du solide ; axe intermédiaire instable (théorème de la raquette).

**Rotation autour d'un axe fixe ($n=3$)** : $L_\Delta=I_\Delta\omega$, $I_\Delta\dot\omega=\mathfrak M_\Delta$, $T=\tfrac12I_\Delta\omega^2$.

## V.4 Moments d'inertie usuels ($n=3$, axe de symétrie)

Tige ($\tfrac1{12}ml^2$ centre ⟂), disque ($\tfrac12mR^2$), cerceau ($mR^2$), sphère pleine ($\tfrac25mR^2$), sphère creuse ($\tfrac23mR^2$), cylindre plein ($\tfrac12mR^2$, axe), cône plein ($\tfrac3{10}mR^2$). **Dimension $n$** : boule homogène, $\int r^2dm=\tfrac n{n+2}mR^2$, coquille $\int r^2dm=mR^2$.

## V.5 Exercices types corrigés (résultats)

- **Pendule de Foucault** (latitude $\lambda$) : le plan d'oscillation tourne à $\Omega_F=-\Omega_{T}\sin\lambda$ ; période $2\pi/(\Omega_T\sin\lambda)$ (Paris : $\simeq$ 32 h). Preuve : à petite amplitude, $\ddot{\xi}=-\omega_0^2\xi-2\,\Omega_{T,z}\,\hat z\times\dot{\xi}$ avec $\Omega_{T,z}=\Omega_T\sin\lambda$, résolu par $\xi=u\,e^{-i\Omega_{T,z}t}$.
- **Cerceau roulant sans glisser** sur plan incliné $\alpha$ : $a=\tfrac12g\sin\alpha$ (car $I=mR^2$). Disque : $\tfrac23g\sin\alpha$ ; sphère : $\tfrac57g\sin\alpha$.
- **Perle sur cerceau tournant** (rayon $R$, vitesse $\omega$ autour de l'axe vertical, $\theta$ depuis la verticale basse) : $\ddot\theta=\sin\theta\big(\omega^2\cos\theta-\tfrac gR\big)$ ; bifurcation fourche en $\omega_c^2=g/R$ : pour $\omega>\omega_c$, équilibre $\cos\theta_0=g/(R\omega^2)$ (brisure spontanée de symétrie $\theta\mapsto-\theta$). Ici l'énergie *mécanique* n'est pas conservée (liaison dépendant du temps) mais $H=\sum p\dot q-L$ l'est (**Jacobi**, VI.3).
- **Toupie de Lagrange** : intégrales premières $p_\phi,p_\psi,E$ ; potentiel effectif en $u=\cos\theta$, $\dot u^2=f(u)$ cubique : nutation entre deux racines.
