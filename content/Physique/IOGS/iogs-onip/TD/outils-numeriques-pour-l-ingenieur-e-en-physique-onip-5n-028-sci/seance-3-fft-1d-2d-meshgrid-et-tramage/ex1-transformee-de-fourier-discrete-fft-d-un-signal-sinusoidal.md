---
title: "Exercice 1 — Transformée de Fourier discrète (FFT) d'un signal sinusoïdal"
tags:
  - td
  - outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci
---

[[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-3-fft-1d-2d-meshgrid-et-tramage/index|⬅ Retour]] · <a href="/pdfs/td3_ONIP1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 1. Transformée de Fourier discrète (FFT) d'un signal sinusoïdal

1. Créer une fonction générant une sinusoïde (amplitude, fréquence,
   vecteur temps en paramètres). \\
2. Générer un signal sinusoïdal de fréquence 200 Hz, période
   d'échantillonnage 300 µs, sur un intervalle de temps de 0.1 s. \\
3. Afficher ce signal. \\
4. Calculer la TF discrète du signal (algorithme FFT). \\
5. Afficher le résultat (parties réelle et imaginaire). Titre, axes,
   légende. Préciser le rôle de \texttt{np.fft.fftshift()}. \\
6. Reconstruire l'axe des fréquences. \\
7. Afficher le module de la TF discrète. Est-ce le résultat voulu ?

**q1.** Écrire \texttt{generate\_sine\_signal(amplitude, frequency,
time\_vector)}, puis générer le signal demandé (200 Hz,
$T_e = 300\,\mu s$, durée 0,1 s) et l'afficher.

> [!tip]- 💡 Coup de pouce
> \texttt{time\_vector = np.arange(0, duration, Te)} ; le nombre de
> points $N$ en découle, il n'est pas fixé a priori.


> [!success]- ✅ Correction
> \texttt{signal = amplitude * np.sin(2*pi*frequency*time\_vector)} ; N $\approx$ 334 points.


> [!example]- 📝 Solution détaillée
> **Génération**
>
> Avec \texttt{duration=0.1} s et \texttt{Te=300e-6} s, on obtient
> $N \approx 334$ points (peut varier de 1 point selon les
> arrondis flottants). Le signal tracé montre bien une sinusoïde
> de fréquence 200 Hz sur l'intervalle de 0,1 s.


**q2.** Calculer la TF du signal, puis afficher ses parties réelle et
imaginaire après \texttt{fftshift}. À quoi sert
\texttt{np.fft.fftshift()} ?

> [!tip]- 💡 Coup de pouce
> Comparez l'ordre des fréquences renvoyé par défaut par
> \texttt{np.fft.fft} à un ordre « naturel » croissant de $-f_{max}$ à
> $+f_{max}$.


> [!success]- ✅ Correction
> fftshift replace la fréquence nulle au centre du tableau, pour un affichage plus lisible.


> [!example]- 📝 Solution détaillée
> **Rôle de fftshift**
>
> Par défaut, \texttt{np.fft.fft} renvoie d'abord les fréquences
> positives croissantes, puis les négatives croissantes : la
> fréquence nulle est donc en tout début de tableau.
> \texttt{np.fft.fftshift} réordonne ce tableau pour placer 0 Hz
> au centre et les fréquences dans l'ordre croissant de gauche à
> droite — un simple réarrangement d'affichage, sans effet sur les
> valeurs elles-mêmes.


**q3.** Reconstruire l'axe des fréquences correspondant à \texttt{TF}, puis
afficher le module de la TF. Le résultat est-il celui attendu ?

> [!tip]- 💡 Coup de pouce
> \texttt{np.fft.fftfreq(N, d=Te)} doit recevoir le même
> \texttt{fftshift} que \texttt{TF} pour rester aligné avec elle.


> [!success]- ✅ Correction
> Deux pics symétriques à environ ±200 Hz : résultat attendu pour un signal réel.


> [!example]- 📝 Solution détaillée
> **Interprétation**
>
> On retrouve bien deux pics, situés (à la résolution
> fréquentielle près, ici 10 Hz) à environ $+200$ Hz et $-200$ Hz,
> cohérents avec la fréquence du signal généré. La présence de
> deux pics symétriques est normale : un signal réel a toujours un
> spectre symétrique par rapport à 0 Hz. Le pic n'est pas
> exactement à 200 Hz mais au multiple de la résolution
> fréquentielle le plus proche, ce qui relie directement la
> résolution du spectre à la durée du signal analysé
> ($1/\text{durée} = 10$ Hz ici), et non au nombre de points ni à
> $T_e$ seuls.


> [!note] 🔗 Voir aussi
> [[physique/IOGS/iogs-onip/TD/outils-numeriques-pour-l-ingenieur-e-en-physique-onip-5n-028-sci/seance-3-fft-1d-2d-meshgrid-et-tramage/ex3-trame-2d-sinusoidale-orientee-et-fft-2d|Exercice 3 — Trame 2D sinusoïdale orientée et FFT 2D]]

