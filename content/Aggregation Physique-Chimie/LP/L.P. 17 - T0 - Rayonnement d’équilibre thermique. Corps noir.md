---
title: L.P. 17 - T0 - Rayonnement d’équilibre thermique. Corps noir
tags:
  - Agrégation
  - Physique
  - Oral
---
# Rayonnement d’équilibre thermique — Corps noir (niveau L2)

## Problématique
Comment décrire l’échange d’énergie par rayonnement entre un système matériel et le champ électromagnétique, et quelles lois universelles émergent à l’équilibre thermique ?

---

# I — Transfert d’énergie par rayonnement

## 1. Grandeurs radiatives

On introduit les grandeurs suivantes :

- **Flux énergétique total** :  
  \[
  \Phi = \frac{dE}{dt}
  \]

- **Flux surfacique** :
  \[
  \phi = \frac{1}{S}\frac{dE}{dt}
  \]

- **Flux spectral** :
  \[
  \phi_\nu,\quad \phi_\lambda
  \]

Relation de changement de variable :
\[
\phi_\lambda = \phi_\nu \left|\frac{d\nu}{d\lambda}\right|
\]

- **Densité volumique d’énergie du rayonnement** :
\[
u(\nu,T),\quad u(\lambda,T)
\]

---

## 2. Interaction matière–rayonnement

On distingue :

- absorption
- émission
- réflexion
- transmission

Cas limites :

| Objet | Condition |
|------|----------|
| Transparent | émission ≈ absorption ≈ 0 |
| Réfléchissant | absorption ≈ 0 |
| Opaque | transmission = 0 |
| Corps noir | absorption totale |

Le comportement réel dépend fortement de la longueur d’onde → nécessité du spectre.

---

# II — Rayonnement d’équilibre thermique

## 1. Hypothèse d’équilibre

Une enceinte à température \(T\) peut être vue comme :

- un gaz de photons
- un champ EM stationnaire en interaction avec les parois

À l’équilibre :
- émission = absorption statistiquement
- champ stationnaire

---

## 2. Densité spectrale d’énergie (résultat de Planck)

\[
u_\nu(\nu,T)=\frac{8\pi h\nu^3}{c^3}\frac{1}{e^{h\nu/k_BT}-1}
\]

\[
u_\lambda(\lambda,T)=\frac{8\pi hc}{\lambda^5}\frac{1}{e^{hc/(\lambda k_BT)}-1}
\]

---

## 3. Limites classiques

### Rayleigh–Jeans (basse fréquence)
\[
u_\nu \sim \frac{8\pi \nu^2 k_B T}{c^3}
\]

→ divergence ultraviolette (catastrophe)

### Loi de Wien (haute fréquence)
\[
u_\lambda \sim \lambda^{-5} e^{-hc/(\lambda k_BT)}
\]

---

## 4. Loi de déplacement de Wien

Maximum spectral :
\[
\lambda_{\max} T = b
\]

→ application :
- température des étoiles
- spectre solaire

---

# III — Flux et loi de Stefan-Boltzmann

## 1. Flux émis par un corps noir

Relation clé (isotropie du rayonnement) :

\[
d\phi = \frac{c}{4} u(T)
\]

---

## 2. Loi de Stefan-Boltzmann

En intégrant sur toutes les fréquences :

\[
\phi = \sigma T^4
\]

avec :
\[
\sigma = \frac{2\pi^5 k_B^4}{15 h^3 c^2}
\]

---

## 3. Interprétation thermodynamique

On peut retrouver :
- \(u \propto T^4\)
- \(S \propto T^3\)

Relation d’état du gaz de photons :
\[
P = \frac{u}{3}
\]

---

# IV — Corps noir réel et applications

## 1. Définition

Un corps noir est un système :
- absorbant totalement le rayonnement incident
- en équilibre radiatif

Réalisations :
- cavité à petit trou
- enceinte thermique

---

## 2. Corps non parfaits

On introduit l’émissivité :
\[
\phi = \varepsilon \sigma T^4
\quad \text{avec } 0 < \varepsilon < 1
\]

---

## 3. Exemple : lampe à incandescence

- filament chauffé par effet Joule
- équilibre entre :
  - puissance électrique reçue
  - pertes radiatives

---

## 4. Effet de serre (modèle simplifié)

- atmosphère transparente au visible
- absorbante dans l’infrarouge

→ déséquilibre radiatif → augmentation de \(T\)

---

# V — Vision unifiée (point agrégation)

## 1. Nature du rayonnement thermique

Le rayonnement thermique est :
- un gaz de photons bosoniques
- décrit par une statistique quantique

---

## 2. Origine de la loi de Planck

Deux ingrédients :
- quantification des modes EM
- occupation Bose-Einstein sans potentiel chimique

---

## 3. Structure profonde

On retrouve une structure universelle :

- **statistique → distribution exponentielle**
- **équilibre → maximisation entropie**
- **loi macroscopique → intégration spectrale**

---

## Conclusion

Le rayonnement thermique relie :

- thermodynamique
- électromagnétisme
- physique statistique

et constitue un exemple paradigmatique de loi universelle émergente à partir de la quantification du champ.