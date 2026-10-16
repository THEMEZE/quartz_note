---
title: "Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a>

### Exercice 9. Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet *(facultatif)*

Une corde homogène de longueur $L$ et de masse linéique $\mu$ est suspendue verticalement par son extrémité supérieure (fixe). Son extrémité inférieure est libre. Soit $g$ l'accélération de la pesanteur.

On repère un point de la corde par son abscisse $x\in[0,L]$, mesurée **vers le haut** à partir de l'extrémité libre (donc $x=0$ est l'extrémité inférieure et $x=L$ le point de suspension). Le déplacement transversal (horizontal) est noté $y(x,t)$ ; on le suppose petit.

Ici la tension n'est pas constante : c'est le poids de la partie de corde située **sous** le point considéré qui la crée.

**q1.** Montrer que la tension vaut $F(x)=\mu g\,x$ pour la corde à l'équilibre. Puis, en appliquant le PFD au tronçon $[x,x+\mathrm{d}x]$ et en projetant sur l'horizontale, établir l'équation
$$\frac{\partial^2y}{\partial t^2}=g\,\frac{\partial}{\partial x}\!\left(x\,\frac{\partial y}{\partial x}\right).$$

> [!tip]- 💡 Coup de pouce
> **Équilibre vertical**
>
> Le tronçon $[0,x]$ est en équilibre sous son poids $\mu g x$ et la tension exercée par la corde au-dessus.
>
> **Composante horizontale de la tension**
>
> La corde est presque verticale : la tension est verticale à l'ordre 0 et sa composante horizontale vaut $F(x)\,\partial_x y$ à l'ordre 1. Le poids n'a pas de composante horizontale.


**q2.** Localement, pour des ondes de longueur d'onde très inférieure à $x$, l'équation ressemble à une équation de d'Alembert. En déduire la célérité locale $c(x)$. Où est-elle nulle ? maximale ? Justifier que le temps mis par une impulsion pour aller de l'extrémité libre à la suspension est $\tau=\displaystyle\int_0^L\dfrac{\mathrm{d}x}{c(x)}$, puis le calculer. Application numérique pour $L=10\ \text{m}$ et comparaison avec le temps de chute libre.

> [!tip]- 💡 Coup de pouce
> **Identification**
>
> Comparer $\partial_t^2y=g\,x\,\partial_x^2y+\dots$ avec $\partial_t^2y=c^2\partial_x^2y$. Pour le temps de trajet : un petit déplacement $\mathrm{d}x$ prend le temps $\mathrm{d}t=\mathrm{d}x/c(x)$.


**q3.** Une bosse est créée à l'extrémité libre ($x=0$) à $t=0$. Établir l'équation $\dfrac{\mathrm{d}x_b}{\mathrm{d}t}=\sqrt{g\,x_b}$ pour la position $x_b(t)$ de la bosse, l'intégrer, et montrer que la bosse monte avec une accélération constante que l'on précisera. Vérifier que $x_b(\tau)=L$.

> [!tip]- 💡 Coup de pouce
> **Changement de variable**
>
> Poser $u=\sqrt{x_b}$. Alors $\dfrac{\mathrm{d}u}{\mathrm{d}t}=\dfrac{1}{2u}\dfrac{\mathrm{d}x_b}{\mathrm{d}t}$.


**q4.** Modes propres. On cherche $y(x,t)=Y(x)\cos(\omega t+\phi)$. Établir l'équation différentielle vérifiée par $Y$. Montrer que le changement de variable $u=2\omega\sqrt{x/g}$ ramène cette équation à l'équation de Bessel d'ordre $0$ : $Z''(u)+\dfrac{1}{u}Z'(u)+Z(u)=0$. On admet que la solution bornée en $x=0$ est $Y(x)=J_0(u)$.

> [!tip]- 💡 Coup de pouce
> **Équation en $Y$**
>
> Remplacer dans l'équation de la question 1 : $-\omega^2Y=g\,(xY''+Y')$.
>
> **Dérivées**
>
> Avec $u=\alpha\sqrt{x}$ et $\alpha=2\omega/\sqrt g$ : $\dfrac{\mathrm{d}u}{\mathrm{d}x}=\dfrac{\alpha^2}{2u}$.


**q5.** La suspension est fixe : $Y(L)=0$. En déduire les pulsations propres $\omega_n$ en fonction des zéros $j_{0,n}$ de $J_0$ ($j_{0,1}\approx2{,}405$, $j_{0,2}\approx5{,}520$, $j_{0,3}\approx8{,}654$). Calculer $f_1$, $f_2$, $f_3$ pour $L=10\ \text{m}$ et les rapports $f_n/f_1$. Comparer avec une corde tendue de tension constante et conclure.

**q6.** (*) Effet de fouet. On admet que, pour une onde de longueur d'onde très inférieure à la distance $x$ au bout libre, il n'y a pas de réflexion notable et que la puissance moyenne transportée est conservée : $\mathcal{P}=Z(x)\,\langle(\partial_t y)^2\rangle=\text{cste}$, avec $Z(x)=\sqrt{F(x)\mu}$. Comment varie l'amplitude de la vitesse transversale $v_m(x)$ d'une onde qui descend vers l'extrémité libre ? Que se passe-t-il quand $x\to0$ ? Faire le lien avec le claquement d'un fouet.

> [!tip]- 💡 Coup de pouce
> **Impédance locale**
>
> $Z(x)=\mu\sqrt{g\,x}$. La conservation de $Z\,v_m^2$ donne $v_m$ en fonction de $x$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex4-equation-des-cordes-vibrantes-et-onde-progressive|Exercice 4 — Équation des cordes vibrantes et onde progressive]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex8-energie-et-puissance-d-une-onde-sur-une-corde-impedance-caracteristique|Exercice 8 — Énergie et puissance d'une onde sur une corde : impédance caractéristique]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex10-corde-discrete-chaine-de-masses-dispersion-coupure-et-vitesse-de-groupe|Exercice 10 — Corde discrète (chaîne de masses) : dispersion, coupure et vitesse de groupe]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex5-corde-fixee-a-ses-deux-extremites-et-ondes-stationnaires|Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex13-corde-pincee-timbre-harmoniques-absents-et-energie-des-modes|Exercice 13 — Corde pincée : timbre, harmoniques absents et énergie des modes]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex14-corde-de-piano-raide-dispersion-et-inharmonicite|Exercice 14 — Corde de piano raide : dispersion et inharmonicité]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex16-masse-en-bout-de-corde-condition-aux-limites-dynamique-et-equation-transcendante|Exercice 16 — Masse en bout de corde : condition aux limites dynamique et équation transcendante]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales-color-blue-part-a-normal-modes-of-a-helical-spring-longitudinal-waves|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde-color-blue-part-b-effect-of-tension-on-the-normal-modes-of-a-string|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde {\color{blue}(Part B — Effect of tension on the normal modes of a string)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres-color-blue-part-d-compatibility-of-wavelengths-with-the-normal-mode-model|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres {\color{blue}(Part D — Compatibility of wavelengths with the normal-mode model)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex5-synthese-scientifique-du-tp-color-blue-scientific-summary-of-the-lab|Exercice 5 — Synthèse scientifique du TP {\color{blue}(Scientific summary of the lab)}]]

