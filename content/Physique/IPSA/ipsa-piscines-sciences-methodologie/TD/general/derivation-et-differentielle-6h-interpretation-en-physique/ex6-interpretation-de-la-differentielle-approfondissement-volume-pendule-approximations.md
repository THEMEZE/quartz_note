---
title: "Exercice 6 — Interprétation de la différentielle : approfondissement (volume, pendule, approximations)"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/index|⬅ Retour]] · <a href="/pdfs/td2_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td2_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 6. Interprétation de la différentielle : approfondissement (volume, pendule, approximations) *(facultatif)*

Cet exercice prolonge l'exercice 2. On y étudie la différence $\Delta f - \mathrm{d}f$ pour une fonction de degré 3 (le volume d'une sphère), on l'applique à un calcul d'incertitude (le pendule simple), puis on utilise $\mathrm{d}f$ pour estimer des valeurs numériques sans calculatrice.

**1.**

  **a)** Le volume d'une sphère de rayon $r$ est $V(r) = \dfrac{4}{3}\pi r^3$. Calculer $\dfrac{\mathrm{d}V}{\mathrm{d}r}$, vérifier l'homogénéité et reconnaître le résultat.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\frac{\mathrm{d}V}{\mathrm{d}r} = 4\pi r^2.$$
> **Homogénéité** : $[V] = L^3$, $[r] = L$, donc $\left[\dfrac{\mathrm{d}V}{\mathrm{d}r}\right] = L^2$, comme $[4\pi r^2] = L^2$.
> On reconnaît la surface $S$ de la sphère : $\dfrac{\mathrm{d}V}{\mathrm{d}r} = S(r)$.


  **b)** En déduire $\mathrm{d}V$ et interpréter géométriquement.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\mathrm{d}V = 4\pi r^2\,\mathrm{d}r.$$
> C'est le volume d'une coquille sphérique d'épaisseur $\mathrm{d}r$, approximée par « surface $\times$ épaisseur ».


  **c)** Exprimer exactement $\Delta V = V(r+\mathrm{d}r) - V(r)$ et l'écrire sous la forme $\mathrm{d}V + (\text{termes d'ordre supérieur})$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$
> \begin{array}{rcl}
> \Delta V & = & \dfrac{4}{3}\pi\left[(r+\mathrm{d}r)^3 - r^3\right]\\[2mm]
> & = & \dfrac{4}{3}\pi\left[3r^2\mathrm{d}r + 3r(\mathrm{d}r)^2 + (\mathrm{d}r)^3\right]\\[2mm]
> & = & \overbrace{4\pi r^2\,\mathrm{d}r}^{\mathrm{d}V} + 4\pi r\,(\mathrm{d}r)^2 + \dfrac{4}{3}\pi(\mathrm{d}r)^3.
> \end{array}
> $$


  **d)** Pour $r = 10\ \text{cm}$, calculer $\mathrm{d}V$, $\Delta V$ et l'erreur relative $\dfrac{\Delta V - \mathrm{d}V}{\Delta V}$ pour $\mathrm{d}r = 1\ \text{cm}$, $0{,}1\ \text{cm}$ et $0{,}01\ \text{cm}$. Que constate-t-on ?

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> - $\mathrm{d}r = 1\ \text{cm}$ : $\mathrm{d}V = 4\pi\cdot 100\cdot 1 \approx 1\,257\ \text{cm}^3$, $\Delta V = \frac{4\pi}{3}(1331 - 1000) \approx 1\,386\ \text{cm}^3$, erreur relative $\approx 9{,}4\ \%$.
> - $\mathrm{d}r = 0{,}1\ \text{cm}$ : $\mathrm{d}V \approx 125{,}7\ \text{cm}^3$, $\Delta V \approx 126{,}9\ \text{cm}^3$, erreur relative $\approx 1{,}0\ \%$.
> - $\mathrm{d}r = 0{,}01\ \text{cm}$ : $\mathrm{d}V \approx 12{,}57\ \text{cm}^3$, $\Delta V \approx 12{,}58\ \text{cm}^3$, erreur relative $\approx 0{,}10\ \%$.
>
>
> L'erreur relative est divisée par 10 quand $\mathrm{d}r$ est divisé par 10. En effet le terme dominant de l'erreur est $4\pi r(\mathrm{d}r)^2$, donc $\dfrac{4\pi r(\mathrm{d}r)^2}{4\pi r^2\,\mathrm{d}r} = \dfrac{\mathrm{d}r}{r}$.


  **e)** Vérifier que le terme $4\pi r(\mathrm{d}r)^2$ est égal à $\dfrac{1}{2}V''(r)(\mathrm{d}r)^2$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $V'(r) = 4\pi r^2$ donc $V''(r) = 8\pi r$, et $\dfrac{1}{2}V''(r)(\mathrm{d}r)^2 = 4\pi r(\mathrm{d}r)^2$.
