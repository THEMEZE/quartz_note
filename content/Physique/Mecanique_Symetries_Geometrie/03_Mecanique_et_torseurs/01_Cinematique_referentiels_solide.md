---
title: Cinématique : référentiels, solide, torseur cinématique
tags:
  - Physique
  - Mathematiques
lang: fr
partie: II
---

> Retour : [[00_Index]] · notations : [[01_Conventions_notations]]

# Cinématique : référentiels, solide, torseur cinématique

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
