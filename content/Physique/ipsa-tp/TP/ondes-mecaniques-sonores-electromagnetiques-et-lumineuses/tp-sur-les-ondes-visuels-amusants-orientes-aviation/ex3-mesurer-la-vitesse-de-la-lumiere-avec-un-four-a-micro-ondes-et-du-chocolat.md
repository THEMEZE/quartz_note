---
title: "Exercice 3 — Mesurer la vitesse de la lumière avec un four à micro-ondes et du chocolat"
tags:
  - tp
  - ondes-mecaniques-sonores-electromagnetiques-et-lumineuses
---

[[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/index|⬅ Retour]] · [📄 Fiche enseignant](/pdfs/TP_IPSA_Generale_fiche.pdf)

### Exercice 3. Mesurer la vitesse de la lumière avec un four à micro-ondes et du chocolat

Un four à micro-ondes est une cavité métallique dans laquelle une onde électromagnétique de fréquence $f=2{,}45\ \text{GHz}$ forme une **onde stationnaire** : des nœuds où le champ électrique est nul et des ventres où il est maximal. Les aliments chauffent aux ventres et restent froids aux nœuds. Si l'on empêche le plateau de tourner, une tablette de chocolat (ou de guimauves) présente des taches fondues régulièrement espacées.

La distance entre deux taches consécutives est $\lambda/2$. Avec la fréquence indiquée sur l'étiquette du four, on obtient la vitesse de la lumière $c=\lambda f$ à quelques pourcents près.

**q1.** Justifier que les taches fondues sont espacées de $\lambda/2$ et non de $\lambda$. On rappelle que la puissance absorbée est proportionnelle à $E^2$ et que $E(x,t)=E_0\sin(kx)\cos(\omega t)$.

> [!success]- ✅ Correction
> **Résultat**
>
> La puissance moyenne absorbée est proportionnelle à $E_0^2\sin^2(kx)$, maximale en chaque ventre, c'est-à-dire tous les $\dfrac{\lambda}{2}$ ($kx=\dfrac{\pi}{2}+p\pi$).


> [!example]- 📝 Solution détaillée
> **Justification**
>
> $\langle E^2\rangle\propto\sin^2(kx)$ est maximale pour $kx=\dfrac{\pi}{2}+p\pi$, soit $x=\dfrac{\lambda}{4}+p\dfrac{\lambda}{2}$. Deux ventres consécutifs sont séparés par $\dfrac{\lambda}{2}$ (idem pour les nœuds, TD1 exercice 4). Comme $\sin^2$ a une période spatiale $\lambda/2$, les taches de chauffage ont une période $\lambda/2$ même si le champ a une période $\lambda$.


**q2.** Calculer $\lambda$ puis $c$ pour les données de l'énoncé, et l'incertitude (on supposera $\Delta f=\pm25\ \text{MHz}$). Comparer avec $c=2{,}998\times10^{8}\ \text{m/s}$.

> [!tip]- 💡 Coup de pouce
> **Moyenne sur $N$ intervalles**
>
> $d=\dfrac{D_{\text{tot}}}{N}$ et l'incertitude sur $D_{\text{tot}}$ (deux pointés de $\pm3\ \text{mm}$) est divisée par $N$.


> [!success]- ✅ Correction
> **Résultat**
>
> $d=\dfrac{24{,}4}{4}=6{,}10\ \text{cm}$, $\lambda=12{,}2\ \text{cm}$, $c=\lambda f=0{,}122\times2{,}45\times10^{9}=2{,}99\times10^{8}\ \text{m/s}$. Incertitude : $\dfrac{\Delta D}{D}=\dfrac{6}{244}=2{,}5\ \%$ (somme absolue) et $\dfrac{\Delta f}{f}=1{,}0\ \%$, donc $\dfrac{\Delta c}{c}=3{,}5\ \%$ soit $\pm1{,}0\times10^{7}$ : $c=(2{,}99\pm0{,}10)\times10^{8}\ \text{m/s}$.


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> $\lambda=2d=\dfrac{2D_{\text{tot}}}{N}=\dfrac{2\times0{,}244}{4}=0{,}122\ \text{m}$. $c=\lambda f=0{,}122\times2{,}45\times10^{9}=2{,}989\times10^{8}\ \text{m/s}$.
> $\dfrac{\Delta c}{c}=\dfrac{\Delta D}{D}+\dfrac{\Delta f}{f}=\dfrac{6}{244}+\dfrac{25}{2450}=2{,}5\ \%+1{,}0\ \%=3{,}5\ \%$ ; en quadratique $2{,}7\ \%$. La valeur de référence est dans l'intervalle. Le résultat $2{,}99\times10^{8}$ est en accord à $0{,}3\ \%$ ; ce très bon accord est en partie fortuit.
> Utiliser un plus grand nombre $N$ d'intervalles diminue l'incertitude sur $d$ ; l'incertitude sur $f$ devient alors dominante.


