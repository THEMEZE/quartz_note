---
title: "Exercice 4 — Génération de signaux et affichage avec matplotlib"
tags:
  - td
  - outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci
---

[[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/index|⬅ Retour]] · <a href="/pdfs/td2_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 4. Génération de signaux et affichage avec matplotlib

1. Créer un vecteur temps de 101 points régulièrement répartis entre 0
   et 1 s. Quelle est la période d'échantillonnage ? \\
2. Importer \texttt{matplotlib.pyplot}. \\
3. Tracer une sinusoïde de période 50 ms en rouge, avec titre, axes et
   légende. \\
4. Que pensez-vous du résultat ? Améliorer le résultat. \\
5. Tracer sur le même graphique une sinusoïde de période 20 ms en bleu. \\
6. Faire un zoom pour n'afficher que quelques périodes des deux
   sinusoïdes. \\
7. Faire une fonction générant un signal sinusoïdal sur 10 périodes avec
   une fréquence d'échantillonnage 6 fois supérieure à la fréquence du
   signal. Arguments : période et amplitude. \\
8. Tester cette fonction avec une période de 30 ms et afficher le
   signal. \\
9. Compléter la fonction pour qu'elle prenne un vecteur temps en
   argument supplémentaire (défaut : liste vide). Si vide, même
   comportement qu'avant ; sinon, générer le signal sur ce vecteur.
   Message si la fréquence d'échantillonnage n'est pas correcte. \\
10. Tester cette nouvelle fonctionnalité.

**q1.** Créer le vecteur temps de 101 points sur [0, 1] s et calculer sa
période d'échantillonnage.

> [!tip]- 💡 Coup de pouce
> Même raisonnement que \texttt{td2\_ex1} : $N$ points, $N-1$
> intervalles.


> [!success]- ✅ Correction
> \texttt{time\_vector = np.linspace(0,1,101)} ; Te = 0.01 s.


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> \texttt{time\_vector = np.linspace(0, 1, 101)} donne
> \texttt{Te = time\_vector[1] - time\_vector[0] = 0{,}01} s.


**q2.** Tracer la sinusoïde de période 50 ms sur ce vecteur temps, en rouge,
avec titre, axes et légende. Que pensez-vous du résultat ? Comment
l'améliorer ?

> [!tip]- 💡 Coup de pouce
> Combien de points par période cela fait-il, avec $T_e=10$ ms et une
> période de 50 ms ?


> [!success]- ✅ Correction
> Seulement 5 points/période : rendu anguleux. Régénérer un vecteur temps plus fin, sans changer la durée.


> [!example]- 📝 Solution détaillée
> **Diagnostic et amélioration**
>
> Avec $T_e = 10$ ms pour une période de $50$ ms, on n'a que
> $50/10 = 5$ points par période : la courbe reliée par segments de
> droite a un aspect anguleux, peu représentatif d'une vraie
> sinusoïde. Ce n'est pas un sous-échantillonnage au sens de
> Nyquist ($5 > 2$), mais c'est insuffisant pour un rendu visuel
> lisse. L'amélioration consiste à augmenter le nombre de points
> du vecteur temps (par ex. \texttt{np.linspace(0, 1, 2001)}), sans
> changer la durée totale du signal.


**q3.** Écrire \texttt{generate\_sine\_10\_periods(period, amplitude)}, qui
génère un signal sur 10 périodes avec $f_e = 6f$. La tester avec une
période de 30 ms.

> [!tip]- 💡 Coup de pouce
> \texttt{duration = 10 * period} ; \texttt{Te = 1 / (6 * frequency)}.


> [!success]- ✅ Correction
> np.arange(0, 10*period, 1/(6/period)) — voir code ci-dessus.


> [!example]- 📝 Solution détaillée
> **Implémentation**
>
> Voir le code commenté ci-dessus (« Questions 7-8 »). Avec
> \texttt{period=0.030}, \texttt{amplitude=2}, on obtient un signal
> de $6$ points par période, sur $10$ périodes, dont le rendu très
> anguleux illustre concrètement l'écart entre le critère de
> Nyquist et un affichage visuellement satisfaisant.


**q4.** Compléter la fonction pour accepter un vecteur temps optionnel
(défaut : liste vide). Si un vecteur est fourni, en déduire $f_e$ et
afficher un message si le critère de Nyquist n'est pas respecté.
Tester avec un vecteur bien échantillonné, puis un vecteur trop
grossier.

> [!tip]- 💡 Coup de pouce
> Utilisez \texttt{np.mean(np.diff(time\_vector))} pour déduire $T_e$
> d'un vecteur temps quelconque (supposé régulier).


> [!success]- ✅ Correction
> Voir \texttt{generate\_sine\_10\_periods\_v2} ci-dessus ; le cas « mal échantillonné » doit afficher le message d'alerte.


> [!example]- 📝 Solution détaillée
> **Validation**
>
> Avec \texttt{t\_manuel\_ok = np.linspace(0, 0.3, 1000)}, largement
> suffisant pour 30 ms, aucun message n'apparaît. Avec
> \texttt{t\_manuel\_ko = np.linspace(0, 0.3, 5)}, bien trop peu de
> points, le message d'avertissement doit s'afficher : c'est le
> test de compréhension à faire vérifier avant de considérer
> l'exercice terminé.


> [!note] 🔗 Voir aussi
> [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex3-generation-d-un-vecteur-avec-numpy-vectorisation|Exercice 3 — Génération d'un vecteur avec Numpy : vectorisation]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex5-fonction-porte-indexation-booleenne-numpy|Exercice 5 — Fonction porte : indexation booléenne Numpy]] · [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-2-listes-fonctions-numpy-et-matplotlib/ex7-equation-du-second-degre-reels-puis-complexes|Exercice 7 — Équation du second degré : réels puis complexes]]

