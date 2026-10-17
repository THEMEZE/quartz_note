---
title: "Exercice 1 — Listes : génération d'un vecteur temps régulier"
tags:
  - td
  - outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci
---

[[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/index|⬅ Retour]] · <a href="/pdfs/td2_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 1. Listes : génération d'un vecteur temps régulier

1. Générer une liste \texttt{L\_temps} de 101 points régulièrement
   répartis entre 0 et 1 s. \\
2. Afficher la taille de cette liste. \\
3. Afficher le dernier élément de la liste. \\
4. Quelle est la période d'échantillonnage ?

**q1.** Générer \texttt{L\_temps}, puis afficher sa taille et son dernier
élément.

> [!tip]- 💡 Coup de pouce
> Combien d'intervalles y a-t-il entre 101 points ?


> [!success]- ✅ Correction
> \texttt{len(L\_temps)} = 101 ; \texttt{L\_temps[-1]} = 1.0.


> [!example]- 📝 Solution détaillée
> **Construction et vérification**
>
> Avec \texttt{pas = 1/100}, la compréhension de liste
> \texttt{[i * pas for i in range(101)]} produit bien 101 valeurs
> allant de $0$ à $100 \times 0{,}01 = 1{,}0$ inclus.


**q2.** Quelle est la période d'échantillonnage $T_e$ de cette liste ?

> [!tip]- 💡 Coup de pouce
> $T_e$ est l'écart entre deux points consécutifs.


> [!success]- ✅ Correction
> Te = 0.01 s.


> [!example]- 📝 Solution détaillée
> **Calcul de Te**
>
> $T_e = L\_temps[1] - L\_temps[0] = 0{,}01$ s. On peut aussi la
> lire directement dans le code (variable \texttt{pas}), mais la
> retrouver à partir de la liste elle-même est une bonne pratique
> si l'on ne connaît pas la formule de génération (utile par
> exemple si la liste provient d'un fichier de données).


**q3.** Si l'on voulait un pas de 5 ms, combien de points faudrait-il pour
couvrir 1 seconde ?

> [!tip]- 💡 Coup de pouce
> 1 seconde / 5 ms donne le nombre d'intervalles, pas directement le
> nombre de points.


> [!success]- ✅ Correction
> 201 points (200 intervalles de 5 ms).


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> Un pas de $5$ ms sur $1$ s correspond à $1/0{,}005 = 200$
> intervalles, donc $200 + 1 = 201$ points.

