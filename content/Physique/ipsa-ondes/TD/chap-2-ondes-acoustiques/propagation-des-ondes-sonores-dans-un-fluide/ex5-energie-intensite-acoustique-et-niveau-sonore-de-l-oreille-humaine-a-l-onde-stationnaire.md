---
title: "Exercice 5 — Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/index|⬅ Retour]] · [📄 Énoncé (td2_PhV212_enonce)](/pdfs/td2_PhV212_enonce.pdf) · [📄 Énoncé (td2_enonce)](/pdfs/td2_enonce.pdf)

### Exercice 5. Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire *(facultatif)*

L'air est modélisé comme un fluide parfait, de masse volumique au repos
$\rho_0=1{,}2~\text{kg}\cdot\text{m}^{-3}$, de célérité $c=340~\text{m}\cdot\text{s}^{-1}$
(impédance $Z=\rho_0c=408~\text{kg}\cdot\text{m}^{-2}\cdot\text{s}^{-1}$) et de pression moyenne
$P_0=10^5$ Pa. On note $\chi=1/(\rho_0c^2)$ son coefficient de compressibilité isentropique.

On rappelle les équations de l'acoustique linéaire à une dimension :
$$\rho_0\frac{\partial v}{\partial t}=-\frac{\partial p}{\partial x},\qquad \frac{\partial\rho'}{\partial t}+\rho_0\frac{\partial v}{\partial x}=0,\qquad \rho'=\rho_0\chi\,p.$$

L'*intensité acoustique* est la moyenne temporelle de la puissance transportée par unité de surface, $I=\langle p\,v\rangle$. Le *niveau sonore* est $L=10\log_{10}(I/I_0)$ avec $I_0=10^{-12}~\text{W}\cdot\text{m}^{-2}$ (seuil d'audition à 1 kHz), exprimé en décibels (dB).

**q1.** À partir des équations linéarisées de l'énoncé, établir la loi de conservation
$\dfrac{\partial e}{\partial t}+\dfrac{\partial \Pi}{\partial x}=0$ avec
$e=\tfrac12\rho_0v^2+\tfrac12\chi p^2$ et $\Pi=pv$. Interpréter chaque terme.

> [!tip]- 💡 Coup de pouce
> Multipliez l'équation d'Euler par $v$ et la conservation de la masse (après élimination de $\rho'$) par $p$, puis additionnez.


**q2.** Pour une onde plane progressive harmonique $p=p_0\cos(\omega t-kx)$ se propageant vers $+x$, montrer que les
énergies cinétique et potentielle volumiques sont égales à chaque instant, puis que
$\langle I\rangle=\dfrac{p_0^2}{2Z}=\dfrac{p_{\mathrm{eff}}^2}{Z}=c\,\langle e\rangle$.

> [!tip]- 💡 Coup de pouce
> Utilisez $v=p/Z$ et $\chi=1/(\rho_0c^2)$ ; remarquez que $\rho_0/Z^2=\chi$.


**q3.** Vérifier que la pression de référence $p_{\mathrm{ref}}=2\times10^{-5}$ Pa (valeur efficace) correspond bien à
$I_0$. Pour un son pur de $1$ kHz au seuil d'audition ($0$ dB), calculer les amplitudes
de pression $p_0$, de vitesse $v_0$ et de déplacement $\xi_0$ des particules de fluide.
Comparer $\xi_0$ à la taille d'un atome ($\sim10^{-10}$ m).

> [!tip]- 💡 Coup de pouce
> $\xi_0=v_0/\omega$ pour une grandeur harmonique. Attention : $p_{\mathrm{ref}}$ est une valeur efficace.


**q4.** Même question pour le seuil de douleur, $120$ dB. Justifier que l'approximation acoustique
(linéarisation) reste valable même à ce niveau.

> [!tip]- 💡 Coup de pouce
> Calculez les rapports adimensionnés $p_0/P_0$ et $v_0/c$ du point cours d'ouverture de l'exercice 1.


**q5.** Une personne qui parle normalement est entendue à $60$ dB à $1$ m. On la modélise comme une source
ponctuelle isotrope rayonnant une puissance acoustique $\mathcal P$ en champ libre
(onde sphérique : $I(r)=\mathcal P/(4\pi r^2)$). Calculer $\mathcal P$. À quelle distance
le niveau est-il de $40$ dB ? Combien de personnes faut-il pour émettre $1$ W acoustique ?

> [!tip]- 💡 Coup de pouce
> La puissance se conserve à travers toute sphère centrée sur la source ; passez par $I(1~\text{m})$ puis exprimez $L(r)-L(r_0)$.


**q6.** Deux sources produisent chacune $70$ dB au point d'écoute. Quel est le niveau total si :
(a) elles sont incohérentes ; (b) elles émettent le même signal, en phase en ce point ;
(c) elles sont en opposition de phase ? Que devient (a) pour $N=100$ sources identiques ?
Calculer enfin $70$ dB $+$ $60$ dB (incohérentes) et commenter.

**q7.** On reprend l'onde stationnaire du tube ouvert-ouvert de l'exercice 2, de section $S$, au mode propre $n$
($kL=n\pi$) : avec $x'=L-x$ et $\varphi=\omega t-kL$,
$\Psi=2A_I\cos(kx')\cos\varphi$ et $p=-2A_I\rho_0c\,\omega\sin(kx')\cos\varphi$ ($A_I$ réel).


1. Calculer $v$, puis le flux d'énergie instantané $\Pi=pv$. Montrer que $\langle\Pi\rangle=0$.
2. Calculer les densités d'énergie cinétique $e_c$ et potentielle $e_p$, puis leurs moyennes temporelles. Où chacune est-elle maximale ?
3. Calculer l'énergie totale $E(t)$ contenue dans le tube. Commenter.

> [!tip]- 💡 Coup de pouce
> Utilisez $\sin2a=2\sin a\cos a$. Pour la dernière question, $\int_0^L\cos^2(k(L-x))\,\mathrm dx=\int_0^L\sin^2(k(L-x))\,\mathrm dx=L/2$ lorsque $kL=n\pi$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex4-reflexion-et-transmission-d-une-onde-acoustique-a-une-interface-entre-deux-fluides|Exercice 4 — Réflexion et transmission d'une onde acoustique à une interface entre deux fluides]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex6-tube-d-impedance-mesurer-l-absorption-d-un-materiau-avec-une-onde-stationnaire-partielle|Exercice 6 — Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex7-resonateur-de-helmholtz-la-bouteille-qui-chante|Exercice 7 — Résonateur de Helmholtz : la bouteille qui chante]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex8-transmission-a-travers-une-lame-adaptation-d-impedance-loi-de-masse-et-double-vitrage|Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex2-onde-stationnaire-tube-de-kundt-ouvert|Exercice 2 — Onde stationnaire, tube de Kundt ouvert]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex3-onde-stationnaire-tube-de-kundt-ferme-a-faire-a-la-maison|Exercice 3 — Onde stationnaire, tube de Kundt fermé (à faire à la maison)]]

