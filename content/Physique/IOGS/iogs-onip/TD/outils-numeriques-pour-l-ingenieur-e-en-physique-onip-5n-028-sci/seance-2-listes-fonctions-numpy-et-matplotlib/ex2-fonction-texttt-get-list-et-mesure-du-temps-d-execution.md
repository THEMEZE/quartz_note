---
title: "Exercice 2 — Fonction \\texttt{get\\_list} et mesure du temps d'exécution"
tags:
  - td
  - outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci
---

[[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/index|⬅ Retour]] · <a href="/pdfs/td2_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 2. Fonction \texttt{get\_list} et mesure du temps d'exécution

1. Créer une fonction \texttt{get\_list} qui génère une liste de $N$
   nombres réels régulièrement répartis entre une valeur \texttt{start}
   et une valeur \texttt{stop}. $N$, \texttt{start} et \texttt{stop}
   seront des paramètres de cette fonction. \texttt{start} aura une
   valeur par défaut de 0. \\
2. Mesurer le temps d'exécution de la création d'une liste
   \texttt{L\_test} de 10 000 points répartis entre 0 et 1.

**q1.** Écrire \texttt{get\_list(N, stop, start=0)} en respectant l'ordre de
paramètres imposé par l'énoncé.

> [!tip]- 💡 Coup de pouce
> Le pas se calcule comme à l'exercice précédent : $N$ points, $N-1$
> intervalles.


> [!success]- ✅ Correction
> step = (stop - start) / (N - 1) ; return [start + i*step for i in range(N)]


> [!example]- 📝 Solution détaillée
> **Implémentation**
>
> \begin{verbatim}
> def get_list(N, stop, start=0):
>     step = (stop - start) / (N - 1)
>     return [start + i * step for i in range(N)]
> \end{verbatim}
> Test rapide : \texttt{get\_list(5, 1)} avec \texttt{start} par
> défaut (0), et \texttt{get\_list(5, 10, 5)} entre 5 et 10.


**q2.** Mesurer le temps d'exécution de la génération de 10 000 points
entre 0 et 1 avec cette fonction.

> [!tip]- 💡 Coup de pouce
> Encadrez uniquement l'appel de \texttt{get\_list}, pas
> l'\texttt{import time} ni le \texttt{print} du résultat.


> [!success]- ✅ Correction
> Environ 0.0005 à 0.001 s pour 10 000 points (ordre de grandeur, dépend de la machine).


> [!example]- 📝 Solution détaillée
> **Mesure**
>
> \begin{verbatim}
> debut = time.perf_counter()
> L_test = get_list(10_000, 1)
> fin = time.perf_counter()
> duree_liste_python = fin - debut
> \end{verbatim}
> La valeur absolue mesurée varie beaucoup d'une machine à
> l'autre : ce qui compte est l'ordre de grandeur, pour la
> comparaison avec la version Numpy de l'exercice suivant.


**q3.** Pourquoi utiliser \texttt{time.perf\_counter()} plutôt que
\texttt{time.time()} ?

> [!tip]- 💡 Coup de pouce
> L'un des deux peut être affecté par une resynchronisation de
> l'horloge système (ex. NTP) pendant la mesure.


> [!success]- ✅ Correction
> \texttt{perf\_counter()} est plus précis et insensible aux ajustements de l'horloge système.


> [!example]- 📝 Solution détaillée
> **Réponse**
>
> \texttt{time.time()} renvoie l'heure « murale » du système, qui
> peut être modifiée pendant l'exécution (synchronisation réseau,
> changement de fuseau...), ce qui fausserait une mesure de durée.
> \texttt{time.perf\_counter()} utilise une horloge monotone dédiée
> aux mesures de performance, avec une meilleure résolution :
> c'est le choix recommandé pour chronométrer un morceau de code.


> [!note] 🔗 Voir aussi
> [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex7-equation-du-second-degre-reels-puis-complexes|Exercice 7 — Équation du second degré : réels puis complexes]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex3-generation-d-un-vecteur-avec-numpy-vectorisation|Exercice 3 — Génération d'un vecteur avec Numpy : vectorisation]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-3-fft-1d-2d-meshgrid-et-tramage/ex2-matrices-2d-double-boucle-vs-meshgrid|Exercice 2 — Matrices 2D : double boucle vs meshgrid]]

