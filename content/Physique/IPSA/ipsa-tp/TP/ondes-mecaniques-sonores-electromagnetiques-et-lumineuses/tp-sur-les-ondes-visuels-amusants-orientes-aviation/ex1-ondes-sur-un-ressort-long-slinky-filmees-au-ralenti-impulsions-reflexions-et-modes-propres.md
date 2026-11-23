---
title: "Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres"
tags:
  - tp
  - ondes-mecaniques-sonores-electromagnetiques-et-lumineuses
---

[[physique/IPSA/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/index|⬅ Retour]]

### Exercice 1. Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres

*⭐ Indispensable · Difficulté ●●○○○ · ⏱ 2 h · Type : TP expérimental visuel (vidéo au ralenti)*

Un ressort long et mou (Slinky en métal ou en plastique) tendu sur le sol ou sur une longue table est un excellent « milieu de propagation à taille humaine » : les impulsions se déplacent à quelques mètres par seconde, on les voit avec l'œil nu et on peut les mesurer avec la vidéo au ralenti d'un smartphone (240 images par seconde).

On y retrouve, à l'échelle visible, les résultats du TD1 : célérité, réflexion sur une extrémité fixe ou libre, ondes stationnaires et fréquences propres. Le résultat le plus surprenant est que la célérité est **proportionnelle à la longueur tendue**, contrairement à une corde ordinaire.

> [!abstract]+ 📚 Prérequis
> **Notions**
>
> TD1 exercices 0 à 6 : ondes progressives, $c=\sqrt{F/\mu}$, conditions aux limites fixe et libre, modes propres.


> [!info]+ 🎯 Objectifs
> **Voir les résultats du cours**
>
> Mesurer une célérité à partir d'une vidéo, voir l'inversion de signe à une extrémité fixe, retrouver expérimentalement les fréquences propres de la corde fixée-fixée et fixée-libre.


> [!note]+ 🧰 Matériel
> Ressort long (Slinky métallique ou plastique), longueur au repos $\approx7\ \text{cm}$ pour $\approx60$ spires
>
> Sol lisse (carrelage, parquet) ou grande table, mètre ruban ($5$ m), craie ou ruban adhésif pour marquer le sol tous les $50\ \text{cm}$
>
> Smartphone en mode ralenti ($240$ images par seconde), trépied ou support
>
> Ficelle fine ($\approx20\ \text{cm}$) pour créer une extrémité libre, cordon ou aimant pour fixer l'autre bout
>
> Application de métronome ou générateur de sons (fréquences de $0{,}2$ à $2\ \text{Hz}$)
>
> Balance de cuisine ($\pm1\ \text{g}$) et poids marqués (facultatif, pour la mesure de $K$)


> [!danger] 🦺 Sécurité
> **Ressort**
>
> Ne jamais lâcher brusquement un ressort étiré (il peut se coincer et se détendre violemment). Toujours étirer et relâcher lentement, ne pas dépasser $4$ à $5$ fois la longueur au repos pour un ressort métallique.


> [!note]+ 🔬 Manipulation
> **1. Impulsion transversale**
>
> Deux opérateurs tendent le ressort à la longueur $L=4{,}0\ \text{m}$, posé sur le sol. L'un des opérateurs donne un coup de poignet transversal rapide, qui crée une bosse se propageant vers l'autre bout. Filmer au ralenti depuis le dessus, avec les repères tous les $50\ \text{cm}$. Relever, image par image, l'instant où la bosse passe devant chaque repère.
>
> **2. Célérité en fonction de la longueur**
>
> Refaire pour $L=2{,}0\ ;\ 3{,}0\ ;\ 4{,}0\ \text{m}$. Pour chaque longueur, mesurer $c$. Attention : garder la même méthode d'étirement (mesurer la longueur avec le ruban).
>
> **3. Réflexions**
>
> Filmer une impulsion réfléchie sur une extrémité tenue fixe (fixée à un pied de table), puis sur une extrémité libre (attachée à la ficelle, elle-même tenue lâchement). Comparer le signe de l'impulsion réfléchie.
>
> **4. Ondes stationnaires**
>
> Extrémités fixes, $L=4{,}0\ \text{m}$. Un opérateur excite l'extrémité de façon périodique avec le métronome (période de $2{,}1$ s environ, puis $1{,}05$ s, puis $0{,}70$ s). Chercher les fréquences pour lesquelles l'amplitude est maximale et compter les nœuds. Refaire avec une extrémité libre.


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


> [!note]- ✈️ Lien avec l'aviation
> **Essais de vibration au sol et flottement**
>
> Avant le premier vol d'un avion, on réalise un essai de vibration au sol (GVT) : des excitateurs font vibrer la structure et on cherche les fréquences propres. Ce sont exactement les fréquences de la question 4 pour l'aile. Le flottement (flutter) survient lorsque l'excitation aérodynamique se couple à un de ces modes propres.


> [!question]- 🔭 Aller plus loin — Licence : Dispersion d'un ressort
> Le ressort est un milieu discret : pour de courtes longueurs d'onde (de l'ordre de quelques spires), la vitesse de phase diminue (voir TD1 exercice 9, chaîne de masses). Les impulsions très brèves s'étalent en se propageant.


> [!question]- 🔭 Aller plus loin — Master : Onde non linéaire
> Pour de grandes amplitudes, la tension varie pendant la propagation et la vitesse dépend de l'amplitude : l'impulsion se déforme (raidissement).


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex2-corde-de-nylon|Exercice 2 — Corde de nylon]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex3-celerite-d-une-onde-sur-une-corde-homogene|Exercice 3 — Célérité d’une onde sur une corde homogène]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex3-partie-c-masse-lineique-de-la-corde-par-deux-methodes|Exercice 3 — Partie C — Masse linéique de la corde par deux méthodes]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex5-synthese-scientifique-du-tp|Exercice 5 — Synthèse scientifique du TP]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex11-une-perle-sur-la-corde-reflexion-transmission-et-filtre-passe-bas-mecanique|Exercice 11 — Une perle sur la corde : réflexion, transmission et filtre passe-bas mécanique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex12-adaptation-d-impedance-lame-quart-d-onde-entre-deux-cordes|Exercice 12 — Adaptation d'impédance : lame quart d'onde entre deux cordes]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex5-corde-fixee-a-ses-deux-extremites-et-ondes-stationnaires|Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales)]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex7-ondes-stationnaires-sur-une-corde-avec-une-extremite-libre|Exercice 7 — Ondes stationnaires sur une corde avec une extrémité libre]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex16-masse-en-bout-de-corde-condition-aux-limites-dynamique-et-equation-transcendante|Exercice 16 — Masse en bout de corde : condition aux limites dynamique et équation transcendante]]

