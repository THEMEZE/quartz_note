---
title: "Exercice 6 — Somme des éléments d'une liste : mauvais argument d'appel"
tags:
  - td
  - bloc-intro-methodes-numeriques-onip-semestre-5
---

[[physique/IOGS/iogs-onip/TD/bloc-intro-methodes-numeriques-onip-semestre-5/intro-prise-en-main-de-pycharm-debogage-et-bonnes-pratiques-python/index|⬅ Retour]] · <a href="/pdfs/td1_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 6. Somme des éléments d'une liste : mauvais argument d'appel

On fournit \texttt{sum\_list\_elements0.py} : la fonction
\texttt{sum\_list\_elements} elle-même est correcte, mais le script
affiche \texttt{Sum of elements = 10} au lieu des \texttt{15} annoncés
par le commentaire « Expected output ». Exercice très court, à traiter
en échauffement ou en fin de séance.

**q1.** Exécuter le script. Le résultat correspond-il au commentaire
« Expected output: Sum of elements = 15 » ? Localiser précisément la
cause de l'écart, sans modifier la fonction \texttt{sum\_list\_elements}.

> [!tip]- 💡 Coup de pouce
> Affichez \texttt{sample\_list[:-1]} séparément avant l'appel à la
> fonction.


> [!success]- ✅ Correction
> \texttt{sample\_list[:-1]} exclut le dernier élément (5) de l'argument transmis.


> [!example]- 📝 Solution détaillée
> **Diagnostic**
>
> Le résultat affiché est \texttt{10}, et non \texttt{15}. La
> fonction \texttt{sum\_list\_elements} additionne correctement
> tous les éléments qu'elle reçoit, mais l'appel
> \texttt{sum\_list\_elements(sample\_list[:-1])} lui transmet
> \texttt{[1, 2, 3, 4]} (le slicing \texttt{[:-1]} exclut le
> dernier élément), et non la liste complète
> \texttt{[1, 2, 3, 4, 5]}.


**q2.** Corriger l'appel pour obtenir \texttt{Sum of elements = 15}.

> [!tip]- 💡 Coup de pouce
> Il suffit de transmettre la liste complète, sans slicing.


> [!success]- ✅ Correction
> \texttt{sum\_list\_elements(sample\_list)} (sans le [:-1]).


> [!example]- 📝 Solution détaillée
> **Correction**
>
> En appelant \texttt{sum\_list\_elements(sample\_list)} (sans le
> slicing \texttt{[:-1]}), les cinq éléments sont bien additionnés
> et le résultat affiché devient \texttt{15}, conforme au
> commentaire.


> [!note] 🔗 Voir aussi
> [[physique/IOGS/iogs-onip/TD/bloc-intro-methodes-numeriques-onip-semestre-5/intro-prise-en-main-de-pycharm-debogage-et-bonnes-pratiques-python/ex2-recherche-dichotomique-recursive-texttt-binary-search|Exercice 2 — Recherche dichotomique récursive (\texttt{binary\_search})]] · [[physique/IOGS/iogs-onip/TD/bloc-intro-methodes-numeriques-onip-semestre-5/intro-prise-en-main-de-pycharm-debogage-et-bonnes-pratiques-python/ex3-tri-a-bulles-texttt-bubble-sort-et-mutation-en-place|Exercice 3 — Tri à bulles (\texttt{bubble\_sort}) et mutation en place]]

