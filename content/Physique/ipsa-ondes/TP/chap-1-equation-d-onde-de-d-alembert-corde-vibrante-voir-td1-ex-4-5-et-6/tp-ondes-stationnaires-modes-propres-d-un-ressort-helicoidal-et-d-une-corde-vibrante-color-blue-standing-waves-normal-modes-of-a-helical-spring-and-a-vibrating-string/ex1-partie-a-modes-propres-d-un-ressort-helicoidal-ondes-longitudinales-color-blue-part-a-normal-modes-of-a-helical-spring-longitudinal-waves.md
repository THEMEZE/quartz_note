---
title: "Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}"
tags:
  - tp
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6
---

[[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/index|⬅ Retour]] · [📄 Corrigé](/pdfs/tp1_PhV212_corrige.pdf) · [📄 Énoncé](/pdfs/tp1_PhV212_enonce.pdf) · [📄 Aides](/pdfs/tp1_PhV212_aides.pdf) · [📄 Fiche enseignant](/pdfs/tp1_PhV212_fiche.pdf)

### Exercice 1. Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}

Un ressort hélicoïdal est accroché entre une tige support et la tige mobile du vibreur. On cherche ses six premiers modes propres et on teste $f_n=nc/(2L)$. **Question scientifique :** le ressort confirme-t-il le modèle des modes propres ?

<span style="color:blue">A helical spring is hooked between a support rod and the moving rod of the vibrator. We look for its first six normal modes and test $f_n=nc/(2L)$. **Scientific question:** does the spring confirm the normal-mode model?</span>

**q1.** A1 — Mesurer la longueur effective $L$ du ressort entre ses deux points d'attache et estimer l'incertitude.

<span style="color:blue">A1 — Measure the effective length $L$ of the spring between its two attachment points and estimate the uncertainty.</span>

> [!tip]- 💡 Coup de pouce
> **Mesure {\color{blue}(Measurement)}**
>
> Mesurer entre les deux points d'accroche (Fig. 2), ressort légèrement tendu, non tordu. Incertitude de lecture et de repérage des points d'attache.
>
> <span style="color:blue">Measure between the two hooks (Fig. 2), spring slightly stretched and not twisted. Reading and positioning uncertainty.</span>


> [!success]- ✅ Correction
> **Valeur provisoire {\color{blue}(Provisional value)}**
>
> $L=0{,}300\ \text{m}$, $\Delta L=0{,}002\ \text{m}$.
>
> <span style="color:blue">$L=0.300$ m, $\Delta L=0.002$ m.</span>


> [!example]- 📝 Solution détaillée
> **Remarque {\color{blue}(Remark)}**
>
> L'incertitude de $2$ mm vient surtout du repérage des points d'attache. Faire noter l'unité SI (m).
>
> <span style="color:blue">The 2 mm uncertainty mostly comes from locating the attachment points. Make sure students write the SI unit (m).</span>


**q2.** A2 — En faisant varier lentement la fréquence, repérer les six premiers modes propres et noter $f_n$.

<span style="color:blue">A2 — By slowly varying the frequency, find the first six normal modes and record $f_n$.</span>

> [!tip]- 💡 Coup de pouce
> **Procédure {\color{blue}(Procedure)}**
>
> Amplitude basse ($\le5$ V), balayage croissant, attendre la stabilisation, noter le nombre de nœuds. Un mode se reconnaît à un motif stable avec des nœuds bien localisés.
>
> <span style="color:blue">Low amplitude ($\le5$ V), increasing sweep, wait for stabilization, note the number of nodes. A mode is recognized by a stable pattern with well-localized nodes.</span>


> [!success]- ✅ Correction
> **Valeurs provisoires {\color{blue}(Provisional values)}**
>
> $f_n\ (\text{Hz})$ pour $n=1,\dots,6$ : $8{,}4\ ;\ 16{,}9\ ;\ 25{,}2\ ;\ 33{,}7\ ;\ 42{,}0\ ;\ 50{,}5$ (incertitude $\pm0{,}1$ Hz).
>
> <span style="color:blue">$f_n$ (Hz) for $n=1,\dots,6$: 8.4; 16.9; 25.2; 33.7; 42.0; 50.5 (uncertainty $\pm0.1$ Hz).</span>


