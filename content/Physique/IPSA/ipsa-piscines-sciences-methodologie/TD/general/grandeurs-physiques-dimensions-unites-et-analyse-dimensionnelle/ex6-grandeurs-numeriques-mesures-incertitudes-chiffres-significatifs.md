---
title: "Exercice 6 — (*) Grandeurs numériques : mesures, incertitudes $\\&$ chiffres significatifs"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/index|⬅ Retour]] · <a href="/pdfs/td1_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 6. (*) Grandeurs numériques : mesures, incertitudes $\&$ chiffres significatifs *(facultatif)*

Cet exercice aborde la manipulation des grandeurs expérimentales, la gestion des incertitudes et l'application stricte des règles sur les chiffres significatifs lors des opérations physiques.

**q1.** **Mesures $\&$ incertitudes**\\

Les valeurs numériques obtenues à partir de mesures comportent toujours une incertitude.\\

Soit une mesure de la masse $m$ dont le résultat est $15,6 ~g$ avec une incertitude de $2 \%$




(a) Donner l’incertitude relative et absolue de la mesure, en précisant leur dimension.

(b) Comment écrit-on le résultat de la mesure de $m$?

(c) Donner l’intervalle contenant la valeur réelle.

(d) Combien de chiffres significatifs contient la mesure ? Le chiffre 6 est-il certain ?

> [!tip]- 💡 Coup de pouce
> **Calcul de $\Delta m$
> **
>
> Calculer l'incertitude absolue en effectuant $2\%$ de $15,6 \text{ g}$, puis arrondir l'incertitude absolue à $1$ chiffre significatif par excès.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 1
> **
>
> (a) - **Incertitude relative** : $\frac{\Delta m}{m} = 2 \% = 0,02$. Elle est adimensionnelle (dimension 1).
> - **Incertitude absolue** : $\Delta m = 0,02 \times 15,6 \text{ g} = 0,312 \text{ g}$. En arrondissant à un chiffre significatif par excès : $\Delta m = 0,3 \text{ g}$. Sa dimension est une masse ($[\Delta m] = M$).
>
> (b) L'écriture rigoureuse demande d'aligner le nombre de décimales de la valeur mesurée sur celui de l'incertitude absolue :
>   $$m = (15,6 \pm 0,3) \text{ g}$$
>
> (c) L'intervalle de confiance est $m_e \in [15,6 - 0,3 ~;~ 15,6 + 0,3]$, soit $m_e \in [15,3 \text{ g} ~;~ 15,9 \text{ g}]$.
>
> (d) La valeur $15,6 \text{ g}$ comporte **3 chiffres significatifs** ($1$, $5$ et $6$). Le chiffre $6$ est incertain (sa valeur réelle oscille entre $3$ et $9$).


**q2.** **Expression rigoureuse d’une grandeur numérique**\\



(a) Indiquer si ces écritures sont correctes pour la mesure de la longueur $\ell$ :
    

- $\ell = 15,62 \pm 0,016 ~ cm$
- $\ell = 15,62 \pm 0,08$
- $\ell = 15,62 \pm 0,04 ~ cm$

(b) Calculer le volume $V$ d’un cylindre de rayon $r= 1,26 ~ cm$ et de hauteur $h= 7,3 ~cm$.

(c) Exprimer avec le bon nombre de chiffres significatifs la somme de : $0,056 \times 10^2 + 11,8 \times 10^{-1}$

> [!tip]- 💡 Coup de pouce
> **Calculs géométriques et sommes
> **
>
> * Volume du cylindre : $V = \pi r^2 h$. Compter le nombre de CS de $r$ ($3$ CS) et $h$ ($2$ CS).
> * Pour la somme : écrire les deux nombres avec la même puissance de $10$ avant d'additionner.


