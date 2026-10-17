---
title: "Exercice 3 — Équilibre et traction d'une automobile en panne"
tags:
  - td
  - general
---

[[physique/IPSA/ipsa-piscines-sciences-methodologie/TD/general/vecteurs-en-physique-4h/index|⬅ Retour]] · <a href="/pdfs/td4_PhV110_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_test_Ph110_0.pdf" target="_blank" rel="noopener">📄 PDF</a> · <a href="/pdfs/td4_PhV110_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 3. Équilibre et traction d'une automobile en panne

Une automobile en panne est tirée par deux câbles $AB$ et $AC$ exerçant des tensions $\vec{T}_{AB}$ et $\vec{T}_{AC}$. La force résultante $\vec{R}$ doit être appliquée strictement le long de l'axe longitudinal du véhicule (axe $Ox$).

Une automobile en panne est remorquée à l’aide de deux câbles
$AB$ et $AC$.

La résultante des deux forces exercées en $A$ est dirigée suivant
l’axe longitudinal de l’automobile.


**1.**

  **a)** Pour $T_{AB} = 2{,}2\text{ kN}$, $\beta = 30^\circ$ et $\alpha = 25^\circ$, déterminer, à l’aide de considérations trigonométriques, la tension $T_{AC}$ dans le câble $AC$ pour que la résultante soit dirigée suivant l’axe longitudinal de l’automobile.

> [!example]- 📝 Solution détaillée
> **Tension dans le câble AC**
>
> Pour que la résultante soit dirigée suivant l’axe $Ox$, sa composante suivant l’axe transversal doit être nulle :
>
> $$
> \overbrace{\left ( \begin{array}{c} R_x = R \\  R_y = 0 \end{array} \right )}^{\vec{R}} = \overbrace{\left ( \begin{array}{c} T_{AB,x} = T_{AB} \cos(\beta) \\  T_{AB,y} = T_{AB} \sin(\beta) \end{array} \right )}^{\vec{T}_{AB}} + \overbrace{\left ( \begin{array}{c} T_{AC,x} = T_{AC} \cos(\alpha) \\  T_{AC,y} = - T_{AC} \sin(\alpha) \end{array} \right )}^{\vec{T}_{AC}} 
> $$
>
> $$T_{AC}\sin(\alpha) = T_{AB}\sin(\beta)$$
>
> On en déduit :
> $$T_{AC} = T_{AB}\frac{\sin(\beta)}{\sin(\alpha)}$$
>
> Avec $T_{AB}=2{,}2\text{ kN}$, $\beta=30^\circ$ et $\alpha=25^\circ$ :
> $$T_{AC} = 2{,}2\frac{\sin(30^\circ)}{\sin(25^\circ)}
> \approx 2{,}60\text{ kN}$$
>
> <p style="text-align:center"><a href="/figures/td4_ex3_phv110_enonce.svg" target="_blank" rel="noopener"><img src="/figures/td4_ex3_phv110_enonce.svg" alt="" loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>


  **b)** En déduire la norme de la résultante $\vec{R}$ des deux forces appliquées en $A$.

> [!example]- 📝 Solution détaillée
> **Norme de la résultante**
>
> La résultante est dirigée suivant l’axe $Ox$. Sa norme correspond donc à la somme des composantes suivant cet axe :
> $$R = T_{AB}\cos(\beta) + T_{AC}\cos(\alpha)$$
>
> En utilisant les valeurs précédentes :
> $$R = 2{,}2\cos(30^\circ) + 2{,}60\cos(25^\circ)$$
> $$R \approx 4{,}30\text{ kN}$$


**2.**

  **a)** La tension dans le câble $AB$ est égale à $T_{AB}=3{,}0\text{ kN}$. On souhaite que la résultante des deux forces appliquées en $A$ soit une force de norme $R=4{,}8\text{ kN}$ dirigée suivant l’axe longitudinal de l’automobile.

Déterminer, à l’aide de relations trigonométriques, la tension $T_{AC}$ dans le câble $AC$.

> [!example]- 📝 Solution détaillée
> **Tension dans le câble AC**
>
> La résultante étant dirigée suivant l’axe $Ox$, les composantes suivant l’axe transversal doivent se compenser :
> $$T_{AC}\sin(\alpha) = T_{AB}\sin(\beta)$$
>
> D’autre part, la composante suivant $Ox$ de la résultante vaut :
> $$R = T_{AB}\cos(\beta) + T_{AC}\cos(\alpha)$$
>
> En combinant ces deux relations, on peut écrire :
> $$R = T_{AB}\cos(\beta)
> + T_{AB}\frac{\sin(\beta)}{\sin(\alpha)}\cos(\alpha)$$
>
> Soit :
> $$R = T_{AB}\left[\cos(\beta)
> + \sin(\beta)\cot(\alpha)\right]$$
>
> On peut également utiliser le triangle des forces. La loi des sinus donne :
> $$\frac{T_{AB}}{\sin(\alpha)}
> = \frac{T_{AC}}{\sin(\beta)}
> = \frac{R}{\sin(\alpha+\beta)}$$
>
> Ainsi :
> $$T_{AC}
> = R\frac{\sin(\beta)}{\sin(\alpha+\beta)}$$


  **b)** En déduire la valeur de l’angle $\alpha$ permettant d’obtenir cette résultante.

> [!example]- 📝 Solution détaillée
> **Calcul de l’angle alpha**
>
> D’après la loi des sinus appliquée au triangle des forces :
> $$\frac{T_{AB}}{\sin(\alpha)}
> = \frac{R}{\sin(\alpha+\beta)}$$
>
> On obtient donc :
> $$T_{AB}\sin(\alpha+\beta)
> = R\sin(\alpha)$$
>
> Avec $T_{AB}=3{,}0\text{ kN}$, $R=4{,}8\text{ kN}$ et $\beta=30^\circ$ :
> $$3{,}0\sin(\alpha+30^\circ)
> = 4{,}8\sin(\alpha)$$
>
> En développant :
> $$3{,}0\left[\sin(\alpha)\cos(30^\circ)
> +\cos(\alpha)\sin(30^\circ)\right]
> =4{,}8\sin(\alpha)$$
>
> D'où :
> $$1{,}5\cos(\alpha)
> =\left(4{,}8-3{,}0\cos(30^\circ)\right)\sin(\alpha)$$
>
> Ainsi :
> $$\tan(\alpha)
> =\frac{1{,}5}{4{,}8-3{,}0\cos(30^\circ)}
> \approx 0{,}952$$
>
> Finalement :
> $$\alpha\approx43{,}6^\circ$$

