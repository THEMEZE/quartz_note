---
title: Détermination de la métrique de Schwarzschild et propriétés
tags:
  - Physique
  - Relativite-generale
  - Trous-noirs
lang: fr
---

> Retour : [[00_Index]] · avant : [[10_Relativite_generale_equations_Einstein]] · suite : [[12_Coordonnees_EF_Kruskal_Penrose_extension_maximale]] · [[13_Kerr_trou_noir_en_rotation]]
> Inspiré de *P.B. : Extension maximale de l'espace-temps de Schwarzschild et de Kerr* (annexes A, B). Unités $G=c=1$.

# La métrique de Schwarzschild

## 1. Espace-temps statique à symétrie sphérique

**Statique** : (i) coordonnées où $g_{\mu\nu}$ est indépendante de $t$ ; (ii) invariance par $t\mapsto-t$ (le vecteur de Killing $\partial_t$ est orthogonal aux hypersurfaces $t=\text{cte}$). Si seule (i) : **stationnaire** (Kerr).
**Symétrie sphérique** : invariance par $SO(3)$ ; les seuls invariants construits avec $x\cdot x=r^2$, $x\cdot dx=r\,dr$, $dx\cdot dx$ donnent la forme générale
$$ds^2=-A_0(r)dt^2+A_1(r)\,r\,dt\,dr+A_2(r)\,r^2dr^2+A_3(r)\big(dr^2+r^2d\Omega^2\big),\quad d\Omega^2=d\theta^2+\sin^2\theta\,d\varphi^2 .$$
On redéfinit $\tilde r^2=A_3r^2$ (rayon aire) puis $t\mapsto\tilde t$ pour éliminer $dt\,dr$ ($d\tilde t=G(r)[A_0dt-\tfrac12A_1r\,dr]$ intégrable). Résultat :
$$\boxed{ds^2=-A(r)\,dt^2+B(r)\,dr^2+r^2d\Omega^2},\qquad A,B>0\ \text{de classe }C^2 .\tag{1}$$

## 2. Courbure de la forme (1)

Posons $A=e^{2\alpha}$, $B=e^{2\beta}$. Les symboles de Christoffel non nuls (calcul direct) :
$$\Gamma^t_{tr}=\alpha',\ \Gamma^r_{tt}=\alpha'e^{2(\alpha-\beta)},\ \Gamma^r_{rr}=\beta',\ \Gamma^r_{\theta\theta}=-re^{-2\beta},\ \Gamma^r_{\varphi\varphi}=-re^{-2\beta}\sin^2\theta,$$
$$\Gamma^\theta_{r\theta}=\Gamma^\varphi_{r\varphi}=\tfrac1r,\ \Gamma^\theta_{\varphi\varphi}=-\sin\theta\cos\theta,\ \Gamma^\varphi_{\theta\varphi}=\cot\theta .$$
Ricci (seules les composantes diagonales sont non nulles ; ce sont $R_{\sigma\nu}=\partial_\rho\Gamma^\rho_{\nu\sigma}-\partial_\nu\Gamma^\rho_{\rho\sigma}+\Gamma^\rho_{\rho\lambda}\Gamma^\lambda_{\nu\sigma}-\Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\rho\sigma}$) :
$$R_{tt}=e^{2(\alpha-\beta)}\Big[\alpha''+\alpha'^2-\alpha'\beta'+\tfrac{2\alpha'}r\Big],\quad R_{rr}=-\alpha''-\alpha'^2+\alpha'\beta'+\tfrac{2\beta'}r,$$
$$R_{\theta\theta}=e^{-2\beta}\big[r(\beta'-\alpha')-1\big]+1,\qquad R_{\varphi\varphi}=\sin^2\theta\,R_{\theta\theta}.$$

## 3. Résolution du vide ($R_{\mu\nu}=\Lambda g_{\mu\nu}$)

