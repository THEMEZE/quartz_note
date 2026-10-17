---
title: "Exercice 8 — Différentielle logarithmique : approfondissement (incertitudes en situation réelle)"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/index|⬅ Retour]] · <a href="/pdfs/td2_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td2_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 8. Différentielle logarithmique : approfondissement (incertitudes en situation réelle) *(facultatif)*

Cet exercice prolonge l'exercice 4 avec des formules réelles de physique et des données numériques. On applique la méthode de la différentielle logarithmique pour obtenir l'incertitude **maximale** (somme des contributions en valeur absolue), on identifie la mesure qui domine l'incertitude, et on rencontre un cas où le logarithme ne suffit pas directement (formule des lentilles).

Pour une grandeur $f = k\,x^\alpha y^\beta z^\gamma$ ($k$ constant) :
$$\frac{\Delta f}{f} = |\alpha|\frac{\Delta x}{x} + |\beta|\frac{\Delta y}{y} + |\gamma|\frac{\Delta z}{z}.$$

**1.**

  **a)** Période d'un pendule simple : $T = 2\pi\sqrt{\dfrac{L}{g}}$, avec $L = 1{,}000 \pm 0{,}005\ \text{m}$ et $g = 9{,}81 \pm 0{,}03\ \text{m}\cdot\text{s}^{-2}$. Établir $\dfrac{\Delta T}{T}$ par la méthode logarithmique, calculer $T$ et $\Delta T$, et écrire le résultat.

> [!tip]- 💡 Coup de pouce
> **Exposants**
>
> $T = 2\pi\,L^{1/2}\,g^{-1/2}$ : $2\pi$ est une constante, $\mathrm{d}(2\pi)=0$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $\ln T = \ln 2\pi + \dfrac{1}{2}\ln L - \dfrac{1}{2}\ln g$, donc
> $$\frac{\mathrm{d}T}{T} = \frac{1}{2}\frac{\mathrm{d}L}{L} - \frac{1}{2}\frac{\mathrm{d}g}{g} \quad\Longrightarrow\quad \frac{\Delta T}{T} = \frac{1}{2}\frac{\Delta L}{L} + \frac{1}{2}\frac{\Delta g}{g}.$$
> Numériquement : $\dfrac{\Delta L}{L} = 0{,}50\ \%$, $\dfrac{\Delta g}{g} = \dfrac{0{,}03}{9{,}81}\approx 0{,}31\ \%$, donc $\dfrac{\Delta T}{T}\approx 0{,}25 + 0{,}15 = 0{,}40\ \%$.
> $T = 2\pi\sqrt{1{,}000/9{,}81}\approx 2{,}006\ \text{s}$ et $\Delta T \approx 2{,}006\times 0{,}0040 \approx 0{,}008\ \text{s}$.
>
> **Résultat** : $T = (2{,}006 \pm 0{,}008)\ \text{s}$.


**2.**

  **a)** Résistance d'un fil cylindrique : $R = \dfrac{\rho L}{S}$ avec $S = \dfrac{\pi d^2}{4}$. Exprimer $R$ en fonction de $\rho$, $L$ et $d$, puis établir $\dfrac{\Delta R}{R}$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $R = \dfrac{4\rho L}{\pi d^2}$, donc $\ln R = \ln\dfrac{4}{\pi} + \ln\rho + \ln L - 2\ln d$ et
> $$\frac{\mathrm{d}R}{R} = \frac{\mathrm{d}\rho}{\rho} + \frac{\mathrm{d}L}{L} - 2\frac{\mathrm{d}d}{d} \quad\Longrightarrow\quad \frac{\Delta R}{R} = \frac{\Delta\rho}{\rho} + \frac{\Delta L}{L} + 2\frac{\Delta d}{d}.$$


  **b)** Données : $\rho = (1{,}7 \pm 0{,}034)\times 10^{-8}\ \Omega\cdot\text{m}$, $L = 2{,}00 \pm 0{,}01\ \text{m}$, $d = 0{,}50 \pm 0{,}01\ \text{mm}$. Calculer $R$, $\Delta R$, écrire le résultat et déterminer quelle mesure contribue le plus à l'incertitude.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $\dfrac{\Delta\rho}{\rho} = 2\ \%$, $\dfrac{\Delta L}{L} = 0{,}5\ \%$, $\dfrac{\Delta d}{d} = 2\ \%$.
