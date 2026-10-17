---
title: "Exercice 5 — Fonction porte : indexation booléenne Numpy"
tags:
  - td
  - outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci
---

[[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/index|⬅ Retour]] · <a href="/pdfs/td2_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 5. Fonction porte : indexation booléenne Numpy

1. Créer une fonction \texttt{porte} qui renvoie un vecteur de booléens
   à partir d'un vecteur \texttt{v\_in} : vrai si \texttt{v\_in} est
   compris entre \texttt{min} et \texttt{max}, faux sinon.
   \texttt{v\_in}, \texttt{min} et \texttt{max} sont des paramètres. \\
2. Tester cette fonction.

**q1.** Écrire \texttt{porte(v\_in, v\_min, v\_max)} et la tester sur
\texttt{v\_in = np.linspace(-5, 5, 11)} avec \texttt{v\_min=-2},
\texttt{v\_max=3}.

> [!tip]- 💡 Coup de pouce
> Combinez deux comparaisons Numpy avec l'opérateur bit à bit adapté,
> en parenthésant chaque comparaison.


> [!success]- ✅ Correction
> \texttt{return (v\_in >= v\_min) \& (v\_in <= v\_max)}


> [!example]- 📝 Solution détaillée
> **Implémentation et test**
>
> \texttt{porte(v\_in, -2, 3)} renvoie \texttt{True} pour les
> éléments de $-2$ à $3$ inclus, \texttt{False} ailleurs. On peut
> récupérer directement les valeurs concernées avec
> \texttt{v\_in[porte(v\_in, -2, 3)]} (indexation booléenne).


**q2.** Que se passe-t-il si l'on utilise \texttt{and} au lieu de
\texttt{\&} ? Pourquoi cette erreur n'apparaît-elle pas avec un seul
flottant ?

> [!tip]- 💡 Coup de pouce
> \texttt{and} exige de convertir chaque opérande en un seul booléen.


> [!success]- ✅ Correction
> ValueError : ambiguïté de la valeur de vérité d'un tableau de plusieurs éléments.


> [!example]- 📝 Solution détaillée
> **Explication**
>
> \texttt{and} tente de convertir chacun de ses deux opérandes en
> un unique \texttt{bool} Python. Pour un seul flottant, la
> comparaison renvoie un unique booléen, sans ambiguïté. Pour un
> tableau Numpy de plusieurs éléments, la comparaison renvoie un
> tableau de plusieurs booléens : Python ne sait pas lequel choisir
> pour représenter « la » valeur de vérité de tout le tableau, d'où
> l'exception \texttt{ValueError}.


**q3.** Comment écrire l'inverse de la fonction porte (vrai en dehors de
l'intervalle) ?

> [!tip]- 💡 Coup de pouce
> L'opérateur \texttt{\textasciitilde} inverse un tableau de
> booléens.


> [!success]- ✅ Correction
> \texttt{\textasciitilde{}porte(v\_in, v\_min, v\_max)}, ou \texttt{(v\_in < v\_min) | (v\_in > v\_max)}.


> [!example]- 📝 Solution détaillée
> **Deux écritures équivalentes**
>
> On peut soit inverser le résultat de \texttt{porte} avec
> \texttt{\textasciitilde porte(v\_in, v\_min, v\_max)}, soit
> écrire directement la condition complémentaire :
> \texttt{(v\_in < v\_min) | (v\_in > v\_max)}. Les deux
> expressions sont équivalentes par les lois de De Morgan.


> [!note] 🔗 Voir aussi
> [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex3-generation-d-un-vecteur-avec-numpy-vectorisation|Exercice 3 — Génération d'un vecteur avec Numpy : vectorisation]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex4-generation-de-signaux-et-affichage-avec-matplotlib|Exercice 4 — Génération de signaux et affichage avec matplotlib]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex7-equation-du-second-degre-reels-puis-complexes|Exercice 7 — Équation du second degré : réels puis complexes]]

