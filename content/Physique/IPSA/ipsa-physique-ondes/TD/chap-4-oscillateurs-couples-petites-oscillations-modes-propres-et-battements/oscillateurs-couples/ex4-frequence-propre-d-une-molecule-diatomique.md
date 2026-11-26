---
title: "Exercice 4 — Fréquence propre d'une molécule diatomique"
tags:
  - td
  - chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/index|⬅ Retour]] · <a href="/pdfs/td4_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 4. Fréquence propre d'une molécule diatomique

*⭐ Indispensable · Difficulté ●●○○○ · ⏱ 40 min · Type : Application directe, à faire à la maison*

Deux particules $M_1$ et $M_2$ ponctuelles, de masses respectives $m_1$ et $m_2$, sont reliées par un ressort de raideur $k$ et de longueur au repos $\ell_0$. Les deux masses, mobiles sans frottement sur une tige fixe horizontale, sont écartées de leur position d'équilibre puis relâchées sans vitesse. Elles sont repérées à chaque instant par les abscisses $x_1(t)=\overline{GM_1}$ et $x_2(t)=\overline{GM_2}$, avec $G$ le centre de masse des deux particules.


> [!question]- 🪝 Accroche
> **Deux masses, un ressort : combien de fréquences ?**
>
> *Durée de l'introduction : 3 min, avant de lire l'énoncé*
>
> *Deux masses reliées par un ressort glissent sur une tige. Elles ont deux degrés de liberté. Combien de pulsations propres le système possède-t-il, et que vaut le mouvement du centre de masse ?*
>
> **Idée clé : seule la distance entre les deux masses vibre.** Le centre de masse n'est soumis à aucune force extérieure : il ne vibre pas, il avance à vitesse constante (mode de pulsation nulle). Il reste une seule vibration, celle de $X=x_2-x_1$, comme si une masse unique $\mu$ était accrochée à un ressort fixe.




> [!abstract]- 🧠 À savoir avant
> **Principe des actions réciproques**
>
> Les forces intérieures au système $\{M_1,M_2\}$ sont opposées : $\vec F_{1\to2}=-\vec F_{2\to1}$. Leur somme est nulle, donc la quantité de mouvement totale ne change pas.
>
> **Centre de masse**
>
> $m_1\overrightarrow{GM_1}+m_2\overrightarrow{GM_2}=\vec0$ par définition de $G$ ; $\vec p_{\rm tot}=(m_1+m_2)\vec v_G$.
>
> **Oscillateur harmonique**
>
> $\ddot X+\omega^2X=0$ a pour solution $X=X_0\cos(\omega t+\varphi)$ et pour période $T=2\pi/\omega$.




> [!info]- 🎯 Ce que tu sauras faire
> **Ramener un problème à deux corps à un problème à un corps**
>
> Savoir que la grandeur *relative* $X=x_2-x_1$ obéit à l'équation d'un oscillateur unique de masse $\mu=\dfrac{m_1m_2}{m_1+m_2}$ (masse réduite).
>
> **Comprendre pourquoi le centre de masse ne vibre pas**
>
> Savoir qu'un système de deux masses reliées par un ressort possède un mode de vibration ($\omega=\sqrt{k/\mu}$) et un mode de translation d'ensemble ($\omega=0$) : le système a deux degrés de liberté mais une seule fréquence non nulle.
>
> **Relier une fréquence spectroscopique à une raideur de liaison**
>
> Passer d'une longueur d'onde infrarouge $\lambda_0$ à la fréquence $f_0=c/\lambda_0$, puis à $k=4\pi^2f_0^2\mu$, avec les masses atomiques en kilogrammes.




