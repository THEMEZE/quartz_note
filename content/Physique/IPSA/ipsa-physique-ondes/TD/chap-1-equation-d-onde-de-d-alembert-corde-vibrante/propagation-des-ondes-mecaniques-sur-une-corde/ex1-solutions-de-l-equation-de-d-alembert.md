---
title: "Exercice 1 — Solutions de l'équation de d'Alembert"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td1_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_ex1_coup_de_pouce.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_coup_de_pouce)</a> · <a href="/pdfs/td1_ex1_solution_detaillee.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_solution_detaillee)</a>

### Exercice 1. Solutions de l'équation de d'Alembert

*⭐ Indispensable · Difficulté ●●○○○ · ⏱ 40 min · Type : Application directe du cours*

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

> [!question]+ 🎣 Accroche
> **Une forme qui avance sans se déformer**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *Quand une secousse remonte le long d'une corde, la « bosse » avance sans changer de forme. Comment une simple fonction $f$ de la variable $x-ct$ peut-elle décrire cela ? Et pourquoi le signe « moins » correspond-il à un déplacement vers la **droite** et non vers la gauche ?*
>
> **Idée clé : une onde progressive est un profil qui se translate à la vitesse $c$.** Toute fonction de la forme $f(x-ct)$ ou $g(x+ct)$ est solution de l'équation de d'Alembert, et, l'équation étant **linéaire**, la somme $f(x-ct)+g(x+ct)$ aussi. Pour savoir où va l'onde, on **suit un point du profil** : son argument reste constant, donc $x-ct=\text{cte}$ donne $x=x_0+ct$, c'est-à-dire une propagation vers les $x$ croissants.


> [!abstract]+ 📚 Prérequis
> **Dérivées partielles et composition**
>
> Savoir dériver une fonction composée à plusieurs variables par la règle
> de la chaîne (**chain rule**). Connaître la définition d'une onde progressive
> et de sa célérité $c$.


> [!info]+ 🎯 Objectifs
> **Vérification formelle et sens de propagation**
>
> - Vérifier mathématiquement qu'une fonction de la forme $f(x \mp ct)$ est solution de l'équation de d'Alembert.
> - Associer le signe devant le terme $ct$ au sens de propagation de l'onde progressive.
> - Utiliser la propriété de linéarité de l'équation d'onde.


> [!note]+ 📖 Point de cours
> **Équation de d'Alembert à 1D**
>
> Toute fonction de classe $\mathcal{C}^2$ de la forme $y(x,t) = f(x-ct) + g(x+ct)$ est solution de l'équation d'onde 1D.\\
>
> La fonction $f(x-ct)$ représente une onde progressive se déplaçant vers les $x$ croissants à la vitesse $c$, tandis que
> $g(x+ct)$ représente une onde se déplaçant vers les $x$ décroissants.


> [!note]- 🧮 Outils mathématiques
> **Dérivée partielle et fonction composée**
>
> Pour $y(x,t)=f(u)$ avec $u=x-ct$ : $\dfrac{\partial y}{\partial x}=f'(u)\dfrac{\partial u}{\partial x}=f'(u)$ et $\dfrac{\partial y}{\partial t}=f'(u)\dfrac{\partial u}{\partial t}=-c\,f'(u)$. Dériver deux fois fait apparaître le facteur $c^2$ : le signe de $c$ disparaît au carré.
>
> **Translation d'un graphe**
>
> Le graphe de $x\mapsto f(x-x_0)$ est celui de $f$ **décalé de $x_0$ vers la droite**. Ici $x_0=ct$ augmente avec le temps : le profil glisse vers la droite sans se déformer.
>
> **Argument constant et loi horaire**
>
> $x-ct=\text{cte}\Rightarrow x(t)=x_0+ct$ : c'est la loi horaire d'un mobile en mouvement rectiligne uniforme de vitesse $c$ (cinématique). Dériver par rapport à $t$ donne directement $\dfrac{\mathrm dx}{\mathrm dt}=+c$.
>
> **Linéarité de la dérivation**
>
> $\dfrac{\partial^2}{\partial x^2}(y_1+y_2)=\dfrac{\partial^2 y_1}{\partial x^2}+\dfrac{\partial^2 y_2}{\partial x^2}$ : toute combinaison linéaire de solutions d'une équation linéaire homogène est solution (espace vectoriel des solutions).
>
> **Coordonnées caractéristiques**
>
> Avec $\xi=x-ct$ et $\eta=x+ct$ : $\partial_x=\partial_\xi+\partial_\eta$ et $\partial_t=c\,(\partial_\eta-\partial_\xi)$, d'où $\partial_x^2-\dfrac1{c^2}\partial_t^2=4\,\partial_\xi\partial_\eta$. L'équation devient $\partial_\xi\partial_\eta y=0$, qui s'intègre en $y=f(\xi)+g(\eta)$.
>
> **Lien avec les sinusoïdes**
>
> $\cos(kx-\omega t)=\cos\!\big(k(x-\tfrac\omega kt)\big)$ est du type $f(x-ct)$ avec $c=\omega/k$ : les ondes sinusoïdales sont des cas particuliers d'ondes progressives.


