---
title: La métrique de Kerr — structure, symétries, horizons et ergorégion
tags:
  - Physique
  - Relativite-generale
  - Trous-noirs
lang: fr
---

> Retour : [[00_Index]] · avant : [[11_Schwarzschild_trou_noir]], [[12_Coordonnees_EF_Kruskal_Penrose_extension_maximale]] · suite : [[14_Kerr_horizons_ergoregion_extension_maximale]]
> D'après *P.B. (annexes D, E)*, complété (calculs des invariants, thermodynamique, Penrose). $G=c=1$.

# Le trou noir de Kerr

## 1. Métrique de Boyer–Lindquist

$$ds^2=-\frac{\Delta-a^2\sin^2\theta}{\rho^2}dt^2-\frac{4amr\sin^2\theta}{\rho^2}dt\,d\varphi+\frac{\rho^2}\Delta dr^2+\rho^2d\theta^2+\frac{\Sigma^2\sin^2\theta}{\rho^2}d\varphi^2\tag{BL}$$
$$\rho^2=r^2+a^2\cos^2\theta,\quad\Delta=r^2-2mr+a^2,\quad\Sigma^2=(r^2+a^2)^2-a^2\Delta\sin^2\theta .$$
Forme équivalente : $ds^2=-\big(1-\tfrac{2mr}{\rho^2}\big)dt^2-\tfrac{4amr\sin^2\theta}{\rho^2}dt\,d\varphi+\tfrac{\rho^2}\Delta dr^2+\rho^2d\theta^2+\big(r^2+a^2+\tfrac{2a^2mr\sin^2\theta}{\rho^2}\big)\sin^2\theta\,d\varphi^2$ (car $\Delta-a^2\sin^2\theta=\rho^2-2mr$ et $\Sigma^2=(r^2+a^2)\rho^2+2mra^2\sin^2\theta$).
**Paramètres** : $m=GM/c^2$, $a=J/(Mc)$ (moment cinétique par unité de masse, ici $J=ma$ en $G=c=1$) ; $a\in[0,m]$ pour un trou noir.
**Statut** : (BL) est une solution **exacte** de $R_{\mu\nu}=0$ (Kerr 1963). Elle se vérifie par un calcul direct (Ricci), ou structurellement par la forme de **Kerr–Schild** :
$$g_{\mu\nu}=\eta_{\mu\nu}+H\,l_\mu l_\nu,\quad H=\frac{2mr^3}{r^4+a^2z^2},\quad l^\mu\ \text{nul et géodésique},$$
dans laquelle les équations d'Einstein du vide deviennent **linéaires** en $H$ (propriété de Kerr–Schild), ce qui permet de les résoudre exactement ; ou par l'algorithme de Newman–Janis (complexification de $r\to r+ia\cos\theta$ de Schwarzschild).

**Déterminant et inverse.** $\det g=-\rho^4\sin^2\theta$ ; composantes contravariantes non nulles :
$$g^{tt}=-\frac{\Sigma^2}{\rho^2\Delta},\ g^{t\varphi}=-\frac{2amr}{\rho^2\Delta},\ g^{rr}=\frac\Delta{\rho^2},\ g^{\theta\theta}=\frac1{\rho^2},\ g^{\varphi\varphi}=\frac{\Delta-a^2\sin^2\theta}{\rho^2\Delta\sin^2\theta}=\frac{\rho^2-2mr}{\rho^2\Delta\sin^2\theta}.$$

## 2. Limites et cas particuliers

