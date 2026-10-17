---
title: "Exercice 3 — Tri à bulles (\\texttt{bubble\\_sort}) et mutation en place"
tags:
  - td
  - bloc-intro-methodes-numeriques-onip-semestre-5
---

[[physique/IOGS/iogs-onip/TD/bloc-intro-methodes-numeriques-onip-semestre-5/intro-prise-en-main-de-pycharm-debogage-et-bonnes-pratiques-python/index|⬅ Retour]] · <a href="/pdfs/td1_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 3. Tri à bulles (\texttt{bubble\_sort}) et mutation en place

On fournit \texttt{bubble\_sort0.py}, un tri à bulles qui trie en fait
la liste dans l'ordre **décroissant** au lieu de croissant. Il faut
identifier la cause avec le débogueur, corriger, puis discuter un effet
de bord discret mais important : la fonction modifie la liste passée en
argument *en place*.

**q1.** Exécuter \texttt{bubble\_sort0.py}. Le résultat correspond-il au
commentaire « Expected output » ? Identifier la ligne responsable.

> [!tip]- 💡 Coup de pouce
> Suivez la liste après le premier échange dans la boucle interne : le
> plus petit ou le plus grand élément remonte-t-il en fin de liste ?


> [!success]- ✅ Correction
> La condition arr[j] < arr[j+1] trie en ordre décroissant.


> [!example]- 📝 Solution détaillée
> **Diagnostic**
>
> Le résultat affiché est \texttt{[90, 64, 34, 25, 22, 12, 11]} :
> décroissant, alors que le commentaire annonçait un ordre
> croissant. La condition d'échange \texttt{arr[j] < arr[j+1]} fait
> remonter les plus petits éléments à la fin, ce qui produit un tri
> décroissant.


**q2.** Corriger la fonction pour obtenir un tri croissant. Valider sur
\texttt{[64, 34, 25, 12, 22, 11, 90]}, \texttt{[]}, \texttt{[1]},
\texttt{[3, 1, 3, 2]} et le pire cas \texttt{[5, 4, 3, 2, 1]}.

> [!tip]- 💡 Coup de pouce
> Il suffit d'inverser le sens de la comparaison, pas de trier la
> liste par un autre moyen.


> [!success]- ✅ Correction
> Remplacer arr[j] < arr[j+1] par values[index] > values[index+1].


> [!example]- 📝 Solution détaillée
> **Correction et validation**
>
> Avec \texttt{values[index] > values[index+1]}, tous les cas
> proposés sont correctement triés en ordre croissant, y compris
> la liste vide et la liste à un seul élément (aucune itération de
> boucle n'est alors nécessaire).


**q3.** Que vaut \texttt{unsorted\_list} *après* l'appel à
\texttt{bubble\_sort(unsorted\_list)} ? Pourquoi ?

> [!tip]- 💡 Coup de pouce
> La fonction échange les éléments avec la notation
> \texttt{arr[j], arr[j+1] = arr[j+1], arr[j]} : sur quel objet
> opère-t-elle réellement ?


> [!success]- ✅ Correction
> La liste d'origine est triée aussi : la fonction modifie l'objet reçu en place.


> [!example]- 📝 Solution détaillée
> **Mutation en place**
>
> En Python, une liste est un objet *mutable* : le paramètre
> \texttt{arr} (ou \texttt{values}) référence le même objet que
> \texttt{unsorted\_list} dans le code appelant, sans en faire une
> copie. Les échanges effectués à l'intérieur de la fonction
> modifient donc directement la liste d'origine, qui se retrouve
> triée après l'appel — même si l'on n'utilise pas la valeur de
> retour de la fonction.


> [!note] 🔗 Voir aussi
> [[physique/IOGS/iogs-onip/TD/bloc-intro-methodes-numeriques-onip-semestre-5/intro-prise-en-main-de-pycharm-debogage-et-bonnes-pratiques-python/ex5-regression-lineaire-bruitee-et-effets-de-bord|Exercice 5 — Régression linéaire bruitée et effets de bord]] · [[physique/IOGS/iogs-onip/TD/bloc-intro-methodes-numeriques-onip-semestre-5/intro-prise-en-main-de-pycharm-debogage-et-bonnes-pratiques-python/ex2-recherche-dichotomique-recursive-texttt-binary-search|Exercice 2 — Recherche dichotomique récursive (\texttt{binary\_search})]] · [[physique/IOGS/iogs-onip/TD/bloc-intro-methodes-numeriques-onip-semestre-5/intro-prise-en-main-de-pycharm-debogage-et-bonnes-pratiques-python/ex6-somme-des-elements-d-une-liste-mauvais-argument-d-appel|Exercice 6 — Somme des éléments d'une liste : mauvais argument d'appel]]