**q1.** Soit $f$ une fonction de classe $\mathcal{C}^2$. Montrer que

$$
y(x,t)=f(x-ct)
$$

est solution de l'équation de d'Alembert.

> [!abstract]+ 📚 Prérequis
> **Dérivation de fonction composée**
>
> Règle de dérivation : si $u(x,t) = x - ct$, alors $\frac{\partial}{\partial x} f(u) = \frac{\partial u}{\partial x} f'(u)$.


> [!info]+ 🎯 Objectifs
> **Calcul des dérivées partielles secondes**
>
> Savoir dériver deux fois par rapport à $x$ et par rapport à $t$ une fonction dépendante de $x-ct$.


> [!note]+ 📖 Point de cours
> **Onde progressive se propageant à la célérité c**
>
> Toute fonction $f(x-ct)$ vérifie algébriquement $\frac{\partial^2 y}{\partial x^2} = \frac{1}{c^2} \frac{\partial^2 y}{\partial t^2}$.


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


> [!question]- 🔭 Aller plus loin — CPGE : Équation aux dérivées partielles
> Remarquer que $f$ n'a pas besoin d'être sinusoïdale : elle peut représenter un paquet d'onde ou une impulsion quelconque.


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

> [!abstract]+ 📚 Prérequis
> **Dérivation de fonction composée**
>
> Utilisation du changement de variable $v = x+ct$.


> [!info]+ 🎯 Objectifs
> **Calcul analogue avec changement de signe**
>
> Observer l'effet du signe positif devant le terme $ct$ lors de la première et de la seconde dérivation.


> [!note]+ 📖 Point de cours
> **Onde rétrograde**
>
> La fonction $g(x+ct)$ est une solution de d'Alembert associée à une propagation en sens inverse.


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


> [!question]- 🔭 Aller plus loin — CPGE : Invariance par réflexion
> C'est la parité spatio-temporelle de l'opérateur $\square = \frac{\partial^2}{\partial x^2} - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}$ qui garantit cette double possibilité.


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

> [!abstract]+ 📚 Prérequis
> **Linéarité de la dérivation**
>
> Propriété de l'opérateur dérivée : $\frac{\partial}{\partial x}(u+v) = \frac{\partial u}{\partial x} + \frac{\partial v}{\partial x}$.


> [!info]+ 🎯 Objectifs
> **Principe de superposition**
>
> Comprendre et appliquer le principe de superposition pour une équation différentielle linéaire et homogène.


> [!note]+ 📖 Point de cours
> **Principe de superposition**
>
> Toute combinaison linéaire de solutions d'une équation linéaire homogène est encore une solution.


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


> [!question]- 🔭 Aller plus loin — CPGE : Linéarité de l'équation de d'Alembert
> L'équation de d'Alembert pour une onde se propageant dans un milieu
> homogène s'écrit
> \[
>   \frac{\partial^2 y}{\partial t^2}
>   -
>   c^2\frac{\partial^2 y}{\partial x^2}
>   =0.
> \]
> On peut introduire l'opérateur d'onde
> \[
>   \mathcal{D}
>   =
>   \frac{\partial^2}{\partial t^2}
>   -
>   c^2\frac{\partial^2}{\partial x^2}.
> \]
> Cet opérateur est **linéaire** : pour deux fonctions $y_1$ et
> $y_2$ et deux constantes $\alpha$ et $\beta$,
> \[
>   \mathcal{D}(\alpha y_1+\beta y_2)
>   =
>   \alpha\mathcal{D}(y_1)
>   +
>   \beta\mathcal{D}(y_2).
> \]
> Ainsi, si $y_1$ et $y_2$ sont deux solutions de l'équation de
> d'Alembert, alors
> \[
>   y=\alpha y_1+\beta y_2
> \]
> est également une solution. C'est la base mathématique du
> **principe de superposition** des ondes.
>
> En revanche, si l'équation comportait un terme non linéaire, par
> exemple
> \[
>   \frac{\partial^2 y}{\partial t^2}
>   -
>   c^2\frac{\partial^2 y}{\partial x^2}
>   +\lambda y^2=0,
> \]
> l'opérateur associé ne serait plus linéaire et le principe de
> superposition ne serait plus valable en général.
>
> **À retenir :** la superposition des ondes n'est pas une
> propriété indépendante de l'équation : elle découle directement de
> la linéarité de l'équation de propagation.


