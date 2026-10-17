---
title: "Exercice 5 — Dérivation de fonctions en physique (approfondissement)"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/index|⬅ Retour]] · <a href="/pdfs/td2_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td2_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 5. Dérivation de fonctions en physique (approfondissement) *(facultatif)*

Cet exercice prolonge l'exercice 1 avec des fonctions plus riches (produits, quotients, exponentielles, fonctions composées de plusieurs niveaux, puissances fractionnaires). Comme dans l'exercice 1, il faut d'abord identifier la **variable** et les **paramètres constants**, puis utiliser la notation différentielle. Pour les dérivées par rapport au temps, on utilise la notation pointée $\dot{x} = \frac{\mathrm{d}x}{\mathrm{d}t}$ et $\ddot{x} = \frac{\mathrm{d}^2x}{\mathrm{d}t^2}$.

Déterminer la dérivée de chacune des fonctions suivantes, puis vérifier l'homogénéité du résultat lorsque les grandeurs ont une dimension physique.

**1.**

  **a)** Déterminer la dérivée de $u(x) = x\ln x - x$.

> [!tip]- 💡 Coup de pouce
> **Produit**
>
> $\mathrm{d}(x\ln x) = \ln x\,\mathrm{d}x + x\,\mathrm{d}(\ln x)$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$
> \begin{array}{rcl}
> \mathrm{d}u & = & \ln x\,\mathrm{d}x + x\dfrac{\mathrm{d}x}{x} - \mathrm{d}x\\[2mm]
> & = & \ln x\,\mathrm{d}x.
> \end{array}
> $$
> Donc $\dfrac{\mathrm{d}u}{\mathrm{d}x} = \ln x$ : $u$ est une primitive de $\ln$.


  **b)** Oscillateur amorti : $x(t) = A\,e^{-\lambda t}\cos(\omega t + \varphi)$ avec $A$, $\lambda$, $\omega$, $\varphi$ constants. Déterminer $\dot{x}(t)$.

> [!tip]- 💡 Coup de pouce
> **Produit de deux composées**
>
> $x = A\,e^{-\lambda t}\cdot\cos(\omega t+\varphi)$ : produit de deux fonctions de $t$, chacune composée.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$
> \begin{array}{rcl}
> \mathrm{d}x & = & A\left[\cos(\omega t+\varphi)\,\mathrm{d}\!\left(e^{-\lambda t}\right) + e^{-\lambda t}\,\mathrm{d}\!\left(\cos(\omega t+\varphi)\right)\right]\\[2mm]
> & = & A\left[-\lambda\,e^{-\lambda t}\cos(\omega t+\varphi) - \omega\,e^{-\lambda t}\sin(\omega t+\varphi)\right]\mathrm{d}t.
> \end{array}
> $$
> Donc
> $$\dot{x}(t) = -A\,e^{-\lambda t}\left[\lambda\cos(\omega t+\varphi) + \omega\sin(\omega t+\varphi)\right].$$


  **c)** Charge d'un système du premier ordre : $v(t) = v_0\left(1 - e^{-t/\tau}\right)$ avec $v_0$ et $\tau$ constants. Déterminer $\dot{v}(t)$, puis $\dot{v}(0)$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\mathrm{d}v = -v_0\,\mathrm{d}\!\left(e^{-t/\tau}\right) = -v_0\left(-\frac{1}{\tau}\right)e^{-t/\tau}\mathrm{d}t,$$
> donc
> $$\dot{v}(t) = \frac{v_0}{\tau}\,e^{-t/\tau}, \qquad \dot{v}(0) = \frac{v_0}{\tau}.$$
> La pente à l'origine vaut $v_0/\tau$ : la tangente en $t=0$ coupe l'asymptote $v=v_0$ en $t=\tau$.


  **d)** Période d'un pendule simple : $T(L) = 2\pi\sqrt{\dfrac{L}{g}}$ avec $g$ constant. Déterminer $\dfrac{\mathrm{d}T}{\mathrm{d}L}$, l'exprimer avec $T$ et $L$, et vérifier l'homogénéité.

