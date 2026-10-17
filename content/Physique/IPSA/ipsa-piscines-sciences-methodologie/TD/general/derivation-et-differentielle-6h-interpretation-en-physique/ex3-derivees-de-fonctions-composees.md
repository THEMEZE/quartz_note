---
title: "Exercice 3 — Dérivées de fonctions composées"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/index|⬅ Retour]] · <a href="/pdfs/td2_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td2_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 3. Dérivées de fonctions composées

Objectif : savoir utiliser la règle de la chaîne pour décomposer puis calculer la dérivée de fonctions composées par rapport au temps $t$.
Rappel : dériver une fonction composée $f(u(x))$ par rapport à $x$ se fait simplement en décomposant la dérivée grâce à la règle de la chaîne : $\frac{\mathrm{d}f}{\mathrm{d}x} = \frac{\mathrm{d}f}{\mathrm{d}u} \cdot \frac{\mathrm{d}u}{\mathrm{d}x}$.

**1.**

  **a)** Soit $f(z) = -a z^3 + b z^2 - c z + 1$ avec $z = z(t)$ et les paramètres $a,b,c$ constants.
Calculer $\frac{\mathrm{d}f}{\mathrm{d}z}$ puis exprimer la dérivée $\frac{\mathrm{d}f}{\mathrm{d}t}$ en fonction de $z$, $\dot{z}$ et des paramètres constants.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\frac{\mathrm{d}f}{\mathrm{d}z} = -3a z^2 + 2b z - c$$
> $$\frac{\mathrm{d}f}{\mathrm{d}t} = \frac{\mathrm{d}f}{\mathrm{d}z} \cdot \frac{\mathrm{d}z}{\mathrm{d}t} = (-3a z^2 + 2b z - c) \cdot \dot{z}$$


  **b)** Étant donné l'expression de $z$ en fonction de $t$ : $z(t) = k t^2$ avec $k$ constant, en déduire l'expression de la dérivée $\frac{\mathrm{d}f}{\mathrm{d}t}$ en fonction de $t$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> Comme $z(t) = k t^2$, on a $\dot{z}(t) = 2kt$.
> $$\frac{\mathrm{d}f}{\mathrm{d}t} = \left(-3a (kt^2)^2 + 2b (kt^2) - c\right) \cdot (2kt) = -6a k^3 t^5 + 4b k^2 t^3 - 2ck t$$


**2.**

  **a)** Soit $x(\theta) = R \cos(\theta)$ avec $\theta = \theta(t)$ et le paramètre $R$ constant.
Calculer $\frac{\mathrm{d}x}{\mathrm{d}\theta}$ puis $\frac{\mathrm{d}x}{\mathrm{d}t}$ en fonction de $\theta$, $\dot{\theta}$ et des paramètres constants.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\frac{\mathrm{d}x}{\mathrm{d}\theta} = -R \sin(\theta)$$
> $$\frac{\mathrm{d}x}{\mathrm{d}t} = \frac{\mathrm{d}x}{\mathrm{d}\theta} \cdot \frac{\mathrm{d}\theta}{\mathrm{d}t} = -R \dot{\theta} \sin(\theta)$$


  **b)** Étant donné l'expression de $\theta$ en fonction de $t$ : $\theta(t) = \omega t^2 + 1$ avec $\omega$ constant, en déduire l'expression de $\frac{\mathrm{d}x}{\mathrm{d}t}$ en fonction de $t$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> On a $\dot{\theta}(t) = 2\omega t$.
> $$\frac{\mathrm{d}x}{\mathrm{d}t} = -R (2\omega t) \sin(\omega t^2 + 1) = -2 R \omega t \sin(\omega t^2 + 1)$$


**3.**

  **a)** (*) On considère un cercle dont le rayon $r$ varie dans le temps : $r = r(t)$. L'aire du cercle est $A(r) = \pi r^2$.
