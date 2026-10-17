---
title: "Exercice 5 — L'analyse dimensionnelle comme outil de prédiction"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/index|⬅ Retour]] · <a href="/pdfs/td1_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 5. L'analyse dimensionnelle comme outil de prédiction

L’analyse des dimensions d’un problème complexe permet de prédire la forme d’une loi physique.

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


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex1-grandeurs-physiques-fondamentales-dimensions-et-unites-de-base|Exercice 1 — Grandeurs physiques fondamentales : dimensions et unités de base]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex2-grandeurs-derivees-equation-au-dimensions-dimension-et-unites-derivees-composees|Exercice 2 — Grandeurs Dérivées : Équation au dimensions , dimension et unités dérivées (composées)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex3-homogeneite-et-analyse-dimensinnelle|Exercice 3 — Homogénéité et Analyse Dimensinnelle]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex4-lois-et-constantes-fondamentales-en-physiques|Exercice 4 — Lois et Constantes Fondamentales en physiques]]

