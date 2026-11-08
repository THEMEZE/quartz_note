---
title: Lagrange, Hamilton, Liouville, Noether, application moment
tags:
  - Physique
  - Mathematiques
lang: fr
partie: VI
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Lagrange, Hamilton, Liouville, Noether, application moment

## VI.1 Formalisme lagrangien

Espace des configurations $Q$ (variété de dimension $d$), **métrique cinétique** $g_{ij}(q)$ ($T=\tfrac12g_{ij}\dot q^i\dot q^j$ ; pour $N$ points libres $Q=\mathbb R^{nN}$ et $g=\operatorname{diag}(m_a\delta)$).
$$
L\colon TQ\times\mathbb R\to\mathbb R,\ (q,\dot q,t)\mapsto L(q,\dot q,t)\doteq T-V,\qquad S[q]\doteq\int_{t_0}^{t_1}L\,dt .
$$
**Euler–Lagrange** : $\delta S=0\Rightarrow\dfrac d{dt}\dfrac{\partial L}{\partial\dot q^i}-\dfrac{\partial L}{\partial q^i}=0$, soit $g_{ij}\big(\ddot q^j+\Gamma^j_{kl}\dot q^k\dot q^l\big)=-\partial_iV$ (géodésique + force).

## VI.2 Hamiltonien, Poisson, Liouville

- **Légendre** : $p_i\doteq\partial L/\partial\dot q^i$, $H(q,p,t)\doteq p_i\dot q^i-L$ ; $\dot q^i=\partial H/\partial p_i$, $\dot p_i=-\partial H/\partial q^i$.
- **Crochet** : $\{f,g\}\doteq\dfrac{\partial f}{\partial q^i}\dfrac{\partial g}{\partial p_i}-\dfrac{\partial f}{\partial p_i}\dfrac{\partial g}{\partial q^i}$ ; $\ \dfrac{df}{dt}=\{f,H\}+\partial_tf$ ; $\{q^i,p_j\}=\delta^i_j$ ; Jacobi.
- **Liouville** : le champ hamiltonien $X_H=(\partial_pH,-\partial_qH)$ est de divergence nulle ; le flot conserve $dq\,dp$ (volume de l'espace des phases).
- **Théorème de Jacobi** : $\dfrac{dH}{dt}=-\dfrac{\partial L}{\partial t}=\dfrac{\partial H}{\partial t}$.

## VI.3 Théorème de Noether (mécanique)

> [!tip] **Noether.** Soit $q\mapsto q+\varepsilon\,\xi(q,t)$ une transformation à un paramètre (éventuellement $t\mapsto t+\varepsilon\tau$) telle que $\delta L=\varepsilon\,\dfrac{dF}{dt}$ sur toute trajectoire (symétrie « quasi-invariante »). Alors
> $$Q\doteq\frac{\partial L}{\partial\dot q^i}\,\xi^i-F=p\cdot\xi-F\qquad\text{est conservé.}$$
> *Preuve.* $\delta L=\partial_qL\,\xi+\partial_{\dot q}L\,\dot\xi=\tfrac d{dt}(p\cdot\xi)$ sur les solutions (EL), d'où $\tfrac d{dt}(p\cdot\xi-F)=0$. $\square$
> Réciproque (hamiltonienne) : $Q$ conservée $\Rightarrow$ $X_Q$ engendre une symétrie ; $\{Q,H\}=0$.

Pour $N$ points $(m_a,x_a)$ avec $L=\sum_a\tfrac12m_a\dot x_a^2-V\big(\{x_a-x_b\}\big)$ :

| Symétrie | Transformation | Charge de Noether | Torseur / théorème |
|---|---|---|---|
| translation $a\in E$ | $x_a\mapsto x_a+\varepsilon a$ | $\vec P=\sum p_a$ | **TRD** (résultante) |
| rotation $\omega\in\mathfrak{so}(n)$ | $x_a\mapsto x_a+\varepsilon\,\omega x_a$ | $L=\sum x_a\wedge p_a$ | **TMC** (moment), force centrale |
| translation en $t$ | $t\mapsto t+\varepsilon$ | $E=H$ | **TEM** ($V$ indép. de $t$) |
| **boost galiléen** $u\in E$ | $x_a\mapsto x_a+\varepsilon\,u\,t$ | $\vec K\doteq m\,\overrightarrow{OG}-\vec P\,t$ | $\dot{\vec K}=0\Leftrightarrow\ddot{\vec G}=0$ ($F=m\,\varepsilon u\cdot x_G$) |
| dilatation $x\mapsto\lambda x$, $t\mapsto\lambda^{2}t$ (seulement pour $V\propto r^{-2}$) | dilatation | $D=\sum p\cdot x-2tE$ | symétrie conforme du potentiel en $1/r^2$ (pour $V\propto r^k$ général : simple loi d'échelle $T\propto R^{1-k/2}$, viriel IV.7) |

> [!note] **Remarques**
> 1. Le torseur « *résultante* $\vec P$, *moment* $L$ » est exactement la charge de Noether de $E(n)=SO(n)\ltimes\mathbb R^n$ ; $\vec K$ (le moment de masse) est la charge du boost.
> 2. **Invariance par rotation $\Rightarrow$ force centrale** : $\{L_{ij},H\}=0\Leftrightarrow\sum_ax_a\wedge F_a=0$.
> 3. **Bargmann** : $\{K_i,P_j\}=m\,\delta_{ij}$ : la masse apparaît comme **extension centrale** de l'algèbre de Galilée (la représentation de Galilée en mécanique quantique est projective).

## VI.4 Algèbre de Poisson des charges et application moment

Avec $L_{ij}=x_ip_j-x_jp_i$, $P_k=p_k$ :
$$
\{L_{ij},P_k\}=\delta_{ik}P_j-\delta_{jk}P_i,\qquad \{L_{ij},L_{kl}\}=-\delta_{jk}L_{il}+\delta_{ik}L_{jl}+\delta_{jl}L_{ik}-\delta_{il}L_{jk},\qquad\{P_i,P_j\}=0 .
$$
C'est $\mathfrak e(n)=\mathfrak{so}(n)\ltimes\mathbb R^n$. En 3D : $\{L_x,L_y\}=L_z$.

**Application moment** (cadre géométrique). Si un groupe $G$ agit sur $Q$ et par relèvement sur $T^\ast Q$ (symplectique), l'application
$$
\mu\colon T^\ast Q\to\mathfrak g^\ast,\qquad\langle\mu(q,p),\xi\rangle\doteq p\cdot\xi_Q(q)
$$
est équivariante : $\mu(g\cdot z)=\mathrm{Ad}^\ast_g\mu(z)$ (à extension centrale près). Pour $G=E(n)$ :
- $\mu=(P,L)\in\mathfrak e(n)^\ast$ : le **torseur cinétique** ;
- $\mathrm{Ad}^\ast_{\text{translation par }a}$ : $(P,L)\mapsto(P,L+a\wedge P)$ = **loi de Varignon**/BABAR ;
- $\mathrm{Ad}^\ast_{g\in SO(n)}$ : $(P,L)\mapsto(gP,\,gLg^{\mathsf T})$.

**Orbites coadjointes** (Kirillov–Souriau). Les orbites de $E(n)$ dans $\mathfrak e(n)^\ast$ sont classées par $|R|$ et la classe de $M_{\min}\in\mathfrak{so}(n-1)^\ast$ (III.3) : en 3D, $|\vec R|$ et l'hélicité $\vec M\cdot\vec R/|\vec R|$ (le **spin**). C'est la version classique de la classification de Wigner (partie X).
