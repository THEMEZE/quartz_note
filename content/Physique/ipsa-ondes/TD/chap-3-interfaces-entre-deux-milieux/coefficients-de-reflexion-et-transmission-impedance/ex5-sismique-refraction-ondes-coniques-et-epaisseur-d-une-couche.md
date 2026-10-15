---
title: "Exercice 5 — Sismique réfraction : ondes coniques et épaisseur d'une couche"
tags:
  - td
  - chap-3-interfaces-entre-deux-milieux
---

[[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/index|⬅ Retour]] · [📄 Corrigé (td3_PhV212_corrige)](/pdfs/td3_PhV212_corrige.pdf) · [📄 Corrigé (td3_corrige)](/pdfs/td3_corrige.pdf) · [📄 Énoncé (td3_PhV212_enonce)](/pdfs/td3_PhV212_enonce.pdf) · [📄 Énoncé (td3_enonce)](/pdfs/td3_enonce.pdf) · [📄 Aides](/pdfs/td3_PhV212_aides.pdf) · [📄 Fiche enseignant](/pdfs/td3_PhV212_fiche.pdf)

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


> [!success]- ✅ Correction
> $t_d=x/c_1$ ; $t_r=\sqrt{x^2+4h^2}/c_1$ ; $t_r(0)=2h/c_1$.


> [!example]- 📝 Solution détaillée
> **Onde directe**
>
> L'onde directe voyage à la surface dans la couche (1) : $t_d=x/c_1$.
>
> **Onde réfléchie**
>
> La méthode de l'image donne un trajet de longueur $\sqrt{x^2+(2h)^2}$ à la vitesse $c_1$ :
> $$t_r=\frac{\sqrt{x^2+4h^2}}{c_1}.$$
> C'est une hyperbole : $t_r^2=x^2/c_1^2+t_0^2$ avec $t_0=t_r(0)=2h/c_1$ (aller-retour vertical). Pour $x\gg h$, $t_r\to t_d$ par valeurs supérieures.


**q2.** Calculer l'angle critique $\theta_c$ de l'interface (1)-(2). Montrer que l'onde conique, qui descend à l'angle $\theta_c$,
glisse le long de l'interface à la vitesse $c_2$ et remonte à $\theta_c$, arrive au temps
$t_h(x)=\dfrac x{c_2}+\dfrac{2h\cos\theta_c}{c_1}$. Pour quelles distances existe-t-elle ?

> [!tip]- 💡 Coup de pouce
> Décomposez le trajet en deux tronçons obliques de longueur $h/\cos\theta_c$ (à $c_1$) et un tronçon horizontal de longueur $x-2h\tan\theta_c$ (à $c_2$). Simplifiez avec $\sin\theta_c=c_1/c_2$.


> [!success]- ✅ Correction
> $\theta_c=19{,}5^\circ$ ; $t_h=x/c_2+2h\cos\theta_c/c_1$ ; elle existe pour $x>x_{\min}=2h\tan\theta_c$.


> [!example]- 📝 Solution détaillée
> **Angle critique**
>
> $\sin\theta_c=c_1/c_2=1/3$, $\theta_c=19{,}5^\circ$ (donc $\cos\theta_c=0{,}943$, $\tan\theta_c=0{,}354$).
>
> **Temps de parcours**
>
> $$t_h=\underbrace{\frac{2h}{c_1\cos\theta_c}}_{\text{deux tronçons obliques}}+\underbrace{\frac{x-2h\tan\theta_c}{c_2}}_{\text{tronçon horizontal}}=\frac x{c_2}+\frac{2h}{c_1\cos\theta_c}\left(1-\frac{c_1}{c_2}\sin\theta_c\right).$$
> Avec $c_1/c_2=\sin\theta_c$ : $1-\sin^2\theta_c=\cos^2\theta_c$, d'où
> $$\boxed{t_h=\frac x{c_2}+\frac{2h\cos\theta_c}{c_1}}.$$
> L'ordonnée à l'origine est $t_i=2h\cos\theta_c/c_1$. Le trajet n'existe que si le tronçon horizontal est positif : $x\ge x_{\min}=2h\tan\theta_c$.


