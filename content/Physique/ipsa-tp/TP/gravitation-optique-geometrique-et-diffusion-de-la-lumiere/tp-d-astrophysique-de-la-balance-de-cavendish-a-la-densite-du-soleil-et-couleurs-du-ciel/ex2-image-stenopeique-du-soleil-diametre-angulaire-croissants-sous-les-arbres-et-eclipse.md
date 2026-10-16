---
title: "Exercice 2 — Image sténopéique du Soleil : diamètre angulaire, croissants sous les arbres et éclipse"
tags:
  - tp
  - gravitation-optique-geometrique-et-diffusion-de-la-lumiere
---

[[physique/ipsa-tp/TP/gravitation-optique-geometrique-et-diffusion-de-la-lumiere/tp-d-astrophysique-de-la-balance-de-cavendish-a-la-densite-du-soleil-et-couleurs-du-ciel/index|⬅ Retour]]

### Exercice 2. Image sténopéique du Soleil : diamètre angulaire, croissants sous les arbres et éclipse

Sous un arbre, les taches de lumière au sol sont rondes : chaque trou entre les feuilles se comporte comme un sténopé et projette une **image du Soleil**. Pendant une éclipse partielle, ces taches deviennent des croissants, images du Soleil partiellement masqué par la Lune. Le 12 août 2026, la France a connu une éclipse partielle profonde en fin de journée (plus de $90\ \%$ à Paris) ; les photographies de ce jour peuvent servir de données.

Dans ce TP, on construit un sténopé, on mesure la taille de l'image du Soleil à différentes distances pour en déduire son **diamètre angulaire** $\theta$, puis son rayon. On étudie ensuite ce qui décide qu'une tache de lumière est l'image du Soleil (croissant) ou la forme du trou. La valeur de $\theta$ sera réutilisée dans le TP A3 (densité du Soleil).

**q1.** Modèle. Un objet lointain vu sous l'angle $\theta$ forme, à travers un trou de très petite taille, une image de taille $d$ sur un écran situé à la distance $D$ du trou. Montrer que $d=2D\tan(\theta/2)\approx D\theta$. L'image est-elle droite ou renversée ? Est-elle plus grande ou plus petite si on double $D$ ?

**q2.** Traiter les données de l'énoncé : tracer $d$ en fonction de $D$, ajuster une droite passant par l'origine, en déduire $\theta$ en radians et en degrés (avec incertitude), puis comparer à la valeur de référence $\theta_{\text{ref}}=9{,}30\ \text{mrad}$ ($0{,}533^\circ$).

> [!tip]- 💡 Coup de pouce
> **Régression**
>
> Pente : $\theta=\dfrac{\sum D_id_i}{\sum D_i^2}$ pour un ajustement par l'origine. Estimer l'incertitude par la dispersion des rapports $d_i/D_i$.


**q3.** Sachant que la distance moyenne Terre-Soleil est $a=1{,}496\times10^{11}\ \text{m}$, calculer le rayon du Soleil. Comparer avec la valeur tabulée $6{,}96\times10^{8}\ \text{m}$. Dans le même esprit, on mesure la Lune sous l'angle $\theta_L=9{,}0\ \text{mrad}$ ; sa distance est de $3{,}84\times10^{8}\ \text{m}$. Calculer son rayon et discuter le rapport avec le Soleil.

**q4.** Effet de la taille du trou $s$. Pour $D=1{,}00\ \text{m}$, décrire ce que l'on attend pour $s=0{,}3\ ;\ 1\ ;\ 3\ ;\ 10\ ;\ 30\ \text{mm}$. On approxime l'étalement de l'image par $\delta\approx s$ (flou géométrique) et par $\delta_{\text{diff}}=\dfrac{2{,}44\lambda D}{s}$ (diffraction, $\lambda=550\ \text{nm}$). Trouver la valeur optimale de $s$ et calculer le diamètre apparent de l'image pour chacune des valeurs de $s$.

> [!tip]- 💡 Coup de pouce
> **Diamètre apparent**
>
> $d_{\text{app}}\approx D\theta+s$ (image du Soleil élargie de la taille du trou), auquel s'ajoute la diffraction si $s$ est très petit.


**q5.** Taches sous un arbre. Les feuilles d'un arbre sont à la hauteur $h=10\ \text{m}$ au-dessus du sol. (a) Quel est le diamètre des taches de lumière si le Soleil est au zénith ? (b) Le Soleil est à la hauteur $\varepsilon=40^\circ$ au-dessus de l'horizon : les taches sont elliptiques. Calculer leur grand axe et expliquer. (c) Le trou entre les feuilles mesure $s=3\ \text{cm}$ : la tache est-elle l'image du Soleil ? (d) Et si $s=50\ \text{cm}$ ?

**q6.** Éclipse partielle. Lors de l'éclipse partielle du 12 août 2026, l'obscuration à Paris atteignait $92\ \%$ au maximum. (a) Pourquoi les taches sous un arbre prennent-elles la forme de croissants ? (b) Le croissant sur le sol pointe-t-il dans la même direction que le croissant du Soleil dans le ciel ? (c) Le diamètre des taches change-t-il pendant l'éclipse ? (d) Photographier une passoire ou un chapeau de paille : chaque trou donne un croissant. Proposer un montage de mesure pour vérifier que la largeur du croissant diminue quand l'obscuration augmente.

**q7.** (*) Pourquoi le diamètre angulaire du Soleil est-il une donnée cruciale pour la suite ? Justifier que la mesure de $\theta$ et de la période orbitale $T$ suffit, avec la constante $G$, à obtenir la densité moyenne du Soleil (TP A3).