> $$\frac{\Delta R}{R} = 2 + 0{,}5 + 2\times 2 = 6{,}5\ \%.$$
> $R = \dfrac{4\times 1{,}7\times 10^{-8}\times 2{,}00}{\pi\,(0{,}50\times 10^{-3})^2}\approx 0{,}173\ \Omega$ et $\Delta R \approx 0{,}173\times 0{,}065\approx 0{,}011\ \Omega$.
>
> **Résultat** : $R = (0{,}173 \pm 0{,}011)\ \Omega$.
>
> Contributions : $\rho$ : 2 points sur 6,5 ($\approx 31\ \%$), $L$ : 0,5 ($\approx 8\ \%$), $d$ : 4 ($\approx 62\ \%$). Le diamètre domine, car il intervient au carré et sa précision relative est faible. Améliorer sa mesure est la priorité.


**3.**

  **a)** Énergie cinétique : $E_c = \dfrac{1}{2}mv^2$, avec $m = 2{,}00 \pm 0{,}02\ \text{kg}$ et $v = 3{,}0 \pm 0{,}1\ \text{m}\cdot\text{s}^{-1}$. Calculer $E_c$ et $\Delta E_c$, et écrire le résultat.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $\dfrac{\Delta E_c}{E_c} = \dfrac{\Delta m}{m} + 2\dfrac{\Delta v}{v} = 1{,}0\ \% + 2\times 3{,}3\ \% \approx 7{,}7\ \%$.
> $E_c = \dfrac{1}{2}\times 2{,}00\times 3{,}0^2 = 9{,}0\ \text{J}$ et $\Delta E_c \approx 9{,}0\times 0{,}077\approx 0{,}7\ \text{J}$.
>
> **Résultat** : $E_c = (9{,}0 \pm 0{,}7)\ \text{J}$. La vitesse est responsable de $\approx 87\ \%$ de l'incertitude relative.


