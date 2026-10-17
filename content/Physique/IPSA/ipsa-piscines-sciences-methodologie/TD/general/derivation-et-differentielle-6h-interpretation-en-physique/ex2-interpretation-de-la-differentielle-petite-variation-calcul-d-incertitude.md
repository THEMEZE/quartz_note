---
title: "Exercice 2 — Interprétation de la différentielle : petite variation $\\&$ calcul d'incertitude"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/index|⬅ Retour]] · <a href="/pdfs/td2_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td2_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 2. Interprétation de la différentielle : petite variation $\&$ calcul d'incertitude

Cet exercice vise à comprendre le lien géométrique et physique entre la variation exacte d'une fonction $\Delta f$ et sa différentielle $\mathrm{d}f$, puis à appliquer cette notion à l'approximation des petites variations et au calcul d'incertitude.

**1.**

  **a)** La surface $S$ d'un carré de côté $x$ est donnée par $S(x) = x^2$. Déterminer la dérivée de $S$ par rapport à $x$, qu'on notera $\frac{\mathrm{d}S}{\mathrm{d}x}$. Vérifier l'homogénéité du résultat.

> [!tip]- 💡 Coup de pouce
> **Vérification des dimensions**
>
> Une surface $S$ est en $\text{m}^2$, un côté $x$ est en $\text{m}$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\frac{\mathrm{d}S}{\mathrm{d}x} = 2x$$
> **Homogénéité** : $[S] = L^2$, $[x] = L \implies \left[\frac{\mathrm{d}S}{\mathrm{d}x}\right] = \frac{L^2}{L} = L$. De même, $[2x] = L$. Le résultat est bien homogène à une longueur.


  **b)** En déduire la différentielle $\mathrm{d}S$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\mathrm{d}S = 2x \mathrm{d}x ~ (=  S'(x)\mathrm{d}x )  $$


  **c)** Exprimer la variation $\Delta S = S(x+\mathrm{d}x) - S(x)$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\Delta S = (x+\mathrm{d}x)^2 - x^2 = x^2 + 2x\mathrm{d}x + (\mathrm{d}x)^2 - x^2$$
> $$\Delta S = \overbrace{2x\mathrm{d}x}^{\mathrm{d}S}  + (\mathrm{d}x)^2$$


  **d)** Comparer $\Delta S$ et $\mathrm{d}S$ : les représenter sur la figure. Calculer pour $x = 10\text{ m}$ avec : $\mathrm{d}x = 3\text{ m}$, $\mathrm{d}x = 0,5\text{ m}$ et $\mathrm{d}x = 0,1\text{ m}$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\Delta S - \mathrm{d}S = (\mathrm{d}x)^2$$
> Géométriquement, $\mathrm{d}S = 2x\mathrm{d}x$ représente la surface de deux bandes rectangulaires de bordure, tandis que $(\mathrm{d}x)^2$ est la surface du petit carré d'angle.
>
> Pour $x = 10\text{ m}$ :
>
>
> - Pour $\mathrm{d}x = 3\text{ m}$ : $\mathrm{d}S(x) = 60\text{ m}^2$, $\Delta S(x) = 69\text{ m}^2$. $(\mathrm{d}x)^2 = 9\text{ m}^2$.
> - Pour $\mathrm{d}x = 0,5\text{ m}$ : $\mathrm{d}S(x) = 10\text{ m}^2$, $\Delta S(x) = 10,25\text{ m}^2$. $(\mathrm{d}x)^2 = 0,25\text{ m}^2$.
> - Pour $\mathrm{d}x = 0,1\text{ m}$ : $\mathrm{d}S(x) = 2\text{ m}^2$, $\Delta S(x) = 2,01\text{ m}^2$. $(\mathrm{d}x)^2 = 0,01\text{ m}^2$.
>
> <p style="text-align:center"><a href="/figures/td2_phv110_surface.svg" target="_blank" rel="noopener"><img src="/figures/td2_phv110_surface.svg" alt="" loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>


  **e)** Commenter l'égalité $\Delta S \approx \mathrm{d}S$ et interpréter.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> Lorsque $\mathrm{d}x \ll x$, le terme d'ordre deux $(\mathrm{d}x)^2$ devient négligeable devant le terme linéaire $2x\mathrm{d}x$. La différentielle est une approximation linéaire de la variation réelle.\\
>
> (Merci NZIENGUI Marc kharl pour la précision)\\
>
> <p style="text-align:center"><a href="/figures/td2_phv110_surface_graph.svg" target="_blank" rel="noopener"><img src="/figures/td2_phv110_surface_graph.svg" alt="" loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>


  **f)** Soit la mesure du côté $a$ d'un carré : $a = 2,5 \pm 0,1\text{ cm}$. Calculer la surface $S$ du carré et déterminer son incertitude $\Delta S$ :
