---
title: "Exercice 4 — Différentielle logarithmique"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/index|⬅ Retour]] · <a href="/pdfs/td2_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td2_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 4. Différentielle logarithmique *(facultatif)*

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 30 min · Type : Méthode $\&$ Calcul*

La méthode de la différentielle logarithmique est un outil puissant pour calculer la variation relative ou l'incertitude relative d'une grandeur donnée sous forme de produits, quotients ou puissances.
Rappel : $\mathrm{d}(\ln f) = \frac{\mathrm{d}f}{f}$.


> [!abstract]- 🧠 À savoir avant
> **Propriétés du logarithme népérien**
>
> $\ln(ab) = \ln a + \ln b$, $\ln(a/b) = \ln a - \ln b$, $\ln(a^n) = n \ln a$.




> [!info]- 🎯 Ce que tu sauras faire
> **Maîtriser la méthode logarithmique**
>
> Calculer facilement $\frac{\mathrm{d}f}{f}$, $\delta f$ et l'incertitude absolue $\Delta f$ pour des fonctions multi-variables.




> [!tip]- 📖 Rappel de cours
> **Méthode de la différentielle logarithmique**
>
> 1. Écrire $f(x,y,\dots)$.
> 2. Prendre le logarithme : $\ln f$.
> 3. Utiliser les propriétés du $\ln$ pour réécrire les termes.
> 4. Prendre la différentielle : $\mathrm{d}(\ln f) = \frac{\mathrm{d}f}{f}$.
> 5. Application aux petites variations $\delta f$ : remplacer $\mathrm{d}$ par $\delta$.
> 6. Application au calcul d'incertitudes $\Delta f$ : remplacer $\mathrm{d}$ par $\Delta$ en comptant chaque terme d'une somme positivement.




> [!tip]- 💡 Coup de pouce
> **Passage aux incertitudes $\Delta$
> **
>
> Pour obtenir l'incertitude maximale $\Delta f$, remplace tous les $\mathrm{d}$ par des $\Delta$ et mets {\bf tous les signes en valeur absolue (+)}.



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




> [!question]- 🔭 Aller plus loin — Master : Incertitudes au plurielle
> Comparer la méthode des incertitudes maximales à la combinaison quadratique $\left(\frac{\Delta f}{f}\right)^2 = \sum \left(\frac{\Delta x_i}{x_i}\right)^2$.\\




