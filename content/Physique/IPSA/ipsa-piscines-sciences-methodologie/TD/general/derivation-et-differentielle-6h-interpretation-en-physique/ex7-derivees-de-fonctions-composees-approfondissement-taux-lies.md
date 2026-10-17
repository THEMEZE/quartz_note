---
title: "Exercice 7 — Dérivées de fonctions composées : approfondissement (taux liés)"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/index|⬅ Retour]] · <a href="/pdfs/td2_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td2_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 7. Dérivées de fonctions composées : approfondissement (taux liés) *(facultatif)*

Cet exercice prolonge l'exercice 3. On utilise la règle de la chaîne avec plusieurs niveaux de composition, puis dans des problèmes de **taux liés** : plusieurs grandeurs dépendent du temps et sont reliées entre elles par une relation géométrique.

Règle de la chaîne à plusieurs niveaux : si $f = f(v)$, $v = v(u)$ et $u = u(t)$, alors
$$\frac{\mathrm{d}f}{\mathrm{d}t} = \frac{\mathrm{d}f}{\mathrm{d}v}\cdot\frac{\mathrm{d}v}{\mathrm{d}u}\cdot\frac{\mathrm{d}u}{\mathrm{d}t}.$$

**1.**

  **a)** Déterminer $\dot{f}(t)$ pour $f(t) = \ln\!\left[1 + \sin^2(\omega t)\right]$ avec $\omega$ constant. Décomposer la fonction en trois niveaux.

> [!tip]- 💡 Coup de pouce
> **Décomposition**
>
> $u = \omega t$, $s = \sin u$, $v = 1 + s^2$, $f = \ln v$. Simplifier ensuite avec $2\sin u\cos u = \sin 2u$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$
> \begin{array}{rcl}
> \dot{f} & = & \dfrac{\mathrm{d}f}{\mathrm{d}v}\cdot\dfrac{\mathrm{d}v}{\mathrm{d}s}\cdot\dfrac{\mathrm{d}s}{\mathrm{d}u}\cdot\dfrac{\mathrm{d}u}{\mathrm{d}t}\\[3mm]
> & = & \dfrac{1}{1+\sin^2(\omega t)}\cdot 2\sin(\omega t)\cdot\cos(\omega t)\cdot\omega\\[3mm]
> & = & \dfrac{\omega\,\sin(2\omega t)}{1+\sin^2(\omega t)}.
> \end{array}
> $$


  **b)** Un mobile se déplace à vitesse constante $b$ selon l'axe $Ox$ : $x(t) = bt$. Il est à distance $d(t) = \sqrt{a^2 + x(t)^2}$ d'un point fixe situé à la distance $a$ de l'axe. Calculer $\dot{d}(t)$, l'exprimer en fonction de $x$ et $d$, et étudier $\dot{d}$ pour $t = 0$ puis $t\to\infty$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $d = \sqrt{a^2 + b^2t^2}$, donc
> $$\mathrm{d}(d) = \frac{2b^2t\,\mathrm{d}t}{2\sqrt{a^2+b^2t^2}} \quad\Longrightarrow\quad \dot{d} = \frac{b^2t}{\sqrt{a^2+b^2t^2}} = b\,\frac{x}{d}.$$
> À $t=0$, $x = 0$ donc $\dot{d} = 0$ : le mobile passe au plus près du point. Quand $t\to\infty$, $x/d\to 1$ donc $\dot{d}\to b$ : la distance augmente presque à la vitesse du mobile. Le rapport $x/d$ est le cosinus de l'angle entre la direction du mobile et la direction du point.


**2.**

  **a)** (*) Un ballon sphérique est gonflé : son volume augmente au rythme $\dfrac{\mathrm{d}V}{\mathrm{d}t} = 20\ \text{cm}^3\cdot\text{s}^{-1}$. Avec $V = \dfrac{4}{3}\pi r^3$, établir l'expression de $\dfrac{\mathrm{d}r}{\mathrm{d}t}$ en fonction de $r$ et $\dfrac{\mathrm{d}V}{\mathrm{d}t}$, puis calculer sa valeur pour $r = 5\ \text{cm}$ et $r = 10\ \text{cm}$.

