---
title: "Exercice 1 — Solutions de l'équation de d'Alembert"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td1_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_ex1_coup_de_pouce.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_coup_de_pouce)</a> · <a href="/pdfs/td1_ex1_solution_detaillee.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_solution_detaillee)</a> · <a href="/pdfs/td1_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_PhV212_fiche)</a> · <a href="/pdfs/td1_ex1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_ex1_fiche)</a> · <a href="/pdfs/td1_exs_maison_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_exs_maison_fiche)</a>

### Exercice 1. Solutions de l'équation de d'Alembert

Le déplacement transversal $y(x,t)$ d'une corde est solution de l'équation
de d'Alembert :

$$
\frac{\partial^2 y}{\partial x^2}
=
\frac{1}{c^2}
\frac{\partial^2 y}{\partial t^2},
$$

où $c$ désigne la célérité des ondes transversales se propageant le long
de la corde.

**q1.** Soit $f$ une fonction de classe $\mathcal{C}^2$. Montrer que

$$
y(x,t)=f(x-ct)
$$

est solution de l'équation de d'Alembert.

> [!tip]- 💡 Coup de pouce
> **Changement de variable**
>
> Poser $u=x-ct$. La fonction s'écrit alors $y(x,t)=f(u)$.
> Calculer successivement les dérivées partielles premières puis
> secondes par rapport à $x$ et à $t$ en utilisant la règle de
> dérivation des fonctions composées.
>
> **Attention aux dérivées temporelles**
>
> On a
>
> $$
> \frac{\partial u}{\partial x}=1
> \qquad\text{et}\qquad
> \frac{\partial u}{\partial t}=-c.
> $$
>
> Le facteur $-c$ apparaît donc dans chaque dérivée temporelle.


> [!question]- 🔭 Aller plus loin — Lycée : Fonctions simples
> Tester le résultat avec $f(u) = \sin(u)$ ou $f(u) = e^{-u^2}$.


> [!question]- 🔭 Aller plus loin — Licence : Régularité $\mathcal{C}^2$

> Discuter le besoin de la classe $\mathcal{C}^2$ pour la définition au sens classique des dérivées.


> [!question]- 🔭 Aller plus loin — Master : Solutions faibles
> Si $f$ est seulement continue par morceaux (par exemple une onde créneau), $f(x-ct)$ reste solution de l'équation des ondes au sens des distributions.


> [!success]- ✅ Correction
> **Dérivées spatiales**
>
> En posant $u=x-ct$, on obtient :
>
> $$
> \frac{\partial y}{\partial x}
> =
> f'(u)\frac{\partial u}{\partial x}
> =
> f'(x-ct).
> $$
>
> Par conséquent :
>
> $$
> \frac{\partial^2 y}{\partial x^2}
> =
> f''(x-ct).
> $$
>
> **Dérivées temporelles**
>
> De même :
>
> $$
> \frac{\partial y}{\partial t}
> =
> f'(u)\frac{\partial u}{\partial t}
> =
> -c\,f'(x-ct).
> $$
>
> En dérivant une seconde fois :
>
> $$
> \frac{\partial^2 y}{\partial t^2}
> =
> c^2f''(x-ct).
> $$
>
> **Conclusion**
>
> On a donc :
>
> $$
> \frac{1}{c^2}
> \frac{\partial^2 y}{\partial t^2}
> =
> \frac{1}{c^2}
> c^2f''(x-ct)
> =
> f''(x-ct)
> =
> \frac{\partial^2 y}{\partial x^2}.
> $$
>
> Ainsi $y(x,t)=f(x-ct)$ vérifie bien l'équation de d'Alembert.