**4.**

  **a)** (*) Lentille mince : $\dfrac{1}{f} = \dfrac{1}{p} + \dfrac{1}{p'}$, soit $f = \dfrac{pp'}{p + p'}$. Établir $\dfrac{\mathrm{d}f}{f}$ par la méthode logarithmique et regrouper les termes en $\mathrm{d}p$ et $\mathrm{d}p'$.

> [!tip]- 💡 Coup de pouce
> **Logarithme d'une somme**
>
> $\ln f = \ln p + \ln p' - \ln(p+p')$ et $\mathrm{d}\ln(p+p') = \dfrac{\mathrm{d}p + \mathrm{d}p'}{p+p'}$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$
> \begin{array}{rcl}
> \dfrac{\mathrm{d}f}{f} & = & \dfrac{\mathrm{d}p}{p} + \dfrac{\mathrm{d}p'}{p'} - \dfrac{\mathrm{d}p + \mathrm{d}p'}{p+p'}\\[3mm]
> & = & \left(\dfrac{1}{p} - \dfrac{1}{p+p'}\right)\mathrm{d}p + \left(\dfrac{1}{p'} - \dfrac{1}{p+p'}\right)\mathrm{d}p'\\[3mm]
> & = & \dfrac{p'}{p\,(p+p')}\,\mathrm{d}p + \dfrac{p}{p'\,(p+p')}\,\mathrm{d}p'.
> \end{array}
> $$
> Donc $\mathrm{d}f = \dfrac{p'^2}{(p+p')^2}\,\mathrm{d}p + \dfrac{p^2}{(p+p')^2}\,\mathrm{d}p'$ (on retrouve $\dfrac{\mathrm{d}f}{f^2} = \dfrac{\mathrm{d}p}{p^2} + \dfrac{\mathrm{d}p'}{p'^2}$ en différentiant directement $\frac{1}{f}$).


  **b)** (*) Pour $p = 30{,}0 \pm 0{,}5\ \text{cm}$ et $p' = 60{,}0 \pm 0{,}5\ \text{cm}$, calculer $f$ et $\Delta f$. Comparer avec le résultat qu'on obtiendrait en mettant en valeur absolue les termes **avant** de regrouper :
$\dfrac{\Delta f}{f} \overset{?}{=} \dfrac{\Delta p}{p} + \dfrac{\Delta p'}{p'} + \dfrac{\Delta p + \Delta p'}{p+p'}$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $f = \dfrac{30\times 60}{90} = 20{,}0\ \text{cm}$. Les coefficients de la question précédente sont tous positifs :
> $$\Delta f = \frac{p'^2}{(p+p')^2}\Delta p + \frac{p^2}{(p+p')^2}\Delta p' = \frac{4}{9}\times 0{,}5 + \frac{1}{9}\times 0{,}5 \approx 0{,}28\ \text{cm}.$$
> **Résultat** : $f = (20{,}0 \pm 0{,}3)\ \text{cm}$.
>
> Avec valeur absolue avant regroupement :
> $$\Delta f \overset{?}{=} 20\left(\frac{0{,}5}{30} + \frac{0{,}5}{60} + \frac{1{,}0}{90}\right) \approx 0{,}72\ \text{cm},$$
> soit plus de deux fois trop. Le terme $-\dfrac{\mathrm{d}p+\mathrm{d}p'}{p+p'}$ compense partiellement les deux autres, et cette compensation disparaît si on met les termes en valeur absolue trop tôt.


**5.**

  **a)** Soit $f = \dfrac{x^3\,z}{y^2}$ avec $\dfrac{\Delta x}{x} = 1\ \%$, $\dfrac{\Delta y}{y} = 2\ \%$ et $\dfrac{\Delta z}{z} = 4\ \%$. Calculer $\dfrac{\Delta f}{f}$, identifier la contribution dominante, et déterminer la valeur maximale de $\dfrac{\Delta z}{z}$ qui permet d'avoir $\dfrac{\Delta f}{f}\le 10\ \%$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $\dfrac{\Delta f}{f} = 3\dfrac{\Delta x}{x} + 2\dfrac{\Delta y}{y} + \dfrac{\Delta z}{z} = 3 + 4 + 4 = 11\ \%$.
> Contributions : $x$ : 3 (27 %), $y$ : 4 (36 %), $z$ : 4 (36 %). $y$ et $z$ dominent à égalité.
> Pour $\dfrac{\Delta f}{f}\le 10\ \%$ avec $x$ et $y$ inchangés : $3 + 4 + \dfrac{\Delta z}{z}\le 10$, donc $\dfrac{\Delta z}{z}\le 3\ \%$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex1-derivation-de-fonctions-en-physique|Exercice 1 — Dérivation de fonctions en physique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex2-interpretation-de-la-differentielle-petite-variation-calcul-d-incertitude|Exercice 2 — Interprétation de la différentielle : petite variation $\&$ calcul d'incertitude]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex3-derivees-de-fonctions-composees|Exercice 3 — Dérivées de fonctions composées]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex4-differentielle-logarithmique|Exercice 4 — Différentielle logarithmique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex5-derivation-de-fonctions-en-physique-approfondissement|Exercice 5 — Dérivation de fonctions en physique (approfondissement)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex6-interpretation-de-la-differentielle-approfondissement-volume-pendule-approximations|Exercice 6 — Interprétation de la différentielle : approfondissement (volume, pendule, approximations)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex7-derivees-de-fonctions-composees-approfondissement-taux-lies|Exercice 7 — Dérivées de fonctions composées : approfondissement (taux liés)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex9-combiner-les-incertitudes-somme-absolue-p-1-quadratique-p-2-puissance-p-et-cas-p-0|Exercice 9 — Combiner les incertitudes : somme absolue ($p=1$), quadratique ($p=2$), puissance $p$ et cas $p=0$]]

