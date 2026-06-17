---
title: Algèbre graduée
tags:
  - Science
---
En  [[Mathématique]]/[mathématiques](https://fr.wikipedia.org/wiki/Math%C3%A9matiques "Mathématiques"), en [[Algèbre linéaire]]/[algèbre linéaire](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_lin%C3%A9aire "Algèbre linéaire"), on appelle **[algèbre graduée](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_gradu%C3%A9e)** une [[Algèbre]]/[algèbre](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_sur_un_anneau "Algèbre sur un anneau") dotée d'une structure supplémentaire, appelée **graduation**.

## Définition

Soit $\mathcal A$ une [algèbre sur un corps](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_sur_un_corps "Algèbre sur un corps") (ou plus généralement [sur un anneau](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_sur_un_anneau "Algèbre sur un anneau")) $\mathbb{K}$. Une graduation sur $\mathcal A$ est la donnée d’une [famille](https://fr.wikipedia.org/wiki/Famille_\(math%C3%A9matiques\) "Famille (mathématiques)") de [sous-espaces vectoriels](https://fr.wikipedia.org/wiki/Sous-espace_vectoriel "Sous-espace vectoriel") $ {\displaystyle ( \mathcal A_{i})_{i\in \mathbb {N} }}$  de $\mathcal A$ vérifiant :

- ${\displaystyle \mathcal A=\bigoplus _{i\in \mathbb {N} } \mathcal A_{i}}$;
- ${\displaystyle \forall i,j\in \mathbb {N} , \mathcal A_{i} \mathcal A_{j}\subset \mathcal A_{i+j}}$, c'est-à-dire que ${\displaystyle \forall \left[i,j\in \mathbb {N} ,x\in \mathcal A_{i},y\in \mathcal A_{j}\right],\ \ x\times y\in \mathcal A_{i+j}}$

L’algèbre $\mathcal A$ est alors dite graduée (parfois ℕ-graduée, comme cas particulier de la notion d'algèbre **_M_-graduée** pour un [monoïde](https://fr.wikipedia.org/wiki/Mono%C3%AFde "Monoïde") _M_ [[1]](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_gradu%C3%A9e#cite_note-B-1)).

Les éléments non nuls de $\mathcal A_i$ sont dits homogènes de degré $i$. Un [[Idéal]]/[idéal](https://fr.wikipedia.org/wiki/Id%C3%A9al "Idéal") est dit **homogène** si, pour chaque élément $a$ qu'il contient, il contient également les composantes homogènes de $a$ (les $a_i$ de l'unique décomposition $a = a_0 + a_1 + \cdots + a_n$ telle que pour tout ${\displaystyle i\in \mathbb {N} ,a_{i}\in \mathcal A_{i}\setminus \{0\}}$. Cela revient à dire que $I$ est engendré par des éléments homogènes.

Tout anneau (non gradué) $\mathcal A$ peut être doté d'une graduation en posant $\mathcal A_0 = \mathcal A$ et $\mathcal A_i = \emptyset \doteq \{ ~ \} $ pour tout $i > 0$. Cette structure est appelée graduation triviale de $\mathcal A$.

Une application $f$ entre des algèbres graduées $\mathcal A$ et $\mathcal B$  (sur le même corps) est un **homomorphisme d'algèbres graduées[[1]](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_gradu%C3%A9e#cite_note-B-1)** si ${\displaystyle f(\mathcal A_{i})\subset \mathcal B_{i}}$ pour tout $i$.

## Exemples

- L'anneau de [polynômes en _d_ indéterminées](https://fr.wikipedia.org/wiki/Polyn%C3%B4me_en_plusieurs_ind%C3%A9termin%C3%A9es "Polynôme en plusieurs indéterminées") $\mathbb{K} [X_1, \cdots , X_D]$, où les éléments homogènes de degré $n$ sont les [polynômes homogènes](https://fr.wikipedia.org/wiki/Polyn%C3%B4me_homog%C3%A8ne "Polynôme homogène") de degré $n$.
- L'[algèbre tensorielle](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_tensorielle "Algèbre tensorielle") $T(V)$ sur un espace vectoriel $V$, où les éléments homogènes de degré _n_ sont les tenseurs de la forme ${\displaystyle v_{1}\otimes v_{2}\otimes \dots \otimes v_{n}}$.
- L'[algèbre symétrique](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_sym%C3%A9trique "Algèbre symétrique") $S(V)$ et l'[algèbre extérieure](https://fr.wikipedia.org/wiki/Alg%C3%A8bre_ext%C3%A9rieure "Algèbre extérieure") $\bigwedge(V)$ sont des algèbres graduées, les éléments homogènes de degré $n$ étant les images des éléments homogènes de $T(V)$. Plus généralement, si un idéal $I$ d'une algèbre graduée $\mathcal A$ est homogène, le quotient $\mathcal A/I$ est naturellement gradué par
$${\displaystyle (\mathcal A/I)_{i}= \mathcal A_{i}/(I\cap \mathcal A_{i}).}$$

## Notes et références

1. [N. Bourbaki](https://fr.wikipedia.org/wiki/N._Bourbaki "N. Bourbaki"), [Algèbre](https://fr.wikipedia.org/wiki/%C3%89l%C3%A9ments_de_math%C3%A9matique "Éléments de mathématique") ([lire en ligne](https://books.google.com/books?id=4RIDPH1ULXcC&pg=RA1-PA30) [[archive](https://archive.wikiwix.com/cache/?url=https%3A%2F%2Fbooks.google.com%2Fbooks%3Fid%3D4RIDPH1ULXcC%26pg%3DRA1-PA30 "archive sur Wikiwix")]), III.30.

## Articles connexes

[Algèbre différentielle graduée](https://fr.wikipedia.org/w/index.php?title=Alg%C3%A8bre_diff%C3%A9rentielle_gradu%C3%A9e&action=edit&redlink=1 "Algèbre différentielle graduée (page inexistante)") [(en)](https://en.wikipedia.org/wiki/Differential_graded_algebra "en:Differential graded algebra")