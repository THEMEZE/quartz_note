---
title: Eddington–Finkelstein, Kruskal–Szekeres, diagramme de Penrose, extension maximale de Schwarzschild
tags:
  - Physique
  - Relativite-generale
  - Trous-noirs
lang: fr
---

> Retour : [[00_Index]] · avant : [[11_Schwarzschild_trou_noir]] · suite : [[13_Kerr_trou_noir_en_rotation]], [[14_Kerr_horizons_ergoregion_extension_maximale]]
> D'après *P.B. : Extension maximale de l'espace-temps de Schwarzschild et de Kerr* (annexes B, C), complété. $G=c=1$, $f(r)\doteq1-\tfrac{2m}r$.

# Du domaine de Schwarzschild à l'extension maximale

## 1. Géodésiques radiales nulles, coordonnée tortue

$ds^2=0$, $d\theta=d\varphi=0$ ⇒ $dt=\pm\dfrac{dr}{f(r)}$. Coordonnée « tortue » :
$$r_\ast\doteq r+2m\ln\Big|\frac r{2m}-1\Big|,\qquad\frac{dr_\ast}{dr}=\frac1f .$$
Rayons nuls **sortants** $t=r_\ast+u$, **entrants** $t=-r_\ast+v$ ; $u\doteq t-r_\ast$ (temps retardé), $v\doteq t+r_\ast$ (temps avancé). Dans $\mathcal M_I$ : $r_\ast\to-\infty$ quand $r\to2m$, donc le rayon atteint l'horizon en $t\to\infty$ : les coordonnées $(t,r)$ ne le traversent pas. Dans $(u,v)$ : $ds^2=-f\,du\,dv+r^2d\Omega^2$ (dégénérée en $r=2m$ car $f\to0$).

## 2. Eddington–Finkelstein entrant (IEF)

Avec $v=t+r_\ast$, $dt=dv-dr/f$ :
$$ds^2=-f\,dv^2+2\,dv\,dr+r^2d\Omega^2 .\tag{EF$^-$}$$
Vérification : $-f(dv-dr/f)^2+dr^2/f=-f\,dv^2+2dv\,dr-dr^2/f+dr^2/f$ ✓. Composantes régulières en $r=2m$ ; $\det g=-r^4\sin^2\theta\ne0$ pour $r\in(0,\infty)$ : métrique lorentzienne **régulière**. Il en résulte que $r=2m$ est une singularité de coordonnées ; on étend
$$\mathcal M_{IEF}=\mathbb R\times(0,\infty)\times S^2=\mathcal M_I\cup\mathcal M_{II}\cup\mathcal H,\quad\mathcal H=\{r=2m\}.$$
Avec $\tilde t=v-r$ : $ds^2=-f\,d\tilde t^2+\tfrac{4m}rd\tilde t\,dr+(1+\tfrac{2m}r)dr^2+r^2d\Omega^2$. Géodésiques radiales nulles :
- entrantes : $v=\text{cte}$, i.e. $\tilde t=-r+v$ (droites à $45^\circ$ dans $(r,\tilde t)$) : traversent $\mathcal H$ vers $\mathcal M_{II}$ ;
- sortantes : $\tilde t=r+4m\ln|\tfrac r{2m}-1|+\text{cte}$ : pour $r<2m$ elles vont **vers** $r\to0$ ; aucune particule de $\mathcal M_{II}$ ne rejoint $\mathcal M_I$ : $\mathcal H$ est un **horizon des événements** ($r=2m$ « trou noir »).
**Eddington–Finkelstein sortant** (avec $u=t-r_\ast$) : $ds^2=-f\,du^2-2du\,dr+r^2d\Omega^2$ ; même calcul avec $t\to-t$ : l'horizon est traversé de $\mathcal M_{II}$ vers $\mathcal M_I$ ; c'est un **trou blanc** (aucune particule ne peut y entrer).
**Horizon de Killing** : $\xi=\partial_{\tilde t}$ (=$\partial_t$) vérifie $\xi\cdot\xi=-f=0$ sur $\mathcal H$, et $\xi$ y est tangent aux génératrices nulles.

## 3. Coordonnées de Kruskal–Szekeres

