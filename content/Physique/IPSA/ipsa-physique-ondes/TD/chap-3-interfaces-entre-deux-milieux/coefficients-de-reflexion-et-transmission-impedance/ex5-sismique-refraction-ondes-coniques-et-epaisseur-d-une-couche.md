---
title: "Exercice 5 — Sismique réfraction : ondes coniques et épaisseur d'une couche"
tags:
  - td
  - chap-3-interfaces-entre-deux-milieux
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/index|⬅ Retour]] · <a href="/pdfs/td3_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_PhV212_enonce)</a> · <a href="/pdfs/td3_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_enonce)</a> · <a href="/pdfs/td3_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td3_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td3_PhV212_corrige)</a> · <a href="/pdfs/td3_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td3_corrige)</a>

### Exercice 5. Sismique réfraction : ondes coniques et épaisseur d'une couche *(facultatif)*

*Difficulté ●●●●○ · ⏱ 50 min · Type : Application / Problème d'ingénieur*

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

> [!question]+ 🎣 Accroche
> **Comment mesurer une couche enfouie sans creuser ?**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *On frappe le sol avec une masse et on enregistre les temps d'arrivée aux capteurs. Les ondes qui vont tout droit à la surface sont-elles toujours les premières ? Peut-on imaginer un trajet plus rapide qui descend dans le sol, parcourt un bout de chemin à grande vitesse et remonte ? **Quel lien avec l'angle critique et la réflexion totale ?***
>
> **Idée clé : au-delà de la distance de croisement, l'onde la plus rapide est celle qui plonge à l'angle critique, glisse le long du substratum rapide ($c_2$) et remonte.** Son temps d'arrivée est une droite de pente $1/c_2$ :
> $$t_h=\frac x{c_2}+\frac{2h\cos\theta_c}{c_1},\qquad x_c=2h\sqrt{\frac{c_2+c_1}{c_2-c_1}}.$$
> La cassure de pente du graphe $t(x)$ donne la profondeur $h$.


> [!abstract]+ 📚 Prérequis
> **Lois de Snell-Descartes et angle critique (exercice 4)**
>
> Savoir que $\sin\theta_1/c_1=\sin\theta_2/c_2$, qu'il existe un angle critique $\theta_c=\arcsin(c_1/c_2)$ quand $c_2>c_1$, et qu'au-delà de $\theta_c$ la réflexion est totale ($|R|=1$) avec une onde évanescente le long de l'interface.
>
> **Coefficient de réflexion en incidence normale**
>
> $R=\dfrac{Z_2-Z_1}{Z_1+Z_2}$ pour la pression, avec $Z=\rho c$.
>
> **Géométrie élémentaire**
>
> Trigonométrie du triangle rectangle, longueur d'un trajet oblique de $h$ de hauteur à l'angle $\theta$ : $h/\cos\theta$, projection horizontale $h\tan\theta$.


> [!info]+ 🎯 Objectifs
> **Utiliser Snell-Descartes pour résoudre un problème d'ingénieur**
>
> Savoir identifier les trois types de trajets (direct, réfléchi, conique), calculer leurs temps de parcours, établir le temps d'arrivée de l'onde conique par construction géométrique, interpréter un graphe de temps d'arrivée (« dromochronique ») pour en déduire $c_1$, $c_2$ et $h$, et discuter les hypothèses (couche plus lente que le substratum, longueurs d'onde, ondes S ignorées).


> [!note]+ 📖 Point de cours
> **Onde conique (head wave) et principe de Fermat**
>
> Quand $\theta_1=\theta_c$, le rayon transmis rase l'interface ($\theta_2=90^\circ$). Il existe alors un trajet particulier où l'énergie se propage le long de l'interface à la vitesse $c_2$ du milieu rapide, en rayonnant continuellement vers le milieu (1) sous le même angle critique (principe de Huygens). Le temps total de ce trajet est inférieur à celui de l'onde directe à grande distance si $c_2>c_1$, ce qui en fait la première arrivée au-delà d'une distance de croisement $x_c$. L'onde conique est la manifestation macroscopique de l'onde évanescente de l'exercice 4 (question 5) : elle est de faible amplitude, mais elle est première.


