---
title: L.P. 08 - F1 - Notion de viscosité d'un fuide. Écoulements visqueux
tags:
  - Agrégation
  - Physique
  - Oral
---
---
### Liens

[^1]: Physique Spé. MP*, MP et PT*, PT, Gié, Sarmant, Olivier, More, Tec & Doc, 2000. 
[^2]: <a href="https://drive.google.com/file/d/1TxXiIyUpuNKw5627Li3pU42FJj_YZc58/view?usp=sharing#page=100&zoom=125" target="_blank" rel="noopener noreferrer">Hydrodynamique physique, Guyon-Hulin-Petit (2001) page ???</a>.

>- 👉 <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/Aggregation%20Physique-Chimie/Oraux/2025%20Guillaume%20Themeze/LP/L.P.08-F1-Notionde_viscosite_Ecoulement_visqueux_split.pdf#page=1&zoom=125" target="_blank" rel="noopener noreferrer">Manuscrit page 1</a>
>- <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/index.html?pdf=Aggregation%20Physique-Chimie/Oraux/" target="_blank" rel="noopener noreferrer">Lectures notes</a>

>-  <a href="https://drive.google.com/drive/folders/1i2FSRuEZTBRqYO-y2Ji_k-yNDNXvW4se?usp=drive_link/" target="_blank" rel="noopener noreferrer">Aggrégatifs</a>
>- <a href="https://drive.google.com/drive/folders/1EC5KW0wH97j7zVyYvGNlaMYUPvEYJwLB?usp=drive_link" target="_blank" rel="noopener noreferrer">Archives</a>

>- <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/Aggregation%20Physique-Chimie/Oraux/2018%20Benjamin%20Marchetti/lecon_physique_marchetti.pdf#page=33&zoom=125" target="_blank" rel="noopener noreferrer">Manuscrit BM</a> <-  <a href="https://marchettibenjamin.wordpress.com/agregation/plans-de-lecons/" target="_blank" >site perso</a>
>- <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/Aggregation%20Physique-Chimie/Oraux/2019%20Jules%20Fillette/LeconsPhysique.pdf#page=35&zoom=125" target="_blank" rel="noopener noreferrer">Manuscrit JF</a>
>- <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/Aggregation%20Physique-Chimie/Oraux/2019%20Julien%20Froustey/Plans_JF_2019.pdf#page=29&zoom=125" target="_blank" rel="noopener noreferrer">Manuscrit JFr</a>
>- <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/Aggregation%20Physique-Chimie/Oraux/2019%20Hugo%20Roussille/plans_lecon_physique.pdf#page=36&zoom=125" target="_blank" rel="noopener noreferrer"> Manuscrit HR</a>
>- <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/Aggregation%20Physique-Chimie/Archives/Physique-agreg.pdf#page=135&zoom=125" target="_blank" rel="noopener noreferrer"> Manuscrit PHS</a>
>- <a href="https://github.com/AnassNajlaoui/Lecons-Anass-Najlaoui-Agregation-Physique-2026/blob/main/F1.%20Notion%20de%20viscosit%C3%A9%20d'un%20fluide.%20%C3%89coulements%20visqueux./Scan_20260416_114156.pdf" target="_blank" rel="noopener noreferrer"> Manuscrit AN</a>

---


### Notion de viscosité d’un fluide. Écoulements visqueux (Cours 40 min – Agrégation)

---

## 🎯 Fil directeur

> **Transport diffusif de quantité de mouvement → équation de Navier–Stokes → compétition convection/diffusion (Re) → régimes d’écoulement**

---

# Plan (annoncé à l’oral)

I. Origine et modélisation de la viscosité  
II. Diffusion de quantité de mouvement  
III. Équation de Navier–Stokes  
IV. Nombre de Reynolds  
V. Écoulements modèles (Couette, Stokes, traînée)

---

