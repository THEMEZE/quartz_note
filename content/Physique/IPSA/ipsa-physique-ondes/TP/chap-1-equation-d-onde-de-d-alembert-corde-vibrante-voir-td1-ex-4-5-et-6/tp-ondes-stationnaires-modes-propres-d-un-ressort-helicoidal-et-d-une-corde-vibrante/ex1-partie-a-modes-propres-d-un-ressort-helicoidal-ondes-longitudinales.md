---
title: "Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales)"
tags:
  - tp
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6
---

[[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/index|⬅ Retour]] · <a href="/pdfs/tp1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/tp1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

<p><span style="color:#1565C0">(Part A — Normal modes of a helical spring, longitudinal waves)</span></p>

### Exercice 1. Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) <span style="color:#1565C0">(Part A — Normal modes of a helical spring, longitudinal waves)</span>

*⭐ Indispensable · Difficulté ●●○○○ · ⏱ 40 min · Type : Manipulation guidée*

Un ressort hélicoïdal est accroché entre une tige support et la tige mobile du vibreur. On cherche ses six premiers modes propres et on teste $f_n=nc/(2L)$. **Question scientifique :** le ressort confirme-t-il le modèle des modes propres ?

<span style="color:#1565C0">A helical spring is hooked between a support rod and the moving rod of the vibrator. We look for its first six normal modes and test $f_n=nc/(2L)$. **Scientific question:** does the spring confirm the normal-mode model?</span>

> [!question]+ 🎣 Accroche
> **Une onde longitudinale peut-elle être stationnaire ? <span style="color:#1565C0">(Can a longitudinal wave be standing?)</span>**
>
> *Durée de l'introduction : 3 min, avant de toucher au matériel*
>
> *Dans un ressort, les spires oscillent **dans la direction de propagation**. Peut-on malgré cela voir des nœuds et des ventres ? Pourquoi la fréquence augmente-t-elle quand on passe d'un mode au suivant ?
>
> <span style="color:#1565C0">In a spring the coils oscillate **along the direction of propagation**. Can we still see nodes and antinodes? Why does the frequency increase from one mode to the next?</span>*
>
> **Idée clé : les conditions aux limites sélectionnent des fréquences.** Avec deux extrémités quasi fixes, $L=n\lambda_n/2$ et $f_n=nc/(2L)$ : la fréquence est **proportionnelle** à $n$, la pente de $f_n=f(n)$ vaut $c/(2L)$.
>
> <span style="color:#1565C0">**Key idea: boundary conditions select frequencies.** With two quasi-fixed ends, $L=n\lambda_n/2$ and $f_n=nc/(2L)$: the frequency is **proportional** to $n$, and the slope of $f_n$ versus $n$ is $c/(2L)$.</span>


> [!note]- 🧮 Outils mathématiques
> **Régression linéaire <span style="color:#1565C0">(Linear regression)</span>**
>
> Pour $f_n=\alpha n$ avec $\alpha=c/(2L)$ : $c=2L\alpha$. Vérifier que l'ordonnée à l'origine est proche de $0$.
>
> <span style="color:#1565C0">For $f_n=\alpha n$ with $\alpha=c/(2L)$: $c=2L\alpha$. Check that the intercept is close to $0$.</span>
>
> **Incertitude sur la pente <span style="color:#1565C0">(Uncertainty on the slope)</span>**
>
> Excel (DROITEREG) donne l'incertitude-type de la pente ; sinon encadrer par deux droites extrêmes. $\Delta c/c=\Delta L/L+\Delta\alpha/\alpha$.
>
> <span style="color:#1565C0">Excel (LINEST) gives the standard error of the slope; otherwise bracket with two extreme lines. $\Delta c/c=\Delta L/L+\Delta\alpha/\alpha$.</span>


**q1.** A1 — Mesurer la longueur effective $L$ du ressort entre ses deux points d'attache et estimer l'incertitude.

<span style="color:#1565C0">A1 — Measure the effective length $L$ of the spring between its two attachment points and estimate the uncertainty.</span>

