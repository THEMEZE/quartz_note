---
title: Relativité générale — de la géométrie aux équations d'Einstein
tags:
  - Physique
  - Relativite-generale
lang: fr
---

> Retour : [[00_Index]] · maths : [[01_Varietes_differentielles]], [[04_Connexions]] · avant : [[02_Relativite_restreinte_Poincare]], [[03_Jauge_EM_YM_Gravite]] · suite : [[11_Schwarzschild_trou_noir]]
> Unités : $G=c=1$ sauf mention ; signature $(-+++)$ ; $\kappa=8\pi G/c^4$.

# Relativité générale : équations d'Einstein

## 1. Principes

1. **Principe d'équivalence** : localement, la gravité est effaçable (cabine en chute libre), donc il existe en tout point un repère localement inertiel où $g_{\mu\nu}=\eta_{\mu\nu}$, $\partial_\lambda g_{\mu\nu}=0$ ; l'égalité masse inertielle/grave ($10^{-15}$ près, MICROSCOPE) en est le principe.
2. **Covariance générale** : les lois s'écrivent de façon tensorielle ; le groupe de symétrie est $\mathrm{Diff}(M)$.
3. **Géométrisation** : l'espace-temps est une variété lorentzienne $(M,g)$ ([[01_Varietes_differentielles]]) ; les corps libres suivent des **géodésiques**, la matière courbe $g$.

## 2. Géométrie : Christoffel, Riemann, Ricci, Einstein

Connexion de Levi-Civita ([[04_Connexions]]) : $\Gamma^\lambda{}_{\mu\nu}=\tfrac12g^{\lambda\sigma}(\partial_\mu g_{\nu\sigma}+\partial_\nu g_{\mu\sigma}-\partial_\sigma g_{\mu\nu})$.
Riemann : $R^\rho{}_{\sigma\mu\nu}=\partial_\mu\Gamma^\rho_{\nu\sigma}-\partial_\nu\Gamma^\rho_{\mu\sigma}+\Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma}-\Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma}$ ; Ricci $R_{\sigma\nu}=R^\rho{}_{\sigma\rho\nu}$ ; scalaire $R=g^{\mu\nu}R_{\mu\nu}$ ; **Einstein** $G_{\mu\nu}=R_{\mu\nu}-\tfrac12Rg_{\mu\nu}$.
Symétries : $R_{\rho\sigma\mu\nu}=-R_{\sigma\rho\mu\nu}=-R_{\rho\sigma\nu\mu}=R_{\mu\nu\rho\sigma}$, $R_{\rho[\sigma\mu\nu]}=0$ ; nombre de composantes indépendantes en dimension $n$ : $\tfrac{n^2(n^2-1)}{12}$ (20 en $n=4$).
**Bianchi** : $\nabla_{[\lambda}R_{\mu\nu]\rho\sigma}=0$ ⇒ en contractant deux fois $\boxed{\nabla^\mu G_{\mu\nu}=0}$.
**Géodésique** : $\ddot x^\mu+\Gamma^\mu{}_{\alpha\beta}\dot x^\alpha\dot x^\beta=0$ ; équation de déviation $\tfrac{D^2\xi^\mu}{d\tau^2}=-R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$ : **la courbure = les forces de marée** ([[01_Varietes_differentielles]] §3 pour la mécanique).
**Vecteurs de Killing** : $\mathcal L_\xi g=0$ ; $p_\mu\xi^\mu$ conservé le long des géodésiques (Noether géométrique). Ex. : $\xi=\partial_t$ (énergie $E=-p_t$), $\eta=\partial_\varphi$ (moment cinétique $L=p_\varphi$).

## 3. Action d'Einstein–Hilbert

