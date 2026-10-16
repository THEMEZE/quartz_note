---
title: "Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td1_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_ex1_coup_de_pouce.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_coup_de_pouce)</a> · <a href="/pdfs/td1_ex1_solution_detaillee.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_solution_detaillee)</a> · <a href="/pdfs/td1_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_PhV212_fiche)</a> · <a href="/pdfs/td1_ex1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_ex1_fiche)</a> · <a href="/pdfs/td1_exs_maison_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_exs_maison_fiche)</a>

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


> [!success]- ✅ Correction
> **Résultat**
>
> $F(x)=\mu g x$ et $\mu\,\partial_t^2y=\partial_x\!\left(\mu g x\,\partial_x y\right)$, soit $\partial_t^2y=g\left(x\,\partial_x^2y+\partial_x y\right)$.


> [!example]- 📝 Solution détaillée
> **Établissement**
>
> - **Tension :** le tronçon $[0,x]$ (du bas jusqu'en $x$) est à l'équilibre : son poids $\mu g x$ est compensé par la tension $F(x)$ exercée par la partie supérieure. Donc $F(x)=\mu g x$, et $F(0)=0$ à l'extrémité libre.
> - **PFD horizontal :** sur le tronçon $[x,x+\mathrm{d}x]$ de masse $\mu\,\mathrm{d}x$, seules les tensions ont une composante horizontale : vers le haut (côté $x+\mathrm{d}x$) $+F(x+\mathrm{d}x)\,\partial_x y(x+\mathrm{d}x)$, vers le bas $-F(x)\,\partial_x y(x)$.
>   $$\mu\,\mathrm{d}x\,\partial_t^2y=F(x+\mathrm{d}x)\,\partial_x y(x+\mathrm{d}x,t)-F(x)\,\partial_x y(x,t)=\partial_x\!\left(F\,\partial_x y\right)\mathrm{d}x.$$
>
>
> On obtient $\mu\,\partial_t^2y=\partial_x(\mu g x\,\partial_x y)$, d'où l'équation cherchée. C'est la seule différence avec l'exercice 3 : la tension est à l'intérieur de la dérivée.


**q2.** Localement, pour des ondes de longueur d'onde très inférieure à $x$, l'équation ressemble à une équation de d'Alembert. En déduire la célérité locale $c(x)$. Où est-elle nulle ? maximale ? Justifier que le temps mis par une impulsion pour aller de l'extrémité libre à la suspension est $\tau=\displaystyle\int_0^L\dfrac{\mathrm{d}x}{c(x)}$, puis le calculer. Application numérique pour $L=10\ \text{m}$ et comparaison avec le temps de chute libre.

> [!tip]- 💡 Coup de pouce
> **Identification**
>
> Comparer $\partial_t^2y=g\,x\,\partial_x^2y+\dots$ avec $\partial_t^2y=c^2\partial_x^2y$. Pour le temps de trajet : un petit déplacement $\mathrm{d}x$ prend le temps $\mathrm{d}t=\mathrm{d}x/c(x)$.


> [!success]- ✅ Correction
> **Résultat**
>
> $c(x)=\sqrt{gx}=\sqrt{F(x)/\mu}$ : nulle en bas, maximale en haut. $\tau=2\sqrt{L/g}\approx2{,}02\ \text{s}$ pour $L=10\ \text{m}$, soit $\sqrt{2}$ fois le temps de chute libre ($1{,}43\ \text{s}$).


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> Le terme dominant à courte longueur d'onde est $g\,x\,\partial_x^2y$, donc $c^2(x)=g\,x$, ce qui est bien la relation $c=\sqrt{F/\mu}$ avec $F=\mu g x$.
>
> Le front de l'onde avance de $\mathrm{d}x=c(x)\,\mathrm{d}t$ pendant $\mathrm{d}t$, d'où
> $$\tau=\int_0^L\frac{\mathrm{d}x}{\sqrt{g\,x}}=\frac{1}{\sqrt g}\Big[2\sqrt{x}\Big]_0^L=2\sqrt{\frac{L}{g}}.$$
> L'intégrale converge malgré $c(0)=0$. Numériquement $\tau=2\sqrt{10/9{,}81}\approx2{,}02\ \text{s}$. Un aller-retour (réflexion sur la suspension fixe) dure $4\sqrt{L/g}\approx4{,}04\ \text{s}$.


**q3.** Une bosse est créée à l'extrémité libre ($x=0$) à $t=0$. Établir l'équation $\dfrac{\mathrm{d}x_b}{\mathrm{d}t}=\sqrt{g\,x_b}$ pour la position $x_b(t)$ de la bosse, l'intégrer, et montrer que la bosse monte avec une accélération constante que l'on précisera. Vérifier que $x_b(\tau)=L$.

> [!tip]- 💡 Coup de pouce
> **Changement de variable**
>
> Poser $u=\sqrt{x_b}$. Alors $\dfrac{\mathrm{d}u}{\mathrm{d}t}=\dfrac{1}{2u}\dfrac{\mathrm{d}x_b}{\mathrm{d}t}$.


> [!success]- ✅ Correction
> **Résultat**
>
> $\sqrt{x_b}=\tfrac{1}{2}\sqrt g\,t$, soit $x_b(t)=\tfrac{1}{4}g\,t^2=\tfrac{1}{2}\cdot\dfrac{g}{2}\,t^2$ : accélération constante $g/2$. Pour $t=\tau=2\sqrt{L/g}$ : $x_b=L$.


> [!example]- 📝 Solution détaillée
> **Intégration**
>
> La bosse se déplace à la célérité locale : $\dfrac{\mathrm{d}x_b}{\mathrm{d}t}=\sqrt{g\,x_b}$. Avec $u=\sqrt{x_b}$ : $2u\dot u=\sqrt g\,u$, donc $\dot u=\dfrac{\sqrt g}{2}$ et $u=\dfrac{\sqrt g}{2}\,t$ (avec $u(0)=0$). D'où
> $$x_b(t)=\frac{g}{4}\,t^2=\frac{1}{2}\left(\frac{g}{2}\right)t^2.$$
> La bosse monte comme un mobile d'accélération constante $g/2$. Pour $t=\tau=2\sqrt{L/g}$, $x_b=\dfrac{g}{4}\cdot\dfrac{4L}{g}=L$ : on retrouve le temps de la question 2.


**q4.** Modes propres. On cherche $y(x,t)=Y(x)\cos(\omega t+\phi)$. Établir l'équation différentielle vérifiée par $Y$. Montrer que le changement de variable $u=2\omega\sqrt{x/g}$ ramène cette équation à l'équation de Bessel d'ordre $0$ : $Z''(u)+\dfrac{1}{u}Z'(u)+Z(u)=0$. On admet que la solution bornée en $x=0$ est $Y(x)=J_0(u)$.

> [!tip]- 💡 Coup de pouce
> **Équation en $Y$**
>
> Remplacer dans l'équation de la question 1 : $-\omega^2Y=g\,(xY''+Y')$.
>
> **Dérivées**
>
> Avec $u=\alpha\sqrt{x}$ et $\alpha=2\omega/\sqrt g$ : $\dfrac{\mathrm{d}u}{\mathrm{d}x}=\dfrac{\alpha^2}{2u}$.


