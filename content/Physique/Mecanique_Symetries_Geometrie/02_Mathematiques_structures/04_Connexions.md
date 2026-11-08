---
title: Connexions, courbure, holonomie
tags:
  - Mathematiques
  - Connexions
  - Jauge
lang: fr
---

> Retour : [[00_Index]] · avant : [[03_Fibres]] · [[02_Formes_differentielles_calcul_exterieur]] · suite : [[03_Jauge_EM_YM_Gravite]] · [[10_Relativite_generale_equations_Einstein]]

# Connexions, courbure, holonomie

## 1. Pourquoi une connexion

Sur une variété il n'y a pas de dérivée canonique d'une section d'un fibré (comment comparer des éléments de fibres différentes ?). Une **connexion** fournit un transport parallèle et une dérivée covariante. Les trois « dérivées » à ne pas confondre :

| Opérateur | Agit sur | Dépend de | Propriété |
|---|---|---|---|
| $d$ | formes $\Omega^p(M)$ | rien | $d^2=0$ |
| $\nabla_X$ | sections d'un fibré vectoriel (tenseurs) | une connexion | $\nabla_{fX}=f\nabla_X$, Leibniz |
| $D=d+\rho_\ast(A)$ | formes à valeurs dans un fibré associé | la connexion $A$ | $D^2=\rho_\ast(F)\ne0$ en général |

## 2. Connexion sur un fibré vectoriel

$E\to M$ vectoriel. Une connexion est un opérateur $\nabla\colon\Gamma(E)\to\Omega^1(M,E)$, $\nabla(f\sigma)=df\otimes\sigma+f\nabla\sigma$. Dans une base locale $(e_a)$ : $\nabla e_a=\omega^b{}_a\,e_b$ ($\omega\in\Omega^1(U,\mathfrak{gl}_r)$) donc
$$
\nabla\sigma=d\sigma+\omega\,\sigma\qquad(\sigma=\sigma^ae_a).
$$
Changement de base $e'=e\,g^{-1}$... (convention) : $\omega'=g\,\omega\,g^{-1}-dg\,g^{-1}$ ; en jauge « de matrice active » : $A\mapsto g^{-1}Ag+g^{-1}dg$.
**Courbure** : $F\doteq\nabla^2\in\Omega^2(M,\mathrm{End}E)$, $F=d\omega+\omega\wedge\omega$, $F(X,Y)=[\nabla_X,\nabla_Y]-\nabla_{[X,Y]}$.
Remarque (**$A\wedge A\ne0$** pour des 1-formes matricielles) : $(A\wedge A)_{\mu\nu}=[A_\mu,A_\nu]$, donc $A\wedge A=\tfrac12[A,A]$, non nul ssi la structure est non abélienne ; pour $U(1)$, $A\wedge A=0$.

## 3. Connexion sur un fibré principal (Ehresmann)

$P\to M$ de groupe $G$, algèbre $\mathfrak g$. Fibre verticale $VP=\ker\pi_\ast$ ; **champ fondamental** $\xi^\sharp_p=\tfrac d{dt}|_0\,p\,e^{t\xi}$.
> **Définition.** Une **connexion** est une 1-forme $\omega\in\Omega^1(P,\mathfrak g)$ telle que (i) $\omega(\xi^\sharp)=\xi$ ; (ii) $R_g^\ast\omega=\mathrm{Ad}_{g^{-1}}\omega$.
> Équivalent : un sous-fibré horizontal $HP=\ker\omega$, $G$-invariant, $TP=HP\oplus VP$.

