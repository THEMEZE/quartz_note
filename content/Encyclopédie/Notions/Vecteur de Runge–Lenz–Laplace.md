---
title: "Vecteur de Runge–Lenz–Laplace"
type: notion
domaine: "Mécanique classique"
niveau: 3
niveau_label: "Master 1"
status: rédigé (à relire)
generated: true
prerequisites:
  - "[[Problème de Kepler]]"
related:
  - "[[Symétrie cachée SO(n+1)]]"
sources:
  - "[[Physique/Mécanique du Solide/V - Problème de Kepler, vecteur de Runge–Lenz–Laplace, symétrie $SO(n+1)$, version quantique, précession de Mercure, exercices corrigés|V - Problème de Kepler, vecteur de Runge–Lenz–Laplace, ]]"
paths:
  - "[[Parcours G]]"
tags:
  - encyclopedie
  - notion
---

# Vecteur de Runge–Lenz–Laplace

> [!abstract] Intégrale première supplémentaire de Kepler
> **Mécanique classique** · niveau 3 (Master 1) · statut : rédigé (à relire)

## Prérequis

- [[Problème de Kepler]] (n3)

## Contenu déjà rédigé

- [[Physique/Mécanique du Solide/V - Problème de Kepler, vecteur de Runge–Lenz–Laplace, symétrie $SO(n+1)$, version quantique, précession de Mercure, exercices corrigés|V - Problème de Kepler, vecteur de Runge–Lenz–Laplace, ]]

## 1. Définition et conservation

Pour $H=\dfrac{\vec p^{\,2}}{2m}-\dfrac kr$ ($k>0$, dimension 3), avec $\vec L=\vec r\times\vec p$ :
$$
\boxed{\vec A=\vec p\times\vec L-mk\,\hat r.}
$$

>[!tip]+ **Théorème.** $\vec A$ est une intégrale première du mouvement de Kepler. De plus $\vec A\cdot\vec L=0$ et $\ \vec A^{\,2}=m^2k^2+2mH\,\vec L^{\,2}$.
>
>*Démonstration.* $\dot{\vec L}=0$ et $\dot{\vec p}=-k\vec r/r^3$. Avec $\vec a\times(\vec b\times\vec c)=\vec b(\vec a\cdot\vec c)-\vec c(\vec a\cdot\vec b)$ :
>$$
>\dot{\vec p}\times\vec L=-\frac k{r^3}\,\vec r\times(\vec r\times\vec p)=\frac{k\vec p}{r}-\frac{k\,\vec r\,(\vec r\cdot\vec p)}{r^3},
>$$
>$$
>mk\,\frac{d\hat r}{dt}=mk\Big(\frac{\vec v}{r}-\frac{\vec r(\vec r\cdot\vec v)}{r^3}\Big)=\frac{k\vec p}{r}-\frac{k\,\vec r(\vec r\cdot\vec p)}{r^3}.
>$$
>Donc $\dot{\vec A}=0$. Orthogonalité : $\vec p\times\vec L\perp\vec L$ et $\hat r\perp\vec L$. Norme : calcul direct avec $\lvert\vec p\times\vec L\rvert^2=p^2L^2$. $\square$

## 2. Forme de l'orbite

$\vec A\cdot\vec r=Ar\cos\theta=\vec r\cdot(\vec p\times\vec L)-mkr=L^2-mkr$ (produit mixte), d'où
$$
r(\theta)=\frac{L^2/(mk)}{1+e\cos\theta},\qquad e=\frac{A}{mk}=\sqrt{1+\frac{2HL^2}{mk^2}}.
$$
$\vec A$ pointe vers le **périhélie**, sa norme fixe l'excentricité. Les coniques sont fermées *parce que* $\vec A$ est conservé : $\vec A$ interdit la précession (voir [[Précession de Mercure]], où une perturbation en $1/r^3$ brise cette conservation).

## 3. Pourquoi n'est-ce pas un Noether « ordinaire »

$\vec A$ est conservé mais ne correspond à aucune symétrie **de l'espace** : la transformation qu'il engendre, $\delta f=\sigma\{f,\vec n\cdot\vec A\}$, mêle $\vec r$ et $\vec p$. C'est une **symétrie cachée** ; voir [[Symétrie cachée SO(n+1)]].

## Pour continuer

- [[Symétrie cachée SO(n+1)]]

## Notions liées

- [[Symétrie cachée SO(n+1)]]

## Parcours

- [[Parcours G]] — Le fil de Noether