> [!tip]- 💡 Coup de pouce
> **Chaîne**
>
> $\dfrac{\mathrm{d}V}{\mathrm{d}t} = \dfrac{\mathrm{d}V}{\mathrm{d}r}\cdot\dfrac{\mathrm{d}r}{\mathrm{d}t}$ avec $\dfrac{\mathrm{d}V}{\mathrm{d}r} = 4\pi r^2$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\frac{\mathrm{d}V}{\mathrm{d}t} = 4\pi r^2\,\frac{\mathrm{d}r}{\mathrm{d}t} \quad\Longrightarrow\quad \frac{\mathrm{d}r}{\mathrm{d}t} = \frac{1}{4\pi r^2}\frac{\mathrm{d}V}{\mathrm{d}t}.$$
>
>
> - $r = 5\ \text{cm}$ : $\dfrac{\mathrm{d}r}{\mathrm{d}t} = \dfrac{20}{4\pi\times 25} = \dfrac{0{,}2}{\pi}\approx 0{,}064\ \text{cm}\cdot\text{s}^{-1}$.
> - $r = 10\ \text{cm}$ : $\dfrac{\mathrm{d}r}{\mathrm{d}t} = \dfrac{20}{4\pi\times 100}\approx 0{,}016\ \text{cm}\cdot\text{s}^{-1}$.
>
>
> À débit de gaz constant, le rayon croît de plus en plus lentement.


  **b)** La surface du ballon est $S = 4\pi r^2$. Exprimer $\dfrac{\mathrm{d}S}{\mathrm{d}t}$ en fonction de $r$ et de $\dfrac{\mathrm{d}V}{\mathrm{d}t}$ seulement, puis calculer sa valeur pour $r = 5\ \text{cm}$ et $r = 10\ \text{cm}$.

> [!tip]- 💡 Coup de pouce
> **Éliminer $\dot{r}$
> **
>
> $\dfrac{\mathrm{d}S}{\mathrm{d}t} = 8\pi r\,\dot{r}$, puis remplacer $\dot{r}$ par le résultat de la question précédente.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\frac{\mathrm{d}S}{\mathrm{d}t} = 8\pi r\,\dot{r} = 8\pi r\cdot\frac{1}{4\pi r^2}\frac{\mathrm{d}V}{\mathrm{d}t} = \frac{2}{r}\,\frac{\mathrm{d}V}{\mathrm{d}t}.$$
>
>
> - $r = 5\ \text{cm}$ : $\dfrac{\mathrm{d}S}{\mathrm{d}t} = \dfrac{2}{5}\times 20 = 8\ \text{cm}^2\cdot\text{s}^{-1}$.
> - $r = 10\ \text{cm}$ : $\dfrac{\mathrm{d}S}{\mathrm{d}t} = \dfrac{2}{10}\times 20 = 4\ \text{cm}^2\cdot\text{s}^{-1}$.
>
>
> **Homogénéité** : $\dfrac{1}{\text{cm}}\cdot\text{cm}^3\cdot\text{s}^{-1} = \text{cm}^2\cdot\text{s}^{-1}$. On a aussi $\dfrac{\mathrm{d}S}{\mathrm{d}V} = \dfrac{2}{r}$.


**3.**

  **a)** (*) Une échelle de longueur $L = 5{,}0\ \text{m}$ est appuyée contre un mur vertical. Le pied de l'échelle est à la distance $x(t)$ du mur et le haut à la hauteur $y(t)$. Écrire la relation entre $x$ et $y$, puis exprimer $\dot{y}$ en fonction de $x$, $y$ et $\dot{x}$.

