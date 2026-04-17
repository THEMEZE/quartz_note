---
title: "L.P. 19 - T0 - Bilans thermiques : flux conductifs, convectifs et radiatifs"
tags:
  - Agrégation
  - Physique
  - Oral
---
# Bilans thermiques : flux conductifs, convectifs et radiatifs  
## Niveau CPGE

---

## Problématique
Comment décrire l’évolution thermique d’un système réel en tenant compte simultanément des trois modes de transfert :
- conduction
- convection
- rayonnement

et comment les unifier dans un cadre de bilan énergétique local ?

---

# I — Équation locale de bilan thermique

## 1. Hypothèse d’équilibre thermodynamique local

On suppose qu’à chaque point de l’espace :

- la matière peut être découpée en cellules mésoscopiques
- chaque cellule est à l’équilibre thermodynamique
- on peut définir :
\[
T(\mathbf{r},t), \quad P(\mathbf{r},t)
\]

Conditions de validité :
- échelle spatiale mésoscopique
- temps de relaxation microscopique ≪ temps macroscopique

---

## 2. Bilan d’énergie local

On considère un milieu continu, incompressible, de capacité thermique massique \(c\) et masse volumique \(\rho\).

Premier principe sur un élément de volume \(dV\) :

\[
dU = \delta Q + \delta W + p_v dV dt
\]

avec \(p_v\) puissance volumique interne (source).

---

### Définition du flux thermique

- flux énergétique traversant une surface :
\[
\Phi = \frac{dQ}{dt}
\]

- flux surfacique :
\[
\phi = \frac{\Phi}{S}
\]

- vecteur densité de courant thermique :
\[
\phi = \vec{j}_Q \cdot \vec{n}
\]

---

### Bilan local

\[
\rho c \frac{\partial T}{\partial t} + \nabla \cdot \vec{j}_Q = p_v
\]

---

## 3. Cas du régime permanent

Sans production interne :

\[
\nabla \cdot \vec{j}_Q = 0
\]

➡️ flux conservatif

---

# II — Lois constitutives des transferts thermiques

Le bilan seul ne suffit pas : il faut fermer le système.

---

## 1. Conduction thermique

### Loi de Fourier

\[
\vec{j}_Q = -\lambda \nabla T
\]

- \(\lambda > 0\) : conductivité thermique
- signe “−” : flux du chaud vers le froid
- processus irréversible

---

### Régime stationnaire 1D

Mur plan :

\[
\Phi = \frac{\lambda S}{L}(T_1 - T_2)
\]

Résistance thermique :

\[
R_{th} = \frac{L}{\lambda S}
\]

Analogies électriques :
- température ↔ tension
- flux ↔ courant

---

## 2. Convection thermique

### Description physique

Transport d’énergie par mouvement de matière.

Modification du bilan local :
\[
\frac{\partial T}{\partial t} \to \frac{\partial T}{\partial t} + (\vec{v}\cdot \nabla)T
\]

---

### Loi de Newton (interface solide–fluide)

\[
\phi = h(T_s - T_f)
\]

- \(h\) : coefficient de transfert convectif
- dépend de la géométrie et de l’écoulement

Résistance associée :
\[
R_{conv} = \frac{1}{hS}
\]

---

## 3. Rayonnement thermique

### Loi de Stefan-Boltzmann

\[
\phi_{émis} = \sigma T^4
\]

avec :
\[
\sigma = 5.67 \times 10^{-8} \, \mathrm{W\,m^{-2}\,K^{-4}}
\]

---

### Échange radiatif

Entre un corps et son environnement à \(T_0\) :

\[
\phi_{rad} = \sigma (T^4 - T_0^4)
\]

Linéarisation proche de l’équilibre :

\[
\phi_{rad} \simeq 4\sigma T_0^3 (T - T_0)
\]

---

### Résistance radiative équivalente

\[
h_{rad} = 4\sigma T_0^3
\quad \Rightarrow \quad
R_{rad} = \frac{1}{h_{rad}S}
\]

---

# III — Unification : réseau de résistances thermiques

## Idée centrale

Tous les transferts thermiques en régime stationnaire peuvent être modélisés par :

> un réseau de résistances thermiques en série et parallèle

---

### Correspondances

| Phénomène | Loi | Résistance |
|-----------|-----|-----------|
| conduction | Fourier | \(L/\lambda S\) |
| convection | Newton | \(1/hS\) |
| rayonnement | Stefan linéarisé | \(1/4\sigma T^3 S\) |

---

## Méthode générale

1. Identifier les interfaces
2. Identifier les modes de transfert
3. Associer une résistance
4. Résoudre un circuit thermique équivalent

---

# IV — Application : cellule solaire thermique

## 1. Modélisation

Système multicouche :
- verre
- absorbeur
- fluide caloporteur
- échanges avec l’air

Hypothèses :
- régime stationnaire
- températures proches de \(T_0\)
- linéarisation du rayonnement

---

## 2. Schéma équivalent

Le système devient un réseau :

- résistances conductives (couches solides)
- résistances convectives (fluide / air)
- résistance radiative (atmosphère)

---

## 3. Rendement

\[
\eta = \frac{\phi_{utile}}{\phi_{incident}}
\]

---

## 4. Résultat physique

- rendement élevé si :
  - faible résistance thermique globale
  - convection forcée efficace
  - pertes radiatives minimisées

---

# Conclusion

Les transferts thermiques peuvent être unifiés dans un cadre simple :

> un bilan local + une loi constitutive → une analogie électrique globale

---

## Idée clé

La physique des transferts thermiques est une **théorie de transport hors équilibre gouvernée par des lois locales linéaires**, qui se résume en régime stationnaire à une **structure de réseau de résistances**.