- $a\to0$ : $\rho\to r$, $\Sigma^2\to r^4$, $\Delta\to r^2f(r)$ : **Schwarzschild** (3) de [[11_Schwarzschild_trou_noir]]. $a$ est lié à la rotation (terme croisé $dt\,d\varphi$, effet de **Lense–Thirring**).
- $m\to0$ : $\Delta\to r^2+a^2$ et la métrique devient celle de **Minkowski en coordonnées sphéroïdales aplaties** : $x=\sqrt{r^2+a^2}\sin\theta\cos\varphi$, $y=\sqrt{r^2+a^2}\sin\theta\sin\varphi$, $z=r\cos\theta$ ; $dx^2+dy^2+dz^2=\tfrac{\rho^2}{r^2+a^2}dr^2+\rho^2d\theta^2+(r^2+a^2)\sin^2\theta\,d\varphi^2$. Les surfaces $r=\text{cte}$ sont des **ellipsoïdes** $\tfrac{x^2+y^2}{r^2+a^2}+\tfrac{z^2}{r^2}=1$ ; $\theta=\text{cte}$ : hyperboloïdes $\tfrac{x^2+y^2}{a^2\sin^2\theta}-\tfrac{z^2}{a^2\cos^2\theta}=1$.
- $a=m$ : Kerr extrémal (un seul horizon, $\kappa=0$) ; $a>m$ : singularité nue (exclue par la censure cosmique).

## 3. Singularités

Les seuls points où (BL) est singulière : $\Delta=0$ et $\rho=0$.
- **$\Delta=0$** : singularité de **coordonnées** (levée en coordonnées ingoing Kerr/Kerr–Schild, [[14_Kerr_horizons_ergoregion_extension_maximale]]) ; racines $r_\pm=m\pm\sqrt{m^2-a^2}$.
- **$\rho=0$** : $r=0$ **et** $\theta=\pi/2$ ; le scalaire de Kretschmann $K=\tfrac{48m^2(r^2-a^2\cos^2\theta)(\rho^4-16r^2a^2\cos^2\theta)}{\rho^{12}}$ diverge : singularité **intrinsèque**. En coordonnées cartésiennes aplaties, $r=0$ est le **disque** $x^2+y^2\le a^2$, $z=0$ ; la singularité est l'**anneau** $x^2+y^2=a^2,z=0$ (de genre **temps**, donc évitable : on peut la contourner et passer dans $r<0$ à travers le disque).

## 4. Symétries : vecteurs de Killing

La métrique ne dépend ni de $t$ ni de $\varphi$ : deux Killing (stationnaire, axisymétrique, **non statique** car $g_{t\varphi}\ne0$)
$$\xi=\partial_t,\qquad\eta=\partial_\varphi,\qquad\xi\cdot\xi=g_{tt}=-\frac{\Delta-a^2\sin^2\theta}{\rho^2},\quad\eta\cdot\eta=g_{\varphi\varphi}=\frac{\Sigma^2\sin^2\theta}{\rho^2}.$$
Intégrales premières de géodésiques : $E=-p_t$, $L=p_\varphi$. **Tenseur de Killing–Yano/Carter** supplémentaire ⇒ constante de Carter $Q$ : le problème est **intégrable** (4 constantes $\mu,E,L,Q$ pour 4 degrés de liberté). Notez : $\partial_t$ et $\partial_\varphi$ forment la sous-algèbre abélienne de $\mathfrak{iso}$ qui se lit dans le torseur $(M,J)$ ([[02_Torseurs_Varignon_generalise]]).

## 5. Surfaces particulières