**q3.** Montrer que l'onde conique devient la première arrivée au-delà d'une distance de croisement
$x_c=2h\sqrt{\dfrac{c_2+c_1}{c_2-c_1}}$. Quelle condition faut-il sur $c_1$ et $c_2$ ?

> [!success]- ✅ Correction
> $x_c=2h\sqrt{(c_2+c_1)/(c_2-c_1)}$ ; il faut $c_2>c_1$.


> [!example]- 📝 Solution détaillée
> **Distance de croisement**
>
> $t_d=t_h\Leftrightarrow x\left(\dfrac1{c_1}-\dfrac1{c_2}\right)=\dfrac{2h\cos\theta_c}{c_1}\Leftrightarrow x\,\dfrac{c_2-c_1}{c_1c_2}=\dfrac{2h\sqrt{c_2^2-c_1^2}}{c_1c_2}$, soit
> $$x_c=2h\,\frac{\sqrt{c_2^2-c_1^2}}{c_2-c_1}=2h\sqrt{\frac{c_2+c_1}{c_2-c_1}}.$$
> Pour $x>x_c$ la pente $1/c_2$ plus faible permet à l'onde conique de passer devant l'onde directe. La condition est $c_2>c_1$ (sinon pas d'angle critique, donc pas d'onde conique).


**q4.** À partir du tableau de l'énoncé, déterminer graphiquement ou par calcul $c_1$, $c_2$, l'ordonnée à l'origine $t_i$,
la distance de croisement $x_c$ et l'épaisseur $h$. Vérifier la cohérence entre $h$ obtenu par $t_i$ et par $x_c$.

> [!tip]- 💡 Coup de pouce
> La pente de $t(x)$ pour les cinq premiers points est $1/c_1$. Pour les cinq derniers, elle est $1/c_2$ ; prolongez cette droite en $x=0$ pour avoir $t_i$.


> [!success]- ✅ Correction
> $c_1=1000$ m/s ; $c_2=3000$ m/s ; $t_i\approx37{,}7$ ms ; $x_c\approx57$ m ; $h\approx20$ m.


> [!example]- 📝 Solution détaillée
> **Lecture des deux droites**
>
> Pour $x\le50$ m, $t=x\times1{,}00$ ms/m : $c_1=1000$ m/s (onde directe). Pour $x\ge60$ m : entre $60$ et $120$ m, $\dfrac{77{,}7-57{,}7}{60}=0{,}333$ ms/m, donc $c_2=3000$ m/s (onde conique). Le prolongement en $x=0$ donne $t_i=77{,}7-120/3\approx37{,}7$ ms.
>
> **Distance de croisement et épaisseur**
>
> Les deux droites se coupent en $x_c$ tel que $x_c=x_c/3+37{,}7$, soit $x_c\approx56{,}6$ m (cohérent avec la cassure entre $50$ et $60$ m). Avec $t_i=2h\cos\theta_c/c_1$ :
> $$h=\frac{c_1t_i}{2\cos\theta_c}=\frac{1000\times37{,}7\times10^{-3}}{2\times0{,}943}\approx20{,}0~\text{m}.$$
> Avec $x_c$ : $h=\dfrac{x_c}{2}\sqrt{\dfrac{c_2-c_1}{c_2+c_1}}=\dfrac{56{,}6}{2}\sqrt{\dfrac{2000}{4000}}=28{,}3\times0{,}707=20{,}0$ m : les deux déterminations concordent. On a aussi $x_{\min}=2h\tan\theta_c=14$ m, bien inférieur à $x_c$ : l'onde conique existe donc déjà dans la zone d'arrivée de l'onde directe, mais est masquée par elle.


**q5.** Vérifier que l'onde réfléchie n'est pas la première arrivée à $x=60$ m. Calculer pour cette distance l'angle
d'incidence du rayon réfléchi et le coefficient de réflexion $|R|$. Calculer aussi $R$ en incidence normale
et commenter : pourquoi les réflexions « grand angle » sont-elles plus énergétiques ?

