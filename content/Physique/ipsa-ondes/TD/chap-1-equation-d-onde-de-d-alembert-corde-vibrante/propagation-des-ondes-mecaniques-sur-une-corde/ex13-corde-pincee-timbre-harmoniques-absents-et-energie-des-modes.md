---
title: "Exercice 13 — Corde pincée : timbre, harmoniques absents et énergie des modes"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td1_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_ex1_coup_de_pouce.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_coup_de_pouce)</a> · <a href="/pdfs/td1_ex1_solution_detaillee.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_solution_detaillee)</a> · <a href="/pdfs/td1_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_PhV212_fiche)</a> · <a href="/pdfs/td1_ex1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_ex1_fiche)</a> · <a href="/pdfs/td1_exs_maison_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_exs_maison_fiche)</a>

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


> [!success]- ✅ Correction
> **Résultat**
>
> $B_n=0$ et $\boxed{b_n=\dfrac{2h}{\pi^2\beta(1-\beta)}\,\dfrac{\sin(n\pi\beta)}{n^2}}$.


> [!example]- 📝 Solution détaillée
> **(a) Modes et conditions initiales**
>
> La séparation $y=X(x)\Theta(t)$ conduit à $X''+k^2X=0$ et $\Theta''+\omega^2\Theta=0$ avec $\omega=ck$ ; avec $X(0)=X(L)=0$, on trouve $X_n=\sin(k_nx)$, $k_n=n\pi/L$, $\omega_n=n\pi c/L$. L'équation étant linéaire, la solution générale est la somme sur $n$ avec $\Theta_n=A_n\cos\omega_nt+B_n\sin\omega_nt$. Alors $\partial_ty(x,0)=\sum_nB_n\omega_n\sin\frac{n\pi x}L=0$ pour tout $x$, et par orthogonalité des sinus, $B_n\omega_n=0$ donc $B_n=0$.
>
> **(b) Coefficients $b_n$**
>
> $y(x,0)=\sum_nb_n\sin(a x)$ avec $a=n\pi/L$ donne $b_n=\dfrac2L\displaystyle\int_0^Ly_0(x)\sin(ax)\,\mathrm dx$. Comme $y_0(0)=y_0(L)=0$, deux intégrations par parties donnent
> $$b_n=-\frac2{La^2}\int_0^Ly_0''(x)\sin(ax)\,\mathrm dx=\frac2{La^2}\cdot\frac{hL}{d(L-d)}\sin(ad)=\frac{2h\,\sin(n\pi d/L)}{a^2\,d\,(L-d)}.$$
> Avec $a^2=n^2\pi^2/L^2$ et $d(L-d)=L^2\beta(1-\beta)$ :
> $$\boxed{b_n=\frac{2h}{\pi^2\beta(1-\beta)}\,\frac{\sin(n\pi\beta)}{n^2}}.$$
> **Vérification** : pour $\beta=\tfrac12$ et $n=1$, $b_1=\dfrac{8h}{\pi^2}\approx0{,}81\,h$, valeur classique du mode fondamental d'une corde pincée en son milieu.


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


> [!success]- ✅ Correction
> **Résumé**
>
> $\beta=\tfrac12$ : seuls les harmoniques impairs, $b_n=\dfrac{8h}{\pi^2}\dfrac{(-1)^{(n-1)/2}}{n^2}$ ; $\beta=\tfrac13$ : $n=3,6,9,\dots$ absents ; $\beta=\tfrac15$ : $n=5,10,\dots$ absents. Près du chevalet, $|b_n|\simeq2h/(\pi n)$ décroît lentement : spectre riche. $y(x,T/2)=-y_0(L-x)$.