Dans $\mathcal M_I$ : $U=-e^{-u/4m}$, $V=e^{v/4m}$ ($U<0<V$). Comme $du=-4m\,dU/U$, $dv=4m\,dV/V$ : $du\,dv=-16m^2dU\,dV/(UV)$ et
$$UV=-e^{r_\ast/2m}=-\Big(\frac r{2m}-1\Big)e^{r/2m},\qquad -f\,du\,dv=-\frac{32m^3}re^{-r/2m}dU\,dV .$$
$$ds^2=-\frac{32m^3}re^{-r/2m}\,dU\,dV+r^2d\Omega^2 ,$$
**régulière** en $r=2m$ ($UV=0$). Posons $T=\tfrac12(U+V)$, $X=\tfrac12(V-U)$ :
$$\boxed{ds^2=\frac{32m^3}re^{-r/2m}(-dT^2+dX^2)+r^2d\Omega^2},\qquad X^2-T^2=\Big(\frac r{2m}-1\Big)e^{r/2m}\doteq F\Big(\frac r{2m}\Big)\tag{K}$$
(la fonction $F(x)=(x-1)e^x$ est un difféomorphisme de $(0,\infty)$ sur $(-1,\infty)$ ; $r=2m\,(W_0((X^2-T^2)/e)+1)$ avec $W_0$ de Lambert). 
- **Rayons nuls radiaux : droites à $\pm45^\circ$** : $T=X+U$ (sortants, $U$ cte), $T=-X+V$ (entrants).
- $\mathcal M_I$ : $X>0$, $|T|<X$. $\mathcal H^+$ : $T=X>0$ ($U=0$) ; $\mathcal H^-$ : $T=-X$.
- $r=2m$ ⇔ $X^2=T^2$ ; $r=0$ ⇔ $T^2-X^2=1$ (hyperboles) ; $t=\text{cte}$ ⇔ droites $T/X=\tanh(t/4m)$ passant par l'origine ; $r=\text{cte}$ ⇔ hyperboles $X^2-T^2=\text{cte}$.
- Relation avec $(t,r)$ dans $\mathcal M_I$ : $T=e^{r/4m}\sqrt{\tfrac r{2m}-1}\,\sinh\tfrac t{4m}$, $X=e^{r/4m}\sqrt{\tfrac r{2m}-1}\,\cosh\tfrac t{4m}$ ; dans $\mathcal M_{II}$ : $T=e^{r/4m}\sqrt{1-\tfrac r{2m}}\cosh\tfrac t{4m}$, $X=e^{r/4m}\sqrt{1-\tfrac r{2m}}\sinh\tfrac t{4m}$ ; $t=2m\ln\tfrac{X+T}{X-T}$ (I), $2m\ln\tfrac{T+X}{T-X}$ (II).
- Avec EF entrant : $T+X=V=e^{v/4m}>0$ : $\mathcal M_{IEF}$ correspond à $-X<T<\sqrt{X^2+1}$.

## 4. Extension maximale

