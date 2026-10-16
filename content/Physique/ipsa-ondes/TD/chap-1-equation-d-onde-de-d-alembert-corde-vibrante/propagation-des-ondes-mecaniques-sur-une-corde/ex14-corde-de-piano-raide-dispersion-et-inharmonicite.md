---
title: "Exercice 14 — Corde de piano raide : dispersion et inharmonicité"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td1_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_ex1_coup_de_pouce.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_coup_de_pouce)</a> · <a href="/pdfs/td1_ex1_solution_detaillee.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_solution_detaillee)</a> · <a href="/pdfs/td1_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_PhV212_fiche)</a> · <a href="/pdfs/td1_ex1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_ex1_fiche)</a> · <a href="/pdfs/td1_exs_maison_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_exs_maison_fiche)</a>

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


> [!success]- ✅ Correction
> **Résultat**
>
> $\omega^2=c^2k^2\left(1+\dfrac{EI}Fk^2\right)$, $v_\varphi=c\sqrt{1+\dfrac{EI}Fk^2}$. La raideur est négligeable pour $\lambda\gg\lambda_c=2\pi\sqrt{EI/F}$.


> [!example]- 📝 Solution détaillée
> **(a) Homogénéité et limite**
>
> $[F\,\partial_x^2y]=\mathrm N\,\mathrm m^{-1}$ $\surd$ ; $[EI\,\partial_x^4y]=\mathrm{N\,m^2}\cdot\mathrm m\cdot\mathrm m^{-4}=\mathrm N\,\mathrm m^{-1}$ $\surd$. Pour $EI\to0$ on retrouve $\mu\ddot y=F\,y''$, l'équation de d'Alembert. Le rapport des deux termes spatiaux est $\dfrac{EI\,k^4}{F\,k^2}=\dfrac{EI}Fk^2$ : la raideur est négligeable pour $k\ll\sqrt{F/(EI)}$, soit $\lambda\gg\lambda_c=2\pi\sqrt{EI/F}$.
>
> **(b) Relation de dispersion**
>
> $-\mu\omega^2=-Fk^2-EI\,k^4$, soit
> $$\boxed{\omega^2=\frac F\mu k^2\left(1+\frac{EI}Fk^2\right)=c^2k^2\left(1+\frac{EI}Fk^2\right)},\qquad v_\varphi=\frac\omega k=\boxed{c\sqrt{1+\frac{EI}Fk^2}}.$$
> La vitesse de phase **croît avec $k$** : les composantes de petite longueur d'onde se propagent plus vite que $c$.


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


> [!success]- ✅ Correction
> **Résultat**
>
> $k_n=\dfrac{n\pi}L$ ; $f_n=nf_0\sqrt{1+Bn^2}$ avec $B=\dfrac{\pi^2EI}{FL^2}$ ; $\Delta_n\simeq\dfrac{1200}{\ln2}\cdot\dfrac{Bn^2}2\approx866\,Bn^2$ cents.


