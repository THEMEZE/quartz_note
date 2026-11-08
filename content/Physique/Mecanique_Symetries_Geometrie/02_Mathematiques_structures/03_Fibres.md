---
title: Fibrés
tags:
  - Mathematiques
  - Fibres
lang: fr
---

> Retour : [[00_Index]] · avant : [[01_Varietes_differentielles]] · [[07_Groupes_de_Lie]] · suite : [[04_Connexions]] · [[05_Cohomologie]]

# Fibrés

**Idée** : une famille d'espaces $F_x$ (« fibres ») paramétrée par $x\in M$, localement un produit $U\times F$ mais pas globalement. Les champs de matière sont des **sections** ; la jauge est le choix d'une trivialisation.

## 1. Fibré, trivialisation, cocycle

**Fibré** $(E,\pi,M,F)$ : variétés $E,M,F$ et submersion $\pi\colon E\to M$ telle que $\forall x$ il existe un voisinage $U$ et un difféomorphisme $\phi_U\colon\pi^{-1}(U)\to U\times F$ avec $\mathrm{pr}_1\circ\phi_U=\pi$ (**trivialisation locale**). Fibre : $E_x=\pi^{-1}(x)\simeq F$.
Si $\{U_\alpha\}$ recouvre $M$, les **fonctions de transition** $g_{\alpha\beta}\colon U_\alpha\cap U_\beta\to G$ ($\phi_\alpha\phi_\beta^{-1}(x,f)=(x,g_{\alpha\beta}(x)f)$) satisfont le **cocycle**
$$
g_{\alpha\beta}\,g_{\beta\gamma}\,g_{\gamma\alpha}=1\ \text{sur }U_\alpha\cap U_\beta\cap U_\gamma,\qquad g_{\alpha\alpha}=1 .
$$
Réciproquement tout cocycle définit un fibré (recollement). Le groupe $G$ est le **groupe de structure**. Deux fibrés sont isomorphes ssi leurs cocycles sont cohomologues (cohomologie de Čech non abélienne $\check H^1(M,G)$, [[05_Cohomologie]]).
**Section** : $s\colon M\to E$ lisse avec $\pi\circ s=\mathrm{id}$ ; $\Gamma(E)$ ses sections ; $s_\alpha=\phi_\alpha\circ s=(x,\sigma_\alpha(x))$, $\sigma_\alpha=g_{\alpha\beta}\sigma_\beta$.

## 2. Fibrés vectoriels

Fibre $F=\mathbb K^r$ (espace vectoriel), $G\subset GL(r,\mathbb K)$. Exemples :
- **tangent** $TM$, **cotangent** $T^\ast M$, $\Lambda^pT^\ast M$ (formes, [[02_Formes_differentielles_calcul_exterieur]]), $T^{(r,s)}M$ (tenseurs) ; transition = jacobiennes ;
- fibré trivial $M\times\mathbb K^r$ ; ruban de Möbius (non trivial, $G=\mathbb Z_2$) ;
- **fibré en droites** $L$ (rang 1) : $c_1(L)\in H^2(M,\mathbb Z)$ ;
- **fibré des spineurs** $S\to M$ ([[09_Algebres_de_Clifford_spineurs]]) ;
- fibré des fonctions d'onde à valeurs dans une représentation ($\psi\in\Gamma(P\times_G V)$).
Opérations : somme directe $\oplus$, produit tensoriel $\otimes$, dual, pull-back $f^\ast E$, fibrés $\mathrm{End}(E)=E\otimes E^\ast$, $\Lambda^kE$.
Un fibré vectoriel est **trivial** ssi il possède $r$ sections linéairement indépendantes (ex. $TS^2$ non trivial : théorème de la boule chevelue, $\chi(S^2)=2\ne0$).

## 3. Fibrés principaux

**Définition.** Un **$G$-fibré principal** $P\xrightarrow{\pi}M$ est un fibré de fibre $G$ muni d'une action libre à droite $P\times G\to P$, $(p,g)\mapsto pg$, dont les orbites sont exactement les fibres, localement triviale : $\pi^{-1}(U)\simeq U\times G$ équivariant. Une **section locale** $s_U\colon U\to P$ ⇔ trivialisation ⇔ **choix de jauge**. Changement de jauge : $s_\beta=s_\alpha\,g_{\alpha\beta}$.
Un fibré principal est trivial ssi il possède une section **globale** (c'est pourquoi une théorie de jauge non triviale n'admet pas de potentiel $A$ global).

