---
title: "Exercice 3 — Perle sur une corde : jonction massive, filtre passe-bas puis passe-bande"
tags:
  - td
  - chap-3-interfaces-entre-deux-milieux
---

[[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/index|⬅ Retour]] · <a href="/pdfs/td3_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_PhV212_enonce)</a> · <a href="/pdfs/td3_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_enonce)</a> · <a href="/pdfs/td3_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 3. Perle sur une corde : jonction massive, filtre passe-bas puis passe-bande *(facultatif)*

Deux cordes tendues horizontalement avec la même tension $F$ sont reliées en $O$ ($x=0$) : la corde (1),
de masse linéique $\mu_1$, occupe $x<0$ ; la corde (2), de masse linéique $\mu_2$, occupe $x>0$. On note
$Z_i=\sqrt{F\mu_i}$ leurs impédances mécaniques. Contrairement à l'exercice 1, on fixe en $O$ une
*perle* ponctuelle de masse $M$, qui ne peut se déplacer que transversalement (pesanteur négligée).

**Convention de cet exercice** (différente de l'exercice 1) : l'onde incidente se propage vers les $x$
*croissants*. En notation complexe $e^{i\omega t}$, les déplacements sont
$$y_1(x,t)=A\big(e^{-ik_1x}+r\,e^{ik_1x}\big)e^{i\omega t}\ (x<0),\qquad y_2(x,t)=t\,A\,e^{-ik_2x}e^{i\omega t}\ (x>0),$$
avec $k_i=\omega\sqrt{\mu_i/F}$, de sorte que $r$ et $t$ sont les coefficients de réflexion et de transmission
en amplitude de *déplacement*.

Données numériques (cordes identiques, parties numériques) : $F=100$ N, $\mu_1=\mu_2=4{,}0~\text{g}\cdot\text{m}^{-1}$,
$M=2{,}0$ g.

**q1.** Écrire la condition de continuité sur $y$ en $x=0$ et l'équation du mouvement de la perle de masse $M$.
Justifier le signe des deux forces de tension exercées sur la perle.

> [!tip]- 💡 Coup de pouce
> Dessinez la perle avec la corde (1) à gauche et la corde (2) à droite ; chaque corde tire la perle le long de sa propre direction, avec une composante verticale $\pm F\sin\theta\approx\pm F\,\partial_xy$.


**q2.** En déduire $r$ et $t$ en fonction de $Z_1$, $Z_2$, $M$ et $\omega$.
Vérifier qu'on retrouve l'exercice 1 pour $M=0$.

> [!tip]- 💡 Coup de pouce
> Utilisez $1+r=t$, puis $F\,k_i=\omega Z_i$ pour remplacer les nombres d'onde par des impédances.


**q3.** Montrer que la perle se comporte comme une impédance $Z_M=iM\omega$ placée en série avec la corde (2).
Quel est l'analogue électrique ? Pourquoi les nombres $r$ et $t$ sont-ils maintenant complexes ?

> [!tip]- 💡 Coup de pouce
> Comparez avec $r=(Z_1-Z_2')/(Z_1+Z_2')$ en posant $Z_2'=Z_2+iM\omega$.


**q4.** La puissance moyenne transportée par une onde progressive est $\langle\mathcal P\rangle=\tfrac12Z\omega^2|A|^2$.
Établir les coefficients énergétiques $R_E=|r|^2$ et $T_E=(Z_2/Z_1)|t|^2$ et montrer que $R_E+T_E=1$.

**q5.** Cordes identiques ($Z_1=Z_2=Z$). Calculer $Z$, montrer que $T_E=\big[1+(M\omega/2Z)^2\big]^{-1}$,
identifier le type de filtre et sa fréquence de coupure à $-3$ dB. Calculer $T_E$ à $25$, $100$ et $400$ Hz
et l'atténuation à haute fréquence en dB par octave.

> [!tip]- 💡 Coup de pouce
> $Z=\sqrt{F\mu}$ avec $\mu$ en kg/m. La coupure est atteinte quand $T_E=1/2$.


**q6.** Régime transitoire. Montrer que, pour une impulsion dont le spectre est contenu dans $\omega\ll\omega_c$, l'onde
transmise est l'onde incidente retardée d'un temps $\tau=M/(2Z)$ et que l'onde réfléchie vaut
$y_r(0,t)\approx-\tau\,\partial_ty_i(0,t)$. Calculer $\tau$ et l'amplitude maximale de l'écho pour une impulsion
gaussienne $y_i(0,t)=Ae^{-t^2/2\sigma^2}$ avec $\sigma=20$ ms. Quelle est l'allure de l'écho ?

> [!tip]- 💡 Coup de pouce
> Développez $t(\omega)=1/(1+i\omega\tau)$ et $r(\omega)=-i\omega\tau/(1+i\omega\tau)$ au premier ordre en $\omega\tau$, puis revenez dans le domaine temporel ($i\omega\leftrightarrow\partial_t$).


**q7.** La perle est maintenant reliée à un support fixe par un ressort de raideur $K$ (rappel transversal $-Ky(0,t)$).
Montrer que $r=\dfrac{Z_1-Z_2-iX}{Z_1+Z_2+iX}$ avec $X=M\omega-K/\omega$. Pour des cordes identiques, à quelle
fréquence la transmission est-elle totale ? Calculer $K$ pour $f_0=250$ Hz, la largeur à mi-puissance
et le facteur de qualité de ce passe-bande.

> [!tip]- 💡 Coup de pouce
> L'équation de la perle devient $M\ddot y=F(\partial_xy_2-\partial_xy_1)-Ky$. Comparez à la question 2 en remplaçant $M\omega^2$ par $M\omega^2-K$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex1-corde-non-homogene-jonction-entre-deux-cordes|Exercice 1 — Corde non homogène, jonction entre deux cordes]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex2-interface-entre-deux-milieux-notion-d-impedance-acoustique|Exercice 2 — Interface entre deux milieux, notion d'impédance acoustique]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex4-incidence-oblique-lois-de-snell-descartes-angle-critique-reflexion-totale-et-onde-evanescente|Exercice 4 — Incidence oblique : lois de Snell-Descartes, angle critique, réflexion totale et onde évanescente]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex6-controle-ultrasonore-d-une-plaque-immergee-train-d-echos-epaisseur-attenuation-et-defaut-de-collage|Exercice 6 — Contrôle ultrasonore d'une plaque immergée : train d'échos, épaisseur, atténuation et défaut de collage]]

