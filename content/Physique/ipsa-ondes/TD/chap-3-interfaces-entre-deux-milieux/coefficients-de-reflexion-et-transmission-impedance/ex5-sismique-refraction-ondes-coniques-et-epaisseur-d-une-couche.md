---
title: "Exercice 5 — Sismique réfraction : ondes coniques et épaisseur d'une couche"
tags:
  - td
  - chap-3-interfaces-entre-deux-milieux
---

[[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/index|⬅ Retour]] · [📄 Énoncé (td3_PhV212_enonce)](/pdfs/td3_PhV212_enonce.pdf) · [📄 Énoncé (td3_enonce)](/pdfs/td3_enonce.pdf)

### Exercice 5. Sismique réfraction : ondes coniques et épaisseur d'une couche *(facultatif)*

Pour déterminer l'épaisseur $h$ d'une couche de sol meuble reposant sur un substratum rocheux, on frappe le sol en
une source $S$ (masse tombante) et on enregistre les temps d'arrivée de l'onde de compression en des capteurs
(géophones) alignés à la surface, à des distances $x$ de $S$. On modélise le sol par deux milieux homogènes superposés
séparés par un plan horizontal : la couche (1), d'épaisseur $h$, ($\rho_1=1800~\text{kg}\cdot\text{m}^{-3}$,
$c_1=1000~\text{m}\cdot\text{s}^{-1}$) et le substratum (2) ($\rho_2=2400~\text{kg}\cdot\text{m}^{-3}$,
$c_2=3000~\text{m}\cdot\text{s}^{-1}$). On ne considère que les ondes de compression (ondes P), traitées comme des
ondes acoustiques ; la surface libre ne joue qu'un rôle de réflecteur parfait en source et en capteur, et on néglige
les ondes de cisaillement.

On a relevé les temps de *première arrivée* suivants (en ms) :
$$\begin{array}{c|cccccccccc}
  x\ (\text{m}) & 10 & 20 & 30 & 40 & 50 & 60 & 70 & 80 & 100 & 120\\
  \hline
  t\ (\text{ms}) & 10{,}0 & 20{,}0 & 30{,}0 & 40{,}0 & 50{,}0 & 57{,}7 & 61{,}0 & 64{,}4 & 71{,}0 & 77{,}7
\end{array}$$

**q1.** Donner les temps de parcours de l'onde directe $t_d(x)$ et de l'onde réfléchie sur le toit du substratum $t_r(x)$
(réflexion spéculaire). Quel est le temps de réflexion minimal $t_r(0)$ ?

> [!tip]- 💡 Coup de pouce
> Pour la réflexion, utilisez la méthode de l'image : le trajet réfléchi a la longueur de la ligne droite de $S'$ (image de $S$ par rapport à l'interface) au capteur.


**q2.** Calculer l'angle critique $\theta_c$ de l'interface (1)-(2). Montrer que l'onde conique, qui descend à l'angle $\theta_c$,
glisse le long de l'interface à la vitesse $c_2$ et remonte à $\theta_c$, arrive au temps
$t_h(x)=\dfrac x{c_2}+\dfrac{2h\cos\theta_c}{c_1}$. Pour quelles distances existe-t-elle ?

> [!tip]- 💡 Coup de pouce
> Décomposez le trajet en deux tronçons obliques de longueur $h/\cos\theta_c$ (à $c_1$) et un tronçon horizontal de longueur $x-2h\tan\theta_c$ (à $c_2$). Simplifiez avec $\sin\theta_c=c_1/c_2$.


**q3.** Montrer que l'onde conique devient la première arrivée au-delà d'une distance de croisement
$x_c=2h\sqrt{\dfrac{c_2+c_1}{c_2-c_1}}$. Quelle condition faut-il sur $c_1$ et $c_2$ ?

**q4.** À partir du tableau de l'énoncé, déterminer graphiquement ou par calcul $c_1$, $c_2$, l'ordonnée à l'origine $t_i$,
la distance de croisement $x_c$ et l'épaisseur $h$. Vérifier la cohérence entre $h$ obtenu par $t_i$ et par $x_c$.

> [!tip]- 💡 Coup de pouce
> La pente de $t(x)$ pour les cinq premiers points est $1/c_1$. Pour les cinq derniers, elle est $1/c_2$ ; prolongez cette droite en $x=0$ pour avoir $t_i$.


**q5.** Vérifier que l'onde réfléchie n'est pas la première arrivée à $x=60$ m. Calculer pour cette distance l'angle
d'incidence du rayon réfléchi et le coefficient de réflexion $|R|$. Calculer aussi $R$ en incidence normale
et commenter : pourquoi les réflexions « grand angle » sont-elles plus énergétiques ?

> [!tip]- 💡 Coup de pouce
> L'angle d'incidence du rayon réfléchi vérifie $\tan\theta_1=x/(2h)$. Appliquer le résultat de l'exercice 4 : $|R|=1$ si $\theta_1>\theta_c$.


**q6.** Discuter les hypothèses du modèle : (a) que se passe-t-il si $c_2<c_1$ ? (b) à quelle condition sur la longueur d'onde
les rayons sont-ils une bonne description ? Estimer la fréquence minimale pour une impulsion sismique avec
$\lambda<h/3$. (c) Que change une interface inclinée ?

> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex4-incidence-oblique-lois-de-snell-descartes-angle-critique-reflexion-totale-et-onde-evanescente|Exercice 4 — Incidence oblique : lois de Snell-Descartes, angle critique, réflexion totale et onde évanescente]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex2-interface-entre-deux-milieux-notion-d-impedance-acoustique|Exercice 2 — Interface entre deux milieux, notion d'impédance acoustique]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex6-controle-ultrasonore-d-une-plaque-immergee-train-d-echos-epaisseur-attenuation-et-defaut-de-collage|Exercice 6 — Contrôle ultrasonore d'une plaque immergée : train d'échos, épaisseur, atténuation et défaut de collage]]

