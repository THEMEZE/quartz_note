---
title: "Exercice 4 — Pourquoi le ciel est bleu et le Soleil couchant rouge : diffusion de Rayleigh dans un aquarium"
tags:
  - tp
  - gravitation-optique-geometrique-et-diffusion-de-la-lumiere
---

[[physique/ipsa-tp/TP/gravitation-optique-geometrique-et-diffusion-de-la-lumiere/tp-d-astrophysique-de-la-balance-de-cavendish-a-la-densite-du-soleil-et-couleurs-du-ciel/index|⬅ Retour]]

### Exercice 4. Pourquoi le ciel est bleu et le Soleil couchant rouge : diffusion de Rayleigh dans un aquarium

La lumière du Soleil est blanche, et pourtant le ciel est bleu à midi alors que le Soleil paraît rouge-orangé à l'horizon. Les deux observations viennent de la même cause : la **diffusion de Rayleigh** de la lumière par les molécules de l'air, dont l'intensité varie en $\lambda^{-4}$. Le bleu est diffusé dans toutes les directions (d'où le ciel bleu) et il est donc retiré du faisceau direct ; plus le trajet dans l'atmosphère est long, plus le faisceau direct devient rouge.

Dans ce TP, on reproduit l'effet à petite échelle : un bac d'eau très légèrement troublée (quelques gouttes de lait) est éclairé par une lampe blanche. Vu de côté, le faisceau est bleuté ; vu dans l'axe, à travers une grande longueur d'eau, le spot devient orange. On **mesure** ensuite le rapport des coefficients d'extinction dans le bleu et dans le rouge à l'aide de photographies du smartphone.

**q1.** Diffusion de Rayleigh. L'intensité diffusée par des particules petites devant $\lambda$ varie comme $\lambda^{-4}$. Calculer les rapports $\dfrac{I(450\ \text{nm})}{I(650\ \text{nm})}$ et $\dfrac{I(400\ \text{nm})}{I(450\ \text{nm})}$. Pourquoi le ciel n'est-il pas violet, alors que le violet est plus diffusé que le bleu ?

**q2.** Atmosphère et coucher de Soleil. L'épaisseur optique verticale de l'atmosphère à $550\ \text{nm}$ vaut $\tau_0\approx0{,}10$ (diffusion de Rayleigh seule). (a) Calculer $\tau$ à $450$, $550$ et $650\ \text{nm}$ pour un faisceau vertical. (b) Pour un Soleil à l'horizon, la masse d'air relative vaut $m\approx38$. Calculer la transmission $e^{-m\tau}$ dans chaque couleur. Quelle est la couleur du Soleil ? (c) Le Soleil est-il plus rouge quand il est bas sur l'horizon ou à $45^\circ$ ($m=1{,}41$) ?

> [!tip]- 💡 Coup de pouce
> **Loi d'échelle**
>
> $\tau(\lambda)=\tau_0\left(\dfrac{550}{\lambda}\right)^4$ et $T=e^{-m\tau}$.


**q3.** Analyse des mesures. Avec les données de l'énoncé, tracer $\ln(I/I_0)$ en fonction de $L$ pour les canaux rouge et bleu. Ajuster deux droites passant par l'origine, en déduire $\alpha_R$, $\alpha_B$ et le rapport $\alpha_B/\alpha_R$. Comparer avec $\left(\dfrac{\lambda_R}{\lambda_B}\right)^4$ pour $\lambda_R=620\ \text{nm}$ et $\lambda_B=450\ \text{nm}$.

> [!tip]- 💡 Coup de pouce
> **Linéarisation**
>
> $\ln\dfrac{I}{I_0}=-\alpha L$. La pente d'un ajustement par l'origine est $-\dfrac{\sum L_i\ln(I_i/I_0)}{\sum L_i^2}$.


**q4.** Critique. Citer trois causes d'erreur sur $\alpha_B/\alpha_R$ dans la manipulation et proposer comment les contrôler.

**q5.** Polarisation. Observer le faisceau à $90^\circ$ à travers un polariseur. (a) Que voit-on quand on tourne le polariseur ? (b) Justifier avec le modèle du dipôle rayonnant : le champ $\vec E$ de la lumière incidente est perpendiculaire à la direction de propagation ; il fait osciller les charges de la molécule dans le plan perpendiculaire. (c) Où faut-il regarder dans le ciel pour observer la polarisation maximale ? Pour quelle direction est-elle nulle ?

**q6.** (*) Aviation et visibilité. La loi de Koschmieder définit la visibilité météorologique par la distance $V$ à laquelle le contraste d'un objet noir sur l'horizon tombe à $2\ \%$ : $V=\dfrac{\ln(1/0{,}02)}{\sigma}=\dfrac{3{,}91}{\sigma}$. (a) Quelle est la visibilité si $\sigma=0{,}4\ \text{km}^{-1}$ ? (b) L'extinction due à la seule diffusion de Rayleigh vaut $\sigma_R\approx1{,}2\times10^{-2}\ \text{km}^{-1}$ à $550\ \text{nm}$ : quelle serait la visibilité maximale dans un air parfaitement pur ? (c) Un pilote voit deux montagnes lointaines : pourquoi la plus éloignée est-elle plus bleue et moins contrastée ?
