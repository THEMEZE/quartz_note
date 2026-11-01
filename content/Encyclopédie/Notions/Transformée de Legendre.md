---
title: "Transformée de Legendre"
type: notion
domaine: "Mécanique classique"
niveau: 3
niveau_label: "Master 1"
status: rédigé (à relire)
generated: true
prerequisites:
  - "[[Analyse]]"
related:
  - "[[Mécanique hamiltonienne]]"
sources: []
paths:
  - "[[Parcours B]]"
  - "[[Parcours G]]"
tags:
  - encyclopedie
  - notion
---

# Transformée de Legendre

> [!abstract] Dualité convexe, passage (q,q̇)→(q,p)
> **Mécanique classique** · niveau 3 (Master 1) · statut : rédigé (à relire)

## Prérequis

- [[Analyse]] (n1)

## 1. Définition

Soit $f:\mathbb R^\ell\to\mathbb R$ de classe $C^2$ à hessienne **définie positive** (strictement convexe, avec croissance sur-linéaire). Sa **transformée de Legendre** est
$$
f^\ast(p)=\sup_{x}\big(p\cdot x-f(x)\big)=p\cdot x(p)-f\big(x(p)\big),\qquad p=\nabla f\big(x(p)\big).
$$

>[!tip]+ **Propriétés.**
>1. $\nabla f^\ast(p)=x(p)$ : le gradient de $f^\ast$ est l'inverse de celui de $f$.
>2. $\mathrm{Hess}\,f^\ast=(\mathrm{Hess}\,f)^{-1}$ est définie positive.
>3. **Involution** : $(f^\ast)^\ast=f$.
>4. **Inégalité de Young** : $p\cdot x\leq f(x)+f^\ast(p)$, égalité ssi $p=\nabla f(x)$.
>
>*Démonstration.* $x\mapsto p\cdot x-f(x)$ est strictement concave, son maximum est atteint en l'unique $x(p)$ tel que $\nabla f(x)=p$ (inversible car $\mathrm{Hess}\,f>0$). Alors $\nabla f^\ast=x(p)+p\,\partial_px-\nabla f\,\partial_px=x(p)$ (1). Dériver $x(p)$ donne $\mathrm{Hess}\,f^\ast=\partial x/\partial p=(\mathrm{Hess}\,f)^{-1}$ (2). (3) : appliquer (1) deux fois. (4) : définition du sup. $\square$

## 2. Avec paramètres

Si $f=f(x;\lambda)$, alors $\partial_\lambda f^\ast(p;\lambda)=-\partial_\lambda f\big(x(p);\lambda\big)$. Les variables « passives » changent de signe. C'est ce qui donne $\partial H/\partial t=-\partial L/\partial t$.

## 3. Usage en physique

- **Mécanique** : $L(q,\dot q,t)\to H(q,p,t)$ ; voir [[Mécanique hamiltonienne]]. La hessienne $\partial^2L/\partial\dot q\partial\dot q=m_{\alpha\beta}$ est inversible, la condition est remplie.
- **Thermodynamique** : $U(S,V)\to F(T,V)$, $H(S,p)$, $G(T,p)$ (potentiels thermodynamiques).
- **Lagrangiens singuliers** (hessienne dégénérée, théories de jauge) : la transformée n'existe plus, il faut les contraintes de Dirac.

## Pour continuer

- [[Mécanique hamiltonienne]]

## Notions liées

- [[Mécanique hamiltonienne]]

## Parcours

- [[Parcours B]] — De la mécanique classique à la théorie des champs
- [[Parcours G]] — Le fil de Noether