> [!example]- 📝 Solution détaillée
> **Démonstration détaillée**
>
> Introduisons la variable intermédiaire :
>
> $$
> u=x-ct.
> $$
>
> La fonction étudiée s'écrit donc $y(x,t)=f(u)$.
>
> Comme $u$ dépend de $x$ et de $t$, les dérivées partielles sont
> obtenues par la règle de dérivation des fonctions composées.
>
> Pour la dérivée spatiale :
>
> $$
> \frac{\partial y}{\partial x}
> =
> f'(u)\frac{\partial u}{\partial x}
> =
> f'(u),
> $$
>
> car $\partial u/\partial x=1$. On obtient alors :
>
> $$
> \frac{\partial^2y}{\partial x^2}
> =
> f''(u)
> =
> f''(x-ct).
> $$
>
> Pour la dérivée temporelle :
>
> $$
> \frac{\partial y}{\partial t}
> =
> f'(u)\frac{\partial u}{\partial t}
> =
> -c\,f'(u),
> $$
>
> puisque $\partial u/\partial t=-c$.
>
> On dérive une seconde fois :
>
> $$
> \frac{\partial^2y}{\partial t^2}
> =
> -c\,f''(u)
> \frac{\partial u}{\partial t}
> =
> c^2f''(u).
> $$
>
> Ainsi :
>
> $$
> \frac{1}{c^2}
> \frac{\partial^2y}{\partial t^2}
> =
> f''(x-ct)
> =
> \frac{\partial^2y}{\partial x^2}.
> $$
>
> La fonction $y(x,t)=f(x-ct)$ est donc bien une solution de
> l'équation de d'Alembert.


**q2.** Soit $g$ une fonction de classe $\mathcal{C}^2$. Montrer que

$$
y(x,t)=g(x+ct)
$$

est également solution de l'équation de d'Alembert.

> [!tip]- 💡 Coup de pouce
> **Même méthode**
>
> Poser cette fois :
>
> $$
> u=x+ct.
> $$
>
> Calculer les dérivées secondes par rapport à $x$ et à $t$.
>
> **Comparaison avec la question précédente**
>
> La seule différence est le signe de $c$ dans la dérivée première
> par rapport au temps. Que devient ce signe après deux dérivations ?


> [!question]- 🔭 Aller plus loin — Lycée : Exemple concret
> Une onde réfléchie sur un obstacle revient vers l'origine : elle est décrite par une fonction du type $g(x+ct)$.


> [!question]- 🔭 Aller plus loin — Licence : Ondes stationnaires
> $g(x+ct)$ permet d'annuler les conditions aux limites (ex: corde fixée à une extrémité).


> [!question]- 🔭 Aller plus loin — Master : Invariance de Lorentz
> L'équation d'onde est invariante sous les transformations de Lorentz, conservant le cône de lumière $x^2 - c^2t^2 = 0$.


> [!success]- ✅ Correction
> **Calcul des dérivées**
>
> Pour $u=x+ct$ :
>
> $$
> \frac{\partial^2y}{\partial x^2}
> =
> g''(x+ct).
> $$
>
> De plus :
>
> $$
> \frac{\partial y}{\partial t}
> =
> c\,g'(x+ct),
> $$
>
> puis :
>
> $$
> \frac{\partial^2y}{\partial t^2}
> =
> c^2g''(x+ct).
> $$
>
> **Conclusion**
>
> Ainsi :
>
> $$
> \frac{1}{c^2}
> \frac{\partial^2y}{\partial t^2}
> =
> g''(x+ct)
> =
> \frac{\partial^2y}{\partial x^2}.
> $$
>
> La fonction $y(x,t)=g(x+ct)$ est donc également solution de
> l'équation de d'Alembert.


> [!example]- 📝 Solution détaillée
> **Démonstration détaillée**
>
> Posons :
>
> $$
> u=x+ct.
> $$
>
> On a alors $y(x,t)=g(u)$.
>
> Pour les dérivées spatiales :
>
> $$
> \frac{\partial y}{\partial x}
> =
> g'(u)\frac{\partial u}{\partial x}
> =
> g'(u),
> $$
>
> puis :
>
> $$
> \frac{\partial^2y}{\partial x^2}
> =
> g''(u)
> =
> g''(x+ct).
> $$
>
> Pour les dérivées temporelles :
>
> $$
> \frac{\partial y}{\partial t}
> =
> g'(u)\frac{\partial u}{\partial t}
> =
> c\,g'(u).
> $$
>
> En dérivant une seconde fois :
>
> $$
> \frac{\partial^2y}{\partial t^2}
> =
> c\,g''(u)
> \frac{\partial u}{\partial t}
> =
> c^2g''(u).
> $$
>
> Il vient donc :
>
> $$
> \frac{1}{c^2}
> \frac{\partial^2y}{\partial t^2}
> =
> g''(x+ct)
> =
> \frac{\partial^2y}{\partial x^2}.
> $$
>
> La fonction $y(x,t)=g(x+ct)$ est donc solution de l'équation
> de d'Alembert.


