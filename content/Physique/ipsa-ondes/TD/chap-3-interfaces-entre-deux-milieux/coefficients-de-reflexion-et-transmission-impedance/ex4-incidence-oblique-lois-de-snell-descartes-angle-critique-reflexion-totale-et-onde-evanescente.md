---
title: "Exercice 4 — Incidence oblique : lois de Snell-Descartes, angle critique, réflexion totale et onde évanescente"
tags:
  - td
  - chap-3-interfaces-entre-deux-milieux
---

[[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/index|⬅ Retour]] · [📄 Énoncé (td3_PhV212_enonce)](/pdfs/td3_PhV212_enonce.pdf) · [📄 Énoncé (td3_enonce)](/pdfs/td3_enonce.pdf)

### Exercice 4. Incidence oblique : lois de Snell-Descartes, angle critique, réflexion totale et onde évanescente *(facultatif)*

Deux fluides parfaits semi-infinis sont séparés par le plan $x=0$ : le milieu (1) ($\rho_1,c_1,Z_1=\rho_1c_1$)
occupe $x<0$, le milieu (2) ($\rho_2,c_2,Z_2=\rho_2c_2$) occupe $x>0$. Une onde plane sinusoïdale de pulsation $\omega$
arrive du milieu (1) avec l'angle d'incidence $\theta_1$ par rapport à la normale $Ox$. Elle donne une onde réfléchie
(angle $\theta_1'$) et une onde transmise (angle $\theta_2$). En notation complexe ($e^{i\omega t}$), avec $\mathbf r=(x,y)$ :
$$p_I=A\,e^{i(\omega t-k_1x\cos\theta_1-k_1y\sin\theta_1)},\quad p_R=R\,A\,e^{i(\omega t+k_1x\cos\theta_1'-k_1y\sin\theta_1')},\quad p_T=T\,A\,e^{i(\omega t-k_2x\cos\theta_2-k_2y\sin\theta_2)},$$
avec $k_i=\omega/c_i$. À l'interface, la pression et la composante normale $v_x$ de la vitesse sont continues.
Pour une onde plane se propageant dans la direction $\hat{\mathbf u}$, on rappelle que $\mathbf v=(p/Z)\,\hat{\mathbf u}$.

Données : air ($\rho=1{,}2~\text{kg}\cdot\text{m}^{-3}$, $c=340~\text{m}\cdot\text{s}^{-1}$), eau
($\rho=1000~\text{kg}\cdot\text{m}^{-3}$, $c=1500~\text{m}\cdot\text{s}^{-1}$), sable saturé
($\rho=1900~\text{kg}\cdot\text{m}^{-3}$, $c=1700~\text{m}\cdot\text{s}^{-1}$), vase
($\rho=1400~\text{kg}\cdot\text{m}^{-3}$, $c=1450~\text{m}\cdot\text{s}^{-1}$).

**q1.** En écrivant la continuité de $p$ en $x=0$ pour tout $y$ et tout $t$, retrouver les lois de la réflexion
et de la réfraction de Snell-Descartes. Quelle grandeur physique est conservée à la traversée de l'interface ?

> [!tip]- 💡 Coup de pouce
> En $x=0$, les trois ondes s'écrivent $e^{i\omega t}e^{-ik_1y\sin\theta_1}$, $Re^{i\omega t}e^{-ik_1y\sin\theta_1'}$ et $Te^{i\omega t}e^{-ik_2y\sin\theta_2}$ : une somme d'exponentielles de $y$ ne peut être égale à une autre que si les dépendances en $y$ coïncident.


**q2.** Écrire la continuité de la pression et de la composante normale de la vitesse en $x=0$ et en déduire
$R(\theta_1)$ et $T(\theta_1)$. Montrer que tout se passe comme en incidence normale avec des impédances apparentes.
Vérifier le cas $\theta_1=0$.

> [!tip]- 💡 Coup de pouce
> $v_x=(p/Z)\cos\theta$ pour l'onde incidente et pour l'onde transmise, mais $v_x=-(p/Z)\cos\theta_1$ pour l'onde réfléchie (elle se propage vers $-x$).