> [!example]- 📝 Solution détaillée
> **Points de vigilance {\color{blue}(Watch points)}**
>
> Ne pas confondre un pic d'amplitude transitoire avec un mode. Si le motif dérive, ajuster la fréquence de $0{,}1$ Hz. Les modes sont à peu près équidistants : $f_{n+1}-f_n\approx8{,}4$ Hz.
>
> <span style="color:blue">Do not confuse a transient amplitude peak with a mode. If the pattern drifts, adjust the frequency by 0.1 Hz. The modes are roughly equally spaced: $f_{n+1}-f_n\approx8.4$ Hz.</span>


**q3.** A3 — Décrire comment reconnaître un mode excité, comment évolue $f_n$ avec $n$, et quelle représentation graphique teste le modèle.

<span style="color:blue">A3 — Describe how to recognize an excited mode, how $f_n$ changes with $n$, and which graph tests the model.</span>

> [!tip]- 💡 Coup de pouce
> **Linéariser {\color{blue}(Linearize)}**
>
> Quelle représentation donne une droite si $f_n=nc/(2L)$ ?
>
> <span style="color:blue">Which plot gives a straight line if $f_n=nc/(2L)$?</span>


> [!success]- ✅ Correction
> **Réponse attendue {\color{blue}(Expected answer)}**
>
> Mode excité : motif stable, nœuds immobiles, amplitude nettement plus grande. $f_n$ croît linéairement avec $n$. On trace $f_n=f(n)$ : droite passant par l'origine de pente $c/(2L)$.
>
> <span style="color:blue">Excited mode: stable pattern, motionless nodes, clearly larger amplitude. $f_n$ increases linearly with $n$. Plot $f_n$ versus $n$: a straight line through the origin with slope $c/(2L)$.</span>


> [!example]- 📝 Solution détaillée
> **Justification {\color{blue}(Justification)}**
>
> La relation est linéaire en $n$ : le graphique $f_n=f(n)$ est le plus direct, la pente donne $c$ sans linéarisation supplémentaire.
>
> <span style="color:blue">The relation is linear in $n$: the plot $f_n$ versus $n$ is the most direct, the slope gives $c$ with no extra linearization.</span>


**q4.** A4 — Tracer le graphique A.1, relever l'équation de la droite et en déduire la célérité $c$ dans le ressort.

<span style="color:blue">A4 — Plot graph A.1, read the fit equation and deduce the wave speed $c$ in the spring.</span>

> [!tip]- 💡 Coup de pouce
> **Pente et célérité {\color{blue}(Slope and speed)}**
>
> Pente $\alpha=c/(2L)$, donc $c=2L\alpha$.
>
> <span style="color:blue">Slope $\alpha=c/(2L)$, so $c=2L\alpha$.</span>


> [!success]- ✅ Correction
> **Valeur provisoire {\color{blue}(Provisional value)}**
>
> Ajustement : $f_n=8{,}42\,n+0{,}0$ (Hz). $c=2L\alpha=2\times0{,}300\times8{,}42\approx5{,}05\ \text{m/s}$, soit $\Delta c\approx0{,}05$ m/s.
>
> <span style="color:blue">Fit: $f_n=8.42\,n+0.0$ (Hz). $c=2L\alpha=2\times0.300\times8.42\approx5.05$ m/s, i.e. $\Delta c\approx0.05$ m/s.</span>


> [!example]- 📝 Solution détaillée
> **Rédaction pas à pas {\color{blue}(Step-by-step write-up)}**
>
> Le modèle donne $f_n=\dfrac{c}{2L}\,n$, droite de pente $\alpha=\dfrac{c}{2L}$. Donc $c=2L\alpha=2\times0{,}300\times8{,}42=5{,}05$ m/s. Incertitude : $\dfrac{\Delta c}{c}=\dfrac{\Delta L}{L}+\dfrac{\Delta\alpha}{\alpha}\approx0{,}007+0{,}003$, soit $\Delta c\approx0{,}05$ m/s.
>
> <span style="color:blue">The model gives $f_n=\dfrac{c}{2L}\,n$, a line of slope $\alpha=\dfrac{c}{2L}$. Hence $c=2L\alpha=2\times0.300\times8.42=5.05$ m/s. Uncertainty: $\dfrac{\Delta c}{c}=\dfrac{\Delta L}{L}+\dfrac{\Delta\alpha}{\alpha}\approx0.007+0.003$, i.e. $\Delta c\approx0.05$ m/s.</span>


