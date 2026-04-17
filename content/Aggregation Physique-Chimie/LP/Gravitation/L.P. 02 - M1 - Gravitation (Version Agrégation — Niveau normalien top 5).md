---
title: L.P. 02 - M1- Gravitation (Version Agrégation — Niveau normalien top 5)
tags:
  - Agrégation
  - Physique
  - Oral
---

# Gravitation (Version Agrégation — Niveau normalien / top 5) 

---

## Fil directeur (à expliciter à l’oral)

> **Symétrie → invariants → intégrabilité → géométrie des trajectoires**

La gravitation newtonienne est un cas paradigmatique où une symétrie forte (force centrale en $1/r^2$) entraîne une intégrabilité complète (existence de $  
\vec L$ et du vecteur de Runge–Lenz), permettant une résolution exacte du mouvement.

---

## I – Formulation fondamentale : force, potentiel, Lagrangien

### 1) Force et potentiel

$$  
\vec{F} = - G \frac{Mm}{r^2} \vec{u}_r  
$$

$$  
V(r) = - G \frac{Mm}{r}  
$$

👉 Force conservative, champ dérivant d’un potentiel scalaire.

---

### 2) Formulation lagrangienne

$$  
\mathcal{L} = T - V = \frac{1}{2} m \dot{\vec r}^2 + G \frac{Mm}{r}  
$$

Symétrie : invariance par rotation ⇒ conservation du moment cinétique (théorème de Noether)

$$  
\vec L = m \vec r \wedge \vec v  
$$

---

### 3) Réduction à un problème à un degré de liberté

On travaille en coordonnées polaires :

$$  
T = \frac{1}{2} m (\dot r^2 + r^2 \dot \theta^2)  
$$

Conservation de $L$ :

$$  
L = m r^2 \dot \theta  
$$

⇒ élimination de $\dot\theta$

---

## II – Structure hamiltonienne et potentiel effectif

### 1) Hamiltonien

$$  
H = \frac{1}{2} m \dot r^2 + \frac{L^2}{2mr^2} - G \frac{Mm}{r}  
$$

👉 Lecture : dynamique radiale dans un potentiel effectif

$$  
V_{eff}(r) = \frac{L^2}{2mr^2} - G \frac{Mm}{r}  
$$

---

### 2) Analyse qualitative fine

- $r \to 0$ : $V_{eff} \to +\infty$ (barrière centrifuge)
    
- $r \to \infty$ : $V_{eff} \to 0^-$
    

Minimum : orbite circulaire stable

Condition :

$$  
\frac{dV_{eff}}{dr} = 0 \Rightarrow r_0 = \frac{L^2}{GMm^2}  
$$

👉 stabilité : $d^2 V_{eff}/dr^2 > 0$

---

## III – Intégrabilité et invariant de Runge–Lenz

### 1) Définition

$$  
\vec A = \vec v \wedge \vec L - GMm \vec u_r  
$$

👉 invariant spécifique au potentiel en $1/r$

---

### 2) Interprétation géométrique

- $\vec A$ pointe vers le périhélie
    
- $|\vec A| = GMm e$
    

👉 encode l’excentricité et l’orientation

---

### 3) Conséquence : trajectoires coniques

$$  
r(\theta) = \frac{p}{1 + e \cos\theta}  
$$

avec :

$$  
p = \frac{L^2}{GMm^2}  
$$

---

## IV – Classification énergétique et géométrique

Lien fondamental :

$$  
E = \frac{G^2 M^2 m^3}{2L^2}(e^2 - 1)  
$$

Donc :

- $E < 0$ ⇔ $e < 1$ : ellipse
    
- $E = 0$ ⇔ $e = 1$ : parabole
    
- $E > 0$ ⇔ $e > 1$ : hyperbole
    

👉 Correspondance exacte énergie ↔ géométrie

---

## V – Lois de Kepler (lecture structurée)

### 1) Loi des aires

Directement issue de :

$$  
\frac{dA}{dt} = \frac{L}{2m}  
$$

👉 conservation du moment cinétique

---

### 2) Loi des orbites

Résultat Runge–Lenz ⇒ coniques

---

### 3) Loi des périodes (démonstration rapide propre)

Aire ellipse : $\pi ab$

Vitesse aréolaire constante ⇒

$$  
T = \frac{2\pi ab}{(L/2m)}  
$$

Avec $b = a \sqrt{1-e^2}$ et $L^2 = GMm^2 a(1-e^2)$ ⇒

$$  
T^2 = \frac{4\pi^2}{GM} a^3  
$$

👉 démonstration compacte très appréciée au jury

---

## VI – Travail, énergie, et lecture physique avancée

### 1) Théorème de l’énergie

$$  
\Delta E_c = W  
$$

Force conservative ⇒

$$  
E = E_c + V = \text{cste}  
$$

---

### 2) Lecture dynamique profonde

Le mouvement radial vérifie :

$$  
\frac{1}{2} m \dot r^2 + V_{eff}(r) = E  
$$

👉 analogue à une particule 1D

---

### 3) Points de retournement

Solutions de :

$$  
E = V_{eff}(r)  
$$

⇒ périhélie / aphélie

---

### 4) Stabilité orbitale

- minimum de $V_{eff}$ ⇒ orbite circulaire stable
    
- perturbations ⇒ oscillations radiales (épicycles)
    

---

### 5) Lecture phase-space (bonus top niveau)

Le problème est intégrable ⇒

- trajectoires dans l’espace des phases régulières
    
- existence d’actions-angle
    

---

## VII – Problème à deux corps (rigoureux)

### 1) Réduction

Deux masses $m_1, m_2$ ⇒ masse réduite :

$$  
\mu = \frac{m_1 m_2}{m_1 + m_2}  
$$

Centre de masse découplé

---

### 2) Hamiltonien relatif

$$  
H = \frac{p^2}{2\mu} - G \frac{m_1 m_2}{r}  
$$

👉 même structure que problème à un corps

---

## VIII – Ordres de grandeur (impératif oral)

- Terre–Soleil : $v \sim 30$ km/s
    
- Satellite basse orbite : $v \sim 8$ km/s
    
- Énergie spécifique : $\sim 10^7$ J/kg
    

👉 montre la maîtrise physique, pas seulement formelle

---

## IX – Limites et ouverture relativiste

### 1) Limites newtoniennes

- non relativiste
    
- instantanéité de l’interaction
    

---

### 2) Relativité générale

- gravitation = géodésiques
    
- métrique courbe
    

Exemple clé :

- avance du périhélie de Mercure
    

---

## X – Points différenciants (ce que le jury attend au top niveau)

- Utilisation explicite de Noether
    
- Mention du Runge–Lenz comme signature d’intégrabilité
    
- Lecture du problème comme système hamiltonien
    
- Discussion du passage 2 corps → masse réduite
    
- Capacité à faire des ordres de grandeur rapidement
    

---

## Conclusion

Le problème de Kepler est un modèle canonique :

👉 intégrabilité exceptionnelle  
👉 lien profond entre symétrie et géométrie  
👉 transition naturelle vers la relativité générale

C’est un cas d’école où la physique théorique et l’observation expérimentale se rencontrent parfaitement.