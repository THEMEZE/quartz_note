---
title: Collisions : de la boule de billard à la dimension $n$
tags:
  - Physique
  - Mathematiques
lang: fr
partie: IX
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Collisions : de la boule de billard à la dimension $n$

## IX.1 Repères historiques

Aristote ($\sim-350$ : mouvement $\Rightarrow$ moteur) $\to$ Galilée (1632–38, plan incliné) $\to$ Descartes (1644, inertie rectiligne) $\to$ Newton (1687, *Principia*, 3 lois) $\to$ Euler (1750, $\sum\vec F=m\vec a$) $\to$ Noether (1918). *Principe d'inertie* : $\sum\vec F^{\text{ext}}=0\Rightarrow\vec v_G=\text{cte}$ ; c'est une **vraie loi** qui *définit* les référentiels galiléens, non un cas particulier de la 2e loi. Une force ne sert pas à *entretenir* le mouvement mais à le *modifier*.

## IX.2 Quantité de mouvement, impulsion

$\vec p\doteq m\vec v$, $E_c=\dfrac{p^2}{2m}$ ; $\dfrac{d\vec p}{dt}=\sum\vec F^{\text{ext}}$ ; **impulsion** $\vec J\doteq\int_{t_i}^{t_f}\vec F\,dt=\Delta\vec p$, $\bar F=\Delta p/\Delta t$.
*Ordre de grandeur* : ballon de 0,43 kg à 20 m/s : $\|\Delta\vec p\|=8{,}6$ kg m/s ; arrêt en 0,01 s : $\bar F=860$ N ; en 0,10 s : 86 N (airbag, zone de déformation).
Système $\{A+B\}$ : $\dot{\vec P}=\sum\vec F^{\text{ext}}$ ; si $\sum\vec F^{\text{ext}}=0$ (isolé ou pseudo-isolé) **ou** si les forces extérieures sont bornées (leur impulsion pendant le choc est négligeable devant celle des forces de contact), $\vec P'=\vec P$.
Le choc est donc modélisé : *avant* (libres) $\to$ *pendant* ($t_i<t<t_f$, forces intenses brèves, seule $\vec J$ compte) $\to$ *après* (libres).

> [!warning] La conservation est **vectorielle** : une équation par composante. $\|\vec p_A+\vec p_B\|\neq\|\vec p_A\|+\|\vec p_B\|$ en général. Choisir le bon système (fusée : inclure les gaz).

## IX.3 Choc de deux disques/boules durs en dimension $n$

Boules de rayons $R_A,R_B$ ($D\doteq R_A+R_B$), normale au contact **de $B$ vers $A$** : $\vec n=\dfrac{\vec x_A-\vec x_B}{\|\vec x_A-\vec x_B\|}$. Vitesse normale relative $u_n\doteq(\vec v_A-\vec v_B)\cdot\vec n<0$ à l'approche. Masse réduite $\mu\doteq\dfrac{m_Am_B}{m_A+m_B}$.

**Coefficient de restitution** $e\doteq-\dfrac{(\vec v'_A-\vec v'_B)\cdot\vec n}{(\vec v_A-\vec v_B)\cdot\vec n}\in[0,1]$ (choc passif).

**Sans frottement** : $\vec J\parallel\vec n$ (force de contact normale) :
$$
\boxed{\vec v'_A=\vec v_A+\frac J{m_A}\vec n,\quad\vec v'_B=\vec v_B-\frac J{m_B}\vec n,\quad J=-(1+e)\,\mu\,u_n>0,\quad\Delta E_c=-\tfrac12\mu(1-e^2)u_n^2\le0 .}
$$
*Preuve.* Projeter $\vec v'_A-\vec v'_B=(\vec v_A-\vec v_B)+J(\tfrac1{m_A}+\tfrac1{m_B})\vec n$ sur $\vec n$ : $-eu_n=u_n+J/\mu$. $\Delta E_c=Ju_n+J^2/2\mu$. $\square$ La composante tangentielle est conservée ; $\vec P$ est conservée automatiquement. Valable en **toute dimension** (la géométrie ne sélectionne que $\vec n$).

