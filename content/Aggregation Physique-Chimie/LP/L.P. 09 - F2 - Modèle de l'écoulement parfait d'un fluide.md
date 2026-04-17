---
title: L.P. 09 - F2 - Modèle de l'écoulement parfait d'un fluide
tags:
  - Agrégation
  - Physique
  - Oral
---

### Modèle de l’écoulement parfait d’un fluide (Cours 40 min – Agrégation, version approfondie)

---

## 🎯 Fil directeur (à annoncer clairement)

> **On simplifie Navier–Stokes en négligeant la viscosité → équation d’Euler → intégrale première = Bernoulli → validité limitée (couche limite) → applications aéronautiques**

---

# Plan (très oral)

I. Équation d’Euler et modèle du fluide parfait  
II. Domaine de validité : couche limite  
III. Relation de Bernoulli (structure + énergie)  
IV. Applications : Pitot, portance, paradoxe de d’Alembert

---

# I – Écoulement parfait et équation d’Euler

## 1) Hypothèse physique

👉 Fluide parfait = **absence de viscosité**

Conséquences :

- pas de diffusion de quantité de mouvement
    
- pas de dissipation
    
- contraintes uniquement normales (pression)
    

---

## 2) Équation d’Euler

$$  
\rho \left( \frac{\partial \vec v}{\partial t} + (\vec v \cdot \nabla) \vec v \right) = -\nabla P + \rho \vec g  
$$

👉 Équation locale, non linéaire, **ordre 1 en espace**

⚠️ Point fin (jury) :

- valable même si fluide compressible
    
- contrairement à Navier–Stokes qui suppose un modèle de viscosité
    

---

## 3) Cas particuliers

- stationnaire : $\partial_t \vec v = 0$
    
- incompressible : $\nabla \cdot \vec v = 0$
    
- irrotationnel : $\nabla \times \vec v = 0$
    

---

## 4) Remarque physique

👉 Exemple limite : superfluide (He II)

---

# II – Validité : couche limite

## 1) Problème fondamental

👉 Euler ne satisfait pas la condition d’adhérence

---

## 2) Rôle de la viscosité

- agit là où gradients forts
    
- donc **près des parois**
    

---

## 3) Couche limite (Prandtl)

$$  
\delta \sim \frac{L}{\sqrt{Re}}  
$$

---

## 4) Structure réelle d’un écoulement

- cœur : fluide parfait
    
- couche limite : fluide visqueux
    

👉 modèle composite essentiel

---

# III – Relation de Bernoulli

## 1) Hypothèses

- fluide parfait
    
- stationnaire
    
- incompressible
    
- référentiel galiléen
    

---

## 2) Démonstration propre (important agrég)

Identité vectorielle :

$$  
(\vec v \cdot \nabla)\vec v = \nabla\left(\frac{v^2}{2}\right) - \vec v \times (\nabla \times \vec v)  
$$

Si écoulement irrotationnel :

$$  
\nabla \times \vec v = 0  
$$

Donc Euler devient :

$$  
\nabla \left( \frac{v^2}{2} + \frac{P}{\rho} + gz \right) = 0  
$$

---

## 3) Résultat (Bernoulli)

$$  
\frac{P}{\rho} + \frac{v^2}{2} + gz = C  
$$

- constante **le long d’une ligne de courant**
    
- constante partout si irrotationnel
    

---

## 4) Interprétation énergétique (clé)

👉 Bernoulli = **conservation de l’énergie mécanique volumique**

- pression → énergie interne disponible
    
- cinétique → $v^2/2$
    
- potentielle → $gz$
    

⚠️ Résultat repose sur :

- absence de dissipation
    
- puissance des forces internes nulle
    

---

# IV – Applications

## 1) Tube de Pitot

Bernoulli entre :

- point d’écoulement
    
- point d’arrêt ($v=0$)
    

$$  
\Delta P = \frac{1}{2} \rho U^2  
$$

👉 mesure de vitesse

---

## 2) Portance (idée)

- différence de vitesse → différence de pression
    
- force résultante sur l’aile
    

---

## 3) Paradoxe de d’Alembert (point fort jury)

👉 fluide parfait ⇒ **traînée nulle**

Explication :

- symétrie des lignes de courant
    
- absence de dissipation
    

👉 contradiction avec expérience

---

## 4) Résolution du paradoxe

👉 rôle de la couche limite :

- séparation
    
- dissipation
    
- création de traînée
    

---

# V – Message physique fort

- Euler = dynamique sans diffusion
    
- Bernoulli = conservation d’énergie
    
- validité locale (hors couche limite)
    

👉 un modèle puissant mais **structurellement incomplet**

---

# VI – Ouvertures intelligentes

- théorie de Prandtl
    
- potentiel des vitesses
    
- turbulence
    
- aérodynamique réelle
    

---

# ⚠️ Questions classiques du jury

- conditions exactes de Bernoulli
    
- pourquoi Euler ≠ Navier–Stokes
    
- origine de la couche limite
    
- paradoxe de d’Alembert
    
- rôle du nombre de Reynolds
    

---

# 💡 Bonus (niveau top)

👉 articulation parfaite :

Navier–Stokes → Euler → Bernoulli → échec (d’Alembert) → correction (couche limite)

👉 montre que tu maîtrises **la physique et pas juste les équations**