> [!note]- 🧮 Outils mathématiques
> **Masse réduite**
>
> $\dfrac1\mu=\dfrac1{m_1}+\dfrac1{m_2}$ ; $\mu=\dfrac{m_1m_2}{m_1+m_2}$ (c'est « la moitié de la moyenne harmonique »).
>
> **Équation avec second membre constant**
>
> $\ddot X+\omega^2X=\omega^2\ell_0$ : solution particulière constante $X=\ell_0$, solution générale $X=\ell_0+X_0\cos(\omega t+\varphi)$ ; on change de variable $\xi=X-\ell_0$ (écart à l'équilibre).
>
> **Valeurs numériques**
>
> $m_C=12\times10^{-3}/(6\times10^{23})=2{,}0\times10^{-26}$ kg ; $m_O=16\times10^{-3}/(6\times10^{23})=2{,}67\times10^{-26}$ kg ; $\mu=1{,}14\times10^{-26}$ kg.



**q1.** **Question 1.** On pose $X(t)=x_2(t)-x_1(t)$. Établir l'équation différentielle du second ordre dont $X(t)$ est solution.


> [!tip]- 💡 Coup de pouce
> **Repère et forces**
>
> Dessinez le ressort allongé ($X>\ell_0$). Dans quel sens agit-il sur $M_1$ ? sur $M_2$ ? Écrivez le principe fondamental pour chaque masse, projeté sur $Ox$.
>
> **Soustraire**
>
> La grandeur $X$ est une *différence* : soustrayez les deux équations après avoir divisé chacune par sa masse.




> [!success]- ✅ Correction
> **Équation différentielle**
>
> $m_1\ddot x_1=+k(X-\ell_0)$ et $m_2\ddot x_2=-k(X-\ell_0)$, d'où
> $$\ddot X+k\Big(\frac1{m_1}+\frac1{m_2}\Big)X=k\Big(\frac1{m_1}+\frac1{m_2}\Big)\ell_0,\qquad\text{soit}\qquad\ddot X+\frac k\mu X=\frac k\mu\ell_0.$$




> [!example]- 📝 Solution détaillée
> **Système, référentiel, hypothèses**
>
> On étudie séparément $M_1$ puis $M_2$. Les seules forces horizontales sont celles du ressort (poids et réaction de la tige s'annulent en projection verticale, pas de frottement). Le système $\{M_1,M_2\}$ est isolé selon $x$ : ses forces extérieures horizontales sont nulles, donc d'après le principe des actions réciproques $m_1\ddot x_1+m_2\ddot x_2=0$ (somme des deux équations ci-dessous) et le centre de masse $G$ a un mouvement rectiligne uniforme. Le référentiel d'origine $G$ (barycentrique) est donc galiléen, et les lois de Newton s'y appliquent sans force d'inertie.
>
> **Allongement du ressort et sens des forces**
>
> Avec $x_1<0<x_2$ (pour $G$ entre les deux), la longueur du ressort est $\overline{M_1M_2}=x_2-x_1=X$ et son allongement algébrique $X-\ell_0$. Si $X>\ell_0$, le ressort est tendu : il tire $M_1$ vers $+x$ et $M_2$ vers $-x$. Forces : $\vec F_1=+k(X-\ell_0)\vec e_x$, $\vec F_2=-k(X-\ell_0)\vec e_x$ (forces opposées : action--réaction). Le signe se vérifie sur un cas : $X>\ell_0$ donne $\ddot x_1>0$, $M_1$ est attirée vers $M_2$ ; $X<\ell_0$ donne l'inverse.
>
> **Équations de Newton**
>
> $$m_1\ddot x_1=k(X-\ell_0),\qquad m_2\ddot x_2=-k(X-\ell_0).$$
> On divise par la masse correspondante : $\ddot x_1=\dfrac k{m_1}(X-\ell_0)$ et $\ddot x_2=-\dfrac k{m_2}(X-\ell_0)$.
>
> **Combinaison « physicienne » : soustraction**
>
> $$\ddot X=\ddot x_2-\ddot x_1=-k\Big(\frac1{m_2}+\frac1{m_1}\Big)(X-\ell_0).$$
> On pose $\dfrac1\mu=\dfrac1{m_1}+\dfrac1{m_2}$ (définition de la masse réduite, $\mu=\dfrac{m_1m_2}{m_1+m_2}$) :
> $$\boxed{\ddot X+\frac k\mu\,X=\frac k\mu\,\ell_0}\qquad\text{ou}\qquad\ddot\xi+\frac k\mu\xi=0\quad(\xi=X-\ell_0).$$
> *Contrôle* : $X=\ell_0$ est la position d'équilibre (second membre) ; la masse réduite est homogène à une masse ; si $m_2\to\infty$, $\mu\to m_1$ : $M_2$ est un mur fixe et on retrouve une masse $m_1$ au bout d'un ressort.
>
> **Lecture « mathématicienne » : valeurs propres $0$ et $k/\mu$**
>
> En abscisses absolues $(y_1,y_2)$ depuis un point fixe, $M\ddot{\vec y}+K\vec y=\vec F_0$ avec $M=\mathrm{diag}(m_1,m_2)$ et $K=k\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$ (le second membre $\vec F_0$ vient de $\ell_0$). $\det K=0$ : $\vec u_0=(1,1)^{\mathsf T}$ est de valeur propre $0$ (translation d'ensemble, aucune force de rappel). L'autre mode : $\det(K-\omega^2M)=0$ donne $\omega^2\big(\omega^2m_1m_2-k(m_1+m_2)\big)=0$, soit $\omega=0$ ou $\omega^2=k/\mu$. La variable $X=y_2-y_1$ est précisément celle du mode non nul ; la variable $m_1y_1+m_2y_2$ (centre de masse) est celle du mode nul. Cette décomposition est celle de la *somme et différence pondérées*.



**q2.** **Question 2.** Exprimer, en fonction de $m_1$, $m_2$ et $k$, la période $T$ avec laquelle les masses oscillent l'une par rapport à l'autre.


> [!tip]- 💡 Coup de pouce
> **Identifier la pulsation**
>
> Comparez $\ddot\xi+\dfrac k\mu\xi=0$ à $\ddot\xi+\omega^2\xi=0$ : que vaut $\omega^2$ ? Puis $T=2\pi/\omega$.




> [!success]- ✅ Correction
> **Période**
>
> $\omega=\sqrt{\dfrac k\mu}=\sqrt{k\dfrac{m_1+m_2}{m_1m_2}}$ et $T=\dfrac{2\pi}\omega=2\pi\sqrt{\dfrac{m_1m_2}{k(m_1+m_2)}}$.




> [!example]- 📝 Solution détaillée
> **Solution générale**
>
> $\xi=X-\ell_0$ vérifie l'équation de l'oscillateur harmonique : $X(t)=\ell_0+X_0\cos(\omega t+\varphi)$ avec $\omega=\sqrt{k/\mu}$. Les conditions initiales (écartées, relâchées sans vitesse) donnent $\varphi=0$ et $X_0=X(0)-\ell_0$.
>
> **Période et mouvement individuel**
>
> $$T=\frac{2\pi}{\omega}=2\pi\sqrt{\frac{m_1m_2}{k(m_1+m_2)}}=2\pi\sqrt{\frac\mu k}.$$
> Chaque masse oscille à la même période, car $x_1=-\dfrac{m_2}{m_1+m_2}X$ et $x_2=\dfrac{m_1}{m_1+m_2}X$ (conséquence de $m_1x_1+m_2x_2=0$ et $x_2-x_1=X$) : les deux masses vibrent en opposition de phase avec des amplitudes inversement proportionnelles à leurs masses, *le centre de masse restant immobile en $x=0$*.
>
> **Cas limites**
>
> - $m_1=m_2=m$ : $\mu=m/2$ et $T=2\pi\sqrt{m/(2k)}$.
> - $m_2\gg m_1$ : $\mu\to m_1$ et $T\to2\pi\sqrt{m_1/k}$ : on retrouve la masse $m_1$ accrochée à un mur.



**q3.** **Question 3.** Deux masses égales $m_1=m_2=0{,}10$ kg couplées oscillent avec une période de $1$ s. Calculer la raideur $k$ du ressort de couplage.


> [!tip]- 💡 Coup de pouce
> **Masse réduite**
>
> Pour $m_1=m_2=m$, que vaut $\mu$ ? Inversez la formule de la période pour isoler $k$.




> [!success]- ✅ Correction
> **Résultat**
>
> $k=\dfrac{4\pi^2\mu}{T^2}=\dfrac{2\pi^2m}{T^2}=\dfrac{2\pi^2\times0{,}10}{1^2}\simeq2{,}0\ \mathrm{N\cdot m^{-1}}$.




> [!example]- 📝 Solution détaillée
> **Application numérique**
>
> $\mu=m/2=0{,}05$ kg ; de $T=2\pi\sqrt{\mu/k}$ on tire $k=\dfrac{4\pi^2\mu}{T^2}=\dfrac{39{,}48\times0{,}05}{1}=1{,}97\ \mathrm{N\cdot m^{-1}}\simeq2\ \mathrm{N\cdot m^{-1}}$.
>
> **Contrôle**
>
> Dimension : $\mathrm{kg\cdot s^{-2}}=\mathrm{N\cdot m^{-1}}$. Ordre de grandeur : un ressort de laboratoire a une raideur de quelques N/m. Avec une seule masse $m=0{,}10$ kg au bout du même ressort accroché à un mur, la période serait $2\pi\sqrt{0{,}1/1{,}97}=1{,}42$ s $=\sqrt2\,T$ : le deuxième corps *raccourcit* la période (le ressort est sollicité aux deux bouts).



**q4.** **Question 4.** Le système étudié modélise les vibrations longitudinales d'une molécule diatomique d'oxyde de carbone CO, dont la longueur d'onde associée à la fréquence propre est $\lambda_0=4{,}6\ \mu\mathrm m$. Calculer la fréquence propre $f_0$ et la constante de rappel élastique $k$ de la liaison carbone--oxygène. A.N. : $C=12$ ; $O=16$ ; nombre d'Avogadro $N_A=6\times10^{23}\ \mathrm{mol^{-1}}$ et $c=3\times10^8\ \mathrm{m\cdot s^{-1}}$ dans le vide.


> [!tip]- 💡 Coup de pouce
> **Fréquence**
>
> Une onde électromagnétique vérifie $\lambda_0=c/f_0$. Attention aux puissances de dix : $1\ \mu\mathrm m=10^{-6}$ m.
>
> **Masses**
>
> La masse atomique « 12 » signifie $12\ \mathrm{g\cdot mol^{-1}}$ ; la masse d'un atome est $M_{\rm molaire}/N_A$ en kg (pensez à $10^{-3}$).
>
> **Raideur**
>
> De $f_0=\dfrac1{2\pi}\sqrt{k/\mu}$, isolez $k=4\pi^2f_0^2\mu$ avec $\mu$ la masse réduite de CO.




> [!success]- ✅ Correction
> **Résultats**
>
> $f_0=\dfrac c{\lambda_0}=6{,}5\times10^{13}$ Hz ; $m_C=2{,}0\times10^{-26}$ kg, $m_O=2{,}67\times10^{-26}$ kg, $\mu=1{,}14\times10^{-26}$ kg ; $k=4\pi^2f_0^2\mu\simeq1{,}9\times10^3\ \mathrm{N\cdot m^{-1}}$.




> [!example]- 📝 Solution détaillée
> **Fréquence propre**
>
> $$f_0=\frac{c}{\lambda_0}=\frac{3\times10^8}{4{,}6\times10^{-6}}=6{,}5\times10^{13}\ \mathrm{Hz}\quad(\omega_0=2\pi f_0=4{,}1\times10^{14}\ \mathrm{rad\cdot s^{-1}}).$$
> C'est un rayonnement infrarouge. *Attention* : le corrigé de l'établissement donne $6{,}5\times10^{23}$ Hz, mais $3\times10^8/10^{-6}=3\times10^{14}$, et $3\times10^{14}/4{,}6=6{,}5\times10^{13}$ ; $10^{23}$ Hz serait un rayonnement gamma bien au-delà de l'énergie d'une liaison.
>
> **Masses atomiques et masse réduite**
>
> $$m_C=\frac{12\times10^{-3}}{6\times10^{23}}=2{,}0\times10^{-26}\ \mathrm{kg},\qquad m_O=\frac{16\times10^{-3}}{6\times10^{23}}=2{,}67\times10^{-26}\ \mathrm{kg},$$
> $$\mu=\frac{m_Cm_O}{m_C+m_O}=\frac{2{,}0\times2{,}67}{4{,}67}\times10^{-26}=1{,}14\times10^{-26}\ \mathrm{kg}.$$
> Raccourci : $\mu=\dfrac{12\times16}{12+16}\ \mathrm{u}=6{,}86\ \mathrm{u}$, soit $6{,}86\times10^{-3}/6\times10^{23}=1{,}14\times10^{-26}$ kg.
>
> **Raideur de la liaison**
>
> D'après la question 2, $T_0=1/f_0=2\pi\sqrt{\mu/k}$ donc
> $$k=4\pi^2f_0^2\mu=39{,}48\times(6{,}5\times10^{13})^2\times1{,}14\times10^{-26}\simeq1{,}9\times10^3\ \mathrm{N\cdot m^{-1}}.$$
> Avec les valeurs exactes $f_0=6{,}522\times10^{13}$ Hz : $k=1{,}92\times10^3$ N/m (le corrigé de l'établissement donne $1\,918$ N/m, ce qui est cohérent).
>
> **Contrôle et interprétation**
>
> La raideur d'une liaison covalente triple (CO) est de l'ordre du millier de N/m, bien supérieure à celle d'un ressort de laboratoire (quelques N/m), et la masse réduite est minuscule : $\omega=\sqrt{k/\mu}\simeq4\times10^{14}\ \mathrm{rad\cdot s^{-1}}$ contre $\simeq6\ \mathrm{rad\cdot s^{-1}}$ pour le ressort de la question 3, soit un rapport $\sim10^{14}$ (rapport $\sqrt{10^{3}/10^{-25}}\sim10^{14}$ en ordre de grandeur). Le nombre d'onde associé est $1/\lambda_0=2\,170\ \mathrm{cm^{-1}}$, proche de la valeur mesurée pour CO ($\simeq2\,143\ \mathrm{cm^{-1}}$).




> [!note]- 🔗 Liens avec d'autres disciplines
> **Chimie physique**
>
> Spectroscopie infrarouge de vibration : la constante de force $k$ mesure la rigidité d'une liaison (simple, double, triple : $k$ croît).
>
> **Mécanique**
>
> Problème à deux corps : le mouvement relatif est celui d'une particule de masse réduite $\mu$ (cas du ressort, de la gravitation, etc.).




> [!question]- 🔭 Aller plus loin — Licence : Mode de translation et matrice des raideurs
> Écrire $M\ddot{\vec x}+K\vec x=\vec0$ en abscisses absolues $(y_1,y_2)$ depuis un point fixe. Montrer que $K=k\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$ est de déterminant nul, que $\vec u_0=(1,1)^{\mathsf T}$ est vecteur propre de valeur propre nulle (translation d'ensemble), et retrouver $\omega^2=k/\mu$ pour l'autre mode.




> [!question]- 🔭 Aller plus loin — Licence : Modes de vibration et déplacements individuels
> Montrer que dans le mode de vibration $x_1=-\dfrac{m_2}{m_1+m_2}(X-\ell_0)$ et $x_2=\dfrac{m_1}{m_1+m_2}(X-\ell_0)$ autour de l'équilibre : le plus léger se déplace le plus (« la plus petite masse a la plus grande amplitude »).




> [!question]- 🔭 Aller plus loin — Master : Isotopes
> Calculer le décalage de fréquence quand on remplace $^{12}$C par $^{13}$C dans CO ($k$ inchangé) : $f_0'/f_0=\sqrt{\mu/\mu'}$. Comparer avec les mesures de spectroscopie ($\approx-2{,}2\,\%$).




> [!question]- 🔭 Aller plus loin — Master : Anharmonicité
> Remplacer le ressort par un potentiel de Morse $V(r)=D(1-e^{-a(r-r_0)})^2$ ; montrer que la liaison est harmonique à petite amplitude avec $k=2Da^2$ et que l'écart au modèle linéaire apparaît à l'ordre cubique (la fréquence dépend de l'amplitude).




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex2-couplage-de-deux-oscillateurs-harmoniques-dissymetriques|Exercice 2 — Couplage de deux oscillateurs harmoniques dissymétriques]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex3-oscillations-libres-et-forcees-d-un-couplage-pendule-chariot|Exercice 3 — Oscillations libres et forcées d'un couplage pendule-chariot]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex5-complement-niveau-1-cpge-pendules-couples-par-un-ressort-attache-a-mi-hauteur|Exercice 5 — Complément (niveau 1, CPGE) : pendules couplés par un ressort attaché à mi-hauteur]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex6-complement-niveau-2-ambitieux-trois-masses-quatre-ressorts-diagonalisation-et-perturbation|Exercice 6 — Complément (niveau 2, ambitieux) : trois masses, quatre ressorts, diagonalisation et perturbation]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex7-complement-niveau-2-ambitieux-oscillateurs-desaccordes-anticroisement-et-transfert-d-energie|Exercice 7 — Complément (niveau 2, ambitieux) : oscillateurs désaccordés, anticroisement et transfert d'énergie]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex8-complement-niveau-3-ens-modes-non-lineaires-de-deux-pendules-couples-stabilite-et-instabilite-parametrique|Exercice 8 — Complément (niveau 3, ENS) : modes non linéaires de deux pendules couplés, stabilité et instabilité paramétrique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex9-complement-niveau-3-ens-anneau-de-n-oscillateurs-modes-de-fourier-et-propagation-du-signal|Exercice 9 — Complément (niveau 3, ENS) : anneau de N oscillateurs, modes de Fourier et propagation du signal]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex1-pendules-couples-et-battements|Exercice 1 — Pendules couplés et battements]]


