---
title: "Exercice 6 — (*) Grandeurs numériques : mesures, incertitudes $\\&$ chiffres significatifs"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/index|⬅ Retour]] · <a href="/pdfs/td1_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 6. (*) Grandeurs numériques : mesures, incertitudes $\&$ chiffres significatifs *(facultatif)*

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 25 min · Type : Révision*

Cet exercice aborde la manipulation des grandeurs expérimentales, la gestion des incertitudes et l'application stricte des règles sur les chiffres significatifs lors des opérations physiques.


> [!abstract]- 🧠 À savoir avant
> **Notions de base de métrologie**
>
> Connaître 
>
>
> - les opérations arithmétiques de base,
> - la notion de pourcentage,
> - l'écriture scientifique et
> - la définition d'un chiffre significatif




> [!info]- 🎯 Ce que tu sauras faire
> **Savoir présenter un résultat expérimental**
>
> - Distinguer incertitude absolue et incertitude relative.
> - Écrire un résultat sous la forme $x = (x_m \pm \Delta x) \text{ unité}$ de manière cohérente.
> - Conserver le bon nombre de chiffres significatifs après une opération (somme ou produit).




> [!tip]- 📖 Rappel de cours
> **Chiffre significatif**
>
> - **Chiffres significatifs** : les chiffres significatifs d'une
>   valeur numérique sont les chiffres qui apportent une information sur
>   la précision de la mesure. On ne conserve que les chiffres justifiés
>   par la précision de l'expérience afin de ne pas donner une précision
>   artificielle au résultat.
> - **Influence de l'unité choisie** : le nombre de chiffres
>   significatifs d'une grandeur physique doit rester cohérent lorsque
>   l'on change d'unité. La valeur numérique et l'unité évoluent
>   conjointement, mais la précision physique de la mesure reste
>   inchangée. Par exemple :
>   $$
>   0,0040~\text{m} = 4,0 \times 10^{-3}~\text{m}
>   = 4,0~\text{mm}.
>   $$
>   Ces trois écritures possèdent toutes **2 chiffres significatifs**.
>   Les zéros servant uniquement à positionner la virgule ne sont pas
>   significatifs.
> - **Lien avec l'écriture scientifique** : l'écriture scientifique
>   permet de faire apparaître explicitement le nombre de chiffres
>   significatifs. Elle s'écrit sous la forme
>   $$
>   a \times 10^n, \qquad 1 \leq |a| < 10.
>   $$
>   Les chiffres significatifs sont alors ceux du coefficient $a$.
>   Par exemple, $0,0040 = 4,0 \times 10^{-3}$ comporte 2 chiffres
>   significatifs, tandis que $4 \times 10^{-3}$ n'en comporte qu'un.
>
>
> **Merci DECHAUX Tom pour les precisions**\\
>
> **Incertitudes et chiffres significatifs**
>
> - **Incertitude absolue** $\Delta x$ : même dimension et unité que $x$. Elle s'arrondit généralement à $1$ seul chiffre significatif par excès.
> - **Incertitude relative** $\frac{\Delta x}{x}$ : grandeur adimensionnelle (souvent exprimée en $\%$).
> - Le dernier chiffre significatif conservé sur la valeur mesurée $x_m$ doit correspondre à la position du chiffre de l'incertitude $\Delta x$.




> [!tip]- 💡 Coup de pouce
> **Gestion des chiffres significatifs
> **
>
> \begin{itemize}[label=$\star$]
> \item Pour une addition/soustraction, aligne les puissances de 10 puis compte le nombre de chiffres {\bf après la virgule} (décimales).
> \item Pour une multiplication/division, compte le nombre total de {\bf chiffres significatifs} des données entrantes.
> \item L'incertitude absolue subit la même unité et la même dimension que la grandeur mesurée.
> \end{itemize}



**q1.** **Mesures $\&$ incertitudes**\\

Les valeurs numériques obtenues à partir de mesures comportent toujours une incertitude.\\

Soit une mesure de la masse $m$ dont le résultat est $15,6 ~g$ avec une incertitude de $2 \%$




(a) Donner l’incertitude relative et absolue de la mesure, en précisant leur dimension.

(b) Comment écrit-on le résultat de la mesure de $m$?

(c) Donner l’intervalle contenant la valeur réelle.

(d) Combien de chiffres significatifs contient la mesure ? Le chiffre 6 est-il certain ?


> [!tip]- 📖 Rappel de cours
> **Définitions de base**
>
> Soit $x$ une grandeur physique.\\
>
>
> - L’**incertitude absolue** sur $x$, notée $\Delta x$ est la différence entre la valeur mesurée $x_m$ et la valeur exacte $x_e$ (vraie valeur inaccessible) :
>     $$
>     \Delta x = \vert x_m - x_e \vert \quad \text{Donc } x_e = x_m \pm \Delta x
>     $$
> - L’**incertitude relative** sur $x$ est le quotient : ${\displaystyle \frac{\Delta x}{x_m}}$
>
>
> En général, l’erreur sur la mesure (absolue ou relative) est une donnée de l’expérience. Elle dépend des méthodes de mesure et de l’appareillage.




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


> [!tip]- 📖 Rappel de cours
> **Règles de présentation et de calcul**
>
> Symbole de la grandeur = (Valeur numérique $\pm$ Incertitude) (Symbole de l’unité).\\
>
>
> - L’unité de la grandeur numérique doit toujours être précisée.
> - La valeur numérique est donnée en écriture scientifique de préférence.
> - Le **nombre** de **chiffres significatifs** doit être adapté à la précision de la mesure.
> - Le résultat d’une addition/soustraction comporte au maximum autant de décimales que la grandeur qui en a le moins.
> - Le résultat d’un produit/quotient comporte au maximum autant de chiffres significatifs que le facteur qui en a le moins.




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




> [!question]- 🔭 Aller plus loin — Lycée : Vocabulaire des mesures

> Identifier l'incertitude de lecture sur des instruments gradués (règle, éprouvette) ou digitaux (balance).




> [!question]- 🔭 Aller plus loin — CPGE : Propagation des incertitudes

> Utiliser la méthode des différentielles logarithmiques ou le calcul d'incertitude-type composée (NF EN ISO/IEC Guide 98-3) pour des fonctions à plusieurs variables.




> [!question]- 🔭 Aller plus loin — Licence : Incertitudes de type A et B

> Évaluer l'incertitude-type par approche statistique (Type A, écart-type de la moyenne) ou par loi de probabilité a priori (Type B, distribution uniforme/rectangulaire).




> [!question]- 🔭 Aller plus loin — Master : Inférence bayésienne en métrologie

> Traiter l'ajustement de données expérimentales complexes et estimer les incertitudes via des méthodes Monte-Carlo.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex9-entrainement-chiffres-significatifs-incertitudes-et-propagation|Exercice 9 — (*) Entraînement : chiffres significatifs, incertitudes et propagation]]