Déterminer la dérivée de $A$ par rapport à $r$, notée $\frac{\mathrm{d}A}{\mathrm{d}r}$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\frac{\mathrm{d}A}{\mathrm{d}r} = 2\pi r$$


  **b)** En déduire une relation entre $\mathrm{d}A$ et $\mathrm{d}r$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\mathrm{d}A = 2\pi r \mathrm{d}r$$


  **c)** Représenter la quantité $\mathrm{d}A$ sur un schéma.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> On définie $$\Delta A(r) = A(r + \mathrm{d}r) - A(r) = \pi (r + \mathrm{d}r)^2 - \pi r^2 = \overbrace{2\pi r \mathrm{d}r}^{\mathrm{d}A(r)} + \pi (\mathrm{d}r)^2$$ (cf fig \ref{figDisque}). On supose que $\mathrm{d}r \ll r$ de tel sorte que $(\mathrm{d}r)^2 \ll r \mathrm{d}r , r^2$. Soit  $$\Delta A(r) \underset{\mathrm{d}r \ll r}{=} \mathrm{d}A(r) + o((\mathrm{d}r)^2).$$ Donc si $\mathrm{d}r \ll r$ alors $$\Delta A(r) \approx \mathrm{d}A(r)$$ et  la quantité $\mathrm{d}A$ est la surface de la couronne circulaire d'épaisseur infinitésimale $\mathrm{d}r$ entourant le cercle de rayon $r$.
>
> <p style="text-align:center"><a href="/figures/td2_phv110_disque.svg" target="_blank" rel="noopener"><img src="/figures/td2_phv110_disque.svg" alt="" loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>


  **d)** En utilisant la règle de la chaîne, décomposer la dérivée $\frac{\mathrm{d}A}{\mathrm{d}t}$ correspondant au taux de variation de $A$ par rapport au temps $t$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\frac{\mathrm{d}A}{\mathrm{d}t} = \frac{\mathrm{d}A}{\mathrm{d}r} \cdot \frac{\mathrm{d}r}{\mathrm{d}t}$$


  **e)** Montrer que le taux de variation de l'aire par rapport au temps dépend du rayon $r$ du cercle et du taux $\frac{\mathrm{d}r}{\mathrm{d}t}$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\frac{\mathrm{d}A}{\mathrm{d}t} = 2\pi r \frac{\mathrm{d}r}{\mathrm{d}t}$$
> L'expression dépend explicitement du rayon $r$ et de la vitesse d'expansion du rayon $\frac{\mathrm{d}r}{\mathrm{d}t}$.


  **f)** On donne la valeur du taux de variation du rayon $\frac{\mathrm{d}r}{\mathrm{d}t} = 0,1\text{ cm}\cdot\text{s}^{-1}$.
Calculer (en précisant l'unité) le taux $\frac{\mathrm{d}A}{\mathrm{d}t}$ pour $r = 2\text{ cm}$ puis pour $r = 12\text{ cm}$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> * Pour $r = 2\text{ cm}$ :
>   $$\frac{\mathrm{d}A}{\mathrm{d}t} = 2\pi \times 2 \times 0,1 = 0,4\pi \approx 1,26\text{ cm}^2\cdot\text{s}^{-1}$$
> * Pour $r = 12\text{ cm}$ :
>   $$\frac{\mathrm{d}A}{\mathrm{d}t} = 2\pi \times 12 \times 0,1 = 2,4\pi \approx 7,54\text{ cm}^2\cdot\text{s}^{-1}$$


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex1-derivation-de-fonctions-en-physique|Exercice 1 — Dérivation de fonctions en physique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex2-interpretation-de-la-differentielle-petite-variation-calcul-d-incertitude|Exercice 2 — Interprétation de la différentielle : petite variation $\&$ calcul d'incertitude]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex4-differentielle-logarithmique|Exercice 4 — Différentielle logarithmique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex5-derivation-de-fonctions-en-physique-approfondissement|Exercice 5 — Dérivation de fonctions en physique (approfondissement)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex6-interpretation-de-la-differentielle-approfondissement-volume-pendule-approximations|Exercice 6 — Interprétation de la différentielle : approfondissement (volume, pendule, approximations)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex7-derivees-de-fonctions-composees-approfondissement-taux-lies|Exercice 7 — Dérivées de fonctions composées : approfondissement (taux liés)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex8-differentielle-logarithmique-approfondissement-incertitudes-en-situation-reelle|Exercice 8 — Différentielle logarithmique : approfondissement (incertitudes en situation réelle)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex9-combiner-les-incertitudes-somme-absolue-p-1-quadratique-p-2-puissance-p-et-cas-p-0|Exercice 9 — Combiner les incertitudes : somme absolue ($p=1$), quadratique ($p=2$), puissance $p$ et cas $p=0$]]