> [!note]- 🧮 Outils mathématiques
> **Construction géométrique d'un trajet brisé**
>
> Pour un trajet qui descend de $h$ à l'angle $\theta$, la longueur est $h/\cos\theta$ et la projection horizontale $h\tan\theta$ : deux descentes/remontées couvrent $2h\tan\theta$ horizontalement et $2h/\cos\theta$ de trajet.
>
> **Simplification trigonométrique avec $\sin\theta_c=c_1/c_2$**
>
> $\dfrac1{c_1}-\dfrac{c_1}{c_2^2}=\dfrac1{c_1}\left(1-\sin^2\theta_c\right)=\dfrac{\cos^2\theta_c}{c_1}$ : cette identité fait disparaître $\tan\theta_c$ et donne la forme simple de $t_h$.
>
> **Résolution d'équation du premier degré (distance de croisement)**
>
> $x\left(\dfrac1{c_1}-\dfrac1{c_2}\right)=\dfrac{2h\cos\theta_c}{c_1}$ avec $\cos\theta_c=\sqrt{c_2^2-c_1^2}/c_2$ : $x_c=2h\sqrt{\dfrac{c_2+c_1}{c_2-c_1}}$.
>
> **Régression linéaire à la main**
>
> Pente $=\Delta t/\Delta x$ entre deux points éloignés ; ordonnée à l'origine en prolongeant la droite jusqu'à $x=0$. Précision à estimer : un écart de $0{,}1$ ms sur $\Delta t\sim20$ ms donne $0{,}5\ \%$ sur $c_2$.
>
> **Hyperbole de réflexion**
>
> $t_r^2=\dfrac{x^2}{c_1^2}+t_0^2$ avec $t_0=\dfrac{2h}{c_1}$ : en traçant $t^2$ en fonction de $x^2$, on obtient une droite de pente $1/c_1^2$ et d'ordonnée $t_0^2$.
>
> **Arcsin et angles remarquables**
>
> $\sin\theta_c=1/3$ donne $\theta_c=19{,}5^\circ$, $\cos\theta_c=2\sqrt2/3=0{,}943$, $\tan\theta_c=1/(2\sqrt2)=0{,}354$.


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


> [!note]- 🔗 Liens avec d'autres disciplines
> **Géophysique appliquée**
>
> La sismique réfraction est utilisée en génie civil (profondeur du toit du rocher avant une fondation), en hydrogéologie (niveau de la nappe), en prospection pétrolière (au tout début de l'exploration). Elle est complétée par la sismique réflexion.
>
> **Sismologie et structure de la Terre**
>
> Mohorovičić a découvert en 1909 la discontinuité entre la croûte et le manteau par l'observation d'une onde conique ($P_n$) qui devance l'onde directe au-delà d'une distance de croisement de l'ordre de $100$ à $200$ km : exactement le phénomène de cet exercice avec $c_2\approx8$ km/s sous une croûte à $c_1\approx6$ km/s.
>
> **Optique**
>
> Les ondes coniques ont un équivalent optique : l'onde de tunnel frustrée, et, pour les ondes radio, les ondes de surface le long du sol. Le principe de Fermat (minimisation du temps de trajet) explique le trajet.
>
> **Contrôle non destructif**
>
> Les ondes ``longitudinales rasantes'' (Lcr) utilisées pour mesurer les contraintes dans les pièces métalliques sont des ondes coniques : le capteur est incliné à l'angle critique de l'interface résine-acier pour générer un rayon rasant.
>
> **Mathématiques : problèmes de minimisation**
>
> Le trajet de l'onde conique est celui qui minimise le temps parmi tous les trajets de la source à la surface passant par l'interface : c'est un problème de calcul variationnel (principe de Fermat) qui conduit à Snell-Descartes.


> [!question]- 🔭 Aller plus loin — Master : Interface inclinée et tir inversé
> Si l'interface est inclinée de l'angle $\beta$, les vitesses apparentes obtenues en tirant dans les deux sens sont $c_2/\sin(\theta_c\pm\beta)$ : on retrouve $\beta$ et $c_2$ par un tir direct et un tir inverse. On pourra établir ce résultat par la méthode de l'exercice (construction géométrique) et en déduire les épaisseurs aux deux extrémités.


> [!question]- 🔭 Aller plus loin — Master : Plusieurs couches et gradient de vitesse
> Pour $N$ couches de vitesses croissantes, la dromochronique est une succession de segments de pentes $1/c_i$ et d'ordonnées à l'origine qui se calculent de proche en proche. Quand la vitesse croît continûment avec la profondeur (cas de la croûte terrestre), les rayons sont courbes (ondes plongeantes) ; c'est l'origine des zones d'ombre et de la détection du noyau.


> [!question]- 🔭 Aller plus loin — Doctorat : Amplitude de l'onde conique
> L'onde conique décroît en $x^{-2}$ (plus vite que l'onde directe en $x^{-1}$ en 2D) et sa forme est la dérivée de la source : on pourra l'établir par la théorie de Cagniard-de Hoop. En pratique, les capteurs doivent détecter un signal très faible après l'arrivée de l'onde directe.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex4-incidence-oblique-lois-de-snell-descartes-angle-critique-reflexion-totale-et-onde-evanescente|Exercice 4 — Incidence oblique : lois de Snell-Descartes, angle critique, réflexion totale et onde évanescente]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex2-interface-entre-deux-milieux-notion-d-impedance-acoustique|Exercice 2 — Interface entre deux milieux, notion d'impédance acoustique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex6-controle-ultrasonore-d-une-plaque-immergee-train-d-echos-epaisseur-attenuation-et-defaut-de-collage|Exercice 6 — Contrôle ultrasonore d'une plaque immergée : train d'échos, épaisseur, atténuation et défaut de collage]]