**q3.** Le flux d'énergie normal à l'interface d'une onde plane est $I_x=\langle p\,v_x\rangle$. Établir
$R_E=|R|^2$ et $T_E=|T|^2\dfrac{Z_1\cos\theta_2}{Z_2\cos\theta_1}$ (quand $\theta_2$ est réel) et montrer que $R_E+T_E=1$.

> [!tip]- 💡 Coup de pouce
> Posez $a=Z_2\cos\theta_1$ et $b=Z_1\cos\theta_2$ ; alors $R=\dfrac{a-b}{a+b}$, $T=\dfrac{2a}{a+b}$.


**q4.** Existe-t-il un angle critique pour le passage air $\to$ eau ? eau $\to$ air ? eau $\to$ sable ? Calculer-le quand il existe.
Pour un son qui sort de l'eau, dans quel cône émerge-t-il dans l'air ? Quelle fraction de l'espace
(demi-sphère) de l'air est concernée pour l'entrée dans l'eau ?

> [!tip]- 💡 Coup de pouce
> $\sin\theta_2=(c_2/c_1)\sin\theta_1\leq1$ impose $\sin\theta_1\le c_1/c_2$ : il faut $c_2>c_1$. La fraction de demi-sphère contenue dans un cône d'angle $\theta_c$ est $1-\cos\theta_c$.


**q5.** Eau $\to$ sable, avec $\theta_1>\theta_c$. Montrer que $\cos\theta_2$ est imaginaire pur, que $|R|=1$, et exprimer
la phase $\varphi$ de $R$. Montrer que l'onde dans le sable est évanescente, calculer sa profondeur de pénétration
$\delta$ puis que sa puissance moyenne normale est nulle. Applications numériques pour $\theta_1=75^\circ$ et $f=1$ kHz.

> [!tip]- 💡 Coup de pouce
> Posez $n=c_2/c_1$ ; $\cos^2\theta_2=1-n^2\sin^2\theta_1<0$. On choisit $\cos\theta_2=-i\beta$ ($\beta>0$) pour que l'onde décroisse avec $x$.


**q6.** Interface air $\to$ eau. Calculer $T_E$ en incidence normale puis pour $\theta_1=10^\circ$. Commenter
(comparer à l'exercice 2 du TD3 et au cône de la question 4).

> [!tip]- 💡 Coup de pouce
> $Z_1=1{,}2\times340=408$ rayl, $Z_2=1{,}5\times10^6$ rayl ; $T_E=4ab/(a+b)^2$ avec $a=Z_2\cos\theta_1$ et $b=Z_1\cos\theta_2$.


**q7.** *Angle d'intromission.* Montrer que $R=0$ pour un angle $\theta_B$ tel que
$\sin^2\theta_B=\dfrac{Z_2^2-Z_1^2}{Z_2^2-n^2Z_1^2}$ ($n=c_2/c_1$). Pour quelles combinaisons
$(\rho_2/\rho_1,\ c_2/c_1)$ cet angle existe-t-il ? L'angle existe-t-il pour l'interface air $\to$ eau ? Calculer $\theta_B$ pour
l'interface eau $\to$ vase et vérifier numériquement que $R=0$.

> [!tip]- 💡 Coup de pouce
> $R=0\Leftrightarrow Z_2\cos\theta_1=Z_1\cos\theta_2$. Élevez au carré et utilisez $\cos^2\theta_2=1-n^2\sin^2\theta_1$. Notez que $Z_2^2-n^2Z_1^2=c_2^2(\rho_2^2-\rho_1^2)$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex2-interface-entre-deux-milieux-notion-d-impedance-acoustique|Exercice 2 — Interface entre deux milieux, notion d'impédance acoustique]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex5-sismique-refraction-ondes-coniques-et-epaisseur-d-une-couche|Exercice 5 — Sismique réfraction : ondes coniques et épaisseur d'une couche]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex6-controle-ultrasonore-d-une-plaque-immergee-train-d-echos-epaisseur-attenuation-et-defaut-de-collage|Exercice 6 — Contrôle ultrasonore d'une plaque immergée : train d'échos, épaisseur, atténuation et défaut de collage]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex3-perle-sur-une-corde-jonction-massive-filtre-passe-bas-puis-passe-bande|Exercice 3 — Perle sur une corde : jonction massive, filtre passe-bas puis passe-bande]]

