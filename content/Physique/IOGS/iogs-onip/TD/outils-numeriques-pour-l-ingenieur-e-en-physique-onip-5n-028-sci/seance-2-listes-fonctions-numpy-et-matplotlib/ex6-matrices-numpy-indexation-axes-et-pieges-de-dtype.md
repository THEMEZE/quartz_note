---
title: "Exercice 6 — Matrices Numpy : indexation, axes et pièges de dtype"
tags:
  - td
  - outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci
---

[[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/index|⬅ Retour]] · <a href="/pdfs/td2_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 6. Matrices Numpy : indexation, axes et pièges de dtype

Soit la matrice
$A = \begin{pmatrix} 4 & 6 & -2 & 3 \\ 2 & -1 & 0 & 1 \\ -7 & 0 & 1 & 12
\end{pmatrix}$. \\
1. Créer \texttt{A} avec \texttt{np.array} et l'afficher. \\
2. Afficher le type de \texttt{A}, le type d'un élément, la taille de
   \texttt{A}. \\
3. Afficher la seconde colonne puis la troisième ligne. \\
4. Afficher la moyenne de tous les éléments, par colonne, par ligne. \\
5. Affichage formaté : « la moyenne de tous les éléments vaut ... ». \\
6. Modifier \texttt{A} : 2 premières lignes $\times 2$, puis dernière
   colonne $/3$. Quel est le type des éléments de \texttt{A} alors ? \\
7. Créer \texttt{B} (3×4, que des 2), remplacer sa première colonne par
   0. \\
8. Que représente \texttt{A*B} ? Comment faire un produit matriciel
   entre \texttt{A} et \texttt{B} ? \\
9. Créer \texttt{CC} : éléments de \texttt{A*B} supérieurs à 5 conservés,
   sinon 0.

**q1.** Créer \texttt{A} avec \texttt{np.array}, afficher son type, le type
d'un élément, et sa taille (\texttt{.shape}, \texttt{.size}).

> [!tip]- 💡 Coup de pouce
> \texttt{type(A)} et \texttt{A.dtype} répondent à deux questions
> différentes.


> [!success]- ✅ Correction
> type(A) -> numpy.ndarray ; A.dtype -> int64 ; A.shape -> (3, 4).


> [!example]- 📝 Solution détaillée
> **Résultat**
>
> \texttt{type(A)} vaut \texttt{numpy.ndarray} (le type de
> l'objet), \texttt{A.dtype} vaut \texttt{int64} (le type des
> nombres stockés, car tous les éléments saisis sont des entiers),
> \texttt{A.shape} vaut $(3, 4)$ et \texttt{A.size} vaut $12$.


**q2.** Afficher la seconde colonne puis la troisième ligne de \texttt{A}.
Puis calculer la moyenne de tous les éléments, par colonne, par
ligne.

> [!tip]- 💡 Coup de pouce
> Les indices commencent à 0 : « seconde colonne » = indice 1,
> « troisième ligne » = indice 2.


> [!success]- ✅ Correction
> A[:, 1] et A[2, :] ; moyennes via np.mean(A, axis=0) et axis=1.


> [!example]- 📝 Solution détaillée
> **Résultat**
>
> Seconde colonne (indice 1) : $[6, -1, 0]$ ; troisième ligne
> (indice 2) : $[-7, 0, 1, 12]$. Moyenne totale $\approx 1{,}583$ ;
> moyenne par colonne (\texttt{axis=0}) :
> $[-0{,}333,\ 1{,}667,\ -0{,}333,\ 5{,}333]$ ; moyenne par ligne
> (\texttt{axis=1}) : $[2{,}75,\ 0{,}5,\ 1{,}5]$.


**q3.** Multiplier les deux premières lignes de \texttt{A} par 2, puis
diviser sa dernière colonne par 3. Quel est le type des éléments de
\texttt{A} après cette opération ? Que se passe-t-il si l'on oublie
de convertir \texttt{A} en \texttt{float} au préalable ?

> [!tip]- 💡 Coup de pouce
> Testez la division par 3 sur la valeur 6 de la dernière colonne, puis
> sur une valeur qui ne tombe pas juste, comme 2.


> [!success]- ✅ Correction
> Sans conversion, la division est tronquée silencieusement (int64) ; avec .astype(float) au préalable, on obtient bien float64.


> [!example]- 📝 Solution détaillée
> **Le piège et sa correction**
>
> Sans conversion préalable, \texttt{A[:, -1] = A[:, -1] / 3} sur
> un tableau \texttt{int64} tronque le résultat sans lever
> d'erreur : $12/3=4$ reste correct par coïncidence, mais $2/3$
> devient $0$ au lieu de $0{,}667$. Pour éviter ce piège, il faut
> convertir \texttt{A} en \texttt{float} *avant* toute
> division réassignée dans le tableau, avec
> \texttt{A = A.astype(float)}. Après conversion, \texttt{A.dtype}
> vaut bien \texttt{float64}.


**q4.** Créer \texttt{B} (3×4, que des 2), remplacer sa première colonne par
des 0. Que représente \texttt{A*B} ? Comment obtenir un véritable
produit matriciel entre \texttt{A} et \texttt{B} ?

> [!tip]- 💡 Coup de pouce
> Vérifiez si les dimensions de \texttt{A} et \texttt{B} permettent un
> produit matriciel direct \texttt{A @ B}.


> [!success]- ✅ Correction
> A*B est un produit élément par élément (Hadamard). A @ B est impossible (3x4 @ 3x4) ; utiliser A @ B.T ou A.T @ B.


> [!example]- 📝 Solution détaillée
> **Produit élément par élément vs matriciel**
>
> \texttt{A*B} effectue une multiplication terme à terme, valable
> car \texttt{A} et \texttt{B} ont la même forme $(3,4)$ : ce
> n'est pas un produit matriciel. Le produit matriciel classique
> nécessite que le nombre de colonnes du premier facteur soit égal
> au nombre de lignes du second : \texttt{A} et \texttt{B} étant
> toutes deux $3\times 4$, \texttt{A @ B} est impossible
> directement. On peut néanmoins calculer \texttt{A @ B.T} (donne
> une matrice $3\times3$) ou \texttt{A.T @ B} (donne une matrice
> $4\times4$).


**q5.** Créer \texttt{CC}, une matrice qui ne conserve que les éléments de
\texttt{A*B} supérieurs à 5, et force les autres à 0.

> [!tip]- 💡 Coup de pouce
> \texttt{np.where(condition, valeur\_si\_vrai, valeur\_si\_faux)} est
> l'outil adapté à ce filtrage conditionnel élément par élément.


> [!success]- ✅ Correction
> CC = np.where(A*B > 5, A*B, 0)


> [!example]- 📝 Solution détaillée
> **Utilisation de np.where**
>
> \texttt{CC = np.where(produit\_elementwise > 5,
> produit\_elementwise, 0)} calcule, pour chaque élément de
> \texttt{A*B}, la valeur elle-même si elle dépasse 5, et 0 sinon
> — un filtrage à la fois plus lisible et plus rapide qu'une
> double boucle \texttt{for} explicite. Ce calcul utilise
> \texttt{A} déjà modifiée par la question précédente (float,
> lignes doublées, dernière colonne divisée par 3).

