---
title: "Exercice 1 — Création d'un projet sous PyCharm"
tags:
  - td
  - bloc-intro-methodes-numeriques-onip-semestre-5
---

[[physique/IOGS/iogs-onip/TD/bloc-intro-methodes-numeriques-onip-semestre-5/intro-prise-en-main-de-pycharm-debogage-et-bonnes-pratiques-python/index|⬅ Retour]] · <a href="/pdfs/td1_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 1. Création d'un projet sous PyCharm

Avant tout calcul scientifique, il faut un environnement de travail
fonctionnel. Cet exercice fait obtenir à chaque étudiant un projet
PyCharm associé à un interpréteur Python 3, contenant un fichier
\texttt{main.py} qui s'exécute sans erreur. Les paquets \texttt{numpy},
\texttt{matplotlib} et \texttt{scikit-learn} devront être installés dans
cet interpréteur : ils sont utilisés dès les exercices suivants.

**q1.** Où PyCharm va-t-il chercher les bibliothèques quand vous écrivez
\texttt{import numpy} ? Quelle est la différence entre le projet
PyCharm et l'interpréteur Python ?

> [!tip]- 💡 Coup de pouce
> Un projet est un dossier ; un interpréteur est un exécutable Python
> avec ses propres paquets installés à côté de lui, indépendamment du
> dossier de travail.


> [!success]- ✅ Correction
> L'interpréteur, pas le projet, détermine les paquets disponibles.


> [!example]- 📝 Solution détaillée
> **Projet vs interpréteur**
>
> Le projet ne contient que le code source et sa configuration
> (fichiers \texttt{.idea}). Les bibliothèques Python sont
> installées à l'intérieur de l'interpréteur choisi (dossier
> \texttt{site-packages}). Deux projets peuvent donc partager le
> même interpréteur (et les mêmes paquets), ou au contraire
> utiliser des interpréteurs différents avec des jeux de paquets
> totalement indépendants.


**q2.** Que se passerait-il si deux projets avaient besoin de deux versions
différentes d'une même bibliothèque ?

> [!tip]- 💡 Coup de pouce
> Un interpréteur ne peut avoir qu'une seule version installée d'un
> paquet donné à la fois.


> [!success]- ✅ Correction
> Il faut deux interpréteurs distincts (ex. deux environnements virtuels).


> [!example]- 📝 Solution détaillée
> **Isolation par environnement virtuel**
>
> Un même interpréteur ne peut contenir qu'une seule version d'un
> paquet donné. Pour faire cohabiter deux versions différentes, il
> faut créer deux environnements virtuels distincts (un par
> projet), chacun avec sa propre version installée : c'est
> précisément le rôle des \texttt{venv}, introduits en
> prolongement de cet exercice.

