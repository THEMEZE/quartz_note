---
title: Théories de jauge — électromagnétisme, Yang–Mills, gravité
tags:
  - Physique
  - Jauge
lang: fr
---

> Retour : [[00_Index]] · maths : [[03_Fibres]], [[04_Connexions]], [[07_Groupes_de_Lie]], [[02_Formes_differentielles_calcul_exterieur]] · suite : [[10_Relativite_generale_equations_Einstein]], [[02_Supergravite_connexion_courbure]]
> Version corrigée et unifiée des notes *Quelques notations pour théorie de jauge*, *Théorie de jauge (EM, YM)*, *Théories de jauge : EM et analogies gravitationnelles* (erreurs relevées dans [[99_Errata_des_notes_importees]]).

# Théories de jauge : $U(1)$, $SU(N)$, gravité

## 1. Dictionnaire des symboles

| Symbole | Sens | Remarque |
|---|---|---|
| $d$ | dérivée extérieure, $d^2=0$ | ne dépend d'aucune structure |
| $\wedge$ | produit extérieur, $dx^\mu\wedge dx^\nu=-dx^\nu\wedge dx^\mu$ | aire orientée ; pour des formes matricielles $A\wedge A=\tfrac12[A,A]$ (non nul si non abélien) |
| $[X,Y]=XY-YX$ | crochet de Lie des champs | défaut de commutation des flots |
| $T_{[\mu\nu]}=\tfrac12(T_{\mu\nu}-T_{\nu\mu})$ | antisymétrisation **normalisée** | pour trois indices : $T_{[\mu\nu\rho]}=\tfrac1{3!}\sum_\sigma\mathrm{sgn}\,\sigma\,T_{\sigma(\mu\nu\rho)}$ |
| $\nabla$ | dérivée covariante (tenseurs) | dépend de $\Gamma$ |
| $D=d+A$ | dérivée covariante extérieure | $D^2=F$ |

**Correction** : $\partial_{[\mu}F_{\nu\rho]}=\tfrac13(\partial_\mu F_{\nu\rho}+\partial_\nu F_{\rho\mu}+\partial_\rho F_{\mu\nu})$ ; la somme cyclique sans facteur $\tfrac13$ n'est pas égale au symbole $[\ ]$ défini avec le facteur $\tfrac12$. L'identité $dF=0$ s'écrit indifféremment $\partial_\mu F_{\nu\rho}+\partial_\nu F_{\rho\mu}+\partial_\rho F_{\mu\nu}=0$.

## 2. Structure unifiée « connexion → courbure → Bianchi »

Connexion $\mathcal A$ sur un fibré principal ([[04_Connexions]]), courbure $\mathcal F=d\mathcal A+\tfrac12[\mathcal A,\mathcal A]=D^2$, identité de Bianchi $D\mathcal F=0$, équations du mouvement $D\star\mathcal F=\star J$ (théories de jauge **internes**).

| | EM | Yang–Mills | Gravité (Cartan) |
|---|---|---|---|
| Groupe de jauge | $U(1)$ (abélien) | $SU(N)$ (non ab.) | $SO(1,3)$ local (ou $ISO(1,3)$ de Cartan) |
| Connexion | $A=A_\mu dx^\mu$ | $A=A^a_\mu T_adx^\mu$ | $(e^a,\omega^{ab})$ |
| Courbure | $F=dA$ | $F=dA+A\wedge A$ | $T^a=de^a+\omega^a{}_b\wedge e^b$, $R^{ab}=d\omega^{ab}+\omega^a{}_c\wedge\omega^{cb}$ |
| Bianchi | $dF=0$ | $DF=0$ | $DR^{ab}=0$, $DT^a=R^a{}_b\wedge e^b$ ; en indices $\nabla_{[\lambda}R_{\mu\nu]\rho\sigma}=0$ |
| Dynamique | $d\star F=\star J$ | $D\star F=\star J$ | $G_{\mu\nu}+\Lambda g_{\mu\nu}=\kappa\,T_{\mu\nu}$ (Einstein) ; Einstein–Cartan si torsion |
| Boson (quantum) | photon, spin 1 | $N^2-1$ gluons/W/Z…, spin 1 | graviton, spin 2 |
| Auto-interaction | non | oui ($[A,\star F]$) | oui (non linéaire) |
| Portée | infinie ($m_\gamma=0$) | **confinement** pour $SU(3)$ de QCD ; massifs $W,Z$ par Higgs | infinie |

