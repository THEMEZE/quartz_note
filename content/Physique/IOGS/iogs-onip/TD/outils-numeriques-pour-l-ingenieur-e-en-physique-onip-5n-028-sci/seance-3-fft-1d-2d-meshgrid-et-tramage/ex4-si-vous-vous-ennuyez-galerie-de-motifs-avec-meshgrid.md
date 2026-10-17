---
title: "Exercice 4 — Si vous vous ennuyez... galerie de motifs avec meshgrid"
tags:
  - td
  - outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci
---

[[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-3-fft-1d-2d-meshgrid-et-tramage/index|⬅ Retour]] · <a href="/pdfs/td3_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 4. Si vous vous ennuyez... galerie de motifs avec meshgrid *(facultatif)*

Si vous avez terminé en avance : écrire des fonctions qui utilisent
\texttt{np.meshgrid} pour générer une image représentant : \\
1. un disque ; \\
2. des anneaux concentriques ; \\
3. un damier ; \\
4. une mire radiale rectangulaire (secteurs alternés noir/blanc) ; \\
5. une mire radiale sinusoïdale ; \\
6. une gaussienne en 2D ; \\
7. une spirale ; \\
8. une étoile.
Afficher chaque image avec \texttt{plt.imshow} en niveaux de gris.

**q1.** Écrire une fonction \texttt{grille(M, N)} renvoyant une grille
centrée, puis \texttt{disque}, \texttt{anneaux} et \texttt{damier}.

> [!tip]- 💡 Coup de pouce
> Un disque est l'ensemble des points tels que $X^2 + Y^2 \leq R^2$.
> Pour les anneaux et le damier, utiliser la partie entière
> (\texttt{np.floor}) et la parité (\texttt{\% 2}).


> [!success]- ✅ Correction
> Disque : X**2 + Y**2 <= R**2 ; anneaux : floor(r/largeur) pair ; damier : floor(X/c) + floor(Y/c) pair.


> [!example]- 📝 Solution détaillée
> **Implémentation**
>
> Voir le code commenté ci-dessus.


**q2.** Écrire \texttt{mire\_radiale\_rect} et \texttt{mire\_radiale\_sin} :
secteurs alternés noir/blanc, puis variation sinusoïdale selon l'angle.

> [!tip]- 💡 Coup de pouce
> Le motif ne dépend que de l'angle $\theta = \mathrm{atan2}(Y, X)$,
> pas du rayon.


> [!success]- ✅ Correction
> Rect : floor(theta*n/pi) pair ; sinusoidale : 0.5*(1 + cos(n*theta)).


> [!example]- 📝 Solution détaillée
> **Implémentation**
>
> Voir le code ci-dessus. Le motif est constant le long de chaque
> demi-droite issue du centre.


**q3.** Écrire \texttt{gaussienne} et \texttt{spirale}.

> [!tip]- 💡 Coup de pouce
> Gaussienne : $e^{-r^2/(2\sigma^2)}$. Spirale : un cosinus dont la
> phase dépend à la fois de $\theta$ et de $r$.


> [!success]- ✅ Correction
> Gaussienne : exp(-r**2/(2*sigma**2)) ; spirale : 0.5*(1 + cos(n*theta - 2*pi*r/pas)).


> [!example]- 📝 Solution détaillée
> **Implémentation**
>
> Voir le code ci-dessus. Pour la spirale, le terme $n\theta$ donne
> le nombre de bras et le terme en $r$ les enroule.


**q4.** Écrire \texttt{etoile(M, N, R, n\_branches)}.

> [!tip]- 💡 Coup de pouce
> Définir un rayon limite qui dépend de l'angle, puis garder les points
> dont le rayon est inférieur à cette limite.


> [!success]- ✅ Correction
> Garder les points tels que r <= R*(creux + (1-creux)*(1 - abs(sin(n*theta/2)))).


> [!example]- 📝 Solution détaillée
> **Implémentation**
>
> Voir le code ci-dessus. Le rayon limite varie avec $\theta$ et
> présente $n$ maxima : un par branche.


> [!note] 🔗 Voir aussi
> [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-3-fft-1d-2d-meshgrid-et-tramage/ex2-matrices-2d-double-boucle-vs-meshgrid|Exercice 2 — Matrices 2D : double boucle vs meshgrid]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-3-fft-1d-2d-meshgrid-et-tramage/ex3-trame-2d-sinusoidale-orientee-et-fft-2d|Exercice 3 — Trame 2D sinusoïdale orientée et FFT 2D]]

