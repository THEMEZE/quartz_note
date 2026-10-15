---
title: "Exercice 14 — Corde de piano raide : dispersion et inharmonicité"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · [📄 Énoncé](/pdfs/td1_PhV212_enonce.pdf)

### Exercice 14. Corde de piano raide : dispersion et inharmonicité *(facultatif)*

Une corde de piano en acier (diamètre $d_c=1{,}0$ mm, masse volumique $\rho=7800$ kg/m$^3$, module d'Young
$E=2{,}0\times10^{11}$ Pa) de longueur $L=0{,}63$ m est tendue par la force $F$ de façon que sa fréquence fondamentale
**idéale** soit $f_0=c/(2L)=261{,}6$ Hz (note $do_3$), avec $c=\sqrt{F/\mu}$. Contrairement à la corde idéale
de d'Alembert, une corde métallique épaisse **résiste à la flexion** : en plus de la tension, la corde exerce une force
élastique de rappel de flexion. Pour de petits mouvements transversaux, on admet l'équation
$$\mu\,\frac{\partial^2y}{\partial t^2}=F\,\frac{\partial^2y}{\partial x^2}-EI\,\frac{\partial^4y}{\partial x^4},\qquad I=\frac{\pi d_c^4}{64},$$
où $I$ est le moment quadratique de la section. Les deux extrémités sont **appuyées** : $y=0$ et $\partial_x^2y=0$ en $x=0$ et $x=L$.

**q1.** (a) Vérifier l'homogénéité de l'équation donnée. Que devient-elle pour $EI\to0$ ? Pour quelles longueurs d'onde le terme de raideur est-il négligeable ?

(b) Déterminer la relation de dispersion $\omega(k)$ pour une onde plane $y=\Re\,[a\,\mathrm e^{j(\omega t-kx)}]$. Exprimer la vitesse de phase $v_\varphi(k)$.

> [!tip]- 💡 Coup de pouce
> **Dimensions**
>
> $[\mu\,\partial_t^2y]=\mathrm{kg\,m^{-1}\cdot m\,s^{-2}}=\mathrm{N\,m^{-1}}$ : toutes les densités de force linéique doivent avoir cette dimension.
>
> **Dispersion**
>
> Remplacez $\partial_t^2\to-\omega^2$, $\partial_x^2\to-k^2$, $\partial_x^4\to k^4$ et factorisez par $\mu$.


**q2.** (a) Montrer que les modes propres s'écrivent $y_n\propto\sin\dfrac{n\pi x}L\cos(\omega_nt+\phi_n)$ et que les fréquences propres sont $f_n=nf_0\sqrt{1+Bn^2}$ avec $B=\dfrac{\pi^2EI}{FL^2}$.

(b) Établir $f_n\simeq nf_0\left(1+\dfrac{Bn^2}2\right)$ et exprimer l'écart $\Delta_n=1200\log_2\dfrac{f_n}{nf_0}$ en cents.

> [!tip]- 💡 Coup de pouce
> **Conditions aux limites appuyées**
>
> $y=0$ et $y''=0$ en $x=0$ et $x=L$ : essayez $Y(x)=\sin(kx)$ ; $Y''=-k^2Y$ s'annule avec $Y$.
>
> **Valeur de $k_n$**
>
> $\sin(kL)=0\Rightarrow k_n=n\pi/L$. Reportez dans $\omega(k)$ ; $\dfrac{EI}Fk_n^2=Bn^2$.


**q3.** (a) Calculer $c$, $\mu$, $F$, $I$, $EI$, le coefficient $B$ et la longueur d'onde critique $\lambda_c$. À partir de quel rang $n$ le terme de raideur domine-t-il ($Bn^2\sim1$) ?

(b) Calculer $f_1$, $f_2$, $f_5$, $f_{10}$ et les écarts correspondants en cents.

(c) Montrer que la vitesse de groupe est $v_g=c\,\dfrac{1+2\kappa k^2}{\sqrt{1+\kappa k^2}}$ avec $\kappa=EI/F$. La calculer pour $n=10$ et la comparer à $c$ et à $v_\varphi$.

(d) Expliquer pourquoi l'accordeur doit « étirer » l'accord : quelle note doit-il choisir pour la note située une octave au-dessus de $do_3$ si la $2^{\text{e}}$ harmonique de $do_3$ est à $f_2$ ?

> [!tip]- 💡 Coup de pouce
> **Chaîne de calculs**
>
> $c=2Lf_0$ ; $\mu=\rho\pi d_c^2/4$ ; $F=\mu c^2$ ; $I=\pi d_c^4/64$ ; $B=\pi^2EI/(FL^2)$ ; $n_B=1/\sqrt B$.
>
> **Vitesse de groupe**
>
> $\omega=ck\sqrt{1+\kappa k^2}$ : dérivez par rapport à $k$ (dérivée d'un produit).


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex15-corde-amortie-attenuation-facteur-de-qualite-et-resonance-de-melde|Exercice 15 — Corde amortie : atténuation, facteur de qualité et résonance de Melde]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex5-corde-fixee-a-ses-deux-extremites-et-ondes-stationnaires|Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex13-corde-pincee-timbre-harmoniques-absents-et-energie-des-modes|Exercice 13 — Corde pincée : timbre, harmoniques absents et énergie des modes]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex16-masse-en-bout-de-corde-condition-aux-limites-dynamique-et-equation-transcendante|Exercice 16 — Masse en bout de corde : condition aux limites dynamique et équation transcendante]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales-color-blue-part-a-normal-modes-of-a-helical-spring-longitudinal-waves|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde-color-blue-part-b-effect-of-tension-on-the-normal-modes-of-a-string|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde {\color{blue}(Part B — Effect of tension on the normal modes of a string)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres-color-blue-part-d-compatibility-of-wavelengths-with-the-normal-mode-model|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres {\color{blue}(Part D — Compatibility of wavelengths with the normal-mode model)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex5-synthese-scientifique-du-tp-color-blue-scientific-summary-of-the-lab|Exercice 5 — Synthèse scientifique du TP {\color{blue}(Scientific summary of the lab)}]]

