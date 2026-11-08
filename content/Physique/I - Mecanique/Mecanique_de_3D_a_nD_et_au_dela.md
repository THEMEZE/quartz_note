---
title: Mécanique, torseurs, symétries — de la 3D à la nD, puis au-delà (supersymétrie, supergravité, gravité quantique, théorie M)
tags:
  - Agrégation
  - Physique
  - Mécanique
  - Torseurs
  - Noether
  - Géométrie-différentielle
  - Supersymétrie
lang: fr
---

> [!abstract] Plan général
> **Fil rouge** : un *torseur* est un élément du dual (type « moment ») ou de l'algèbre (type « vitesse ») du groupe euclidien $E(n)$ ; les torseurs de la mécanique sont des **charges de Noether** de $E(n)$ (puis de Galilée, Poincaré, super-Poincaré). Chaque partie élargit le groupe de symétrie de la précédente.
>
> | Partie | Contenu | Groupe de symétrie |
> |---|---|---|
> | 0 | Conventions | — |
> | I | Géométrie : métrique, bivecteurs, opérateurs différentiels, sous-variétés | $O(n)$ |
> | II | Cinématique : référentiels, solide, torseur cinématique | $E(n)$ |
> | III | Moments, Varignon généralisé, théorie des torseurs | $E(n)$ |
> | IV | Dynamique des systèmes, torseurs cinétique/dynamique/actions | $E(n)$, Galilée |
> | V | Solide rigide, inertie, Euler–Arnold | $SO(n)$ |
> | VI | Lagrange, Hamilton, Liouville, **Noether**, application moment | Galilée / Bargmann |
> | VII | Noether pour les champs, Schrödinger, jauge | $U(1)$, Poincaré |
> | VIII | Kepler, Runge–Lenz, $SO(n+1)$, hydrogène, Mercure | $SO(n+1)$ caché |
> | IX | Collisions en dimension $n$, rotation, frottement | $E(n)$ |
> | X | Relativité restreinte : torseurs de Poincaré | Poincaré |
> | XI | Équilibre statistique : GE / GGE | quantités conservées |
> | XII | **Supersymétrie** | super-Poincaré |
> | XIII | **Supergravité** | super-Poincaré *local* |
> | XIV | **Gravité quantique** | difféomorphismes, Cartan |
> | XV | **Théorie M** | dualités, branes |
> | XVI | Synthèse, pièges, bibliographie | — |

---

# Partie 0 — Conventions et notations

## 0.1 Symboles logiques

| Symbole | Sens | Usage |
|---|---|---|
| $a \doteq b$ | **définition** de $a$ par $b$ | remplace $:=$ partout dans ce document |
| $a = b$ | égalité **démontrée** / équation | résultat, calcul |
| $a \equiv b$ | identité valable $\forall$ valeur des variables, ou congruence $a\equiv b \pmod n$ | structurel |
| $f \colon X \to Y,\; x \mapsto f(x)$ | **définition d'une application** | convention imposée ici |
| $\simeq,\ \approx$ | approximation | numérique / développement |
| $\propto$ | proportionnel | |

Exemple : $\;q \colon \mathbb R \to \mathscr E,\; t \mapsto q(t)$ ; $\;g \colon E\times E \to \mathbb R,\; (u,v)\mapsto g(u,v) \doteq g_{ij}u^iv^j$.

## 0.2 Objets de base

- $\mathscr E$ : espace affine euclidien de dimension $n$, d'espace directeur $E$, produit scalaire $g=\langle\cdot,\cdot\rangle$ ; points $A,B,M,\dots$ ; $\overrightarrow{AB}\in E$.
- Base orthonormée $(e_i)$ ; indices latins $i,j,\dots\in\{1,\dots,n\}$ ; sommation d'Einstein ; $\delta_{ij}$ Kronecker, $\varepsilon_{i_1\dots i_n}$ Levi-Civita.
- $\mathscr R$ référentiel (repère $(O,(e_i))$ + horloge) ; $\mathscr S$ système matériel ; $G$ centre d'inertie ; $\mathscr R^\ast$ référentiel barycentrique.
- $\vec{\ }$ pour les vecteurs ; les bivecteurs/tenseurs antisymétriques sont notés sans flèche ($M$, $L$, $\Omega$).
- Dérivée temporelle dans $\mathscr R$ : $\dfrac{d\,\cdot}{dt}\Big)_{\mathscr R}$.
- Définitions de $\mathscr T$ : $\mathscr V$ (cinématique), $\mathscr C$ (cinétique), $\mathscr D$ (dynamique), $\mathscr A$ (actions).

## 0.3 Convention de transport « BABAR »

Pour un torseur de **type moment** $\{R;\,M(A)\}$ :
$$
M(B) = M(A) + \overrightarrow{BA}\wedge R \qquad(\textbf{B}\text{ égale }\textbf{A}\text{ plus }\textbf{BA}\text{ vectoriel }\textbf{R}).
$$
Pour un torseur de **type vitesse** $\{\Omega;\,v(A)\}$ : $\;v(B)=v(A)+\Omega\cdot\overrightarrow{AB}$ (en 3D : $=v(A)+\overrightarrow{BA}\wedge\vec\Omega$).

## 0.4 Niveaux

Les sections marquées **[3D]** n'ont de sens qu'en dimension 3 (produit vectoriel, rotationnel, vecteur rotation) ; **[nD]** valent en toute dimension $n\geq 2$ ; **[Mink]** en espace-temps ; ★ = niveau avancé.

---

# Partie I — Géométrie : tenseurs, bivecteurs, opérateurs différentiels

## I.1 Métrique et coordonnées

Variété $(M,g)$ (pseudo-)riemannienne de dimension $n$, coordonnées $q^i$, base naturelle $e_i\doteq\partial_i$, $g_{ij}\doteq g(e_i,e_j)$, $g^{ij}$ l'inverse, $g\doteq\det(g_{ij})$.

