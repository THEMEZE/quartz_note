---
title: "Exercice 2 — Matrices 2D : double boucle vs meshgrid"
tags:
  - td
  - outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci
---

[[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-3-fft-1d-2d-meshgrid-et-tramage/index|⬅ Retour]] · <a href="/pdfs/td3_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 2. Matrices 2D : double boucle vs meshgrid

1. Générer une matrice 2D de taille 200 par 100 avec \texttt{np.ones()}. \\
2. Avec une double boucle, générer une matrice 2D (largeur 200, hauteur
   100 ; $x$ de 0 à 199 pas 1 ; $y$ de 0 à 99 pas 1) dont les valeurs
   décrivent une sinusoïde de période 10 dans le sens vertical. \\
3. Visualiser avec \texttt{plt.imshow()}. \\
4. Mesurer le temps d'exécution de cette fonction. \\
5. Générer cette même matrice avec un \texttt{meshgrid}. \\
6. Visualiser avec \texttt{plt.imshow()}. \\
7. Mesurer et comparer le temps d'exécution. Conclusion ?

**q1.** Générer, avec une double boucle, une matrice (hauteur 100, largeur
200) dont les valeurs décrivent une sinusoïde de période 10 dans le
sens vertical, et l'afficher avec \texttt{plt.imshow()}.

> [!tip]- 💡 Coup de pouce
> La valeur ne doit dépendre que de la coordonnée verticale $y$
> (numéro de ligne), pas de $x$.


> [!success]- ✅ Correction
> matrice[y, x] = sin(2*pi*y/10), boucle sur y puis x.


> [!example]- 📝 Solution détaillée
> **Implémentation**
>
> Voir le code commenté ci-dessus. Le résultat est une image de
> bandes horizontales (variation uniquement verticale), avec une
> période de 10 pixels.


**q2.** Générer la même matrice avec \texttt{np.meshgrid}, vérifier qu'elle
est identique à la version en double boucle, puis mesurer et
comparer les deux temps d'exécution.

> [!tip]- 💡 Coup de pouce
> \texttt{X, Y = np.meshgrid(np.arange(largeur), np.arange(hauteur))}
> donne deux matrices de forme (hauteur, largeur).


> [!success]- ✅ Correction
> np.allclose(...) -> True ; meshgrid environ 4x plus rapide que la double boucle.


> [!example]- 📝 Solution détaillée
> **Comparaison**
>
> Les deux matrices sont identiques (\texttt{np.allclose} renvoie
> \texttt{True}). Le temps mesuré est d'environ $0{,}0027$ s pour
> la double boucle contre $0{,}0006$ s pour la version meshgrid,
> soit un facteur $\approx 4$ sur cette taille modeste — un écart
> qui s'amplifie fortement sur de plus grandes matrices, exactement
> comme observé en 1D à la séance 2 entre liste Python et vecteur
> Numpy.


> [!note] 🔗 Voir aussi
> [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-3-fft-1d-2d-meshgrid-et-tramage/ex3-trame-2d-sinusoidale-orientee-et-fft-2d|Exercice 3 — Trame 2D sinusoïdale orientée et FFT 2D]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-3-fft-1d-2d-meshgrid-et-tramage/ex4-si-vous-vous-ennuyez-galerie-de-motifs-avec-meshgrid|Exercice 4 — Si vous vous ennuyez... galerie de motifs avec meshgrid]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex2-fonction-texttt-get-list-et-mesure-du-temps-d-execution|Exercice 2 — Fonction \texttt{get\_list} et mesure du temps d'exécution]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex3-generation-d-un-vecteur-avec-numpy-vectorisation|Exercice 3 — Génération d'un vecteur avec Numpy : vectorisation]]

