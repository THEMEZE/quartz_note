---
title: "Exercice 9 — Combiner les incertitudes : somme absolue ($p=1$), quadratique ($p=2$), puissance $p$ et cas $p=0$"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/index|⬅ Retour]] · <a href="/pdfs/td2_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td2_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 9. Combiner les incertitudes : somme absolue ($p=1$), quadratique ($p=2$), puissance $p$ et cas $p=0$ *(facultatif)*

Pour une grandeur $f(x_1,\dots,x_n)$, la différentielle
$$\mathrm{d}f = \sum_{i=1}^{n}\frac{\partial f}{\partial x_i}\,\mathrm{d}x_i$$
donne des **contributions** $c_i = \left|\dfrac{\partial f}{\partial x_i}\right|\Delta x_i$ (une par grandeur mesurée). Il existe plusieurs façons de les combiner pour obtenir l'incertitude $\Delta f$. Cet exercice les regroupe dans une même famille : la combinaison de puissance $p$,
$$\boxed{\;\Delta_p f = \left(\sum_{i=1}^{n} c_i^{\,p}\right)^{1/p}\;}\qquad (p>0).$$



- $p=1$ : somme **absolue** (incertitude maximale, exercices 4 et 8) : $\Delta_1 f = \sum_i c_i$.
- $p=2$ : somme **quadratique** (incertitudes indépendantes et aléatoires) : $\Delta_2 f = \sqrt{\sum_i c_i^2}$.
- $p$ quelconque et limites $p\to\infty$, $p\to 0$ : à étudier.



Attention : ce $p$ est l'exposant de la combinaison. Il n'a rien à voir avec les exposants $\alpha,\beta,\gamma$ de la formule $f = x^\alpha y^\beta z^\gamma$.

**1.**

  **a)** Soit $f = k\,x^\alpha y^\beta z^\gamma$ avec $k$ constant. Écrire $\dfrac{\Delta_p f}{f}$ en fonction des incertitudes relatives, puis donner explicitement les cas $p=1$ et $p=2$. Retrouver la formule de l'exercice 4.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $\dfrac{\mathrm{d}f}{f} = \alpha\dfrac{\mathrm{d}x}{x} + \beta\dfrac{\mathrm{d}y}{y} + \gamma\dfrac{\mathrm{d}z}{z}$, donc les contributions relatives sont $r_x = |\alpha|\dfrac{\Delta x}{x}$, $r_y = |\beta|\dfrac{\Delta y}{y}$, $r_z = |\gamma|\dfrac{\Delta z}{z}$ et
> $$\frac{\Delta_p f}{f} = \left(r_x^p + r_y^p + r_z^p\right)^{1/p}.$$
>
>
> - $p=1$ : $\dfrac{\Delta_1 f}{f} = |\alpha|\dfrac{\Delta x}{x} + |\beta|\dfrac{\Delta y}{y} + |\gamma|\dfrac{\Delta z}{z}$ : c'est la formule de l'incertitude maximale de l'exercice 4.
> - $p=2$ : $\left(\dfrac{\Delta_2 f}{f}\right)^2 = \alpha^2\left(\dfrac{\Delta x}{x}\right)^2 + \beta^2\left(\dfrac{\Delta y}{y}\right)^2 + \gamma^2\left(\dfrac{\Delta z}{z}\right)^2$ : c'est la combinaison quadratique.


  **b)** Cas d'une somme : $L = L_1 + L_2$ avec $L_1 = 12{,}0\pm 0{,}2\ \text{cm}$ et $L_2 = 8{,}0\pm 0{,}1\ \text{cm}$. Exprimer $c_1$, $c_2$, puis calculer $\Delta_1 L$ et $\Delta_2 L$. Écrire les deux résultats.