**q3.** Critique. (a) Pourquoi retirer le plateau tournant ? (b) Pourquoi mesurer sur plusieurs intervalles ? (c) La fréquence d'un four est-elle exactement $2450\ \text{MHz}$ ? (d) La cavité est tridimensionnelle : que peut-on dire de la disposition des taches ? (e) Pourquoi les taches sont-elles plus larges que ponctuelles ?

> [!success]- ✅ Correction
> **Résultat**
>
> (a) Le plateau déplace l'aliment dans l'onde et efface le motif. (b) Réduire l'incertitude. (c) Non : la fréquence de $2450\ \text{MHz}$ est nominale ; un magnétron réel dérive de quelques dizaines de MHz. (d) Le motif est 2D ou 3D (plusieurs modes), on ne mesure sur une seule ligne qu'en première approximation. (e) La conduction de la chaleur dans le chocolat étale la tache.


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> (a) Sans rotation, le chocolat reste fixe par rapport au champ : les ventres sont repérables. (b) Voir question 2. (c) Le magnétron n'est pas stabilisé ; sa fréquence dépend de la charge et de la température, de $2{,}45$ à $\pm0{,}05\ \text{GHz}$ selon les modèles (bande ISM $2{,}400$–$2{,}500\ \text{GHz}$). C'est l'incertitude la plus difficile à réduire : on peut la mesurer avec un analyseur de spectre (SDR radio bon marché).
> (d) Les ondes se réfléchissent sur les six parois : le champ est la superposition de nombreux modes de la cavité. On mesure l'espacement le long de la direction où les taches sont les plus alignées. (e) Le chocolat conduit la chaleur, donc la tache s'étend d'un demi-centimètre autour du ventre : c'est pourquoi on pointe les centres.


**q4.** Aviation. Calculer la longueur d'onde (a) de la fréquence d'urgence $121{,}5\ \text{MHz}$, (b) du radar météo de bord en bande X ($9{,}4\ \text{GHz}$), (c) du GPS L1 ($1575{,}42\ \text{MHz}$). Quelle est la longueur d'une antenne quart d'onde pour (a) ? Les gouttes de pluie ($1$ à $5\ \text{mm}$) sont-elles petites ou grandes devant $\lambda$ pour (b) ? Quelle loi de diffusion en résulte (cf. TP A4) ?

> [!success]- ✅ Correction
> **Résultat**
>
> (a) $\lambda=\dfrac{c}{f}=2{,}47\ \text{m}$ et $\dfrac{\lambda}{4}=0{,}62\ \text{m}$. (b) $\lambda=3{,}2\ \text{cm}$. (c) $\lambda=19{,}0\ \text{cm}$. Pour (b), les gouttes sont petites devant $\lambda$ : diffusion de Rayleigh, dont l'intensité varie en $D^6/\lambda^4$ ($D$ diamètre de la goutte).


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> (a) $\lambda=\dfrac{2{,}998\times10^{8}}{121{,}5\times10^{6}}=2{,}47\ \text{m}$ ; l'antenne quart d'onde mesure $61{,}7\ \text{cm}$. (b) $\lambda=\dfrac{2{,}998\times10^{8}}{9{,}4\times10^{9}}=3{,}19\ \text{cm}$. (c) $\lambda=19{,}0\ \text{cm}$.
> Pour le radar météo, les gouttes ($1$–$5\ \text{mm}$) sont petites devant $3{,}2\ \text{cm}$ : c'est le régime de Rayleigh, avec une réflectivité radar proportionnelle à $D^6$ : les grosses gouttes (grêle, forte pluie) renvoient très fortement l'énergie et sont détectées de loin. Les gouttes de nuage ($\approx10\ \mu\text{m}$) sont pratiquement invisibles. C'est le même phénomène que la diffusion du ciel bleu (TP A4), avec une longueur d'onde $10^{4}$ fois plus grande.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex6-experience-de-melde-oscillations-forcees-d-une-corde-resonance|Exercice 6 — Expérience de Melde, oscillations forcées d'une corde, résonance]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex15-corde-amortie-attenuation-facteur-de-qualite-et-resonance-de-melde|Exercice 15 — Corde amortie : atténuation, facteur de qualité et résonance de Melde]]