**q5.** A5 — Le modèle décrit-il correctement les mesures ? Quelles sont les principales sources d'incertitude ?

<span style="color:blue">A5 — Does the model describe the measurements correctly? What are the main sources of uncertainty?</span>

> [!tip]- 💡 Coup de pouce
> **Critères {\color{blue}(Criteria)}**
>
> Linéarité, ordonnée à l'origine proche de $0$, résidus petits devant l'incertitude de $f_n$.
>
> <span style="color:blue">Linearity, intercept close to $0$, residuals small compared with the uncertainty on $f_n$.</span>


> [!success]- ✅ Correction
> **Réponse attendue {\color{blue}(Expected answer)}**
>
> Oui : points alignés ($R^2>0{,}999$), ordonnée à l'origine compatible avec $0$. Sources d'écart : repérage de la résonance (pic large), longueur effective incertaine, vibreur quasi fixe, masse propre du ressort, spires qui se touchent ou tension résiduelle non uniforme.
>
> <span style="color:blue">Yes: aligned points ($R^2>0.999$), intercept compatible with $0$. Sources of deviation: locating the resonance (broad peak), uncertain effective length, quasi-fixed vibrator, spring's own mass, touching coils or non-uniform residual tension.</span>


> [!example]- 📝 Solution détaillée
> **Discussion {\color{blue}(Discussion)}**
>
> Un petit décalage systématique vers le bas de $f_n$ est attendu si la longueur effective dépasse $L$. Pousser l'étudiant à relier l'écart à une hypothèse du modèle (extrémités parfaitement fixes, milieu homogène non dispersif).
>
> <span style="color:blue">A small systematic downward shift of $f_n$ is expected if the effective length exceeds $L$. Push students to link the deviation to a model hypothesis (perfectly fixed ends, homogeneous non-dispersive medium).</span>


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex5-corde-fixee-a-ses-deux-extremites-et-ondes-stationnaires|Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex12-adaptation-d-impedance-lame-quart-d-onde-entre-deux-cordes|Exercice 12 — Adaptation d'impédance : lame quart d'onde entre deux cordes]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres-color-blue-part-d-compatibility-of-wavelengths-with-the-normal-mode-model|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres {\color{blue}(Part D — Compatibility of wavelengths with the normal-mode model)}]] · [[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex1-ondes-sur-un-ressort-long-slinky-filmees-au-ralenti-impulsions-reflexions-et-modes-propres|Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex13-corde-pincee-timbre-harmoniques-absents-et-energie-des-modes|Exercice 13 — Corde pincée : timbre, harmoniques absents et énergie des modes]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex14-corde-de-piano-raide-dispersion-et-inharmonicite|Exercice 14 — Corde de piano raide : dispersion et inharmonicité]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex16-masse-en-bout-de-corde-condition-aux-limites-dynamique-et-equation-transcendante|Exercice 16 — Masse en bout de corde : condition aux limites dynamique et équation transcendante]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde-color-blue-part-b-effect-of-tension-on-the-normal-modes-of-a-string|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde {\color{blue}(Part B — Effect of tension on the normal modes of a string)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex5-synthese-scientifique-du-tp-color-blue-scientific-summary-of-the-lab|Exercice 5 — Synthèse scientifique du TP {\color{blue}(Scientific summary of the lab)}]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex6-experience-de-melde-oscillations-forcees-d-une-corde-resonance|Exercice 6 — Expérience de Melde, oscillations forcées d'une corde, résonance]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex15-corde-amortie-attenuation-facteur-de-qualite-et-resonance-de-melde|Exercice 15 — Corde amortie : atténuation, facteur de qualité et résonance de Melde]]

