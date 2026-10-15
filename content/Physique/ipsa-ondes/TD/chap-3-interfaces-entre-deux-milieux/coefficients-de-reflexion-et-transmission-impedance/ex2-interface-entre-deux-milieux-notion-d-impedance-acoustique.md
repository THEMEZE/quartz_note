---
title: "Exercice 2 — Interface entre deux milieux, notion d'impédance acoustique"
tags:
  - td
  - chap-3-interfaces-entre-deux-milieux
---

[[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/index|⬅ Retour]] · [📄 Corrigé (td3_PhV212_corrige)](/pdfs/td3_PhV212_corrige.pdf) · [📄 Corrigé (td3_corrige)](/pdfs/td3_corrige.pdf) · [📄 Énoncé (td3_PhV212_enonce)](/pdfs/td3_PhV212_enonce.pdf) · [📄 Énoncé (td3_enonce)](/pdfs/td3_enonce.pdf) · [📄 Aides](/pdfs/td3_PhV212_aides.pdf) · [📄 Fiche enseignant](/pdfs/td3_PhV212_fiche.pdf)

### Exercice 2. Interface entre deux milieux, notion d'impédance acoustique

Une onde ultrasonore (non perceptible par l'oreille humaine) plane,
progressive, sinusoïdale de fréquence $f=500$ kHz se propage dans l'air
(qui occupe la région $x<0$) suivant la direction $x'Ox$. Elle rencontre
l'interface air-aluminium en $x=0$.

On donne les masses volumiques de l'air $\rho_1=1{,}3~\text{kg}\cdot\text{m}^{-3}$
et de l'aluminium $\rho_2=2700~\text{kg}\cdot\text{m}^{-3}$. On donne les
célérités de l'onde ultrasonore dans l'air $c_1=340~\text{m}\cdot\text{s}^{-1}$
et dans l'aluminium $c_2=5110~\text{m}\cdot\text{s}^{-1}$.

[![Suggestion : reprendre le schéma de l'interface fluide-fluide du TD2 (exercice 4), en remplaçant le second milieu par un solide (hachures caractéristiques d'un matériau rigide) ; faire figurer $\rho_1,c_1,Z_1$ côté air et $\rho_2,c_2,Z_2$ côté aluminium, avec des flèches d'épaisseurs très différentes pour l'onde réfléchie (quasi totale) et l'onde transmise (quasi nulle).](/figures/td3_ex2_interface_air_alu.svg)](/figures/td3_ex2_interface_air_alu.svg)

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


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex4-incidence-oblique-lois-de-snell-descartes-angle-critique-reflexion-totale-et-onde-evanescente|Exercice 4 — Incidence oblique : lois de Snell-Descartes, angle critique, réflexion totale et onde évanescente]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex5-sismique-refraction-ondes-coniques-et-epaisseur-d-une-couche|Exercice 5 — Sismique réfraction : ondes coniques et épaisseur d'une couche]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex6-controle-ultrasonore-d-une-plaque-immergee-train-d-echos-epaisseur-attenuation-et-defaut-de-collage|Exercice 6 — Contrôle ultrasonore d'une plaque immergée : train d'échos, épaisseur, atténuation et défaut de collage]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex3-perle-sur-une-corde-jonction-massive-filtre-passe-bas-puis-passe-bande|Exercice 3 — Perle sur une corde : jonction massive, filtre passe-bas puis passe-bande]]