> [!tip]- 💡 Coup de pouce
> **Puissance fractionnaire**
>
> $T = 2\pi g^{-1/2}\,L^{1/2}$, donc $\mathrm{d}\!\left(L^{1/2}\right) = \frac{1}{2}L^{-1/2}\mathrm{d}L$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\mathrm{d}T = \frac{2\pi}{\sqrt{g}}\cdot\frac{\mathrm{d}L}{2\sqrt{L}} = \frac{\pi}{\sqrt{gL}}\,\mathrm{d}L,$$
> donc
> $$\frac{\mathrm{d}T}{\mathrm{d}L} = \frac{\pi}{\sqrt{gL}} = \frac{T}{2L}.$$
> **Homogénéité** : $\left[\dfrac{\mathrm{d}T}{\mathrm{d}L}\right] = \dfrac{\text{s}}{\text{m}}$ et $\left[\dfrac{1}{\sqrt{gL}}\right] = \dfrac{1}{\sqrt{\text{m}\cdot\text{s}^{-2}\cdot\text{m}}} = \dfrac{\text{s}}{\text{m}}$. Le résultat est homogène.


  **e)** Déterminer la dérivée de $\varphi(\theta) = \dfrac{\sin\theta}{1+\cos\theta}$ et la simplifier.

> [!tip]- 💡 Coup de pouce
> **Quotient**
>
> $\mathrm{d}\!\left(\dfrac{f}{g}\right) = \dfrac{g\,\mathrm{d}f - f\,\mathrm{d}g}{g^2}$ avec $f=\sin\theta$ et $g = 1+\cos\theta$. Utiliser $\sin^2\theta + \cos^2\theta = 1$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$
> \begin{array}{rcl}
> \dfrac{\mathrm{d}\varphi}{\mathrm{d}\theta} & = & \dfrac{(1+\cos\theta)\cos\theta - \sin\theta\,(-\sin\theta)}{(1+\cos\theta)^2}\\[3mm]
> & = & \dfrac{\cos\theta + \cos^2\theta + \sin^2\theta}{(1+\cos\theta)^2} ~=~ \dfrac{1+\cos\theta}{(1+\cos\theta)^2}\\[3mm]
> & = & \dfrac{1}{1+\cos\theta}.
> \end{array}
> $$
> Remarque : $\varphi(\theta) = \tan(\theta/2)$ et $\dfrac{1}{2\cos^2(\theta/2)} = \dfrac{1}{1+\cos\theta}$, ce qui confirme le résultat.


  **f)** Potentiel de Lennard-Jones : $U(r) = \varepsilon\left[\left(\dfrac{r_0}{r}\right)^{12} - 2\left(\dfrac{r_0}{r}\right)^{6}\right]$ avec $\varepsilon$ et $r_0$ constants. Déterminer $\dfrac{\mathrm{d}U}{\mathrm{d}r}$ puis la position $r_{\mathrm{eq}}$ où cette dérivée s'annule.

> [!tip]- 💡 Coup de pouce
> **Puissances de $r$**
>
> $\left(\dfrac{r_0}{r}\right)^{n} = r_0^{\,n}\,r^{-n}$ : seule $r$ est la variable.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$
> \begin{array}{rcl}
> \mathrm{d}U & = & \varepsilon\left[-12\,r_0^{12}\,r^{-13} + 12\,r_0^{6}\,r^{-7}\right]\mathrm{d}r,
> \end{array}
> $$
> donc
> $$\frac{\mathrm{d}U}{\mathrm{d}r} = \frac{12\,\varepsilon}{r_0}\left[\left(\frac{r_0}{r}\right)^{7} - \left(\frac{r_0}{r}\right)^{13}\right].$$
> Cette dérivée s'annule si $\left(\dfrac{r_0}{r}\right)^{7}\left[1 - \left(\dfrac{r_0}{r}\right)^{6}\right] = 0$, soit $r_{\mathrm{eq}} = r_0$. Pour $r<r_0$ la dérivée est négative, pour $r>r_0$ elle est positive : c'est un minimum de $U$.


  **g)** Déterminer la dérivée de $y(t) = \ln\!\left[\tan\!\left(\dfrac{\omega t}{2}\right)\right]$ pour $0 < \omega t < \pi$, avec $\omega$ constant.

> [!tip]- 💡 Coup de pouce
> **Trois niveaux**
>
> $u = \omega t/2$, puis $v = \tan u$, puis $y = \ln v$. On rappelle $\mathrm{d}(\tan u) = \dfrac{\mathrm{d}u}{\cos^2 u}$. Simplifier avec $\sin(2u) = 2\sin u\cos u$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$
> \begin{array}{rcl}
> \mathrm{d}y & = & \dfrac{\mathrm{d}(\tan u)}{\tan u} ~=~ \dfrac{1}{\tan u}\cdot\dfrac{\mathrm{d}u}{\cos^2 u} ~=~ \dfrac{\mathrm{d}u}{\sin u\cos u},\qquad \mathrm{d}u = \dfrac{\omega}{2}\mathrm{d}t.
> \end{array}
> $$
> Avec $\sin u\cos u = \frac{1}{2}\sin(2u) = \frac{1}{2}\sin(\omega t)$ :
> $$\dot{y}(t) = \frac{\omega/2}{\frac{1}{2}\sin(\omega t)} = \frac{\omega}{\sin(\omega t)}.$$


  **h)** Facteur de Lorentz : $\gamma(v) = \left(1 - \dfrac{v^2}{c^2}\right)^{-1/2}$ avec $c$ constant. Montrer que $\dfrac{\mathrm{d}\gamma}{\mathrm{d}v} = \dfrac{v}{c^2}\,\gamma^3$.

