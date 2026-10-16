---
title: "Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/index|⬅ Retour]] · <a href="/pdfs/td2_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_PhV212_enonce)</a> · <a href="/pdfs/td2_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_enonce)</a> · <a href="/pdfs/td2_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_aides)</a> · <a href="/pdfs/td2_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_exs_maison_aide)</a>

### Exercice 8. Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage *(facultatif)*

On étudie la transmission d'une onde plane, en incidence normale, à travers une *lame* d'épaisseur $e$
insérée entre deux fluides semi-infinis. Le fluide (1), d'impédance $Z_1=\rho_1c_1$, occupe $x<0$ ; la lame
(2), de masse volumique $\rho_2$, de célérité $c_2$, d'impédance $Z_2=\rho_2c_2$ et de nombre d'onde
$k_2=\omega/c_2$, occupe $0<x<e$ ; le fluide (3), d'impédance $Z_3$, occupe $x>e$. On pose $u=k_2e$.
Il n'y a pas d'onde incidente venant de la droite. En notation complexe $e^{i\omega t}$ :
$$\tilde p_1=A\big(e^{-ik_1x}+Re^{ik_1x}\big),\quad\tilde p_2=Be^{-ik_2x}+Ce^{ik_2x},\quad\tilde p_3=D\,e^{-ik_3(x-e)}.$$
Les vitesses particulaires s'en déduisent par $\tilde v=\pm\tilde p/Z$ selon le sens de propagation ($+$ pour $x$
croissant). On note $R_I=|R|^2$ et $T_I$ les coefficients énergétiques ($R_I+T_I=1$, milieux non absorbants).

**q1.** Écrire les vitesses particulaires dans chaque région, puis les quatre équations de continuité de
$\tilde p$ et $\tilde v$ en $x=0$ et $x=e$. Pourquoi $\tilde p_3$ ne comporte-t-il qu'une onde progressive ?

> [!tip]- 💡 Coup de pouce
> Une onde se propageant vers les $x$ décroissants a $\tilde v=-\tilde p/Z$. En $x=e$, $e^{-ik_3(x-e)}=1$.


**q2.** Montrer que l'impédance ramenée $Z_{\mathrm{in}}=\tilde p(0)/\tilde v(0)$ vue dans la lame en $x=0^+$ vaut
$Z_{\mathrm{in}}=Z_2\dfrac{Z_3\cos u+iZ_2\sin u}{Z_2\cos u+iZ_3\sin u}$. En déduire $R$ en fonction de $Z_{\mathrm{in}}$ et $Z_1$.

> [!tip]- 💡 Coup de pouce
> En $x=e$, $\tilde p/\tilde v=Z_3$ : cela donne le rapport $C/B$. Reportez-le dans $\tilde p/\tilde v$ en $x=0$ et multipliez numérateur et dénominateur par $e^{iu}$.


**q3.** Calculer $Z_{\mathrm{in}}$ pour une lame demi-onde ($e=\lambda_2/2$) puis quart d'onde ($e=\lambda_2/4$).
Que peut-on en conclure sur le rôle de la lame quand $Z_1=Z_3$ dans le premier cas ?

**q4.** Démontrer que $T_I=\dfrac{4Z_1Z_3}{(Z_1+Z_3)^2\cos^2u+\left(Z_2+Z_1Z_3/Z_2\right)^2\sin^2u}$.
En déduire la condition d'annulation de la réflexion et la valeur de $T_I$ dans ce cas.

> [!tip]- 💡 Coup de pouce
> Mettez $R=(Z_{\mathrm{in}}-Z_1)/(Z_{\mathrm{in}}+Z_1)$ sous la forme $(a+ib)/(c+id)$ avec $a,b,c,d$ réels, puis calculez $1-|R|^2$.


**q5.** Sonde échographique : céramique ($Z_1=30$ MRayl) vers tissu ($Z_3=1{,}5$ MRayl) à $f_0=3$ MHz. Calculer $T_I$
sans lame. On insère une couche d'adaptation de célérité $c_2=2700$ m/s : quelle impédance $Z_2$,
quelle épaisseur $e$, quelle valeur de $T_I$ ? Calculer $T_I$ à $0{,}8f_0$ et $1{,}2f_0$.
Pourquoi ne gagne-t-on pas «~un facteur 5~» sur le signal aller-retour mais davantage ?

> [!tip]- 💡 Coup de pouce
> $1~\text{MRayl}=10^6~\text{kg}\cdot\text{m}^{-2}\cdot\text{s}^{-1}$. À la fréquence $f=\beta f_0$, $u=\beta\pi/2$.


**q6.** Loi de masse. Une paroi mince (épaisseur $e$, masse volumique $\rho_2$, impédance $Z_2\gg Z_0$) sépare deux
zones d'air ($Z_1=Z_3=Z_0$). En supposant $u\ll1$, montrer que $T_I\approx\left[1+\left(\dfrac{\omega m_s}{2Z_0}\right)^2\right]^{-1}$
avec $m_s=\rho_2e$. Calculer la perte par transmission $TL=10\log_{10}(1/T_I)$ pour une vitre de $4$ mm
($\rho_2=2500~\text{kg}\cdot\text{m}^{-3}$, $c_2=5000~\text{m}\cdot\text{s}^{-1}$) à $1$ kHz. Quel est l'effet d'un doublement de la fréquence ou de la masse ?

> [!tip]- 💡 Coup de pouce
> Pour $u\ll1$, $\cos u\approx1$, $\sin u\approx u$, et $Z_2u=\rho_2c_2\omega e/c_2=\omega m_s$.


**q7.** Double paroi. Deux plaques de masses surfaciques $m_1$ et $m_2$ sont séparées par une lame d'air d'épaisseur
$d\ll\lambda$. L'air se comporte comme un ressort de raideur surfacique $K$ (isentropique).


1. Montrer que $K=\rho_0c^2/d$.
2. Écrire les équations du mouvement des deux plaques ; en déduire la fréquence de résonance masse-ressort-masse $f_{mam}$.
3. Application : deux vitres de $4$ mm ($m_1=m_2=10~\text{kg}\cdot\text{m}^{-2}$), $d=12$ mm. Commenter l'intérêt et la limite du double vitrage.

> [!tip]- 💡 Coup de pouce
> Pour des déplacements $\xi_1$ et $\xi_2$, l'épaisseur de la lame d'air varie de $\xi_2-\xi_1$. Utilisez $p=-\Delta V/(\chi_SV)$ comme dans l'exercice 7.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex4-reflexion-et-transmission-d-une-onde-acoustique-a-une-interface-entre-deux-fluides|Exercice 4 — Réflexion et transmission d'une onde acoustique à une interface entre deux fluides]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex5-energie-intensite-acoustique-et-niveau-sonore-de-l-oreille-humaine-a-l-onde-stationnaire|Exercice 5 — Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex6-tube-d-impedance-mesurer-l-absorption-d-un-materiau-avec-une-onde-stationnaire-partielle|Exercice 6 — Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex7-resonateur-de-helmholtz-la-bouteille-qui-chante|Exercice 7 — Résonateur de Helmholtz : la bouteille qui chante]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex2-onde-stationnaire-tube-de-kundt-ouvert|Exercice 2 — Onde stationnaire, tube de Kundt ouvert]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex3-onde-stationnaire-tube-de-kundt-ferme-a-faire-a-la-maison|Exercice 3 — Onde stationnaire, tube de Kundt fermé (à faire à la maison)]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex1-celerite-d-une-onde-acoustique-dans-un-fluide-parfait|Exercice 1 — Célérité d'une onde acoustique dans un fluide parfait]]

