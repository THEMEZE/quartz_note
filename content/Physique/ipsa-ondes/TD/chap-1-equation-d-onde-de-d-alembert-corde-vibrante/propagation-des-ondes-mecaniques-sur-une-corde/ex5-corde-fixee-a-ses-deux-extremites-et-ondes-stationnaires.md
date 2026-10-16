---
title: "Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a>

### Exercice 5. Corde fixée à ses deux extrémités et ondes stationnaires

Une corde homogène, de masse linéique $\mu$ et de longueur $L$, est fixée en ses deux extrémités $A(x=0)$ et $B(x=L)$. La corde de tension $F$, écartée de sa position d'équilibre, est abandonnée à l'instant $t=0$. Le déplacement transversal $y(x,t)$ obéit à l'équation de d'Alembert :
$$\frac{\partial^2 y}{\partial x^2} = \frac{\mu}{F} \frac{\partial^2 y}{\partial t^2}$$

<p style="text-align:center"><a href="/figures/td1_ex4_phv212_corde_fixe.svg" target="_blank" rel="noopener"><img src="/figures/td1_ex4_phv212_corde_fixe.svg" alt="" loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>

**q1.** On admet la solution particulière $y(x,t) = f(x)\cdot g(t)$ (séparation des variables).
Montrer que $y(x,t) = A\cos(kx+\varphi)\cos(\omega t+\phi)$.
Quelle relation existe-t-il entre $k$, $\omega$ et la célérité $c$ ? (Relation de dispersion).

> [!tip]- 💡 Coup de pouce
> **Méthode simple**
>
> Injectez $y(x,t) = A\cos(kx+\varphi)\cos(\omega t+\phi)$ dans l'équation de d'Alembert, séparez les termes en $x$ et en $t$. Et on aura une relation entre $\omega$ , $k$ et $c$
>
> **Méthode de séparation**
>
> Injectez $y(x,t) = f(x)g(t)$ dans l'équation d'onde, séparez les termes en $x$ et en $t$ pour égaler chaque membre à une constante négative $-k^2$.


**q2.** Montrer que les fréquences de vibration sont des multiples entiers d'une fréquence fondamentale $f_1$ ($f_N = N f_1$). Exprimer $f_1$ en fonction de $F$, $L$ et $\mu$.

> [!tip]- 💡 Coup de pouce
> **Conditions aux limites**
>
> Appliquez les conditions aux limites $y(0,t) = 0$ et $y(L,t) = 0$ pour déterminer $k$ puis $f_N$.


**q3.** Application : Pour la 3ème corde de guitare ($\ell = 63$ cm, $\rho = 1200\text{ kg}\cdot\text{m}^{-3}$, $S = 0.42\text{ mm}^2$), calculer la tension $F$ pour $f_1 = 147$ Hz.

> [!tip]- 💡 Coup de pouce
> **Masse linéique**
>
> Calculez d'abord $\mu = \rho\cdot S$, puis isolez $F$ dans la formule de $f_1$.


**q4.** Exprimer, en fonction de la longueur $L$, les longueurs d'ondes possibles $\lambda_N$.

> [!tip]- 💡 Coup de pouce
> **Relation $k_N$ et $\lambda_N$
> **
>
> Utilisez $k_N = \dfrac{2\pi}{\lambda_N} = \dfrac{N\pi}{L}$.


**q5.** Exprimer $y_N(x,t)$ pour le mode $N$. Préciser le nombre et la position des nœuds et des ventres. Distance entre 2 ventres / 2 nœuds ?

> [!tip]- 💡 Coup de pouce
> **Positions récurrencielles**
>
> Les nœuds annulent le sinus ($\sin(k_N x) = 0$), les ventres le maximisent ($|\sin(k_N x)| = 1$).


**q6.** Dessiner la corde pour $N=1$ et $N=4$.

> [!tip]- 💡 Coup de pouce
> **Représentation**
>
> $N=1$ présente 1 fuseau (0 nœud interne), $N=4$ présente 4 fuseaux (3 nœuds internes).


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex12-adaptation-d-impedance-lame-quart-d-onde-entre-deux-cordes|Exercice 12 — Adaptation d'impédance : lame quart d'onde entre deux cordes]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales-color-blue-part-a-normal-modes-of-a-helical-spring-longitudinal-waves|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres-color-blue-part-d-compatibility-of-wavelengths-with-the-normal-mode-model|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres {\color{blue}(Part D — Compatibility of wavelengths with the normal-mode model)}]] · [[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex1-ondes-sur-un-ressort-long-slinky-filmees-au-ralenti-impulsions-reflexions-et-modes-propres|Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex13-corde-pincee-timbre-harmoniques-absents-et-energie-des-modes|Exercice 13 — Corde pincée : timbre, harmoniques absents et énergie des modes]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex14-corde-de-piano-raide-dispersion-et-inharmonicite|Exercice 14 — Corde de piano raide : dispersion et inharmonicité]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex16-masse-en-bout-de-corde-condition-aux-limites-dynamique-et-equation-transcendante|Exercice 16 — Masse en bout de corde : condition aux limites dynamique et équation transcendante]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde-color-blue-part-b-effect-of-tension-on-the-normal-modes-of-a-string|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde {\color{blue}(Part B — Effect of tension on the normal modes of a string)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex5-synthese-scientifique-du-tp-color-blue-scientific-summary-of-the-lab|Exercice 5 — Synthèse scientifique du TP {\color{blue}(Scientific summary of the lab)}]]

