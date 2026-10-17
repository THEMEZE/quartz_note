---
title: "Exercice 4 — Premier script scientifique : signal sinusoïdal (mauvaises pratiques)"
tags:
  - td
  - bloc-intro-methodes-numeriques-onip-semestre-5
---

[[physique/IOGS/iogs-onip/TD/bloc-intro-methodes-numeriques-onip-semestre-5/intro-prise-en-main-de-pycharm-debogage-et-bonnes-pratiques-python/index|⬅ Retour]] · <a href="/pdfs/td1_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 4. Premier script scientifique : signal sinusoïdal (mauvaises pratiques)

On fournit \texttt{first\_try0.py}, dont l'en-tête annonce lui-même :
« This code shows bad programming behaviors ». Le script plante avec
\texttt{NameError: name 'plt' is not defined} après avoir affiché 101
valeurs. Au-delà du bug d'import, un second défaut, purement physique
celui-là, se cache dans le choix de l'échantillonnage temporel : c'est
lui qui doit être identifié en priorité.

**q1.** Exécuter \texttt{first\_try0.py}. Quelle erreur apparaît, et à quelle
ligne ? Corriger ce premier problème.

> [!tip]- 💡 Coup de pouce
> Le message d'erreur nomme précisément le symbole non défini.


> [!success]- ✅ Correction
> NameError: name 'plt' is not defined ; il manque l'import de matplotlib.pyplot.


> [!example]- 📝 Solution détaillée
> **Diagnostic et correctif**
>
> Le traceback indique \texttt{NameError: name 'plt' is not
> defined} à la ligne \texttt{plt.figure()}. Le fichier utilise
> \texttt{plt} sans jamais l'importer : il faut ajouter
> \texttt{import matplotlib.pyplot as plt} en tête de fichier.


**q2.** Une fois \texttt{plt} importé, le script s'exécute sans erreur.
Calculer la fréquence d'échantillonnage réellement utilisée
(\texttt{c1 = np.linspace(0, 50, 101)}) et la comparer au critère de
Nyquist pour un signal de 850 Hz. Conclure sur la validité de la
courbe affichée.

> [!tip]- 💡 Coup de pouce
> 101 points sur 50 secondes donnent 100 intervalles : quel est le pas
> temporel, puis la fréquence d'échantillonnage associée ?


> [!success]- ✅ Correction
> fe = 2 Hz, très inférieure à 2×850 = 1700 Hz requis : le critère de Nyquist n'est pas respecté.


> [!example]- 📝 Solution détaillée
> **Calcul et diagnostic physique**
>
> Le pas temporel est $T_e = 50/100 = 0{,}5$ s, soit
> $f_e = 1/T_e = 2$ Hz. Le critère de Nyquist exige
> $f_e > 2 \times 850 = 1700$ Hz : il est massivement violé (par un
> facteur supérieur à 800). La courbe affichée est donc un artefact
> de repliement de spectre, sans rapport avec une véritable
> sinusoïde à 850 Hz, même si le script ne lève plus aucune
> erreur Python.


**q3.** Proposer un nouveau vecteur temps qui respecte largement le critère
de Nyquist pour un signal de 850 Hz, et réécrire le script en
corrigeant également le nom de fonction, les variables et
l'utilisation de \texttt{np.pi} à la place de \texttt{3.14}.

> [!tip]- 💡 Coup de pouce
> Choisir une fenêtre temporelle courte (quelques millisecondes) et un
> grand nombre de points, plutôt qu'une longue fenêtre peu échantillonnée.


> [!success]- ✅ Correction
> time = np.linspace(0, 0.01, 10001) donne fe = 1 MHz, largement suffisant.


> [!example]- 📝 Solution détaillée
> **Correction complète**
>
> En choisissant \texttt{time = np.linspace(0, 0.01, 10001)}, le
> pas devient $1\,\mu s$, soit $f_e = 1$ MHz, très largement
> supérieur au minimum de 1700 Hz exigé par Nyquist : la courbe
> affichée montre alors environ 8,5 périodes d'une véritable
> sinusoïde à 850 Hz sur 10 ms, conforme à l'amplitude de 20
> annoncée.

