---
title: "Exercice 6 — Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/index|⬅ Retour]] · [📄 Énoncé (td2_PhV212_enonce)](/pdfs/td2_PhV212_enonce.pdf) · [📄 Énoncé (td2_enonce)](/pdfs/td2_enonce.pdf)

### Exercice 6. Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle *(facultatif)*

Un ingénieur acousticien veut caractériser une mousse absorbante. Il place un échantillon à l'extrémité
$x=0$ d'un tube rigide cylindrique de rayon $a=2{,}0$ cm. Un haut-parleur, placé loin à gauche, envoie dans
le tube ($x<0$) une onde plane de fréquence $f=1000$ Hz. Dans l'air ($c=340~\text{m}\cdot\text{s}^{-1}$),
la surpression est la somme d'une onde incidente et d'une onde réfléchie par l'échantillon :
$$\tilde p_I=A\,e^{i(\omega t-kx)},\qquad\tilde p_R=R\,A\,e^{i(\omega t+kx)},\qquad R=|R|\,e^{i\varphi}\in\mathbb C,\quad A>0.$$
Un microphone-sonde mobile mesure l'amplitude $|\tilde p|$ en fonction de la distance $d=-x$ à l'échantillon.
On relève : $|\tilde p|_{\max}/|\tilde p|_{\min}=3$ et le premier minimum, le plus proche de l'échantillon,
est situé à $d_1=4{,}25$ cm.

**q1.** Montrer que $|\tilde p(x)|^2=A^2\big(1+|R|^2+2|R|\cos(2kx+\varphi)\big)$ et que le signal total se décompose
en une onde progressive et une onde stationnaire pure dont on précisera les amplitudes.

> [!tip]- 💡 Coup de pouce
> Écrivez $|a+b|^2=(a+b)(a+b)^{*}$. Pour la décomposition, écrivez $R=|R|e^{i\varphi}$ et séparez $1=(1-|R|)+|R|$.


**q2.** Définir le rapport d'ondes stationnaires $s=p_{\max}/p_{\min}$ et l'exprimer en fonction de
$|R|$. En déduire $|R|(s)$. Que valent $s$ pour $|R|=0$ et $|R|=1$ ?

> [!tip]- 💡 Coup de pouce
> Maximum et minimum du cosinus : $\pm1$, donc $|\tilde p|_{\max/\min}=A\sqrt{1+|R|^2\pm2|R|}$.


**q3.** Montrer que les minima de $|\tilde p|$ sont aux distances $d_m=\dfrac{\varphi+\pi}{2k}+m\dfrac\lambda2$.
En déduire $\varphi$ en fonction de $d_1$ et $k$.

> [!tip]- 💡 Coup de pouce
> Dans la formule de la question 1, remplacez $x$ par $-d$ ; le minimum est atteint quand le cosinus vaut $-1$.


**q4.** Application numérique : calculer $\lambda$, $|R|$, $\varphi$ et $R$. En déduire le coefficient
d'absorption $\alpha=1-|R|^2$ puis l'impédance de l'échantillon $Z_s=\tilde p(0)/\tilde v(0)$,
en fonction de $Z_0$. Cet échantillon se comporte-t-il comme une masse ou comme un ressort ?

> [!tip]- 💡 Coup de pouce
> $\tilde v(x)=(A/Z_0)\big(e^{-ikx}-Re^{ikx}\big)e^{i\omega t}$ (onde réfléchie : signe moins). Pour la fraction complexe, multipliez par le conjugué du dénominateur.


**q5.** Retrouver, avec ce formalisme, les cas limites : paroi rigide, extrémité ouverte idéale, matériau
parfaitement adapté. Pour chacun, donner $Z_s$, $R$, $s$ et la position du premier minimum.
Faire le lien avec les exercices 2 et 3.

**q6.** Pour mesurer $R$ sur toute une bande de fréquences, on utilise deux microphones fixes en $x_1$ et
$x_2$ ($x_1-x_2=\sigma>0$). On mesure la fonction de transfert complexe
$H=\tilde p(x_2)/\tilde p(x_1)$. Exprimer $R$ en fonction de $H$, $k$, $x_1$, $x_2$.
Pourquoi la méthode échoue-t-elle quand $k\sigma=\pi$ ? En déduire la fréquence maximale
d'utilisation pour $\sigma=5$ cm. Pourquoi le tube de rayon $a=2$ cm impose-t-il aussi une limite
haute (on admettra que la propagation est plane si $f<1{,}84\,c/(2\pi a)$) ?

> [!tip]- 💡 Coup de pouce
> $H$ est une fonction affine de $R$ : écrivez $H\,\tilde p(x_1)=\tilde p(x_2)$ et isolez $R$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex2-onde-stationnaire-tube-de-kundt-ouvert|Exercice 2 — Onde stationnaire, tube de Kundt ouvert]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex3-onde-stationnaire-tube-de-kundt-ferme-a-faire-a-la-maison|Exercice 3 — Onde stationnaire, tube de Kundt fermé (à faire à la maison)]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex5-energie-intensite-acoustique-et-niveau-sonore-de-l-oreille-humaine-a-l-onde-stationnaire|Exercice 5 — Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex8-transmission-a-travers-une-lame-adaptation-d-impedance-loi-de-masse-et-double-vitrage|Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex4-reflexion-et-transmission-d-une-onde-acoustique-a-une-interface-entre-deux-fluides|Exercice 4 — Réflexion et transmission d'une onde acoustique à une interface entre deux fluides]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex7-resonateur-de-helmholtz-la-bouteille-qui-chante|Exercice 7 — Résonateur de Helmholtz : la bouteille qui chante]]

