---
title: "Exercice 2 — Interface entre deux milieux, notion d'impédance acoustique"
tags:
  - td
  - chap-3-interfaces-entre-deux-milieux
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/index|⬅ Retour]] · <a href="/pdfs/td3_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_PhV212_enonce)</a> · <a href="/pdfs/td3_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_enonce)</a> · <a href="/pdfs/td3_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td3_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td3_PhV212_corrige)</a> · <a href="/pdfs/td3_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td3_corrige)</a>

### Exercice 2. Interface entre deux milieux, notion d'impédance acoustique

*⭐ Indispensable · Difficulté ●●○○○ · ⏱ 20 min · Type : Application numérique*

Une onde ultrasonore (non perceptible par l'oreille humaine) plane,
progressive, sinusoïdale de fréquence $f=500$ kHz se propage dans l'air
(qui occupe la région $x<0$) suivant la direction $x'Ox$. Elle rencontre
l'interface air-aluminium en $x=0$.

On donne les masses volumiques de l'air $\rho_1=1{,}3~\text{kg}\cdot\text{m}^{-3}$
et de l'aluminium $\rho_2=2700~\text{kg}\cdot\text{m}^{-3}$. On donne les
célérités de l'onde ultrasonore dans l'air $c_1=340~\text{m}\cdot\text{s}^{-1}$
et dans l'aluminium $c_2=5110~\text{m}\cdot\text{s}^{-1}$.

<p style="text-align:center"><a href="/figures/td3_ex2_interface_air_alu.svg" target="_blank" rel="noopener"><img src="/figures/td3_ex2_interface_air_alu.svg" alt="Suggestion : reprendre le schéma de l'interface fluide-fluide du TD2 (exercice 4), en remplaçant le second milieu par un solide (hachures caractéristiques d'un matériau rigide) ; faire figurer $\rho_1,c_1,Z_1$ côté air et $\rho_2,c_2,Z_2$ côté aluminium, avec des flèches d'épaisseurs très différentes pour l'onde réfléchie (quasi totale) et l'onde transmise (quasi nulle)." loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>


> [!question]- 🪝 Accroche
> **Pourquoi un gel pour l'échographie, un bain d'eau pour les métaux ?**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *Pour contrôler une pièce métallique aux ultrasons, on place la sonde dans un bain d'eau ou on étale du gel, jamais directement dans l'air. Quelle fraction de l'énergie ultrasonore traverse une interface air-aluminium ? Un millième ? Un dix-millième ? Avant de calculer, faites un pari, puis calculez.*
>
> **Idée clé : seul le contraste d'impédance $Z=\rho c$ compte.** À une interface, $R=\left(\dfrac{Z_1-Z_2}{Z_1+Z_2}\right)^2$ et $T=\dfrac{4Z_1Z_2}{(Z_1+Z_2)^2}$ avec $R+T=1$. Pour l'air ($Z_1\approx442$ rayl) et l'aluminium ($Z_2\approx1{,}38\times10^7$ rayl), le rapport est $Z_2/Z_1\approx3\times10^4$ : $R\approx0{,}9999$ et $T\approx1{,}3\times10^{-4}$. Le désaccord d'impédance interdit la transmission, quelles que soient les valeurs de $\rho$ et de $c$ prises séparément.




> [!abstract]- 🧠 À savoir avant
> **Coefficients de réflexion et de transmission en énergie à une interface**
>
> Cet exercice réutilise directement les résultats généraux établis pour l'interface fluide-fluide (TD2) : à une interface entre deux milieux d'impédances acoustiques caractéristiques $Z_1=\rho_1c_1$ et $Z_2=\rho_2c_2$, les coefficients **énergétiques** de réflexion et de transmission s'écrivent
> $$R = \left(\frac{Z_1-Z_2}{Z_1+Z_2}\right)^2, \qquad T = 1-R = \frac{4Z_1Z_2}{(Z_1+Z_2)^2}.$$
> Ces formules restent valables à une interface fluide-solide dès lors que l'on assimile la propagation dans le solide à une onde de compression (longitudinale) de célérité $c_2$ caractérisée par la même impédance $Z=\rho c$ — approximation raisonnable en incidence normale, tant que l'on ignore les ondes de cisaillement propres aux solides (cf. aller plus loin).




> [!info]- 🎯 Ce que tu sauras faire
> **Appliquer numériquement le concept d'impédance à un cas fluide-solide**
>
> Savoir calculer une impédance acoustique caractéristique à partir de données tabulées, évaluer le degré d'adaptation d'impédance entre deux milieux très différents, et interpréter physiquement un coefficient de transmission énergétique très faible en le reliant à une application concrète (imagerie médicale par ultrasons).




> [!tip]- 📖 Rappel de cours
> **Rappel express : de l'amplitude à l'énergie**
>
> On rappelle (TD2) que le passage des coefficients en *amplitude de pression* $R_p=(Z_2-Z_1)/(Z_1+Z_2)$ aux coefficients en *énergie* (intensité acoustique moyenne, proportionnelle au carré de l'amplitude) se fait simplement par mise au carré : $R=R_p^2$, ce qui rend le résultat indépendant du signe de $Z_2-Z_1$ — un point important ici, où l'on peut directement écrire $R=((Z_1-Z_2)/(Z_1+Z_2))^2$ sans se soucier de l'ordre des indices.
>
> **Attention de notation** : dans cet exercice (comme souvent dans les énoncés), les lettres $R$ et $T$ désignent directement les coefficients *énergétiques* (et non plus les coefficients en amplitude de pression notés $R,T$ dans l'exercice 4 du TD2) : il faut donc être attentif, d'un exercice à l'autre, à la grandeur physique que ces mêmes lettres désignent.




> [!note]- 🧮 Outils mathématiques
> **Ordres de grandeur et notation scientifique**
>
> $Z_1=1{,}3\times340=442$ et $Z_2=2700\times5110\approx1{,}38\times10^7$ : travailler avec des puissances de $10$ évite les erreurs de plusieurs décades. Le rapport $Z_2/Z_1\approx3{,}1\times10^4$ est l'information essentielle.
>
> **Éviter la soustraction de deux nombres proches**
>
> $T=1-R=1-0{,}999872$ fait perdre des chiffres significatifs (annulation catastrophique). Il vaut mieux calculer directement $T=\dfrac{4Z_1Z_2}{(Z_1+Z_2)^2}$, qui n'implique aucune soustraction.
>
> **Développement pour un grand rapport**
>
> En posant $x=Z_2/Z_1\gg1$ : $T=\dfrac{4x}{(1+x)^2}\approx\dfrac4x$, donc $T\approx\dfrac{4\times442}{1{,}38\times10^7}=1{,}3\times10^{-4}$ : on retrouve le résultat sans calculatrice.
>
> **Carré d'une amplitude et énergie**
>
> L'intensité est proportionnelle au carré de l'amplitude : $R=R_p^2$. La mise au carré rend $R$ indépendant du signe de $Z_2-Z_1$, d'où $R=T$ dans les deux sens de propagation.
>
> **Décibels**
>
> $10\log_{10}T=10\log_{10}(1{,}3\times10^{-4})\approx-39$ dB : une atténuation de transmission d'environ $39$ dB, soit un facteur $8\times10^3$ en énergie.
>
> **Longueur d'onde et résolution**
>
> $\lambda=c/f$ : à $500$ kHz, $\lambda_{\text{air}}=0{,}68$ mm et $\lambda_{\text{Al}}\approx1{,}0$ cm. On ne détecte que des défauts de taille au moins comparable à $\lambda$, ce qui explique le choix de fréquences élevées en imagerie.
>
> **Moyenne géométrique pour l'impédance intermédiaire**
>
> Une couche d'adaptation d'impédance $Z_m=\sqrt{Z_1Z_2}=\sqrt{442\times1{,}38\times10^7}\approx7{,}8\times10^4$ rayl minimise la réflexion entre deux milieux de forts contrastes (cf. lame quart d'onde, exercice 11 du chapitre 1).



**q1.** Calculer les impédances acoustiques $Z_1$ et $Z_2$ caractéristiques de l'air et de l'aluminium. Conclusion : le système est-il adapté en impédance ?


> [!tip]- 💡 Coup de pouce
> Impédance acoustique caractéristique : $Z=\rho c$ (cf. prérequis et TD2).




> [!success]- ✅ Correction
> $Z_1=\rho_1c_1=1.3\times340\approx442$ kg·m$^{-2}$·s$^{-1}$ (rayl).
> $Z_2=\rho_2c_2=2700\times5110\approx1.38\times10^7$ rayl.
> $Z_2\gg Z_1$ : le système est très mal adapté en impédance.




> [!example]- 📝 Solution détaillée
> **Calcul numérique des deux impédances**
>
> $$Z_1 = \rho_1 c_1 = 1{,}3 \times 340 = 442~\text{kg}\cdot\text{m}^{-2}\cdot\text{s}^{-1},$$
> $$Z_2 = \rho_2 c_2 = 2700 \times 5110 = 13\,797\,000 \approx 1{,}38\times10^7~\text{kg}\cdot\text{m}^{-2}\cdot\text{s}^{-1}.$$
>
> **Conclusion sur l'adaptation d'impédance**
>
> Le rapport des impédances vaut
> $$\frac{Z_2}{Z_1} = \frac{1{,}38\times10^7}{442} \approx 3{,}1\times10^4,$$
> soit un désaccord de plus de quatre ordres de grandeur. Le système air/aluminium est donc extrêmement **mal adapté en impédance** : on s'attend, d'après le bilan qualitatif du TD2, à ce que la quasi-totalité de l'énergie incidente soit réfléchie à l'interface (à vérifier quantitativement en question 2).



**q2.** Calculer le pourcentage d'énergie de l'onde incidente qui est transmise dans l'aluminium. Interpréter ce résultat. Vous pouvez calculer les coefficients en énergie $R$ et $T$.


> [!tip]- 💡 Coup de pouce
> Coefficient de réflexion en énergie $R=\left(\dfrac{Z_1-Z_2}{Z_1+Z_2}\right)^2$, et $T=1-R=\dfrac{4Z_1Z_2}{(Z_1+Z_2)^2}$ (cf. prérequis).




> [!success]- ✅ Correction
> $R\approx\left(\dfrac{442-1.38\times10^7}{442+1.38\times10^7}\right)^2\approx0.9999$ (quasi tout est réfléchi).
> $T=1-R\approx1.3\times10^{-4}$, soit environ $0.013\%$ de l'énergie transmise :
> un fort désaccord d'impédance réfléchit presque toute l'onde -- c'est le
> principe utilisé en échographie (gel de couplage) pour éviter cette perte.




> [!example]- 📝 Solution détaillée
> **Calcul détaillé de $R$**
>
> Avec $Z_1=442$ et $Z_2=1{,}3797\times10^7$ (SI), on calcule d'abord la somme et la différence :
> $$Z_1+Z_2 \approx 1{,}379744\times10^7, \qquad Z_2-Z_1 \approx 1{,}379656\times10^7.$$
> Le rapport vaut
> $$\frac{Z_2-Z_1}{Z_1+Z_2} \approx \frac{1{,}379656}{1{,}379744} \approx 0{,}999936,$$
> d'où, en mettant au carré (le signe de la différence n'a pas d'importance pour le coefficient énergétique) :
> $$R = \left(\frac{Z_2-Z_1}{Z_1+Z_2}\right)^2 \approx (0{,}999936)^2 \approx 0{,}999872.$$
>
> **Coefficient de transmission et interprétation**
>
> Par conservation de l'énergie (aucune dissipation supposée à l'interface) :
> $$T = 1-R \approx 1-0{,}999872 = 0{,}000128 \approx 1{,}3\times10^{-4},$$
> soit environ $\boxed{0{,}013\,\%}$ de l'énergie incidente transmise dans l'aluminium — une fraction extrêmement faible, cohérente avec le très fort désaccord d'impédance mis en évidence en question 1.
>
> **Interprétation physique** : plus de $99{,}98\,\%$ de l'énergie acoustique incidente est réfléchie à l'interface air/aluminium. C'est précisément la raison pour laquelle, en échographie médicale, on interpose un gel de couplage entre la sonde et la peau : sans lui, la moindre lame d'air entre la sonde et le corps réfléchirait la quasi-totalité du signal ultrasonore (comme ici pour l'aluminium), rendant l'examen inexploitable. Le gel, dont l'impédance acoustique est proche de celle des tissus mous, permet au contraire une transmission efficace de l'onde vers le corps.




> [!note]- 🔗 Liens avec d'autres disciplines
> **Imagerie médicale**
>
> Les tissus mous ont une impédance proche de $1{,}5\times10^6$ rayl : le gel fait disparaître la lame d'air entre la sonde et la peau, qui réfléchirait presque tout. Chaque interface entre organes renvoie un écho dont l'amplitude dépend de leur contraste d'impédance.
>
> **Contrôle non destructif**
>
> Fissures, inclusions de gaz et décollements dans les soudures, les pièces d'avion ou les rails sont détectés comme des interfaces à très fort contraste d'impédance : l'écho est quasi total et permet de les localiser.
>
> **Biologie et physiologie de l'audition**
>
> Les osselets de l'oreille moyenne servent d'adaptateur d'impédance entre l'air et le liquide de l'oreille interne ($Z$ presque $3600$ fois plus grande) : sans eux, la plus grande partie de l'énergie sonore serait réfléchie.
>
> **Optique**
>
> Le même contraste produit les reflets sur une vitre ($R\approx4\ \%$ pour l'optique air-verre) et justifie les couches antireflet quart d'onde de $n_m=\sqrt{n_1n_2}$.
>
> **Électricité**
>
> Adaptation d'impédance entre un générateur et une charge pour maximiser la puissance transmise : on utilise un transformateur ou un étage d'adaptation, analogue du gel acoustique.




> [!question]- 🔭 Aller plus loin — Master : Ondes de compression et de cisaillement dans un solide
> Contrairement à un fluide, un solide comme l'aluminium peut également transmettre des ondes de cisaillement (transverses), en plus des ondes de compression (longitudinales) considérées ici. En incidence oblique, une partie de l'énergie incidente se convertit en onde transverse dans le solide (conversion de mode), ce qui complique le bilan énergétique par rapport au cas purement fluide-fluide du TD2 : la matrice de passage à l'interface doit alors tenir compte de deux célérités distinctes dans le solide ($c_L$ pour les ondes longitudinales, $c_T<c_L$ pour les ondes transverses).




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex4-incidence-oblique-lois-de-snell-descartes-angle-critique-reflexion-totale-et-onde-evanescente|Exercice 4 — Incidence oblique : lois de Snell-Descartes, angle critique, réflexion totale et onde évanescente]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex5-sismique-refraction-ondes-coniques-et-epaisseur-d-une-couche|Exercice 5 — Sismique réfraction : ondes coniques et épaisseur d'une couche]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex6-controle-ultrasonore-d-une-plaque-immergee-train-d-echos-epaisseur-attenuation-et-defaut-de-collage|Exercice 6 — Contrôle ultrasonore d'une plaque immergée : train d'échos, épaisseur, atténuation et défaut de collage]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex3-perle-sur-une-corde-jonction-massive-filtre-passe-bas-puis-passe-bande|Exercice 3 — Perle sur une corde : jonction massive, filtre passe-bas puis passe-bande]]