> Le terme correctif principal est bien donné par la dérivée seconde. Le terme $\frac{4}{3}\pi(\mathrm{d}r)^3$ est d'ordre 3.


**2.**

  **a)** Pendule simple : $T(L) = 2\pi\sqrt{\dfrac{L}{g}}$, avec $g = 9{,}81\ \text{m}\cdot\text{s}^{-2}$ (supposé exact) et $L = 0{,}500 \pm 0{,}002\ \text{m}$. Calculer $T$ puis $\dfrac{\mathrm{d}T}{\mathrm{d}L}$ à $L = 0{,}500\ \text{m}$.

> [!tip]- 💡 Coup de pouce
> **Rappel**
>
> D'après l'exercice 5, $\dfrac{\mathrm{d}T}{\mathrm{d}L} = \dfrac{\pi}{\sqrt{gL}} = \dfrac{T}{2L}$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $T = 2\pi\sqrt{\dfrac{0{,}500}{9{,}81}} \approx 1{,}419\ \text{s}$.
> $$\frac{\mathrm{d}T}{\mathrm{d}L} = \frac{T}{2L} = \frac{1{,}419}{2\times 0{,}500} \approx 1{,}419\ \text{s}\cdot\text{m}^{-1}.$$


  **b)** En déduire l'incertitude $\Delta T$ par la méthode différentielle, puis vérifier avec les valeurs extrêmes de $L$. Écrire le résultat avec le bon nombre de chiffres significatifs.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> **Méthode différentielle** : $\Delta T \approx \left|\dfrac{\mathrm{d}T}{\mathrm{d}L}\right|\Delta L = 1{,}419\times 0{,}002 \approx 0{,}003\ \text{s}$.
>
> **Extrema** : $L_{\max} = 0{,}502\ \text{m} \Rightarrow T_{\max} \approx 1{,}4214\ \text{s}$ ; $L_{\min} = 0{,}498\ \text{m} \Rightarrow T_{\min} \approx 1{,}4157\ \text{s}$. La demi-différence vaut $\approx 0{,}003\ \text{s}$, en accord.
>
> **Résultat** : $T = (1{,}419 \pm 0{,}003)\ \text{s}$.


  **c)** Comparer l'incertitude relative $\dfrac{\Delta T}{T}$ à $\dfrac{\Delta L}{L}$. Que dire du rapport ?

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $\dfrac{\Delta T}{T} = \dfrac{1}{2}\dfrac{\Delta L}{L} = \dfrac{1}{2}\times 0{,}4\ \% = 0{,}2\ \%$.
> Le rapport vaut $1/2$, qui est l'exposant de $L$ dans $T\propto L^{1/2}$. Les exposants se lisent directement sur les incertitudes relatives (voir exercice 8).


**3.**

  **a)** Sans calculatrice, estimer à l'aide de la différentielle, puis comparer avec la valeur exacte (donnée entre parenthèses) :



1. $\sqrt{4{,}04}$ \quad ($\approx 2{,}009975$)
2. $\dfrac{1}{1{,}02}$ \quad ($\approx 0{,}980392$)
3. $\sin(31^\circ)$ \quad ($\approx 0{,}515038$)