- Musicaux : $v_i = g_{ij}v^j$ ($\flat$), $\alpha^i = g^{ij}\alpha_j$ ($\sharp$).
- Changement de coordonnées $q\mapsto q'$ : $v'^{\,i}=\dfrac{\partial q'^i}{\partial q^j}v^j$ (contravariant), $\alpha'_i=\dfrac{\partial q^j}{\partial q'^i}\alpha_j$ (covariant).
- **Connexion de Levi-Civita** : $\Gamma^k_{ij}\doteq\tfrac12 g^{kl}(\partial_i g_{jl}+\partial_j g_{il}-\partial_l g_{ij})$, $\nabla_j v^i=\partial_jv^i+\Gamma^i_{jk}v^k$.
- **Accélération en coordonnées quelconques** : $a^i=\ddot q^i+\Gamma^i_{jk}\dot q^j\dot q^k$. Le mouvement libre est donc la **géodésique** $a^i=0$ : première loi de Newton $=$ géodésique de la métrique plate (idée généralisée en relativité générale, partie XIV).

## I.2 Bivecteurs, $\mathfrak{so}(n)$, produit extérieur

- $\Lambda^kE$ : $k$-vecteurs, $\dim\Lambda^kE=\binom nk$. Pour $a,b\in E$ :
$$
a\wedge b\doteq a\,b^{\mathsf T}-b\,a^{\mathsf T},\qquad (a\wedge b)^{ij}=a^ib^j-a^jb^i,\qquad (a\wedge b)(u)=a\,(b\cdot u)-b\,(a\cdot u).
$$
- $\mathfrak{so}(n)\doteq\{\Omega\in\mathrm{End}(E):\Omega^{\mathsf T}=-\Omega\}\;\cong\;\Lambda^2E$, $\dim=\tfrac{n(n-1)}2$, crochet $[\Omega_1,\Omega_2]=\Omega_1\Omega_2-\Omega_2\Omega_1$ ; $SO(n)=\exp\mathfrak{so}(n)$.
- **Dimension 3** (*et seulement elle, avec $n=7$ par accident octonionique*) : il existe un produit vectoriel, via la dualité de Hodge $\star\colon\Lambda^2E\to E$. Identifications :
$$
M^{ij}=\varepsilon^{ijk}M_k\ \ (\text{bivecteur-moment}),\qquad \Omega^{ij}=-\varepsilon^{ijk}\Omega_k\ \ (\text{endomorphisme}: \Omega\cdot u=\vec\Omega\times u),\qquad a\wedge b\leftrightarrow a\times b.
$$
- $n=2$ : $\Lambda^2E\cong\mathbb R$ (pseudo-scalaire $\omega$, $\Omega=\omega\begin{pmatrix}0&-1\\1&0\end{pmatrix}$). $n=4$ : $\Lambda^2=\Lambda^2_+\oplus\Lambda^2_-$ (auto-dual/anti-auto-dual), $\mathfrak{so}(4)=\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ — ce sera la clé de l'hydrogène (VIII).
- **Forme normale** (Youla) : tout $\Omega\in\mathfrak{so}(n)$ s'écrit, dans une base orthonormée adaptée, $\Omega=\sum_{k=1}^{\lfloor n/2\rfloor}\omega_k\,e_{2k-1}\wedge e_{2k}$ ; les $\omega_k$ sont les $\lfloor n/2\rfloor$ invariants. Si $n$ est impair, $\ker\Omega\neq\{0\}$.
- Produit scalaire sur $\Lambda^2$ : $\langle A,B\rangle\doteq\tfrac12A^{ij}B_{ij}$.

## I.3 Opérateurs différentiels métriques

Pour $f\colon M\to\mathbb R$, $v$ champ de vecteurs :
$$
\operatorname{grad}f\doteq(df)^\sharp=g^{ij}\partial_jf\,e_i,\qquad
\operatorname{div}v\doteq\nabla_iv^i=\frac1{\sqrt{|g|}}\partial_i\!\big(\sqrt{|g|}\,v^i\big),\qquad
\Delta f\doteq\operatorname{div}\operatorname{grad}f=\frac1{\sqrt{|g|}}\partial_i\!\big(\sqrt{|g|}\,g^{ij}\partial_jf\big).
$$
- Élément de volume $dV=\sqrt{|g|}\,dq^1\cdots dq^n$ (le facteur $\sqrt{|g|}$ est une densité de volume, pas un facteur à ajouter « à la main » aux composantes physiques).
- **Théorème de la divergence** : $\displaystyle\int_\Omega\operatorname{div}v\,dV=\int_{\partial\Omega}g(v,\nu)\,dS$.
- **Rotationnel** : $\operatorname{rot}v\doteq d(v^\flat)$, 2-forme $(\partial_iv_j-\partial_jv_i)$ en toute dimension ; identifié à un vecteur par $\star$ **seulement en 3D** : $\operatorname{rot}v=\star\,d v^\flat=\nabla\times v$.

**Coordonnées orthogonales** ($g_{ii}=h_i^2$, facteurs de Lamé) :
$$
\operatorname{grad}f=\sum_i\frac1{h_i}\partial_if\,\hat e_i,\quad
\operatorname{div}v=\frac1{\prod h}\sum_i\partial_i\!\Big(\frac{\prod h}{h_i}\hat v_i\Big),\quad
\Delta f=\frac1{\prod h}\sum_i\partial_i\!\Big(\frac{\prod h}{h_i^{2}}\partial_if\Big).
$$

| Système $\mathbb R^3$ | $(h_1,h_2,h_3)$ | $dV$ | $\Delta f$ |
|---|---|---|---|
| cartésien $(x,y,z)$ | $(1,1,1)$ | $dx\,dy\,dz$ | $\partial_x^2f+\partial_y^2f+\partial_z^2f$ |
| cylindrique $(r,\theta,z)$ | $(1,r,1)$ | $r\,dr\,d\theta\,dz$ | $\frac1r\partial_r(r\partial_rf)+\frac1{r^2}\partial_\theta^2f+\partial_z^2f$ |
| sphérique $(r,\theta,\varphi)$ | $(1,r,r\sin\theta)$ | $r^2\sin\theta\,dr\,d\theta\,d\varphi$ | $\frac1{r^2}\partial_r(r^2\partial_rf)+\frac1{r^2\sin\theta}\partial_\theta(\sin\theta\,\partial_\theta f)+\frac1{r^2\sin^2\theta}\partial_\varphi^2f$ |

**Dimension $n$ en coordonnées radiales** : $dV=r^{n-1}dr\,d\Omega_{n-1}$, $|S^{n-1}|=\dfrac{2\pi^{n/2}}{\Gamma(n/2)}$, $|B^n|=\dfrac{\pi^{n/2}}{\Gamma(n/2+1)}$, et
$$
\Delta=r^{1-n}\partial_r\big(r^{n-1}\partial_r\big)+r^{-2}\Delta_{S^{n-1}}.
$$
Solution fondamentale du laplacien : $\propto r^{2-n}$ ($n\geq3$), $\ln r$ ($n=2$) — c'est pourquoi la force de gravitation/Coulomb en $1/r^{n-1}$ est la « bonne » en dimension $n$ (VIII).

## I.4 Hypersurfaces $\Sigma\subset M$ (dimension $n-1$)

Paramétrage $q^i=X^i(u)$, $\mathbf t_a=\partial_aX^i e_i$.
$$
\gamma_{ab}\doteq g_{ij}\partial_aX^i\partial_bX^j,\qquad dS=\sqrt{|\gamma|}\,du^1\cdots du^{n-1}.
$$
- Sphère $S^2_R$ : $dS=R^2\sin\theta\,d\theta\,d\varphi$. Graphe $q^n=h(q')$ : $dS=\sqrt{1+|\nabla h|^2}\,dq'$.
- Normale si $\Sigma=\{F=0\}$ : $\nu=\operatorname{grad}F/|\operatorname{grad}F|$, $dS=\iota_\nu dV|_\Sigma$.
- Projecteur tangent $P^i{}_j=\delta^i{}_j-\nu^i\nu_j$ ; $\operatorname{grad}_\Sigma f=P\operatorname{grad}f=\gamma^{ab}\partial_af\,\mathbf t_b$ ; $\operatorname{div}_\Sigma v=\nabla_iv^i-\nu_i\nu^j\nabla_jv^i$ ; $\Delta_\Sigma f=\dfrac1{\sqrt{|\gamma|}}\partial_a\big(\sqrt{|\gamma|}\gamma^{ab}\partial_bf\big)$.
- **Courbure moyenne** $H\doteq\operatorname{div}_\Sigma\nu$ (somme des courbures principales ; sphère de rayon $R$, $\nu$ sortante : $H=2/R$) et
$$
\Delta f=\Delta_\Sigma f+H\,\partial_\nu f+\partial_\nu^2f\qquad(\text{espace euclidien}).
$$
- **Divergence sur $\Sigma$ à bord** (conormale sortante $n$) : $\displaystyle\int_\Sigma\operatorname{div}_\Sigma v\,dS=\int_{\partial\Sigma}g(v,n)\,d\ell-\int_\Sigma H\,g(v,\nu)\,dS$. Si $v$ tangent, le dernier terme disparaît ; $\Sigma$ fermée et $w$ tangent : $\int_\Sigma\operatorname{div}_\Sigma w\,dS=0$.

## I.5 Sous-variétés de codimension $k$ (dimension $m=n-k$)

$$
\gamma_{ab}=g_{ij}\partial_aX^i\partial_bX^j,\qquad dS=\sqrt{\det\gamma}\,d^mu,\qquad P_T^{ij}=\gamma^{ab}t_a^it_b^j,\qquad P_N=g^{-1}-P_T .
$$
Définition implicite $S=\{F^1=\dots=F^k=0\}$, $G^{\alpha\beta}\doteq g^{ij}\partial_iF^\alpha\partial_jF^\beta$, $J\doteq\sqrt{\det G^{\alpha\beta}}$ :
$$
\int_M\varphi\,\delta^{(k)}(F)\,J\,dV=\int_S\varphi\,dS\quad(\text{Dirac}),\qquad
\int_M\varphi\,J\,dV=\int_{\mathbb R^k}\Big(\int_{\{F=c\}}\varphi\,dS\Big)d^kc\quad(\text{co-aire}).
$$
- Seconde forme fondamentale $\mathrm{II}(X,Y)=(\nabla_XY)^\perp$, **vecteur courbure moyenne** $\vec H=\gamma^{ab}\mathrm{II}(\mathbf t_a,\mathbf t_b)$ ; pour $k=1$, $\nu$ sortante : $\vec H=-H\nu$.
- $\operatorname{div}_Sv=\operatorname{div}_S(v^T)-g(v,\vec H)$ ; $\displaystyle\int_S\operatorname{div}_Sv\,dS=\int_{\partial S}g(v,n)d\sigma-\int_Sg(v,\vec H)\,dS$ ; première variation de l'aire : $\delta\,\mathrm{Aire}(S)=-\int_Sg(v,\vec H)\,dS$.

---

# Partie II — Cinématique : référentiels, solide, torseur cinématique

## II.1 Deux référentiels

Soit $\mathscr R=(O,(e_i))$ et $\mathscr R'=(O',(e'_i))$ avec $e'_j(t)=Q(t)e_j$, $Q(t)\in SO(n)$. On définit la **rotation instantanée** (antisymétrique car $QQ^{\mathsf T}=1$) :
$$
\Omega_{\mathscr R'/\mathscr R}\doteq\dot Q\,Q^{\mathsf T}\in\mathfrak{so}(n),\qquad \dot e'_j=\Omega\,e'_j .
$$
En 3D, $\Omega\cdot u=\vec\Omega\times u$.

## II.2 Théorème de transport (**[nD]**)

Pour tout vecteur $A(t)=A'^j(t)e'_j(t)$ :
$$
\frac{dA}{dt}\Big)_{\mathscr R}=\frac{dA}{dt}\Big)_{\mathscr R'}+\Omega_{\mathscr R'/\mathscr R}\cdot A .
$$
*Preuve* : $\dot A=\dot A'^je'_j+A'^j\dot e'_j=\dot A)_{\mathscr R'}+\Omega A$. $\square$

## II.3 Compositions des vitesses et accélérations

Avec $\mathscr R$ « absolu », $\mathscr R'$ « relatif », $\Omega\doteq\Omega_{\mathscr R'/\mathscr R}$, $v_r,a_r$ relatives :
$$
\boxed{v_a(M)=v_r(M)+\underbrace{v_a(O')+\Omega\cdot\overrightarrow{O'M}}_{v_e(M)}},\qquad
\boxed{a_a=a_r+\underbrace{a_a(O')+\dot\Omega\,\overrightarrow{O'M}+\Omega^2\overrightarrow{O'M}}_{a_e}+\underbrace{2\,\Omega\cdot v_r}_{a_c}}.
$$
En 3D, $\Omega^2\overrightarrow{O'M}=\vec\Omega\times(\vec\Omega\times\overrightarrow{O'M})=-|\vec\Omega|^2\overrightarrow{O'M}_\perp$ ; $a_c=2\vec\Omega\times v_r$.

## II.4 Référentiels galiléens, forces d'inertie

- Si $\mathscr R$ est galiléen, $\mathscr R'$ l'est ssi $\Omega=0$ et $a_a(O')=0$ (translation rectiligne uniforme).
- Dans un $\mathscr R'$ quelconque : $m\,a_r=\vec F+\vec F_{ie}+\vec F_{ic}$ avec $\vec F_{ie}\doteq-m\,a_e$, $\vec F_{ic}\doteq-m\,a_c$. Centrifuge (3D) : $+m|\Omega|^2\overrightarrow{O'M}_\perp$ ; Coriolis : $-2m\,\Omega\cdot v_r$ (ne travaille pas).
- **Groupe de Galilée** $\mathrm{Gal}(n)$ : rotations ($\tfrac{n(n-1)}2$), translations spatiales ($n$), *boosts* ($n$), translation temporelle ($1$) : dimension $\tfrac{n(n+1)}2+n+1$.

## II.5 Solide rigide et torseur cinématique

$\mathscr S$ est rigide si $\|\overrightarrow{AB}\|$ est constante pour tous $A,B\in\mathscr S$. Alors $\overrightarrow{AB}=Q(t)\overrightarrow{AB}_0$, d'où
$$
\boxed{v(B)=v(A)+\Omega_{\mathscr S/\mathscr R}\cdot\overrightarrow{AB}}\qquad\Big(=v(A)+\overrightarrow{BA}\wedge\vec\Omega\ \text{ en 3D}\Big).
$$
**Torseur cinématique** $\mathscr V_{\mathscr S/\mathscr R}(A)\doteq\{\Omega_{\mathscr S/\mathscr R};\,v_{\mathscr S/\mathscr R}(A)\}$. Composition : $\mathscr V_{\mathscr S/\mathscr R}=\mathscr V_{\mathscr S/\mathscr R'}+\mathscr V_{\mathscr R'/\mathscr R}$ (les $\Omega$ s'additionnent).

## II.6 Classification instantanée (Chasles généralisé, **[nD]**)

Comme $\operatorname{Im}\Omega=(\ker\Omega)^\perp$ ($\Omega$ antisymétrique), la projection $v_\parallel\doteq\Pi_{\ker\Omega}\,v(A)$ **ne dépend pas de $A$** (car $\Omega\cdot\overrightarrow{AB}\in\operatorname{Im}\Omega$). Le mouvement instantané est donc :
- une rotation autour du sous-espace affine $\{C:\ \Omega\,\overrightarrow{AC}=-v(A)_\perp\}$ (de dimension $\dim\ker\Omega$) ;
- composée d'une translation de vitesse $v_\parallel\in\ker\Omega$ (« glissement hélicoïdal »).

Cas particuliers : **$n$ pair et $\Omega$ inversible** $\Rightarrow$ $\ker\Omega=0$, **centre instantané de rotation unique**. **$n=3$** : $\ker\Omega=\mathbb R\vec\Omega$, $\vec\Omega\cdot v(A)$ invariant, axe central hélicoïdal (théorème de Chasles). **$n=2$** : centre instantané de rotation (ou translation pure si $\Omega=0$).

## II.7 Dérivées de bases et angles (exemple 3D)

Cylindrique : $\dot{\hat e}_r=\dot\theta\hat e_\theta$, $\dot{\hat e}_\theta=-\dot\theta\hat e_r$. Sphérique : $\vec\Omega=\dot\varphi\hat e_z+\dot\theta\hat e_\varphi$ pour la base mobile $(\hat e_r,\hat e_\theta,\hat e_\varphi)$. Angles d'Euler $(\psi,\theta,\phi)$ : $\vec\Omega=\dot\psi\,\hat e_{z}+\dot\theta\,\hat e_{N}+\dot\phi\,\hat e_{z'}$ (précession, nutation, rotation propre).

---

# Partie III — Moments, Varignon généralisé, théorie des torseurs

## III.1 Moment d'un vecteur appliqué

Pour un vecteur $w$ appliqué en $M$ et un point $A$ :
$$
\mathfrak m_A(M,w)\doteq\overrightarrow{AM}\wedge w\in\Lambda^2E,\qquad \big(\mathfrak m_A\big)^{ij}=AM^i\,w^j-AM^j\,w^i .
$$
En 3D, $\mathfrak m_A=\overrightarrow{AM}\times w$ (via $M^{ij}=\varepsilon^{ijk}M_k$).

## III.2 Système de vecteurs : théorème de Varignon généralisé

Pour $(M_k,w_k)_k$ (ou une mesure) :
$$
R\doteq\sum_kw_k,\qquad M(A)\doteq\sum_k\overrightarrow{AM_k}\wedge w_k .
$$

> [!tip] Théorème (Varignon généralisé, **[nD]**)
> $$M(B)=M(A)+\overrightarrow{BA}\wedge R .$$
> *Preuve.* $\overrightarrow{BM_k}=\overrightarrow{BA}+\overrightarrow{AM_k}$, donc $M(B)=\sum_k\overrightarrow{BA}\wedge w_k+\sum_k\overrightarrow{AM_k}\wedge w_k$. $\square$
> En composantes : $M^{ij}(B)=M^{ij}(A)+BA^iR^j-BA^jR^i$.

**Composition de transports** : $M(C)=M(B)+\overrightarrow{CB}\wedge R=M(A)+\overrightarrow{CA}\wedge R$ (cocycle, compatible avec $\overrightarrow{CB}+\overrightarrow{BA}=\overrightarrow{CA}$).

**Version bilinéaire abstraite.** Soit $\beta\colon E\times W\to Z$ bilinéaire et $M_\beta(A)\doteq\sum_k\beta(\overrightarrow{AM_k},w_k)$. Alors $M_\beta(B)=M_\beta(A)+\beta(\overrightarrow{BA},R)$. Avec $\beta=\wedge$ : moments ; $\beta=\cdot$ : moment *scalaire* $\sum\overrightarrow{AM_k}\cdot w_k$ ; $\beta=\times$ en 3D.

**Dérivée d'un torseur à point de réduction mobile.** Si $A=A(t)$, la dérivée du torseur de type moment $\{R;M(A)\}$ est
$$
\dot{\mathscr T}(A)\doteq\{\dot R;\ \dot M(A)+v_A\wedge R\},\qquad \dot M(A)\doteq\textstyle\sum\overrightarrow{AM_k}\wedge\dot w_k .
$$
(Le terme $v_A\wedge R$ provient de $\frac d{dt}\overrightarrow{AM_k}=v_{M_k}-v_A$ ; il redonne $\mathscr D=\dot{\mathscr C}$ en IV.)

## III.3 Structure de torseur ; classification (**[nD]**)

- $\mathscr T(A)=\{R;M(A)\}$ est **un seul objet** : $R\in E$ et $M\in\Lambda^2E$, d'où $\dim=n+\tfrac{n(n-1)}2=\tfrac{n(n+1)}2=\dim\mathfrak e(n)$. En 3D : 6, d'où « deux vecteurs » — mais en général le moment n'est **pas** un vecteur.
- **Addition** : $\{R_1;M_1\}+\{R_2;M_2\}\doteq\{R_1+R_2;M_1+M_2\}$ (réduits au même point).
- **Résultante nulle** : $M$ est indépendant du point (**couple**), classifié par la forme normale de $\mathfrak{so}(n)$ (I.2) : $\lfloor n/2\rfloor$ invariants. Deux forces opposées $\pm w$ appliquées en $M_1,M_2$ : $M=\overrightarrow{M_2M_1}\wedge w$.
- **Invariant fondamental** : $M(B)\wedge R=M(A)\wedge R$ (car $R\wedge R=0$). Le **trivecteur** $M\wedge R\in\Lambda^3E$ est invariant. En 3D, $\star(M\wedge R)=\vec M\cdot\vec R$ (invariant scalaire classique) ; en espace-temps de dimension 4, c'est le **vecteur de Pauli–Lubański** (X).
- **Axe central généralisé.** Pour $R\neq0$ : on cherche $B$ avec $M(B)\lrcorner R=0$ (contraction $M^{ij}R_j=0$). Comme $M(B)R=M(A)R+\overrightarrow{BA}\,|R|^2-R\,(\overrightarrow{BA}\cdot R)$, la solution est
$$
\overrightarrow{AB}=\frac{M(A)\,R}{|R|^2}+\lambda R,\quad\lambda\in\mathbb R\quad(\text{droite affine}).
$$
Sur cette droite, $M_{\min}\in\Lambda^2(R^\perp)$ : forme canonique $\{R;M_{\min}\}$. En 3D, $\Lambda^2(R^\perp)=\mathbb R\,\star R$, donc $M_{\min}\parallel R$ (**torseur de Poinsot / hélicoïde**). En $n\geq4$, $M_{\min}$ reste un bivecteur de $R^\perp$ à $\lfloor(n-1)/2\rfloor$ invariants.
- **Existence d'un point où $M=0$** : possible ssi $M(A)\in\{a\wedge R\}$, i.e. ssi $M\wedge R=0$ (pour $R\neq0$) ; en 3D ssi $\vec M\cdot\vec R=0$.

## III.4 Deux types de torseurs, dualité, comoment

| | Type **vitesse** (élément de $\mathfrak e(n)$) | Type **moment** (élément de $\mathfrak e(n)^\ast$) |
|---|---|---|
| Données | $\{\Omega;v(A)\}$, $\Omega\in\mathfrak{so}(n)$ | $\{R;M(A)\}$, $R\in E$, $M\in\Lambda^2E$ |
| Transport | $v(B)=v(A)+\Omega\,\overrightarrow{AB}$ | $M(B)=M(A)+\overrightarrow{BA}\wedge R$ |
| Exemples | cinématique $\mathscr V$ | cinétique $\mathscr C$, dynamique $\mathscr D$, actions $\mathscr A$ |

**Comoment** (couplage $\mathfrak e(n)^\ast\times\mathfrak e(n)\to\mathbb R$) :
$$
\boxed{\langle\mathscr T,\mathscr V\rangle\doteq R\cdot v(A)-\tfrac12M^{ij}(A)\,\Omega_{ij}}\qquad(\text{3D : } \vec R\cdot v(A)+\vec M(A)\cdot\vec\Omega).
$$
*Indépendance de $A$* : $R\cdot\Omega\overrightarrow{AB}$ compense exactement $-\tfrac12(\overrightarrow{BA}\wedge R)^{ij}\Omega_{ij}$ (calcul direct). Conséquences :
- **Puissance** $\mathcal P=\langle\mathscr A,\mathscr V\rangle$ d'un système de forces sur un solide ;
- **Énergie cinétique** d'un solide : $2T=\langle\mathscr C,\mathscr V\rangle$ (IV.5).

## III.5 Systèmes continus et formulaire

Pour une mesure $dR(M)$ : $R=\iiint dR(M)$, $M(A)=\iiint\overrightarrow{AM}\wedge dR(M)$ ; Varignon inchangé. Les quatre torseurs de la mécanique ($\mathscr V,\mathscr C,\mathscr D,\mathscr A$) sont des instances (IV).

---

# Partie IV — Dynamique des systèmes matériels fermés

## IV.1 Axiomes (rappels)

1. Les forces d'interaction sont invariantes par changement de référentiel.
2. Il existe des référentiels galiléens ; ils sont en translation rectiligne uniforme les uns par rapport aux autres.
3. Dans un galiléen, pour un point matériel : $\dfrac{d\vec p}{dt}=\vec F$, $\vec p\doteq m\vec v$ ($m\vec a=\vec F$ si $m$ constante). *Historique* : la forme $\sum\vec F=m\vec a$ est d'Euler (1750) ; Newton écrit $\dot{\vec p}$.
4. **Principe des actions réciproques** (forme forte) : $\vec F_{1\to2}=-\vec F_{2\to1}$, portées par la droite $(M_1M_2)$ ; pour deux systèmes disjoints, le torseur $\mathscr A_{1\to2}=-\mathscr A_{2\to1}$.

> [!warning] Forme faible/forte
> Avec la seule forme faible (forces opposées mais non alignées), $\vec P$ est conservée **mais pas $L$** (IX.3).

## IV.2 Masse, centre d'inertie, mesure

$m_{\mathscr S}=\int dm$, $\overrightarrow{OG}\doteq\frac1m\int\overrightarrow{OM}\,dm$, $\vec P\doteq\int\vec v\,dm=m\,v_G$.

## IV.3 Les quatre torseurs

Pour un système $\mathscr S$ dans $\mathscr R$ (réduits en $A$) :

| Torseur | Résultante | Moment en $A$ | Type |
|---|---|---|---|
| **cinématique** $\mathscr V$ | $\Omega_{\mathscr S/\mathscr R}$ | $v(A)$ | vitesse (solide) |
| **cinétique** $\mathscr C$ | $\vec P=\int\vec v\,dm$ | $L(A)\doteq\int\overrightarrow{AM}\wedge\vec v\,dm$ | moment |
| **dynamique** $\mathscr D$ | $\vec S=\int\vec a\,dm$ (quantité d'accélération) | $D(A)\doteq\int\overrightarrow{AM}\wedge\vec a\,dm$ | moment |
| **actions** $\mathscr A$ | $\vec F=\int d\vec F$ | $\mathfrak M(A)\doteq\int\overrightarrow{AM}\wedge d\vec F$ | moment |

Les trois derniers satisfont **BABAR** :
$$
L(B)=L(A)+\overrightarrow{BA}\wedge\vec P,\quad D(B)=D(A)+\overrightarrow{BA}\wedge\vec S,\quad\mathfrak M(B)=\mathfrak M(A)+\overrightarrow{BA}\wedge\vec F .
$$
Le torseur cinématique est de type vitesse et n'a de sens (loi de Varignon cinématique) que pour un **solide**.

## IV.4 Relations entre les torseurs : la chaîne

$$
\mathscr V\ \xrightarrow{\ \ \mathbb I\ \ }\ \mathscr C\ \xrightarrow{\ \ d/dt\ \ }\ \mathscr D\ \overset{\text{PFD}}=\ \mathscr A .
$$
- $\mathscr V\to\mathscr C$ : opérateur d'inertie (partie V), linéaire pour un solide ; $\vec P=m\,v_G$ (translation) et $L(G)=-\mathbb I_G(\Omega)$ (rotation).
- $\mathscr C\to\mathscr D$ : $\;D(A)=\dfrac{dL(A)}{dt}\Big)_{\mathscr R}+v(A)\wedge\vec P$ pour $A$ mobile, et $\vec S=\dot{\vec P}$ (cf. III.2).
  *Preuve* : $\dot L(A)=\int(\vec v-v_A)\wedge\vec v\,dm+\int\overrightarrow{AM}\wedge\vec a\,dm=-v_A\wedge\vec P+D(A)$ car $\int\vec v\wedge\vec v=0$. $\square$
  Si $A$ est fixe dans $\mathscr R$, ou si $A=G$ (car $v_G\wedge\vec P=m\,v_G\wedge v_G=0$) : $D(A)=\dot L(A)$.
- $\mathscr D=\mathscr A$ : PFD généralisé ; $\mathscr D=\mathscr A^{\text{ext}}$ pour un système fermé dans un galiléen.

## IV.5 Théorèmes généraux (systèmes fermés, $\mathscr R$ galiléen)

**Forces intérieures/extérieures.** $d\vec F_M=d\vec F^{\text{ext}}_M+\int_{M'}d\vec F_{M'\to M}$, avec $d\vec F_{M'\to M}=-d\vec F_{M\to M'}$ (3e loi) et colinéaire à $\overrightarrow{MM'}$ (forme forte).

> [!tip] **TRD** (résultante). $\ \dfrac{d\vec P}{dt}\Big)_{\mathscr R}=\vec F^{\text{ext}}$, i.e. $m\,a_G=\vec F^{\text{ext}}$.
> *Preuve.* Double intégrale des interactions $=\tfrac12\iint(d\vec F_{M'\to M}+d\vec F_{M\to M'})=0$.

> [!tip] **TMD** (moment dynamique). $\ D(A)=\mathfrak M^{\text{ext}}(A)\quad\forall A$.
> *Preuve.* Terme intérieur $\tfrac12\iint(\overrightarrow{AM}\wedge dF_{M'\to M}+\overrightarrow{AM'}\wedge dF_{M\to M'})=\tfrac12\iint\overrightarrow{M'M}\wedge dF_{M'\to M}=0$ par colinéarité.

> [!tip] **TMC** en $A$ fixe : $\dfrac{dL(A)}{dt}\Big)_{\mathscr R}=\mathfrak M^{\text{ext}}(A)$. **TMC\*** barycentrique : $\dfrac{dL^\ast}{dt}\Big)_{\mathscr R}=\mathfrak M^{\text{ext}}(G)$ (valable même si $G$ accélère, car $\overrightarrow{GM}\wedge(-a_G)$ s'intègre en zéro).

**Version torseur.** $\mathscr D_{\mathscr S/\mathscr R}(A)=\mathscr A^{\text{ext}}_{\mathscr S/\mathscr R}(A)$ : deux torseurs égaux en un point le sont partout (transport identique).

## IV.6 Théorèmes de König

$$
L(A)=L^\ast+\overrightarrow{AG}\wedge m\,v_G,\qquad T=\tfrac12m\,v_G^2+T^\ast,\qquad L^\ast\doteq\int\overrightarrow{GM}\wedge v^\ast\,dm,\ T^\ast\doteq\int\tfrac12 v^{\ast2}dm .
$$
Corollaire : l'énergie cinétique de $G$ ne peut pas être dissipée dans un système isolé (X, IX).

## IV.7 Énergie

- **TEC** (point) : $\Delta T=\sum W$, avec $W_{A\to B}(\vec F)=\int_A^B\vec F\cdot d\vec r$. Preuve : $m\vec v\cdot d\vec v=d(\tfrac12mv^2)$.
- Force conservative : $\vec F=-\nabla E_p$ ; **TEM** : $\Delta E_m=W_{\text{nc}}$, $E_m=T+E_p$.
- **Système** : $dT/dt=\mathcal P^{\text{ext}}+\mathcal P^{\text{int}}$ ; pour un solide, $\mathcal P^{\text{int}}=0$ et $\mathcal P^{\text{ext}}=\langle\mathscr A,\mathscr V\rangle$.
- **Viriel en dimension $n$** : pour $V$ homogène de degré $k$ (V(λx)=λ^kV(x)) et mouvement borné, $2\langle T\rangle=k\langle V\rangle$. Kepler ($k=-1$) : $\langle T\rangle=-\tfrac12\langle V\rangle=-E$.
- Trois conservations distinctes : énergie **totale** (toujours), $E_m$ (si $W_{\text{nc}}=0$), $E_c$ (seulement chocs élastiques).

## IV.8 Référentiels non galiléens

TRD/TMD dans $\mathscr R'$ : ajouter aux actions les torseurs d'inertie :
$$
\mathscr A^{\text{ie}}\!:\ \vec F_{ie}=-m\,a_e(G)\ \text{(si champ homogène)},\ \ \mathfrak M_{ie}(A)=\int\overrightarrow{AM}\wedge(-a_e)\,dm,\qquad \mathscr A^{\text{ic}}:\ \int-2\Omega v_r\,dm\ \text{etc.}
$$
Pour le barycentre : $\mathfrak M^{\text{ext}}(G)=\mathfrak M^{\text{ext}}(A)+\overrightarrow{AG}\wedge(-m\,a_G)$.

---

# Partie V — Solide rigide : tenseur d'inertie, dynamique

## V.1 Tenseur d'inertie en dimension $n$

Soit $x=\overrightarrow{AM}$ et le tenseur de **second moment** $K_A\doteq\int x\,x^{\mathsf T}dm$ (symétrique, $\geq0$). Pour une rotation $\Omega$ : $v=\Omega x$,
$$
L(A)=\int x\wedge(\Omega x)\,dm=-(K_A\Omega+\Omega K_A)\ \ \Longrightarrow\ \ \mathbb I_A(\Omega)\doteq K_A\Omega+\Omega K_A,\quad L(A)=-\mathbb I_A(\Omega)
$$
($\mathbb I_A\colon\mathfrak{so}(n)\to\mathfrak{so}(n)$ linéaire symétrique). Énergie de rotation : $T_{\text{rot}}=\tfrac12\int|\Omega x|^2dm=\tfrac12\operatorname{tr}(\Omega K\Omega^{\mathsf T})$, et $2T_{\text{rot}}=\langle\mathscr C,\mathscr V\rangle_{\text{rot}}$.

**Cas $n=3$** : avec $K\,[\vec a]_\times+[\vec a]_\times K=[(\operatorname{tr}K\,\mathbb 1-K)\vec a]_\times$ on retrouve $\vec L=I\vec\Omega$, $I=\operatorname{tr}K\,\mathbb 1-K=\int(|x|^2\mathbb 1-xx^{\mathsf T})dm$ (matrice d'inertie classique, moments $I_{ij}=\int(r^2\delta_{ij}-x_ix_j)dm$). **Cas $n=2$** : $I=\int r^2dm$ scalaire, $L=I\omega$.

**Axes principaux.** On diagonalise $K=\operatorname{diag}(k_1,\dots,k_n)$ : les bivecteurs de base $e_i\wedge e_j$ sont propres, de valeur propre $k_i+k_j$ (**moments d'inertie de plan** $I_{ij}=k_i+k_j$). En 3D : $I_1=k_2+k_3$, etc.

**Boule homogène** (rayon $R$, masse $m$, dim $n$) : $K=\dfrac{mR^2}{n+2}\mathbb 1$, donc $\mathbb I=\dfrac{2mR^2}{n+2}\ \ (\kappa_n\doteq\tfrac2{n+2}$ : $\kappa_2=\tfrac12,\ \kappa_3=\tfrac25)$.

## V.2 Théorème de Huygens–Steiner (**[nD]**)

$$
K_A=K_G+m\,\overrightarrow{GA}\,\overrightarrow{GA}^{\mathsf T}\ \ \Longrightarrow\ \ \mathbb I_A(\Omega)=\mathbb I_G(\Omega)+m\big(\overrightarrow{GA}\,\overrightarrow{GA}^{\mathsf T}\Omega+\Omega\,\overrightarrow{GA}\,\overrightarrow{GA}^{\mathsf T}\big).
$$
En 3D, axe parallèle à $\Delta_G$ à distance $d$ : $I_\Delta=I_{\Delta_G}+md^2$.

## V.3 Dynamique du solide

Rotation + translation : $m\,a_G=\vec F^{\text{ext}}$ ; $\dfrac{dL^\ast}{dt}\Big)_{\mathscr R}=\mathfrak M^{\text{ext}}(G)$ avec $L^\ast=-\mathbb I_G(\Omega)$ et $T=\tfrac12mv_G^2+\tfrac12\langle\mathscr C^\ast,\mathscr V^\ast\rangle$.

**Équation d'Euler–Arnold.** Dans le repère propre du solide (où $\mathbb I$ est constant) :
$$
\dot L_b=[L_b,\Omega_b]+M_b,\qquad L_b=-\mathbb I(\Omega_b)\qquad\Big(\text{3D : }I\dot{\vec\Omega}+\vec\Omega\times I\vec\Omega=\vec M\Big).
$$
Géodésique de $SO(n)$ muni de la métrique invariante à gauche $\mathbb I$ en l'absence de couple. Pour $n=3$ : solide symétrique $\Rightarrow$ précession libre à la fréquence $|\Omega_p|=\big|\frac{I_3-I_1}{I_1}\big||\Omega_3|$ dans le repère du solide ; axe intermédiaire instable (théorème de la raquette).

**Rotation autour d'un axe fixe ($n=3$)** : $L_\Delta=I_\Delta\omega$, $I_\Delta\dot\omega=\mathfrak M_\Delta$, $T=\tfrac12I_\Delta\omega^2$.

## V.4 Moments d'inertie usuels ($n=3$, axe de symétrie)

Tige ($\tfrac1{12}ml^2$ centre ⟂), disque ($\tfrac12mR^2$), cerceau ($mR^2$), sphère pleine ($\tfrac25mR^2$), sphère creuse ($\tfrac23mR^2$), cylindre plein ($\tfrac12mR^2$, axe), cône plein ($\tfrac3{10}mR^2$). **Dimension $n$** : boule homogène, $\int r^2dm=\tfrac n{n+2}mR^2$, coquille $\int r^2dm=mR^2$.

## V.5 Exercices types corrigés (résultats)

- **Pendule de Foucault** (latitude $\lambda$) : le plan d'oscillation tourne à $\Omega_F=-\Omega_{T}\sin\lambda$ ; période $2\pi/(\Omega_T\sin\lambda)$ (Paris : $\simeq$ 32 h). Preuve : à petite amplitude, $\ddot{\xi}=-\omega_0^2\xi-2\,\Omega_{T,z}\,\hat z\times\dot{\xi}$ avec $\Omega_{T,z}=\Omega_T\sin\lambda$, résolu par $\xi=u\,e^{-i\Omega_{T,z}t}$.
- **Cerceau roulant sans glisser** sur plan incliné $\alpha$ : $a=\tfrac12g\sin\alpha$ (car $I=mR^2$). Disque : $\tfrac23g\sin\alpha$ ; sphère : $\tfrac57g\sin\alpha$.
- **Perle sur cerceau tournant** (rayon $R$, vitesse $\omega$ autour de l'axe vertical, $\theta$ depuis la verticale basse) : $\ddot\theta=\sin\theta\big(\omega^2\cos\theta-\tfrac gR\big)$ ; bifurcation fourche en $\omega_c^2=g/R$ : pour $\omega>\omega_c$, équilibre $\cos\theta_0=g/(R\omega^2)$ (brisure spontanée de symétrie $\theta\mapsto-\theta$). Ici l'énergie *mécanique* n'est pas conservée (liaison dépendant du temps) mais $H=\sum p\dot q-L$ l'est (**Jacobi**, VI.3).
- **Toupie de Lagrange** : intégrales premières $p_\phi,p_\psi,E$ ; potentiel effectif en $u=\cos\theta$, $\dot u^2=f(u)$ cubique : nutation entre deux racines.

---

# Partie VI — Lagrange, Hamilton, Liouville, Noether, application moment

## VI.1 Formalisme lagrangien

Espace des configurations $Q$ (variété de dimension $d$), **métrique cinétique** $g_{ij}(q)$ ($T=\tfrac12g_{ij}\dot q^i\dot q^j$ ; pour $N$ points libres $Q=\mathbb R^{nN}$ et $g=\operatorname{diag}(m_a\delta)$).
$$
L\colon TQ\times\mathbb R\to\mathbb R,\ (q,\dot q,t)\mapsto L(q,\dot q,t)\doteq T-V,\qquad S[q]\doteq\int_{t_0}^{t_1}L\,dt .
$$
**Euler–Lagrange** : $\delta S=0\Rightarrow\dfrac d{dt}\dfrac{\partial L}{\partial\dot q^i}-\dfrac{\partial L}{\partial q^i}=0$, soit $g_{ij}\big(\ddot q^j+\Gamma^j_{kl}\dot q^k\dot q^l\big)=-\partial_iV$ (géodésique + force).

## VI.2 Hamiltonien, Poisson, Liouville

- **Légendre** : $p_i\doteq\partial L/\partial\dot q^i$, $H(q,p,t)\doteq p_i\dot q^i-L$ ; $\dot q^i=\partial H/\partial p_i$, $\dot p_i=-\partial H/\partial q^i$.
- **Crochet** : $\{f,g\}\doteq\dfrac{\partial f}{\partial q^i}\dfrac{\partial g}{\partial p_i}-\dfrac{\partial f}{\partial p_i}\dfrac{\partial g}{\partial q^i}$ ; $\ \dfrac{df}{dt}=\{f,H\}+\partial_tf$ ; $\{q^i,p_j\}=\delta^i_j$ ; Jacobi.
- **Liouville** : le champ hamiltonien $X_H=(\partial_pH,-\partial_qH)$ est de divergence nulle ; le flot conserve $dq\,dp$ (volume de l'espace des phases).
- **Théorème de Jacobi** : $\dfrac{dH}{dt}=-\dfrac{\partial L}{\partial t}=\dfrac{\partial H}{\partial t}$.

## VI.3 Théorème de Noether (mécanique)

> [!tip] **Noether.** Soit $q\mapsto q+\varepsilon\,\xi(q,t)$ une transformation à un paramètre (éventuellement $t\mapsto t+\varepsilon\tau$) telle que $\delta L=\varepsilon\,\dfrac{dF}{dt}$ sur toute trajectoire (symétrie « quasi-invariante »). Alors
> $$Q\doteq\frac{\partial L}{\partial\dot q^i}\,\xi^i-F=p\cdot\xi-F\qquad\text{est conservé.}$$
> *Preuve.* $\delta L=\partial_qL\,\xi+\partial_{\dot q}L\,\dot\xi=\tfrac d{dt}(p\cdot\xi)$ sur les solutions (EL), d'où $\tfrac d{dt}(p\cdot\xi-F)=0$. $\square$
> Réciproque (hamiltonienne) : $Q$ conservée $\Rightarrow$ $X_Q$ engendre une symétrie ; $\{Q,H\}=0$.

Pour $N$ points $(m_a,x_a)$ avec $L=\sum_a\tfrac12m_a\dot x_a^2-V\big(\{x_a-x_b\}\big)$ :

| Symétrie | Transformation | Charge de Noether | Torseur / théorème |
|---|---|---|---|
| translation $a\in E$ | $x_a\mapsto x_a+\varepsilon a$ | $\vec P=\sum p_a$ | **TRD** (résultante) |
| rotation $\omega\in\mathfrak{so}(n)$ | $x_a\mapsto x_a+\varepsilon\,\omega x_a$ | $L=\sum x_a\wedge p_a$ | **TMC** (moment), force centrale |
| translation en $t$ | $t\mapsto t+\varepsilon$ | $E=H$ | **TEM** ($V$ indép. de $t$) |
| **boost galiléen** $u\in E$ | $x_a\mapsto x_a+\varepsilon\,u\,t$ | $\vec K\doteq m\,\overrightarrow{OG}-\vec P\,t$ | $\dot{\vec K}=0\Leftrightarrow\ddot{\vec G}=0$ ($F=m\,\varepsilon u\cdot x_G$) |
| dilatation $x\mapsto\lambda x$, $t\mapsto\lambda^{2}t$ (seulement pour $V\propto r^{-2}$) | dilatation | $D=\sum p\cdot x-2tE$ | symétrie conforme du potentiel en $1/r^2$ (pour $V\propto r^k$ général : simple loi d'échelle $T\propto R^{1-k/2}$, viriel IV.7) |

> [!note] **Remarques**
> 1. Le torseur « *résultante* $\vec P$, *moment* $L$ » est exactement la charge de Noether de $E(n)=SO(n)\ltimes\mathbb R^n$ ; $\vec K$ (le moment de masse) est la charge du boost.
> 2. **Invariance par rotation $\Rightarrow$ force centrale** : $\{L_{ij},H\}=0\Leftrightarrow\sum_ax_a\wedge F_a=0$.
> 3. **Bargmann** : $\{K_i,P_j\}=m\,\delta_{ij}$ : la masse apparaît comme **extension centrale** de l'algèbre de Galilée (la représentation de Galilée en mécanique quantique est projective).

## VI.4 Algèbre de Poisson des charges et application moment

Avec $L_{ij}=x_ip_j-x_jp_i$, $P_k=p_k$ :
$$
\{L_{ij},P_k\}=\delta_{ik}P_j-\delta_{jk}P_i,\qquad \{L_{ij},L_{kl}\}=-\delta_{jk}L_{il}+\delta_{ik}L_{jl}+\delta_{jl}L_{ik}-\delta_{il}L_{jk},\qquad\{P_i,P_j\}=0 .
$$
C'est $\mathfrak e(n)=\mathfrak{so}(n)\ltimes\mathbb R^n$. En 3D : $\{L_x,L_y\}=L_z$.

**Application moment** (cadre géométrique). Si un groupe $G$ agit sur $Q$ et par relèvement sur $T^\ast Q$ (symplectique), l'application
$$
\mu\colon T^\ast Q\to\mathfrak g^\ast,\qquad\langle\mu(q,p),\xi\rangle\doteq p\cdot\xi_Q(q)
$$
est équivariante : $\mu(g\cdot z)=\mathrm{Ad}^\ast_g\mu(z)$ (à extension centrale près). Pour $G=E(n)$ :
- $\mu=(P,L)\in\mathfrak e(n)^\ast$ : le **torseur cinétique** ;
- $\mathrm{Ad}^\ast_{\text{translation par }a}$ : $(P,L)\mapsto(P,L+a\wedge P)$ = **loi de Varignon**/BABAR ;
- $\mathrm{Ad}^\ast_{g\in SO(n)}$ : $(P,L)\mapsto(gP,\,gLg^{\mathsf T})$.

**Orbites coadjointes** (Kirillov–Souriau). Les orbites de $E(n)$ dans $\mathfrak e(n)^\ast$ sont classées par $|R|$ et la classe de $M_{\min}\in\mathfrak{so}(n-1)^\ast$ (III.3) : en 3D, $|\vec R|$ et l'hélicité $\vec M\cdot\vec R/|\vec R|$ (le **spin**). C'est la version classique de la classification de Wigner (partie X).

---

# Partie VII — Noether pour les champs, Schrödinger, jauge

## VII.1 Théorème de Noether pour un champ

Soit $\varphi^a(x)$ un champ sur $\mathbb R^{1,n}$ (ou $\mathbb R^{n+1}$), $\mathcal L(\varphi,\partial\varphi)$ une densité lagrangienne, $S=\int\mathcal L\,d^{n+1}x$. Pour $\delta\varphi=\varepsilon\,\Phi$ avec $\delta\mathcal L=\varepsilon\,\partial_\mu K^\mu$ :
$$
J^\mu\doteq\frac{\partial\mathcal L}{\partial(\partial_\mu\varphi^a)}\Phi^a-K^\mu,\qquad\partial_\mu J^\mu=0,\qquad Q\doteq\int J^0\,d^nx\ \text{ conservée.}
$$

## VII.2 Tenseur énergie-impulsion et torseur d'un champ

Translations $\Rightarrow$ tenseur canonique $T^\mu{}_\nu\doteq\dfrac{\partial\mathcal L}{\partial(\partial_\mu\varphi)}\partial_\nu\varphi-\delta^\mu_\nu\mathcal L$, $\partial_\mu T^{\mu\nu}=0$. Torseur du champ :
$$
P^\nu\doteq\int T^{0\nu}d^nx,\qquad M^{\mu\nu}\doteq\int\big(x^\mu T^{0\nu}-x^\nu T^{0\mu}\big)d^nx\ (+\text{terme de spin}).
$$
Changement d'origine $x\mapsto x+a$ : $M'^{\mu\nu}=M^{\mu\nu}-a^\mu P^\nu+a^\nu P^\mu$ : **Varignon dans l'espace-temps**. Les composantes spatiales $M^{ij}$ sont le moment cinétique ; $M^{0i}=t\,P^i-\int x^iT^{00}$ est le *moment de boost* (centre d'énergie).

## VII.3 Schrödinger comme théorie de champ

$$
\mathcal L=i\hbar\,\psi^\ast\partial_t\psi-\frac{\hbar^2}{2m}\nabla\psi^\ast\!\cdot\nabla\psi-V\psi^\ast\psi\ \ \Longrightarrow\ \ i\hbar\partial_t\psi=-\frac{\hbar^2}{2m}\Delta\psi+V\psi .
$$
- Invariance $\psi\mapsto e^{i\alpha}\psi$ ($U(1)$ global) $\Rightarrow$ $\rho=|\psi|^2$, $\vec j=\frac\hbar m\operatorname{Im}(\psi^\ast\nabla\psi)$, $\partial_t\rho+\nabla\!\cdot\vec j=0$ (conservation de la probabilité/charge).
- Translations $\Rightarrow\hat{\vec P}=-i\hbar\nabla$ ; rotations $\Rightarrow\hat L_{ij}=-i\hbar(x_i\partial_j-x_j\partial_i)$ ; $[\hat L_{ij},\hat P_k]=i\hbar(\delta_{ik}\hat P_j-\delta_{jk}\hat P_i)$ : on retrouve VI.4 avec $\{\cdot,\cdot\}\to\tfrac1{i\hbar}[\cdot,\cdot]$.
- Boost galiléen $\Rightarrow\psi'(x,t)=e^{\frac i\hbar(mu\cdot x-\frac12mu^2t)}\psi(x-ut,t)$ (phase de Bargmann).

## VII.4 Jauge locale et couplage minimal

Exiger l'invariance sous $\psi\mapsto e^{iq\alpha(x)/\hbar}\psi$ impose $D_\mu\doteq\partial_\mu-\tfrac{iq}\hbar A_\mu$, $A_\mu\mapsto A_\mu+\partial_\mu\alpha$, et $F_{\mu\nu}\doteq\partial_\mu A_\nu-\partial_\nu A_\mu$, $\mathcal L_{\text{Maxwell}}=-\tfrac14F_{\mu\nu}F^{\mu\nu}$. La **charge** est la charge de Noether de $U(1)$ ; elle ne provient pas de l'espace-temps (symétrie interne). Théorème de Noether (second) : une symétrie *locale* donne des identités (loi de Gauss, $\partial_\nu F^{\mu\nu}=j^\mu$ implique $\partial_\mu j^\mu=0$), non plus des charges indépendantes. **Gravité** = jauge des translations/difféomorphismes (XIV).

---

# Partie VIII — Problème de Kepler, vecteur de Runge–Lenz–Laplace, $SO(n+1)$

## VIII.1 Classique, dimension $n$

$H=\dfrac{p^2}{2m}-\dfrac kr$ ($k>0$). Charges : $E$, $L_{ij}=x_ip_j-x_jp_i$ (donc mouvement plan), et le **vecteur RLL**
$$
A^i\doteq L^{ij}p_j-mk\,\frac{x^i}r\qquad\Big(\text{3D : }\vec A=\vec p\times\vec L-mk\,\hat r\Big).
$$
Propriétés : $\{A_i,H\}=0$ ; $A\cdot L=0$ ; $A^2=m^2k^2+2mE\,L^2$ (où $L^2\doteq\tfrac12L_{ij}L^{ij}$).
**Trajectoire** : $\vec A\cdot\vec r=Ar\cos\theta=L^2-mkr\Rightarrow$
$$
r(\theta)=\frac{p}{1+e\cos\theta},\quad p=\frac{L^2}{mk},\ e=\frac{|A|}{mk}=\sqrt{1+\frac{2EL^2}{mk^2}} .
$$
**Hodographe** : $p$ décrit un cercle de rayon $mk/L$ de centre déporté de $A/L$ (cercle de vitesses : cf. IX).

> [!note] Dans $\mathbb R^n$, le potentiel « de Kepler » naturel est $1/r^{n-2}$ (solution fondamentale du laplacien, I.3) ; le résultat $SO(n+1)$ ci-dessous vaut pour le potentiel en $1/r$ **en dimension $n$** (cas de Bertrand), pas pour $1/r^{n-2}$.

## VIII.2 Algèbre hamiltonienne et trois régimes

$\{L_{ij},A_k\}=\delta_{ik}A_j-\delta_{jk}A_i$ (vecteur), et
$$
\{A_i,A_j\}=-2mH\,L_{ij}\quad(\text{à la convention de signe près selon }L_{ij}).
$$
En posant, pour $E<0$, $D_i\doteq A_i/\sqrt{-2mE}$, on obtient $\{D_i,D_j\}=L_{ij}$ : $\mathfrak{so}(n+1)$ ; $E>0$ : $\mathfrak{so}(n,1)$ ; $E=0$ : $\mathfrak e(n)$. **Compte** : $\tfrac{n(n-1)}2+n=\tfrac{n(n+1)}2=\dim\mathfrak{so}(n+1)=\dim\mathfrak e(n)$ : le couple $(L,A)$ a autant de composantes qu'un torseur de $\mathbb R^n$.
- **Fock–Moser** : la projection stéréographique de l'espace des impulsions $\mathbb R^n$ sur $S^n$ transforme le flot de Kepler à $E<0$ en flot géodésique sur $S^n$ (grands cercles) ; $SO(n+1)$ est la symétrie isométrique de $S^n$.
- $n=3$ : $\mathfrak{so}(4)=\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ via $J^\pm=\tfrac12(L\pm D)$.

## VIII.3 Version quantique (Pauli)

$\hat A=\frac1{2m}(\hat p\times\hat L-\hat L\times\hat p)-k\hat r/r$, $[\hat A_i,\hat A_j]=-\tfrac{2i\hbar}m\hat H\varepsilon_{ijk}\hat L_k$. Pour $H<0$, $\hat D=\sqrt{-m/2\hat H}\,\hat A$, $[\hat D_i,\hat D_j]=i\hbar\varepsilon_{ijk}\hat L_k$ ; $j^+=j^-=j$ (car $L\cdot D=0$), $N=2j+1$ :
$$
E_N=-\frac{mk^2}{2\hbar^2N^2},\qquad\text{dégénérescence }N^2=\sum_{\ell=0}^{N-1}(2\ell+1).
$$
**Dimension $n$** : représentation de $\mathfrak{so}(n+1)$ à $\ell$ **symétrique sans trace** de $\mathfrak{so}(n+1)$ (harmoniques sphériques sur $S^n$) :
$$
E_\ell=-\frac{mk^2}{2\hbar^2\big(\ell+\tfrac{n-1}2\big)^2},\qquad g_\ell=\binom{\ell+n}{n}-\binom{\ell+n-2}{n}\quad(\ell\in\mathbb N).
$$
Contrôle : $n=3$, $\ell=N-1$ : $g=N^2$ ; $n=2$ : $E=-\frac{2mk^2}{\hbar^2(2\ell+1)^2}$, $g=2\ell+1$.
**Brisure** : tout écart à $1/r$ ($1/r^3$ relativiste, effet Lamb, potentiel écranté) brise $SO(n+1)\to SO(n)$ et lève la dégénérescence en $\ell$.

## VIII.4 Perturbation : précession de $A$ et périhélie de Mercure

Pour $H=H_0+\delta H$ : $\dot A_i=\{A_i,\delta H\}$ ; moyenne sur l'orbite $\Rightarrow$ rotation de $\vec A$ dans le plan. Pour $\delta V=-\beta/r^3$ :
$$
\Delta\varphi_{\text{orbite}}=\frac{6\pi m\beta}{L^2\,p}\qquad\Big(p=\frac{L^2}{mk}\Big).
$$
**Relativité générale (Schwarzschild)** : le terme post-newtonien $\beta=GML^2/(mc^2)$ ($\beta$ est alors proportionnelle à $L^2$) donne
$$
\boxed{\Delta\varphi=\frac{6\pi GM}{c^2\,a(1-e^2)}\ \text{rad par révolution}}\ \Longrightarrow\ \text{Mercure : }0{,}1038''\text{ par orbite}\simeq43''\text{ par siècle}.
$$
Décomposition du total observé ($\simeq5600''$/siècle) : $\simeq5025''$ (précession des équinoxes, repère) $+\ \simeq532''$ (perturbations newtoniennes des autres planètes) $+\ 43''$ (relativité). Lecture en termes de symétrie : la précession mesure la brisure de $SO(4)$ par le $1/r^3$.
Dérivation par Schwarzschild : $u=1/r$, $u''+u=\frac{GM}{\ell^2}+\frac{3GM}{c^2}u^2$ ; solution perturbative $u=\frac1p\big[1+e\cos((1-\varepsilon)\varphi)\big]$, $\varepsilon=\frac{3GM}{c^2p}$, $\Delta\varphi\simeq2\pi\varepsilon=6\pi GM/(c^2p)$.

---

# Partie IX — Collisions : de la boule de billard à la dimension $n$

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

---

# Partie X — Relativité restreinte : torseurs de Poincaré

## X.1 Quadri-impulsion et chocs relativistes

Signature $(-+\cdots+)$ ou $(+-\cdots-)$ au choix ; ici $\eta=\operatorname{diag}(-1,1,\dots,1)$, $D=n+1$. $p^\mu=(E/c,\gamma m\vec v)$, $E=\gamma mc^2$, $\gamma=(1-v^2/c^2)^{-1/2}$, $E^2=(pc)^2+(mc^2)^2$, $p_\mu p^\mu=-m^2c^2$.
Dans un choc d'un système isolé, c'est **$P^\mu=\sum p^\mu_i$** (quadri-vecteur) qui est conservé ; la masse **n'est pas additive** : $Mc^2=\sqrt{(\sum E_i)^2-\|\sum\vec p_ic\|^2}$.
- Deux boules d'argile à $\pm0{,}6c$ qui fusionnent : $M=2\gamma m=2{,}5m$.
- **Invariant** $s\doteq(\sum E_i)^2-\|\sum\vec p_ic\|^2$ : seuil de création de paires. Proton sur cible fixe : $s=2m^2c^4(1+\gamma)\ge(4mc^2)^2\Rightarrow\gamma\ge7$ ($E_c=6mc^2\simeq5{,}6$ GeV, Bevatron 1955) ; collisionneur symétrique $\sqrt s=2\gamma mc^2$ ($\gamma\ge2$ suffit). LHC $\sqrt s=13{,}6$ TeV $\Leftrightarrow$ cible fixe $\simeq10^{17}$ eV.
- **Règle des $90^\circ$** : masses égales, $B$ au repos, élastique : $\tan\theta_A\tan\theta_B=\dfrac2{\gamma+1}$ ; $\gamma\to1$ : $\theta_A+\theta_B=90^\circ$, sinon $<90^\circ$.

## X.2 Groupe et algèbre de Poincaré, torseurs

$\mathrm{ISO}(1,n)=SO(1,n)\ltimes\mathbb R^{1,n}$, $\dim=\tfrac{(n+1)(n+2)}2$ : même structure que $E(n+1)$ avec une métrique lorentzienne. Un **torseur de Poincaré** est le couple
$$
\{P^\mu;\ M^{\mu\nu}\},\qquad M^{\mu\nu}(a)=M^{\mu\nu}(0)-a^\mu P^\nu+a^\nu P^\mu\quad(\text{Varignon}).
$$
Charges de Noether : $P^\mu$ (translations), $M^{ij}$ (rotations), $M^{0i}=t\,P^i-E\,x_E^i/c^2$ (boosts ; limite $c\to\infty$ : le moment de masse $\vec K=m\vec x_G-\vec Pt$ de VI.3). Algèbre :
$$
[P_\mu,P_\nu]=0,\quad[M_{\mu\nu},P_\rho]=i\hbar(\eta_{\nu\rho}P_\mu-\eta_{\mu\rho}P_\nu),\quad[M_{\mu\nu},M_{\rho\sigma}]=i\hbar(\eta_{\nu\rho}M_{\mu\sigma}-\eta_{\mu\rho}M_{\nu\sigma}-\eta_{\nu\sigma}M_{\mu\rho}+\eta_{\mu\sigma}M_{\nu\rho}).
$$
*Contraction* : $c\to\infty$ donne Galilée ; avec la masse comme extension centrale : Bargmann.

## X.3 Invariants, classification de Wigner

- Casimir 1 : $P^2=-M^2c^2$ (la masse). Casimir 2 : $W\doteq\star(M\wedge P)$, i.e. en $D=4$ le **vecteur de Pauli–Lubański** $W_\mu=\tfrac12\varepsilon_{\mu\nu\rho\sigma}M^{\nu\rho}P^\sigma$ ; $W^2=m^2c^2\hbar^2s(s+1)$ pour $m>0$ ; $W^\mu=\lambda P^\mu$ si $m=0$ (hélicité).
- **C'est l'invariant $M\wedge R$ de III.3 transposé à l'espace-temps** : le spin d'une particule est l'invariant du torseur de Poincaré, comme l'hélicité $\vec M\cdot\vec R/|R|$ en 3D. Les orbites coadjointes de $\mathrm{ISO}(1,3)$ (VI.4) $\leftrightarrow$ représentations unitaires irréductibles (Wigner).
- Groupe d'invariance du petit groupe : $SO(n)$ ($m>0$), $ISO(n-1)$ ($m=0$), etc.

---

# Partie XI — Quantités conservées et équilibre statistique (GE et GGE)

**Invariants de collision** (gaz de boules identiques, dimension $n$) : $1$, $\vec v$, $v^2$ ; ajouter $L$ du gaz $\Rightarrow$ $1+1+n+\tfrac{n(n-1)}2$ constantes. Théorème $H$ (Boltzmann) : stationnaire $\ln f=a+\vec b\cdot\vec v+c\,v^2$ (Maxwell–Boltzmann).

**Ensembles de Gibbs (GE)** : maximiser l'entropie sous contraintes $\langle Q_k\rangle$ donne $\rho\propto\exp(-\sum_k\lambda_kQ_k)$ :

| Situation | Distribution | Conservées |
|---|---|---|
| isolé | microcanonique | $E$ |
| échange d'énergie | canonique $e^{-\beta H}$ | $\langle E\rangle$ |
| énergie + particules | grand-canonique $e^{-\beta(H-\mu N)}$ | $\langle E\rangle,\langle N\rangle$ |
| gaz en mouvement et rotation | $\exp[-\beta(H-\vec u\cdot\vec P-\Omega:L)]$ | $E,\vec P,L$ |

**Le multiplicateur de Lagrange du torseur cinétique est le torseur cinématique** : dans la dernière ligne, $(\vec u,\Omega)\doteq$ $\mathscr V$ (vitesse d'entraînement, rotation d'ensemble) est conjugué du torseur $(\vec P,L)$ par $\lambda_k$ — l'équilibre « fait tourner » le système comme un solide.

**Quand il y a trop de constantes du mouvement.** 1D, masses égales : chaque choc élastique **échange les vitesses**, donc $\sum_i\varphi(v_i)$ est conservée pour toute $\varphi$ : infinité d'invariants, système **intégrable** (bâtonnets durs ; Lieb–Liniger, ansatz de Bethe). Le gaz ne thermalise pas.
Simulation : $N=4000$ boules, départ $\pm1$ : en 2D, relaxation vers la gaussienne ($\langle v_x^4\rangle=0{,}78\simeq3\langle v_x^2\rangle^2=0{,}75$) ; en 1D, aucun changement.
**GGE** : $\rho_{\text{GGE}}=Z^{-1}\exp(-\sum_k\lambda_kQ_k)$, $\lambda_k$ fixés par $\langle Q_k\rangle_{\text{GGE}}=\langle Q_k\rangle_{\text{départ}}$ (Rigol et al. 2007) ; expérience : berceau de Newton quantique (Kinoshita–Wenger–Weiss 2006), hydrodynamique généralisée (Castro-Alvaredo–Doyon–Yoshimura, Bertini et al. 2016).
Mise en garde : conservation d'une grandeur $\ne$ ensemble statistique ; plus il y a de conservées, plus l'équilibre « se souvient » de l'état initial.

---

# Partie XII — Supersymétrie ★★★

> [!info] Statut
> Cadre mathématique rigoureux (superalgèbres, théorème de Coleman–Mandula, HLS, indice de Witten) ; **aucune superparticule n'a été observée** à ce jour. Les formules explicites en notation à deux composantes suivent les conventions de Wess–Bagger, **au signe et au facteur de convention près**.

## XII.1 Pourquoi des symétries fermioniques

- **Coleman–Mandula (1967)** : dans une théorie quantique des champs relativiste avec matrice $S$ non triviale (et écart de masse), l'algèbre de Lie des symétries de $S$ est $\mathfrak{iso}(1,3)\oplus\mathfrak g_{\text{interne}}$ : on ne peut **pas** mélanger spin et symétrie interne avec des générateurs bosoniques.
- **Haag–Łopuszański–Sohnius (1975)** : l'unique échappatoire est d'autoriser des générateurs **fermioniques** : algèbres de Lie **graduées** (superalgèbres). La symétrie la plus générale est le **super-Poincaré**.

## XII.2 Superalgèbres de Lie

Un espace $\mathfrak g=\mathfrak g_0\oplus\mathfrak g_1$ ($\mathbb Z_2$-gradué) avec un **super-crochet** $[\cdot,\cdot\}$ : commutateur sur $\mathfrak g_0\times\mathfrak g_0$ et $\mathfrak g_0\times\mathfrak g_1$ ; **anticommutateur symétrique** sur $\mathfrak g_1\times\mathfrak g_1$ :
$$
[X,Y\}=-(-1)^{|X||Y|}[Y,X\},\qquad(-1)^{|X||Z|}[X,[Y,Z\}\}+\text{(perm. cycliques)}=0\ \ (\text{super-Jacobi}).
$$
Les paramètres de transformation fermioniques sont des **nombres de Grassmann** ($\epsilon_1\epsilon_2=-\epsilon_2\epsilon_1$).

## XII.3 Super-Poincaré ($\mathcal N=1$, $D=4$)

Générateurs : $P_\mu$, $M_{\mu\nu}$ (Poincaré, X.2) et supercharges $Q_\alpha,\bar Q_{\dot\alpha}$ (spineurs de Weyl) :
$$
\{Q_\alpha,\bar Q_{\dot\beta}\}=2\,\sigma^\mu_{\alpha\dot\beta}P_\mu,\qquad\{Q_\alpha,Q_\beta\}=0=\{\bar Q_{\dot\alpha},\bar Q_{\dot\beta}\},\qquad[P_\mu,Q_\alpha]=0,\qquad[M_{\mu\nu},Q_\alpha]\propto(\sigma_{\mu\nu})_\alpha{}^\beta Q_\beta .
$$
**Lecture « torseur »** : $Q$ est une « racine carrée » de la translation ; le *super-torseur* $\{P^\mu;M^{\mu\nu};Q\}$ se transporte par Varignon *sans* mélange de $Q$ (car $[P,Q]=0$), mais $Q$ tourne sous $M$.
**Version étendue** $\mathcal N$ : $\{Q^I_\alpha,\bar Q_{J\dot\beta}\}=2\delta^I_J\sigma^\mu_{\alpha\dot\beta}P_\mu$, $\{Q^I_\alpha,Q^J_\beta\}=\varepsilon_{\alpha\beta}Z^{IJ}$ avec **charges centrales** $Z^{IJ}$ (antisymétriques, commutant avec tout) ; **symétrie R** $U(\mathcal N)$ des $Q$.

**Conséquences immédiates** :
1. $\sum_\alpha\{Q_\alpha,Q_\alpha^\dagger\}=4P^0=4H$ ⟹ $\boxed{H\geq0}$ ; l'énergie du vide est nulle ssi la supersymétrie n'est pas brisée.
2. $[P^2,Q]=0$ ⟹ les membres d'un supermultiplet ont **même masse** ; $(-1)^F$ anticommute avec $Q$ ⟹ autant de degrés de liberté bosoniques que fermioniques (hors vide).
3. Représentations : massless $\mathcal N=1$ : hélicités $(\lambda,\lambda+\tfrac12)$ ; multiplet chiral $(\phi,\psi)$ spin $(0,\tfrac12)$ ; vectoriel $(A_\mu,\lambda)$ spin $(1,\tfrac12)$.

## XII.4 Noether et superespace

- **Supercourant** $S^\mu_\alpha$, $\partial_\mu S^\mu_\alpha=0$, $Q_\alpha=\int S^0_\alpha\,d^3x$ : charge de Noether d'une symétrie à paramètre de Grassmann ; $[\epsilon Q+\bar\epsilon\bar Q,\phi]=\delta_\epsilon\phi$ (crochets gradués).
- **Algèbre sur les champs** : $[\delta_{\epsilon_1},\delta_{\epsilon_2}]\phi=-2i\,(\epsilon_1\sigma^\mu\bar\epsilon_2-\epsilon_2\sigma^\mu\bar\epsilon_1)\,\partial_\mu\phi$ : deux supersymétries successives *font une translation*.
- **Superespace** $(x^\mu,\theta^\alpha,\bar\theta^{\dot\alpha})$, $\theta$ de Grassmann. La super-translation $(\xi,\epsilon)$ agit par
$$
\theta\mapsto\theta+\epsilon,\qquad x^\mu\mapsto x^\mu+\xi^\mu+i(\theta\sigma^\mu\bar\epsilon-\epsilon\sigma^\mu\bar\theta),\qquad Q_\alpha=\partial_{\theta^\alpha}-i\sigma^\mu_{\alpha\dot\alpha}\bar\theta^{\dot\alpha}\partial_\mu .
$$
Un superchamp chiral : $\Phi=\phi+\sqrt2\theta\psi+\theta\theta F$.

## XII.5 Modèle de Wess–Zumino

Multiplet chiral $(\phi,\psi,F)$ avec superpotentiel holomorphe $W(\phi)$ :
$$
\mathcal L=-\partial_\mu\phi^\ast\partial^\mu\phi-i\bar\psi\bar\sigma^\mu\partial_\mu\psi+F^\ast F+\Big[W'(\phi)F-\tfrac12W''(\phi)\psi\psi+\text{h.c.}\Big].
$$
$F$ est auxiliaire : $F=-W'^\ast$, d'où $V(\phi)=|W'(\phi)|^2\ge0$. **Brisure spontanée** $\Leftrightarrow$ $W'(\phi)=0$ sans solution (O'Raifeartaigh) $\Rightarrow V_{\min}>0$, apparition d'un **goldstino**. **Théorèmes de non-renormalisation** (Grisaru–Siegel–Roček) : $W$ n'est pas corrigé perturbativement ; les divergences quadratiques se compensent boson/fermion (motivation : problème de hiérarchie).

## XII.6 Mécanique quantique supersymétrique et indice de Witten

$\mathcal H=\mathcal H_B\oplus\mathcal H_F$, $Q$ nilpotent ($Q^2=0$), $H\doteq\{Q,Q^\dagger\}\ge0$. Exemple $\mathcal N=2$ : $H=\tfrac12\big(p^2+W'(x)^2\big)+\tfrac\hbar2W''(x)\,\sigma_3$.
> [!tip] **Indice de Witten** $\ \operatorname{Tr}(-1)^Fe^{-\beta H}=n_B^{E=0}-n_F^{E=0}$, indépendant de $\beta$ et des déformations continues.
> *Preuve.* Les états $E>0$ sont appariés par $Q$ (bosons $\leftrightarrow$ fermions) et se compensent.

**Réalisation géométrique** (Witten 1982) : sur une variété riemannienne compacte $(M,g)$, $\mathcal H=\Omega^\bullet(M)$ (formes différentielles, $(-1)^F=(-1)^{\deg}$), $Q=d$, $Q^\dagger=\delta$, $H=\{d,\delta\}=\Delta_{\text{Hodge}}$. Alors $E=0\Leftrightarrow$ forme harmonique, et $\operatorname{Tr}(-1)^F=\sum(-1)^kb_k=\chi(M)$ (**caractéristique d'Euler**). Retour aux opérateurs de la partie I : le laplacien de Laplace–Beltrami est le $H$ de la SUSY-QM.

## XII.7 États BPS et classification

- Avec charges centrales : $M\ge|Z|$ (borne de **Bogomolny–Prasad–Sommerfield**) ; les états saturant la borne préservent une fraction de la SUSY, forment des multiplets courts, et leur masse est exacte (protégée).
- **Nahm (1978)** : une théorie avec particules de spin $\le2$ a au plus **32 supercharges réelles**, donc $D\le11$.

| $D$ | spineur minimal | supercharges max | théorie |
|---|---|---|---|
| 4 | Majorana (4 réelles) | 32 ($\mathcal N=8$) | sugra $\mathcal N=8$ |
| 10 | Majorana–Weyl (16) | 32 | IIA, IIB (32) ; I, hétérotique (16) |
| 11 | Majorana (32) | 32 | supergravité à 11 dimensions |

## XII.8 Phénoménologie (statut)

MSSM : un superpartenaire par particule du Modèle Standard, symétrie $R$-parité $\Rightarrow$ particule stable (neutralino, candidat matière noire) ; unification des constantes de couplage vers $\sim2\times10^{16}$ GeV. **Aucun signal au LHC** à ce jour : des limites de l'ordre du TeV pèsent sur gluinos/squarks (modèles dépendants). La supersymétrie reste surtout un outil mathématique central (sugra, cordes, QFT exactes).

---

# Partie XIII — Supergravité ★★★

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

---

# Partie XIV — Gravitation quantique ★★★

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

---

# Partie XV — Théorie des cordes et théorie M ★★★

## XV.1 La corde et son torseur

Action de Nambu–Goto, puis de Polyakov ($\gamma_{ab}$ métrique auxiliaire) :
$$
S_{NG}=-T\int d^2\sigma\sqrt{-\det h_{ab}},\ \ h_{ab}\doteq\partial_aX^\mu\partial_bX_\mu,\ \ T=\frac1{2\pi\alpha'}=\frac1{2\pi\ell_s^2};\qquad S_P=-\frac T2\int d^2\sigma\sqrt{-\gamma}\,\gamma^{ab}\partial_aX\cdot\partial_bX .
$$
**Torseur de la corde** (système continu de III.5) : $P^\mu=T\int d\sigma\,\partial_\tau X^\mu$, $M^{\mu\nu}=T\int d\sigma(X^\mu\partial_\tau X^\nu-X^\nu\partial_\tau X^\mu)$, avec la même loi de transport de Varignon.
**Cohérence quantique** (annulation de l'anomalie conforme) : $D=26$ (bosonique) ; $D=10$ (superstring : RNS/Green–Schwarz). Le spectre fermé contient un **graviton** $g_{\mu\nu}$, un champ $B_{\mu\nu}$, un dilaton $\Phi$ ($g_s=e^{\langle\Phi\rangle}$) : la gravitation est incluse automatiquement ; $2\kappa_{10}^2=(2\pi)^7g_s^2\ell_s^8$.

## XV.2 Cinq théories de supercordes et dualités

| Théorie | Supercharges | Jauge |
|---|---|---|
| Type I | 16 | $SO(32)$ |
| Type IIA | 32 | — |
| Type IIB | 32 (chirale) | — |
| Hétérotique $SO(32)$ | 16 | $SO(32)$ |
| Hétérotique $E_8\times E_8$ | 16 | $E_8\times E_8$ |

Annulation d'anomalies de Green–Schwarz (1984) $\Rightarrow$ $SO(32)$ ou $E_8\times E_8$. **Dualités** : T ($R\leftrightarrow\ell_s^2/R$) ; S de IIB ($g_s\to1/g_s$, $SL(2,\mathbb Z)$) ; type I $\leftrightarrow$ hétérotique $SO(32)$ ($g_s\to1/g_s$).

## XV.3 Théorie M (Witten 1995)

À fort couplage, IIA devient une théorie à **11 dimensions** de rayon $R_{11}=g_s\ell_s$ :
$$
\ell_{11}=g_s^{1/3}\ell_s,\qquad2\kappa_{11}^2=(2\pi)^8\ell_{11}^9,\qquad\text{limite basse énergie}=\text{sugra à 11D (XIII.2)}.
$$
- Les **D0-branes** sont les modes de Kaluza–Klein ($m=1/R_{11}=1/g_s\ell_s$) : leur charge est la charge de Noether de l'isométrie $\partial_{11}$ (XIII.3).
- **Membranes** : M2 ($T_{M2}=\frac1{(2\pi)^2\ell_{11}^3}$) et M5 ($T_{M5}=\frac1{(2\pi)^5\ell_{11}^6}$), charges $Z_2,Z_5$ de la superalgèbre. M2 enroulée sur le cercle $\Rightarrow$ corde F1 de IIA : $T_{F1}=2\pi R_{11}T_{M2}=\frac1{2\pi\ell_s^2}$ ✓ ; M2 non enroulée $\Rightarrow$ D2 ; M5 enroulée $\Rightarrow$ D4, non enroulée $\Rightarrow$ NS5.
- **Hořava–Witten** : $E_8\times E_8$ hétérotique $=$ théorie M sur l'intervalle $S^1/\mathbb Z_2$, un $E_8$ sur chaque bord.
- **Théorie des matrices** (Banks–Fischler–Shenker–Susskind 1996) : M-théorie en moment infini $\simeq$ mécanique quantique supersymétrique **de $N$ D0-branes** à $N\to\infty$, $H\propto\operatorname{tr}\big(\Pi_i^2-\tfrac12[X^i,X^j]^2\big)+\text{fermions}$, avec $X^i\in\mathfrak u(N)$ (9 matrices) : les positions deviennent **non commutatives**.
- **AdS/CFT** (XIV.5) : $AdS_4\times S^7\leftrightarrow$ théorie ABJM ($N$ M2) ; $AdS_7\times S^4\leftrightarrow$ théorie $(2,0)$ en $D=6$ ($N$ M5).

## XV.4 Compactifications et statut

$4+7=11$ : théorie M sur une variété d'holonomie $G_2$ $\Rightarrow\mathcal N=1$, $D=4$ ; cordes sur Calabi–Yau $CY_3$. Flux et $\sim10^{500}$ vides estimés (paysage ; estimation heuristique) ; programme du « marais » (swampland). **Statut** : cohérence mathématique remarquable, dualités précises, AdS/CFT nonperturbatif ; **pas de confirmation expérimentale** ni de définition nonperturbative complète indépendante en espace plat. Ce qu'il faut retenir de l'ensemble XII–XV : à chaque palier, **le groupe de symétrie s'étend** (Poincaré $\to$ super-Poincaré $\to$ symétries locales $\to$ dualités), et les charges du torseur $\{P;M\}$ sont enrichies ($Q$, $Z_2$, $Z_5$, $D$-charges).

---

# Partie XVI — Synthèse, pièges, bibliographie

## XVI.1 Tableau de synthèse : symétrie $\leftrightarrow$ charge $\leftrightarrow$ théorème

| Groupe | Générateurs | Charge de Noether | Théorème « mécanique » |
|---|---|---|---|
| translations $\mathbb R^n$ | $P_i$ | $\vec P$ | TRD |
| rotations $SO(n)$ | $L_{ij}$ | $L=\sum x\wedge p$ | TMC, forces centrales |
| temps | $H$ | $E$ | TEM |
| boosts galiléens | $K_i$ | $m\vec x_G-\vec Pt$ | mouvement de $G$ rectiligne uniforme |
| $E(n)$ | $(P,L)$ | **torseur** | Varignon $=\mathrm{Ad}^\ast$ |
| $SO(n+1)$ (Kepler) | $(L,A)$ | RLL | fermeture des orbites |
| $U(1)$ | $Q$ | charge électrique/proba | continuité |
| Poincaré | $(P^\mu,M^{\mu\nu})$ | spin = $\star(M\wedge P)$ | Wigner |
| super-Poincaré | $(P,M,Q)$ | $Q$ fermionique | $H\ge0$, BPS |
| difféomorphismes | $\xi^\mu$ | $T^{\mu\nu}$ conservé, $H\approx0$ | Einstein–Cartan, ADM |

## XVI.2 Pièges classiques

1. $\doteq$ pour *définir*, $=$ pour *démontrer* ; ne pas écrire $=$ à la place d'une définition.
2. Le produit vectoriel et « le moment est un vecteur » n'existent qu'en **3D** ; en général $M\in\Lambda^2E$. Signes : $M^{ij}=\varepsilon^{ijk}M_k$ mais $\Omega^{ij}=-\varepsilon^{ijk}\Omega_k$.
3. Le torseur cinématique $\{\Omega;v\}$ est de type **vitesse** ($v(B)=v(A)+\Omega\overrightarrow{AB}$) ; les autres de type **moment** ($M(B)=M(A)+\overrightarrow{BA}\wedge R$).
4. $D(A)=\dot L(A)+v_A\wedge P$ ; $D(A)=\dot L(A)$ seulement pour $A$ fixe ou $A=G$.
5. $E_{\text{totale}}$ conservée toujours ; $E_m$ sous conditions ; $E_c$ seulement pour les chocs élastiques ; **$\vec P$ se conserve même si $E_c$ non**.
6. $e\neq\alpha=E_c'/E_c$ ; $\alpha=e^2$ cas particulier seulement.
7. Règle des $90^\circ$ : masses égales, cible immobile, élastique, **sans rotation ni frottement**.
8. $L$ conservé avec la forme **forte** de la 3e loi.
9. Noether donne les charges des symétries **globales** ; les symétries locales donnent des identités (Noether II) et des contraintes.

## XVI.3 Exercices pour continuer

1. $(\star)$ Fusée $m_0=100$ t, $v_e=3$ km/s, $\Delta V=6$ km/s : $m_f/m_0=e^{-2}$, soit $\simeq86{,}5\%$ de carburant.
2. $(\star\star)$ Fronde frontale à contre-courant : $v_f=v_i+2U$ en norme ; pourquoi aucun gain depuis l'infini dans $\mathscr R_{\text{planète}}$.
3. $(\star\star)$ Collisionneur vs cible fixe pour des protons de 7 TeV : $\sqrt s=14$ TeV contre $\sqrt{2mc^2E}\simeq114$ GeV ; énergie équivalente cible fixe $\approx10^8$ GeV.
4. $(\star\star\star)$ Boules identiques en 1D : $\sum v_i^3$ conservée ; à masses différentes, faux en général.
5. $(\star\star)$ Montrer en dimension $n$ que le couple $(L,A)$ de Kepler a $\tfrac{n(n+1)}2$ composantes ; calculer $\{A_i,A_j\}$.
6. $(\star\star\star)$ Montrer que $M\wedge R$ est invariant de transport (III.3) et le relier à l'hélicité.
7. $(\star\star\star)$ SUSY-QM : vérifier que $H=\{d,\delta\}$ sur $S^2$ donne $\operatorname{Tr}(-1)^F=2$.
8. $(\star\star\star)$ Retrouver $T_{F1}=1/2\pi\ell_s^2$ à partir de $T_{M2}$ enroulée (fait en XV.3) puis $T_{D4}$ à partir de $T_{M5}$.

## XVI.4 Bibliographie

**Mécanique** : J. Fillette, J. Froustey, H. Roussille, *Physique pour l'agrégation* ; S. Olivier, H. Gié, J.-P. Sarmant, *Physique Spé PC\*/PC* ; B. Hauchecorne, *Formulaire MPSI-MP* ; B. Beaufils, *Formulaire PCSI-MPSI/PTSI-PSI* ; J. R. Taylor, *Classical Mechanics* (2005) ; L. Landau & E. Lifchitz, *Mécanique* (Mir, 1966) ; V. I. Arnold, *Méthodes mathématiques de la mécanique classique* ; J.-M. Souriau, *Structure des systèmes dynamiques* (1970) ; R. Abraham & J. Marsden, *Foundations of Mechanics*.
**Symétries** : E. Noether, *Invariante Variationsprobleme* (1918) ; V. Bargmann (1954) ; V. Fock, *Z. Phys.* 98 (1935) ; W. Pauli, *Z. Phys.* 36 (1926) ; E. Wigner (1939).
**Collisions et GGE** : M. Rigol et al., PRL 98, 050405 (2007) ; T. Kinoshita, T. Wenger, D. Weiss, Nature 440, 900 (2006) ; E. Lieb & W. Liniger, Phys. Rev. 130, 1605 (1963) ; O. Castro-Alvaredo, B. Doyon, T. Yoshimura, PRX 6, 041065 (2016) ; B. Bertini et al., PRL 117, 207201 (2016).
**Gravité/relativité** : B. P. Abbott et al. (LIGO/Virgo), PRL 116, 061102 (2016) ; P. Touboul et al. (MICROSCOPE), PRL 129, 121102 (2022).
**SUSY, sugra** : Coleman–Mandula (1967) ; Haag–Łopuszański–Sohnius (1975) ; J. Wess & J. Bagger, *Supersymmetry and Supergravity* ; E. Witten, *Nucl. Phys. B* 202 (1982) ; Freedman–Van Proeyen, *Supergravity* ; Cremmer–Julia–Scherk (1978) ; Nahm (1978).
**Gravité quantique, cordes** : C. Rovelli, *Quantum Gravity* ; C. Kiefer, *Quantum Gravity* ; J. Donoghue, PRD 50 (1994) ; J. Polchinski, *String Theory* ; Becker–Becker–Schwarz ; E. Witten, *Nucl. Phys. B* 443 (1995) ; Hořava–Witten (1996) ; Banks–Fischler–Shenker–Susskind (1997) ; J. Maldacena, *Adv. Theor. Math. Phys.* 2 (1998).

*Fin du document.*
