---
title: "Exercice 13 — Corde pincée : timbre, harmoniques absents et énergie des modes"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a>

### Exercice 13. Corde pincée : timbre, harmoniques absents et énergie des modes *(facultatif)*

Une corde de guitare de longueur $L$, de masse linéique $\mu$, tendue avec la force $F$ ($c=\sqrt{F/\mu}$), est
fixée à ses deux extrémités $y(0,t)=y(L,t)=0$. À $t=0$, on la pince en $x=d$ ($0<d<L$) en l'écartant d'une hauteur $h\ll L$
de sorte que son profil est formé de deux segments de droite, puis on la lâche **sans vitesse initiale** :
$$y(x,0)=\begin{cases}h\,\dfrac xd & 0\le x\le d\\[2mm] h\,\dfrac{L-x}{L-d} & d\le x\le L\end{cases},\qquad\partial_ty(x,0)=0.$$
On note $\beta=d/L$, $\omega_n=n\pi c/L$ et $f_1=c/(2L)$.

**q1.** (a) Justifier la forme $y(x,t)=\sum_n(A_n\cos\omega_nt+B_n\sin\omega_nt)\sin\dfrac{n\pi x}L$ et montrer que la condition $\partial_ty(x,0)=0$ impose $B_n=0$ pour tout $n$.

(b) Établir l'expression de $A_n=b_n$ en fonction de $h$, $L$, $\beta$ et $n$ (on pourra dériver deux fois le profil initial).

> [!tip]- 💡 Coup de pouce
> **Séparation des variables**
>
> Cherchez $y=X(x)\,\Theta(t)$ dans l'équation de d'Alembert ; les conditions $X(0)=X(L)=0$ imposent $X\propto\sin(n\pi x/L)$.
>
> **Dérivée seconde du profil**
>
> La pente passe de $h/d$ à $-h/(L-d)$ en $x=d$ : $y''(x,0)=-\dfrac{hL}{d(L-d)}\,\delta(x-d)$. Utilisez $\int g\sin(ax)=-\dfrac1{a^2}\int g''\sin(ax)$ avec $a=n\pi/L$.


**q2.** (a) Pincement au milieu ($\beta=1/2$) : quels harmoniques sont présents ? Comment décroissent leurs amplitudes ? Que se passe-t-il pour $\beta=1/3$ ? Pour $\beta=1/5$ ?

(b) Pincement près du chevalet ($\beta\ll1$) : montrer que $|b_n|\simeq\dfrac{2h}{\pi n}$ tant que $n\beta\ll1$. Interpréter qualitativement le timbre « brillant ».

(c) Montrer que la corde est périodique, de période $T=2L/c$, et que $y(x,T/2)=-y(L-x,0)$. Décrire le mouvement avec la solution de d'Alembert : à $t=0^+$, de quoi est composé le signal ?

> [!tip]- 💡 Coup de pouce
> **Harmoniques absents**
>
> $b_n=0$ si $\sin(n\pi\beta)=0$, c'est-à-dire si $n\beta$ est entier.
>
> **Petits $\beta$**
>
> Pour $n\beta\ll1$, $\sin(n\pi\beta)\simeq n\pi\beta$ et $1-\beta\simeq1$.
>
> **Solution de d'Alembert**
>
> Prolongez $y_0$ à $\mathbb R$ de façon impaire et $2L$-périodique : $y(x,t)=\tfrac12\big[f(x-ct)+f(x+ct)\big]$. Chaque morceau de profil se divise en deux demi-profils qui se propagent en sens opposés.


**q3.** (a) Calculer l'énergie initiale $E_0$ de la corde en fonction de $F$, $h$, $L$ et $\beta$.

(b) Exprimer l'énergie $E_n$ du mode $n$. Montrer que $\sum_nE_n=E_0$. Quelle est la proportion d'énergie dans chaque mode ?

(c) Application : $L=0{,}65$ m, $f_1=110$ Hz, $\mu=5{,}0$ g/m, $h=3{,}0$ mm, $\beta=1/5$. Calculer $c$, $F$, $T$, $E_0$, les amplitudes $b_1,\dots,b_5$ et la part d'énergie dans les quatre premiers modes. Comparer avec le pincement au milieu.

> [!tip]- 💡 Coup de pouce
> **Énergie initiale**
>
> $E_0=\dfrac F2\displaystyle\int_0^L(y_0')^2\mathrm dx$ avec deux pentes constantes : $h/d$ sur $[0,d]$ et $-h/(L-d)$ sur $[d,L]$.
>
> **Énergie modale**
>
> $E_n=\tfrac14\mu L\omega_n^2b_n^2$ avec $\mu\omega_1^2=F\pi^2/L^2$. La somme $\sum\sin^2(n\pi\beta)/n^2=\pi^2\beta(1-\beta)/2$ permet de conclure.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex5-corde-fixee-a-ses-deux-extremites-et-ondes-stationnaires|Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex14-corde-de-piano-raide-dispersion-et-inharmonicite|Exercice 14 — Corde de piano raide : dispersion et inharmonicité]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex16-masse-en-bout-de-corde-condition-aux-limites-dynamique-et-equation-transcendante|Exercice 16 — Masse en bout de corde : condition aux limites dynamique et équation transcendante]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales-color-blue-part-a-normal-modes-of-a-helical-spring-longitudinal-waves|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde-color-blue-part-b-effect-of-tension-on-the-normal-modes-of-a-string|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde {\color{blue}(Part B — Effect of tension on the normal modes of a string)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres-color-blue-part-d-compatibility-of-wavelengths-with-the-normal-mode-model|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres {\color{blue}(Part D — Compatibility of wavelengths with the normal-mode model)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex5-synthese-scientifique-du-tp-color-blue-scientific-summary-of-the-lab|Exercice 5 — Synthèse scientifique du TP {\color{blue}(Scientific summary of the lab)}]]

