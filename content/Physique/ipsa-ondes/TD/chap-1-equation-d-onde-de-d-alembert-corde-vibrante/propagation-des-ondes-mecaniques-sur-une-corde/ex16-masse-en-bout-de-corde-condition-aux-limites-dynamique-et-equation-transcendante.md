---
title: "Exercice 16 — Masse en bout de corde : condition aux limites dynamique et équation transcendante"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · [📄 Énoncé](/pdfs/td1_PhV212_enonce.pdf)

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


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex7-ondes-stationnaires-sur-une-corde-avec-une-extremite-libre|Exercice 7 — Ondes stationnaires sur une corde avec une extrémité libre]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex5-corde-fixee-a-ses-deux-extremites-et-ondes-stationnaires|Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex13-corde-pincee-timbre-harmoniques-absents-et-energie-des-modes|Exercice 13 — Corde pincée : timbre, harmoniques absents et énergie des modes]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex14-corde-de-piano-raide-dispersion-et-inharmonicite|Exercice 14 — Corde de piano raide : dispersion et inharmonicité]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales-color-blue-part-a-normal-modes-of-a-helical-spring-longitudinal-waves|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde-color-blue-part-b-effect-of-tension-on-the-normal-modes-of-a-string|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde {\color{blue}(Part B — Effect of tension on the normal modes of a string)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres-color-blue-part-d-compatibility-of-wavelengths-with-the-normal-mode-model|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres {\color{blue}(Part D — Compatibility of wavelengths with the normal-mode model)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex5-synthese-scientifique-du-tp-color-blue-scientific-summary-of-the-lab|Exercice 5 — Synthèse scientifique du TP {\color{blue}(Scientific summary of the lab)}]] · [[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex1-ondes-sur-un-ressort-long-slinky-filmees-au-ralenti-impulsions-reflexions-et-modes-propres|Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres]]

