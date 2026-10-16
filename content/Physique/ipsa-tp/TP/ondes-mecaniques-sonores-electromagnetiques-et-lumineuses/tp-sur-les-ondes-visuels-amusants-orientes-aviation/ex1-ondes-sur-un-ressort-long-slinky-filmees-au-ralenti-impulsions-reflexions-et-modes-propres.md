---
title: "Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres"
tags:
  - tp
  - ondes-mecaniques-sonores-electromagnetiques-et-lumineuses
---

[[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/index|⬅ Retour]] · <a href="/pdfs/TP_IPSA_Generale_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 1. Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres

Un ressort long et mou (Slinky en métal ou en plastique) tendu sur le sol ou sur une longue table est un excellent « milieu de propagation à taille humaine » : les impulsions se déplacent à quelques mètres par seconde, on les voit avec l'œil nu et on peut les mesurer avec la vidéo au ralenti d'un smartphone (240 images par seconde).

On y retrouve, à l'échelle visible, les résultats du TD1 : célérité, réflexion sur une extrémité fixe ou libre, ondes stationnaires et fréquences propres. Le résultat le plus surprenant est que la célérité est **proportionnelle à la longueur tendue**, contrairement à une corde ordinaire.

**q1.** Traiter la mesure de $c$ pour $L=4{,}0\ \text{m}$ : en supposant que la mesure de la durée est faite à $\pm3$ images près et celle de la distance à $\pm5\ \text{cm}$, calculer $c$ et son incertitude relative. Combien de temps faudrait-il pour détecter un écart de $2\ \%$ entre deux mesures ?

> [!success]- ✅ Correction
> **Résultat**
>
> $c=\dfrac{4{,}0}{1{,}05}=3{,}81\ \text{m}\cdot\text{s}^{-1}$ ; $\dfrac{\Delta t}{t}=\dfrac{3/240}{1{,}05}=1{,}2\ \%$, $\dfrac{\Delta L}{L}=1{,}25\ \%$, donc $\dfrac{\Delta c}{c}=2{,}4\ \%$ (somme absolue) ou $1{,}7\ \%$ (quadratique) : $c=(3{,}8\pm0{,}1)\ \text{m}\cdot\text{s}^{-1}$.


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> $c=\dfrac{L}{t}$ donc $\dfrac{\Delta c}{c}=\dfrac{\Delta L}{L}+\dfrac{\Delta t}{t}$ (méthode logarithmique, cf. TD2 exercice 8). $\Delta t=\dfrac{3}{240}=0{,}0125\ \text{s}$ donne $1{,}2\ \%$ et $\Delta L=5\ \text{cm}$ donne $1{,}25\ \%$. On obtient $2{,}4\ \%$ en somme absolue.
> Comme $\dfrac{\Delta t}{t}$ varie en $\dfrac{1}{t}$, un trajet plus long (aller-retour) diminue l'incertitude relative sur le temps. Pour repérer un écart de $2\ \%$, il faut $\Delta c/c<1\ \%$, donc filmer un aller-retour ($t\approx2{,}1\ \text{s}$).


**q2.** Célérité et longueur. (a) Montrer que si le ressort a une longueur au repos négligeable, sa tension vaut $F=KL$ ($K$ raideur) et sa masse linéique $\mu=M/L$ ; en déduire $c=L\sqrt{K/M}$. (b) Tracer $c$ en fonction de $L$ avec les données ; interpréter. (c) En déduire $K/M$ puis $K$ pour $M=0{,}20\ \text{kg}$. (d) Que se passe-t-il pour une corde ordinaire de masse linéique et tension fixées si on l'allonge ?