- **Potentiel de jauge** : pour une section locale $s$, $A\doteq s^\ast\omega\in\Omega^1(U,\mathfrak g)$ ; $s'=sg\Rightarrow A'=g^{-1}Ag+g^{-1}dg$.
- **Dérivée covariante** sur un fibré associé $P\times_GV$ : $D_A\psi=d\psi+\rho_\ast(A)\psi$.
- **Relèvement horizontal / transport parallèle** : à $\gamma$ dans $M$ on associe l'unique $\tilde\gamma$ horizontale au-dessus ; $\tilde\gamma(1)=\tilde\gamma(0)\,\mathrm{Hol}_\gamma$, $\mathrm{Hol}=\mathcal P\exp(-\!\int_\gamma A)$ (exponentielle ordonnée).
- **Courbure** : $\Omega\doteq d\omega+\tfrac12[\omega,\omega]=D\omega\in\Omega^2(P,\mathfrak g)$ (équation de structure de Cartan), horizontale équivariante ; $F=s^\ast\Omega=dA+A\wedge A=dA+\tfrac12[A,A]$, soit $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu]$.
- **Bianchi** : $D\Omega=0$, en jauge $dF+[A,F]=0$ ( $D F\doteq dF+A\wedge F-F\wedge A$ ). *Preuve* : $dF=dA\wedge A-A\wedge dA$ et $[A,F]=A\wedge dA-dA\wedge A+A^3-A^3$. $\square$ (Pour $U(1)$ : $dF=0$.)
- **Holonomie infinitésimale** autour d'un petit lacet d'aire $\epsilon^2$ dans le plan $(\mu\nu)$ : $\mathrm{Hol}=1-\epsilon^2F_{\mu\nu}+\dots$ : **la courbure est le défaut de commutation du transport parallèle**.
- **Théorème d'Ambrose–Singer** : l'algèbre de Lie du groupe d'holonomie est engendrée par les valeurs de $F$ transportées.

## 4. Yang–Mills

Action $S_{YM}=-\tfrac1{2g^2}\int\langle F\wedge\star F\rangle$ ($\langle,\rangle$ = forme invariante, Killing). Équations : **Bianchi** (identité) $D F=0$ ; **dynamique** $D\star F=\star J$, i.e. $D_\mu F^{\mu\nu}=J^\nu$. Pour $G=U(1)$ : Maxwell $dF=0$, $d\star F=\star J$. Non-linéarité : $[A,\star F]$ ⇒ auto-interaction des gluons.
*Remarque* : $DF=0$ est une **identité géométrique** (équivalent de $dF=0$) ; $D\star F=\star J$ est une **équation du mouvement** ($\ne$ identité). Il n'existe pas en général d'équation du type « $D\star R=\star T$ » en gravité ; voir §6.

## 5. Chern–Weil, charges topologiques

Pour un polynôme invariant $P$ sur $\mathfrak g$, la forme $P(F,\dots,F)$ est fermée et sa classe dans $H^\ast(M)$ ne dépend pas de $A$ ([[05_Cohomologie]]) :
$$c_1=\Big[\tfrac i{2\pi}\operatorname{tr}F\Big],\quad c_2=\Big[\tfrac1{8\pi^2}\operatorname{tr}F\wedge F\Big]\ (\text{instantons }SU(2)).$$
**Chern–Simons** : $\operatorname{tr}(F\wedge F)=d\,\mathrm{CS}(A)$, $\mathrm{CS}(A)=\operatorname{tr}(A\,dA+\tfrac23A^3)$.

## 6. Connexions sur $TM$ : Levi-Civita, tétrades, torsion

**Connexion affine** $\nabla$ : $\nabla_{\partial_\mu}\partial_\nu=\Gamma^\rho{}_{\mu\nu}\partial_\rho$ ; $\nabla_\mu V^\rho=\partial_\mu V^\rho+\Gamma^\rho{}_{\mu\sigma}V^\sigma$.
- **Torsion** $T(X,Y)=\nabla_XY-\nabla_YX-[X,Y]$ ; $T^\rho{}_{\mu\nu}=\Gamma^\rho{}_{\mu\nu}-\Gamma^\rho{}_{\nu\mu}$.
- **Courbure de Riemann** $R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z$ ; $R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho_{\nu\sigma}-\partial_\nu\Gamma^\rho_{\mu\sigma}+\Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma}-\Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma}$.
- **Théorème fondamental** : sur $(M,g)$ il existe une unique connexion **sans torsion** ($T=0$) et **compatible** ($\nabla g=0$) : **Levi-Civita**, $\Gamma^l_{jk}=\tfrac12g^{lr}(\partial_jg_{rk}+\partial_kg_{rj}-\partial_rg_{jk})$ (**attention** : le dernier terme est $\partial_rg_{jk}$).