> [!example]- 📝 Solution détaillée
> **Correction détaillée de la question 2
> **
>
> %
>
> (a) %
>
> (b) %  
>
> - %
> - $\ell = 15,62 \pm 0,016 \text{ cm}$ : **Incorrecte**. L'incertitude a $3$ décimales alors que la valeur mesurée n'en a que $2$. De plus, il manque des parenthèses.
> %
> - $\ell = 15,62 \pm 0,08$ : **Incorrecte**. L'unité est absente.
> %
> - $\ell = 15,62 \pm 0,04 \text{ cm}$ : **Incorrecte** (sans parenthèses), mais la cohérence des décimales est respectée. L'écriture rigoureuse est $\ell = (15,62 \pm 0,04) \text{ cm}$.
> %
>
>
> %
>
> (c) $V = \pi \times r^2 \times h = \pi \times (1,26)^2 \times 7,3 \approx 36,408 \text{ cm}^3$.\\
> %  Le facteur le moins précis est $h = 7,3 \text{ cm}$ ($2$ chiffres significatifs). Le résultat doit donc être arrondi à **2 chiffres significatifs** :
> %  $$V = 36 \text{ cm}^3 \quad \text{ou} \quad V = 3,6 \times 10^1 \text{ cm}^3$$
> %
>
> (d) Ramenons les deux termes à la même puissance de $10$ (par exemple $10^0 = 1$) :
> %  $$A = 0,056 \times 10^2 = 5,6 \quad (\text{1 décimale})$$
> %  $$B = 11,8 \times 10^{-1} = 1,18 \quad (\text{2 décimales})$$
> %  La somme donne $5,6 + 1,18 = 6,78$. Le résultat doit être arrondi à la donnée ayant le moins de décimales ($1$ seule décimale, imposée par $5,6$) :
> %  $$\text{Somme} = 6,8$$
> %
>
>
>
>
>
> (a) - $\ell = 15,62 \pm 0,016 \text{ cm}$ : **Incorrecte**. L'incertitude comporte $3$ décimales, tandis que la valeur mesurée n'en comporte que $2$. Il faut harmoniser le nombre de décimales de la valeur et de son incertitude (ou écrire la mesure entre parenthèses : $(15,620 \pm 0,016) \text{ cm}$).
> - $\ell = 15,62 \pm 0,08$ : **Incorrecte**.
>     L'unité de longueur n'est pas précisée.
> - $\ell = 15,62 \pm 0,04 \text{ cm}$ : **Correcte**. 
>     Cette écriture peut être rencontrée dans la littérature scientifique.
>     Cependant, l'utilisation de parenthèses est préférable, car elle
>     rend explicite le fait que l'incertitude et la valeur mesurée
>     possèdent la même unité et évite toute ambiguïté :
>     $$
>     \ell = (15,62 \pm 0,04) \text{ cm}.
>     $$
>
> (b) $V = \pi \times r^2 \times h
>   = \pi \times (1,26)^2 \times 7,3
>   \approx 36,408 \text{ cm}^3$.\\
>
>   Le facteur le moins précis est $h = 7,3 \text{ cm}$
>   ($2$ chiffres significatifs). Le résultat doit donc être arrondi
>   à **2 chiffres significatifs** :
>
>   $$
>   V = 36 \text{ cm}^3
>   \quad \text{ou} \quad
>   V = 3,6 \times 10^1 \text{ cm}^3
>   $$
>
> (c) Ramenons les deux termes à la même puissance de $10$
>   (par exemple $10^0 = 1$) :
>
>   $$
>   A = 0,056 \times 10^2 = 5,6
>   \quad (\text{1 décimale})
>   $$
>
>   $$
>   B = 11,8 \times 10^{-1} = 1,18
>   \quad (\text{2 décimales})
>   $$
>
>   La somme donne $5,6 + 1,18 = 6,78$.
>   Le résultat doit être arrondi à la donnée ayant le moins de décimales
>   ($1$ seule décimale, imposée par $5,6$) :
>
>   $$
>   \text{Somme} = 6,8
>   $$


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex9-entrainement-chiffres-significatifs-incertitudes-et-propagation|Exercice 9 — (*) Entraînement : chiffres significatifs, incertitudes et propagation]]

