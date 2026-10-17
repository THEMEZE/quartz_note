---
title: "Exercice 6 — Expérience de Melde, oscillations forcées d'une corde, résonance"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td1_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_ex1_coup_de_pouce.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_coup_de_pouce)</a> · <a href="/pdfs/td1_ex1_solution_detaillee.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_solution_detaillee)</a> · <a href="/pdfs/td1_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_PhV212_fiche)</a> · <a href="/pdfs/td1_ex1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_ex1_fiche)</a> · <a href="/pdfs/td1_exs_maison_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_exs_maison_fiche)</a>

### Exercice 6. Expérience de Melde, oscillations forcées d'une corde, résonance *(facultatif)*

Une corde $OA$ de longueur $\ell = 50\text{ cm}$ et $\mu = 0.02\text{ kg}\cdot\text{m}^{-1}$ est tendue avec $F = 50\text{ N}$. Un vibreur impose en $x=0$ : $y(0,t) = a e^{j\omega t}$. On pose $k = \omega\sqrt{\mu/F}$. La corde est fixée en $x=\ell$.

<p style="text-align:center"><a href="/figures/td1_ex5_phv212_corde_melde.svg" target="_blank" rel="noopener"><img src="/figures/td1_ex5_phv212_corde_melde.svg" alt="Corde de Melde en régime forcé." loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>

**q1.** Établir en régime forcé l'équation $y(x,t)$ du mouvement de la corde en tout point $M(x)$ à l'instant $t$. Conclusion.

> [!tip]- 💡 Coup de pouce
> **Forme complexe**
>
> Cherchez une solution complexe $\underline{y}(x,t) = \underline{Y}(x)e^{j\omega t}$ vérifiant $\underline{Y}(0) = a$ et $\underline{Y}(\ell) = 0$.


> [!question]- 🔭 Aller plus loin — Licence : Résolution du régime forcé pour une corde vibrante fixée à une extrémité
> **1. Établissement de l'équation du mouvement $y(x,t)$**
>
> La corde obéit à l'équation de d'Alembert unidimensionnelle :
> $$\frac{\partial^2 y}{\partial x^2} - \frac{1}{c^2}\frac{\partial^2 y}{\partial t^2} = 0 \quad \text{avec } c = \sqrt{\frac{F}{\mu}} = \sqrt{\frac{50}{0{,}02}} = 50\text{ m}\cdot\text{s}^{-1}$$
>
> En régime sinusoïdal forcé établi à la pulsation $\omega$ imposée par le vibreur, la solution est de la forme $y(x,t) = Y(x)e^{i\omega t}$.
> En injectant cette forme dans l'équation de d'Alembert :
> $$\frac{\mathrm{d}^2 Y}{\mathrm{d}x^2} + k^2 Y(x) = 0 \quad \text{avec } k = \frac{\omega}{c} = \omega\sqrt{\frac{\mu}{F}}$$
>
> La solution générale de cette EDO spatiale s'écrit :
> $$Y(x) = A \cos(kx) + B \sin(kx)$$
>
> On applique les conditions aux limites (CL) :
>
>
> - **En $x = 0$ :** $y(0,t) = a e^{i\omega t} \implies Y(0) = a \implies A = a$.
> - **En $x = \ell$ (extrémité fixée) :** $y(\ell,t) = 0 \implies Y(\ell) = 0$.
>
>
>
> D'où :
> $$a \cos(k\ell) + B \sin(k\ell) = 0 \implies B = -a \frac{\cos(k\ell)}{\sin(k\ell)}$$
>
> En réinjectant $B$ dans l'expression de $Y(x)$ :
> $$Y(x) = a \left[ \cos(kx) - \frac{\cos(k\ell)}{\sin(k\ell)} \sin(kx) \right] = a \frac{\sin(k\ell)\cos(kx) - \cos(k\ell)\sin(kx)}{\sin(k\ell)} = a \frac{\sin\big(k(\ell - x)\big)}{\sin(k\ell)}$$
>
> L'expression complexe du déplacement transversal est donc :
> $$y(x,t) = a \frac{\sin\big(k(\ell - x)\big)}{\sin(k\ell)} e^{i\omega t}$$
>
> **Conclusion :**
>
>
> - Il s'agit d'une **onde stationnaire** : tous les points de la corde oscillent en phase (ou opposition de phase) à la pulsation $\omega$, avec un profil d'amplitude spatiale $Y(x)$.
> - **Résonance :** Lorsque $\sin(k\ell) = 0$, c'est-à-dire pour $k\ell = n\pi$ ($n \in \mathbb{N}^*$), l'amplitude $Y(x)$ tend vers l'infini (en l'absence d'amortissement). Les pulsations de résonance sont $\omega_n = \frac{n\pi c}{\ell}$.
> - **Noeuds et Ventres :** La corde présente des noeuds de vibration fixes aux positions $x$ telles que $k(\ell - x) = p\pi$.