**Formalisme des tétrades (Cartan).** Repère mobile orthonormé $e_a=e_a{}^\mu\partial_\mu$, coframe $e^a$, $g=\eta_{ab}e^ae^b$. Connexion de spin $\omega^a{}_b$ avec $\nabla e_a=\omega^b{}_a\otimes e_b$ ; compatibilité métrique $\Leftrightarrow\omega_{ab}=-\omega_{ba}$ ($\omega\in\mathfrak{so}(1,3)$).
$$
\boxed{T^a=de^a+\omega^a{}_b\wedge e^b},\qquad \boxed{R^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b} .
$$
*Preuve* (équivalence avec $T(X,Y)$) : en projetant $T(X,Y)=\nabla_XY-\nabla_YX-[X,Y]$ sur $e^a$ on trouve $X(e^a(Y))-Y(e^a(X))-e^a([X,Y])+\omega^a{}_b(X)e^b(Y)-\omega^a{}_b(Y)e^b(X)$, soit $de^a(X,Y)+(\omega^a{}_b\wedge e^b)(X,Y)$ par la formule invariante de [[02_Formes_differentielles_calcul_exterieur]]. $\square$
**Bianchi** : $DR^a{}_b=0$ (deuxième), $DT^a=R^a{}_b\wedge e^b$ (première ; pour Levi-Civita $R^a{}_b\wedge e^b=0$). *Preuve de $DR=0$* : $dR=d\omega\wedge\omega-\omega\wedge d\omega$ ; $\omega\wedge R-R\wedge\omega=\omega\wedge d\omega-d\omega\wedge\omega$ (les termes en $\omega^3$ se simplifient) ; somme nulle. $\square$ En indices : $\nabla_{[\lambda}R_{\mu\nu]\rho\sigma}=0$ (antisymétrisation sur 3 indices).
**Dictionnaire** : $\Gamma^\rho{}_{\mu\nu}=e_a{}^\rho(\partial_\mu e^a{}_\nu+\omega^a{}_{b\mu}e^b{}_\nu)$ ; $R^\rho{}_{\sigma\mu\nu}=e_a{}^\rho e^b{}_\sigma R^a{}_{b\mu\nu}$.

**Tableau (corrigé).**
| Théorie | Connexion | Courbure | Identité | Équation dynamique |
|---|---|---|---|---|
| EM, $U(1)$ | $A$ | $F=dA$ | $dF=0$ | $d\star F=\star J$ |
| Yang–Mills | $A$ | $F=dA+A\wedge A$ | $DF=0$ | $D\star F=\star J$ |
| Gravité (tétrade) | $(e^a,\omega^{ab})$ | $(T^a,R^{ab})$ | $DR=0$, $DT^a=R^a{}_b e^b$ | Einstein–Cartan : $\varepsilon_{abcd}e^b\wedge R^{cd}\propto\tau_a$ ; $\varepsilon_{abcd}e^c\wedge T^d\propto\sigma_{ab}$ |

## 7. Connexion de spin sur le fibré des spineurs

$\nabla_\mu\psi=\partial_\mu\psi+\tfrac14\omega_\mu{}^{ab}\gamma_{ab}\psi$ avec $\gamma_{ab}=\tfrac12[\gamma_a,\gamma_b]$ ([[09_Algebres_de_Clifford_spineurs]]) ; $[\nabla_\mu,\nabla_\nu]\psi=\tfrac14R_{\mu\nu}{}^{ab}\gamma_{ab}\psi$. Équation de Dirac courbe : $i\gamma^\mu\nabla_\mu\psi-m\psi=0$. Gravitino : $D_\mu\epsilon=\nabla_\mu\epsilon$, transformation de supergravité $\delta\psi_\mu=D_\mu\epsilon$ ([[02_Supergravite_connexion_courbure]]).

## 8. Connexion de Cartan, Poincaré, super-Poincaré

Connexion à valeurs dans $\mathfrak g=\mathfrak{iso}(1,3)$ : $\mathcal A=e^aP_a+\tfrac12\omega^{ab}J_{ab}$, courbure $\mathcal F=d\mathcal A+\tfrac12[\mathcal A,\mathcal A]=T^aP_a+\tfrac12R^{ab}J_{ab}$ ; composantes : $T^a$ (translations) et $R^{ab}$ (rotations de Lorentz). **Torseur de courbure** : le couple (résultante-translation, moment-rotation) de [[02_Torseurs_Varignon_generalise]]. Extension super : $\mathcal A\to\mathcal A+\bar\psi Q$ ([[02_Supergravite_connexion_courbure]]).