> [!example]- 📝 Solution détaillée
> **(c) Milieu, tiers et cinquième**
>
> Pour $\beta=\tfrac12$ : $\sin(n\pi/2)=0$ si $n$ pair, $=(-1)^{(n-1)/2}$ si $n$ impair, donc $b_n=\dfrac{8h}{\pi^2}\dfrac{(-1)^{(n-1)/2}}{n^2}$ (n impair) : les harmoniques de rang pair sont **absents** et les impairs décroissent en $1/n^2$ : son « rond ». Le fait que le milieu soit un ventre pour les modes impairs et un nœud pour les modes pairs l'explique : on ne peut pas exciter un mode en pinçant en l'un de ses **nœuds**. Pour $\beta=\tfrac13$, le point de pincement est un nœud des modes $n=3,6,9,\dots$ qui sont donc absents ; pour $\beta=\tfrac15$, ceux de rang $5,10,\dots$.
>
> **(d) Pincement près du chevalet**
>
> Pour $n\beta\ll1$ : $b_n\simeq\dfrac{2h}{\pi^2\beta}\dfrac{n\pi\beta}{n^2}=\dfrac{2h}{\pi n}$. Les amplitudes décroissent **seulement en $1/n$** jusqu'à $n\sim1/\beta$, puis en $1/n^2$ : beaucoup d'harmoniques élevés sont présents. À l'oreille, un spectre riche en aigus donne un son « brillant, nasillard » ; pincer au milieu, un spectre dominé par le fondamental, un son « rond ».
>
> **(e) Périodicité et solution de d'Alembert**
>
> Comme $\omega_n=n\omega_1$, $y(x,t+T)=y(x,t)$ avec $T=2\pi/\omega_1=2L/c$. À $t=T/2$, $\cos(n\omega_1T/2)=\cos(n\pi)=(-1)^n$ et $(-1)^n\sin\frac{n\pi x}L=-\sin\frac{n\pi(L-x)}L$, donc $y(x,T/2)=-y_0(L-x)$ : le triangle est **renversé et retourné** (image en miroir par rapport à $x=L/2$ et par rapport à l'axe). Avec d'Alembert, $y(x,t)=\tfrac12[f(x-ct)+f(x+ct)]$ où $f$ est le prolongement impair $2L$-périodique de $y_0$ : à $t=0^+$, le triangle de hauteur $h$ se scinde en deux triangles de hauteur $h/2$, qui s'écartent à la vitesse $c$ ; ils se réfléchissent aux extrémités fixes (avec changement de signe) et se recombinent.


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


> [!question]- 🔭 Aller plus loin — Licence : Pincement par une pointe finie : filtrage
> Si le doigt a une largeur $w$, le profil initial est arrondi sur $w$ : le coefficient $b_n$ est multiplié par $\dfrac{\sin(n\pi w/(2L))}{n\pi w/(2L)}$, un **sinus cardinal**. Montrer que cela atténue les harmoniques de rang $n\gtrsim2L/w$ et expliquer pourquoi le jeu au doigt est plus doux qu'au médiator.


> [!question]- 🔭 Aller plus loin — Master : Mouvement de Helmholtz (violon)
> Pour une corde frottée par un archet à vitesse constante, le mouvement observé est un **coude unique** qui parcourt le trajet aller-retour de la corde en $T=2L/c$, avec un profil en dents de scie à la position de l'archet. Écrire ce mouvement avec la solution de d'Alembert et montrer que le spectre décroît en $1/n$.


> [!success]- ✅ Correction
> **Résultat**
>
> $E_0=\dfrac{F h^2L}{2d(L-d)}=\dfrac{Fh^2}{2L\beta(1-\beta)}$ ; $\dfrac{E_n}{E_0}=\dfrac{2\sin^2(n\pi\beta)}{\pi^2\beta(1-\beta)\,n^2}$. AN : $c=143$ m/s, $F\approx102$ N, $T=9{,}1$ ms, $E_0\approx4{,}4$ mJ ; $b_1\dots b_5\approx2{,}23;\ 0{,}90;\ 0{,}40;\ 0{,}14;\ 0$ mm ; $\approx88\,\%$ de l'énergie dans les 4 premiers modes.


> [!example]- 📝 Solution détaillée
> **(f) Énergie initiale**
>
> $$E_0=\dfrac F2\left[\left(\dfrac hd\right)^2d+\left(\dfrac h{L-d}\right)^2(L-d)\right]=\dfrac{Fh^2}2\left(\dfrac1d+\dfrac1{L-d}\right)=\boxed{\dfrac{Fh^2L}{2\,d\,(L-d)}}.$$
> En fonction de $\beta$ : $E_0=\dfrac{Fh^2}{2L\beta(1-\beta)}$. Pour $h$ fixé, l'énergie est minimale au milieu ($\beta=\tfrac12$) et croît quand on s'approche du chevalet : il faut plus d'énergie pour déplacer de $h$ un point proche d'un point fixe.
>
> **(g) Énergie des modes et conservation**
>
> $E_n=\tfrac14\mu L\,n^2\omega_1^2b_n^2=\dfrac{\pi^2Fn^2}{4L}\,b_n^2$ car $\mu\omega_1^2=F\pi^2/L^2$. Avec $b_n$ de la question (b) :
> $$E_n=\frac{F\,h^2L^3}{\pi^2\,d^2(L-d)^2}\,\frac{\sin^2(n\pi\beta)}{n^2}\ \Longrightarrow\ \frac{E_n}{E_0}=\boxed{\frac{2\,\sin^2(n\pi\beta)}{\pi^2\beta(1-\beta)\,n^2}}.$$
> En sommant avec $\sum_n\dfrac{\sin^2(n\pi\beta)}{n^2}=\dfrac{\pi^2\beta(1-\beta)}2$ : $\sum_nE_n=E_0$ $\surd$. Chaque mode conserve son énergie au cours du temps (les modes sont indépendants), ce qui n'est pas le cas des énergies cinétique et potentielle totales, qui s'échangent à la fréquence $2f_1$.
>
> **(h) Application numérique**
>
> $c=2Lf_1=2\times0{,}65\times110=143$ m/s ; $F=\mu c^2=5{,}0\times10^{-3}\times143^2\approx102$ N ; $T=1/f_1=9{,}1$ ms ; $E_0=\dfrac{102\times(3\times10^{-3})^2\times0{,}65}{2\times0{,}13\times0{,}52}\approx4{,}4$ mJ.
> Pour $\beta=\tfrac15$, $\dfrac{2h}{\pi^2\beta(1-\beta)}=\dfrac{6{,}0\ \text{mm}}{1{,}579}\approx3{,}80$ mm, d'où
> $$b_1\approx2{,}23,\ \ b_2\approx0{,}90,\ \ b_3\approx0{,}40,\ \ b_4\approx0{,}14,\ \ b_5=0\ \ (\text{mm}).$$
> Parts d'énergie : $E_1/E_0\approx44\,\%$, $E_2/E_0\approx29\,\%$, $E_3/E_0\approx13\,\%$, $E_4/E_0\approx3\,\%$, $E_5=0$ : environ $88\,\%$ dans les quatre premiers modes. Pour $\beta=\tfrac12$ (même $h$) : $b_1=8h/\pi^2\approx2{,}43$ mm, $b_2=0$, $b_3\approx-0{,}27$ mm : le fondamental domine ($81\,\%$ de l'énergie) et le deuxième harmonique est absent. **Validation** : le fondamental est un peu plus fort au milieu (même $h$), mais le spectre est nettement plus pauvre.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex5-corde-fixee-a-ses-deux-extremites-et-ondes-stationnaires|Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex14-corde-de-piano-raide-dispersion-et-inharmonicite|Exercice 14 — Corde de piano raide : dispersion et inharmonicité]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex16-masse-en-bout-de-corde-condition-aux-limites-dynamique-et-equation-transcendante|Exercice 16 — Masse en bout de corde : condition aux limites dynamique et équation transcendante]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales-color-blue-part-a-normal-modes-of-a-helical-spring-longitudinal-waves|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde-color-blue-part-b-effect-of-tension-on-the-normal-modes-of-a-string|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde {\color{blue}(Part B — Effect of tension on the normal modes of a string)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres-color-blue-part-d-compatibility-of-wavelengths-with-the-normal-mode-model|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres {\color{blue}(Part D — Compatibility of wavelengths with the normal-mode model)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex5-synthese-scientifique-du-tp-color-blue-scientific-summary-of-the-lab|Exercice 5 — Synthèse scientifique du TP {\color{blue}(Scientific summary of the lab)}]]