> [!question]- 🔭 Aller plus loin — Licence : Lustification rigoureuse du postulat $y(x,t) = Y(x)e^{i\omega t}$

> **1. Linéarité et invariance par translation temporelle**
>
> L'équation de d'Alembert $\mathcal{L}[y] = 0$ (où $\mathcal{L} = \frac{\partial^2}{\partial x^2} - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}$) est un opérateur différentiel linéaire à coefficients constants.
>
>
>
> - **Invariance temporelle :** L'opérateur $\mathcal{L}$ commute avec l'opérateur de dérivation temporelle $\frac{\partial}{\partial t}$. Les fonctions propres de la dérivation temporelle $\frac{\partial}{\partial t}$ sont les fonctions exponentielles $t \mapsto e^{s t}$ avec $s \in \mathbb{C}$.
> - **Excitation harmonique :** La source impose une sollicitation monochromatique $y(0,t) = a e^{i\omega t}$ à la frontière $x=0$.
>
>
>
> **2. Théorème de la réponse en régime permanent (Analyse spectrale)**
>
> Par linéarité, la réponse d'un système linéaire invariant dans le temps (SLIT) à une entrée de la forme $e^{i\omega t}$ est obligatoirement, en régime permanent établi (après extinction des régimes transitoires propres), une sortie à la **même fréquence** $\omega$, simplement modulée en amplitude et en phase selon la position spatiale :
> $$y(x,t) = Y(x) e^{i\omega t}$$
> où $Y(x) \in \mathbb{C}$ est l'amplitude complexe englobant le module $|Y(x)|$ et le déphasage spatial $\arg(Y(x))$.
>
> **3. Interprétation en termes d'ondes progressives croisées**
>
> En utilisant la représentation complexe, une onde stationnaire s'interprète comme la superposition d'une onde incidente et d'une onde réfléchie de même pulsation $\omega$ :
> $$y(x,t) = C_1 e^{i(\omega t - kx)} + C_2 e^{i(\omega t + kx)} = \underbrace{\left( C_1 e^{-ikx} + C_2 e^{ikx} \right)}_{Y(x)} e^{i\omega t}$$
>
> Cette factorisation isole complètement la dépendance temporelle imposée par la source de la structure spatiale $Y(x)$ imposée par la géométrie du milieu et les conditions aux limites.


> [!success]- ✅ Correction
> **Résultat**
>
> $y(x,t) = a \dfrac{\sin(k(\ell-x))}{\sin(k\ell)} \cos(\omega t)$ (en partie réelle).
> L'onde complexe établie est une onde stationnaire forcée par le vibreur.