> [!question]- 🔭 Aller plus loin — CPGE : Équations non linéaires
> Si l'équation contenait des termes non linéaires (ex: $y^2$), le principe de superposition ne s'appliquerait plus.


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

> [!abstract]+ 📚 Prérequis
> **Maniement des inégalités**
>
> Si $t_2 > t_1$ et $c > 0$, alors $c(t_2-t_1) > 0$.


> [!info]+ 🎯 Objectifs
> **Démonstration du sens de propagation**
>
> Établir formellement que $f(x-ct)$ se propage vers les $x$ croissants.


> [!note]+ 📖 Point de cours
> **Onde progressive dans le sens direct**
>
> L'expression $f(x-ct)$ décrit une onde progressive se propageant dans le sens des $x$ croissants à la célérité $c$.


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


> [!question]- 🔭 Aller plus loin — CPGE : Dérivation temporelle du suivi
> En dérivant $x(t) - ct = \text{Cte}$ par rapport à $t$, on obtient directement la vitesse de la crête $\frac{\mathrm{d}x}{\mathrm{d}t} = +c > 0$.


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

> [!abstract]+ 📚 Prérequis
> **Raisonnements de la question 4a**
>
> Maniement de l'argument de phase constant.


> [!info]+ 🎯 Objectifs
> **Démonstration de la propagation rétrograde**
>
> Établir formellement que $g(x+ct)$ se propage vers les $x$ décroissants.


> [!note]+ 📖 Point de cours
> **Onde progressive rétrograde**
>
> L'expression $g(x+ct)$ décrit une onde progressive se propageant dans le sens des $x$ décroissants à la célérité $c$.


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


> [!question]- 🔭 Aller plus loin — CPGE : Vitesse de phase
> Pour une onde sinusoïdale :
>
> $$
> y(x,t)=A\cos(kx-\omega t+\phi),
> $$
>
> une surface de phase constante vérifie :
>
> $$
> kx-\omega t=\text{constante}.
> $$
>
> On retrouve ainsi une vitesse de propagation :
>
> $$
> v_\varphi=\frac{\omega}{k}=c.
> $$


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


> [!note]- 🔗 Liens avec d'autres disciplines
> **Cinématique**
>
> Une crête est un « mobile » : sa position $x=x_0+ct$ est une loi horaire de mouvement rectiligne uniforme. Aucune matière ne se déplace avec elle : la corde, elle, ne fait que monter et descendre.
>
> **Mathématiques**
>
> Équations aux dérivées partielles, changement de variables, espaces vectoriels de solutions. La solution générale $f(x-ct)+g(x+ct)$ est l'analogue de la solution générale d'une EDO linéaire du second ordre (deux fonctions arbitraires au lieu de deux constantes).
>
> **Électromagnétisme et optique**
>
> Les champs $E$ et $B$ dans le vide vérifient la même équation avec $c=1/\sqrt{\varepsilon_0\mu_0}\approx3\times10^8$ m/s : la lumière est une onde progressive.
>
> **Océanographie et géophysique**
>
> Tsunamis et ondes sismiques se propagent comme des profils qui se translatent : mesurer le retard entre deux stations donne la célérité et localise la source.
>
> **Relativité**
>
> Les droites $x=\pm ct$ sont les **caractéristiques** de l'équation : ce sont aussi les trajectoires de la lumière dans un diagramme d'espace-temps (cône de lumière).


> [!question]- 🔭 Aller plus loin — Lycée : Retard temporel
> En physique au lycée, l'onde se propageant vers la droite s'écrit souvent $y(x,t) = s(t - \tau)$
> avec $\tau = x/c$ le retard à l'origine. On remarque que $t - x/c = -\frac{1}{c}(x - ct)$,
> ce qui est bien une fonction de $x-ct$.


> [!question]- 🔭 Aller plus loin — CPGE : Superposition et ondes stationnaires
> La superposition de deux ondes identiques se propageant en sens opposés $f(x-ct) + f(x+ct)$
> peut conduire, dans le cas d'ondes sinusoïdales, à une onde stationnaire de la forme
> $A \cos(kx) \cos(\omega t)$ où la dépendance spatiale et la dépendance temporelle sont séparées.


