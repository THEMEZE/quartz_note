---
title: Variétés différentielles
tags:
  - Mathematiques
  - Geometrie-differentielle
lang: fr
---

> Retour : [[00_Index]] · suite : [[02_Formes_differentielles_calcul_exterieur]] · [[03_Fibres]] · [[04_Connexions]]

# Variétés différentielles

**Rôle dans le projet** : l'espace des configurations $Q$ d'un système mécanique ([[05_Lagrange_Hamilton_Noether]]), l'espace-temps $(M,g)$ de la relativité ([[10_Relativite_generale_equations_Einstein]]) et l'espace des phases $T^\ast Q$ sont des variétés ; tous les objets (torseurs, champs, connexions) y vivent.

## 1. Définitions

**Variété topologique** de dimension $n$ : espace topologique $M$ séparé, à base dénombrable, localement homéomorphe à $\mathbb R^n$. **Carte** $(U,\varphi)$ : $\varphi\colon U\to\varphi(U)\subset\mathbb R^n$ homéomorphisme ; **atlas** $\{(U_\alpha,\varphi_\alpha)\}$ de recouvrement. Changements de cartes $\varphi_\beta\circ\varphi_\alpha^{-1}$.

**Structure différentiable** ($C^\infty$) : atlas dont tous les changements de cartes sont $C^\infty$, pris maximal. Une application $f\colon M\to N$ est lisse si ses lectures en cartes le sont ; **difféomorphisme** : bijection lisse d'inverse lisse.

Exemples : $\mathbb R^n$, sphères $S^n$ (2 cartes stéréographiques), tores $T^n=(S^1)^n$, espaces projectifs $\mathbb{RP}^n$, graphes, groupes de Lie ($SO(3)\simeq\mathbb{RP}^3$, [[07_Groupes_de_Lie]]), espace des configurations d'un solide $E(3)$, fibrés (voir [[03_Fibres]]).

**Fonctions plateaux et partitions de l'unité** : toute variété lisse paracompacte admet une partition de l'unité subordonnée à un recouvrement ; conséquence : existence de métriques riemanniennes, de connexions, de formes volume (si orientable), d'intégrales globales.

**Théorème de Whitney** : toute variété lisse de dimension $n$ se plonge dans $\mathbb R^{2n}$. Une variété est une sous-variété d'un espace euclidien : $M=\{F=0\}$ avec $dF$ de rang maximal (théorème des valeurs régulières, cf. [[02_Geometrie_metrique_operateurs]] §I.4–I.5).

## 2. Espace tangent, cotangent

Trois définitions équivalentes de $T_pM$ ($\dim=n$) :
1. classes de courbes $\gamma\colon(-\epsilon,\epsilon)\to M$, $\gamma(0)=p$, de même vitesse en carte ;
2. **dérivations** $v\colon C^\infty(M)\to\mathbb R$, $v(fg)=f(p)v(g)+g(p)v(f)$ ;
3. vecteurs-colonnes $v^i$ qui se transforment par la jacobienne : $v'^i=\tfrac{\partial q'^i}{\partial q^j}v^j$.

Base naturelle $\partial_i=\partial/\partial q^i$. **Cotangent** $T_p^\ast M$ : base duale $dq^i$. **Différentielle** d'une application : $df_p\colon T_pM\to T_{f(p)}N$.
Fibrés : $TM=\bigsqcup T_pM$ et $T^\ast M$ sont des variétés de dimension $2n$ ($T^\ast Q$ = espace des phases, 1-forme de Liouville $\theta=p_i\,dq^i$, forme symplectique $\omega=d\theta=dp_i\wedge dq^i$).

