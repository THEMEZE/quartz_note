---
title: "Mécanique lagrangienne"
type: chapitre
domaine: "Mécanique classique"
niveau: 3
niveau_label: "Master 1"
status: rédigé (à relire)
generated: true
prerequisites:
  - "[[Principe de moindre action]]"
  - "[[Mécanique du point]]"
  - "[[Métrique]]"
related:
  - "[[Mécanique hamiltonienne]]"
sources:
  - "[[Physique/Mécanique du Solide/III - Mécanique du point au solide (nD)#6. Formalisme lagrangien|III - Mécanique du point au solide (nD)#6. Formalisme lagrangien]]"
paths:
  - "[[Parcours A]]"
  - "[[Parcours B]]"
  - "[[Parcours G]]"
  - "[[Parcours H]]"
tags:
  - encyclopedie
  - chapitre
---

# Mécanique lagrangienne

> [!abstract] Euler–Lagrange, métrique cinétique, jauge
> **Mécanique classique** · niveau 3 (Master 1) · statut : rédigé (à relire)

## Prérequis

- [[Principe de moindre action]] (n3)
- [[Mécanique du point]] (n1)
- [[Métrique]] (n2)

## Contenu déjà rédigé

- [[Physique/Mécanique du Solide/III - Mécanique du point au solide (nD)#6. Formalisme lagrangien|III - Mécanique du point au solide (nD)#6. Formalisme lagrangien]]

## 1. Espace des configurations et métrique cinétique

Un système de $N$ points avec $\ell$ degrés de liberté (liaisons holonomes) vit sur $Q$ de coordonnées $q^\alpha$ : $\vec r_a=\vec r_a(q,t)$. Pour des liaisons indépendantes du temps,
$$
T=\tfrac12\,m_{\alpha\beta}(q)\,\dot q^\alpha\dot q^\beta,\qquad m_{\alpha\beta}=\sum_a m_a\,g_{ij}\,\frac{\partial r_a^i}{\partial q^\alpha}\frac{\partial r_a^j}{\partial q^\beta},
$$
où $m_{\alpha\beta}$ est la **métrique cinétique** (riemannienne) de $Q$. $q^\alpha$ et $\dot q^\alpha$ sont traitées comme indépendantes.

## 2. Équations et moments

Avec $L=T-V$, le [[Principe de moindre action]] donne les équations d'Euler–Lagrange. Le **moment conjugué** $p_\alpha=\partial L/\partial\dot q^\alpha=m_{\alpha\beta}\dot q^\beta$ est **covariant**.

>[!tip]+ **Équivalence avec le PFD.** Les équations d'Euler–Lagrange s'écrivent
>$$
>m_{\alpha\beta}\big(\ddot q^\beta+\Gamma^\beta{}_{\gamma\delta}\dot q^\gamma\dot q^\delta\big)=-\partial_\alpha V ,
>$$
>où $\Gamma$ sont les symboles de Christoffel de $m_{\alpha\beta}$ : c'est le **PFD sur $Q$**. Sans force, ce sont les géodésiques de $m_{\alpha\beta}$ (première loi de Newton).
>
>*Démonstration.* $\frac{d}{dt}(m_{\alpha\beta}\dot q^\beta)=m_{\alpha\beta}\ddot q^\beta+\partial_\gamma m_{\alpha\beta}\dot q^\gamma\dot q^\beta$ et $\partial L/\partial q^\alpha=\tfrac12\partial_\alpha m_{\beta\gamma}\dot q^\beta\dot q^\gamma-\partial_\alpha V$. On symétrise $\partial_\gamma m_{\alpha\beta}\dot q^\gamma\dot q^\beta=\tfrac12(\partial_\gamma m_{\alpha\beta}+\partial_\beta m_{\alpha\gamma})\dot q^\beta\dot q^\gamma$ et on reconnaît $m_{\alpha\delta}\Gamma^\delta{}_{\beta\gamma}$. $\square$

**Forces non conservatives** : $\frac{d}{dt}\partial_{\dot q^\alpha}L-\partial_{q^\alpha}L=Q^{\rm nc}_\alpha$, avec $Q^{\rm nc}_\alpha=\vec F^{\rm nc}\cdot\partial\vec r/\partial q^\alpha$ (d'Alembert).

## 3. Énergie de Jacobi

>[!tip]+ **Théorème de l'énergie.** Soit $h:=p_\alpha\dot q^\alpha-L$. Sur les solutions, $\ \dfrac{dh}{dt}=-\dfrac{\partial L}{\partial t}$. Pour $L=T-V$ à liaisons fixes, $h=T+V$.
>
>*Démonstration.* $\dot h=\dot p_\alpha\dot q^\alpha+p_\alpha\ddot q^\alpha-\frac{\partial L}{\partial q^\alpha}\dot q^\alpha-\frac{\partial L}{\partial\dot q^\alpha}\ddot q^\alpha-\frac{\partial L}{\partial t}$, et $\dot p_\alpha=\partial L/\partial q^\alpha$ (EL). $\square$

## 4. Exemples

>[!example]- Pendule simple
>$L=\tfrac12m\ell^2\dot\theta^2+mg\ell\cos\theta$, $p_\theta=m\ell^2\dot\theta$, et EL donne $\ddot\theta=-\dfrac g\ell\sin\theta$.

>[!example]- Particule chargée
>$L=\tfrac12m\,g_{ij}v^iv^j-q\varphi+qA_iv^i$ donne $p_i=mv_i+qA_i$ et $m\,a_i=q(E_i+F_{ij}v^j)$ avec $F=dA$ : le champ magnétique est une 2-forme ([[Forme différentielle]]).

## 5. Fil de Noether

Une coordonnée **cyclique** ($\partial L/\partial q^\alpha=0$) donne $\dot p_\alpha=0$ : c'est le cas le plus simple du [[Théorème de Noether]] (invariance par translation de $q^\alpha$). Si $\partial_tL=0$, $h$ est conservée (invariance par translation du temps).

## 6. Contrôles

- $m_{\alpha\beta}$ définie positive ⇒ $T>0$ ; sinon le système est dégénéré.
- Cartésien : $m_{ij}=m\,g_{ij}$, on retrouve $m\ddot x_i=-\partial_iV$.

## Pour continuer

- [[Mécanique hamiltonienne]]
- [[Théorème de Noether]]
- [[Théorie lagrangienne des champs]]

## Notions liées

- [[Mécanique hamiltonienne]]

## Parcours

- [[Parcours A]] — Physique générale
- [[Parcours B]] — De la mécanique classique à la théorie des champs
- [[Parcours G]] — Le fil de Noether
- [[Parcours H]] — Déjà rédigé : Mécanique du Solide I → VIII