**q3.** En déduire que toute fonction de la forme

$$
y(x,t)=f(x-ct)+g(x+ct)
$$

est également solution de l'équation de d'Alembert.

> [!tip]- 💡 Coup de pouce
> **Linéarité**
>
> L'équation de d'Alembert est une équation différentielle
> linéaire homogène.
>
> Si deux fonctions sont solutions, étudier ce que deviennent les
> dérivées secondes de leur somme.


> [!question]- 🔭 Aller plus loin — Lycée : Croisement d'ondes
> Deux vagues arrivant en sens inverse se croisent, s'additionnent, puis poursuivent leur chemin sans altération.


> [!question]- 🔭 Aller plus loin — Licence : Analyse spectrale
> Toute solution peut être décomposée en une somme (ou intégrale) de Fourier de fonctions sinusoïdales $\alpha_k e^{i(kx-\omega t)} + \beta_k e^{i(kx+\omega t)}$.


> [!question]- 🔭 Aller plus loin — Master : Croisement de solitones
> Pour des équations non linéaires intégratibles (type KdV), les solitons se croisent avec seulement un déphasage, mimant la linéarité.


> [!success]- ✅ Correction
> **Principe de superposition**
>
> Les fonctions
>
> $$
> y_1(x,t)=f(x-ct)
> $$
>
> et
>
> $$
> y_2(x,t)=g(x+ct)
> $$
>
> sont toutes deux solutions de l'équation de d'Alembert.
>
> Comme les dérivées partielles sont linéaires :
>
> $$
> \frac{\partial^2(y_1+y_2)}{\partial x^2}
> =
> \frac{\partial^2y_1}{\partial x^2}
> +
> \frac{\partial^2y_2}{\partial x^2},
> $$
>
> et :
>
> $$
> \frac{\partial^2(y_1+y_2)}{\partial t^2}
> =
> \frac{\partial^2y_1}{\partial t^2}
> +
> \frac{\partial^2y_2}{\partial t^2}.
> $$
>
> La somme $y=y_1+y_2$ est donc également solution.


> [!example]- 📝 Solution détaillée
> **Principe de superposition**
>
> Posons :
>
> $$
> y_1(x,t)=f(x-ct)
> \qquad\text{et}\qquad
> y_2(x,t)=g(x+ct).
> $$
>
> D'après les deux questions précédentes :
>
> $$
> \frac{\partial^2y_1}{\partial x^2}
> =
> \frac{1}{c^2}
> \frac{\partial^2y_1}{\partial t^2}
> $$
>
> et :
>
> $$
> \frac{\partial^2y_2}{\partial x^2}
> =
> \frac{1}{c^2}
> \frac{\partial^2y_2}{\partial t^2}.
> $$
>
> Pour $y=y_1+y_2$, la linéarité des dérivées donne :
>
> $$
> \frac{\partial^2y}{\partial x^2}
> =
> \frac{\partial^2y_1}{\partial x^2}
> +
> \frac{\partial^2y_2}{\partial x^2}.
> $$
>
> En utilisant les équations vérifiées par $y_1$ et $y_2$ :
>
> $$
> \frac{\partial^2y}{\partial x^2}
> =
> \frac{1}{c^2}
> \left(
> \frac{\partial^2y_1}{\partial t^2}
> +
> \frac{\partial^2y_2}{\partial t^2}
> \right).
> $$
>
> Finalement :
>
> $$
> \boxed{
> \frac{\partial^2y}{\partial x^2}
> =
> \frac{1}{c^2}
> \frac{\partial^2y}{\partial t^2}
> }
> $$
>
> et donc :
>
> $$
> \boxed{
> y(x,t)=f(x-ct)+g(x+ct)
> }
> $$
>
> est une solution de l'équation de d'Alembert.


