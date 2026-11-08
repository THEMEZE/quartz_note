---
title: Noether pour les champs, Schrödinger, jauge
tags:
  - Physique
  - Mathematiques
lang: fr
partie: VII
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Noether pour les champs, Schrödinger, jauge

## VII.1 Théorème de Noether pour un champ

Soit $\varphi^a(x)$ un champ sur $\mathbb R^{1,n}$ (ou $\mathbb R^{n+1}$), $\mathcal L(\varphi,\partial\varphi)$ une densité lagrangienne, $S=\int\mathcal L\,d^{n+1}x$. Pour $\delta\varphi=\varepsilon\,\Phi$ avec $\delta\mathcal L=\varepsilon\,\partial_\mu K^\mu$ :
$$
J^\mu\doteq\frac{\partial\mathcal L}{\partial(\partial_\mu\varphi^a)}\Phi^a-K^\mu,\qquad\partial_\mu J^\mu=0,\qquad Q\doteq\int J^0\,d^nx\ \text{ conservée.}
$$

## VII.2 Tenseur énergie-impulsion et torseur d'un champ

Translations $\Rightarrow$ tenseur canonique $T^\mu{}_\nu\doteq\dfrac{\partial\mathcal L}{\partial(\partial_\mu\varphi)}\partial_\nu\varphi-\delta^\mu_\nu\mathcal L$, $\partial_\mu T^{\mu\nu}=0$. Torseur du champ :
$$
P^\nu\doteq\int T^{0\nu}d^nx,\qquad M^{\mu\nu}\doteq\int\big(x^\mu T^{0\nu}-x^\nu T^{0\mu}\big)d^nx\ (+\text{terme de spin}).
$$
Changement d'origine $x\mapsto x+a$ : $M'^{\mu\nu}=M^{\mu\nu}-a^\mu P^\nu+a^\nu P^\mu$ : **Varignon dans l'espace-temps**. Les composantes spatiales $M^{ij}$ sont le moment cinétique ; $M^{0i}=t\,P^i-\int x^iT^{00}$ est le *moment de boost* (centre d'énergie).

## VII.3 Schrödinger comme théorie de champ

$$
\mathcal L=i\hbar\,\psi^\ast\partial_t\psi-\frac{\hbar^2}{2m}\nabla\psi^\ast\!\cdot\nabla\psi-V\psi^\ast\psi\ \ \Longrightarrow\ \ i\hbar\partial_t\psi=-\frac{\hbar^2}{2m}\Delta\psi+V\psi .
$$
- Invariance $\psi\mapsto e^{i\alpha}\psi$ ($U(1)$ global) $\Rightarrow$ $\rho=|\psi|^2$, $\vec j=\frac\hbar m\operatorname{Im}(\psi^\ast\nabla\psi)$, $\partial_t\rho+\nabla\!\cdot\vec j=0$ (conservation de la probabilité/charge).
- Translations $\Rightarrow\hat{\vec P}=-i\hbar\nabla$ ; rotations $\Rightarrow\hat L_{ij}=-i\hbar(x_i\partial_j-x_j\partial_i)$ ; $[\hat L_{ij},\hat P_k]=i\hbar(\delta_{ik}\hat P_j-\delta_{jk}\hat P_i)$ : on retrouve VI.4 avec $\{\cdot,\cdot\}\to\tfrac1{i\hbar}[\cdot,\cdot]$.
- Boost galiléen $\Rightarrow\psi'(x,t)=e^{\frac i\hbar(mu\cdot x-\frac12mu^2t)}\psi(x-ut,t)$ (phase de Bargmann).

## VII.4 Jauge locale et couplage minimal

Exiger l'invariance sous $\psi\mapsto e^{iq\alpha(x)/\hbar}\psi$ impose $D_\mu\doteq\partial_\mu-\tfrac{iq}\hbar A_\mu$, $A_\mu\mapsto A_\mu+\partial_\mu\alpha$, et $F_{\mu\nu}\doteq\partial_\mu A_\nu-\partial_\nu A_\mu$, $\mathcal L_{\text{Maxwell}}=-\tfrac14F_{\mu\nu}F^{\mu\nu}$. La **charge** est la charge de Noether de $U(1)$ ; elle ne provient pas de l'espace-temps (symétrie interne). Théorème de Noether (second) : une symétrie *locale* donne des identités (loi de Gauss, $\partial_\nu F^{\mu\nu}=j^\mu$ implique $\partial_\mu j^\mu=0$), non plus des charges indépendantes. **Gravité** = jauge des translations/difféomorphismes (XIV).