> [!example]- 📝 Solution détaillée
> **(c) Modes propres**
>
> On cherche $y=Y(x)\cos(\omega t+\phi)$ : $Y''''$ et $Y''$ sont proportionnelles à $Y$ si $Y=\sin(kx)$. Les conditions $Y(0)=Y''(0)=0$ sont vérifiées, $Y(L)=Y''(L)=0$ imposent $\sin kL=0$, d'où $k_n=\dfrac{n\pi}L$. La relation de dispersion donne
> $$\omega_n=c\,k_n\sqrt{1+\frac{EI}Fk_n^2},\qquad f_n=\frac{\omega_n}{2\pi}=\frac{nc}{2L}\sqrt{1+\frac{EI}F\frac{n^2\pi^2}{L^2}}=\boxed{nf_0\sqrt{1+Bn^2}},\quad B=\frac{\pi^2EI}{FL^2}.$$
> Le fondamental n'est pas modifié à l'ordre $B$ ($f_1=f_0\sqrt{1+B}$), mais les harmoniques s'écartent de plus en plus des multiples de $f_0$ : le spectre n'est plus harmonique.
>
> **(d) Développement et cents**
>
> Pour $Bn^2\ll1$ : $f_n\simeq nf_0\left(1+\dfrac{Bn^2}2\right)$. En cents,
> $$\Delta_n=1200\log_2\!\left(\frac{f_n}{nf_0}\right)=\frac{1200}{\ln2}\ln\sqrt{1+Bn^2}\simeq\frac{1200}{\ln2}\cdot\frac{Bn^2}2\approx\boxed{866\,B\,n^2\ \text{cents}}.$$
> L'écart croît comme le **carré du rang** : il est négligeable pour le fondamental, mais audible pour les harmoniques élevés.


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


> [!question]- 🔭 Aller plus loin — Licence : Conditions aux limites encastrées
> Pour une corde **encastrée** ($y=0$, $y'=0$), les modes ne sont plus des sinus purs : ils présentent une couche limite de largeur $\sqrt{EI/F}$ près des extrémités. Montrer qu'à l'ordre un, $f_n\simeq nf_0\left(1+\dfrac2{\pi}\dfrac{\ell_c}{L}+\dots\right)\sqrt{1+Bn^2}$ avec $\ell_c=\sqrt{EI/F}$.


> [!question]- 🔭 Aller plus loin — Master : Propagation d'une impulsion dispersive
> Pour une impulsion de largeur spectrale $\Delta k$, la distance $z$ au bout de laquelle elle s'élargit significativement est $z\sim\dfrac{1}{\Delta k^2\,|\omega''(k)|}$ avec $\omega''=\mathrm d^2\omega/\mathrm dk^2$. Calculer $\omega''(k)$ pour la corde raide, discuter la forme du « chirp » entendu après un impact (son aigu qui précède le grave) et comparer avec les ondes de surface de l'eau ($\omega^2=gk$).


> [!success]- ✅ Correction
> **Résultats**
>
> $c\approx330$ m/s, $\mu\approx6{,}13$ g/m, $F\approx666$ N, $EI\approx9{,}8\times10^{-3}$ N·m², $B\approx3{,}7\times10^{-4}$, $\lambda_c\approx2{,}4$ cm, $n_B\approx52$. $\Delta_2\approx1{,}3$, $\Delta_5\approx8$, $\Delta_{10}\approx31$ cents. $v_g(n=10)\approx1{,}054\,c$.


> [!example]- 📝 Solution détaillée
> **(e) Données et coefficient d'inharmonicité**
>
> $c=2Lf_0=2\times0{,}63\times261{,}6\approx330$ m/s. $\mu=\rho\dfrac{\pi d_c^2}4=7800\times7{,}85\times10^{-7}\approx6{,}13\times10^{-3}$ kg/m. $F=\mu c^2\approx666$ N (valeur réaliste : une corde de piano supporte $\sim700$ N). $I=\dfrac{\pi(10^{-3})^4}{64}\approx4{,}9\times10^{-14}$ m$^4$, $EI\approx9{,}8\times10^{-3}$ N·m$^2$.
> $$B=\frac{\pi^2EI}{FL^2}=\frac{9{,}87\times9{,}8\times10^{-3}}{666\times0{,}397}\approx3{,}7\times10^{-4}.$$
> $\lambda_c=2\pi\sqrt{EI/F}=2\pi\sqrt{1{,}47\times10^{-5}}\approx2{,}4$ cm. $Bn^2\sim1$ pour $n\approx1/\sqrt B\approx52$ ; ce rang correspond à $\lambda_n=2L/n=2{,}4$ cm : cohérent avec $\lambda_c$.
>
> **(f) Fréquences et écarts**
>
> $f_n=nf_0\sqrt{1+3{,}7\times10^{-4}\,n^2}$. $n=1$ : $261{,}6\times1{,}00018=261{,}7$ Hz ($0{,}3$ cent). $n=2$ : $523{,}2\times1{,}00073=523{,}6$ Hz ($1{,}3$ cent). $n=5$ : $1308\times1{,}0046=1314$ Hz ($7{,}9$ cents). $n=10$ : $2616\times1{,}0182=2664$ Hz ($31$ cents). Les écarts valent $866Bn^2$ cents ($0{,}3$, $1{,}3$, $8$, $32$ cents) : le $10^{\text{e}}$ harmonique est environ un **tiers de demi-ton plus haut** que le multiple idéal : parfaitement audible.
>
> **(g) Vitesse de groupe**
>
> $\omega=ck\sqrt{1+\kappa k^2}$ avec $\kappa=EI/F$ :
> $$v_g=\frac{\mathrm d\omega}{\mathrm dk}=c\left[\sqrt{1+\kappa k^2}+\frac{\kappa k^2}{\sqrt{1+\kappa k^2}}\right]=\boxed{c\,\frac{1+2\kappa k^2}{\sqrt{1+\kappa k^2}}}.$$
> Pour $n=10$, $\kappa k^2=Bn^2=0{,}0367$ : $v_\varphi=c\sqrt{1,0367}\approx1{,}018\,c$ et $v_g=c\,\dfrac{1{,}0734}{1{,}0182}\approx1{,}054\,c$. Les deux dépassent $c$ ; $v_g\simeq c(1+\tfrac32\kappa k^2)>v_\varphi\simeq c(1+\tfrac12\kappa k^2)$. Une impulsion frappée par le marteau se disperse : les aigus arrivent en avance (« précurseur » aigu).
>
> **(h) Conséquence pour l'accord**
>
> Le $2^{\text{e}}$ partiel de $do_3$ est à $f_2=523{,}6$ Hz, un peu plus haut que $2f_0=523{,}2$ Hz, fréquence « idéale » de $do_4$. Si l'accordeur accorde $do_4$ sur $2f_0$, le battement entre le partiel de $do_3$ et le fondamental de $do_4$ est $\Delta f\approx0{,}4$ Hz ; pour l'annuler, il **monte** $do_4$ à $f_2$. De proche en proche, chaque octave est élargie : par rapport au milieu du clavier, les notes aiguës sont accordées de plus en plus haut et les graves de plus en plus bas. C'est l'**accord étiré** : l'accordeur préfère des octaves légèrement « fausses » mais sans battements.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex15-corde-amortie-attenuation-facteur-de-qualite-et-resonance-de-melde|Exercice 15 — Corde amortie : atténuation, facteur de qualité et résonance de Melde]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex5-corde-fixee-a-ses-deux-extremites-et-ondes-stationnaires|Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex13-corde-pincee-timbre-harmoniques-absents-et-energie-des-modes|Exercice 13 — Corde pincée : timbre, harmoniques absents et énergie des modes]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex16-masse-en-bout-de-corde-condition-aux-limites-dynamique-et-equation-transcendante|Exercice 16 — Masse en bout de corde : condition aux limites dynamique et équation transcendante]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales-color-blue-part-a-normal-modes-of-a-helical-spring-longitudinal-waves|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde-color-blue-part-b-effect-of-tension-on-the-normal-modes-of-a-string|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde {\color{blue}(Part B — Effect of tension on the normal modes of a string)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres-color-blue-part-d-compatibility-of-wavelengths-with-the-normal-mode-model|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres {\color{blue}(Part D — Compatibility of wavelengths with the normal-mode model)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex5-synthese-scientifique-du-tp-color-blue-scientific-summary-of-the-lab|Exercice 5 — Synthèse scientifique du TP {\color{blue}(Scientific summary of the lab)}]]