(i) soit en exprimant la valeur maximale et minimale de $S$
(ii) soit par la méthode différentielle ($\Delta S \approx \mathrm{d}S$).

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $a_m = \overbrace{2,5\text{ cm} }^{a} \pm \overbrace{0,1 \text{ cm} }^{\mathrm{d}a }$ \\
>
> Valeur centrale : $S(a) = a^2 = (2,5 \text{ cm} ) ^2 = 6,25\text{ cm}^2$.
>
>
>
> - **Méthode des extrema** :
>
>
> - $S_{\max} = \overbrace{2,5\text{ cm} }^{a} +  \overbrace{0,1 \text{ cm}}^{\mathrm{d}a}  = (2,6\text{ cm})^2 = 6,76\text{ cm}^2$
> - $S_{\min} = \overbrace{2,5\text{ cm} }^{a} -  \overbrace{0,1 \text{ cm}}^{\mathrm{d}a} = (2,4\text{ cm}) ^2 = 5,76\text{ cm}^2$
>
>
>   $\Delta S \approx \frac{S_{\max} - S_{\min}}{2} = 0,50\text{ cm}^2$.
> - **Méthode différentielle** :
>   $\Delta S(a) \approx \mathrm{d}S(a) = 2 \, a  \, \mathrm{d} a = 2 \times 2,5 \times 0,1 \text{ cm}^2 = 0,50\text{ cm}^2$.
> - $\Delta S(a) = \overbrace{S(a+da)}^{S_{\max}} - S(a) = 0.51 \text{ cm}^2$
>
>
>
> **Résultat**  : $S = (6,3 \pm 0,5)\text{ cm}^2$. (Attention 2 CS)


**2.**

  **a)** Soit la position $z(t) = 1 - 2t^2$ (en cm) d'une particule sur un axe $Oz$ en fonction du temps $t$ (en s). Calculer la dérivée $\frac{\mathrm{d}z}{\mathrm{d}t} = \dot{z}$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\dot{z}(t) = \frac{\mathrm{d}z}{\mathrm{d}t} = -4t \quad (\text{en cm}\cdot\text{s}^{-1})$$


  **b)** En déduire l'expression de $\mathrm{d}z$ en fonction de $t$ et $\mathrm{d}t$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\mathrm{d}z = -4t \mathrm{d}t ~ (=  \dot{z}(t)\mathrm{d}t ) $$


  **c)** Exprimer la différence $z(t+\mathrm{d}t) - z(t)$ et comparer avec $\mathrm{d}z$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\Delta z  \equiv z(t+\mathrm{d}t) - z(t) = [1 - 2(t+\mathrm{d}t)^2] - [1 - 2t^2] = \overbrace{-4t\mathrm{d}t}^{\mathrm{d}z} - 2(\mathrm{d}t)^2$$
> D'où :
> $$\Delta z  - \mathrm{d}z =  - 2(\mathrm{d}t)^2$$


  **d)** Dans quelles conditions peut-on écrire $z(t+\mathrm{d}t) - z(t) = \mathrm{d}z$ ? Donner une interprétation de la différentielle $\mathrm{d}z$ et de la dérivée $\dot{z}$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> Cette égalité approchée est valable si $\mathrm{d}t \ll t$, rendant le terme $-2(\mathrm{d}t)^2$ négligeable devant $-4t\mathrm{d}t$.
>
>
> - $\dot{z}$ représente la **vitesse instantanée** de la particule.
> - $\mathrm{d}z$ représente le **déplacement élémentaire** sur un intervalle de temps très court $\mathrm{d}t$.


  **e)** Tracer la courbe représentant $z$ en fonction de $t$ puis représenter sur le graphique la différence $z(t+\mathrm{d}t)-z(t)$ et la différentielle $\mathrm{d}z$ à un instant $t$ fixé et pour une durée $\mathrm{d}t$ donnée.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> Sur le graphe $z(t)$, la différence $z(t+\mathrm{d}t) - z(t)$ mesure le déplacement vertical sur la courbe parabole, tandis que $\mathrm{d}z$ se mesure le long de la tangente au point d'abscisse $t$.
>
> <p style="text-align:center"><a href="/figures/td2_phv110_position_graph.svg" target="_blank" rel="noopener"><img src="/figures/td2_phv110_position_graph.svg" alt="" loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>


  **f)** Déterminer la dérivée seconde $\ddot{z}$ et interpréter.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\ddot{z}(t) = \frac{\mathrm{d}^2 z}{\mathrm{d}t^2} = -4 \quad (\text{en cm}\cdot\text{s}^{-2})$$
> $\ddot{z}$ représente **l'accélération** de la particule. Elle est constante et négative.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex1-derivation-de-fonctions-en-physique|Exercice 1 — Dérivation de fonctions en physique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex3-derivees-de-fonctions-composees|Exercice 3 — Dérivées de fonctions composées]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex4-differentielle-logarithmique|Exercice 4 — Différentielle logarithmique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex5-derivation-de-fonctions-en-physique-approfondissement|Exercice 5 — Dérivation de fonctions en physique (approfondissement)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex6-interpretation-de-la-differentielle-approfondissement-volume-pendule-approximations|Exercice 6 — Interprétation de la différentielle : approfondissement (volume, pendule, approximations)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex7-derivees-de-fonctions-composees-approfondissement-taux-lies|Exercice 7 — Dérivées de fonctions composées : approfondissement (taux liés)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex8-differentielle-logarithmique-approfondissement-incertitudes-en-situation-reelle|Exercice 8 — Différentielle logarithmique : approfondissement (incertitudes en situation réelle)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex9-combiner-les-incertitudes-somme-absolue-p-1-quadratique-p-2-puissance-p-et-cas-p-0|Exercice 9 — Combiner les incertitudes : somme absolue ($p=1$), quadratique ($p=2$), puissance $p$ et cas $p=0$]]