> [!tip]- 💡 Coup de pouce
> **Attention**
>
> Ici $\dfrac{\partial L}{\partial L_1} = \dfrac{\partial L}{\partial L_2} = 1$ : ce sont les incertitudes **absolues** qui se combinent.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $c_1 = \Delta L_1 = 0{,}2\ \text{cm}$ et $c_2 = \Delta L_2 = 0{,}1\ \text{cm}$.
>
>
> - $\Delta_1 L = 0{,}2 + 0{,}1 = 0{,}3\ \text{cm}$ : $L = (20{,}0\pm 0{,}3)\ \text{cm}$.
> - $\Delta_2 L = \sqrt{0{,}2^2 + 0{,}1^2} = \sqrt{0{,}05}\approx 0{,}22\ \text{cm}$ : $L = (20{,}0\pm 0{,}2)\ \text{cm}$.
>
>
> Le résultat $p=2$ est plus petit : il suppose que les erreurs sur $L_1$ et $L_2$ ne sont pas toutes deux à leur valeur extrême, dans le même sens.


**2.**

  **a)** Soit $f = \dfrac{x^2 y}{z}$ avec $x = 2{,}00\pm 0{,}02$, $y = 5{,}0\pm 0{,}1$, $z = 4{,}0\pm 0{,}2$ (mêmes unités arbitraires). Calculer $f$, les contributions relatives $r_x$, $r_y$, $r_z$, puis $\dfrac{\Delta_p f}{f}$ et $\Delta_p f$ pour $p = 1,\,2,\,3,\,4$ et $p\to\infty$.

> [!tip]- 💡 Coup de pouce
> **Contributions**
>
> $\dfrac{\Delta x}{x} = 1\ \%$, $\dfrac{\Delta y}{y} = 2\ \%$, $\dfrac{\Delta z}{z} = 5\ \%$. Ne pas oublier l'exposant $2$ sur $x$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $f = \dfrac{2{,}00^2\times 5{,}0}{4{,}0} = 5{,}0$.
> $r_x = 2\times 1 = 2\ \%$, $r_y = 1\times 2 = 2\ \%$, $r_z = 1\times 5 = 5\ \%$.
>
> $$
> \begin{array}{c|c|c}
> p & \Delta_p f / f & \Delta_p f\\ \hline
> 1 & 2+2+5 = 9{,}00\ \% & 0{,}45\\
> 2 & \sqrt{4+4+25} \approx 5{,}74\ \% & 0{,}29\\
> 3 & (8+8+125)^{1/3} \approx 5{,}20\ \% & 0{,}26\\
> 4 & (16+16+625)^{1/4} \approx 5{,}06\ \% & 0{,}25\\
> \infty & \max = 5{,}00\ \% & 0{,}25
> \end{array}
> $$
> Le résultat décroît quand $p$ augmente et tend vers la plus grande contribution ($z$ ici).


**3.**

  **a)** Montrer que $\Delta_2 f\le\Delta_1 f$, avec égalité si et seulement si une seule contribution est non nulle.

> [!tip]- 💡 Coup de pouce
> **Élever au carré**
>
> Développer $\left(\sum_i c_i\right)^2$ et comparer à $\sum_i c_i^2$. Les $c_i$ sont positifs ou nuls.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $$\left(\sum_i c_i\right)^2 = \sum_i c_i^2 + 2\sum_{i<j}c_ic_j \ge \sum_i c_i^2.$$
> Comme tout est positif, on peut prendre la racine : $\Delta_1 f\ge\Delta_2 f$. L'égalité impose $c_ic_j = 0$ pour tout $i\ne j$, donc une seule contribution non nulle.


  **b)** Soit $c_{\max} = \max_i c_i$. Montrer que $c_{\max}\le\Delta_p f\le n^{1/p}\,c_{\max}$ et en déduire la limite de $\Delta_p f$ quand $p\to\infty$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $c_{\max}^p\le\sum_i c_i^p\le n\,c_{\max}^p$. En prenant la puissance $1/p$ :
> $$c_{\max}\le\Delta_p f\le n^{1/p}\,c_{\max}.$$
> Quand $p\to\infty$, $n^{1/p}\to 1$, donc $\Delta_p f\to c_{\max}$ : on retrouve $\Delta_\infty f = \max_i c_i$.


  **c)** Interpréter la chaîne $\Delta_\infty f\le\Delta_2 f\le\Delta_1 f$ en termes d'hypothèses sur les erreurs de mesure. Dans quelle situation la prudence impose $p=1$ ? Dans quelle situation $p=2$ est-il justifié ?

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> - $p=1$ correspond au **pire cas** : toutes les erreurs valent leur maximum et agissent dans le sens qui s'additionne. C'est la bonne règle pour une borne garantie (tolérance, sécurité), ou quand on ne sait rien sur les erreurs.
> - $p=2$ correspond à des erreurs **indépendantes**, à distribution symétrique, chaque $\Delta x_i$ étant une incertitude-type. Il est peu probable que toutes les erreurs se cumulent dans le même sens, d'où $\Delta_2<\Delta_1$.
> - $p=\infty$ ne tient compte que de la contribution dominante : il ne peut servir que de borne inférieure. Aucune combinaison raisonnable ne peut donner moins que la plus grande contribution.


