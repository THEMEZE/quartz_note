---
title: Supergravité ★★★
tags:
  - Physique
  - Mathematiques
lang: fr
partie: XIII
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Supergravité ★★★

## XIII.1 Supersymétrie locale $\Rightarrow$ gravité

Puisque $\{Q,\bar Q\}\sim P$, rendre le paramètre $\epsilon(x)$ **local** exige un $P$ local, i.e. des **difféomorphismes** : la supersymétrie locale contient la gravité. C'est la même logique que $U(1)$ global $\to$ local $\Rightarrow A_\mu$ (VII.4), appliquée au super-Poincaré. Le **gravitino** $\psi_\mu$ (spin $3/2$) est le champ de jauge de la SUSY.

**$\mathcal N=1$, $D=4$** (Freedman–van Nieuwenhuizen–Ferrara ; Deser–Zumino, 1976). Champs : tétrade $e^a{}_\mu$, gravitino $\psi_\mu$. Transformations (schématiques) :
$$
\delta e^a{}_\mu=\tfrac12\bar\epsilon\gamma^a\psi_\mu,\qquad\delta\psi_\mu=D_\mu\epsilon\doteq\big(\partial_\mu+\tfrac14\omega_\mu{}^{ab}\gamma_{ab}\big)\epsilon,\qquad
[\delta_{\epsilon_1},\delta_{\epsilon_2}]=\delta_{\text{diff}}(\xi^\mu=\tfrac12\bar\epsilon_2\gamma^\mu\epsilon_1)+\dots
$$
Action (Einstein–Rarita–Schwinger, conventions à vérifier) :
$$
S=\frac1{2\kappa^2}\int d^4x\,e\Big[R-\varepsilon^{\mu\nu\rho\sigma}\bar\psi_\mu\gamma_5\gamma_\nu D_\rho\psi_\sigma\Big],\qquad\kappa^2=8\pi G .
$$
**Super-Higgs** : si la SUSY est brisée, le goldstino est « mangé » par le gravitino, $m_{3/2}\sim F/M_{\text{Pl}}$ ($M_{\text{Pl}}=1/\sqrt{8\pi G}$ réduite). Avec constante cosmologique négative : sugra anti-de Sitter, superalgèbre $\mathfrak{osp}(\mathcal N|4)$.

## XIII.2 Supergravité à 11 dimensions

**Cremmer–Julia–Scherk (1978)** : champs $(g_{MN},\psi_M,C_{MNP})$ ($M=0,\dots,10$) ; degrés de liberté sur couche : graviton $44$ + $C_3$ $84$ $=128$ bosons ; gravitino $128$ fermions.
$$
S_{\text{bos}}=\frac1{2\kappa_{11}^2}\int\Big(R\star1-\tfrac12G_4\wedge\star G_4-\tfrac16C_3\wedge G_4\wedge G_4\Big),\qquad G_4\doteq dC_3,
$$
(le terme de Chern–Simons est exigé par la SUSY). **Superalgèbre** (Townsend) :
$$
\{Q,Q\}=C\Gamma^MP_M+\tfrac12C\Gamma^{MN}Z_{MN}+\tfrac1{5!}C\Gamma^{M_1\dots M_5}Z_{M_1\dots M_5},
$$
les charges centrales $Z_2$ et $Z_5$ sont les charges des **membranes M2** et **M5** (XV).

## XIII.3 Réduction dimensionnelle, Kaluza–Klein, symétries cachées

- **Kaluza–Klein** : sur $M_4\times S^1_R$, $ds^2=g_{\mu\nu}dx^\mu dx^\nu+e^{2\sigma}(dy+A_\mu dx^\mu)^2$ : l'**isométrie** $\partial_y$ (vecteur de Killing) est une symétrie ; sa **charge de Noether** — l'impulsion $n/R$ le long de $y$ — est la **charge électrique** 4D ($q=n\hbar/R$). La jauge $U(1)$ naît d'une symétrie de l'espace.
- **11D sur $T^7$** $\Rightarrow$ sugra $\mathcal N=8$, $D=4$, **symétrie globale cachée $E_{7(7)}$** (dim 133) avec $SU(8)$ locale, scalaires dans $E_{7(7)}/SU(8)$ (70 scalaires) — Cremmer–Julia. Analogue de la symétrie cachée $SO(n+1)$ de Kepler : la symétrie visible $SL(7)\ltimes\dots$ s'élargit après dualisation des formes.
- IIA = 11D sur $S^1$ ; IIB sugra (chirale) a $SL(2,\mathbb R)$ ; $D=10$ $\mathcal N=1$ $\leftrightarrow$ type I/hétérotiques.

## XIII.4 Comportement ultraviolet

Les calculs explicites (Bern, Carrasco, Dixon, Johansson, Roiban et al.) montrent que la sugra $\mathcal N=8$ est **finie à 3 et 4 boucles**, au-delà de ce que prévoit le comptage naïf. La finitude à tous les ordres reste ouverte. **Double copie** (KLT/BCJ) : amplitudes de gravité $\simeq$ (amplitudes de Yang–Mills)$^2$.

> **Voir aussi** : version détaillée en formes : [[02_Supergravite_connexion_courbure]] ; géométrie : [[04_Connexions]], [[03_Fibres]].
