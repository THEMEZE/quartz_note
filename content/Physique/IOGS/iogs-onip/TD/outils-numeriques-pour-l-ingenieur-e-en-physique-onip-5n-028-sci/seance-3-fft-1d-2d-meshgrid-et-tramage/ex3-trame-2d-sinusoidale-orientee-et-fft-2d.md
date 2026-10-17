---
title: "Exercice 3 — Trame 2D sinusoïdale orientée et FFT 2D"
tags:
  - td
  - outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci
---

[[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-3-fft-1d-2d-meshgrid-et-tramage/index|⬅ Retour]] · <a href="/pdfs/td3_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 3. Trame 2D sinusoïdale orientée et FFT 2D

1. Réaliser une fonction qui génère une trame 2D sinusoïdale de taille
   $M$ par $N$, de pas spatial \texttt{step}, selon un angle
   \texttt{alpha}. \\
2. Tester cette fonction : trame de 200 par 100, pas de 10.1, angle de
   35°. \\
3. Utiliser \texttt{np.fft.fftshift} sur la matrice générée. \\
4. Faire la TF en 2D de la trame et afficher le résultat.

**q1.** Écrire \texttt{generate\_grating(M, N, step, alpha\_deg)} et générer
une trame de 200 par 100, pas de 10.1, angle de 35°.

> [!tip]- 💡 Coup de pouce
> Projetez chaque point de la grille \texttt{meshgrid} sur le vecteur
> directeur $(\cos\alpha, \sin\alpha)$ avant d'appliquer un cosinus.


> [!success]- ✅ Correction
> projection = X*cos(alpha) + Y*sin(alpha) ; trame = cos(2*pi*projection/step).


> [!example]- 📝 Solution détaillée
> **Implémentation**
>
> Voir le code commenté ci-dessus. Si blocage sur le calcul de la
> projection, partir des cas simples $\alpha = 0^\circ$ (franges
> verticales, seul $X$ intervient) et $\alpha = 90^\circ$ (franges
> horizontales, seul $Y$ intervient) avant de généraliser.


**q2.** Appliquer \texttt{np.fft.fftshift} directement sur la trame
(image spatiale, pas encore une TF). Que constate-t-on ?

> [!tip]- 💡 Coup de pouce
> \texttt{fftshift} est une opération purement géométrique sur un
> tableau, indépendante de la signification physique de son contenu.


> [!success]- ✅ Correction
> L'image est simplement réarrangée par permutation de quadrants (haut-gauche <-> bas-droite, etc.).


> [!example]- 📝 Solution détaillée
> **Interprétation**
>
> \texttt{fftshift} permute les quadrants de l'image (haut-gauche
> avec bas-droite, haut-droite avec bas-gauche), quel que soit le
> contenu du tableau : ici appliqué à une image spatiale, cela
> produit simplement une version « recollée » de la trame, sans
> aucun rapport pour l'instant avec une transformée de Fourier —
> bonne façon de dissocier la mécanique de \texttt{fftshift} de son
> usage habituel sur un spectre.


**q3.** Calculer la FFT 2D de la trame et afficher son module (avec
\texttt{fftshift} et une échelle \texttt{log1p} pour la lisibilité).
Interpréter la position des pics observés.

> [!tip]- 💡 Coup de pouce
> La distance des pics au centre est liée au pas spatial \texttt{step},
> et leur orientation à l'angle \texttt{alpha\_deg} de la trame.


> [!success]- ✅ Correction
> Deux pics symétriques par rapport au centre, perpendiculaires aux franges, à une distance inversement proportionnelle à step.


> [!example]- 📝 Solution détaillée
> **Interprétation physique**
>
> Comme pour la FFT 1D, la trame étant réelle, sa TF2D présente une
> symétrie centrale : deux pics symétriques par rapport au centre
> de l'image, alignés perpendiculairement à la direction des
> franges (donc dans la direction $(\cos\alpha, \sin\alpha)$), à
> une distance du centre d'autant plus grande que le pas spatial
> \texttt{step} est petit (fréquence spatiale élevée). Si l'on
> double \texttt{step}, la distance des pics au centre est divisée
> par deux.


> [!note] 🔗 Voir aussi
> [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-3-fft-1d-2d-meshgrid-et-tramage/ex2-matrices-2d-double-boucle-vs-meshgrid|Exercice 2 — Matrices 2D : double boucle vs meshgrid]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-3-fft-1d-2d-meshgrid-et-tramage/ex4-si-vous-vous-ennuyez-galerie-de-motifs-avec-meshgrid|Exercice 4 — Si vous vous ennuyez... galerie de motifs avec meshgrid]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-3-fft-1d-2d-meshgrid-et-tramage/ex1-transformee-de-fourier-discrete-fft-d-un-signal-sinusoidal|Exercice 1 — Transformée de Fourier discrète (FFT) d'un signal sinusoïdal]]