> [!example]- 📝 Solution détaillée
> **Résolution complète**
>
> En régime sinusoïdal forcé à la pulsation $\omega$, on pose $\underline{y}(x,t) = \underline{Y}(x) e^{j\omega t}$.
> L'équation de d'Alembert impose : $\dfrac{d^2\underline{Y}}{dx^2} + k^2 \underline{Y} = 0 \implies \underline{Y}(x) = C_1 \cos(kx) + C_2 \sin(kx)$.
>
>
>
> - Condition en $x=\ell$ : $\underline{Y}(\ell) = 0 \implies C_1 \cos(k\ell) + C_2 \sin(k\ell) = 0 \implies C_1 = -C_2 \tan(k\ell)$.
> - Ainsi : $\underline{Y}(x) = C_2 \left[\sin(kx) - \tan(k\ell)\cos(kx)\right] = C_2 \dfrac{\sin(k(x-\ell))}{\cos(k\ell)}$.
> - Condition en $x=0$ : $\underline{Y}(0) = a \implies -C_2 \tan(k\ell) = a \implies C_2 = -a \cot(k\ell)$.
>
>
> On obtient : $\underline{Y}(x) = a \dfrac{\sin(k(\ell-x))}{\sin(k\ell)}$. \\
>
> **Conclusion :** Le mouvement est celui d'une onde stationnaire d'amplitude spatiale $A(x) = a \left|\dfrac{\sin(k(\ell-x))}{\sin(k\ell)}\right|$.


**q2.** Pour les fréquences $f < f_1$, seul existe un nœud de vibration en $A$. Calculer $f_1$.

> [!tip]- 💡 Coup de pouce
> **Fréquence limite**
>
> $f_1$ correspond à la fréquence pour laquelle la demi-longueur d'onde égale la longueur de la corde ($\ell = \lambda/2$).


> [!success]- ✅ Correction
> **Résultat**
>
> $c = 50\text{ m/s} \implies f_1 = \dfrac{c}{2\ell} = 50\text{ Hz}$.


> [!example]- 📝 Solution détaillée
> **Application numérique**
>
> $c = \sqrt{\dfrac{F}{\mu}} = \sqrt{\dfrac{50}{0.02}} = 50\text{ m/s}$.
> La première fréquence de résonance (fondamental) est $f_1 = \dfrac{c}{2\ell} = \dfrac{50}{2 \times 0.50} = 50\text{ Hz}$.


**q3.** Pour les fréquences $f \ge f_1$, calculer l'amplitude des ventres de vibration. Pour quelles fréquences observe-t-on la résonance d'amplitude ?

> [!tip]- 💡 Coup de pouce
> **Dénominateur nul**
>
> L'amplitude devient infinie (en l'absence d'amortissement) quand le dénominateur $\sin(k\ell)$ s'annule.


> [!question]- 🔭 Aller plus loin — Licence : Prise en compte de l'amortissement
> En réalité, les frottements fluides introduisent une partie imaginaire à la vitesse de propagation $c$, ce qui borne l'amplitude à la résonance à une valeur finie inversement proportionnelle au coefficient d'amortissement.


> [!success]- ✅ Correction
> **Résultat**
>
> Amplitude d'un ventre : $A_v = \dfrac{a}{|\sin(k\ell)|}$.
> Résonance d'amplitude si $\sin(k\ell) = 0$, soit $f = N f_1 = N \times 50\text{ Hz}$ ($N \in \mathbb{N}^*$).


> [!example]- 📝 Solution détaillée
> **Analyse de la résonance**
>
> Les ventres de vibration correspondent aux maxima du sinus au numérateur ($|\sin(k(\ell-x))| = 1$).
> L'amplitude au niveau des ventres est donc :
> $$A_{\text{ventre}} = \frac{a}{|\sin(k\ell)|}$$
> Le phénomène de résonance d'amplitude a lieu lorsque le dénominateur tend vers zéro :
> $$\sin(k\ell) = 0 \implies k\ell = N\pi \implies \frac{2\pi f}{c}\ell = N\pi \implies f = N \frac{c}{2\ell} = N f_1$$
> On observe la résonance pour toutes les fréquences harmoniques $f_N = N \times 50\text{ Hz}$ ($50\text{ Hz}, 100\text{ Hz}, 150\text{ Hz}, \dots$).


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex15-corde-amortie-attenuation-facteur-de-qualite-et-resonance-de-melde|Exercice 15 — Corde amortie : atténuation, facteur de qualité et résonance de Melde]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales)]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde]] · [[physique/IPSA/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex3-mesurer-la-vitesse-de-la-lumiere-avec-un-four-a-micro-ondes-et-du-chocolat|Exercice 3 — Mesurer la vitesse de la lumière avec un four à micro-ondes et du chocolat]]

