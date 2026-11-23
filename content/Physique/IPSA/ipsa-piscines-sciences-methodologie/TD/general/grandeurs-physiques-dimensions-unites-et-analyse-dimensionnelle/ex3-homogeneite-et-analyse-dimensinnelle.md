---
title: "Exercice 3 — Homogénéité et Analyse Dimensinnelle"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/index|⬅ Retour]] · <a href="/pdfs/td1_PhV110_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 3. Homogénéité et Analyse Dimensinnelle

*⭐ Indispensable · Difficulté ●●○○○ · ⏱ 25 min · Type : Révision*

L'analyse dimensionnelle est un outil permettant de vérifier rapidement
la cohérence d'une relation physique. Elle repose notamment sur le principe
d'homogénéité : deux grandeurs additionnées ou soustraites doivent avoir
la même dimension, et les deux membres d'une équation physique doivent
également avoir la même dimension.

Cet exercice permet de revoir les règles fondamentales de l'analyse
dimensionnelle et de les appliquer à différentes relations physiques.

> [!abstract]+ 📚 Prérequis
> **Grandeurs fondamentales et dérivées du S.I.**
>
> - Connaître les grandeurs fondamentales du S.I. et leurs dimensions :
>     longueur $L$, masse $M$, temps $T$.
> - Savoir exprimer la dimension des grandeurs dérivées à partir
>     des dimensions fondamentales.
> - Connaître notamment :
>     \[
>       [v]=L*T^{-1},
>       \qquad
>       [a]=L*T^{-2}.
>     \]
>
> **Calcul dimensionnel**
>
> - **Calcul dimensionnel **
>
>
> - Savoir calculer la dimension d'un produit ou d'un quotient
>       de grandeurs.
> - Savoir utiliser les puissances d'une grandeur dans une
>       expression dimensionnelle.
> - Savoir reconnaître une grandeur sans dimension.
> - **Opérations sur les grandeurs physiques **
>
>
> - Savoir que l'addition et la soustraction ne sont possibles
>       qu'entre grandeurs de même dimension.
> - Savoir que les dimensions se multiplient lors d'un produit
>       et se divisent lors d'un quotient.


> [!info]+ 🎯 Objectifs
> - **Vérification de l'homogénéité ** 
>
> - Savoir déterminer si une équation physique est homogène en comparant les dimensions de ses différents termes et de ses deux membres.
> - Savoir identifier rapidement une relation nécessairement fausse lorsqu'elle n'est pas homogène.
> - **Détermination de la dimension d'une constante ** 
>
> - Savoir retrouver la dimension d'une constante ou d'un paramètre physique à partir d'une relation connue.
> - Savoir isoler dimensionnellement une grandeur inconnue à partir d'une équation physique.
> - **Fonctions mathématiques ** 
>
> - Savoir que les arguments des fonctions trigonométriques, exponentielles et logarithmiques doivent être sans dimension.
> - Savoir déterminer les dimensions des grandeurs intervenant dans l'argument d'une fonction mathématique.
> - **Utilisation de l'analyse dimensionnelle ** 
>
> - Utiliser l'analyse dimensionnelle comme outil de contrôle rapide d'une relation physique.
> - Comprendre qu'une relation homogène n'est pas nécessairement vraie, mais qu'une relation non homogène ne peut pas être correcte.


> [!note]+ 📖 Point de cours
> **Principe d'homogénéité**
>
> Une relation physique doit être homogène : tous les termes qui sont
> additionnés ou soustraits doivent avoir la même dimension et les deux
> membres d'une équation doivent avoir la même dimension.
>
> **Règles de calcul dimensionnel**
>
> - Pour un produit :
>     \[
>       [AB]=[A][B].
>     \]
> - Pour un quotient :
>     \[
>       \left[\frac{A}{B}\right]=\frac{[A]}{[B]}.
>     \]
> - Pour une puissance :
>     \[
>       [A^n]=[A]^n.
>     \]
> - Pour une somme ou une différence, les termes doivent avoir
>     la même dimension.
>
> **Grandeurs sans dimension $\&$ Fonctions mathématiques**
>
> - **Grandeurs sans dimension **
>
>
> - Une grandeur sans dimension possède une dimension égale à $1$..
> - Les constantes numériques pures sont sans dimension et ne modifient pas la dimension d'une expression.
> - **Fonctions mathématiques**
>
>
> - Les fonctions $\exp$, $\cos$, $\sin$ et $\ln$ prennent un argument sans dimension. Ainsi, si $f(x)$ désigne l'une de ces fonctions, l'argument $x$ doit vérifier :
>       \[
>         [x]=1.
>       \]
>
> **Dérivation**
>
> Pour une grandeur $f$ dépendant d'une variable $x$, la dimension
> de la dérivée est donnée par :
> \[
>   \left[\frac{df}{dx}\right]=\frac{[f]}{[x]}.
> \]