> [!tip]- 💡 Coup de pouce
> L'angle d'incidence du rayon réfléchi vérifie $\tan\theta_1=x/(2h)$. Appliquer le résultat de l'exercice 4 : $|R|=1$ si $\theta_1>\theta_c$.


> [!success]- ✅ Correction
> $t_r(60)=72{,}1$ ms $>57{,}7$ ms ; $\theta_1=56^\circ>\theta_c$ : $|R|=1$ ; $R(0)=0{,}60$.


> [!example]- 📝 Solution détaillée
> **Ordre des arrivées**
>
> $t_r(60)=\sqrt{60^2+40^2}/1000=72{,}1$ ms, supérieur à $t_h(60)=57{,}7$ ms (et à $t_d=60$ ms) : l'onde réfléchie est la dernière des trois.
>
> **Coefficient de réflexion en fonction de l'angle**
>
> Pour $x=60$ m, $\tan\theta_1=60/40=1{,}5$, $\theta_1=56{,}3^\circ>\theta_c=19{,}5^\circ$ : la réflexion est totale ($|R|=1$, avec déphasage). En incidence normale, $Z_1=1800\times1000=1{,}8\times10^6$ et $Z_2=2400\times3000=7{,}2\times10^6$ rayl : $R(0)=\dfrac{7{,}2-1{,}8}{7{,}2+1{,}8}=0{,}60$, soit seulement $36\ \%$ de l'énergie réfléchie. Au-delà de l'angle critique, $|R|=1$ : le signal réfléchi « grand angle » est beaucoup plus intense que celui à incidence quasi normale (c'est pourquoi on exploite la sismique « grand angle » pour imager les discontinuités profondes).


**q6.** Discuter les hypothèses du modèle : (a) que se passe-t-il si $c_2<c_1$ ? (b) à quelle condition sur la longueur d'onde
les rayons sont-ils une bonne description ? Estimer la fréquence minimale pour une impulsion sismique avec
$\lambda<h/3$. (c) Que change une interface inclinée ?

> [!success]- ✅ Correction
> (a) pas d'onde conique, couche cachée ; (b) $\lambda\ll h$, soit $f>150$ Hz pour $\lambda<h/3\approx6{,}7$ m ; (c) les vitesses apparentes dépendent du sens du tir.


> [!example]- 📝 Solution détaillée
> **Conditions de validité**
>
> (a) Si $c_2<c_1$, il n'y a pas d'angle critique donc pas d'onde conique : une couche lente sous une couche rapide est invisible à la réfraction (couche cachée) et on peut mal estimer les profondeurs.
>
> (b) Le raisonnement en rayons suppose $\lambda\ll h$. Avec $\lambda<h/3\approx6{,}7$ m dans la couche (1), $f=c_1/\lambda>1000/6{,}7\approx150$ Hz : les sources de sismique réfraction proche surface utilisent des fréquences de quelques dizaines à quelques centaines de Hz. En dessous, l'onde ne ``voit'' plus la couche comme une interface nette.
>
> (c) Si l'interface est inclinée d'un angle $\beta$, les vitesses apparentes de l'onde conique diffèrent selon le sens du tir ($c_2/\sin(\theta_c\pm\beta)$) : un tir direct et un tir inverse sont nécessaires pour séparer pente et vitesse (cf. aller plus loin).


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex4-incidence-oblique-lois-de-snell-descartes-angle-critique-reflexion-totale-et-onde-evanescente|Exercice 4 — Incidence oblique : lois de Snell-Descartes, angle critique, réflexion totale et onde évanescente]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex2-interface-entre-deux-milieux-notion-d-impedance-acoustique|Exercice 2 — Interface entre deux milieux, notion d'impédance acoustique]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex6-controle-ultrasonore-d-une-plaque-immergee-train-d-echos-epaisseur-attenuation-et-defaut-de-collage|Exercice 6 — Contrôle ultrasonore d'une plaque immergée : train d'échos, épaisseur, atténuation et défaut de collage]]

