---
title: "Exercice 2 — Recherche dichotomique récursive (\\texttt{binary\\_search})"
tags:
  - td
  - bloc-intro-methodes-numeriques-onip-semestre-5
---

[[physique/IOGS/iogs-onip/TD/bloc-intro-methodes-numeriques-onip-semestre-5/intro-prise-en-main-de-pycharm-debogage-et-bonnes-pratiques-python/index|⬅ Retour]] · <a href="/pdfs/td1_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 2. Recherche dichotomique récursive (\texttt{binary\_search})

On fournit \texttt{binary\_search0.py}, une recherche dichotomique
récursive dans une liste triée qui renvoie un résultat *faux sans
planter* : elle affiche que 10 n'est pas présent dans la liste
\texttt{[2, 3, 4, 10, 40]}, alors qu'il est bien à l'indice 3. Il faut
localiser le bug avec le débogueur, le corriger, puis améliorer la
lisibilité du code (noms, docstring, annotations de type).

**q1.** Exécuter \texttt{binary\_search0.py}. Le résultat affiché
(\texttt{"10 is not present in list"}) est-il correct ? Utiliser le
débogueur pour identifier précisément où le raisonnement échoue.

> [!tip]- 💡 Coup de pouce
> Posez un point d'arrêt sur la ligne de calcul de \texttt{mid} et
> observez \texttt{arr[mid]} comparé à \texttt{x} à chaque appel.


> [!success]- ✅ Correction
> Les branches elif/else de la récursion sont inversées.


> [!example]- 📝 Solution détaillée
> **Diagnostic**
>
> Le résultat est faux : 10 est présent à l'indice 3. En suivant
> l'exécution, on constate qu'à l'appel 1, \texttt{arr[mid]=4} est
> plus petit que la cible \texttt{10}, ce qui devrait orienter la
> recherche vers la *droite* (indices 3 à 4) ; or le code
> appelle \texttt{binary\_search(arr, low, mid-1, x)}, c'est-à-dire
> la partie *gauche*. Les deux branches récursives sont
> inverties.


**q2.** Corriger le bug, puis vérifier le résultat sur les cas de test :
cible 10 (attendu : indice 3), cible 2 (indice 0), cible 40 (indice
4), cible 5 (absente, -1), liste vide (-1), liste à un seul élément.

> [!tip]- 💡 Coup de pouce
> Dans la branche \texttt{arr[mid] < x}, il faut appeler
> \texttt{binary\_search(arr, mid + 1, high, x)}.


> [!success]- ✅ Correction
> Échanger les deux appels récursifs des branches elif et else.


> [!example]- 📝 Solution détaillée
> **Correction et validation**
>
> Après échange des deux appels récursifs, tous les cas de test
> suivants sont vérifiés :
>
> \begin{center}
> \begin{tabular}{lcc}
> \hline
> Liste & Cible & Résultat attendu \\
> \hline
> \texttt{[2,3,4,10,40]} & 10 & 3 \\
> \texttt{[2,3,4,10,40]} & 2 & 0 \\
> \texttt{[2,3,4,10,40]} & 40 & 4 \\
> \texttt{[2,3,4,10,40]} & 5 & -1 \\
> \texttt{[]} & 1 & -1 \\
> \texttt{[7]} & 7 & 0 \\
> \hline
> \end{tabular}
> \end{center}


**q3.** Pourquoi la liste doit-elle impérativement être triée pour que
l'algorithme fonctionne ? Combien de comparaisons au maximum sont
nécessaires pour une liste de 1 000 000 d'éléments ?

> [!tip]- 💡 Coup de pouce
> À chaque appel récursif, la zone de recherche est divisée par deux.


> [!success]- ✅ Correction
> Environ log2(1 000 000) $\approx$ 20 comparaisons au maximum.


> [!example]- 📝 Solution détaillée
> **Rôle du tri et complexité**
>
> L'algorithme décide de quel côté chercher en comparant la cible
> à \texttt{arr[mid]} : ce raisonnement n'est valable que si la
> liste est triée (sinon la cible pourrait très bien se trouver du
> « mauvais » côté sans que l'algorithme ne le sache). Comme la
> zone de recherche est divisée par 2 à chaque appel, il faut au
> maximum $\lceil \log_2(n) \rceil$ comparaisons, soit environ 20
> pour $n = 1\,000\,000$ — une complexité logarithmique bien plus
> favorable qu'une recherche linéaire en $O(n)$.


> [!note] 🔗 Voir aussi
> [[physique/IOGS/iogs-onip/TD/bloc-intro-methodes-numeriques-onip-semestre-5/intro-prise-en-main-de-pycharm-debogage-et-bonnes-pratiques-python/ex3-tri-a-bulles-texttt-bubble-sort-et-mutation-en-place|Exercice 3 — Tri à bulles (\texttt{bubble\_sort}) et mutation en place]] · [[physique/IOGS/iogs-onip/TD/bloc-intro-methodes-numeriques-onip-semestre-5/intro-prise-en-main-de-pycharm-debogage-et-bonnes-pratiques-python/ex6-somme-des-elements-d-une-liste-mauvais-argument-d-appel|Exercice 6 — Somme des éléments d'une liste : mauvais argument d'appel]]