**q1_intro.** **Notions de cours S.I.** 
%Répondre aux questions de cours relatives à l'homogénéité
%(a) Définir une équation homogène. (b) Une équation homogène est-elle forcément vraie ? (c) Une équation non homogène peut-elle être vraie ? (d) Quelles sont les règles d'addition/soustraction ? (e) De multiplication/division ? (f) Quelle est la dimension d'une dérivée df/dx ? (g) Quelle est la dimension des fonctions transcendentales (exp, cos, ln) et de leurs arguments ?


(a) Définir la notion d’homogénéité.

(b) Une équation homogène est elle nécessairement vraie ?

(c) Une équation non homogène est elle nécessairement fausse ?

(d) Dans quels cas, peut on additionner/soustraire des grandeurs entre elles ?

(e) Dans quels cas, peut on multiplier/diviser des grandeurs entre elles ?

(f) Quelle est la dimension de la dérivée d’une grandeur par rapport à une variable ?

(g) Que peut on dire de la dimension des fonctions mathématiques $\exp(x)$ , $\cos(x)$ , $\ln(x)$ ? Et de leur argument ?

> [!example]- 📝 Solution détaillée
> (a) Une équation est homogène si tous ses termes ont la même dimension.
>
> (b) Non, elle peut être physiquement fausse à cause d'un facteur numérique.
>
> (c) Oui, une équation non homogène est toujours fausse.
>
> (d) On ne peut additionner que des grandeurs de même dimension.
>
> (e) On peut multiplier ou diviser des grandeurs de dimensions différentes.
>
> (f) $[df/dx] = [f] / [x]$.
>
> (g) Les fonctions transcendentales et leurs arguments sont adimensionnels $([f] = 1, [x] = 1)$.


**q2.** **L’analyse dimensionnelle pour vérifier l’homogénéité.**\\



(a) Soit $x$, la coordonnée donnant la position d’un mobile sur un axe, $v$ sa vitesse et $a$ son accélération, vérifier si les équations suivantes sont homogènes :
    $$
      x = a t,\quad  x = \frac{1}2 a t^2 + vt, \quad \text{et }  x = \frac{v^2}{2 a}.
    $$

(b) La vitesse $v$ d’une particule varie avec le temps $t$ selon : $v= At+ Bt^2$.
    Quelles sont les dimensions des constantes $A$ et $B$ ?

(c) La position $x$ d’une particule varie avec le temps $t$ selon : $x= R cos(\omega t+ \varphi )$. \\
    Quelles sont les dimensions des constantes $R$ , $\omega$  et $\varphi$ ?

(d) Vérifier l’homogénéité de l’énergie potentielle de pesanteur : $\mathcal{E}_p = mgz$.

> [!tip]- 💡 Coup de pouce
> **Vérifier l'homogénéité d'une équation
> **
>
> - Pour qu'une équation soit homogène, les deux membres doivent avoir la **même dimension**.
> - Pour une somme ou une différence, tous les termes doivent également avoir **la même dimension**.
> - Rappeler les dimensions :
>
>
> - $[x]=L$
> - $[v]=L*T^{-1}$
> - $[a]=L*T^{-2}$
> - $[t]=T$
> - Commencer par calculer la dimension de chaque terme du membre de droite, puis la comparer à $[x]$.
>
> **Dimensions des constantes $A$ et $B$
> **
>
> - Dans $v=At+Bt^2$, les deux termes $At$ et $Bt^2$ doivent avoir la **même dimension que $v$**.
> - On a $[v]=L*T^{-1}$.
> - Utiliser :
>
>
> - $[A]=\dfrac{[v]}{[t]}$
> - $[B]=\dfrac{[v]}{[t]^2}$
>
> **Dimensions de $R$, $\omega$ et $\varphi$
> **
>
> - Dans $x=R\cos(\omega t+\varphi)$, commencer par comparer les dimensions de $x$ et de $R$.
> - Une fonction trigonométrique comme $\cos$ prend un argument **sans dimension**.
> - Il faut donc que :
>
>
> - $[\omega t+\varphi]=1$
> - $[\omega t]=1$
> - $[\varphi]=1$
> - En déduire la dimension de $\omega$ à partir de $[\omega][t]=1$.
>
> **Vérifier l'homogénéité de $\mathcal{E}_p=mgz$
> **
>
> - Pour vérifier l'équation, comparer $[\mathcal{E}_p]$ et $[mgz]$.
> - Rappeler les dimensions :
>
>
> - $[m]=M$
> - $[g]=L*T^{-2}$
> - $[z]=L$
> - Calculer ensuite :
>     $$
>       [mgz]=[m][g][z].
>     $$
> - La dimension d'une énergie est :
>     $$
>       [\mathcal{E}]=M*L^2*T^{-2}.
>     $$
> - Comparer les deux résultats pour conclure sur l'homogénéité.


