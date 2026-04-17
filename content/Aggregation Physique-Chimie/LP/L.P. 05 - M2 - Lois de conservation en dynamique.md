---
title: L.P. 05 - M2 - Lois de conservation en dynamique
tags:
  - Agrégation
  - Physique
  - Oral
---


---

## 🎯 Fil directeur

> **Symétries → lois de conservation → réduction drastique des équations du mouvement**

Les lois de conservation ne sont pas des « accidents » : elles proviennent de propriétés fondamentales de l’espace et du temps (théorème de Noether).

---

# Plan (annoncé à l’oral)

I. Quantité de mouvement (translation spatiale)  
II. Moment cinétique (rotation)  
III. Énergie (translation temporelle)  
IV. Application structurante : problème à deux corps  
V. Ouverture : Noether et portée générale

---

# I – Conservation de la quantité de mouvement

## 1) Théorème fondamental

Pour un système :

$$  
\frac{d\vec P}{dt} = \vec R_{ext}  
$$

avec :

$$  
\vec P = \sum_i m_i \vec v_i  
$$

👉 Si système isolé :

$$  
\vec R_{ext} = 0 \Rightarrow \vec P = \text{cste}  
$$

---

## 2) Interprétation profonde

👉 **Homogénéité de l’espace**

Si les lois de la physique ne dépendent pas de la position ⇒ conservation de la quantité de mouvement.

Version "physicien" :

Si $U(x)$ ne dépend pas de $x$ ⇒ $p_x$ conservée.

---

## 3) Centre de masse

$$  
\vec R_G = \frac{1}{M} \sum m_i \vec r_i  
$$

Alors :

$$  
M \vec V_G = \vec P  
$$

👉 Mouvement du centre de masse :

$$  
M \frac{d\vec V_G}{dt} = \vec R_{ext}  
$$

---

## 4) Exemple clé (oral)

Ours sur la banquise :

- Pas besoin de connaître le détail du mouvement
    
- Seule la conservation de $\vec P$ fixe le résultat final
    

👉 Message jury : **puissance globale des lois de conservation**

---

# II – Conservation du moment cinétique

## 1) Théorème du moment cinétique

$$  
\frac{d\vec L_O}{dt} = \vec M_O^{ext}  
$$

avec :

$$  
\vec L_O = \sum \vec{OM_i} \wedge m_i \vec v_i  
$$

---

## 2) Cas de conservation

- Système isolé
    
- Force centrale
    

$$  
\vec F \parallel \vec r \Rightarrow \vec M = 0  
$$

👉 Donc :

$$  
\vec L = \text{cste}  
$$

---

## 3) Interprétation

👉 **Isotropie de l’espace**

Si le système ne dépend pas de l’angle ⇒ moment cinétique conservé

---

## 4) Conséquences majeures

- Mouvement plan
    
- Loi des aires :
    

$$  
r^2 \dot\theta = \text{cste}  
$$

👉 Kepler 2 directement

---

## 5) Exemple physique

Patineur / disque :

$$  
L = I \omega = \text{cste}  
$$

👉 variation de $\omega$ sans force externe

---

# III – Conservation de l’énergie

## 1) Théorème de l’énergie cinétique

$$  
\Delta E_c = W_{ext} + W_{int}  
$$

👉 Attention : forces internes apparaissent

---

## 2) Systèmes conservatifs

Si forces dérivent d’un potentiel :

$$  
E_m = E_c + E_p = \text{cste}  
$$

---

## 3) Origine fondamentale

👉 **Invariance par translation temporelle**

Le temps est homogène ⇒ énergie conservée

---

## 4) Subtilités importantes (oral++)

- Énergie mécanique pas toujours conservée
    
- Dissipation ⇒ énergie interne
    
- Vision correcte : **énergie totale conservée**
    

---

## 5) Puissance en 1D

$$  
\frac{1}{2} m \dot x^2 + V(x) = E  
$$

👉 résolution complète sans équation différentielle

---

# IV – Application : problème à deux corps

## 1) Réduction du problème

Deux corps $m_1, m_2$ ⇒ masse réduite :

$$  
\mu = \frac{m_1 m_2}{m_1 + m_2}  
$$

Centre de masse découplé

---

## 2) Quantité de mouvement

$$  
\vec P = \text{cste} \Rightarrow \vec V_G = \text{cste}  
$$

👉 Travail dans le référentiel barycentrique

---

## 3) Moment cinétique

Force centrale ⇒

$$  
\vec L = \text{cste}  
$$

👉 mouvement plan + loi des aires

---

## 4) Énergie

$$  
E = \frac{1}{2} \mu \dot r^2 + \frac{L^2}{2\mu r^2} + U(r)  
$$

👉 potentiel effectif :

$$  
V_{eff}(r) = \frac{L^2}{2\mu r^2} + U(r)  
$$

---

## 5) Lecture qualitative

- Points de retournement
    
- États liés vs diffusion
    
- Orbites circulaires (minimum)
    

👉 **Sans résoudre les équations !**

---

## 6) Cas newtonien (bonus top niveau)

$$  
U(r) = - \frac{GM\mu}{r}  
$$

👉 invariant supplémentaire : Runge–Lenz

⇒ trajectoires coniques

---

# V – Synthèse : puissance des lois de conservation

|Symétrie|Quantité conservée|
|---|---|
|Translation espace|Quantité de mouvement|
|Rotation|Moment cinétique|
|Translation temps|Énergie|

👉 Structure universelle de la physique

---

# VI – Ouverture : théorème de Noether

## Énoncé (version simple)

Toute symétrie continue d’un système ⇒ quantité conservée

---

## Lecture physique

- espace homogène ⇒ $\vec P$
    
- espace isotrope ⇒ $\vec L$
    
- temps homogène ⇒ $E$
    

---

## Message final (très important à l’oral)

> Les lois de conservation ne sont pas seulement des outils de calcul :  
> elles révèlent la structure profonde des lois physiques.

---

# Conclusion

Les lois de conservation permettent :

- simplification drastique des problèmes
    
- compréhension qualitative sans résolution
    
- lien profond entre mathématiques et physique
    

👉 Exemple ultime : problème de Kepler entièrement contrôlé par ces invariants

---

# ⚠️ Questions classiques du jury

- Différence système isolé / pseudo-isolé
    
- Validité du référentiel barycentrique
    
- Pourquoi une force centrale conserve $\vec L$ ?
    
- Différence énergie mécanique / totale
    
- Peut-on avoir conservation de $\vec P$ sans homogénéité ?
    

---

# 💡 Bonus différenciant

- Mention explicite de Noether
    
- Lecture hamiltonienne (si question)
    
- Insister sur "sans résoudre les équations"
    
- Faire un lien avec relativité ou collisions