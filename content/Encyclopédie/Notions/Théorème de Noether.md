---
title: "Théorème de Noether"
type: notion
domaine: "Mécanique classique"
niveau: 3
niveau_label: "Master 1"
status: rédigé (à relire)
generated: true
prerequisites:
  - "[[Mécanique lagrangienne]]"
related:
  - "[[Groupe de Lie]]"
  - "[[Lois de conservation en dynamique]]"
sources:
  - "[[Physique/Mécanique du Solide/III - Mécanique du point au solide (nD)#8. Théorème de Noether en mécanique|III - Mécanique du point au solide (nD)#8. Théorème de Noether en méca]]"
paths:
  - "[[Parcours B]]"
  - "[[Parcours G]]"
  - "[[Parcours H]]"
tags:
  - encyclopedie
  - notion
---

# Théorème de Noether

> [!abstract] Symétrie continue ⇒ grandeur conservée
> **Mécanique classique** · niveau 3 (Master 1) · statut : rédigé (à relire)

## Prérequis

- [[Mécanique lagrangienne]] (n3)

## Contenu déjà rédigé

- [[Physique/Mécanique du Solide/III - Mécanique du point au solide (nD)#8. Théorème de Noether en mécanique|III - Mécanique du point au solide (nD)#8. Théorème de Noether en méca]]

## 1. Énoncé

Soit $L(q,\dot q,t)$ et une famille de transformations $q^\alpha\to q^\alpha+\sigma\,\zeta^\alpha(q,t)$ (à $t$ fixé), de générateur $\zeta$, avec $\delta\dot q^\alpha=\frac{d}{dt}\zeta^\alpha$. C'est une **symétrie** (à une divergence près) si
$$
\delta L=\frac{\partial L}{\partial q^\alpha}\zeta^\alpha+\frac{\partial L}{\partial\dot q^\alpha}\dot\zeta^\alpha=\frac{dK}{dt}
$$
pour une fonction $K(q,t)$ (**quasi-symétrie** si $K\neq0$).

>[!tip]+ **Théorème de Noether.** Si $\zeta$ est une symétrie de $L$ de « jauge » $K$, la quantité
>$$
>\boxed{\mathscr Q=p_\alpha\,\zeta^\alpha-K}
>$$
>est **conservée** sur les solutions des équations d'Euler–Lagrange.
>
>*Démonstration.* Sur les solutions, $\partial L/\partial q^\alpha=\dot p_\alpha$. Donc
>$$
>\frac{d}{dt}\big(p_\alpha\zeta^\alpha\big)=\dot p_\alpha\zeta^\alpha+p_\alpha\dot\zeta^\alpha=\frac{\partial L}{\partial q^\alpha}\zeta^\alpha+\frac{\partial L}{\partial\dot q^\alpha}\dot\zeta^\alpha=\delta L=\frac{dK}{dt}.\qquad\square
>$$

>[!note]+ **Translation du temps.** Si $\partial_tL=0$, la quantité conservée est $h=p_\alpha\dot q^\alpha-L$ (voir [[Mécanique lagrangienne]]). On l'obtient en prenant $t\to t+\sigma$, ou directement par $\dot h=-\partial_tL$.

## 2. Tableau des symétries

| Symétrie du lagrangien | Générateur $\zeta$ | Grandeur conservée (ou loi de bilan si non invariant) |
| --- | --- | --- |
| Translation d'espace | $\zeta^i=n^i$ | $g(\vec n,\vec P)$ ; sinon TRD |
| Rotation $SO(n,g)$ | $\zeta^i=\Omega^i{}_jx^j$ | $\mathsf L^{ij}$ ; sinon TMC |
| Translation de temps | $t\to t+\sigma$ | $H=\mathcal E_m$ ; sinon TEM, TEC |
| Boost galiléen | $\zeta^i=tn^i$ | $m\overrightarrow{OG}-t\vec P$ (1re loi) |
| Jauge globale $U(1)$ (champ complexe) | $\delta\psi=i\sigma\psi$ | $\int\lvert\psi\rvert^2$ |
| Dilatation (potentiel $\propto r^{-2}$) | $\zeta=x,\ t\to\lambda^2t$ | $D=\vec x\cdot\vec p-2tH$ |
| Kepler ($-k/r$) | non ponctuelle | $\vec A$ (RLL) |

>[!example]- Boost galiléen (quasi-symétrie)
>$L=\tfrac12m\dot x^2$, $\zeta=t\,n$ : $\delta L=m\dot x\cdot n=\frac d{dt}(m\,x\cdot n)$, donc $K=m\,x\cdot n$ et $\mathscr Q=t\,n\cdot P-m\,x\cdot n=-n\cdot(m\vec x-t\vec P)$ : le centre d'inertie est en mouvement rectiligne uniforme.

>[!example]- Rotation, central
>$L=\tfrac12m\dot{\vec r}^2-V(|\vec r|)$ est invariant par $\delta\vec r=\sigma\,\vec\Omega\times\vec r$, et $\mathscr Q=\vec p\cdot(\vec\Omega\times\vec r)=\vec\Omega\cdot(\vec r\times\vec p)$ : conservation de $\vec L$ (2e loi de Kepler).

## 3. Version hamiltonienne et réciproque

$\mathscr Q$ engendre le flot $\delta f=\sigma\{f,\mathscr Q\}$ ; $\{\mathscr Q,H\}=0$ s'écrit aussi « $H$ est invariant par ce flot ». En formulation hamiltonienne, **symétries et intégrales premières se correspondent exactement** (voir [[Crochet de Poisson]]). Le théorème de Noether lagrangien en est la version avec $L$.

>[!warning]+ Limites
>- Seules les symétries **continues** donnent des charges (pas les symétries discrètes : parité, etc.).
>- Une symétrie de l'**action** n'est pas toujours une symétrie ponctuelle de $q$ : $\vec A$ de Kepler agit sur l'espace des phases, voir [[Symétrie cachée SO(n+1)]].
>- Pour une symétrie locale (dépendant de fonctions), voir [[Deuxième théorème de Noether]].

## 4. Généralisation

Aux champs : [[Théorème de Noether pour les champs]] (courant $\partial_\mu J^\mu=0$, [[Tenseur énergie-impulsion]]).

## Pour continuer

- [[Symétrie cachée SO(n+1)]]
- [[Théorème de Noether pour les champs]]

## Notions liées

- [[Groupe de Lie]]
- [[Lois de conservation en dynamique]]

## Parcours

- [[Parcours B]] — De la mécanique classique à la théorie des champs
- [[Parcours G]] — Le fil de Noether
- [[Parcours H]] — Déjà rédigé : Mécanique du Solide I → VIII
