---
title: L.P. 09 - F2 - Modèle de l'écoulement parfait d'un fluide
tags:
  - Agrégation
  - Physique
  - Oral
---

### Liens

[^1]: Physique Spé. MP*, MP et PT*, PT, Gié, Sarmant, Olivier, More, Tec & Doc, 2000. 
[^2]: <a href="https://drive.google.com/file/d/1TxXiIyUpuNKw5627Li3pU42FJj_YZc58/view?usp=sharing#page=100&zoom=125" target="_blank" rel="noopener noreferrer">Hydrodynamique physique, Guyon-Hulin-Petit (2001) page ???</a>.

>- 👉 <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/Aggregation%20Physique-Chimie/Oraux/2021%20Guillaume%20Themeze/Orale.pdf#page=81&zoom=125" target="_blank" rel="noopener noreferrer">Manuscrit page 81</a>
>- <a href="https://themeze.github.io/quartz_note/Aggregation-Physique-Chimie/LP/L.P.-05---M2---Lois-de-conservation-en-dynamique#iv--lois-de-conservation-en-mécanique-des-fluides" target="_blank" rel="noopener noreferrer">M2-IV-Lois de conservation en mécanique des fluides</a> ---- [[Aggregation Physique-Chimie/LP/L.P. 05 - M2 - Lois de conservation en dynamique#IV – Lois de conservation en mécanique des fluides|M2-IV-Lois de conservation en mécanique des fluides]]
>- <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/index.html?pdf=Aggregation%20Physique-Chimie/Oraux/" target="_blank" rel="noopener noreferrer">Lectures notes</a>

>-  <a href="https://drive.google.com/drive/folders/1i2FSRuEZTBRqYO-y2Ji_k-yNDNXvW4se?usp=drive_link/" target="_blank" rel="noopener noreferrer">Aggrégatifs</a>
>- <a href="https://drive.google.com/drive/folders/1EC5KW0wH97j7zVyYvGNlaMYUPvEYJwLB?usp=drive_link" target="_blank" rel="noopener noreferrer">Archives</a>

>- <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/Aggregation%20Physique-Chimie/Oraux/2018%20Benjamin%20Marchetti/lecon_physique_marchetti.pdf#page=45&zoom=125" target="_blank" rel="noopener noreferrer">Manuscrit BM</a> <-  <a href="https://marchettibenjamin.wordpress.com/agregation/plans-de-lecons/" target="_blank" >site perso</a>
>- <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/Aggregation%20Physique-Chimie/Oraux/2019%20Jules%20Fillette/LeconsPhysique.pdf#page=39&zoom=125" target="_blank" rel="noopener noreferrer">Manuscrit JF</a>
>- <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/Aggregation%20Physique-Chimie/Oraux/2019%20Julien%20Froustey/Plans_JF_2019.pdf#page=31&zoom=125" target="_blank" rel="noopener noreferrer">Manuscrit JFr</a>
>- <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/Aggregation%20Physique-Chimie/Oraux/2019%20Hugo%20Roussille/plans_lecon_physique.pdf#page=39&zoom=125" target="_blank" rel="noopener noreferrer"> Manuscrit HR</a>
>- <a href="https://themeze.github.io/portfolio_recherche_2/physics/faculty/themeze/documents/Aggregation%20Physique-Chimie/Archives/Physique-agreg.pdf#page=151&zoom=125" target="_blank" rel="noopener noreferrer"> Manuscrit PHS</a>
>- <a href="https://github.com/AnassNajlaoui/Lecons-Anass-Najlaoui-Agregation-Physique-2026/blob/main/F1.%20Notion%20de%20viscosit%C3%A9%20d'un%20fluide.%20%C3%89coulements%20visqueux./Scan_20260416_114156.pdf" target="_blank" rel="noopener noreferrer"> Manuscrit AN ???</a>

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