> [!success]- ✅ Correction
> **Résultat**
>
> $xY''+Y'+\dfrac{\omega^2}{g}Y=0$. Avec $u=2\omega\sqrt{x/g}$ : $\dfrac{\omega^2}{g}\left[Z''+\dfrac{1}{u}Z'+Z\right]=0$.


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> Avec $\alpha=2\omega/\sqrt g$, $u=\alpha\sqrt x$ et $\dfrac{\mathrm{d}u}{\mathrm{d}x}=\dfrac{\alpha^2}{2u}$ :
> $$Y'=\frac{\alpha^2}{2u}Z',\qquad Y''=\frac{\alpha^4}{4}\left(\frac{Z''}{u^2}-\frac{Z'}{u^3}\right).$$
> Avec $x=u^2/\alpha^2$ :
> $$xY''+Y'+\frac{\omega^2}{g}Z=\frac{\alpha^2}{4}\left(Z''-\frac{Z'}{u}\right)+\frac{\alpha^2}{2u}Z'+\frac{\alpha^2}{4}Z=\frac{\alpha^2}{4}\left[Z''+\frac{Z'}{u}+Z\right]=0,$$
> car $\omega^2/g=\alpha^2/4$. C'est l'équation de Bessel d'ordre $0$, dont la solution régulière en $u=0$ est $J_0(u)$. Le mode s'écrit $Y(x)=J_0\!\left(2\omega\sqrt{x/g}\right)$. L'extrémité libre $x=0$ est un ventre : $Y(0)=1$ et $Y'(0)$ est fini, cohérent avec $F(0)=0$.


**q5.** La suspension est fixe : $Y(L)=0$. En déduire les pulsations propres $\omega_n$ en fonction des zéros $j_{0,n}$ de $J_0$ ($j_{0,1}\approx2{,}405$, $j_{0,2}\approx5{,}520$, $j_{0,3}\approx8{,}654$). Calculer $f_1$, $f_2$, $f_3$ pour $L=10\ \text{m}$ et les rapports $f_n/f_1$. Comparer avec une corde tendue de tension constante et conclure.