# I – Notions sur  viscosité la viscosité
[^1] page 417
[^2] page 174 
## 1) Mise en évidence

- Plaque mobile entraînant un fluide
    
- Gradient de vitesse transverse
    

👉 existence de contraintes tangentielles

---

## 2) Loi de Newton (fluide newtonien)

Écoulement simple $v_x(y)$ :

$$  
\tau = \eta \frac{\partial v_x}{\partial y}  
$$

Force sur une surface :

$$  
d\vec F = \eta \frac{\partial v_x}{\partial y} dS \vec u_x  
$$

>[!info]- ### Mesure de la viscosité avec un rhéomètre $\sigma = \eta \, \dot{\gamma}$.
>
>##### 1. Relation constitutive fondamentale
>
>Pour un fluide newtonien, la loi rhéologique est :
>
>$$
>\sigma = \eta \, \dot{\gamma}
>$$
>
>où :
>- $\sigma$ : contrainte de cisaillement (Pa)
>- $\dot{\gamma}$ : taux de cisaillement ($s^{-1}$)
>- $\eta$ : viscosité dynamique (Pa·s)
>
>👉 **But du rhéomètre : mesurer expérimentalement $\sigma$ et $\dot{\gamma}$ pour en déduire $\eta$.**
>##### 2. Principe général d’un rhéomètre
>
>Un rhéomètre impose :
>- soit une vitesse (donc $\dot{\gamma}$ imposé),
>- soit un couple / contrainte (donc $\sigma$ imposé),
>
>et mesure la réponse mécanique du fluide.
>##### 3. Rhéomètre de Couette cylindrique
>
>###### Géométrie
>Deux cylindres coaxiaux :
>- cylindre interne tournant,
>- cylindre externe fixe (ou inverse).
>
>###### Grandeurs mesurées
>
>$$
>\sigma = \frac{M}{2 \pi R^2 h}
>$$
>
>$$
>\dot{\gamma} = \frac{R}{\Delta R} \, \omega_0
>$$
>
>où :
>- $M$ : moment du couple mesuré (N·m)
>- $R$ : rayon moyen
>- $h$ : hauteur immergée
>- $\Delta R$ : entrefer
>- $\omega_0$ : vitesse angulaire
>
>###### Interprétation
>- $M \rightarrow \sigma$ : effort résistant du fluide
>- $\omega_0 \rightarrow \dot{\gamma}$ : déformation imposée
>
>👉 Le fluide relie les deux via sa viscosité :
>$$
>\eta = \frac{\sigma}{\dot{\gamma}}
>$$
>
>##### 4. Rhéomètre cône-plan
>
>###### Géométrie
>- un cône de petit angle $\alpha$,
>- une plaque plane.
>
>###### Relations
>
>$$
>\sigma = \frac{3M}{2 \pi R^3}
>$$
>
>$$
>\dot{\gamma} = \frac{\omega_0}{\alpha}
>$$
>
>où :
>- $\alpha$ est petit le $4^\circ$ → approximation de cisaillement uniforme
>
>###### Intérêt physique
>- $\dot{\gamma}$  est **constant dans tout l’échantillon**
>- donc $\sigma$ et $\dot{\gamma}$ sont directement homogènes
>
>##### 5. Lien fondamental entre $\sigma$ et $\dot{\gamma}$
>
>Dans les deux géométries :
>
>$$
>\sigma \propto M
>\quad \text{et} \quad
>\dot{\gamma} \propto \omega_0
>$$
>
>Donc le rhéomètre réalise une mesure expérimentale de la fonction :
>
>$$
>\sigma = f(\dot{\gamma})
>$$
>
>- Fluide newtonien : droite → pente = $\eta$
>- Fluide non-newtonien : courbe → $\eta(\dot{\gamma})$
>
>##### 6. Résumé conceptuel
>
>Le rhéomètre convertit :
>
>- un **effort mécanique global** → $M \rightarrow \sigma$
>- une **cinématique de rotation** → $\omega_0 \rightarrow \dot{\gamma}$
>
>et permet d’accéder à la loi constitutive du fluide :
>
>$$
>\sigma(\dot{\gamma})
>$$
>
## 3) Interprétation physique

