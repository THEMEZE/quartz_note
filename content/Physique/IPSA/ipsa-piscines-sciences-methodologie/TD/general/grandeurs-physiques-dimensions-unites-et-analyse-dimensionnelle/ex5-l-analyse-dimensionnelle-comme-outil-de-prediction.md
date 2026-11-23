---
title: "Exercice 5 — L'analyse dimensionnelle comme outil de prédiction"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/index|⬅ Retour]] · <a href="/pdfs/td1_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 5. L'analyse dimensionnelle comme outil de prédiction

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 25 min · Type : Révision*

L’analyse des dimensions d’un problème complexe permet de prédire la forme d’une loi physique.

> [!abstract]+ 📚 Prérequis
> **Grandeurs physiques et dimensions**
>
> - **Dimensions fondamentales**
>
>
>
> - Connaître les dimensions de la masse $M$,
>       de la longueur $L$ et du temps $T$.
> - Savoir exprimer une grandeur dérivée
>       à partir des dimensions fondamentales.
> - **Grandeurs dérivées**
>
>
>
> - Connaître la dimension de la force :
>       $[F] = M L T^{-2}$.
> - Connaître la dimension de la vitesse :
>       $[v] = L T^{-1}$.
> - Connaître la dimension de l'accélération :
>       $[a] = L T^{-2}$.
> - Connaître la dimension de la pression :
>       $[P] = M L^{-1} T^{-2}$.
>
> **Règles de calcul dimensionnel**
>
> - **Opérations sur les dimensions**
>
>
>
> - Savoir multiplier et diviser
>       des dimensions physiques.
> - Savoir manipuler les puissances
>       de grandeurs physiques.
> - Savoir additionner les exposants
>       des dimensions lors d'un produit.
> - **Homogénéité dimensionnelle**
>
>
>
> - Vérifier que les deux membres
>       d'une relation possèdent la même dimension.
> - Identifier les dimensions fondamentales
>       présentes dans une expression.
>
> **Manipulation algébrique et puissances**
>
> - **Calcul littéral**
>
>
>
> - Savoir écrire une relation sous la forme
>       d'un produit de puissances.
> - Savoir résoudre un système linéaire
>       à plusieurs inconnues.
> - Savoir manipuler les exposants
>       d'une expression algébrique.


> [!info]+ 🎯 Objectifs
> **Identifier les grandeurs pertinentes**
>
> - **Analyse du problème physique**
>
>
>
> - Identifier les grandeurs physiques
>       susceptibles d'influencer la grandeur recherchée.
> - Distinguer les grandeurs fondamentales
>       des grandeurs dérivées.
> - Déterminer les dimensions des grandeurs
>       intervenant dans un problème physique.
>
> **Construire une loi physique par analyse dimensionnelle**
>
> - **Forme générale d'une loi**
>
>
>
> - Émettre une hypothèse sur la forme
>       de la dépendance entre les grandeurs.
> - Exprimer la grandeur recherchée
>       sous la forme d'un produit de puissances :
>
>       \[
>         X = k A^\alpha B^\beta C^\gamma.
>       \]
> - Comprendre le rôle de la constante
>       sans dimension $k$.
> - **Mise en équation**
>
>
>
> - Écrire l'équation aux dimensions
>       correspondant à la relation supposée.
> - Décomposer chaque grandeur
>       en dimensions fondamentales.
> - Identifier les exposants des dimensions
>       de chaque côté de l'égalité.
>
> **Résoudre un système d'équations dimensionnelles**
>
> - **Construction du système**
>
>
>
> - Associer une équation à chaque dimension
>       fondamentale présente.
> - Résoudre le système linéaire
>       obtenu pour les exposants inconnus.
> - Vérifier la cohérence des valeurs
>       des exposants avec la relation initiale.
>
> **Prédire une loi physique**
>
> - **Application à la loi de Stokes**
>
>
>
> - Déterminer la dépendance de la force
>       visqueuse en fonction de $\eta$, $r$ et $v$.
> - Retrouver la structure de la loi :
>
>       \[
>         F = k \eta r v.
>       \]
> - Comprendre que l'analyse dimensionnelle
>       ne permet pas de déterminer le facteur numérique
>       $k$.
> - **Application au pendule simple**
>
>
>
> - Identifier les grandeurs pertinentes
>       pour la période d'oscillation.
> - Montrer que la masse n'intervient pas
>       dans l'expression dimensionnelle recherchée.
> - Déterminer la dépendance de la période
>       en fonction de $\ell$ et $g$.
>
> **Identifier les limites de la méthode**
>
> - **Interprétation des résultats**
>
>
>
> - Distinguer la forme dimensionnelle
>       d'une loi de sa forme exacte.
> - Identifier le rôle des constantes
>       sans dimension.
> - Comprendre que plusieurs lois peuvent
>       être compatibles avec une même analyse
>       dimensionnelle.