Les équations d'Einstein du vide avec constante cosmologique ([[10_Relativite_generale_equations_Einstein]]) : $R_{\mu\nu}=\Lambda g_{\mu\nu}$, $R=4\Lambda$.
- $e^{-2(\alpha-\beta)}R_{tt}+R_{rr}=\tfrac2r(\alpha'+\beta')=\Lambda(-1+1)=0$ ⇒ $\alpha'+\beta'=0$ ⇒ $AB=\text{cte}$, qu'on fixe à $1$ par réechelonnage de $t$ ($\tfrac{d}{dr}(AB)=0$, éq. (A.7) de la note importée).
- Avec $B=1/A$ (donc $\beta=-\alpha$, $\beta'-\alpha'=-A'/A$) : $R_{\theta\theta}=\Lambda r^2$ devient $-rA'-A+1=\Lambda r^2$, i.e. $(rA)'=1-\Lambda r^2$ :
$$rA=r-\tfrac\Lambda3r^3-2m\ \Longrightarrow\ A(r)=1-\frac{2m}r-\frac\Lambda3r^2 .\tag{2}$$
$m$ est une constante d'intégration. L'équation $tt$ (ou $rr$) est alors identiquement vérifiée. **Pour $\Lambda=0$ :**
$$\boxed{ds^2=-\Big(1-\frac{2m}r\Big)dt^2+\Big(1-\frac{2m}r\Big)^{-1}dr^2+r^2\big(d\theta^2+\sin^2\theta\,d\varphi^2\big)}\tag{3}$$
Avec $\Lambda\ne0$ : **Schwarzschild–(anti)de Sitter** (A = (2)), $R=4\Lambda$ (vérifié).
**Interprétation de $m$** : pour $r\to\infty$, $g_{tt}\simeq-(1+2\Phi)$ avec $\Phi=-GM/r$, donc $m=GM/c^2$ (masse ADM/Komar) et le **rayon de Schwarzschild** $R_s=2GM/c^2$ (Soleil : 2,95 km ; Terre : 8,9 mm).
**Théorème de Birkhoff** : (3) est l'unique solution sphérique du vide, même sans hypothèse de staticité ; l'extérieur d'une étoile en effondrement sphérique est encore Schwarzschild.
**Erreurs à éviter** : (i) dans la formule de Christoffel le dernier terme est $-\partial_\sigma g_{\mu\nu}$ (pas $-\partial_\sigma g_{\beta\sigma}$) ; (ii) la forme (1) n'est qu'un ansatz : il est *prouvé*, pas supposé, que $AB=1$.

## 4. Domaine de Schwarzschild–Droste et singularités

(3) est définie sur $\mathcal M_{SD}=\mathcal M_I\cup\mathcal M_{II}$ avec
$$\mathcal M_I=\mathbb R\times(2m,\infty)\times S^2,\qquad\mathcal M_{II}=\mathbb R\times(0,2m)\times S^2 .$$
- $r=2m$ : $g_{tt}=0$ et $g_{rr}=\infty$ : **singularité de coordonnées** (invariants de courbure finis ; levée en coordonnées d'Eddington–Finkelstein, [[12_Coordonnees_EF_Kruskal_Penrose_extension_maximale]]).
- $r=0$ : **singularité intrinsèque** : scalaire de Kretschmann $K=R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}=\dfrac{48m^2}{r^6}\to\infty$ ; $R_{\mu\nu}=0$ donc $R=0$ (le scalaire de Ricci ne la détecte pas).
- Pour $r<2m$, $g_{tt}>0$, $g_{rr}<0$ : **$t$ devient spatial et $r$ temporel** (permutation espace-temps) ; tout observateur est entraîné vers $r=0$ en temps propre fini ($\le\pi m$) ; singularité de genre **espace**.

## 5. Horizon des événements

Une **hypersurface** $\{f=0\}$ est de **genre lumière (nulle)** si sa normale $\partial_\mu f$ est de pseudo-norme nulle : $g^{\mu\nu}\partial_\mu f\partial_\nu f=0$. Une particule (ligne d'univers de genre temps ou lumière, donc à l'intérieur du cône) ne peut la traverser que dans un seul sens ⇒ **horizon des événements = hypersurface nulle**. Pour $f=f(r)$ et $f'\ne0$ : $g^{rr}=0$ ⇒ $1-2m/r=0$, $r=2m$ ✓.
$\xi=\partial_t$ est de Killing et **nul sur $r=2m$** ($\xi\cdot\xi=-(1-2m/r)$) : $r=2m$ est un **horizon de Killing**.

## 6. Géodésiques, orbites, tests

Intégrales premières (Killing $\partial_t,\partial_\varphi$, plan équatorial $\theta=\pi/2$) :
$$E=\Big(1-\tfrac{2m}r\Big)\dot t,\qquad L=r^2\dot\varphi,\qquad\dot r^2=E^2-\Big(1-\tfrac{2m}r\Big)\Big(\mu^2+\tfrac{L^2}{r^2}\Big)\quad(\mu=1\text{ massif},\,0\text{ lumière}).$$
Potentiel effectif massif par unité de masse $V_{\text{eff}}=-\tfrac mr+\tfrac{L^2}{2r^2}-\tfrac{mL^2}{r^3}$ : le dernier terme (relativiste, en $1/r^3$) **brise la symétrie $SO(4)$** de Kepler et fait précesser l'orbite ([[06_Kepler_Runge_Lenz_SO_n+1]]) : $\Delta\varphi=6\pi m/p$, avec $u=1/r$ : $u''+u=\tfrac m{L^2}+3mu^2$.
- **Orbite circulaire stable la plus interne (ISCO)** : $r=6m$ ; **sphère de photons** : $r=3m$ ; paramètre d'impact critique $b_c=3\sqrt3\,m$ ; déviation de la lumière $\simeq4m/b$.
- **Chute radiale** : $\tau$ de $2m$ à $0$ : $\pi m$ ; pour un observateur lointain $t\to\infty$ en $r\to2m$ (gel de l'image).
- **Surface de gravité** et température de Hawking : voir [[12_Coordonnees_EF_Kruskal_Penrose_extension_maximale]] §6.

## 7. Généralisations

Reissner–Nordström (charge $Q$) : $A=1-\tfrac{2m}r+\tfrac{Q^2}{r^2}$, deux horizons $r_\pm=m\pm\sqrt{m^2-Q^2}$ ; Kerr (rotation) : [[13_Kerr_trou_noir_en_rotation]] ; Kerr–Newman ; **Schwarzschild en dimension $D$** (Tangherlini) $A=1-(\mu/r)^{D-3}$ (dimension $D$ ; théorie des cordes, [[04_Cordes_et_theorie_M]]).