> [!success]- ✅ Correction
> **Résultat**
>
> (a) $c=\sqrt{F/\mu}=\sqrt{KL\cdot L/M}=L\sqrt{K/M}$. (b) $c/L=0{,}95\ ;\ 0{,}97\ ;\ 0{,}95\ \text{s}^{-1}$ : constant, donc $c\propto L$. (c) $K/M=0{,}90\ \text{s}^{-2}$, $K\approx0{,}18\ \text{N}\cdot\text{m}^{-1}$. (d) Pour une corde, $c$ est indépendant de la longueur.


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> (a) Un ressort de longueur au repos nulle a une tension $F=KL$ proportionnelle à son allongement ; la masse linéique est $\mu=M/L$ car la masse est répartie sur la longueur $L$. Donc $c=\sqrt{\dfrac{KL}{M/L}}=L\sqrt{\dfrac{K}{M}}$.
> (b) Les rapports $c/L$ valent $0{,}95\ ;\ 0{,}97\ ;\ 0{,}95\ \text{s}^{-1}$ : constants aux incertitudes près, donc $c\propto L$. On en déduit $\sqrt{K/M}=0{,}95\ \text{s}^{-1}$ et $K/M=0{,}90\ \text{s}^{-2}$, soit $K\approx0{,}18\ \text{N}\cdot\text{m}^{-1}$ pour $M=0{,}20\ \text{kg}$.
> (c) On vérifie $K$ en suspendant des masses et en mesurant l'allongement (méthode statique).
> (d) Pour une corde ordinaire, allonger la corde ne change pas $\mu$ ni $F$ (si elle est inextensible) : $c=\sqrt{F/\mu}$ est constante. Le ressort est un cas très particulier.
> Un ressort réel (spires jointives au repos) présente une longueur au repos $L_0$ non nulle ; la relation devient $F=K(L-L_0)$ et $c$ n'est plus proportionnelle à $L$ pour $L\approx L_0$.


**q3.** Réflexions. (a) Décrire ce que l'on observe (signe de l'impulsion réfléchie) pour l'extrémité fixe et pour l'extrémité libre. (b) Justifier avec les conditions aux limites $y(L,t)=0$ (fixe) et $\partial_xy(L,t)=0$ (libre), sachant que $y=f(x-ct)+g(x+ct)$. (c) Pourquoi l'impulsion réfléchie est-elle un peu plus petite que l'impulsion incidente ?

> [!success]- ✅ Correction
> **Résultat**
>
> Fixe : $g(L+ct)=-f(L-ct)$ : impulsion inversée. Libre : $g(L+ct)=+f(L-ct)$ : impulsion de même signe. L'amortissement (frottements et rayonnement) réduit l'amplitude à chaque aller-retour.


> [!example]- 📝 Solution détaillée
> **Démonstration**
>
> Extrémité fixe : $f(L-ct)+g(L+ct)=0$, donc $g=-f$ : l'onde réfléchie est l'opposée de l'onde incidente (inversion). Extrémité libre : $\partial_xy=f'+g'=0$ en $x=L$, donc $g'(L+ct)=-f'(L-ct)$ ; en intégrant $g(L+ct)=-\left[-f(L-ct)\right]=+f(L-ct)$ (l'onde est réfléchie sans inversion, par la variable $u=L-ct$ qui remonte à $L+ct$). Dans la pratique, une extrémité « libre » attachée par une ficelle légère n'est pas parfaitement libre : l'amplitude réfléchie est un peu plus faible.
> (c) Les frottements (air, sol, spires) amortissent l'onde, et la ficelle ajoute une petite masse et des pertes.


**q4.** Modes propres. Pour $L=4{,}0\ \text{m}$ et $c=3{,}8\ \text{m}\cdot\text{s}^{-1}$, prévoir les trois premières fréquences de résonance (a) pour deux extrémités fixes, (b) pour une extrémité fixe et une libre. Proposer un protocole pour les vérifier avec le métronome et donner le nombre de nœuds attendu pour chaque mode.

> [!success]- ✅ Correction
> **Résultat**
>
> (a) $f_N=N\dfrac{c}{2L}=0{,}475\ ;\ 0{,}95\ ;\ 1{,}43\ \text{Hz}$ (périodes $2{,}1\ ;\ 1{,}05\ ;\ 0{,}70\ \text{s}$), soit $N-1$ nœuds internes. (b) $f_N=(2N-1)\dfrac{c}{4L}=0{,}2375\ ;\ 0{,}7125\ ;\ 1{,}19\ \text{Hz}$ ; $N-1$ nœuds internes et un ventre à l'extrémité libre.


> [!example]- 📝 Solution détaillée
> **Calcul et protocole**
>
> (a) $\dfrac{c}{2L}=\dfrac{3{,}8}{8}=0{,}475\ \text{Hz}$, d'où $f_N=0{,}475\ ;\ 0{,}95\ ;\ 1{,}425\ \text{Hz}$, soit des périodes de $2{,}1\ ;\ 1{,}05\ ;\ 0{,}70\ \text{s}$. (b) $\dfrac{c}{4L}=0{,}2375\ \text{Hz}$, d'où $0{,}2375\ ;\ 0{,}7125\ ;\ 1{,}1875\ \text{Hz}$.
> Protocole : régler un métronome à la fréquence (en battements par minute : $28{,}5\ ;\ 57\ ;\ 85{,}5$ pour (a)), déplacer l'extrémité transversalement à chaque battement, ajuster jusqu'à l'amplitude maximale. Les fréquences mesurées doivent être à $\pm5\ \%$ des prévisions ; l'écart est dû à l'imprécision de $c$ et à la masse de la main.
> Rappel : les fréquences fixée-libre sont les harmoniques impairs de $f_1=\dfrac{c}{4L}$ (TD1 exercice 6).