👉 transfert de quantité de mouvement entre couches

- analogue à diffusion thermique
    
- mécanisme microscopique : collisions
    

---

## 4) Ordres de grandeur

- air : $\eta \sim 10^{-5}$ Pa·s
    
- eau : $\eta \sim 10^{-3}$ Pa·s
    

---

# II – Diffusion de quantité de mouvement

## 1) Équation de diffusion

$$  
\frac{\partial p_x}{\partial t} = \nu \frac{\partial^2 p_x}{\partial y^2}  
$$

avec :

$$  
\nu = \frac{\eta}{\rho}  
$$

---

## 2) Interprétation

👉 viscosité = diffusion de quantité de mouvement

---

## 3) Échelle caractéristique

$$  
\delta \sim \sqrt{\nu t}  
$$

👉 épaisseur de pénétration

---

# III – Équation de Navier–Stokes

## 1) Forme générale

$$  
\rho \left( \frac{\partial \vec v}{\partial t} + (\vec v \cdot \nabla) \vec v \right) = -\nabla p + \eta \Delta \vec v + \vec f  
$$

---

## 2) Structure des termes

- inertie : $\partial_t \vec v$
    
- convection : $(\vec v \cdot \nabla)\vec v$
    
- diffusion : $\eta \Delta \vec v$
    

---

## 3) Point subtil (oral important)

👉 pourquoi $\rho$ est devant ?

- conservation de la masse
    
- théorème de Reynolds
    

---

## 4) Conditions aux limites

- adhérence (no-slip)
    
- impénétrabilité
    
- continuité des contraintes
    

---

# IV – Nombre de Reynolds

## 1) Définition

$$  
Re = \frac{UL}{\nu}  
$$

---

## 2) Interprétation

$$  
Re = \frac{\text{convection}}{\text{diffusion}}  
$$

---

## 3) Régimes

- $Re \ll 1$ : laminaire visqueux
    
- $Re \gg 1$ : turbulent
    

---

## 4) Temps caractéristiques

- convection : $L/U$
    
- diffusion : $L^2/\nu$
    

---

# V – Écoulements visqueux

## 1) Écoulement de Couette

### Hypothèses

- stationnaire
    
- parallèle
    

$$  
\vec v = v_x(y) \vec u_x  
$$

---

### Résolution

$$  
\frac{d^2 v_x}{dy^2} = 0  
$$

Solution :

$$  
v_x(y) = ay + b  
$$

👉 profil linéaire

---

### Application

👉 viscosimètre de Couette

---

## 2) Régime de Stokes ($Re \ll 1$)

Équation simplifiée :

$$  
0 = -\nabla p + \eta \Delta \vec v  
$$

---

### Propriété clé

👉 réversibilité cinématique

---

## 3) Force de Stokes

Pour une sphère :

$$  
\vec F = -6 \pi \eta R \vec v  
$$

👉 traînée visqueuse

---

## 4) Analyse dimensionnelle

Coefficient de traînée :

$$  
C_d = f(Re)  
$$

---

# VI – Message physique fort

- viscosité = diffusion de quantité de mouvement
    
- NS = bilan local de quantité de mouvement
    
- Reynolds = compétition des mécanismes
    

---

# VII – Ouvertures

- écoulement de Poiseuille
    
- turbulence
    
- fluides non newtoniens
    

---

# ⚠️ Questions du jury

- origine microscopique de la viscosité
    
- différence η / ν
    
- validité de Navier–Stokes
    
- interprétation de Re
    
- conditions aux limites
    

---

# 💡 Bonus différenciant

- insister sur analogie diffusion
    
- interprétation en temps caractéristiques
    
- lien avec turbulence