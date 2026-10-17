---
title: "Exercice 4 — Différentielle logarithmique"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/index|⬅ Retour]] · <a href="/pdfs/td2_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td2_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 4. Différentielle logarithmique *(facultatif)*

La méthode de la différentielle logarithmique est un outil puissant pour calculer la variation relative ou l'incertitude relative d'une grandeur donnée sous forme de produits, quotients ou puissances.
Rappel : $\mathrm{d}(\ln f) = \frac{\mathrm{d}f}{f}$.

**1.**

  **a)** Compléter l'exemple ci-dessous pour la fonction $f(x,y) = \frac{x^2}{y}$ en suivant la méthode :

  {
    %\fontsize{10pt}{10pt}\selectfont

    \tikzset{
        pointillesPerso/.style={
        % dotted,
        % line width=2pt,
        % line cap=round,
        % dash pattern=on 1pt off 1pt on 1pt off 1pt
        line width=1.5pt,
        line cap=round,
        dash pattern=on 0pt off 3.5pt
      }
    }
    $$
    \begin{array}{rclcrcll
      %r@{\;}c@{\;}c@{\;}l
      %@{\qquad}
      %c@{\;}l
      %@{\qquad}
      %l
    }
    f(x,y) & = & \displaystyle \frac{x^2}{y} & \Longrightarrow & \ln f 
    & = &   \displaystyle  \ln \left ( \frac{x^2}{y} \right )  ~= ~ \tikz[baseline=-0.5ex]\draw[pointillesPerso] (0,0) -- (2.5,0); & \textit{[propriétés du ln]}
    \\[2mm]
    & &  & \Longrightarrow & \mathrm{d} \ln f & = &   \displaystyle  \mathrm{d} \Big ( 2 \, \ln x  ~-~ \tikz[baseline=-0.5ex]\draw[pointillesPerso] (0,0) -- (3,0); \Big )  & \textit{[différentielle d'une somme]}
    \\
    & &  & & & = &   \displaystyle  2 \, \mathrm{d} \ln x  ~-~ \tikz[baseline=-0.5ex]\draw[pointillesPerso] (0,0) -- (3,0);  & 
    \\[2mm]
    & &  & \Longrightarrow & \displaystyle \frac{\mathrm{d}f}{f}& = &   \displaystyle  2 \, \frac{\mathrm{d}x}{x} ~ - ~ \tikz[baseline=-0.5ex]\draw[pointillesPerso] (0,0) -- (3,0);   & \textit{[différentielle du ln]} \\
    & &  & \Longrightarrow  & \displaystyle \mathrm{d}f& = &   \displaystyle  f \Big (2 \, \frac{\mathrm{d}x}{x} ~- ~ \tikz[baseline=-0.5ex]\draw[pointillesPerso] (0,0) -- (3,0);  \Big )   &  \\[2mm]
    & &  & \Longrightarrow  & \displaystyle \delta f& = &   \displaystyle  f \Big (2 \, \frac{\delta x}{x} ~- ~ \tikz[baseline=-0.5ex]\draw[pointillesPerso] (0,0) -- (3,0);  \Big )   &  \textit{[Petite variation de $f$]} \\[2mm]
    & &  & \Longrightarrow  & \displaystyle \displaystyle \frac{\Delta f}{f}& = &   \displaystyle  2 \, \frac{\Delta x}{x} ~ + ~ \tikz[baseline=-0.5ex]\draw[pointillesPerso] (0,0) -- (3,0);     &  \textit{[Incertitude relative]} \\[2mm]
    & &  & \Longrightarrow  & \displaystyle \displaystyle \Delta f& = &   \displaystyle  f \Big (2 \, \frac{\Delta x}{x} ~+ ~ \tikz[baseline=-0.5ex]\draw[pointillesPerso] (0,0) -- (3,0);  \Big )   &  \textit{[Incertitude Absolue]} \\[2mm]
    \end{array}
    $$

  %

}


% * $f(x,y) = \frac{x^2}{y} \implies \ln f = \ln\left(\frac{x^2}{y}\right) = \dots$
% * $\mathrm{d}\ln f = \mathrm{d}(2\ln x - \dots) = 2 \mathrm{d}\ln x - \dots = \dots \implies \frac{\mathrm{d}f}{f} = \dots$ et $\mathrm{d}f = \dots$
% * Petite variation de $f$ : $\delta f = \dots$
% * Incertitude relative : $\frac{\Delta f}{f} = \dots$ et absolue : $\Delta f = \dots$

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> {
> %\fontsize{10pt}{10pt}\selectfont
>
> \tikzset{
>     pointillesPerso/.style={
>     % dotted,
>     % line width=2pt,
>     % line cap=round,
>     % dash pattern=on 1pt off 1pt on 1pt off 1pt
>     line width=1.5pt,
>     line cap=round,
>     dash pattern=on 0pt off 3.5pt
>   }
> }
> $$
> \begin{array}{rclcrcll
>   %r@{\;}c@{\;}c@{\;}l
>   %@{\qquad}
>   %c@{\;}l
>   %@{\qquad}
>   %l
> }
> f(x,y) & = & \displaystyle \frac{x^2}{y} & \Longrightarrow & \ln f 
> & = &   \displaystyle  \ln \left ( \frac{x^2}{y} \right )  & \textit{[propriétés du ln]}\\
> &&&&&=& \ln(x^2) - \ln(y) \\
> &&&&&=& 2\ln x - \ln y 
> \\[2mm]
> & &  & \Longrightarrow & \mathrm{d} \ln f & = &   \displaystyle  \mathrm{d} \Big ( 2\ln x - \ln y  \Big )  & \textit{[différentielle d'une somme]}
> \\
> & &  & & & = &   \displaystyle  2 \, \mathrm{d} \ln x  -  \mathrm{d} \ln y  & 
> \\[2mm]
> & &  & \Longrightarrow & \displaystyle \frac{\mathrm{d}f}{f}& = &   \displaystyle  2 \, \frac{\mathrm{d}x}{x}  -  \frac{\mathrm{d}y}{y}  & \textit{[différentielle du ln]} \\
> & &  & \Longrightarrow  & \displaystyle \mathrm{d}f& = &   \displaystyle  f \Big (2 \, \frac{\mathrm{d}x}{x} - \frac{\mathrm{d}y}{y}  \Big )   &  \\[2mm]
> & &  & \Longrightarrow  & \displaystyle \delta f& = &   \displaystyle  f \Big (2 \, \frac{\delta x}{x} -   \frac{\delta y}{y}  \Big )   &  \textit{[Petite variation de $f$]} \\[2mm]
> & &  & \Longrightarrow  & \displaystyle \displaystyle \frac{\Delta f}{f}& = &   \displaystyle  2 \, \frac{\Delta x}{x}  + \frac{\Delta y}{y}     &  \textit{[Incertitude relative]} \\[2mm]
> & &  & \Longrightarrow  & \displaystyle \displaystyle \Delta f& = &   \displaystyle  f \Big (2 \, \frac{\Delta x}{x} + + \frac{\Delta y}{y}   \Big )   &  \textit{[Incertitude Absolue]} \\
> &&&&& =  &  \displaystyle \frac{2x}{y}\Delta x + \frac{x^2}{y^2}\Delta y\\[2mm]
> \end{array}
> $$
>
>   %
>
> }
> %* **Logarithme** : $\ln f = \ln(x^2) - \ln(y) = 2\ln x - \ln y$
> %* **Différentielle** : $\mathrm{d}\ln f = 2 \mathrm{d}(\ln x) - \mathrm{d}(\ln y) = 2 \frac{\mathrm{d}x}{x} - \frac%%{\mathrm{d}y}{y}$
> %* **Calcul de $\frac{\mathrm{d}f}{f}$ et $\mathrm{d}f$** :
> %  $$\frac{\mathrm{d}f}{f} = 2 \frac{\mathrm{d}x}{x} - \frac{\mathrm{d}y}{y}$$
> %  $$\mathrm{d}f = f \left(2 \frac{\mathrm{d}x}{x} - \frac{\mathrm{d}y}{y}\right) = \frac{x^2}{y} \left(2 \frac{\mathrm{d}x}{x} - \frac{\mathrm{d}y}{y}\right) = \frac{2x}{y}\mathrm{d}x - \frac{x^2}{y^2}\mathrm{d}y$$
> %* **Petite variation** : $\delta f = \frac{x^2}{y} \left(2 \frac{\delta x}{x} - \frac{\delta y}{y}\right) = \frac{2x}{y}\delta x - \frac{x^2}{y^2}\delta y$
> %* **Incertitudes** :
> %  $$\text{Relative : } \frac{\Delta f}{f} = 2 \frac{\Delta x}{x} + \frac{\Delta y}{y}$$
> %  $$\text{Absolue : } \Delta f = \frac{x^2}{y} \left(2 \frac{\Delta x}{x} + \frac{\Delta y}{y}\right) = \frac{2x}{y}\Delta x + \frac{x^2}{y^2}\Delta y$$


**2.**

  **a)** Calculer la variation $\delta f$ et l'incertitude absolue $\Delta f$ pour la fonction $f(x) = x^2$ par la méthode logarithmique.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> 1. $\ln f = 2\ln x$
> 2. $\frac{\mathrm{d}f}{f} = 2 \frac{\mathrm{d}x}{x}$
> 3. Variation : $\delta f = 2 x \delta x$
> 4. Incertitude relative : $\frac{\Delta f}{f} = 2 \frac{\Delta x}{x}$
> 5. Incertitude absolue : $\Delta f = 2 x \Delta x$


  **b)** Calculer la variation $\delta f$ et l'incertitude absolue $\Delta f$ pour la fonction $f(x,y) = xy$ par la méthode logarithmique.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> 1. $\ln f = \ln x + \ln y$
> 2. $\frac{\mathrm{d}f}{f} = \frac{\mathrm{d}x}{x} + \frac{\mathrm{d}y}{y}$
> 3. Variation : $\delta f = y \delta x + x \delta y$
> 4. Incertitude relative : $\frac{\Delta f}{f} = \frac{\Delta x}{x} + \frac{\Delta y}{y}$
> 5. Incertitude absolue : $\Delta f = y \Delta x + x \Delta y$


  **c)** Calculer la variation $\delta f$ et l'incertitude absolue $\Delta f$ pour la fonction $f(x,y,z) = \frac{xy}{z}$ par la méthode logarithmique.

> [!example]- 📝 Solution détaillée
> **Résolution**
>
> 1. $\ln f = \ln x + \ln y - \ln z$
> 2. $\frac{\mathrm{d}f}{f} = \frac{\mathrm{d}x}{x} + \frac{\mathrm{d}y}{y} - \frac{\mathrm{d}z}{z}$
> 3. Variation : $\delta f = \frac{xy}{z} \left(\frac{\delta x}{x} + \frac{\delta y}{y} - \frac{\delta z}{z}\right)$
> 4. Incertitude relative : $\frac{\Delta f}{f} = \frac{\Delta x}{x} + \frac{\Delta y}{y} + \frac{\Delta z}{z}$
> 5. Incertitude absolue : $\Delta f = \frac{xy}{z} \left(\frac{\Delta x}{x} + \frac{\Delta y}{y} + \frac{\Delta z}{z}\right) = \frac{y}{z}\Delta x + \frac{x}{z}\Delta y + \frac{xy}{z^2}\Delta z$


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex1-derivation-de-fonctions-en-physique|Exercice 1 — Dérivation de fonctions en physique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex2-interpretation-de-la-differentielle-petite-variation-calcul-d-incertitude|Exercice 2 — Interprétation de la différentielle : petite variation $\&$ calcul d'incertitude]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex3-derivees-de-fonctions-composees|Exercice 3 — Dérivées de fonctions composées]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex5-derivation-de-fonctions-en-physique-approfondissement|Exercice 5 — Dérivation de fonctions en physique (approfondissement)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex6-interpretation-de-la-differentielle-approfondissement-volume-pendule-approximations|Exercice 6 — Interprétation de la différentielle : approfondissement (volume, pendule, approximations)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex7-derivees-de-fonctions-composees-approfondissement-taux-lies|Exercice 7 — Dérivées de fonctions composées : approfondissement (taux liés)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex8-differentielle-logarithmique-approfondissement-incertitudes-en-situation-reelle|Exercice 8 — Différentielle logarithmique : approfondissement (incertitudes en situation réelle)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex9-combiner-les-incertitudes-somme-absolue-p-1-quadratique-p-2-puissance-p-et-cas-p-0|Exercice 9 — Combiner les incertitudes : somme absolue ($p=1$), quadratique ($p=2$), puissance $p$ et cas $p=0$]]