**Exemples.**
| Fibré principal | Base | Groupe | Physique |
|---|---|---|---|
| $\mathrm{Fr}(M)$, repères de $TM$ | $M$ | $GL(n,\mathbb R)$ | gravité (connexion affine) |
| $\mathrm{Fr}_O(M)$, repères orthonormés | $(M,g)$ | $O(n)$ ou $SO(1,3)$ | tétrades, spin connexion |
| $\mathrm{Spin}(M)\to\mathrm{Fr}_{SO}(M)$ | $M$ | $Spin(n)$ | spineurs |
| Hopf $S^3\to S^2$ | $S^2$ | $U(1)$ | monopôle de Dirac |
| $G\to G/H$ | $G/H$ | $H$ | espaces homogènes |
| fibré de jauge | espace-temps | $U(1),SU(2),SU(3)$ | EM, électrofaible, QCD |
| fibré de Poincaré | espace-temps | $ISO(1,3)$ | gravité de Cartan ([[03_Jauge_EM_YM_Gravite]]) |

**Hopf** : $S^3=\{(z_1,z_2)\in\mathbb C^2,|z|^2=1\}\to\mathbb{CP}^1=S^2$, $(z_1,z_2)\mapsto[z_1:z_2]$, de fibre $U(1)$ (multiplication par $e^{i\alpha}$). Non trivial car $S^3\not\simeq S^2\times S^1$. $c_1=\pm1$ : charge magnétique $1$.

## 4. Fibrés associés

$P$ un $G$-fibré principal, $\rho\colon G\to GL(V)$ une représentation. Le **fibré associé** est
$$
E=P\times_GV\doteq(P\times V)/\{(p,v)\sim(pg,\rho(g^{-1})v)\}.
$$
Ses sections s'identifient aux fonctions **équivariantes** $\tilde\psi\colon P\to V$, $\tilde\psi(pg)=\rho(g)^{-1}\tilde\psi(p)$ ; relues en jauge $s$ : $\psi=\tilde\psi\circ s$, et $\psi'=\rho(g^{-1})\psi$ sous $s'=sg$. Cas : $\rho=\mathrm{Ad}$ ⇒ $\mathrm{Ad}\,P$ (fibré en algèbres de Lie) ; $\rho=$ représentation de spin ⇒ fibré des spineurs.
**Les champs de matière sont des sections de fibrés associés ; le champ de jauge est une connexion sur $P$** ([[04_Connexions]]).

## 5. Transformations de jauge, suite d'Atiyah

- **Groupe de jauge** $\mathcal G=\mathrm{Aut}_{\text{vert}}(P)\simeq\Gamma(P\times_{\mathrm{Ad}}G)$ : difféomorphismes $\Phi\colon P\to P$ équivariants couvrant $\mathrm{id}_M$. En jauge : $g\colon M\to G$.
- **Algèbre de jauge** : $\Gamma(\mathrm{Ad}P)$, $\xi\colon M\to\mathfrak g$.
- **Suite d'Atiyah** (exacte, de fibrés vectoriels sur $M$) :
$$0\longrightarrow\mathrm{Ad}P\longrightarrow TP/G\xrightarrow{\ \pi_\ast\ }TM\longrightarrow0 .$$
Une **connexion** est un scindement de cette suite ; la courbure en mesure l'obstruction à l'intégrabilité ([[04_Connexions]]). Pour $P=\mathrm{Fr}_O(M)$ : $\mathrm{Ad}P=\mathfrak{so}(TM)$ (bivecteurs, cf. moments, [[02_Torseurs_Varignon_generalise]]) et $TP/G$ est le **fibré de Atiyah** de la gravité de Cartan : une connexion de Cartan est un scindement avec la torsion $T$ en plus.

## 6. Classification, classes caractéristiques

- Les $G$-fibrés principaux sur $M$ sont classés (à iso près) par $[M,BG]$ (espace classifiant, $BU(1)=\mathbb{CP}^\infty$, $BSU(2)=\mathbb{HP}^\infty$).
- **Classes caractéristiques** (Chern, Pontryagin, Stiefel–Whitney, Euler) : éléments de $H^\ast(M)$ construits à partir de la courbure par Chern–Weil ([[04_Connexions]], [[05_Cohomologie]]) ; ex. $c_1(L)=\big[\tfrac i{2\pi}F\big]$, quantification de la charge de Dirac $\tfrac{1}{2\pi}\int_{S^2}F=n\in\mathbb Z$.
- **Réduction du groupe de structure** : une métrique réduit $GL(n)\to O(n)$ ; une orientation $O\to SO$ ; une structure de spin relève $SO\to Spin$ (obstruction $w_2(M)\in H^2(M,\mathbb Z_2)$) ; une structure presque complexe $GL(2n,\mathbb R)\to GL(n,\mathbb C)$ ; holonomie spéciale $SU(3)$ (Calabi–Yau), $G_2$ (théorie M, [[04_Cordes_et_theorie_M]]).

## 7. Superfibrés (renvoi)

En supergravité la connexion est valeur dans l'algèbre de **super-Poincaré** ([[01_Supersymetrie]], [[02_Supergravite_connexion_courbure]]) : un **supergroupe** de structure et une base supervariété (coordonnées de Grassmann $\theta$).