**Instant de contact** ($\Delta\vec x\doteq\vec x_A-\vec x_B$, $\Delta\vec v\doteq\vec v_A-\vec v_B$) : $\|\Delta\vec x+\Delta\vec v\,t\|^2=D^2$,
$$
t_c=\frac{-\Delta\vec x\cdot\Delta\vec v-\sqrt{(\Delta\vec x\cdot\Delta\vec v)^2-\|\Delta\vec v\|^2(\|\Delta\vec x\|^2-D^2)}}{\|\Delta\vec v\|^2},
$$
contact ssi $\Delta\vec x\cdot\Delta\vec v<0$ et discriminant $\|\Delta\vec v\|^2(D^2-b^2)>0$ où $b$ est le **paramètre d'impact** (distance du centre de $B$ à la droite décrite par $A$ dans $\mathscr R_B$). Angle d'impact $\sin\varphi=b/D$, déviation dans $\mathscr R^\ast$ : $\chi=\pi-2\varphi$.

## IX.4 Classification

| Type | $e$ | $\vec P$ | $E_c$ |
|---|---|---|---|
| Parfaitement élastique | $1$ | conservée | conservée |
| Partiellement élastique | $0<e<1$ | conservée | diminue |
| Parfaitement inélastique | $0$ | conservée | diminue (comp. normale) |
| Accrochage (choc mou) | — | conservée | perte maximale, $\vec v'_A=\vec v'_B$ |
| Explosion / ressort | $e>1$ | conservée | augmente |

