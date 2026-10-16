---
title: "Exercice 1 — Balance de Cavendish : peser la Terre et mesurer G"
tags:
  - tp
  - gravitation-optique-geometrique-et-diffusion-de-la-lumiere
---

[[physique/ipsa-tp/TP/gravitation-optique-geometrique-et-diffusion-de-la-lumiere/tp-d-astrophysique-de-la-balance-de-cavendish-a-la-densite-du-soleil-et-couleurs-du-ciel/index|⬅ Retour]]

### Exercice 1. Balance de Cavendish : peser la Terre et mesurer G

En 1798, Henry Cavendish mesure l'attraction gravitationnelle entre deux boules de plomb de quelques dizaines de centimètres à l'aide d'un fléau suspendu à un fil de torsion. Il en déduit la densité moyenne de la Terre. Sa mesure ne donne pas $G$ directement ; c'est le lien $g=GM_T/R_T^2$ qui permet, une fois $G$ connue, de « peser » la Terre.

Dans ce TP, on utilise une balance de Cavendish de démonstration (deux petites masses $m$ au bout d'un fléau, deux grosses masses $M$ mobiles, miroir et pointeur laser) pour **mesurer $G$**, évaluer une incertitude, et identifier les erreurs systématiques. La valeur de $G$ obtenue est réutilisée dans le TP A3 pour déterminer la densité du Soleil.

**q1.** Modèle. Deux masses $m$ sont placées aux extrémités d'un fléau de longueur $2r$ (masse négligée) suspendu à un fil de constante de torsion $\kappa$. Chaque petite masse subit de la part de la grosse masse la plus proche, à la distance $b$, la force $GMm/b^2$ (on néglige d'abord l'attraction de la grosse masse sur l'autre petite masse). À l'équilibre le fléau a tourné de l'angle $\theta$. Écrire l'équation d'équilibre des moments et la période $T$ des petites oscillations. En déduire
$$G=\frac{4\pi^2\,r\,b^2\,\theta}{M\,T^2}.$$

> [!tip]- 💡 Coup de pouce
> **Deux relations**
>
> Équilibre : $\kappa\theta=2r\times\dfrac{GMm}{b^2}$. Oscillations : $I\ddot\theta=-\kappa\theta$ avec $I=2mr^2$. Éliminer $\kappa$ pour que la masse $m$ disparaisse.


**q2.** Levier optique. Un miroir solidaire du fléau renvoie un faisceau laser sur un écran situé à $L$ du miroir. Montrer qu'un retournement des grosses masses qui fait tourner le fléau de $2\theta$ déplace le spot de $\Delta s=4\theta L$. Application numérique pour $\Delta s=78\ \text{mm}$ et $L=3{,}00\ \text{m}$.

**q3.** Correction de la géométrie. Les grosses masses attirent aussi la petite masse la plus éloignée, dont le moment s'oppose au moment principal. En plaçant chaque grosse masse à la distance $b$ perpendiculairement au fléau devant une petite masse, la distance à l'autre petite masse est $D=\sqrt{b^2+4r^2}$. Montrer que le moment total est $\Gamma=\dfrac{2rGMm}{b^2}(1-\beta)$ avec $\beta=\dfrac{b^3}{D^3}$. Calculer $\beta$ pour $b=46\ \text{mm}$ et $r=50\ \text{mm}$. Quelle conséquence sur $G$ ?

> [!tip]- 💡 Coup de pouce
> **Composante utile**
>
> La force de la grosse masse $A$ sur la petite masse éloignée fait un angle avec la perpendiculaire au fléau : sa composante utile est $\dfrac{GMm}{D^2}\times\dfrac{b}{D}$, avec un bras de levier $r$ et un signe opposé.


**q4.** Calculer $G$ avec les données de l'énoncé, avant puis après correction. Estimer l'incertitude relative sur $G$ (i) par la méthode logarithmique en somme absolue (TD2 exercice 8), (ii) en somme quadratique (TD2 exercice 9). Comparer avec la valeur tabulée $6{,}674\times10^{-11}\ \text{N}\cdot\text{m}^2\cdot\text{kg}^{-2}$.

> [!tip]- 💡 Coup de pouce
> **Exposants**
>
> $G\propto r\,b^2\,\Delta s\,M^{-1}L^{-1}T^{-2}$ : les exposants $1,2,1,-1,-1,-2$ pondèrent les incertitudes relatives (le facteur $1-\beta$ est traité à part).


**q5.** Critique des mesures. Pour chacune des sources suivantes, dire dans quel sens elle biaise $G$ et proposer une manière de la contrôler : (a) équilibre non atteint, (b) courants d'air et gradients thermiques, (c) forces électrostatiques, (d) attraction des murs, de la table et de l'opérateur, (e) fil de torsion non linéaire et dérive, (f) fléau de masse non nulle, (g) mesure de $b$.

**q6.** Peser la Terre. Avec $g=9{,}81\ \text{m}\cdot\text{s}^{-2}$ et $R_T=6{,}371\times10^{6}\ \text{m}$, calculer la masse $M_T$ et la densité moyenne $\rho_T$ de la Terre à partir de votre valeur de $G$. Comparer avec la valeur de Cavendish ($5{,}45\ \text{g}\cdot\text{cm}^{-3}$) et avec les densités du granite ($2{,}7$) et du fer ($7{,}9$). Que peut-on en conclure sur l'intérieur de la Terre ?

> [!note] 🔗 Voir aussi
> [[physique/ipsa-tp/TP/gravitation-optique-geometrique-et-diffusion-de-la-lumiere/tp-d-astrophysique-de-la-balance-de-cavendish-a-la-densite-du-soleil-et-couleurs-du-ciel/ex3-densite-du-soleil-de-cavendish-au-stenope|Exercice 3 — Densité du Soleil : de Cavendish au sténopé]]