La métrique (K) est invariante par $\Phi\colon(T,X)\mapsto(-T,-X)$ et définie pour tout $(T,X)$ avec $T^2-X^2<1$ (hors $r=0$). **Extension maximale analytique (Kruskal)** :
$$\boxed{\mathcal M=\{(T,X,\theta,\varphi):T^2-X^2<1\}=\mathcal M_I\cup\mathcal M_{II}\cup\mathcal M_{III}\cup\mathcal M_{IV}\cup\hat{\mathcal H}},\quad\hat{\mathcal H}=\{T^2=X^2\}.$$
- $\mathcal M_{III}$ : $X<0$, $|T|<-X$ (second univers asymptotiquement plat, **isométrique à $\mathcal M_I$** par $\Phi$) ; $\mathcal M_{IV}$ : $T<-|X|$, $T>-\sqrt{X^2+1}$ : **trou blanc** (singularité passée $r=0$).
- Cette extension est **maximale** : toute géodésique est soit complète, soit s'arrête sur la singularité $r=0$ ($K=48m^2/r^6\to\infty$) ; elle est unique (Hawking–Ellis) comme solution du vide globalement hyperbolique, simplement connexe.
- Les régions $\mathcal M_I$ et $\mathcal M_{III}$ sont causalement déconnectées (jamais de contact sauf à l'intérieur du trou noir) : le « pont d'Einstein–Rosen » **non traversable** ; sur la tranche $T=0$ la géométrie est un col de gorge de rayon $2m$ (bifurcation sphère $T=X=0$, $\mathcal H^+\cap\mathcal H^-$).
- Un trou noir **réaliste** (formé par effondrement) n'a que $\mathcal M_I\cup\mathcal M_{II}$ plus l'intérieur de la matière : pas de trou blanc ni d'univers parallèle.

## 5. Transformation de Penrose, diagramme de Penrose–Carter

**Idée** : compactifier par une transformation **conforme** $\tilde g=\Omega^2g$, $\Omega\to0$ à l'infini, pour amener $\infty$ à distance finie en conservant les **cônes de lumière** (les rayons nuls restent à $45^\circ$).

*Exemple Minkowski.* $t\pm r=\tan\tfrac{T\pm R}2$, $T\pm R\in(-\pi,\pi)$ :
$$ds^2=\Omega^{-2}\big(-dT^2+dR^2+\sin^2R\,d\Omega^2\big),\quad\Omega=\cos T+\cos R,$$
(car $4\cos^2\tfrac{T+R}2\cos^2\tfrac{T-R}2=\Omega^2$ et $r=\sin R/\Omega$) : diamant $|T|+R<\pi$, $R\ge0$. Bords : $i^0$ (infini spatial : $T=0,R=\pi$), $i^\pm$ (infini temporel : $T=\pm\pi,R=0$), $\mathscr I^\pm$ (infini nul : $T\pm R=\pm\pi$).

*Schwarzschild.* Dans $(U,V)$ : $U=\tan\hat U$, $V=\tan\hat V$ avec $\hat U,\hat V\in(-\tfrac\pi2,\tfrac\pi2)$, puis $\hat T=\hat U+\hat V$, $\hat X=\hat V-\hat U$ ; alors $dU\,dV=\sec^2\hat U\sec^2\hat V\,d\hat U\,d\hat V$ et
$$ds^2=\sec^2\hat U\sec^2\hat V\Big[-\frac{32m^3}re^{-r/2m}d\hat U\,d\hat V\Big]+r^2d\Omega^2=\Omega^{-2}\big(-d\hat T^2+d\hat X^2\big)+\dots$$
avec $\Omega^{-2}=\tfrac{8m^3}{r}e^{-r/2m}\sec^2\hat U\sec^2\hat V$ ; les géodésiques nulles radiales restent $\hat T=\pm\hat X+\text{cte}$. Équation de **$r=0$** : $UV=1$ ⇔ $\tan\hat U\tan\hat V=1$ ⇔ $\hat U+\hat V=\pm\tfrac\pi2$ ⇔ **$\hat T=\pm\tfrac\pi2$ : lignes droites horizontales** (singularités de genre espace). Équation de l'horizon : $\hat T=\pm\hat X$. L'infini nul : $\hat V=\tfrac\pi2$ ($\mathscr I^+$ de $\mathcal M_I$), $\hat U=-\tfrac\pi2$ ($\mathscr I^-$).
**Diagramme (schéma)** :
```
                 r=0 (singularité, T̂=π/2)
          ┌──────────────────────────────┐
         /  \        II (trou noir)      /  \
   I⁺'  /    \                          /    \  𝒥⁺ (de I)
       /  III  \        H⁺            /   I   \
  i⁰'  <        >-------X---------<         >  i⁰
       \        /        H⁻         \        /
        \      /                      \      /
         \    /      IV (trou blanc)   \    /
          └──────────────────────────────┘
                 r=0 (singularité, T̂=−π/2)
```
Lecture : chaque point est une 2-sphère ; $I$ et $III$ : deux univers plats ; l'observateur qui entre en $II$ ne revient pas ; la ligne $r=0$ est de genre espace (ni évitable ni visible avant la chute).

## 6. Surface de gravité, température de Hawking

Pour l'horizon de Killing $\xi=\partial_t$ : $\xi^\nu\nabla_\nu\xi^\mu=\kappa\,\xi^\mu$ sur $\mathcal H$. On trouve $\kappa=\tfrac12f'(2m)=\dfrac1{4m}$. **Température de Hawking** $T_H=\dfrac{\hbar\kappa}{2\pi k_Bc}$ ⇒ $T_H=\dfrac{\hbar c^3}{8\pi GMk_B}$ ; **entropie** $S=\dfrac{k_BA}{4\ell_P^2}$, $A=16\pi m^2$ ; **lois de la mécanique des trous noirs** (Bardeen–Carter–Hawking) : $\kappa=\text{cte}$ sur $\mathcal H$ (loi 0), $dM=\tfrac\kappa{8\pi}dA+\Omega_HdJ+\Phi_HdQ$ (1ʳᵉ), $\delta A\ge0$ (2ᵉ), $\kappa\ne0$ atteint en un nombre fini d'étapes (3ᵉ) ([[03_Gravitation_quantique]]).

## 7. Singularités et censure

**Théorèmes de singularité** (Penrose 1965, Hawking–Penrose 1970) : surface piégée + condition d'énergie faible ⇒ incomplétude géodésique. **Censure cosmique** (Penrose) : les singularités génériques sont cachées derrière un horizon (conjecture ouverte). **Théorème d'unicité (no-hair)** : les trous noirs stationnaires d'Einstein–Maxwell sont la famille de Kerr–Newman $(M,J,Q)$.
