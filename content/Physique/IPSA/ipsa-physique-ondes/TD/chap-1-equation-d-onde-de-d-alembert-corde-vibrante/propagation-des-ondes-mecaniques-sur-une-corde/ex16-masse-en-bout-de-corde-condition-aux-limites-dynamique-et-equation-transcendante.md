---
title: "Exercice 16 — Masse en bout de corde : condition aux limites dynamique et équation transcendante"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td1_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_ex1_coup_de_pouce.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_coup_de_pouce)</a> · <a href="/pdfs/td1_ex1_solution_detaillee.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_solution_detaillee)</a> · <a href="/pdfs/td1_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_PhV212_fiche)</a> · <a href="/pdfs/td1_ex1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_ex1_fiche)</a> · <a href="/pdfs/td1_exs_maison_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_exs_maison_fiche)</a>

### Exercice 16. Masse en bout de corde : condition aux limites dynamique et équation transcendante *(facultatif)*

Une corde homogène de longueur $L$, de masse linéique $\mu$ (masse totale $m=\mu L$), tendue avec la force $F$
($c=\sqrt{F/\mu}$), est fixée en $x=0$. Son autre extrémité $x=L$ est attachée à une **masse ponctuelle** $M$ qui
peut se déplacer transversalement sans frottement (par exemple le long d'une tige verticale lisse) ; on néglige la pesanteur.
Pour de petits mouvements, la tension reste égale à $F$ et la composante transversale de la force exercée par la corde
sur la masse est $-F\,\partial_xy(L,t)$.

**q1.** (a) Écrire la condition aux limites en $x=0$ et la condition dynamique en $x=L$.

(b) Pour un mode $y=A\sin(kx)\cos(\omega t)$ avec $\omega=ck$, établir $kL\tan(kL)=m/M$.

(c) Vérifier les cas limites $M\to\infty$ et $M\to0$ en les comparant aux exercices sur la corde fixée aux deux bouts et à extrémité libre.

> [!tip]- 💡 Coup de pouce
> **Newton**
>
> $M\,\partial_t^2y(L,t)=-F\,\partial_xy(L,t)$ ; reportez $y=A\sin(kx)\cos\omega t$ et utilisez $c^2=F/\mu$.


> [!success]- ✅ Correction
> **Résultat**
>
> $y(0,t)=0$ ; $-M\omega^2\sin kL=-Fk\cos kL$ soit $kL\tan kL=\dfrac{\mu L}M=\dfrac mM$. $M\to\infty$ : $kL=n\pi$ (fixe-fixe) ; $M\to0$ : $kL=(2n-1)\dfrac\pi2$ (fixe-libre).


> [!example]- 📝 Solution détaillée
> **(a)-(b) Équation transcendante**
>
> En $x=0$ : $y=0$, d'où $y=A\sin(kx)\cos\omega t$. En $x=L$ : $M\,\partial_t^2y=-F\,\partial_xy$ donne $-M\omega^2A\sin kL=-FkA\cos kL$, soit $M\omega^2\sin kL=Fk\cos kL$. Avec $\omega=ck$ et $c^2=F/\mu$ : $M\dfrac F\mu k^2\sin kL=Fk\cos kL$, soit $\dfrac M\mu\,k\tan kL=1$ et finalement
> $$\boxed{kL\tan(kL)=\frac{\mu L}M=\frac mM}.$$
>
> **(c) Cas limites**
>
> $M\to\infty$ : second membre nul, $\tan kL=0$, $kL=n\pi$ : corde fixée aux deux bouts, $f_n=nc/(2L)$ $\surd$. $M\to0$ : second membre infini, $\tan kL\to\infty$, $kL=(2n-1)\pi/2$ : corde fixe-libre, $f_n=(2n-1)c/(4L)$ (exercice 6) $\surd$. Le comportement est donc continu entre les deux cas : la masse $M$ interpole entre « fixe » et « libre ».


**q2.** (a) Résoudre graphiquement l'équation pour $m/M=1$ en traçant $\tan u$ et $1/u$ ($u=kL$). Combien de solutions par intervalle ? Où se situent-elles ?

(b) Pour $M\gg m$ (masse lourde), établir $\omega_1\simeq\sqrt{\dfrac F{ML}}$. Interpréter (pendule : tension $F$, longueur $L$). Montrer que la correction d'ordre suivant est $M\to M+m/3$.

(c) Pour $M\gg m$, montrer que les modes supérieurs vérifient $kL\simeq n\pi+\dfrac m{n\pi M}$ ($n\ge1$). En déduire que ces fréquences sont proches de celles de la corde fixe-fixe, légèrement plus élevées.

> [!tip]- 💡 Coup de pouce
> **Petits $u$**
>
> Pour $u\ll1$ : $u\tan u\simeq u^2+\tfrac{u^4}3$ ; posez $\varepsilon=m/M$ et résolvez à l'ordre un en $\varepsilon$.
>
> **Autour de $n\pi$**
>
> Posez $u=n\pi+\delta$ avec $\delta\ll1$ : $u\tan u\simeq n\pi\delta$.


> [!success]- ✅ Correction
> **Résultats**
>
> Une solution par intervalle $](n-1)\pi,(n-1)\pi+\tfrac\pi2[$ ; $u_1^2\simeq\dfrac m{M+m/3}$, $\omega_1^2=\dfrac F{L\,(M+m/3)}$ ; $u_n\simeq n\pi+\dfrac m{n\pi M}$.


> [!example]- 📝 Solution détaillée
> **(d) Résolution graphique**
>
> Les courbes $\tan u$ (croissante sur chaque branche) et $\dfrac1u$ (décroissante) se coupent en un point unique sur chaque intervalle $](n-1)\pi,(n-1)\pi+\tfrac\pi2[$ : on trouve $u_1\approx0{,}86$, $u_2\approx3{,}43$, $u_3\approx6{,}44$, \dots{} (pour $m/M=1$). Il y a une infinité de modes, mais le $n$-ième est dans la **première moitié** de l'intervalle $](n-1)\pi,n\pi[$.
>
> **(e) Masse lourde : mode fondamental**
>
> Pour $u\ll1$ : $u^2+\dfrac{u^4}3=\varepsilon$. À l'ordre un : $u^2=\varepsilon$, donc $\omega_1^2=\dfrac{c^2u^2}{L^2}=\dfrac{F}{\mu L^2}\cdot\dfrac{\mu L}M=\boxed{\dfrac F{ML}}$ : c'est la pulsation d'un pendule de longueur $L$ sous la tension $F$, la corde se comportant comme un ressort de raideur $F/L$. À l'ordre suivant, $u^2\simeq\varepsilon\left(1-\dfrac\varepsilon3\right)\simeq\dfrac\varepsilon{1+\varepsilon/3}$, soit
> $$\omega_1^2=\frac F{L\,(M+m/3)}.$$
> On retrouve la **masse effective de Rayleigh** : la corde contribue pour un tiers de sa masse à l'inertie.
>
> **(f) Modes supérieurs**
>
> $u=n\pi+\delta$ : $\tan u=\tan\delta\simeq\delta$ et $u\tan u\simeq n\pi\delta=\varepsilon$, soit $\delta=\dfrac\varepsilon{n\pi}=\dfrac m{n\pi M}$. Les fréquences $f_n\simeq\dfrac c{2L}\left(n+\dfrac m{n\pi^2M}\right)$ sont légèrement **supérieures** à celles de la corde fixe-fixe (la masse n'est pas infinie : l'extrémité est un peu mobile, ce qui allonge la corde effective) ; le décalage décroît en $1/n$.


**q3.** (a) Application : $L=1{,}00$ m, $\mu=10$ g/m, $F=100$ N, $M=100$ g. Calculer $c$, $m/M$, la valeur exacte de $u_1=kL$ (équation transcendante), $f_1$ et la comparer aux approximations de la question (e). Calculer $u_2$ et $f_2$ ; $f_2/f_1$ est-il entier ?

(b) Exprimer l'amplitude de la masse en fonction de l'amplitude $A$ du mode et de $u_n$. La calculer pour les modes 1 et 2 de la question (g).

(c) Dans la limite $M\to0$, montrer que l'extrémité est un ventre ; dans la limite $M\to\infty$, un nœud. Quelle est l'amplitude de la masse pour $m/M=1$ au premier mode ?

> [!tip]- 💡 Coup de pouce
> **Résolution numérique**
>
> Pour $\varepsilon=0{,}1$, partez de $u\simeq\sqrt\varepsilon\approx0{,}316$ et corrigez par $u\tan u=\varepsilon$ (itération simple ou dichotomie).
>
> **Amplitude de la masse**
>
> $y_M(t)=A\sin(kL)\cos\omega t$ : comparez $\sin u_1$ à la valeur maximale $1$.


> [!question]- 🔭 Aller plus loin — Licence : Orthogonalité modifiée des modes
> Les modes $\sin(u_nx/L)$ ne sont plus orthogonaux au sens usuel $\int_0^Ly_ny_p\,\mathrm dx=0$ : montrer que la condition correcte est $\int_0^L\mu\,y_ny_p\,\mathrm dx+M\,y_n(L)y_p(L)=0$ (la masse contribue à l'inertie du système). Calculer la norme d'un mode et en déduire l'énergie de chaque mode.


> [!question]- 🔭 Aller plus loin — Master : Impédance de charge et coefficient de réflexion
> Une onde progressive $y_i=a\,\mathrm e^{j(\omega t-kx)}$ arrive sur la masse $M$ à l'extrémité. Montrer que le coefficient de réflexion en amplitude, défini en $x=L$, vaut $r=\dfrac{Z_c-j\omega M}{Z_c+j\omega M}$ avec $Z_c=\sqrt{\mu F}$ l'impédance caractéristique de la corde, et que $|r|=1$ (réflexion totale, avec un déphasage qui dépend de la fréquence). Retrouver les cas fixe et libre.


> [!success]- ✅ Correction
> **Résultats**
>
> $c=100$ m/s ; $m/M=0{,}1$ ; $u_1\approx0{,}311$ ; $f_1=\dfrac{cu_1}{2\pi L}\approx4{,}95$ Hz (approx. d'ordre un : $5{,}03$ Hz ; avec $m/3$ : $4{,}95$ Hz). $u_2\approx3{,}173$ ; $f_2\approx50{,}5$ Hz ; $f_2/f_1\approx10{,}2$, non entier.


> [!example]- 📝 Solution détaillée
> **(g) Application numérique**
>
> $c=\sqrt{100/0{,}010}=100$ m/s, $m=\mu L=10$ g, donc $\varepsilon=m/M=0{,}1$. L'équation $u\tan u=0{,}1$ a pour solution $u_1\approx0{,}311$ ($0{,}311\times\tan0{,}311=0{,}311\times0{,}3216=0{,}1000$ $\surd$). Alors $f_1=\dfrac{c\,u_1}{2\pi L}=\dfrac{100\times0{,}311}{6{,}283}=4{,}95$ Hz. Approximations : ordre un $\omega_1=\sqrt{F/(ML)}=31{,}6$ rad/s, soit $5{,}03$ Hz (écart $1{,}6\,\%$) ; avec masse effective $M+m/3=0{,}1033$ kg : $\omega_1=31{,}1$ rad/s, soit $4{,}95$ Hz (écart $<0{,}1\,\%$ : excellent).
> Mode 2 : $u=\pi+\delta$ avec $(\pi+\delta)\delta=0{,}1$, soit $\delta\approx0{,}0315$, $u_2\approx3{,}173$ ; $f_2=\dfrac{100\times3{,}173}{2\pi}\approx50{,}5$ Hz, très proche de $c/(2L)=50$ Hz (corde fixe-fixe). $f_2/f_1\approx10{,}2$ n'est pas entier : le spectre n'est pas harmonique.
>
> **(h)-(i) Amplitudes et limites**
>
> Le mode $n$ a pour profil $\sin(u_nx/L)$ : en $x=L$, l'amplitude vaut $A\sin u_n$. Pour $m/M=0{,}1$ et $n=1$ : $\sin0{,}311\approx0{,}306$, la masse oscille avec une amplitude trois fois plus petite que celle d'un ventre ($=A$). Pour le mode 2, $\sin(3{,}173)\approx-0{,}031$ : la masse est presque à un **nœud** (corde quasi fixe-fixe). Limites : $M\to0$, $u_n\to(2n-1)\pi/2$ et $|\sin u_n|\to1$ : ventre (extrémité libre) ; $M\to\infty$, $u_n\to n\pi$ et $\sin u_n\to0$ : nœud (extrémité fixe). Le coefficient $|\sin u_n|$ mesure donc à quel point la masse est « libre ». Pour $m/M=1$ et $n=1$ ($u_1\approx0{,}860$) : $\sin u_1\approx0{,}76$, la masse oscille avec $76\,\%$ de l'amplitude maximale $A$ du mode.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex7-ondes-stationnaires-sur-une-corde-avec-une-extremite-libre|Exercice 7 — Ondes stationnaires sur une corde avec une extrémité libre]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex5-corde-fixee-a-ses-deux-extremites-et-ondes-stationnaires|Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex13-corde-pincee-timbre-harmoniques-absents-et-energie-des-modes|Exercice 13 — Corde pincée : timbre, harmoniques absents et énergie des modes]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex14-corde-de-piano-raide-dispersion-et-inharmonicite|Exercice 14 — Corde de piano raide : dispersion et inharmonicité]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales)]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex5-synthese-scientifique-du-tp|Exercice 5 — Synthèse scientifique du TP]] · [[physique/IPSA/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex1-ondes-sur-un-ressort-long-slinky-filmees-au-ralenti-impulsions-reflexions-et-modes-propres|Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres]]