**Corrections** : (i) la portée d'une théorie de Yang–Mills n'est **pas** « infinie sans brisure » : les gluons, quoique de masse nulle dans le lagrangien, sont **confinés** (échelle $\Lambda_{QCD}$) ; (ii) la loi de gravité n'est pas « $D\star R=\star T$ » (voir §5).

## 3. Électromagnétisme

$F=dA$, $A\mapsto A+d\lambda$. En composantes $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$, $dF=0$ ⇔ Faraday + $\nabla\!\cdot\vec B=0$ ; $d\star F=\star J$ ⇔ Gauss + Ampère–Maxwell. Action $S=-\tfrac14\int F_{\mu\nu}F^{\mu\nu}d^4x+\int A_\mu J^\mu$. Couplage minimal $D_\mu=\partial_\mu-iqA_\mu/\hbar$ ; $[D_\mu,D_\nu]=-\tfrac{iq}\hbar F_{\mu\nu}$. Phase d'Aharonov–Bohm = holonomie $\exp(\tfrac{iq}\hbar\oint A)$ : **observable non locale, sensible à la topologie**.

## 4. Yang–Mills

$A_\mu=A^a_\mu T_a$, $F^a_{\mu\nu}=\partial_\mu A^a_\nu-\partial_\nu A^a_\mu+f_{bc}{}^aA^b_\mu A^c_\nu$, $\mathcal L=-\tfrac1{4g^2}F^a_{\mu\nu}F^{a\mu\nu}$, $D_\mu F^{\mu\nu}=J^\nu$ ; $\dim SU(N)=N^2-1$. Jauge : $A\mapsto g^{-1}Ag+g^{-1}dg$, $F\mapsto g^{-1}Fg$. Modèle standard : $SU(3)\times SU(2)\times U(1)$. **Instantons** : $F=\pm\star F$ minimisent l'action, charge topologique $\tfrac1{8\pi^2}\int\operatorname{tr}F\wedge F\in\mathbb Z$ ([[05_Cohomologie]]).

## 5. Gravité comme jauge de Poincaré

Connexion de Cartan $\mathcal A=e^aP_a+\tfrac12\omega^{ab}J_{ab}$ à valeurs dans $\mathfrak{iso}(1,3)$ ($[P_a,P_b]=0$, $[J_{ab},P_c]=\eta_{bc}P_a-\eta_{ac}P_b$) ; courbure $\mathcal F=T^aP_a+\tfrac12R^{ab}J_{ab}$. Action d'Einstein–Cartan–Palatini
$$S[e,\omega]=\frac1{4\kappa^2}\int\varepsilon_{abcd}\,e^a\wedge e^b\wedge R^{cd}+S_{\text{mat}},\qquad\kappa^2=8\pi G .$$
Variations :
- $\delta\omega$ : $\varepsilon_{abcd}\,e^c\wedge T^d\propto\kappa^2\sigma_{ab}$ (densité de spin ; vide : $T=0$, $\omega=\omega(e)$ de Levi-Civita) ;
- $\delta e$ : $\varepsilon_{abcd}\,e^b\wedge R^{cd}\propto\kappa^2\tau_a$ (énergie-impulsion) ⇒ équations d'Einstein.
Les deux équations ci-dessus remplacent la formule erronée « $D\star R=\star T$ ». **Dictionnaire torseur** : sources $(\tau_a;\sigma_{ab})$ = résultante + moment ([[02_Torseurs_Varignon_generalise]]) ; $(T^a;R^{ab})$ = courbure de translations + rotations. Tableau détaillé : [[10_Relativite_generale_equations_Einstein]].

## 6. Noether et jauge

Une symétrie **globale** donne une charge ([[05_Lagrange_Hamilton_Noether]]) ; **locale** : identités de Noether (II) : Gauss $\partial_\mu J^\mu=0$ (EM), $D_\mu J^\mu=0$ (YM), $\nabla_\mu T^{\mu\nu}=0$ (difféos, Bianchi contractée). Les théories de jauge sont **à contraintes** (premiers classes, Dirac) : $\nabla\!\cdot\vec E=\rho$, et $\mathcal H\approx0$ en gravité ([[03_Gravitation_quantique]]).
