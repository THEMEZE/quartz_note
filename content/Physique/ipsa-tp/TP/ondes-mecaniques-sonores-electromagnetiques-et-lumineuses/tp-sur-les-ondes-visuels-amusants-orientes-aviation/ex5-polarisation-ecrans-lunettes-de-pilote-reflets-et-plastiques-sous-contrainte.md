---
title: "Exercice 5 — Polarisation : écrans, lunettes de pilote, reflets et plastiques sous contrainte"
tags:
  - tp
  - ondes-mecaniques-sonores-electromagnetiques-et-lumineuses
---

[[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/index|⬅ Retour]]

### Exercice 5. Polarisation : écrans, lunettes de pilote, reflets et plastiques sous contrainte

Les lunettes de soleil polarisantes éliminent les reflets sur l'eau ou sur une piste mouillée, mais elles peuvent rendre un écran LCD noir quand on incline la tête. Dans un cockpit, cela pose la question de la lisibilité des instruments. Ce TP étudie la polarisation de la lumière avec trois objets du quotidien : un écran, une paire de lunettes polarisantes, et des morceaux de plastique transparent.

On vérifie la loi de Malus, on explique les reflets par l'angle de Brewster, on observe les couleurs dues à la contrainte dans des plastiques (visibles aussi dans certains pare-brise), et on discute l'orientation de la polarisation des écrans avec des lunettes de pilote.

**q1.** Loi de Malus. Vérifier que les données suivent la loi $I=I_{\max}\cos^2\theta+I_{\min}\sin^2\theta$ avec $I_{\max}=100$ et $I_{\min}=3$. Calculer le rapport d'extinction $I_{\max}/I_{\min}$. Que vaudrait $I$ à $45^\circ$ pour un polariseur idéal ?

**q2.** Reflets. (a) Établir que le rayon réfléchi est polarisé totalement lorsque l'angle d'incidence vérifie $\tan\theta_B=n$ (rayon réfléchi $\perp$ rayon réfracté). (b) Calculer $\theta_B$ pour l'eau ($n=1{,}33$) et le verre ($n=1{,}50$). (c) À quelle hauteur au-dessus de l'horizon est le Soleil quand son reflet sur un lac est complètement polarisé ? (d) Dans quelle direction faut-il orienter les lunettes polarisantes pour éliminer ce reflet ?

> [!tip]- 💡 Coup de pouce
> **Condition**
>
> À l'incidence de Brewster, $\theta_i+\theta_t=90^\circ$. Utiliser $\sin\theta_i=n\sin\theta_t$ et $\cos\theta_i=\sin\theta_t$.


**q3.** Biréfringence sous contrainte. Une plaque de plexiglas d'épaisseur $e=10\ \text{mm}$ subit une contrainte $\sigma=5\ \text{MPa}$. Le retard optique vaut $\Gamma=C\,\sigma\,e$ avec $C=4{,}5\times10^{-12}\ \text{Pa}^{-1}$ (coefficient photoélastique du PMMA). (a) Calculer $\Gamma$. (b) Entre polariseurs croisés, l'intensité transmise pour une lame orientée à $45^\circ$ est $I=I_0\sin^2\left(\dfrac{\pi\Gamma}{\lambda}\right)$ : calculer $I/I_0$ pour $\lambda=450$, $550$ et $650\ \text{nm}$. Quelle est la couleur de la plaque ? (c) Pourquoi voit-on des franges dans les zones où la contrainte varie ?

**q4.** Orientation des écrans. Dans le TP, un téléphone en mode portrait est noir à travers les lunettes quand celles-ci sont tournées de $90^\circ$ par rapport à la verticale, et lisible en paysage. (a) Que peut-on dire de la direction de polarisation de l'écran ? (b) Un pilote porte des lunettes polarisantes (axe vertical) et lit une tablette dont la polarisation est verticale ou horizontale selon l'orientation : que se passe-t-il ? (c) Comment une lame quart d'onde placée devant l'écran résout-elle le problème ?

**q5.** (*) Ciel polarisé. On regarde le ciel à $90^\circ$ du Soleil à travers un polariseur que l'on tourne. On mesure $I_{\max}=85$ et $I_{\min}=15$ (unités arbitraires). Calculer le degré de polarisation $P=\dfrac{I_{\max}-I_{\min}}{I_{\max}+I_{\min}}$. Comparer avec la valeur théorique de Rayleigh $P(\gamma)=\dfrac{\sin^2\gamma}{1+\cos^2\gamma}$ pour $\gamma=90^\circ$ et $\gamma=45^\circ$, et expliquer pourquoi la valeur mesurée est plus faible (voir aussi TP A4).