> [!note]+ 📖 Point de cours
> **Principe de l'analyse dimensionnelle**
>
> - **Objectif de la méthode**
>
>
>
> - Utiliser les dimensions physiques
>       pour contraindre la forme d'une relation.
> - Exploiter l'homogénéité dimensionnelle
>       d'une loi physique.
> - Déterminer les dépendances en puissances
>       de plusieurs grandeurs physiques.
> - **Hypothèse de départ**
>
>
>
> - On suppose que la grandeur recherchée
>       peut s'écrire sous la forme :
>
>       \[
>         X = k A^\alpha B^\beta C^\gamma.
>       \]
> - La constante $k$ est supposée sans dimension.
> - Les exposants $\alpha$, $\beta$ et $\gamma$
>       sont déterminés par homogénéité dimensionnelle.
>
> **Méthode générale de résolution**
>
> - **Étape 1 : Identifier les grandeurs**
>
>
>
> - Lister les grandeurs susceptibles
>       d'influencer la grandeur recherchée.
> - Déterminer les dimensions de chaque grandeur.
> - **Étape 2 : Proposer une relation**
>
>
>
> - Écrire la grandeur recherchée
>       comme un produit de puissances.
> - Introduire une constante sans dimension.
> - **Étape 3 : Écrire l'équation aux dimensions**
>
>
>
> - Remplacer chaque grandeur par sa dimension.
> - Développer les puissances
>       des dimensions fondamentales.
> - **Étape 4 : Construire le système**
>
>
>
> - Identifier les exposants de $M$, $L$ et $T$.
> - Égaler les exposants de chaque dimension
>       fondamentale entre les deux membres.
> - **Étape 5 : Résoudre et conclure**
>
>
>
> - Résoudre le système linéaire
>       sur les exposants inconnus.
> - Remplacer les exposants dans la relation
>       de départ.
> - Interpréter le résultat obtenu.
>
> **Application à la loi de Stokes**
>
> - **Grandeurs physiques**
>
>
>
> - Force :
>
>       \[
>         [F] = M L T^{-2}.
>       \]
> - Viscosité dynamique :
>
>       \[
>         [\eta] = M L^{-1} T^{-1}.
>       \]
> - Rayon :
>
>       \[
>         [r] = L.
>       \]
> - Vitesse :
>
>       \[
>         [v] = L T^{-1}.
>       \]
> - **Forme supposée**
>
>
>
> - On suppose :
>
>       \[
>         F = k\eta^\alpha r^\beta v^\gamma.
>       \]
> - L'équation aux dimensions donne :
>
>       \[
>         M L T^{-2}
>         =
>         M^\alpha
>         L^{-\alpha+\beta+\gamma}
>         T^{-\alpha-\gamma}.
>       \]
> - **Résolution**
>
>
>
> - Équations sur les exposants :
>
>       \[
>         \begin{cases}
>           \alpha = 1,\\
>           -\alpha+\beta+\gamma = 1,\\
>           -\alpha-\gamma = -2.
>         \end{cases}
>       \]
> - Solution :
>
>       \[
>         \alpha = \beta = \gamma = 1.
>       \]
> - Expression obtenue :
>
>       \[
>         F = k\eta r v.
>       \]
>
> **Application au pendule simple**
>
> - **Grandeurs physiques**
>
>
>
> - Période :
>
>       \[
>         [T] = T.
>       \]
> - Masse :
>
>       \[
>         [m] = M.
>       \]
> - Longueur :
>
>       \[
>         [\ell] = L.
>       \]
> - Accélération de la pesanteur :
>
>       \[
>         [g] = L T^{-2}.
>       \]
> - **Forme supposée**
>
>
>
> - On suppose :
>
>       \[
>         T = k m^\alpha \ell^\beta g^\gamma.
>       \]
> - Équation aux dimensions :
>
>       \[
>         T
>         =
>         M^\alpha
>         L^{\beta+\gamma}
>         T^{-2\gamma}.
>       \]
> - **Résolution**
>
>
>
> - Le système donne :
>
>       \[
>         \begin{cases}
>           \alpha = 0,\\
>           \beta+\gamma = 0,\\
>           -2\gamma = 1.
>         \end{cases}
>       \]
> - Solution :
>
>       \[
>         \alpha=0,\qquad
>         \beta=\frac{1}{2},\qquad
>         \gamma=-\frac{1}{2}.
>       \]
> - Expression obtenue :
>
>       \[
>         T = k\sqrt{\frac{\ell}{g}}.
>       \]
>
> **Limites de l'analyse dimensionnelle**
>
> - **Constante sans dimension**
>
>
>
> - L'analyse dimensionnelle ne permet
>       généralement pas de déterminer le facteur
>       numérique sans dimension $k$.
> - Dans la loi de Stokes,
>       la théorie hydrodynamique donne $k=6\pi$
>       pour une sphère dans le régime de Stokes.
> - Pour le pendule simple,
>       l'approximation des petites oscillations
>       conduit à $k=2\pi$.
> - **Domaine de validité**
>
>
>
> - La méthode dépend des grandeurs
>       sélectionnées au départ.
> - Une grandeur pertinente oubliée
>       peut modifier la forme de la loi.
> - Les dépendances plus complexes,
>       comme les fonctions trigonométriques,
>       ne sont pas nécessairement déterminées
>       par une simple approche en puissances.


