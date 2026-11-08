---
title: Supergravité — connexion, courbure, actions, MacDowell–Mansouri
tags:
  - Physique
  - Supergravite
lang: fr
---

> Retour : [[00_Index]] · avant : [[01_Supersymetrie]], [[02_Supergravite_resume]], [[04_Connexions]], [[08_Algebres_graduees_ideaux_superalgebres]] · suite : [[03_Gravitation_quantique]], [[04_Cordes_et_theorie_M]]
> Version corrigée et complétée de la note *Supergravité* (conventions de signes variables selon les auteurs : les coefficients numériques sont donnés **à convention près**).

# Supergravité comme théorie de jauge du super-Poincaré

## 1. Connexion de super-Poincaré

Super-algèbre : $[P,P]=0$, $[J_{ab},P_c]=\eta_{bc}P_a-\eta_{ac}P_b$, $[J_{ab},Q]=-\tfrac12\gamma_{ab}Q$, $[P_a,Q]=0$, $\{Q_\alpha,Q_\beta\}=(\gamma^aC)_{\alpha\beta}P_a$ ($\mathcal N=1$, $D=4$ Majorana). Connexion
$$\mathcal A=\tfrac12\omega^{ab}J_{ab}+e^aP_a+\bar\psi Q,$$
$\omega^{ab}$ : jauge de Lorentz, $e^a$ : jauge des translations (vielbein), $\psi$ : jauge de SUSY, **gravitino** (spin 3/2, **pas « gravition »**).
**Courbure** $\mathcal F=d\mathcal A+\tfrac12[\mathcal A,\mathcal A\}=\tfrac12R^{ab}J_{ab}+T^aP_a+\bar\rho\,Q$ :
$$R^{ab}=d\omega^{ab}+\omega^a{}_c\wedge\omega^{cb},\qquad T^a=de^a+\omega^a{}_b\wedge e^b-\tfrac12\bar\psi\wedge\gamma^a\psi,\qquad\rho=D\psi=d\psi+\tfrac14\omega^{ab}\gamma_{ab}\psi .$$
Le terme $\bar\psi\gamma^a\psi$ dans la torsion vient de $\{Q,Q\}\sim P$ : **la torsion est sourcée par le courant fermionique** ; $T^a=0$ (supergravité 1.5 ordre : $\omega=\omega(e,\psi)$ en résolvant la contrainte).
**Table** : $R^{ab}$ ↔ rotations de Lorentz ; $T^a$ ↔ translations ; $\rho$ ↔ supertranslations.

## 2. Bianchi

$D\mathcal F=0$ se décompose :
$$DR^{ab}=0,\qquad DT^a=R^a{}_b\wedge e^b-\bar\psi\wedge\gamma^a\rho\ (\text{à conv. près}),\qquad D\rho=\tfrac14R^{ab}\gamma_{ab}\wedge\psi .$$
La dernière relation généralise $[D_\mu,D_\nu]\epsilon=\tfrac14R_{\mu\nu}{}^{ab}\gamma_{ab}\epsilon$ ([[04_Connexions]]).

## 3. Symétries locales

$\delta e^a=\bar\epsilon\gamma^a\psi$ (à $\tfrac12$ près), $\delta\psi=D\epsilon$, $\delta\omega=\dots$. **Algèbre fermée** : $[\delta_{\epsilon_1},\delta_{\epsilon_2}]=\delta_{\text{diff}}(\xi^\mu=\tfrac12\bar\epsilon_2\gamma^\mu\epsilon_1)+\delta_{\text{Lorentz}}+\delta_{\text{SUSY}}$ : deux SUSY locales font un difféomorphisme. C'est ce qui fait de la sugra une théorie de **gravité**.

## 4. Action (formulation en formes, 4D $\mathcal N=1$)

$$S=\frac1{4\kappa^2}\int\varepsilon_{abcd}\,e^a\wedge e^b\wedge R^{cd}\;-\;\frac1{\kappa^2}\int\bar\psi\wedge\gamma_5\gamma_a\,D\psi\wedge e^a\quad(\text{coefficients à convention près}).$$
(La note importée écrivait $\bar\psi\wedge\gamma_5\gamma\wedge D\psi$ sans $e^a$ ; il faut $\gamma_a\,e^a$ pour que la 4-forme soit bien définie : $\psi$ et $D\psi$ de degrés $1$ et $2$, $e^a$ de degré $1$.) Premier terme : Einstein–Hilbert ; second : **Rarita–Schwinger** couplé. Équations : (i) Einstein avec source $T_{\mu\nu}^{(\psi)}$ ; (ii) $\varepsilon^{\mu\nu\rho\sigma}\gamma_5\gamma_\nu D_\rho\psi_\sigma=0$ (équation du gravitino).