**4.**

  **a)** On suppose $n$ contributions égales : $c_1=\dots=c_n=c$. Exprimer $\Delta_p f$ en fonction de $n$, $p$ et $c$. Pour quelle valeur de $n$ a-t-on $\Delta_1 f = 3\,\Delta_2 f$ ?

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $\Delta_p f = (n\,c^p)^{1/p} = n^{1/p}\,c$.
> $\dfrac{\Delta_1 f}{\Delta_2 f} = \dfrac{n}{\sqrt{n}} = \sqrt{n}$, donc $\Delta_1 f = 3\,\Delta_2 f$ si $\sqrt{n} = 3$, soit $n = 9$.
> Plus il y a de mesures indépendantes de poids comparables, plus la somme absolue surestime l'incertitude par rapport à la quadratique.


  **b)** Dans l'exercice de la question 2, quelle proportion de $\Delta_2 f$ vient de $z$ seul ? Que dire de l'intérêt d'améliorer la mesure de $x$ ?

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $\dfrac{r_z^2}{r_x^2+r_y^2+r_z^2} = \dfrac{25}{33}\approx 76\ \%$ de $\left(\dfrac{\Delta_2 f}{f}\right)^2$ vient de $z$.
> Diviser $\Delta x/x$ par 2 (donc $r_x$ de 2 % à 1 %) donne $\sqrt{1+4+25}\approx 5{,}48\ \%$ au lieu de $5{,}74\ \%$ : gain d'environ $5\ \%$ seulement. Pour progresser, il faut d'abord améliorer la mesure de $z$.


**5.**

  **a)** (*) Cas $p=0$. Pour $p\to 0^+$ et $n\ge 2$ contributions strictement positives, étudier la limite de $\Delta_p f = \left(\sum_i c_i^p\right)^{1/p}$.

> [!tip]- 💡 Coup de pouce
> **Cas limite**
>
> Quand $p\to 0$, $c_i^p\to 1$ pour chaque $i$. Donc $\sum_i c_i^p\to n$. Que devient alors la puissance $1/p$ ?


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $\sum_i c_i^p\to n>1$ et $1/p\to+\infty$, donc
> $$\Delta_p f = \left(\sum_i c_i^p\right)^{1/p}\xrightarrow[p\to 0^+]{} +\infty.$$
> La combinaison de puissance $0$ n'est pas définie, et sa limite est infinie : elle ne donne aucune information sur l'incertitude.


  **b)** (*) Pour corriger cela, on normalise : $M_p = \left(\dfrac{1}{n}\sum_i c_i^p\right)^{1/p}$. Montrer que $M_p\to\left(\prod_i c_i\right)^{1/n}$ quand $p\to 0$ (moyenne géométrique). Calculer cette valeur pour $r_x=2\ \%$, $r_y=2\ \%$, $r_z=5\ \%$, et discuter : cette quantité est-elle acceptable comme incertitude ?

> [!tip]- 💡 Coup de pouce
> **Développement au premier ordre**
>
> $c^p = e^{p\ln c}\approx 1 + p\ln c$ pour $p$ petit, puis $\ln\!\left(1+\varepsilon\right)\approx\varepsilon$.


> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $\dfrac{1}{n}\sum_i c_i^p \approx 1 + \dfrac{p}{n}\sum_i\ln c_i$, donc
> $$\ln M_p = \frac{1}{p}\ln\!\left(1 + \frac{p}{n}\sum_i\ln c_i\right)\approx\frac{1}{n}\sum_i\ln c_i \quad\Longrightarrow\quad M_p\to\left(\prod_i c_i\right)^{1/n}.$$
> Numériquement (contributions relatives, $n=3$) : $M_0 = (2\times 2\times 5)^{1/3} = 20^{1/3}\approx 2{,}7\ \%$.
>
> **Discussion** : $2{,}7\ \%$ est **inférieur à la plus grande contribution** ($5\ \%$) : une incertitude combinée ne peut pas être plus petite que l'une de ses composantes ($\Delta f\ge c_{\max}$, question 3b). De plus, si une seule grandeur est mesurée sans incertitude ($c_i = 0$), on trouve $M_0 = 0$, alors que les autres incertitudes existent toujours. La moyenne géométrique n'est donc pas acceptable comme incertitude.


  **c)** (*) Montrer que pour $0<p<1$ la combinaison $\Delta_p$ viole l'inégalité triangulaire (sous-additivité) : trouver un exemple avec $p=\tfrac{1}{2}$ et deux vecteurs de contributions $(1,0)$ et $(0,1)$. En déduire pourquoi on se limite à $p\ge 1$.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> Pour $p = \dfrac{1}{2}$ : $\Delta_{1/2}(1,0) = (1)^2 = 1$ et $\Delta_{1/2}(0,1) = 1$, mais
> $$\Delta_{1/2}(1,1) = \left(1^{1/2}+1^{1/2}\right)^{2} = 4 > 1 + 1 = 2.$$
> L'inégalité triangulaire $\Delta(\vec c+\vec c')\le\Delta(\vec c)+\Delta(\vec c')$ est fausse : combiner deux jeux de contributions donne plus que la somme des incertitudes séparées. Pour $p<1$, $\Delta_p$ n'est pas une norme et n'a pas les propriétés qu'on attend d'une incertitude. Seul $p\ge 1$ est cohérent. Avec $p=1$ (pire cas) et $p=2$ (quadratique), les deux cas utiles sont bien dans cette famille.


**6.**

  **a)** Pour $f = \dfrac{x^3z}{y^2}$ avec $\dfrac{\Delta x}{x}=1\ \%$, $\dfrac{\Delta y}{y}=2\ \%$, $\dfrac{\Delta z}{z}=4\ \%$ (exercice 8, question 5), calculer $\dfrac{\Delta_1 f}{f}$, $\dfrac{\Delta_2 f}{f}$ et $\dfrac{\Delta_\infty f}{f}$. Donner une phrase de conclusion pour un rapport de TP.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> $r_x = 3\ \%$, $r_y = 4\ \%$, $r_z = 4\ \%$.
>
>
> - $\dfrac{\Delta_1 f}{f} = 3+4+4 = 11\ \%$
> - $\dfrac{\Delta_2 f}{f} = \sqrt{9+16+16} = \sqrt{41}\approx 6{,}4\ \%$
> - $\dfrac{\Delta_\infty f}{f} = 4\ \%$
>
>
> Conclusion : « L'incertitude relative sur $f$ vaut $11\ \%$ en incertitude maximale (pire cas) et $6{,}4\ \%$ en combinaison quadratique (incertitudes-types indépendantes) ; les mesures de $y$ et $z$ dominent. » Il faut toujours préciser quelle règle a été utilisée.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex1-derivation-de-fonctions-en-physique|Exercice 1 — Dérivation de fonctions en physique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex2-interpretation-de-la-differentielle-petite-variation-calcul-d-incertitude|Exercice 2 — Interprétation de la différentielle : petite variation $\&$ calcul d'incertitude]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex3-derivees-de-fonctions-composees|Exercice 3 — Dérivées de fonctions composées]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex4-differentielle-logarithmique|Exercice 4 — Différentielle logarithmique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex5-derivation-de-fonctions-en-physique-approfondissement|Exercice 5 — Dérivation de fonctions en physique (approfondissement)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex6-interpretation-de-la-differentielle-approfondissement-volume-pendule-approximations|Exercice 6 — Interprétation de la différentielle : approfondissement (volume, pendule, approximations)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex7-derivees-de-fonctions-composees-approfondissement-taux-lies|Exercice 7 — Dérivées de fonctions composées : approfondissement (taux liés)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex8-differentielle-logarithmique-approfondissement-incertitudes-en-situation-reelle|Exercice 8 — Différentielle logarithmique : approfondissement (incertitudes en situation réelle)]]