> [!tip]- 💡 Coup de pouce
> **Relation géométrique**
>
> Théorème de Pythagore : $x^2 + y^2 = L^2$, avec $L$ constant. Dériver par rapport à $t$ : $\dfrac{\mathrm{d}(x^2)}{\mathrm{d}t} = 2x\dot{x}$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $x(t)^2 + y(t)^2 = L^2$. En dérivant par rapport à $t$ (avec $\dot{L}=0$) :
> $$2x\dot{x} + 2y\dot{y} = 0 \quad\Longrightarrow\quad \dot{y} = -\frac{x}{y}\,\dot{x}.$$
> On peut aussi écrire $y = \sqrt{L^2 - x^2}$, donc $\dfrac{\mathrm{d}y}{\mathrm{d}x} = -\dfrac{x}{\sqrt{L^2-x^2}} = -\dfrac{x}{y}$, puis $\dot{y} = \dfrac{\mathrm{d}y}{\mathrm{d}x}\dot{x}$ (règle de la chaîne).


  **b)** Le pied glisse à la vitesse constante $\dot{x} = 0{,}50\ \text{m}\cdot\text{s}^{-1}$. Calculer $\dot{y}$ lorsque $x = 3{,}0\ \text{m}$, puis lorsque $x = 4{,}0\ \text{m}$. Interpréter le signe et l'évolution. Que se passe-t-il quand $x\to L$ ?

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> - $x = 3{,}0\ \text{m}$ : $y = 4{,}0\ \text{m}$, $\dot{y} = -\dfrac{3}{4}\times 0{,}50 = -0{,}375\ \text{m}\cdot\text{s}^{-1}$.
> - $x = 4{,}0\ \text{m}$ : $y = 3{,}0\ \text{m}$, $\dot{y} = -\dfrac{4}{3}\times 0{,}50 \approx -0{,}67\ \text{m}\cdot\text{s}^{-1}$.
>
>
> $\dot{y}<0$ : le haut descend. Sa vitesse (en valeur absolue) augmente à mesure que le pied s'éloigne. Quand $x\to L$, $y\to 0$ et $|\dot{y}|\to\infty$ : le modèle ne peut pas rester valable (en pratique l'échelle décolle du mur avant).


**4.**

  **a)** Un pendule de longueur $L$ (constante) oscille avec l'angle $\theta(t) = \theta_0\cos(\omega t)$ ($\theta_0$, $\omega$ constants). L'abscisse de la masse est $x(t) = L\sin\theta(t)$. Calculer $\dot{x}(t)$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\dot{x} = L\cos\theta\cdot\dot{\theta}, \qquad \dot{\theta} = -\theta_0\omega\sin(\omega t),$$
> donc
> $$\dot{x}(t) = -L\,\theta_0\,\omega\,\sin(\omega t)\,\cos\!\big(\theta_0\cos(\omega t)\big).$$


  **b)** Simplifier $\dot{x}$ dans le cas des petites oscillations ($\theta_0\ll 1$ rad) et donner l'amplitude de la vitesse. Vérifier l'homogénéité.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> Si $\theta_0\ll 1$ alors $\cos\!\big(\theta_0\cos\omega t\big)\approx 1$ et
> $$\dot{x}(t) \approx -L\,\theta_0\,\omega\,\sin(\omega t).$$
> L'amplitude de la vitesse est $v_{\max} = L\theta_0\omega$.
> **Homogénéité** : $\theta_0$ est sans dimension et $[\omega] = \text{s}^{-1}$, donc $[L\theta_0\omega] = \text{m}\cdot\text{s}^{-1}$, une vitesse.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex1-derivation-de-fonctions-en-physique|Exercice 1 — Dérivation de fonctions en physique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex2-interpretation-de-la-differentielle-petite-variation-calcul-d-incertitude|Exercice 2 — Interprétation de la différentielle : petite variation $\&$ calcul d'incertitude]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex3-derivees-de-fonctions-composees|Exercice 3 — Dérivées de fonctions composées]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex4-differentielle-logarithmique|Exercice 4 — Différentielle logarithmique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex5-derivation-de-fonctions-en-physique-approfondissement|Exercice 5 — Dérivation de fonctions en physique (approfondissement)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex6-interpretation-de-la-differentielle-approfondissement-volume-pendule-approximations|Exercice 6 — Interprétation de la différentielle : approfondissement (volume, pendule, approximations)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex8-differentielle-logarithmique-approfondissement-incertitudes-en-situation-reelle|Exercice 8 — Différentielle logarithmique : approfondissement (incertitudes en situation réelle)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex9-combiner-les-incertitudes-somme-absolue-p-1-quadratique-p-2-puissance-p-et-cas-p-0|Exercice 9 — Combiner les incertitudes : somme absolue ($p=1$), quadratique ($p=2$), puissance $p$ et cas $p=0$]]