> [!tip]- 💡 Coup de pouce
> **Méthodologie 
> **
>
> {\bf Méthode pour déterminer une relation par analyse dimensionnelle.}\\
>
> \begin{enumerate}[label = (\roman*)]
>   \item Lister les grandeurs dont peut dépendre la grandeur recherchée $X$
>   \item Exprimer $X$ en fonction des autres grandeurs $A$,$B$,$C$ :
>   $$
>   X = k A^\alpha B^\beta C^\gamma \quad \text{où $k$ est une constante sans dimension}
>   $$
>   \item Écrire l’équation aux dimensions de la relation :
>   $$
>   [X] = k [A]^\alpha [B]^\beta [C]^\gamma 
>   $$
>   \item Préciser les dimensions des grandeurs de chaque côté de l’égalité.
>   \item En déduire le système d’équations vérifié par $\alpha$, $\beta$, $\gamma$.
>   \item Résoudre le système et conclure sur l’expression de $X$.
> \end{enumerate}


**q1.** **Loi de Stokes.**\\

La loi de Stokes donne la force de frottement sur une sphère en déplacement dans un fluide. L’expérience montre que la force subie par une sphère immergée dans un fluide dépend :



- du coefficient de viscosité $\eta$ du fluide, d’unités : $Pa.s$ (pascal seconde)
- du rayon $r$ de la sphère,
- de la vitesse $v$ de la sphère par rapport au fluide.





(a) Indiquer si les grandeurs physiques citées dans l’énoncé sont des grandeurs fondamentales ou dérivées et donner leur dimension.

(b) En supposant que la force $F$ s’écrit en fonction des autres grandeurs sous cette forme :
  $$
  F= k\eta^\alpha r^\beta v^\gamma, \quad  \text{où $k$ est une constante sans dimension,}
  $$
  écrire l’équation aux dimensions reliant la dimension $[F]$ à celle des autres grandeurs.

