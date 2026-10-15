---
title: "Exercice 6 — Expérience de Melde, oscillations forcées d'une corde, résonance"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · [📄 Énoncé](/pdfs/td1_PhV212_enonce.pdf)

### Exercice 6. Expérience de Melde, oscillations forcées d'une corde, résonance *(facultatif)*

Une corde $OA$ de longueur $\ell = 50\text{ cm}$ et $\mu = 0.02\text{ kg}\cdot\text{m}^{-1}$ est tendue avec $F = 50\text{ N}$. Un vibreur impose en $x=0$ : $y(0,t) = a e^{j\omega t}$. On pose $k = \omega\sqrt{\mu/F}$. La corde est fixée en $x=\ell$.

[![Corde de Melde en régime forcé.](/figures/td1_ex5_phv212_corde_melde.svg)](/figures/td1_ex5_phv212_corde_melde.svg)

**q1.** Établir en régime forcé l'équation $y(x,t)$ du mouvement de la corde en tout point $M(x)$ à l'instant $t$. Conclusion.

> [!tip]- 💡 Coup de pouce
> **Forme complexe**
>
> Cherchez une solution complexe $\underline{y}(x,t) = \underline{Y}(x)e^{j\omega t}$ vérifiant $\underline{Y}(0) = a$ et $\underline{Y}(\ell) = 0$.


**q2.** Pour les fréquences $f < f_1$, seul existe un nœud de vibration en $A$. Calculer $f_1$.

> [!tip]- 💡 Coup de pouce
> **Fréquence limite**
>
> $f_1$ correspond à la fréquence pour laquelle la demi-longueur d'onde égale la longueur de la corde ($\ell = \lambda/2$).


**q3.** Pour les fréquences $f \ge f_1$, calculer l'amplitude des ventres de vibration. Pour quelles fréquences observe-t-on la résonance d'amplitude ?

> [!tip]- 💡 Coup de pouce
> **Dénominateur nul**
>
> L'amplitude devient infinie (en l'absence d'amortissement) quand le dénominateur $\sin(k\ell)$ s'annule.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex15-corde-amortie-attenuation-facteur-de-qualite-et-resonance-de-melde|Exercice 15 — Corde amortie : atténuation, facteur de qualité et résonance de Melde]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales-color-blue-part-a-normal-modes-of-a-helical-spring-longitudinal-waves|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde-color-blue-part-b-effect-of-tension-on-the-normal-modes-of-a-string|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde {\color{blue}(Part B — Effect of tension on the normal modes of a string)}]] · [[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex3-mesurer-la-vitesse-de-la-lumiere-avec-un-four-a-micro-ondes-et-du-chocolat|Exercice 3 — Mesurer la vitesse de la lumière avec un four à micro-ondes et du chocolat]]

