---
title: "Théorème de Liouville"
type: notion
domaine: "Mécanique classique"
niveau: 3
niveau_label: "Master 1"
status: rédigé (à relire)
generated: true
prerequisites:
  - "[[Mécanique hamiltonienne]]"
related:
  - "[[Ensembles statistiques]]"
sources:
  - "[[Physique/Mécanique du Solide/III - Mécanique du point au solide (nD)#7. Formalisme hamiltonien et théorème de Liouville|III - Mécanique du point au solide (nD)#7. Formalisme hamiltonien et t]]"
paths:
  - "[[Parcours B]]"
tags:
  - encyclopedie
  - notion
---

# Théorème de Liouville

> [!abstract] Conservation du volume de phase
> **Mécanique classique** · niveau 3 (Master 1) · statut : rédigé (à relire)

## Prérequis

- [[Mécanique hamiltonienne]] (n3)

## Contenu déjà rédigé

- [[Physique/Mécanique du Solide/III - Mécanique du point au solide (nD)#7. Formalisme hamiltonien et théorème de Liouville|III - Mécanique du point au solide (nD)#7. Formalisme hamiltonien et t]]

>[!tip]+ **Théorème de Liouville.** Le flot hamiltonien $\Phi_t:\Gamma\to\Gamma$ **conserve le volume** de l'espace des phases : $\mathrm{Vol}(\Phi_t(D))=\mathrm{Vol}(D)$ pour tout domaine $D$. Il est même **symplectique** : $\Phi_t^\ast\omega=\omega$.
>
>*Démonstration (divergence).* $X_H=(\partial_pH,-\partial_qH)$ vérifie $\operatorname{div}X_H=\partial_{q^\alpha}\partial_{p_\alpha}H-\partial_{p_\alpha}\partial_{q^\alpha}H=0$ (Schwarz). Pour $\mathcal J(t)=\det\big(\partial\Phi_t(z_0)/\partial z_0\big)$, $\dot{\mathcal J}=(\operatorname{div}X_H)\circ\Phi_t\,\mathcal J=0$ et $\mathcal J(0)=1$, donc $\mathcal J\equiv1$.
>
>*Démonstration (symplectique).* $M_t=\partial\Phi_t/\partial z_0$ vérifie $\dot M=J\,S\,M$ avec $S=\mathrm{Hess}\,H$ symétrique. Avec $J^T=-J$ et $J^2=-\mathbb 1$ :
>$$
>\frac d{dt}(M^TJM)=M^TS\,J^TJ\,M+M^TJ\,J\,S\,M=M^TSM-M^TSM=0,
>$$
>donc $M_t^TJM_t=J$, d'où $\det M_t=\pm1$, et $+1$ par continuité. $\square$

## Équation de Liouville

Pour une densité $\rho(z,t)$ transportée par le flot :
$$
\partial_t\rho+\operatorname{div}(\rho X_H)=0\iff\boxed{\partial_t\rho+\{\rho,H\}=0}\iff\frac{d\rho}{dt}\Big|_{\text{flot}}=0 :
$$
le « fluide » des points de phase est **incompressible**.

## Conséquences

- **Équilibre** : $\rho=\rho(H)$ est stationnaire (fondement des [[Ensembles statistiques]]).
- **Récurrence de Poincaré** : un flot conservant un volume fini revient arbitrairement près de tout état initial.
- **Invariance par transformation ponctuelle** : $Q=Q(q)$, $P_\alpha=\frac{\partial q^\beta}{\partial Q^\alpha}p_\beta$ a une jacobienne triangulaire par blocs de déterminant 1 : la mesure $d^\ell q\,d^\ell p$ est intrinsèque.

## Pour continuer

- [[Ensembles statistiques]]

## Notions liées

- [[Ensembles statistiques]]

## Parcours

- [[Parcours B]] — De la mécanique classique à la théorie des champs