- **Accrochage** (sans rotation d'ensemble) : $\vec v'=\vec v_G=\dfrac{m_A\vec v_A+m_B\vec v_B}{m_A+m_B}$, $\Delta E_c=-\tfrac12\mu\|\vec v_A-\vec v_B\|^2$ (énergie du mouvement relatif, la seule convertible ; $\tfrac12Mv_G^2$ ne peut l'être).
- Ne pas confondre $e$, $\alpha\doteq E_c'/E_c$ et la perte $-\Delta E_c$. **$\alpha=e^2$ seulement** pour un choc frontal sur cible de masse infinie.
- **Exemple 1D** ($m_A=1{,}5$ kg, $m_B=1$ kg, $v_A=1$ m/s, $v_B=0$) : $\vec P=1{,}5$ kg m/s, $E_c=0{,}75$ J.

| | $v'_A$ | $v'_B$ | $E'_c$ (J) | $\alpha$ |
|---|---|---|---|---|
| élastique | 0,2 | 1,2 | 0,75 | 1 |
| $e=0{,}5$ | 0,4 | 0,9 | 0,525 | 0,70 |
| accrochage | 0,6 | 0,6 | 0,45 | 0,60 |

## IX.4 bis Collision élastique : formules et géométrie

- **1D** : $v'_A=\dfrac{m_A-m_B}{m_A+m_B}v_A+\dfrac{2m_B}{m_A+m_B}v_B$, $v'_B=\dfrac{2m_A}{m_A+m_B}v_A+\dfrac{m_B-m_A}{m_A+m_B}v_B$. Masses égales : échange des vitesses (canon, pendule de Newton).
- **Règle des $90^\circ$** (valable en toute dimension $n\geq2$) : $m_A=m_B$, $B$ au repos, $e=1$ $\Rightarrow$ $\vec v_0=\vec v'_A+\vec v'_B$ et $v_0^2=v_A'^2+v_B'^2$ donc $\vec v'_A\cdot\vec v'_B=0$ ; $\theta_A+\theta_B=90^\circ$ ; si $\varphi$ est l'angle d'impact : $\vec v'_B=v_0\cos\varphi\,(-\vec n)$, fractions d'énergie $\cos^2\varphi$ ($B$) et $\sin^2\varphi$ ($A$). Cet angle n'est $90^\circ$ que : masses égales, $B$ au repos, élastique, **sans rotation/frottement**.
- **Un choc 2D n'est pas déterminé par les conservations** : 2 (composantes de $\vec P$) + 1 ($E_c$) $=3$ équations pour 4 inconnues $(v'_A,v'_B,\theta_A,\theta_B)$ : il faut le **paramètre d'impact**, i.e. la direction de $\vec n$. En dimension $n$ : $2n$ inconnues, $n+1$ équations (vectorielle $+E_c$), et $\vec n\in S^{n-1}$ fournit le reste (ce que résume la formule $\vec v'_A=\vec v_A+\frac J{m_A}\vec n$).
- **Cercle (sphère) des vitesses** : $B$ au repos, $e=1$ : $\vec v_G=\frac{m_A}{m_A+m_B}\vec v_0$ est constante ; dans $\mathscr R^\ast$, $\|\vec u'_A\|=\frac{m_B}{m_A+m_B}v_0\doteq r$. L'extrémité de $\vec v'_A$ décrit la **sphère $S^{n-1}$** de centre $\vec v_G$ et de rayon $r$. Si $m_A>m_B$ : $\sin\theta_{A,\max}=m_B/m_A$ ($m_A=1{,}5,m_B=1$ : $41{,}8^\circ$) ; si $m_A<m_B$ : rebond possible jusqu'à $180^\circ$ ; si $m_A=m_B$ : $\le90^\circ$.
- **Transfert maximal** (frontal) : $\dfrac{E'_{c,B}}{E_c}=\dfrac{4m_Am_B}{(m_A+m_B)^2}$ (modérateur de neutrons : $A=1\Rightarrow\langle E'/E\rangle=\tfrac12$).
- **Section efficace** (disques/boules durs) : $b=D\cos(\chi/2)$ ; $\dfrac{d\sigma}{d\chi}=\dfrac D2\sin\dfrac\chi2$ (2D), $\dfrac{d\sigma}{d\Omega}=\dfrac{D^2}4$ (3D, isotrope) ; **section totale en dimension $n$** : $\sigma_{\text{tot}}=\omega_{n-1}D^{n-1}$, $\omega_k=\dfrac{\pi^{k/2}}{\Gamma(k/2+1)}$ ($2D$ en 2D, $\pi D^2$ en 3D). Géiger–Marsden : rebond d'un $\alpha$ léger sur de l'or $\Rightarrow$ noyau massif (Rutherford 1911). Neutrinos : $\sum\vec P_{\text{visible}}\neq0$ dans le plan transverse $\Rightarrow$ particule invisible.

## IX.5 Boules qui tournent : moment cinétique, frottement (**[nD]**)

**Spin** : tenseur $S_X\in\Lambda^2E$ (bivecteur ; en 2D $I\omega\,e_z$) ; boule homogène $S=-\mathbb I(\Omega)$, $\mathbb I=\kappa_nmR^2$, $\kappa_n=\tfrac2{n+2}$. **Moment cinétique total** et énergie :
$$
L=\sum_X\big(\vec x_X\wedge m_X\vec v_X+S_X\big),\qquad E_c=\sum_X\Big(\tfrac12m_Xv_X^2+\tfrac12\kappa_nm_XR_X^2\cdot\tfrac12\Omega_{X,ij}\Omega_X^{ij}\Big).
$$
Vitesse du point de contact de $A$ : $\vec v_A-R_A\Omega_A\vec n$ ; de $B$ : $\vec v_B+R_B\Omega_B\vec n$ (en 2D : $\vec v_A-R_A\omega_At$, $\vec v_B+R_B\omega_Bt$). **Vitesse de glissement** : $\vec u_t\doteq\Pi_{\vec n^\perp}\big[\vec v_A-\vec v_B-(R_A\Omega_A+R_B\Omega_B)\vec n\big]$ (2D : $(\vec v_A-\vec v_B)\cdot t-R_A\omega_A-R_B\omega_B$).

**Impulsion de contact** sur $A$ : $\vec J_{B\to A}=J\vec n+\vec F$, $\vec F\perp\vec n$ ($J$ normal, $\vec F$ tangentielle=frottement) ; sur $B$ l'opposée.
$$
m_A\vec v'_A=m_A\vec v_A+J\vec n+\vec F,\qquad m_B\vec v'_B=m_B\vec v_B-J\vec n-\vec F,\qquad\Delta S_A=-R_A\,\vec n\wedge\vec F,\quad\Delta S_B=-R_B\,\vec n\wedge\vec F .
$$
(2D : $I\Delta\omega=-RF$ car $\vec n\wedge t=e_z$.)

> [!tip] **$L$ est conservé** (forme forte de la 3e loi : forces opposées, appliquées au même point de contact).
> $\Delta L_{\text{orb}}=(\vec x_A-\vec x_B)\wedge\Delta\vec p_A=(R_A+R_B)\,\vec n\wedge\vec F$ et $\Delta S_A+\Delta S_B=-(R_A+R_B)\,\vec n\wedge\vec F$, somme nulle. $\square$
> Avec la seule forme faible de la 3e loi (forces opposées mais décalées), $\vec P$ est conservée **et pas $L$**.

**Loi de Coulomb au contact.** Masse tangentielle effective $\dfrac1{m_t}=\sum_{X}\dfrac{1+1/\kappa_X}{m_X}$ (boule homogène : $\tfrac{n+4}{2m_X}$ ; 2D disques : $3/m$ ; 3D sphères : $7/(2m)$) ; $\vec u_t'=\vec u_t+\vec F/m_t$.
- sans frottement : $\vec F=0$, spins inchangés ;
- **adhérence** : $\vec F=-m_t\vec u_t$ si $|m_tu_t|\le\mu_fJ$ ($u_t'=0$) ;
- **glissement** : $\vec F=-\mu_fJ\,\vec u_t/|\vec u_t|$ ; le frottement ne fournit jamais d'énergie ($\Delta E_c^{\text{tang}}\le0$) ;
- élasticité tangentielle $\beta\in[0,1]$ : $\vec F=-m_t(1+\beta)\vec u_t$ en adhérence, $\vec u_t'=-\beta\vec u_t$.

**Exemple** : $m_A=m_B=1$ kg, $R=0{,}4$ m, $\kappa=\tfrac12$ ($I=0{,}08$), $e=1$, $\mu_f=0{,}3$, $A$ à $(2;0)$ m/s avec $\omega_A=5$ rad/s sur $B$ immobile, $\vec n=(-1;0)$, $t=(0;-1)$. $u_n=-2$ ; $J=2$ ; $u_t=-R\omega_A=-2$ ; $m_t=\tfrac16$ ; $F_{\text{adh}}=\tfrac13\le\mu_fJ=0{,}6$ : **adhérence**, $F=\tfrac13$. Alors $\vec v'_A=(0;-\tfrac13)$, $\vec v'_B=(2;\tfrac13)$, $\omega'_A=\tfrac{10}3$, $\omega'_B=-\tfrac53$ rad/s ; $L=I\omega_A=0{,}4$ avant et après ; énergie 3 J $\to\tfrac83$ J, perte $\tfrac13$ J $=\tfrac12m_tu_t^2$. Avec $\mu_f=0{,}1$ : glissement ($\mu_fJ=0{,}2<\tfrac13$). **La règle des $90^\circ$ n'est plus valable avec frottement.**

**Accrochage hors axe** : le doublet tourne autour de $G$ : $\omega'=L_G/I_G$, $L_G=\sum(I_X\omega_X+m_X\vec r_X\wedge\vec v_X)$, $I_G=\sum(I_X+m_Xr_X^2)$. Exemple : $b=0{,}5$ m, $R=0{,}4$ m, $v_A=2$, $m=1$ : $L_G=-0{,}5$, $I_G=0{,}48$, $\omega'\simeq-1{,}04$ rad/s ; $E_c$ : $2{,}00\to1{,}26$ J (perte $0{,}74$ J, pas $1{,}00$ J : une partie de l'énergie relative reste en rotation).

## IX.6 Systèmes à masse variable ; fronde gravitationnelle

- **Fusée** (système fermé $\{$fusée$+$gaz$\}$) : $m\,dv=-v_e\,dm\Rightarrow\Delta V=v_e\ln\dfrac{m_0}{m_f}$ (Tsiolkovski) ; relativiste $\Delta V=c\tanh\!\big(\frac{v_e}c\ln\frac{m_0}{m_f}\big)<c$. *Pendule balistique* : $v=\frac{m+M}m\sqrt{2gh}$, fraction d'énergie conservée $\frac m{m+M}$.
- **Fronde** : choc élastique vu depuis la planète ($\|\vec w'\|=\|\vec w\|$), $\vec v_f=\vec U+\vec w'$ ; frontale à contre-courant : $v_f=-v_i+2U$ (jusqu'à $2U$ ; Jupiter $U\simeq13$ km/s). L'énergie vient de la planète (qui ralentit de $\sim10^{-21}$ m/s). Impossible si la sonde arrive de très loin dans $\mathscr R_{\text{planète}}$ (réversibilité) : le gain est une affaire de référentiel.

## IX.7 Exploiter une chronophotographie

Positions $M_k$ à $t_k=k\tau$ : $\vec v\simeq\overrightarrow{M_kM_{k+n}}/(n\tau)$ (points du **même côté** du choc), $\delta E_c/E_c\simeq2\,\delta v/v$. $\tau$ n'est pas la durée du choc. Un écart de quelques % sur $\vec P$ est à comparer à l'incertitude de pointage (exemple : $\vec P\simeq(0{,}06;1{,}28)$ vs $\vec P'\simeq(0{,}00;1{,}26)$ kg m/s : 4 %, compatible). La variation de $\vec p_A$, $\vec p_B$ « pendant » le choc dans une simulation est un modèle d'affichage (choc instantané, seule $\vec J$ compte).
