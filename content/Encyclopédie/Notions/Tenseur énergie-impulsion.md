---
title: "Tenseur énergie-impulsion"
type: notion
domaine: "Théories des champs"
niveau: 4
niveau_label: "Master 2"
status: rédigé (à relire)
generated: true
prerequisites:
  - "[[Théorème de Noether pour les champs]]"
related:
  - "[[Équations d'Einstein]]"
sources: []
paths:
  - "[[Parcours B]]"
  - "[[Parcours G]]"
tags:
  - encyclopedie
  - notion
---

# Tenseur énergie-impulsion

> [!abstract] Courant de Noether des translations
> **Théories des champs** · niveau 4 (Master 2) · statut : rédigé (à relire)

## Prérequis

- [[Théorème de Noether pour les champs]] (n4)

## 1. Tenseur canonique

Des translations d'espace-temps ([[Théorème de Noether pour les champs]]) :
$$
T^\mu{}_\nu=\frac{\partial\mathscr L}{\partial(\partial_\mu\phi_A)}\partial_\nu\phi_A-\delta^\mu_\nu\mathscr L,\qquad\partial_\mu T^\mu{}_\nu=0 .
$$
$\nu=0$ : énergie ($T^0{}_0=\pi\dot\phi-\mathscr L=\mathscr H$) ; $\nu=i$ : impulsion. Les charges sont $P_\nu=\int T^0{}_\nu\,d^nx$.

>[!warning]+ Défauts du tenseur canonique
>$T^{\mu\nu}$ n'est en général **ni symétrique ni invariant de jauge** (pour le champ électromagnétique). On l'améliore en ajoutant $\partial_\lambda B^{\lambda\mu\nu}$ avec $B$ antisymétrique en ses deux premiers indices : c'est le tenseur de **Belinfante**, qui laisse $P_\nu$ inchangé.

## 2. Tenseur métrique (Hilbert)

Dans un espace-temps de métrique $g$ (signature $-+++$), on définit
$$
\boxed{T_{\mu\nu}=-\frac{2}{\sqrt{|g|}}\frac{\delta S_{\rm m}}{\delta g^{\mu\nu}}} ,
$$
automatiquement symétrique et invariant de jauge. Pour un champ scalaire, $T_{\mu\nu}=\partial_\mu\phi\,\partial_\nu\phi+g_{\mu\nu}\mathscr L$ avec $\mathscr L=-\tfrac12(\partial\phi)^2-V$.

## 3. Conservation et gravité

L'invariance de $S_{\rm m}$ par difféomorphismes (symétrie **locale**, [[Deuxième théorème de Noether]]) entraîne $\nabla_\mu T^{\mu\nu}=0$ sur les solutions matière. C'est la source des [[Équations d'Einstein]] $G_{\mu\nu}=8\pi G\,T_{\mu\nu}$ (et l'identité de Bianchi contractée $\nabla^\mu G_{\mu\nu}=0$ assure la cohérence).

## 4. Fil de Noether

Le tenseur énergie-impulsion est **le courant de Noether de l'espace-temps** : la conservation de l'énergie et de l'impulsion exprime l'homogénéité de l'espace-temps, et sa version locale fait de lui la source de la courbure.

## Pour continuer

- (fin de branche)

## Notions liées

- [[Équations d'Einstein]]

## Parcours

- [[Parcours B]] — De la mécanique classique à la théorie des champs
- [[Parcours G]] — Le fil de Noether