> [!question]- 🔭 Aller plus loin — Licence : Lien avec la méthode des caractéristiques
> En introduisant les variables $\xi = x-ct$ et $\eta = x+ct$, l'équation de d'Alembert
> se réduit à $\frac{\partial^2 y}{\partial \xi \partial \eta} = 0$, dont l'intégration
> directe fournit la forme $y(\xi,\eta) = f(\xi) + g(\eta)$.


> [!question]- 🔭 Aller plus loin — Master : Lien avec les coordonnées caractéristiques et la notation covariante
> Introduire les coordonnées caractéristiques :
> \[
>   \xi=x-ct,
>   \qquad
>   \eta=x+ct.
> \]
>
> Dans ces coordonnées, l'opérateur d'onde se factorise :
> \[
>   \frac{\partial^2}{\partial x^2}
>   -
>   \frac{1}{c^2}
>   \frac{\partial^2}{\partial t^2}
>   =
>   4
>   \frac{\partial^2}{\partial\xi\,\partial\eta}.
> \]
>
> Les fonctions $f(\xi)$ et $g(\eta)$ sont alors directement
> identifiées comme les deux familles d'ondes se propageant dans
> les directions opposées.
>
>
>
>
> **Ouverture vers la notation covariante.**
>
> En relativité, les coordonnées d'espace et de temps peuvent être
> regroupées dans un quadrivecteur
> \[
>   x^\mu=(ct,x,y,z).
> \]
> On introduit alors la dérivée covariante
> \[
>   \partial_\mu
>   \equiv
>   \frac{\partial}{\partial x^\mu}.
> \]
> Avec la convention de signature
> \[
>   \eta_{\mu\nu}=\operatorname{diag}(1,-1,-1,-1),
> \]
> on obtient
> \[
>   \partial_\mu
>   =
>   \left(
>     \frac{1}{c}\frac{\partial}{\partial t},
>     \frac{\partial}{\partial x},
>     \frac{\partial}{\partial y},
>     \frac{\partial}{\partial z}
>   \right).
> \]
>
> La dérivée à indice contravariant est obtenue en relevant l'indice
> avec la métrique :
> \[
>   \partial^\mu
>   =
>   \eta^{\mu\nu}\partial_\nu.
> \]
> Ainsi,
> \[
>   \partial^\mu
>   =
>   \left(
>     \frac{1}{c}\frac{\partial}{\partial t},
>     -\frac{\partial}{\partial x},
>     -\frac{\partial}{\partial y},
>     -\frac{\partial}{\partial z}
>   \right).
> \]
>
> La contraction des deux dérivées donne alors l'opérateur
> de d'Alembert :
> \[
>   \boxed{
>   \partial_\mu\partial^\mu
>   =
>   \frac{1}{c^2}\frac{\partial^2}{\partial t^2}
>   -
>   \nabla^2
>   }.
> \]
>
> L'équation d'onde dans le vide,
> \[
>   \frac{1}{c^2}\frac{\partial^2\psi}{\partial t^2}
>   -
>   \nabla^2\psi
>   =0,
> \]
> peut donc s'écrire de manière compacte
> \[
>   \boxed{\partial_\mu\partial^\mu\psi=0}.
> \]
>
> Dans le cas unidimensionnel,
> \[
>   \partial_\mu\partial^\mu
>   =
>   \frac{1}{c^2}\frac{\partial^2}{\partial t^2}
>   -
>   \frac{\partial^2}{\partial x^2},
> \]
> qui est, à un signe près selon la convention choisie pour
> l'opérateur d'onde, l'opérateur rencontré précédemment.
>
>
>
>
> **Point important :** la distinction entre $\partial_\mu$
> et $\partial^\mu$ ne signifie pas qu'il s'agit de deux dérivées
> différentes. L'indice est simplement abaissé ou relevé à l'aide
> de la métrique :
> \[
>   \partial^\mu=\eta^{\mu\nu}\partial_\nu.
> \]
> Cette notation permet d'écrire les équations relativistes sous une
> forme indépendante du choix particulier des coordonnées.


> [!question]- 🔭 Aller plus loin — Master : Solutions fondamentales et fonction de Green
> La formule de d'Alembert permet d'exprimer la solution du problème de Cauchy pour l'équation
> des ondes avec conditions initiales $y(x,0) = y_0(x)$ et $\frac{\partial y}{\partial t}(x,0) = v_0(x)$ :
> $y(x,t) = \frac{1}{2}[y_0(x-ct) + y_0(x+ct)] + \frac{1}{2c} \int_{x-ct}^{x+ct} v_0(s) \, \mathrm{d}s$.

