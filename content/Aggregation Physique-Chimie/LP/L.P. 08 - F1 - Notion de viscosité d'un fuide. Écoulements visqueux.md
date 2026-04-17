---
title: L.P. 08 - F1 - Notion de viscosité d'un fuide. Écoulements visqueux
tags:
  - Agrégation
  - Physique
  - Oral
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

# I – Notion de viscosité

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

---

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