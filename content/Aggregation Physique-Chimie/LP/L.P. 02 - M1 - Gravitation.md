---
title: L.P. 02 - Gravitation
tags:
  - Agrégation
  - Physique
  - Oral
---

### Gravitation (Niveau Licence → Agrégation)

## Objectifs

- Introduire la gravitation newtonienne comme interaction fondamentale
    
- Relier force, champ et énergie
    
- Étudier le mouvement dans un potentiel central
    
- Retrouver les lois de Kepler
    
- Introduire des ouvertures vers la relativité générale
    
(autre version [[L.P. 02 - M1 - Gravitation (Version Agrégation — Niveau normalien top 5)]])

---

## I – Force gravitationnelle

### 1) Loi de Newton

Deux masses ponctuelles $M$ et $m$ séparées par une distance $r$ interagissent via :

$$  
\vec{F} = - G \frac{Mm}{r^2} \vec{u}_r  
$$

- Force **centrale**
    
- Force **attractive**
    
- Force **conservative**
    

### 2) Énergie potentielle gravitationnelle

On associe une énergie potentielle :

$$  
E_p(r) = - G \frac{Mm}{r}  
$$

- Origine choisie à l'infini
    
- Interaction à longue portée
    

### 3) Travail de la force gravitationnelle

Le travail entre $r_1$ et $r_2$ vaut :

$$  
W = \int_{r_1}^{r_2} \vec{F} \cdot d\vec{r} = E_p(r_1) - E_p(r_2)  
$$

Donc :

$$  
W = - \Delta E_p  
$$

👉 Interprétation :

- Si la particule se rapproche ($r$ diminue), le travail est **positif**
    
- L'énergie potentielle diminue, transformée en énergie cinétique
    

---

## II – Champ gravitationnel et analogie électrostatique

### 1) Champ gravitationnel

$$  
\vec{G} = \frac{\vec{F}}{m} = - G \frac{M}{r^2} \vec{u}_r  
$$

### 2) Analogie électrostatique

|Gravitation|Électrostatique|
|---|---|
|Masse $m$|Charge $q$|
|Champ $\vec{G}$|Champ $\vec{E}$|
|$-G M / r^2$|$k q / r^2$|

### 3) Théorème de Gauss gravitationnel

$$  
\nabla \cdot \vec{G} = -4\pi G \rho  
$$

- Analogue direct de l’électrostatique
    
- Permet de retrouver le champ d’une sphère
    

👉 Résultat clé :  
Une distribution sphérique agit comme une masse ponctuelle à l’extérieur.

---

## III – Mouvement dans un potentiel newtonien

### 1) Équation du mouvement

$$  
m \ddot{\vec{r}} = - G \frac{Mm}{r^2} \vec{u}_r  
$$

👉 Force centrale ⇒ conservation du moment cinétique

$$  
\vec{L} = m \vec{r} \wedge \vec{v} = \text{cste}  
$$

### 2) Loi des aires

$$  
\frac{dA}{dt} = \frac{L}{2m} = \text{cste}  
$$

👉 **Deuxième loi de Kepler**

---

### 3) Énergie mécanique

$$  
E_m = E_c + E_p = \frac{1}{2} m v^2 - G \frac{Mm}{r}  
$$

👉 Conservée (force conservative)

---

### 4) Potentiel effectif

On réduit le problème radial :

$$  
E_m = \frac{1}{2} m \dot{r}^2 + E_{p,eff}(r)  
$$

avec :

$$  
E_{p,eff}(r) = \frac{L^2}{2mr^2} - G \frac{Mm}{r}  
$$

👉 Interprétation :

- Terme $\sim 1/r^2$ : barrière centrifuge
    
- Terme gravitationnel : attractif
    

### 5) Types de trajectoires

- $E_m < 0$ : orbites **liées** (ellipse)
    
- $E_m = 0$ : **parabole**
    
- $E_m > 0$ : **hyperbole**
    

---

## IV – Équation de la trajectoire

Résultat :

$$  
r(\theta) = \frac{p}{1 + e \cos\theta}  
$$

- $e$ : excentricité
    
- $p = \frac{L^2}{GMm^2}$
    

### Interprétation

- $e < 1$ : ellipse
    
- $e = 1$ : parabole
    
- $e > 1$ : hyperbole
    

👉 **Première loi de Kepler** retrouvée

---

## V – Troisième loi de Kepler

Pour une orbite elliptique :

$$  
T^2 \propto a^3  
$$

avec :

$$  
T^2 = \frac{4\pi^2}{GM} a^3  
$$

👉 Universelle pour tous les corps orbitant autour de $M$

---

## VI – Applications

### 1) Planètes

- Référentiel héliocentrique
    
- Orbites quasi elliptiques
    
- Faible excentricité
    

### Limites

- Précession de Mercure
    
- Découverte de Neptune
    

👉 Nécessite la relativité générale

---

### 2) Satellites terrestres

#### Vitesse orbitale

$$  
v_0 = \sqrt{\frac{GM_T}{R_T}}  
$$

#### Vitesse de libération

$$  
v_{lib} = \sqrt{\frac{2GM_T}{R_T}}  
$$

---

## VII – Travail et énergie (point clé oral)

### 1) Théorème de l’énergie cinétique

$$  
\Delta E_c = W_{tot}  
$$

Dans le cas gravitationnel :

$$  
\Delta E_c = - \Delta E_p  
$$

Donc :

$$  
E_m = E_c + E_p = \text{cste}  
$$

### 2) Lecture physique

- Chute libre : conversion $E_p \to E_c$
    
- Satellite : équilibre dynamique entre énergie cinétique et potentielle
    
- Évasion : $E_m \geq 0$
    

### 3) Interprétation graphique

Le potentiel effectif permet de lire :

- points de retournement
    
- orbites possibles
    
- stabilité
    

---

## VIII – Ouverture : Relativité Générale

- Gravitation = courbure de l’espace-temps
    
- Pas une force au sens newtonien
    
- Géodésiques dans une métrique courbe
    

Exemple :

- Précession du périhélie de Mercure
    
- Rayon de Schwarzschild
    

---

## IX – Points à maîtriser (questions jury)

- Mesure de la constante $G$
    
- Différence gravitation / pesanteur
    
- Référentiel barycentrique
    
- Mouvement à deux corps
    
- Limites du modèle newtonien
    

---

## Conclusion

La gravitation newtonienne fournit un cadre extrêmement puissant pour comprendre :

- la chute des corps
    
- les orbites
    
- la structure du système solaire
    

Elle illustre parfaitement :  
👉 lien entre symétries, invariants et intégrabilité  
👉 rôle central de l’énergie et du moment cinétique

Ouverture naturelle : relativité générale.