> [!tip]- 💡 Coup de pouce
> **Puissance d'une composée**
>
> $\mathrm{d}(u^n) = n\,u^{n-1}\mathrm{d}u$ avec $u = 1 - v^2/c^2$ et $n=-\tfrac{1}{2}$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$
> \begin{array}{rcl}
> \mathrm{d}\gamma & = & -\dfrac{1}{2}\left(1-\dfrac{v^2}{c^2}\right)^{-3/2}\cdot\left(-\dfrac{2v}{c^2}\right)\mathrm{d}v\\[3mm]
> & = & \dfrac{v}{c^2}\left(1-\dfrac{v^2}{c^2}\right)^{-3/2}\mathrm{d}v ~=~ \dfrac{v}{c^2}\,\gamma^3\,\mathrm{d}v.
> \end{array}
> $$
> Pour $v\ll c$, $\gamma\approx 1$ et $\dfrac{\mathrm{d}\gamma}{\mathrm{d}v}\approx\dfrac{v}{c^2}$ ; quand $v\to c$, la dérivée diverge.


**2.**

  **a)** On reprend $x(t) = A\,e^{-\lambda t}\cos(\omega t)$ (avec $\varphi = 0$). Calculer $\ddot{x}$, puis montrer que $\ddot{x} + 2\lambda\dot{x} + (\lambda^2 + \omega^2)\,x = 0$.

> [!tip]- 💡 Coup de pouce
> **Dériver deux fois**
>
> Utiliser $\dot{x} = -A\,e^{-\lambda t}\left[\lambda\cos(\omega t) + \omega\sin(\omega t)\right]$ (question 1b avec $\varphi = 0$), puis dériver à nouveau ce produit.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$
> \begin{array}{rcl}
> \ddot{x} & = & \lambda A\,e^{-\lambda t}\left[\lambda\cos\omega t + \omega\sin\omega t\right] - A\,e^{-\lambda t}\left[-\lambda\omega\sin\omega t + \omega^2\cos\omega t\right]\\[2mm]
> & = & A\,e^{-\lambda t}\left[(\lambda^2 - \omega^2)\cos\omega t + 2\lambda\omega\sin\omega t\right].
> \end{array}
> $$
> Alors
> $$
> \begin{array}{rcl}
> \ddot{x} + 2\lambda\dot{x} + (\lambda^2+\omega^2)x & = & A\,e^{-\lambda t}\Big[(\lambda^2-\omega^2)\cos\omega t + 2\lambda\omega\sin\omega t\\
> & & \qquad - 2\lambda^2\cos\omega t - 2\lambda\omega\sin\omega t + (\lambda^2+\omega^2)\cos\omega t\Big] ~=~ 0.
> \end{array}
> $$


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex1-derivation-de-fonctions-en-physique|Exercice 1 — Dérivation de fonctions en physique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex2-interpretation-de-la-differentielle-petite-variation-calcul-d-incertitude|Exercice 2 — Interprétation de la différentielle : petite variation $\&$ calcul d'incertitude]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex3-derivees-de-fonctions-composees|Exercice 3 — Dérivées de fonctions composées]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex4-differentielle-logarithmique|Exercice 4 — Différentielle logarithmique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex6-interpretation-de-la-differentielle-approfondissement-volume-pendule-approximations|Exercice 6 — Interprétation de la différentielle : approfondissement (volume, pendule, approximations)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex7-derivees-de-fonctions-composees-approfondissement-taux-lies|Exercice 7 — Dérivées de fonctions composées : approfondissement (taux liés)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex8-differentielle-logarithmique-approfondissement-incertitudes-en-situation-reelle|Exercice 8 — Différentielle logarithmique : approfondissement (incertitudes en situation réelle)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex9-combiner-les-incertitudes-somme-absolue-p-1-quadratique-p-2-puissance-p-et-cas-p-0|Exercice 9 — Combiner les incertitudes : somme absolue ($p=1$), quadratique ($p=2$), puissance $p$ et cas $p=0$]]