> [!example]- 📝 Solution détaillée
> (a) 1. $x = a t$
>     \vspace{-1cm}
>
>
> - **analyse : ** $[x] = L$ est une longueur  alors que $[a*t] = \overbrace{L*T^{-2}}^{[a]}*\overbrace{T}^{[t]} =  L*T^{-1} = [v]$ est une vitesse
> - **Donc : ** Non-homogène \\
>
>
>       \vspace{-0.5cm}
> 2. ${\displaystyle x = \frac{1}2a t^2 + v t} $ 
>       \vspace{-0.5cm}
>
>
> - **analyse : ** $[x] = L$ est une longueur, $[a*t^2] = \overbrace{L*T^{-2}}^{[a]}*\overbrace{T^2}^{[t^2]} =  L = [x]$ et $v*t = \overbrace{L*T^{-1}}^{[v]}*\overbrace{T}^{[t]} =  L = [x] $
> - **Donc : ** homogène à une longueur \\
> 3. ${\displaystyle x = \frac{v^2}{2a}} $ 
>       \vspace{-0.5cm}
>
>
> - **analyse : ** $[x] = L$ est une longueur, $\left [\frac{v^2}{2*a} \right ] = \frac{\overbrace{(L*T^{-1})^2 }^{[v]^2}}{2 \underbrace{L*T^{-2}}_{[a]} } =  L = [x]$  
>         \vspace{-0.5cm}
> - **Donc : ** homogène à une longueur
>
> (b) $ [v] = L * T^{-1} $  et $v= At+ Bt^2$ donc $\left [ At \right ] = \left [ Bt^2 \right ]  = [v]  = L * T^{-1}  $
>
>
> - ${\displaystyle [A] = \frac{\overbrace{L * T^{-1}}^{[v]} }{ \underbrace{T}_{[t]}}  } = L * T^{-2} = [a]$ une accélération.
> - ${\displaystyle [B] = \frac{\overbrace{L * T^{-1}}^{[v]} }{ \underbrace{T^2}_{[t]^2}}  } = L * T^{-3} $
>
> (c) $L = [x] = R \overbrace{\cos(\underbrace{\omega t + \varphi}_{[1]})}^{[1]}$ 
>
>
> - ${\displaystyle [R] = \frac{\overbrace{L}^{[x]} }{ \underbrace{[1]}_{[\cos(\omega t + \varphi)]}  } = L  = [x] }$ est une longueur.
> - ${\displaystyle [\omega] = \frac{\overbrace{[1]}^{[\omega t + \phi ]} }{ \underbrace{T}_{[t]}  } = T^{-1} }$ est une pulsation.
> - ${\displaystyle [\varphi] = [1] }$ est sans dimesntion
>
> (d) - ${\displaystyle [\mathcal{E}_p] = M * L^2 * T^{-2}] }$ est une énergie.
> - ${\displaystyle [mgz] = \overbrace{M}^{[m]}*\overbrace{L*T^{-2}}^{[g]}* \overbrace{L}^{[z]} = M * L^2 * T^{-2} }$ est une énergie.
>
>
>     donc $\mathcal{E}_p = mgz$ est bien homogène a une énergie


> [!question]- 🔭 Aller plus loin — Lycée : Vérifier des relations physiques simples

> Utiliser l'analyse dimensionnelle pour vérifier les relations
> classiques de mécanique et d'électricité, par exemple
> $v=d/t$, $E_c=\frac12mv^2$ ou $P=UI$.


> [!question]- 🔭 Aller plus loin — CPGE : Retrouver une relation par analyse dimensionnelle

> Utiliser l'analyse dimensionnelle pour déterminer la forme possible
> d'une loi physique à partir des grandeurs dont elle dépend.
> On pourra notamment introduire l'analyse dimensionnelle de lois
> faisant intervenir plusieurs paramètres.


> [!question]- 🔭 Aller plus loin — Licence : Théorème de Vaschy-Buckingham

> Introduire le théorème $\Pi$ de Vaschy-Buckingham et la construction
> de grandeurs sans dimension. Montrer comment cette méthode permet
> de réduire le nombre de paramètres indépendants d'un problème physique.


> [!question]- 🔭 Aller plus loin — Master : Analyse d'échelles et similitude

> Étendre l'analyse dimensionnelle à l'analyse d'échelles, aux lois
> d'échelle et aux nombres sans dimension utilisés en physique
> et en mécanique des fluides, tels que les nombres de Reynolds,
> de Froude ou de Mach.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex1-grandeurs-physiques-fondamentales-dimensions-et-unites-de-base|Exercice 1 — Grandeurs physiques fondamentales : dimensions et unités de base]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex2-grandeurs-derivees-equation-au-dimensions-dimension-et-unites-derivees-composees|Exercice 2 — Grandeurs Dérivées : Équation au dimensions , dimension et unités dérivées (composées)]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex4-lois-et-constantes-fondamentales-en-physiques|Exercice 4 — Lois et Constantes Fondamentales en physiques]] · [[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/grandeurs-physiques-dimensions-unites-et-analyse-dimensionnelle/ex5-l-analyse-dimensionnelle-comme-outil-de-prediction|Exercice 5 — L'analyse dimensionnelle comme outil de prédiction]]