**Immersion** ($df$ injective), **submersion** ($df$ surjective), **plongement** (immersion + homéomorphisme sur l'image). Pour une submersion, les fibres $f^{-1}(c)$ sont des sous-variétés.

## 3. Champs de vecteurs, flot, crochet de Lie

Un champ $X\in\mathfrak X(M)$ est une section lisse de $TM$ ; $X=X^i\partial_i$ agit sur $C^\infty(M)$ par $X(f)=X^i\partial_if$.
**Flot** $\phi^X_t$ : $\tfrac d{dt}\phi^X_t(p)=X(\phi^X_t(p))$ (groupe à un paramètre local ; global si $M$ compacte).
**Crochet de Lie** : $[X,Y]\doteq XY-YX$, i.e. $[X,Y]^i=X^j\partial_jY^i-Y^j\partial_jX^i$. Propriétés : bilinéaire, antisymétrique, **Jacobi** $[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0$ : $\mathfrak X(M)$ est une algèbre de Lie de dimension infinie ([[06_Algebres_de_Lie]]).
**Dérivée de Lie** : $\mathcal L_XY=\tfrac d{dt}\big|_0(\phi^X_{-t})_\ast Y=[X,Y]$ ; pour un tenseur $T$ : $\mathcal L_XT=\tfrac d{dt}|_0(\phi^X_t)^\ast T$.
**Interprétation du crochet** : $[X,Y]$ mesure le défaut de fermeture du parallélogramme $\phi^X_s\phi^Y_t\phi^X_{-s}\phi^Y_{-t}$ ; $[X,Y]=0$ ssi les flots commutent.
**Théorème de Frobenius** : une distribution $D\subset TM$ de rang $k$ est intégrable (feuilletage) ssi $[D,D]\subset D$. Équivalent, côté formes : l'idéal différentiel engendré par les 1-formes annulant $D$ est stable par $d$ ([[08_Algebres_graduees_ideaux_superalgebres]]).

**Vecteur de Killing** : $\mathcal L_\xi g=0$ ($\nabla_{(\mu}\xi_{\nu)}=0$). Tout Killing donne un invariant le long des géodésiques : $p\cdot\xi=\text{cte}$ (Noether géométrique, [[05_Lagrange_Hamilton_Noether]]). Exemples : $\partial_t,\partial_\varphi$ pour Schwarzschild/Kerr ([[11_Schwarzschild_trou_noir]], [[13_Kerr_trou_noir_en_rotation]]).

## 4. Tenseurs, tirés en arrière

Un tenseur de type $(r,s)$ : section de $(TM)^{\otimes r}\otimes(T^\ast M)^{\otimes s}$. Pour $f\colon M\to N$ : **pull-back** $f^\ast\alpha(v_1,\dots)=\alpha(df\,v_1,\dots)$ de tout tenseur covariant ; **push-forward** $f_\ast X$ des vecteurs (si $f$ difféo). Propriétés : $f^\ast(\alpha\wedge\beta)=f^\ast\alpha\wedge f^\ast\beta$, $f^\ast d=d f^\ast$ ([[02_Formes_differentielles_calcul_exterieur]]).
**Métrique riemannienne** : section $g$ de $S^2T^\ast M$ définie positive ; **pseudo-riemannienne** : non dégénérée de signature $(p,q)$ ; **lorentzienne** $(-+\cdots+)$. Toute variété paracompacte admet une métrique riemannienne ; l'existence d'une lorentzienne exige un champ de lignes non nul (caractéristique d'Euler nulle en compact).

## 5. Orientation, intégration, Stokes

Orientable ssi il existe une $n$-forme sans zéro ($\mathrm{vol}$). Pour $\omega$ de degré $n$ à support compact : $\int_M\omega$ est défini par partition de l'unité, indépendant de la carte (à orientation fixée).

> **Théorème de Stokes.** $M$ orientée de dimension $n$ à bord $\partial M$ (orienté par la normale sortante), $\alpha\in\Omega^{n-1}_c(M)$ : $\displaystyle\int_Md\alpha=\int_{\partial M}\alpha .$

Cas particuliers : théorème fondamental, Green, Kelvin–Stokes, Ostrogradski ($\int\operatorname{div}v\,dV=\oint v\cdot dS$, [[02_Geometrie_metrique_operateurs]]), théorème de la divergence de surface.

## 6. Structures supplémentaires utiles

| Structure | Donnée | Exemple mécanique/physique |
|---|---|---|
| riemannienne | $g$ définie positive | énergie cinétique $T=\tfrac12g(\dot q,\dot q)$ |
| lorentzienne | $g$ signature $(-+++)$ | espace-temps |
| symplectique | $\omega$ fermée non dégénérée | $T^\ast Q$, crochet de Poisson |
| de contact, de Poisson | généralisations | thermodynamique, systèmes dégénérés |
| complexe, kählérienne | $J$, $g$, $\omega$ compatibles | espaces de Calabi–Yau (théorie M) |
| spin | relèvement du fibré des repères à $Spin$ | spineurs ([[09_Algebres_de_Clifford_spineurs]]) |
| groupe de Lie | variété + groupe | symétries ([[07_Groupes_de_Lie]]) |

**Variété symplectique** $(M^{2n},\omega)$ : $d\omega=0$, $\omega$ non dégénérée. Hamiltonien $H$ : $\iota_{X_H}\omega=-dH$ ; $\{f,g\}=\omega(X_f,X_g)$ ; **Darboux** : localement $\omega=dp_i\wedge dq^i$ ; le flot hamiltonien préserve $\omega$ et $\omega^n/n!$ (Liouville).

## 7. Exercices

1. Montrer que $S^n$ n'est pas contractile ($H^n_{dR}(S^n)=\mathbb R$, [[05_Cohomologie]]) mais que $\mathbb R^n$ l'est.
2. Calculer $[\partial_x,\,x\partial_y]$ ; en déduire que $\{\partial_x,x\partial_y,\partial_y\}$ engendre l'algèbre de Heisenberg.
3. Vérifier que $\xi=-y\partial_x+x\partial_y$ est de Killing pour $\mathbb R^2$ et que son flot est la rotation.