On rappelle qu'une onde progressive correspond à un profil qui se
déplace sans se déformer.

On suit un point identifiable du profil, par exemple une crête ou un
creux, repéré par une valeur constante de l'argument de la fonction.


**4.**

  **a)** Pour une onde :

$$
y(x,t)=f(x-ct),
$$

on note $(x_1,t_1)$ puis $(x_2,t_2)$, avec $t_2>t_1$, les coordonnées
de ce même point du profil à deux instants différents.

Montrer que :

$$
x_2=x_1+c(t_2-t_1).
$$

Représenter schématiquement le profil de l'onde aux instants $t_1$
et $t_2$ sur un même graphique, en faisant apparaître le déplacement
du point considéré. Conclure quant au sens de propagation de l'onde.

> [!tip]- 💡 Coup de pouce
> **Même point du profil**
>
> Une crête donnée correspond à la même valeur de l'argument de
> la fonction $f$ aux deux instants :
>
> $$
> x_1-ct_1=x_2-ct_2.
> $$
>
> Isoler ensuite $x_2$.
>
> **Interprétation**
>
> Puisque $t_2>t_1$ et $c>0$, comparer $x_2$ et $x_1$.


> [!question]- 🔭 Aller plus loin — Lycée : Sens direct
> Une onde de choc créée à gauche avance vers la droite au cours du temps.


> [!question]- 🔭 Aller plus loin — Licence : Représentation complexe
> Une onde plane $e^{i(kx-\omega t)}$ a pour argument $k(x - \frac{\omega}{k}t)$, ce qui équivaut à $x-ct$ avec $c=\omega/k$.


> [!question]- 🔭 Aller plus loin — Master : Ondes dans l'espace 3D
> L'équivalent 3D est une onde plane progressive $f(\mathbf{k}\cdot\mathbf{r} - \omega t)$ se propageant dans la direction du vecteur d'onde $\mathbf{k}$.


> [!success]- ✅ Correction
> **Position du même point du profil**
>
> Pour suivre exactement le même motif, l'argument de la fonction
> doit rester constant :
>
> $$
> x_1-ct_1=x_2-ct_2.
> $$
>
> On obtient alors :
>
> $$
> x_2=x_1+c(t_2-t_1).
> $$
>
> **Sens de propagation**
>
> Comme $t_2>t_1$ et $c>0$ :
>
> $$
> x_2>x_1.
> $$
>
> Le point suivi se déplace donc vers les valeurs croissantes de
> $x$.
>
> L'onde $f(x-ct)$ se propage dans le sens des $x$ croissants.


> [!example]- 📝 Solution détaillée
> **Suivi d'une crête**
>
> Considérons une crête particulière du profil. Sa position
> correspond à une valeur constante de l'argument de la fonction
> $f$.
>
> À l'instant $t_1$, son argument vaut :
>
> $$
> x_1-ct_1.
> $$
>
> À l'instant $t_2$, ce même point du profil est situé en $x_2$.
> Son argument est donc :
>
> $$
> x_2-ct_2.
> $$
>
> Puisqu'il s'agit du même point du profil :
>
> $$
> x_1-ct_1=x_2-ct_2.
> $$
>
> En isolant $x_2$, on obtient :
>
> $$
> \boxed{
> x_2=x_1+c(t_2-t_1)
> }.
> $$
>
> Le déplacement spatial du motif vaut donc :
>
> $$
> \Delta x=x_2-x_1=c(t_2-t_1).
> $$
>
> Puisque $c>0$ et $t_2-t_1>0$, on a $\Delta x>0$.
>
> Le profil entier est donc translaté vers la droite, c'est-à-dire
> dans le sens des $x$ croissants.
>
> Ainsi :
>
> $$
> \boxed{
> y(x,t)=f(x-ct)
> \quad\text{est une onde se propageant vers les }x\text{ croissants.}
> }
> $$
>
> <p style="text-align:center"><a href="/figures/td1_ex0_onde_x_minus_ct.svg" target="_blank" rel="noopener"><img src="/figures/td1_ex0_onde_x_minus_ct.svg" alt="Translation du profil d'une onde $y(x,t)=f(x-ct)$ entre
> les instants $t_1$ et $t_2$." loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>


  **b)** Reprendre les mêmes questions pour une onde :

