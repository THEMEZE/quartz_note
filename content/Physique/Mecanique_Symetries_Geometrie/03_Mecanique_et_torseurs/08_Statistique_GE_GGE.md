---
title: Quantités conservées et équilibre statistique (GE et GGE)
tags:
  - Physique
  - Mathematiques
lang: fr
partie: XI
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Quantités conservées et équilibre statistique (GE et GGE)

**Invariants de collision** (gaz de boules identiques, dimension $n$) : $1$, $\vec v$, $v^2$ ; ajouter $L$ du gaz $\Rightarrow$ $1+1+n+\tfrac{n(n-1)}2$ constantes. Théorème $H$ (Boltzmann) : stationnaire $\ln f=a+\vec b\cdot\vec v+c\,v^2$ (Maxwell–Boltzmann).

**Ensembles de Gibbs (GE)** : maximiser l'entropie sous contraintes $\langle Q_k\rangle$ donne $\rho\propto\exp(-\sum_k\lambda_kQ_k)$ :

| Situation | Distribution | Conservées |
|---|---|---|
| isolé | microcanonique | $E$ |
| échange d'énergie | canonique $e^{-\beta H}$ | $\langle E\rangle$ |
| énergie + particules | grand-canonique $e^{-\beta(H-\mu N)}$ | $\langle E\rangle,\langle N\rangle$ |
| gaz en mouvement et rotation | $\exp[-\beta(H-\vec u\cdot\vec P-\Omega:L)]$ | $E,\vec P,L$ |

**Le multiplicateur de Lagrange du torseur cinétique est le torseur cinématique** : dans la dernière ligne, $(\vec u,\Omega)\doteq$ $\mathscr V$ (vitesse d'entraînement, rotation d'ensemble) est conjugué du torseur $(\vec P,L)$ par $\lambda_k$ — l'équilibre « fait tourner » le système comme un solide.

**Quand il y a trop de constantes du mouvement.** 1D, masses égales : chaque choc élastique **échange les vitesses**, donc $\sum_i\varphi(v_i)$ est conservée pour toute $\varphi$ : infinité d'invariants, système **intégrable** (bâtonnets durs ; Lieb–Liniger, ansatz de Bethe). Le gaz ne thermalise pas.
Simulation : $N=4000$ boules, départ $\pm1$ : en 2D, relaxation vers la gaussienne ($\langle v_x^4\rangle=0{,}78\simeq3\langle v_x^2\rangle^2=0{,}75$) ; en 1D, aucun changement.
**GGE** : $\rho_{\text{GGE}}=Z^{-1}\exp(-\sum_k\lambda_kQ_k)$, $\lambda_k$ fixés par $\langle Q_k\rangle_{\text{GGE}}=\langle Q_k\rangle_{\text{départ}}$ (Rigol et al. 2007) ; expérience : berceau de Newton quantique (Kinoshita–Wenger–Weiss 2006), hydrodynamique généralisée (Castro-Alvaredo–Doyon–Yoshimura, Bertini et al. 2016).
Mise en garde : conservation d'une grandeur $\ne$ ensemble statistique ; plus il y a de conservées, plus l'équilibre « se souvient » de l'état initial.
