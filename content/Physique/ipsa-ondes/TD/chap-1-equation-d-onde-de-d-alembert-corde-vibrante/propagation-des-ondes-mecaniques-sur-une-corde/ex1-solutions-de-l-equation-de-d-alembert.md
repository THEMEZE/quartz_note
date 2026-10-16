---
title: "Exercice 1 — Solutions de l'équation de d'Alembert"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a>

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

