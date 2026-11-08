---
title: Relativité restreinte : torseurs de Poincaré
tags:
  - Physique
  - Mathematiques
lang: fr
partie: X
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Relativité restreinte : torseurs de Poincaré

## X.1 Quadri-impulsion et chocs relativistes

Signature $(-+\cdots+)$ ou $(+-\cdots-)$ au choix ; ici $\eta=\operatorname{diag}(-1,1,\dots,1)$, $D=n+1$. $p^\mu=(E/c,\gamma m\vec v)$, $E=\gamma mc^2$, $\gamma=(1-v^2/c^2)^{-1/2}$, $E^2=(pc)^2+(mc^2)^2$, $p_\mu p^\mu=-m^2c^2$.
Dans un choc d'un système isolé, c'est **$P^\mu=\sum p^\mu_i$** (quadri-vecteur) qui est conservé ; la masse **n'est pas additive** : $Mc^2=\sqrt{(\sum E_i)^2-\|\sum\vec p_ic\|^2}$.
- Deux boules d'argile à $\pm0{,}6c$ qui fusionnent : $M=2\gamma m=2{,}5m$.
- **Invariant** $s\doteq(\sum E_i)^2-\|\sum\vec p_ic\|^2$ : seuil de création de paires. Proton sur cible fixe : $s=2m^2c^4(1+\gamma)\ge(4mc^2)^2\Rightarrow\gamma\ge7$ ($E_c=6mc^2\simeq5{,}6$ GeV, Bevatron 1955) ; collisionneur symétrique $\sqrt s=2\gamma mc^2$ ($\gamma\ge2$ suffit). LHC $\sqrt s=13{,}6$ TeV $\Leftrightarrow$ cible fixe $\simeq10^{17}$ eV.
- **Règle des $90^\circ$** : masses égales, $B$ au repos, élastique : $\tan\theta_A\tan\theta_B=\dfrac2{\gamma+1}$ ; $\gamma\to1$ : $\theta_A+\theta_B=90^\circ$, sinon $<90^\circ$.

## X.2 Groupe et algèbre de Poincaré, torseurs

$\mathrm{ISO}(1,n)=SO(1,n)\ltimes\mathbb R^{1,n}$, $\dim=\tfrac{(n+1)(n+2)}2$ : même structure que $E(n+1)$ avec une métrique lorentzienne. Un **torseur de Poincaré** est le couple
$$
\{P^\mu;\ M^{\mu\nu}\},\qquad M^{\mu\nu}(a)=M^{\mu\nu}(0)-a^\mu P^\nu+a^\nu P^\mu\quad(\text{Varignon}).
$$
Charges de Noether : $P^\mu$ (translations), $M^{ij}$ (rotations), $M^{0i}=t\,P^i-E\,x_E^i/c^2$ (boosts ; limite $c\to\infty$ : le moment de masse $\vec K=m\vec x_G-\vec Pt$ de VI.3). Algèbre :
$$
[P_\mu,P_\nu]=0,\quad[M_{\mu\nu},P_\rho]=i\hbar(\eta_{\nu\rho}P_\mu-\eta_{\mu\rho}P_\nu),\quad[M_{\mu\nu},M_{\rho\sigma}]=i\hbar(\eta_{\nu\rho}M_{\mu\sigma}-\eta_{\mu\rho}M_{\nu\sigma}-\eta_{\nu\sigma}M_{\mu\rho}+\eta_{\mu\sigma}M_{\nu\rho}).
$$
*Contraction* : $c\to\infty$ donne Galilée ; avec la masse comme extension centrale : Bargmann.

## X.3 Invariants, classification de Wigner

- Casimir 1 : $P^2=-M^2c^2$ (la masse). Casimir 2 : $W\doteq\star(M\wedge P)$, i.e. en $D=4$ le **vecteur de Pauli–Lubański** $W_\mu=\tfrac12\varepsilon_{\mu\nu\rho\sigma}M^{\nu\rho}P^\sigma$ ; $W^2=m^2c^2\hbar^2s(s+1)$ pour $m>0$ ; $W^\mu=\lambda P^\mu$ si $m=0$ (hélicité).
- **C'est l'invariant $M\wedge R$ de III.3 transposé à l'espace-temps** : le spin d'une particule est l'invariant du torseur de Poincaré, comme l'hélicité $\vec M\cdot\vec R/|R|$ en 3D. Les orbites coadjointes de $\mathrm{ISO}(1,3)$ (VI.4) $\leftrightarrow$ représentations unitaires irréductibles (Wigner).
- Groupe d'invariance du petit groupe : $SO(n)$ ($m>0$), $ISO(n-1)$ ($m=0$), etc.
