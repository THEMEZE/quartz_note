---
title: "Exercice 3 — Génération d'un vecteur avec Numpy : vectorisation"
tags:
  - td
  - outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci
---

[[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/index|⬅ Retour]] · <a href="/pdfs/td2_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 3. Génération d'un vecteur avec Numpy : vectorisation

1. Importer la bibliothèque Numpy. \\
2. Générer un vecteur \texttt{V\_test} de 10 000 nombres réels répartis
   entre 0 et 1 avec Numpy. \\
3. Afficher la taille de ce vecteur. \\
4. Afficher le dernier élément de ce vecteur. \\
5. Mesurer le temps d'exécution de cette génération. \\
6. Comparer à la mesure de l'exercice précédent. Que concluez-vous ?

**q1.** Générer \texttt{V\_test = np.linspace(0, 1, 10\_000)}. Afficher sa
taille (\texttt{.size}), sa forme (\texttt{.shape}) et son dernier
élément.

> [!tip]- 💡 Coup de pouce
> \texttt{.size} donne le nombre total d'éléments ; \texttt{.shape}
> donne la forme du tableau sous forme de tuple.


> [!success]- ✅ Correction
> \texttt{V\_test.size} = 10000 ; \texttt{V\_test.shape} = (10000,) ; \texttt{V\_test[-1]} = 1.0.


> [!example]- 📝 Solution détaillée
> **Résultat**
>
> \texttt{np.linspace(0, 1, 10\_000)} génère 10 000 valeurs entre 0
> et 1 (bornes incluses), donc \texttt{.size} vaut $10\,000$,
> \texttt{.shape} vaut $(10\,000,)$ et le dernier élément vaut
> exactement $1{,}0$.


**q2.** Mesurer le temps d'exécution de cette génération et le comparer à
celui de la fonction \texttt{get\_list} de l'exercice précédent.
Conclure.

> [!tip]- 💡 Coup de pouce
> Recalculez si besoin \texttt{duree\_liste\_python} dans le même
> script, pour comparer sur la même exécution.


> [!success]- ✅ Correction
> Numpy est nettement plus rapide (souvent x10 à x100) : vectorisation, code C compilé.


> [!example]- 📝 Solution détaillée
> **Comparaison**
>
> Sur une exécution typique : liste Python $\approx 0{,}00067$ s,
> vecteur Numpy $\approx 0{,}00007$ s, soit un facteur d'environ
> $\times 10$ (le facteur exact varie fortement d'une machine à
> l'autre, parfois de $\times 5$ à $\times 100$). La cause : une
> boucle Python réévalue chaque itération une par une (overhead de
> l'interpréteur CPython à chaque tour), alors que
> \texttt{np.linspace} est implémenté en C et exécute le calcul de
> façon vectorisée, en une seule opération sur tout le tableau.


**q3.** Le facteur d'accélération serait-il le même avec $N=10$ ou
$N=1\,000\,000$ ?

> [!tip]- 💡 Coup de pouce
> Un tableau Numpy a un coût fixe de création, indépendant de $N$.


> [!success]- ✅ Correction
> Non : pour un petit N le coût fixe de création domine, Numpy peut même être plus lent.


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> Pour un très petit $N$ (quelques dizaines de points), le coût
> fixe de création de l'objet \texttt{ndarray} peut dominer le
> calcul lui-même : Numpy peut alors se révéler plus lent qu'une
> simple liste Python. À l'inverse, pour un très grand $N$ (par
> ex. $1\,000\,000$), le coût par élément de la boucle Python
> domine largement le coût fixe de Numpy, et le facteur
> d'accélération devient encore plus favorable à Numpy qu'avec
> $N=10\,000$.


> [!note] 🔗 Voir aussi
> [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex4-generation-de-signaux-et-affichage-avec-matplotlib|Exercice 4 — Génération de signaux et affichage avec matplotlib]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex5-fonction-porte-indexation-booleenne-numpy|Exercice 5 — Fonction porte : indexation booléenne Numpy]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex7-equation-du-second-degre-reels-puis-complexes|Exercice 7 — Équation du second degré : réels puis complexes]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex2-fonction-texttt-get-list-et-mesure-du-temps-d-execution|Exercice 2 — Fonction \texttt{get\_list} et mesure du temps d'exécution]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-3-fft-1d-2d-meshgrid-et-tramage/ex2-matrices-2d-double-boucle-vs-meshgrid|Exercice 2 — Matrices 2D : double boucle vs meshgrid]]