$$
y(x,t)=g(x+ct).
$$

Conclure quant au sens de propagation de cette onde.

> [!tip]- 💡 Coup de pouce
> **Argument constant**
>
> Pour suivre le même point du profil :
>
> $$
> x_1+ct_1=x_2+ct_2.
> $$
>
> Isoler $x_2$ et comparer sa valeur à $x_1$.


> [!question]- 🔭 Aller plus loin — Lycée : Sens de propagation
> Retenir la règle pratique :
>
> $$
> f(x-ct)
> $$
>
> correspond à une propagation vers la droite, dans le sens des
> $x$ croissants, tandis que :
>
> $$
> g(x+ct)
> $$
>
> correspond à une propagation vers la gauche, dans le sens des
> $x$ décroissants.


> [!question]- 🔭 Aller plus loin — Licence : Solution générale de d'Alembert
> La solution générale de l'équation de d'Alembert à une dimension
> peut s'écrire :
>
> $$
> y(x,t)=f(x-ct)+g(x+ct).
> $$
>
> Elle correspond à la superposition de deux ondes progressives se
> propageant en sens opposés.


> [!question]- 🔭 Aller plus loin — Master : Lien avec les coordonnées caractéristiques
> Introduire les coordonnées caractéristiques :
>
> $$
> \xi=x-ct,
> \qquad
> \eta=x+ct.
> $$
>
> Dans ces coordonnées, l'opérateur d'onde se factorise :
>
> $$
> \frac{\partial^2}{\partial x^2}
> -
> \frac{1}{c^2}
> \frac{\partial^2}{\partial t^2}
> =
> 4
> \frac{\partial^2}{\partial\xi\partial\eta}.
> $$
>
> Les fonctions $f(\xi)$ et $g(\eta)$ sont alors directement
> identifiées comme les deux familles d'ondes se propageant dans
> les directions opposées.


> [!success]- ✅ Correction
> **Position du même point du profil**
>
> Le même motif est caractérisé par une valeur constante de
> l'argument :
>
> $$
> x_1+ct_1=x_2+ct_2.
> $$
>
> On obtient :
>
> $$
> x_2=x_1-c(t_2-t_1).
> $$
>
> **Sens de propagation**
>
> Puisque $t_2>t_1$ et $c>0$ :
>
> $$
> x_2<x_1.
> $$
>
> Le point du profil se déplace donc vers les valeurs décroissantes
> de $x$.
>
> L'onde $g(x+ct)$ se propage dans le sens des $x$ décroissants.


> [!example]- 📝 Solution détaillée
> **Suivi d'un motif**
>
> Pour suivre un même point identifiable du profil, l'argument de
> la fonction $g$ doit rester constant.
>
> On écrit donc :
>
> $$
> x_1+ct_1=x_2+ct_2.
> $$
>
> En isolant $x_2$ :
>
> $$
> x_2=x_1-c(t_2-t_1).
> $$
>
> Le déplacement du motif vaut ainsi :
>
> $$
> \Delta x=x_2-x_1=-c(t_2-t_1).
> $$
>
> Comme $t_2>t_1$ et $c>0$, on a :
>
> $$
> \Delta x<0.
> $$
>
> Le profil se déplace donc vers les valeurs décroissantes de $x$.
>
> Ainsi :
>
> $$
> \boxed{
> y(x,t)=g(x+ct)
> \quad\text{est une onde se propageant vers les }x\text{ décroissants.}
> }
> $$
>
> <p style="text-align:center"><a href="/figures/td1_ex0_onde_x_plus_ct.svg" target="_blank" rel="noopener"><img src="/figures/td1_ex0_onde_x_plus_ct.svg" alt="Translation du profil d'une onde $y(x,t)=g(x+ct)$ entre
> les instants $t_1$ et $t_2$." loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>