(c) Préciser les dimensions des grandeurs en dimensions de base de chaque côté de l’égalité.

(d) Résoudre le système d’équations pour trouver les valeurs de $\alpha$, $\beta$ et $\gamma$.

(e) Conclure sur l’expression de la force $F$.

(f) Peut on déterminer la valeur de la constante $k$ par analyse dimensionnelle ?

> [!tip]- 💡 Coup de pouce
> On écrit $X = k * A^\alpha * B^\beta * C^\gamma$. L'égalité des puissances de $M$, $L$,$T$ de chaque côté génère un système linéaire sur $\alpha$, $\beta$, $\gamma$.


> [!example]- 📝 Solution détaillée
> (a) %\vspace{-0.5cm}
>
>
> - la force : $[F] = M * L * T^{-2}$ (grandeur dérivée)
> - la distance : $[r] = L$ (grandeur fondamental)
> - la vitesse : $[v] = L * T^{-1}$ (grandeur dérivée)
> - du coefficient de viscosité $\eta$ du fluide : $[\eta] = M * L^{-1} * T^{-1} $ (grandeur dérivée) .
>
> (b) [b) et c)] $M^1 * L^1 * T^{-2} = [F] = \overbrace{(M * L^{-1} * T^{-1})^\alpha}^{[\eta^\alpha]} * \overbrace{L^\beta}^{[r^\beta]}* \overbrace{(L * T^{-1})^\gamma}^{[v^\gamma]} = M^\alpha * L^{(\beta - \alpha + \gamma)} * T^{-(\alpha + \gamma )} $ donc :
>
> (c) [d)] 
>   $$
>   \alpha = 1 ; \quad \beta - \alpha + \gamma = 1; \quad  \alpha + \gamma  = 2 
>   $$
>   Donc 
>   $$
>   \alpha = \beta = \gamma = 1.
>   $$
>
> (d) [e)] 
>   $$
>   F = k  \eta  r v
>   $$
>
> (e) [f)] $k$ ne peut pas être déterminé uniquement par l'analyse dimensionnelle.


**q2.** **(${}^\ast$) Période $\bm{T}$ des oscillations d’un pendule simple**\\

Soit un pendule simple constitué d’une masse $m$ accrochée à l’extrémité d’un fil de longueur $\ell$. L’étude s’effectue dans le référentiel terrestre où le champ de pesanteur est $\vec{g}$ .



(a) Énumérer les grandeurs et dimensions qui interviennent dans le problème.

(b) Déterminer l’expression de la période $T$ par analyse dimensionnelle. *Appliquer la méthode !*

> [!tip]- 💡 Coup de pouce
> Si la dimension d'une grandeur n'apparaît pas dans le membre de gauche, son exposant correspondant dans le système doit être égal à 0.


> [!example]- 📝 Solution détaillée
> (a) %\vspace{-0.5cm}
>
>
> - la masse $m$ : $[m] = M $ (grandeur fondamental)
> - la longueur $\ell$ : $[\ell] = L$ (grandeur fondamental)
> - la pesanteur $g$ : $[g] = L * T^{-2} = [a]$  une accélération (grandeur dérivée)
>
> (b) Pour $T = k ~m^\alpha ~  ~\ell^\beta g^\gamma$ donc  
>   $$
>   M^{0} * L^{0} * T^1 = [T] = \overbrace{M^\alpha}^{[m^\alpha]} * \overbrace{L^\beta}^{[\ell^\beta]}* \overbrace{(L * T^{-2})^\gamma}^{[g^\gamma]} = M^\alpha * L^{(\beta + \gamma)} * T^{-2*\gamma} 
>   $$ 
>   Donc 
>   $$
>   \alpha = 0 ; \quad \beta + \gamma = 0; \quad  2 * \gamma  = -1 
>   $$
>   Donc 
>   $$
>   \alpha = 0; \quad  \beta = 1/2 ; \quad \gamma = -1/2.
>   $$
>   Donc
>   $$
>   T = k  \sqrt{\frac{\ell}{g}}
>   $$