> [!success]- ✅ Correction
> **Résultat**
>
> $\omega_n=\dfrac{j_{0,n}}{2}\sqrt{g/L}$. Pour $L=10\ \text{m}$ : $f_1\approx0{,}190\ \text{Hz}$, $f_2\approx0{,}435\ \text{Hz}$, $f_3\approx0{,}682\ \text{Hz}$ ; $f_n/f_1\approx1\ ;\ 2{,}30\ ;\ 3{,}60$. Le spectre n'est pas harmonique.


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> $Y(L)=J_0\!\left(2\omega\sqrt{L/g}\right)=0\Rightarrow2\omega_n\sqrt{L/g}=j_{0,n}$, donc $\omega_n=\dfrac{j_{0,n}}{2}\sqrt{\dfrac{g}{L}}$.
>
> Pour $L=10\ \text{m}$, $\sqrt{g/L}\approx0{,}990\ \text{s}^{-1}$ :
> $\omega_1\approx1{,}19\ \text{rad/s}$ ($f_1\approx0{,}190\ \text{Hz}$, $T_1\approx5{,}3\ \text{s}$), $\omega_2\approx2{,}73\ \text{rad/s}$ ($f_2\approx0{,}435\ \text{Hz}$), $\omega_3\approx4{,}29\ \text{rad/s}$ ($f_3\approx0{,}682\ \text{Hz}$).
>
> Rapports : $f_2/f_1\approx2{,}295$ et $f_3/f_1\approx3{,}598$. Pour une corde fixée aux deux bouts à tension constante, on aurait $f_n/f_1=n$ (exercice 4). Ici, la célérité varie avec $x$ et le spectre est **inharmonique**. Asymptotiquement $j_{0,n}\approx\left(n-\tfrac{1}{4}\right)\pi$, donc $f_n\approx\dfrac{n-1/4}{4}\sqrt{g/L}$ : les modes successifs sont presque équidistants, mais ce ne sont pas des multiples entiers de $f_1$.


**q6.** (*) Effet de fouet. On admet que, pour une onde de longueur d'onde très inférieure à la distance $x$ au bout libre, il n'y a pas de réflexion notable et que la puissance moyenne transportée est conservée : $\mathcal{P}=Z(x)\,\langle(\partial_t y)^2\rangle=\text{cste}$, avec $Z(x)=\sqrt{F(x)\mu}$. Comment varie l'amplitude de la vitesse transversale $v_m(x)$ d'une onde qui descend vers l'extrémité libre ? Que se passe-t-il quand $x\to0$ ? Faire le lien avec le claquement d'un fouet.

> [!tip]- 💡 Coup de pouce
> **Impédance locale**
>
> $Z(x)=\mu\sqrt{g\,x}$. La conservation de $Z\,v_m^2$ donne $v_m$ en fonction de $x$.


> [!success]- ✅ Correction
> **Résultat**
>
> $Z\,v_m^2=\text{cste}\Rightarrow v_m\propto x^{-1/4}$ : l'amplitude de la vitesse augmente quand l'onde descend et **diverge** quand $x\to0$ (en pratique, elle est limitée par le non-respect des petits angles et de la validité de l'approximation). C'est l'effet de fouet : une perturbation de faible énergie, en descendant le long d'une corde de tension décroissante, atteint des vitesses très élevées à l'extrémité libre.


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> $Z(x)v_m^2=\mu\sqrt{g\,x}\,v_m^2=\text{cste}\Rightarrow v_m(x)\propto x^{-1/4}$.
> Le rapport des vitesses entre $x=L$ et $x=L/100$ vaut $100^{1/4}\approx3{,}2$. Dans un fouet, le rétrécissement du diamètre (donc de $\mu$ et de la tension) vers l'extrémité amplifie encore le phénomène ; la vitesse en bout atteint des valeurs supersoniques, ce qui explique le claquement.
> Attention : l'hypothèse $\lambda\ll x$ cesse d'être valable près de $x=0$ et l'approximation des petits angles aussi. Le modèle indique la tendance, mais ne donne pas la valeur de la vitesse en $x=0$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex4-equation-des-cordes-vibrantes-et-onde-progressive|Exercice 4 — Équation des cordes vibrantes et onde progressive]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex8-energie-et-puissance-d-une-onde-sur-une-corde-impedance-caracteristique|Exercice 8 — Énergie et puissance d'une onde sur une corde : impédance caractéristique]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex10-corde-discrete-chaine-de-masses-dispersion-coupure-et-vitesse-de-groupe|Exercice 10 — Corde discrète (chaîne de masses) : dispersion, coupure et vitesse de groupe]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex5-corde-fixee-a-ses-deux-extremites-et-ondes-stationnaires|Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex13-corde-pincee-timbre-harmoniques-absents-et-energie-des-modes|Exercice 13 — Corde pincée : timbre, harmoniques absents et énergie des modes]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex14-corde-de-piano-raide-dispersion-et-inharmonicite|Exercice 14 — Corde de piano raide : dispersion et inharmonicité]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex16-masse-en-bout-de-corde-condition-aux-limites-dynamique-et-equation-transcendante|Exercice 16 — Masse en bout de corde : condition aux limites dynamique et équation transcendante]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales-color-blue-part-a-normal-modes-of-a-helical-spring-longitudinal-waves|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde-color-blue-part-b-effect-of-tension-on-the-normal-modes-of-a-string|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde {\color{blue}(Part B — Effect of tension on the normal modes of a string)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres-color-blue-part-d-compatibility-of-wavelengths-with-the-normal-mode-model|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres {\color{blue}(Part D — Compatibility of wavelengths with the normal-mode model)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex5-synthese-scientifique-du-tp-color-blue-scientific-summary-of-the-lab|Exercice 5 — Synthèse scientifique du TP {\color{blue}(Scientific summary of the lab)}]]

