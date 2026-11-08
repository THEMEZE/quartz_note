---
title: Gravitation quantique ★★★
tags:
  - Physique
  - Mathematiques
lang: fr
partie: XIV
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Gravitation quantique ★★★

## XIV.1 Le problème

Échelles de Planck : $\ell_P=\sqrt{\hbar G/c^3}\simeq1{,}6\times10^{-35}$ m, $t_P\simeq5{,}4\times10^{-44}$ s, $E_P=\sqrt{\hbar c^5/G}\simeq1{,}22\times10^{19}$ GeV. $\kappa^2=8\pi G$ a la dimension $[\text{masse}]^{2-D}$ : par comptage de puissance la relativité générale est **non renormalisable** pour $D>2$ (développement en $E^2/E_P^2$).
- **Théorie effective** (Donoghue) : à basse énergie, des corrections quantiques *calculables et universelles* existent, p. ex.
$$
V(r)=-\frac{Gm_1m_2}r\Big[1+3\frac{G(m_1+m_2)}{rc^2}+\frac{41}{10\pi}\frac{G\hbar}{r^2c^3}\Big].
$$
- UV : la gravité pure est finie à un boucle sur couche ('t Hooft–Veltman 1974) mais pas avec matière ; divergence à deux boucles $\propto R^3$ (Goroff–Sagnotti 1986).

## XIV.2 Gravité comme théorie de jauge de Poincaré : Einstein–Cartan

Connexion de Cartan à valeurs dans $\mathfrak{iso}(1,3)$ :
$$
\mathcal A=e^aP_a+\tfrac12\omega^{ab}M_{ab},\qquad T^a\doteq de^a+\omega^a{}_b\wedge e^b,\qquad R^{ab}\doteq d\omega^{ab}+\omega^a{}_c\wedge\omega^{cb},\qquad S=\frac1{2\kappa^2}\int\varepsilon_{abcd}\,e^a\wedge e^b\wedge R^{cd}.
$$
> [!tip] **Dictionnaire torseur ↔ gravité**
> | Mécanique des systèmes | Gravité de Cartan |
> |---|---|
> | résultante $R$ (translations) | tétrade $e^a$ ; courbure $\to$ **torsion** $T^a$ |
> | moment $M$ (rotations) | connexion de spin $\omega^{ab}$ ; courbure $R^{ab}$ |
> | torseur des actions $\{F;\mathfrak M\}$ | sources : **énergie-impulsion $\tau_a$** et **densité de spin $\sigma_{ab}$** ($\delta S/\delta e,\ \delta S/\delta\omega$) |
> | TRD, TMD | $\nabla_\mu T^{\mu\nu}=0$ et conservation du moment total (Noether **secondes** identités des difféos et du groupe de Lorentz local) |
> Équations : $G_{\mu\nu}=\kappa\tau_{\mu\nu}$ et torsion $\propto\kappa\sigma$ (Einstein–Cartan) ; en relativité générale usuelle la torsion est contrainte à $0$ et le spin ne joue pas de rôle sourcé.

## XIV.3 Quantification canonique : ADM, Wheeler–DeWitt, boucles

$ds^2=-N^2dt^2+h_{ij}(dx^i+N^idt)(dx^j+N^jdt)$, $\;S=\dfrac1{2\kappa^2}\displaystyle\int dt\,d^3x\,N\sqrt h\big({}^{(3)}\!R+K_{ij}K^{ij}-K^2\big)$, $\pi^{ij}=\dfrac{\sqrt h}{2\kappa^2}(K^{ij}-Kh^{ij})$.
$N,N^i$ sont des multiplicateurs de Lagrange : **contraintes** $\mathcal H\approx0$ (hamiltonienne), $\mathcal H_i\approx0$ (difféomorphismes spatiaux) ; **$H_{\text{tot}}=\int(N\mathcal H+N^i\mathcal H_i)\approx0$**. Quantification : $\hat{\mathcal H}\Psi[h_{ij}]=0$ (**Wheeler–DeWitt**) ; **problème du temps**.
*Analogue de dimension finie* : $S=-mc\int\sqrt{-\dot x^2}\,d\lambda$ est invariante par reparamétrisation $\Rightarrow H\approx0\Rightarrow p^2+m^2c^2=0$ (couche de masse, Klein–Gordon).
**Gravité quantique à boucles** (Ashtekar, Rovelli, Smolin) : variables $(A^i_a,E^a_i)$, $\{A^i_a(x),E^b_j(y)\}=8\pi\gamma G\,\delta^b_a\delta^i_j\delta^3(x-y)$ ($\gamma$ de Barbero–Immirzi), états = **réseaux de spin** ; spectres discrets :
$$
\hat A=8\pi\gamma\,\ell_P^2\sum_i\sqrt{j_i(j_i+1)}\quad(\text{aire}),
$$
volume discret ; $\gamma$ est calé par l'entropie du trou noir.

## XIV.4 Trous noirs, holographie

$T_H=\dfrac{\hbar c^3}{8\pi GMk_B}$, $S_{BH}=\dfrac{k_Bc^3A}{4G\hbar}=\dfrac{k_BA}{4\ell_P^2}$ : l'entropie croît avec l'**aire** (pas le volume) $\Rightarrow$ principe holographique ('t Hooft, Susskind). Décompte microscopique : états de D-branes (Strominger–Vafa 1996) ; réseaux de spin (LQG). Intégrale de chemin euclidienne (Gibbons–Hawking) : $Z=\int\mathcal Dg\,e^{-S_E[g]/\hbar}$.

## XIV.5 AdS/CFT (Maldacena 1997)

La théorie des cordes IIB sur $AdS_5\times S^5$ est **équivalente** à la théorie de jauge $\mathcal N=4$ $SU(N)$ super-Yang–Mills en $D=4$ ; $L^4=4\pi g_sN\,\ell_s^4$ ($\lambda=g^2_{YM}N$ le couplage de 't Hooft). **Dictionnaire** (Gubser–Klebanov–Polyakov–Witten) :
$$
Z_{\text{grav}}\big[\phi\big|_\partial=\phi_0\big]=\Big\langle e^{\int\phi_0\mathcal O}\Big\rangle_{\text{CFT}} .
$$
Les isométries de $AdS_5$ ($SO(4,2)$) sont le **groupe conforme du bord** ; $SO(4,2)\times SO(6)\subset PSU(2,2|4)$ (superconformal) : encore une identification « symétrie du volume $\leftrightarrow$ charge de Noether du bord ».

## XIV.6 Autres approches

Sécurité asymptotique (Weinberg ; Reuter 1998 : point fixe UV du flot de $G(k)$), triangulations dynamiques causales (Ambjørn–Loll), ensembles causaux (Sorkin), mousses de spin, géométrie non commutative. Aucune n'est vérifiée expérimentalement.

> **Voir aussi** : relativité générale et trous noirs : [[10_Relativite_generale_equations_Einstein]], [[11_Schwarzschild_trou_noir]], [[13_Kerr_trou_noir_en_rotation]] ; cohomologie/BRST : [[05_Cohomologie]].