> [!tip]- 💡 Coup de pouce
> **Point de départ**
>
> Choisir un point $x_0$ proche où la fonction est connue : $x_0 = 4$, $x_0 = 1$, $x_0 = 30^\circ = \pi/6$, puis $f(x_0+\mathrm{d}x) \approx f(x_0) + f'(x_0)\,\mathrm{d}x$. Pour (iii), convertir $1^\circ$ en radians.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> 1. $f = \sqrt{x}$, $f' = \dfrac{1}{2\sqrt{x}}$, $x_0 = 4$, $\mathrm{d}x = 0{,}04$ : $\sqrt{4{,}04}\approx 2 + \dfrac{0{,}04}{4} = 2{,}01$.
> 2. $f = \dfrac{1}{x}$, $f' = -\dfrac{1}{x^2}$, $x_0 = 1$, $\mathrm{d}x = 0{,}02$ : $\dfrac{1}{1{,}02}\approx 1 - 0{,}02 = 0{,}98$.
> 3. $f = \sin$, $f' = \cos$, $x_0 = \dfrac{\pi}{6}$, $\mathrm{d}x = \dfrac{\pi}{180}\approx 0{,}01745\ \text{rad}$ : $\sin 31^\circ \approx \dfrac{1}{2} + \dfrac{\sqrt{3}}{2}\times 0{,}01745 \approx 0{,}5151$.
>
>
> Les erreurs sont respectivement $\approx 2{,}5\times 10^{-5}$, $4\times 10^{-4}$ et $8\times 10^{-5}$.


**4.**

  **a)** (*) Dans les trois estimations précédentes, dire si l'approximation par la différentielle est une valeur par excès ou par défaut. Relier la réponse au signe de $f''$.

> [!tip]- 💡 Coup de pouce
> **Point de cours**
>
> $\Delta f - \mathrm{d}f \approx \dfrac{1}{2}f''(x_0)(\mathrm{d}x)^2$ : le signe de l'erreur est celui de $f''$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> - $f = \sqrt{x}$ : $f'' = -\dfrac{1}{4}x^{-3/2} < 0$. Fonction concave, $\Delta f < \mathrm{d}f$ : l'estimation $2{,}01$ est **par excès** (exact $2{,}009975$).
> - $f = \dfrac{1}{x}$ : $f'' = \dfrac{2}{x^3} > 0$. Fonction convexe, $\Delta f > \mathrm{d}f$ : l'estimation $0{,}98$ est **par défaut** (exact $0{,}980392$).
> - $f = \sin$ près de $\pi/6$ : $f'' = -\sin < 0$. Fonction concave, l'estimation $0{,}5151$ est **par excès** (exact $0{,}515038$).
>
>
> Géométriquement, une courbe concave est en dessous de sa tangente, une courbe convexe est au-dessus.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex1-derivation-de-fonctions-en-physique|Exercice 1 — Dérivation de fonctions en physique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex2-interpretation-de-la-differentielle-petite-variation-calcul-d-incertitude|Exercice 2 — Interprétation de la différentielle : petite variation $\&$ calcul d'incertitude]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex3-derivees-de-fonctions-composees|Exercice 3 — Dérivées de fonctions composées]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex4-differentielle-logarithmique|Exercice 4 — Différentielle logarithmique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex5-derivation-de-fonctions-en-physique-approfondissement|Exercice 5 — Dérivation de fonctions en physique (approfondissement)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex7-derivees-de-fonctions-composees-approfondissement-taux-lies|Exercice 7 — Dérivées de fonctions composées : approfondissement (taux liés)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex8-differentielle-logarithmique-approfondissement-incertitudes-en-situation-reelle|Exercice 8 — Différentielle logarithmique : approfondissement (incertitudes en situation réelle)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex9-combiner-les-incertitudes-somme-absolue-p-1-quadratique-p-2-puissance-p-et-cas-p-0|Exercice 9 — Combiner les incertitudes : somme absolue ($p=1$), quadratique ($p=2$), puissance $p$ et cas $p=0$]]