$$S[g,\Phi]=\frac1{16\pi G}\int(R-2\Lambda)\sqrt{-g}\,d^4x+S_m[g,\Phi].$$
**Variation.** $\delta\sqrt{-g}=-\tfrac12\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$ ; $\delta R=R_{\mu\nu}\delta g^{\mu\nu}+g_{\mu\nu}\Box\delta g^{\mu\nu}-\nabla_\mu\nabla_\nu\delta g^{\mu\nu}$ (le dernier terme est une divergence totale et s'annule avec $\sqrt{-g}$, intégrée, à bord nul ; terme de Gibbons–Hawking–York sinon). D'où
$$\delta S_{EH}=\frac1{16\pi G}\int\big(R_{\mu\nu}-\tfrac12Rg_{\mu\nu}+\Lambda g_{\mu\nu}\big)\delta g^{\mu\nu}\sqrt{-g}\,d^4x .$$
Tenseur énergie-impulsion : $T_{\mu\nu}\doteq-\dfrac2{\sqrt{-g}}\dfrac{\delta S_m}{\delta g^{\mu\nu}}$. Annuler $\delta S=0$ :
$$\boxed{G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G\,T_{\mu\nu}}\qquad(c=1).$$
- **Conservation** : $\nabla^\mu T_{\mu\nu}=0$ (Bianchi, ou invariance de $S_m$ par difféomorphisme = Noether II).
- **Forme à trace inversée** : trace de l'équation : $-R+4\Lambda=8\pi GT$ ; donc $R_{\mu\nu}=8\pi G(T_{\mu\nu}-\tfrac12Tg_{\mu\nu})+\Lambda g_{\mu\nu}$.
- **Vide** ($T_{\mu\nu}=0$) : $G_{\mu\nu}=-\Lambda g_{\mu\nu}$, $R=4\Lambda$, **$R_{\mu\nu}=\Lambda g_{\mu\nu}$** (espace d'Einstein). Cas $\Lambda=0$ : $R_{\mu\nu}=0$.
- **Hilbert–Palatini–Cartan** : $S=\tfrac1{4\kappa^2}\int\varepsilon_{abcd}e^a e^b R^{cd}$ ([[03_Jauge_EM_YM_Gravite]]).
- **Fluide parfait** : $T_{\mu\nu}=(\rho+p)u_\mu u_\nu+pg_{\mu\nu}$ ; Maxwell : $T_{\mu\nu}=F_{\mu\alpha}F_\nu{}^\alpha-\tfrac14g_{\mu\nu}F^2$ (sans trace).
- **Torseur de l'espace-temps** : la masse et le moment cinétique d'un espace-temps stationnaire sont les intégrales de Komar $M=-\tfrac1{8\pi}\oint\nabla^\mu\xi^\nu dS_{\mu\nu}$, $J=\tfrac1{16\pi}\oint\nabla^\mu\eta^\nu dS_{\mu\nu}$ : le couple $(P^0,J)$ du torseur de Poincaré ([[02_Torseurs_Varignon_generalise]], [[02_Relativite_restreinte_Poincare]]).

## 4. Limite newtonienne et champ faible

Métrique stationnaire faible : $g_{00}=-(1+2\Phi/c^2)$, $g_{ij}=(1-2\Phi/c^2)\delta_{ij}$. Géodésique lente : $\ddot x^i=-\partial_i\Phi$. L'équation $R_{00}\simeq\nabla^2\Phi$ et $T_{00}-\tfrac12Tg_{00}\simeq\tfrac12\rho$ donnent $\nabla^2\Phi=4\pi G\rho$ (Poisson).
**Linéarisation** $g=\eta+h$, jauge de Lorenz $\partial^\mu\bar h_{\mu\nu}=0$ ($\bar h=h-\tfrac12\eta h$) : $\Box\bar h_{\mu\nu}=-16\pi GT_{\mu\nu}$ ; dans le vide, **ondes** $\bar h_{\mu\nu}=\epsilon_{\mu\nu}e^{ik\cdot x}$, $k^2=0$ ; jauge TT : **deux polarisations** $+$ et $\times$ (hélicité $\pm2$ : graviton de spin 2, [[03_Jauge_EM_YM_Gravite]]). Puissance rayonnée (quadrupôle) $P=\tfrac G{5c^5}\langle\dddot Q_{ij}\dddot Q^{ij}\rangle$. GW150914 : ~$3M_\odot c^2$ rayonnés ([[03_Gravitation_quantique]]).

## 5. Tests classiques (à l'ordre post-newtonien)

Décalage vers le rouge $\Delta\nu/\nu=\Delta\Phi/c^2$ ; déviation de la lumière par le Soleil $4GM/(c^2b)=1{,}75''$ ; périhélie de Mercure $\Delta\varphi=6\pi GM/(c^2a(1-e^2))$ par orbite ([[06_Kepler_Runge_Lenz_SO_n+1]]) ; retard Shapiro ; précession de Lense–Thirring (rotation, lié à $g_{t\varphi}$, [[13_Kerr_trou_noir_en_rotation]]).

## 6. Formulation hamiltonienne (rappel)

$3+1$ : $ds^2=-N^2dt^2+h_{ij}(dx^i+N^idt)(dx^j+N^jdt)$, contraintes $\mathcal H\approx0$, $\mathcal H_i\approx0$ ([[03_Gravitation_quantique]]). **Théorème de Birkhoff** : toute solution du vide à symétrie sphérique est (localement) Schwarzschild, donc statique ([[11_Schwarzschild_trou_noir]]). **Théorème de singularité de Penrose–Hawking** : l'existence de surfaces piégées + condition d'énergie ⇒ géodésiques incomplètes ([[12_Coordonnees_EF_Kruskal_Penrose_extension_maximale]]).

## 7. Exercices

1. Vérifier $\nabla^\mu G_{\mu\nu}=0$ à partir de Bianchi.
2. Montrer que pour $T_{\mu\nu}=-\rho_\Lambda g_{\mu\nu}$ on retrouve $\Lambda=8\pi G\rho_\Lambda$ (énergie du vide).
3. Dériver $R=4\Lambda$ pour le vide avec constante cosmologique (trace de $G+\Lambda g=0$, $g^\mu{}_\mu=4$).