**q5.** (*) Puissance. Pour une onde progressive d'amplitude $a=10\ \text{cm}$ à la fréquence $f=0{,}475\ \text{Hz}$ sur le ressort ($L=4{,}0\ \text{m}$, $M=0{,}20\ \text{kg}$, $c=3{,}8\ \text{m}\cdot\text{s}^{-1}$), calculer la puissance transportée $\langle\mathcal{P}\rangle=\tfrac{1}{2}Z\omega^2a^2$ (TD1 exercice 7). Comparer à la puissance musculaire d'un opérateur.

> [!success]- ✅ Correction
> **Résultat**
>
> $F=KL=0{,}72\ \text{N}$, $\mu=0{,}05\ \text{kg/m}$, $Z=\sqrt{F\mu}=0{,}19\ \text{kg/s}$, $\omega=2{,}99\ \text{rad/s}$, $\langle\mathcal{P}\rangle\approx8{,}5\ \text{mW}$ : faible devant les $\approx100\ \text{W}$ du métabolisme d'un adulte (et les dizaines de watts de puissance musculaire mobilisable).


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> $F=KL=0{,}18\times4{,}0=0{,}72\ \text{N}$ ; $\mu=\dfrac{M}{L}=0{,}05\ \text{kg/m}$ ; $Z=\sqrt{0{,}72\times0{,}05}=0{,}19\ \text{kg/s}$ (et $c=\sqrt{F/\mu}=3{,}8\ \text{m/s}$, cohérent). $\omega=2\pi\times0{,}475=2{,}99\ \text{rad/s}$.
> $\langle\mathcal{P}\rangle=\tfrac{1}{2}\times0{,}19\times2{,}99^2\times0{,}1^2=8{,}5\times10^{-3}\ \text{W}$.
> Une très petite puissance suffit à entretenir l'onde ; c'est pourquoi les pertes (frottements) sont visibles : une onde stationnaire s'atténue en quelques secondes si on arrête d'exciter.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex2-corde-de-nylon|Exercice 2 — Corde de nylon]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex3-celerite-d-une-onde-sur-une-corde-homogene|Exercice 3 — Célérité d’une onde sur une corde homogène]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde-color-blue-part-b-effect-of-tension-on-the-normal-modes-of-a-string|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde {\color{blue}(Part B — Effect of tension on the normal modes of a string)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex3-partie-c-masse-lineique-de-la-corde-par-deux-methodes-color-blue-part-c-linear-mass-density-of-the-string-by-two-methods|Exercice 3 — Partie C — Masse linéique de la corde par deux méthodes {\color{blue}(Part C — Linear mass density of the string by two methods)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex5-synthese-scientifique-du-tp-color-blue-scientific-summary-of-the-lab|Exercice 5 — Synthèse scientifique du TP {\color{blue}(Scientific summary of the lab)}]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex11-une-perle-sur-la-corde-reflexion-transmission-et-filtre-passe-bas-mecanique|Exercice 11 — Une perle sur la corde : réflexion, transmission et filtre passe-bas mécanique]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex12-adaptation-d-impedance-lame-quart-d-onde-entre-deux-cordes|Exercice 12 — Adaptation d'impédance : lame quart d'onde entre deux cordes]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex5-corde-fixee-a-ses-deux-extremites-et-ondes-stationnaires|Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales-color-blue-part-a-normal-modes-of-a-helical-spring-longitudinal-waves|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres-color-blue-part-d-compatibility-of-wavelengths-with-the-normal-mode-model|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres {\color{blue}(Part D — Compatibility of wavelengths with the normal-mode model)}]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex7-ondes-stationnaires-sur-une-corde-avec-une-extremite-libre|Exercice 7 — Ondes stationnaires sur une corde avec une extrémité libre]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex16-masse-en-bout-de-corde-condition-aux-limites-dynamique-et-equation-transcendante|Exercice 16 — Masse en bout de corde : condition aux limites dynamique et équation transcendante]]