**Surfaces limites de stationnarité** ($g_{tt}=0$) : $r^2-2mr+a^2\cos^2\theta=0$ ⇒
$$r_{E\pm}(\theta)=m\pm\sqrt{m^2-a^2\cos^2\theta}.$$
**Surfaces $\Delta=0$** : $r_\pm=m\pm\sqrt{m^2-a^2}$ (existent ssi $a\le m$) ; $r_{E+}\ge r_+$ avec égalité aux pôles ($\theta=0,\pi$). Seules les surfaces $\Delta=0$ sont **nulles** : pour $f=r-r_\pm$ : $g^{\mu\nu}\partial_\mu f\partial_\nu f=g^{rr}=\Delta/\rho^2=0$ ; pour $f=r-r_{E\pm}(\theta)$ : $g^{rr}f_r^2+g^{\theta\theta}f_\theta^2\ne0$ (elles sont de genre temps) ⇒ **horizons** : $\mathcal H=\{r=r_+\}$, $\mathcal H_{in}=\{r=r_-\}$ ; **ergosphères** $\mathcal E^\pm=\{r=r_{E\pm}\}$.
**Régions de Boyer–Lindquist** : $\mathcal M_I=\{r>r_+\}$, $\mathcal M_{II}=\{r_-<r<r_+\}$, $\mathcal M_{III}=\{r<r_-\}$ (privée de l'anneau).

## 6. Dragging des repères et ergorégion

Statut du vecteur $\xi$ :
- $\xi$ **temps** si $g_{tt}<0$ : $r>r_{E+}$ ou $r<r_{E-}$ ;
- **nul** sur $\mathcal E^\pm$ ;
- **espace** dans l'**ergorégion** $\mathcal G=\{r_{E-}<r<r_{E+}\}$ (contient tout $\mathcal M_{II}$ car $\Delta<0\Rightarrow g_{tt}>0$).
*Conséquence* : dans $\mathcal G$ aucune particule ne peut rester **statique** ($u^\mu=(u^t,0,0,0)$ donne $g_{tt}(u^t)^2=-1$, impossible si $g_{tt}>0$).
**Vitesses angulaires admissibles.** Pour un observateur $u\propto(1,0,0,\Omega)$ : $g_{tt}+2g_{t\varphi}\Omega+g_{\varphi\varphi}\Omega^2<0$ ⇔ $\Omega_-<\Omega<\Omega_+$,
$$\Omega_\pm=\omega\pm\sqrt{\omega^2-\frac{g_{tt}}{g_{\varphi\varphi}}},\qquad\omega\doteq-\frac{g_{t\varphi}}{g_{\varphi\varphi}}=\frac{2amr}{\Sigma^2}\quad(\text{entraînement des repères}).$$
Pour $g_{tt}<0$ : $\Omega_-<0<\Omega_+$ (observateur statique possible) ; sur $\mathcal E^\pm$ ($g_{tt}=0$) : $\Omega_-=0$ ⇒ **aucun observateur statique**. À l'horizon $\Omega_+=\Omega_-$ : tout observateur tourne avec
$$\boxed{\Omega_H=\omega(r_+)=\frac a{r_+^2+a^2}=\frac a{2mr_+}} .$$
(Vérification : à $\Delta=0$, $\Sigma^2=(r_+^2+a^2)^2$ et $\omega=2amr_+/(r_+^2+a^2)^2=a/(r_+^2+a^2)$ car $r_+^2+a^2=2mr_+$.) Le signe de $a$ donne le sens de rotation.

## 7. « Machine temporelle » de Carter

$\eta\cdot\eta=g_{\varphi\varphi}=\tfrac{\Sigma^2\sin^2\theta}{\rho^2}$ avec $\Sigma^2=(r^2+a^2)(r^2+a^2\cos^2\theta)+2mra^2\sin^2\theta$. $\eta$ est **espace** là où $\Sigma^2>0$ ; $\Sigma^2<0$ exige $r<0$ (si $m>0$) : région $\mathcal T\subset\mathcal M_{III}$ où $\eta$ est de **genre temps**, donc les cercles $t,r,\theta=\text{cte}$ sont des **courbes temporelles fermées** (violation de causalité) ; $\mathcal T$ est située à $r<0$ près de l'anneau, hors de $\mathcal M_I\cup\mathcal M_{II}$ ; bord : $\eta$ nul.

## 8. Géodésiques : Hamilton–Jacobi et constante de Carter

Hamiltonien $H=\tfrac12g^{\mu\nu}p_\mu p_\nu=-\tfrac12\mu^2$ ($\mu=0$ pour la lumière). L'équation de Hamilton–Jacobi $\partial_\tau S+\tfrac12g^{\mu\nu}\partial_\mu S\partial_\nu S=0$ est **séparable** : $S=\tfrac12\mu^2\tau-Et+L\varphi+S_r(r)+S_\theta(\theta)$ (signe choisi pour $p_t=-E$, $p_\varphi=L$). La séparation introduit la **constante de Carter** $\mathcal K$ (ou $Q=\mathcal K-(L-aE)^2$) :
$$\rho^4\dot r^2=R(r)\doteq\big[E(r^2+a^2)-aL\big]^2-\Delta\big[\mu^2r^2+\mathcal K\big],$$
$$\rho^4\dot\theta^2=\Theta(\theta)\doteq\mathcal K-(L-aE\sin^2\theta)^2/\sin^2\theta-\mu^2a^2\cos^2\theta,$$
$$\rho^2\dot\varphi=-\Big(aE-\frac L{\sin^2\theta}\Big)+\frac{aP}\Delta,\quad\rho^2\dot t=-a(aE\sin^2\theta-L)+\frac{(r^2+a^2)P}\Delta,\quad P=E(r^2+a^2)-aL .$$
**Géodésiques nulles principales** ($\mathcal K=0$, $L=aE\sin^2\theta$, $\theta=\text{cte}$) : $\dot r=\pm E$ ; tangentes
$$\ell_\pm=\frac1\Delta\big[(r^2+a^2)\partial_t\pm\Delta\,\partial_r+a\,\partial_\varphi\big],$$
**sortantes ($+$) et entrantes ($-$)**, singulières en $\Delta=0$ (coordonnées) ; régulières en coordonnées de Kerr–Schild ([[14_Kerr_horizons_ergoregion_extension_maximale]]). Ces deux congruences sont les directions principales nulles du tenseur de Weyl (**type D**).
**Orbites circulaires équatoriales** : ISCO de $r=6m$ ($a=0$) à $r=m$ ($a=m$, corotatif) ; $r=9m$ pour contrarotatif.

## 9. Thermodynamique et processus de Penrose

Surface de gravité : $\kappa=\dfrac{r_+-r_-}{2(r_+^2+a^2)}=\dfrac{\sqrt{m^2-a^2}}{2mr_+}$ ; aire de l'horizon : $A=4\pi(r_+^2+a^2)=8\pi mr_+$ ; entropie $S=A/4$ ; température $T_H=\kappa/2\pi$.
**Formule de Smarr** : $M=2\Omega_HJ+\dfrac{\kappa A}{4\pi}$. *Vérification* : $2\Omega_HJ=2\tfrac a{2mr_+}ma=\tfrac{a^2}{r_+}=r_-$ (car $r_+r_-=a^2$) ; $\tfrac{\kappa A}{4\pi}=\tfrac{r_+-r_-}{4mr_+}\cdot2mr_+=\tfrac{r_+-r_-}2$ ; somme $=\tfrac{r_++r_-}2=m$ ✓.
**Premier principe** : $dM=\tfrac\kappa{8\pi}dA+\Omega_HdJ$ (analogue de $dE=TdS+\Omega dJ$ : le moment cinétique $J$ du torseur).
**Processus de Penrose** : dans l'ergorégion, l'énergie conservée $E=-p\cdot\xi$ peut être **négative** (car $\xi$ est de genre espace) ; une particule d'énergie $E_1<0$ tombe dans $\mathcal H$ tandis que l'autre s'échappe avec $E_2=E_0-E_1>E_0$ : **extraction d'énergie rotationnelle**. Limite : masse irréductible $M_{irr}^2=A/16\pi=mr_+/2$, $M^2=M_{irr}^2+\dfrac{J^2}{4M_{irr}^2}$ (vérifié : $\tfrac{mr_+}2+\tfrac{m^2a^2}{2mr_+}=\tfrac m2(r_++r_-)=m^2$ ✓) ; on peut extraire jusqu'à $1-\tfrac1{\sqrt2}\approx29\,\%$ de $M$ ; $\delta A\ge0$ (Hawking) interdit de diminuer $M_{irr}$. **Superradiance** : analogue ondulatoire.
