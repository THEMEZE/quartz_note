---
title: "Principe de moindre action"
type: notion
domaine: "Mécanique classique"
niveau: 3
niveau_label: "Master 1"
status: rédigé (à relire)
generated: true
prerequisites:
  - "[[Trajectoires, chemins et champs]]"
  - "[[Analyse]]"
related:
  - "[[Géodésique]]"
sources:
  - "[[Physique/Mécanique du Solide/III - Mécanique du point au solide (nD)#6. Formalisme lagrangien|III - Mécanique du point au solide (nD)#6. Formalisme lagrangien]]"
paths:
  - "[[Parcours A]]"
  - "[[Parcours B]]"
  - "[[Parcours E]]"
  - "[[Parcours G]]"
tags:
  - encyclopedie
  - notion
---

# Principe de moindre action

> [!abstract] Action stationnaire, variations à extrémités fixées
> **Mécanique classique** · niveau 3 (Master 1) · statut : rédigé (à relire)

## Prérequis

- [[Trajectoires, chemins et champs]] (n1)
- [[Analyse]] (n1)

## Contenu déjà rédigé

- [[Physique/Mécanique du Solide/III - Mécanique du point au solide (nD)#6. Formalisme lagrangien|III - Mécanique du point au solide (nD)#6. Formalisme lagrangien]]

## 1. Cadre

Une **configuration** est un point $q=(q^1,\dots,q^\ell)$ d'une variété $Q$ ; une **trajectoire** est une courbe $q:[t_1,t_2]\to Q$ de classe $C^2$. Un **lagrangien** est une fonction $L(q,\dot q,t)$ de classe $C^2$ ; son **action** est la fonctionnelle
$$
S[q]=\int_{t_1}^{t_2}L\big(q(t),\dot q(t),t\big)\,dt .
$$

>[!tip]+ **Principe de Hamilton (moindre action).** Le mouvement réel $q$ est un **point stationnaire** de $S$ parmi les trajectoires de mêmes extrémités : pour toute variation $q_\varepsilon=q+\varepsilon\,\eta$ avec $\eta(t_1)=\eta(t_2)=0$,
>$$
>\frac{d}{d\varepsilon}\Big|_{\varepsilon=0}S[q_\varepsilon]=0 .
>$$

## 2. Équations d'Euler–Lagrange

>[!tip]+ **Théorème.** $q$ est stationnaire pour $S$ si et seulement si
>$$
>\boxed{\frac{d}{dt}\frac{\partial L}{\partial\dot q^\alpha}-\frac{\partial L}{\partial q^\alpha}=0,\qquad\alpha=1,\dots,\ell .}
>$$
>
>*Démonstration.* En dérivant sous l'intégrale et en intégrant par parties ($\delta\dot q=\dot\eta$) :
>$$
>\frac{dS}{d\varepsilon}\Big|_0=\underbrace{\Big[\frac{\partial L}{\partial\dot q^\alpha}\eta^\alpha\Big]_{t_1}^{t_2}}_{=0}+\int_{t_1}^{t_2}\Big(\frac{\partial L}{\partial q^\alpha}-\frac{d}{dt}\frac{\partial L}{\partial\dot q^\alpha}\Big)\eta^\alpha\,dt .
>$$
>Le crochet est nul car $\eta(t_{1,2})=0$. La fonction entre parenthèses, notée $E_\alpha$, est continue ; le **lemme fondamental** (si $\int E_\alpha\eta^\alpha=0$ pour tout $\eta\in C_c^\infty$, alors $E_\alpha\equiv0$ : sinon on prend $\eta=E_\alpha\chi$ avec $\chi\geq0$ une bosse supportée là où $E_\alpha\neq0$, et l'intégrale est $>0$) conclut. $\square$

## 3. Ce que le principe n'affirme pas

>[!warning]+ Stationnaire n'est pas minimal
>Pour l'oscillateur harmonique $L=\tfrac12m(\dot q^2-\omega^2q^2)$, la trajectoire réelle minimise $S$ si $t_2-t_1<\pi/\omega$ et devient un **col** au-delà. Le principe est **variationnel local**, pas un principe de minimum.

>[!note]+ Invariance de forme et de jauge
>- Les équations d'Euler–Lagrange sont **covariantes** : elles gardent la même forme pour tout changement de coordonnées $q\to Q(q,t)$ (la stationnarité de $S$ ne dépend pas des coordonnées).
>- $L\to L+\dfrac{d\phi}{dt}(q,t)$ change $S$ de $\phi|_{t_2}-\phi|_{t_1}$, terme de bord fixé : mêmes équations du mouvement.
>- Pour $L=T=\tfrac12m_{\alpha\beta}\dot q^\alpha\dot q^\beta$, les trajectoires sont les **géodésiques** de $m_{\alpha\beta}$ (voir [[Géodésique]]).

## 4. Fil de Noether

Une **symétrie** est une transformation qui laisse $S$ invariante (à un terme de bord près). Tout le [[Théorème de Noether]] est la lecture de cette phrase : le principe fournit les équations, la symétrie de $S$ fournit les lois de conservation.

## 5. Contrôles de cohérence

- $[S]=[L]\cdot[t]$ = énergie × temps (dimension d'un moment cinétique, celle de $\hbar$ : voir [[Intégrale de chemin]]).
- Si $L$ est multiplié par une constante, les équations ne changent pas.

## Pour continuer

- [[Mécanique lagrangienne]]
- [[Intégrale de chemin]]
- [[Géodésique]]

## Notions liées

- [[Géodésique]]

## Parcours

- [[Parcours A]] — Physique générale
- [[Parcours B]] — De la mécanique classique à la théorie des champs
- [[Parcours E]] — De la géométrie à la relativité générale
- [[Parcours G]] — Le fil de Noether