> [!question]- 🔭 Aller plus loin — Lycée : Vérification dimensionnelle de lois physiques

> - **Lois de la mécanique**
>
>
>
> - Vérifier la dimension de la vitesse
>       à partir de $v=d/t$.
> - Vérifier la dimension de l'énergie
>       cinétique :
>
>       \[
>         E_c = \frac{1}{2}mv^2.
>       \]
> - Déterminer la dimension
>       de la constante de raideur $k$
>       dans la loi de Hooke :
>
>       \[
>         F = kx.
>       \]
> - **Analyse de relations**
>
>
>
> - Identifier les relations homogènes
>       et non homogènes.
> - Vérifier la cohérence des unités
>       dans une formule de physique.


> [!question]- 🔭 Aller plus loin — CPGE : Théorème de Buckingham et lois d'échelle

> - **Théorème de Buckingham**
>
>
>
> - Comprendre le principe du théorème
>       des groupes sans dimension.
> - Déterminer le nombre de groupes
>       sans dimension indépendants.
> - Construire des groupes $\Pi$
>       à partir des grandeurs physiques.
> - **Applications**
>
>
>
> - Étudier les lois d'échelle
>       dans des problèmes de mécanique des fluides.
> - Introduire le nombre de Reynolds :
>
>       \[
>         \mathrm{Re} = \frac{\rho v L}{\eta}.
>       \]
> - Relier le nombre de Reynolds
>       aux régimes d'écoulement.


> [!question]- 🔭 Aller plus loin — Licence : Analyse dimensionnelle et lois physiques exactes

> - **Loi de Stokes**
>
>
>
> - Étudier les hypothèses de validité
>       de la loi de Stokes.
> - Comprendre le rôle du nombre de Reynolds
>       dans l'écoulement autour d'une sphère.
> - Relier l'analyse dimensionnelle
>       aux équations de Navier--Stokes.
> - **Pendule simple**
>
>
>
> - Démontrer l'équation différentielle
>       du pendule simple.
> - Utiliser l'approximation
>       des petits angles.
> - Comparer la période exacte
>       et la période approchée.
> - **Analyse dimensionnelle avancée**
>
>
>
> - Étudier le rôle des groupes
>       sans dimension dans la modélisation.
> - Identifier les limites d'une
>       approche purement dimensionnelle.


> [!question]- 🔭 Aller plus loin — Master : Similarité physique et modélisation avancée

> - **Théorie de la similarité**
>
>
>
> - Étudier les conditions de similarité
>       entre deux systèmes physiques.
> - Distinguer la similarité géométrique,
>       cinématique et dynamique.
> - Utiliser les nombres sans dimension
>       pour construire des modèles réduits.
> - **Mécanique des fluides**
>
>
>
> - Étudier les nombres de Reynolds,
>       de Froude et de Weber.
> - Relier les groupes sans dimension
>       aux régimes physiques observés.
> - Comprendre les limites
>       de la transposition d'une expérience
>       à un système réel.
> - **Modélisation théorique**
>
>
>
> - Comparer les prédictions
>       de l'analyse dimensionnelle
>       aux solutions des équations physiques.
> - Étudier les dépendances
>       qui ne peuvent pas être déterminées
>       par la seule homogénéité dimensionnelle.
> - Introduire l'analyse asymptotique
>       et les approximations de modèles.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex1-grandeurs-physiques-fondamentales-dimensions-et-unites-de-base|Exercice 1 — Grandeurs physiques fondamentales : dimensions et unités de base]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex2-grandeurs-derivees-equation-au-dimensions-dimension-et-unites-derivees-composees|Exercice 2 — Grandeurs Dérivées : Équation au dimensions , dimension et unités dérivées (composées)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex3-homogeneite-et-analyse-dimensinnelle|Exercice 3 — Homogénéité et Analyse Dimensinnelle]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex4-lois-et-constantes-fondamentales-en-physiques|Exercice 4 — Lois et Constantes Fondamentales en physiques]]