> [!question]- 🔭 Aller plus loin — Master : Incertitudes au pluriel : comparer les méthodes
> Pour une grandeur
> \[
>   f(x,y,z)=x^\alpha y^\beta z^\gamma,
> \]
> on peut estimer l'incertitude sur $f$ de plusieurs façons. Les méthodes ne correspondent pas au même modèle d'incertitude et ne conduisent donc pas nécessairement au même résultat.
>
>
>
>
> **1. Incertitude absolue et incertitude relative**
>
> L'incertitude absolue sur une grandeur $x$ est notée $\Delta x$ et possède
> la même unité que $x$. L'incertitude relative est le rapport sans dimension
> \[
>   \frac{\Delta x}{x}.
> \]
> Elle permet notamment de comparer la précision de mesures exprimées dans
> des unités ou à des échelles différentes.
>
>
>
>
> **2. Propagation des incertitudes par différentiation**
>
> Pour de petites variations des grandeurs d'entrée, on peut écrire
> \[
>   \mathrm{d}f
>   =
>   \frac{\partial f}{\partial x}\mathrm{d}x
>   +
>   \frac{\partial f}{\partial y}\mathrm{d}y
>   +
>   \frac{\partial f}{\partial z}\mathrm{d}z.
> \]
>
> Pour
> \[
>   f=x^\alpha y^\beta z^\gamma,
> \]
> on obtient
> \[
>   \frac{\mathrm{d}f}{f}
>   =
>   \alpha\frac{\mathrm{d}x}{x}
>   +
>   \beta\frac{\mathrm{d}y}{y}
>   +
>   \gamma\frac{\mathrm{d}z}{z}.
> \]
>
> Cette relation montre notamment le rôle des exposants : une grandeur
> élevée à une puissance importante contribue davantage à l'incertitude
> relative de $f$.
>
>
>
>
> **3. Méthode des incertitudes maximales**
>
> Si l'on cherche une **borne maximale** de variation et que les
> contributions peuvent toutes se cumuler dans le même sens, on considère
> les valeurs absolues :
> \[
>   \boxed{
>   \frac{\Delta f}{f}
>   \simeq
>   |\alpha|\frac{\Delta x}{x}
>   +
>   |\beta|\frac{\Delta y}{y}
>   +
>   |\gamma|\frac{\Delta z}{z}
>   }.
> \]
>
> Cette méthode est volontairement conservative : elle correspond à la
> situation où toutes les contributions s'ajoutent de manière défavorable.
>
>
>
>
> **4. Combinaison quadratique des incertitudes**
>
> Lorsque les incertitudes sont considérées comme des contributions
> indépendantes et aléatoires, on utilise plutôt une combinaison
> quadratique :
> \[
>   \boxed{
>   \left(\frac{u(f)}{f}\right)^2
>   =
>   \alpha^2
>   \left(\frac{u(x)}{x}\right)^2
>   +
>   \beta^2
>   \left(\frac{u(y)}{y}\right)^2
>   +
>   \gamma^2
>   \left(\frac{u(z)}{z}\right)^2
>   }.
> \]
>
> Ainsi,
> \[
>   \frac{u(f)}{f}
>   =
>   \sqrt{
>   \alpha^2\left(\frac{u(x)}{x}\right)^2
>   +
>   \beta^2\left(\frac{u(y)}{y}\right)^2
>   +
>   \gamma^2\left(\frac{u(z)}{z}\right)^2
>   }.
> \]
>
>
>
>
> **5. Influence des puissances**
>
> Les exposants permettent d'identifier rapidement les grandeurs les plus
> influentes. Par exemple, pour
> \[
>   f=x^2y,
> \]
> l'incertitude maximale relative vaut
> \[
>   \frac{\Delta f}{f}
>   \simeq
>   2\frac{\Delta x}{x}
>   +
>   \frac{\Delta y}{y},
> \]
> tandis que la combinaison quadratique donne
> \[
>   \frac{u(f)}{f}
>   =
>   \sqrt{
>     4\left(\frac{u(x)}{x}\right)^2
>     +
>     \left(\frac{u(y)}{y}\right)^2
>   }.
> \]
>
> Pour
> \[
>   f=\frac{x^2}{y},
> \]
> on a
> \[
>   \frac{\mathrm{d}f}{f}
>   =
>   2\frac{\mathrm{d}x}{x}
>   -
>   \frac{\mathrm{d}y}{y}.
> \]
> Le signe «$-$» indique le sens de variation de $f$ lorsque $y$
> varie, mais il disparaît dans l'expression de l'incertitude maximale :
> \[
>   \frac{\Delta f}{f}
>   \simeq
>   2\frac{\Delta x}{x}
>   +
>   \frac{\Delta y}{y}.
> \]
>
>
>
>
> **6. Ce qu'il faut retenir**
>
>
>
> - Une **incertitude absolue** $\Delta x$ possède la même unité
>     que $x$.
> - Une **incertitude relative** $\Delta x/x$ est sans dimension
>     et s'exprime souvent en pourcentage.
> - Dans une relation de type
>     $f=x^\alpha y^\beta z^\gamma$, les exposants $\alpha$, $\beta$ et
>     $\gamma$ pondèrent les contributions relatives.
> - Pour une **incertitude maximale**, les contributions sont
>     additionnées en valeur absolue :
>     \[
>       \frac{\Delta f}{f}
>       \simeq
>       \sum_i |a_i|\frac{\Delta x_i}{x_i}.
>     \]
> - Pour des **incertitudes indépendantes et aléatoires**, les
>     contributions sont combinées quadratiquement :
>     \[
>       \left(\frac{u(f)}{f}\right)^2
>       =
>       \sum_i
>       a_i^2
>       \left(\frac{u(x_i)}{x_i}\right)^2.
>     \]
> - Il ne faut pas confondre ces deux méthodes : la première cherche
>     une **borne de variation maximale**, tandis que la seconde
>     décrit une **incertitude-type composée** sous des hypothèses
>     statistiques.
> - Pour une analyse expérimentale, il est important d'indiquer
>     **quelle définition de l'incertitude est utilisée** et de ne
>     pas mélanger $\Delta x$, qui peut désigner une incertitude maximale,
>     avec $u(x)$, qui désigne généralement une incertitude-type.
>
>
>
>
>
>
> **À mettre en avant :**
>
>
>
> - les **incertitudes relatives** plutôt que seulement les
>     incertitudes absolues lorsque l'on compare des contributions ;
> - les **exposants** devant chaque incertitude relative : ils
>     indiquent immédiatement quelles mesures peuvent dominer
>     l'incertitude finale ;
> - la différence entre une **somme linéaire** (incertitude
>     maximale) et une **somme quadratique** (incertitude-type
>     composée) ;
> - les hypothèses associées à chaque méthode plutôt que de retenir
>     une formule sans préciser son domaine d'utilisation.
>
>
>
>
>
>
> **Exercice conseillé :**
> proposer successivement
> \[
>   f_1=xy,\qquad
>   f_2=\frac{x^2}{y},\qquad
>   f_3=\frac{x^3z}{y^2},
> \]
> avec des incertitudes relatives différentes pour $x$, $y$ et $z$.
> Demander aux étudiants de calculer, pour chaque cas, l'incertitude
> maximale puis l'incertitude-type composée, et de comparer la contribution
> de chaque grandeur.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex1-derivation-de-fonctions-en-physique|Exercice 1 — Dérivation de fonctions en physique]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex2-interpretation-de-la-differentielle-petite-variation-calcul-d-incertitude|Exercice 2 — Interprétation de la différentielle : petite variation $\&$ calcul d'incertitude]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex3-derivees-de-fonctions-composees|Exercice 3 — Dérivées de fonctions composées]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex5-derivation-de-fonctions-en-physique-approfondissement|Exercice 5 — Dérivation de fonctions en physique (approfondissement)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex6-interpretation-de-la-differentielle-approfondissement-volume-pendule-approximations|Exercice 6 — Interprétation de la différentielle : approfondissement (volume, pendule, approximations)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex7-derivees-de-fonctions-composees-approfondissement-taux-lies|Exercice 7 — Dérivées de fonctions composées : approfondissement (taux liés)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex8-differentielle-logarithmique-approfondissement-incertitudes-en-situation-reelle|Exercice 8 — Différentielle logarithmique : approfondissement (incertitudes en situation réelle)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/derivation-et-differentielle-6h-interpretation-en-physique/ex9-combiner-les-incertitudes-somme-absolue-p-1-quadratique-p-2-puissance-p-et-cas-p-0|Exercice 9 — Combiner les incertitudes : somme absolue ($p=1$), quadratique ($p=2$), puissance $p$ et cas $p=0$]]