> [!tip]- 💡 Coup de pouce
> **Mesure <span style="color:#1565C0">(Measurement)</span>**
>
> Mesurer entre les deux points d'accroche (Fig. 2), ressort légèrement tendu, non tordu. Incertitude de lecture et de repérage des points d'attache.
>
> <span style="color:#1565C0">Measure between the two hooks (Fig. 2), spring slightly stretched and not twisted. Reading and positioning uncertainty.</span>


**q2.** A2 — En faisant varier lentement la fréquence, repérer les six premiers modes propres et noter $f_n$.

<span style="color:#1565C0">A2 — By slowly varying the frequency, find the first six normal modes and record $f_n$.</span>

> [!tip]- 💡 Coup de pouce
> **Procédure <span style="color:#1565C0">(Procedure)</span>**
>
> Amplitude basse ($\le5$ V), balayage croissant, attendre la stabilisation, noter le nombre de nœuds. Un mode se reconnaît à un motif stable avec des nœuds bien localisés.
>
> <span style="color:#1565C0">Low amplitude ($\le5$ V), increasing sweep, wait for stabilization, note the number of nodes. A mode is recognized by a stable pattern with well-localized nodes.</span>


**q3.** A3 — Décrire comment reconnaître un mode excité, comment évolue $f_n$ avec $n$, et quelle représentation graphique teste le modèle.

<span style="color:#1565C0">A3 — Describe how to recognize an excited mode, how $f_n$ changes with $n$, and which graph tests the model.</span>

> [!tip]- 💡 Coup de pouce
> **Linéariser <span style="color:#1565C0">(Linearize)</span>**
>
> Quelle représentation donne une droite si $f_n=nc/(2L)$ ?
>
> <span style="color:#1565C0">Which plot gives a straight line if $f_n=nc/(2L)$?</span>


**q4.** A4 — Tracer le graphique A.1, relever l'équation de la droite et en déduire la célérité $c$ dans le ressort.

<span style="color:#1565C0">A4 — Plot graph A.1, read the fit equation and deduce the wave speed $c$ in the spring.</span>

> [!tip]- 💡 Coup de pouce
> **Pente et célérité <span style="color:#1565C0">(Slope and speed)</span>**
>
> Pente $\alpha=c/(2L)$, donc $c=2L\alpha$.
>
> <span style="color:#1565C0">Slope $\alpha=c/(2L)$, so $c=2L\alpha$.</span>


**q5.** A5 — Le modèle décrit-il correctement les mesures ? Quelles sont les principales sources d'incertitude ?

<span style="color:#1565C0">A5 — Does the model describe the measurements correctly? What are the main sources of uncertainty?</span>

> [!tip]- 💡 Coup de pouce
> **Critères <span style="color:#1565C0">(Criteria)</span>**
>
> Linéarité, ordonnée à l'origine proche de $0$, résidus petits devant l'incertitude de $f_n$.
>
> <span style="color:#1565C0">Linearity, intercept close to $0$, residuals small compared with the uncertainty on $f_n$.</span>


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex5-corde-fixee-a-ses-deux-extremites-et-ondes-stationnaires|Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex12-adaptation-d-impedance-lame-quart-d-onde-entre-deux-cordes|Exercice 12 — Adaptation d'impédance : lame quart d'onde entre deux cordes]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres]] · [[physique/IPSA/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex1-ondes-sur-un-ressort-long-slinky-filmees-au-ralenti-impulsions-reflexions-et-modes-propres|Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex13-corde-pincee-timbre-harmoniques-absents-et-energie-des-modes|Exercice 13 — Corde pincée : timbre, harmoniques absents et énergie des modes]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex14-corde-de-piano-raide-dispersion-et-inharmonicite|Exercice 14 — Corde de piano raide : dispersion et inharmonicité]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex16-masse-en-bout-de-corde-condition-aux-limites-dynamique-et-equation-transcendante|Exercice 16 — Masse en bout de corde : condition aux limites dynamique et équation transcendante]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex5-synthese-scientifique-du-tp|Exercice 5 — Synthèse scientifique du TP]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex6-experience-de-melde-oscillations-forcees-d-une-corde-resonance|Exercice 6 — Expérience de Melde, oscillations forcées d'une corde, résonance]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex15-corde-amortie-attenuation-facteur-de-qualite-et-resonance-de-melde|Exercice 15 — Corde amortie : atténuation, facteur de qualité et résonance de Melde]]