## 5. Constante cosmologique, MacDowell–Mansouri

Pour $\Lambda<0$ : jauge $\mathfrak{so}(3,2)=\mathfrak{sp}(4,\mathbb R)\supset\mathfrak{so}(3,1)$. Connexion $\mathcal A^{AB}$ avec $\mathcal A^{ab}=\omega^{ab}$, $\mathcal A^{a4}=e^a/\ell$ ; courbure $\mathcal F^{ab}=R^{ab}-\tfrac1{\ell^2}e^a\wedge e^b$, $\mathcal F^{a4}=T^a/\ell$. **Action de MacDowell–Mansouri**
$$S_{MM}\propto\int\varepsilon_{abcd}\,\mathcal F^{ab}\wedge\mathcal F^{cd}=\int\varepsilon_{abcd}\Big(R^{ab}R^{cd}-\tfrac2{\ell^2}R^{ab}e^ce^d+\tfrac1{\ell^4}e^ae^be^ce^d\Big)$$
= (terme topologique de Gauss–Bonnet) $+$ Einstein–Hilbert $+$ $\Lambda$ avec $\Lambda=-3/\ell^2$ : gravité comme théorie de jauge $SO(3,2)$ **brisée** à $SO(3,1)$ par le choix de $e^a=\mathcal A^{a4}\ell$. **Super-version** : $\mathfrak{osp}(1|4)$ ([[08_Algebres_graduees_ideaux_superalgebres]]) ⇒ sugra AdS $\mathcal N=1$ ; supergroupe de jauge $OSp(\mathcal N|4)$.

## 6. Géométrie de Cartan, fibrés principaux

Une **géométrie de Cartan** modelée sur $G/H$ est un $H$-fibré $P\to M$ avec une 1-forme $\omega\in\Omega^1(P,\mathfrak g)$ **isomorphisme** $T_pP\to\mathfrak g$ sur chaque fibre ([[03_Fibres]]). Sa courbure $\Omega=d\omega+\tfrac12[\omega,\omega]$ :
- modèle $G/H=ISO(1,3)/SO(1,3)$ ⇒ **Einstein–Cartan** ($\omega=(e,\omega^{ab})$, $\Omega=(T,R)$) ;
- modèle $SO(3,2)/SO(3,1)$ ⇒ MacDowell–Mansouri ;
- modèle super ⇒ supergravité.
La différence avec une théorie de jauge ordinaire : $e^a$ n'est pas indépendant, c'est l'**identification** $\mathfrak g/\mathfrak h\simeq T_xM$ (le fibré tangent).

## 7. Liens avec le 11D et la forme $C$

Sugra 11D : $(e^a,\omega^{ab},\psi;\,C_3)$ avec $G_4=dC_3$, $dG_4=0$ (Bianchi), action
$$S=\frac1{2\kappa_{11}^2}\int\Big(R\star1-\tfrac12G_4\wedge\star G_4-\tfrac16C_3\wedge G_4\wedge G_4\Big)+\text{fermions}.$$
**La note importée omettait** les coefficients $\tfrac1{2\kappa^2}$, $\tfrac12$ et $\tfrac16$ et le $\star$ de $|G_4|^2=G_4\wedge\star G_4$. Équation du mouvement : $d\star G_4+\tfrac12G_4\wedge G_4=0$ ; **dual** $C_6$ : $G_7=dC_6+\tfrac12C_3\wedge G_4=\star G_4$.
Les **branes** sont des sources/des charges de $C$ : la M2 se couple électriquement à $C_3$ ($\mu_2\int_{M2}C_3$), la M5 magnétiquement (à $C_6$) ; charges centrales $Z_2$, $Z_5$ de $\{Q,Q\}$ ([[01_Supersymetrie]], [[04_Cordes_et_theorie_M]]). Réduction sur $S^1$ : $G_4\to F_4,H_3$, $C_3\to C_3,B_2$ (IIA), $g_{11}\to$ photon $C_1$.

## 8. Hiérarchie de géométries (corrigée)

| Théorie | Champ de jauge | Courbure | Identités |
|---|---|---|---|
| EM | $A$ | $F=dA$ | $dF=0$ |
| YM | $A$ | $F$ | $DF=0$ |
| GR (Cartan) | $(e,\omega)$ | $(T,R)$ | $DR=0$, $DT=R\wedge e$ |
| SUGRA | $(e,\omega,\psi)$ | $(T,R,\rho)$ | $D\mathcal F=0$ |
| sugra 11D / théorie M | $(e,\omega,\psi,C_3,C_6)$ | $G_4$, $G_7$ | $dG_4=0$ |
