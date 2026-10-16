---
title: "Exercice 6 — Contrôle ultrasonore d'une plaque immergée : train d'échos, épaisseur, atténuation et défaut de collage"
tags:
  - td
  - chap-3-interfaces-entre-deux-milieux
---

[[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/index|⬅ Retour]] · <a href="/pdfs/td3_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_PhV212_enonce)</a> · <a href="/pdfs/td3_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_enonce)</a> · <a href="/pdfs/td3_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 6. Contrôle ultrasonore d'une plaque immergée : train d'échos, épaisseur, atténuation et défaut de collage *(facultatif)*

Pour contrôler une plaque d'aluminium d'épaisseur $e$ inconnue, on l'immerge dans l'eau et on envoie, sous
incidence normale, une impulsion ultrasonore brève (fréquence centrale $5$ MHz, durée $\simeq0{,}4~\mu$s) à l'aide d'une
sonde émettrice-réceptrice placée dans l'eau. La face arrière de la plaque est en contact avec l'air.
On enregistre sur la sonde un train d'échos notés $E_0$, $E_1$, $E_2,\dots$ : $E_0$ est l'écho de la face avant, $E_n$
($n\ge1$) celui qui a effectué $n$ allers-retours dans la plaque. On note $r_{ij}$ et $t_{ij}$ les coefficients de réflexion
et de transmission en *amplitude de pression* pour une onde allant du milieu $i$ au milieu $j$ :
$r_{ij}=\dfrac{Z_j-Z_i}{Z_i+Z_j}$, $t_{ij}=1+r_{ij}$.

Données : eau ($\rho_w=1000~\text{kg}\cdot\text{m}^{-3}$, $c_w=1500~\text{m}\cdot\text{s}^{-1}$), aluminium
($\rho_A=2700~\text{kg}\cdot\text{m}^{-3}$, $c_A=5110~\text{m}\cdot\text{s}^{-1}$), air ($Z_{\mathrm{air}}=442$ rayl).
On néglige l'atténuation sauf à la question 5, et on admet que le faisceau reste plan (pas de diffraction).

**q1.** Calculer les impédances $Z_w$ et $Z_A$, puis $r_{wA}$, $t_{wA}$, $r_{Aw}$, $t_{Aw}$ et $r_{A,\mathrm{air}}$.
Vérifier que $t_{wA}\,t_{Aw}=1-r_{wA}^2$. Comparer à l'interface air-aluminium de l'exercice 2.

> [!tip]- 💡 Coup de pouce
> $r_{ij}=(Z_j-Z_i)/(Z_i+Z_j)$ et $t_{ij}=1+r_{ij}$ ; $r_{ji}=-r_{ij}$.


**q2.** Établir l'expression de l'amplitude de l'écho $E_n$ et calculer numériquement $E_0$, $E_1$, $E_2$ et $E_3$ (l'amplitude de l'onde incidente
dans l'eau est prise égale à $1$). Quels sont les signes des échos ? Quel est le rapport $E_{n+1}/E_n$ ?

> [!tip]- 💡 Coup de pouce
> Suivez l'impulsion : aller dans la plaque ($t_{wA}$), réflexion sur la face arrière ($r_{Ab}$), retour dans l'eau ($t_{Aw}$) pour $E_1$ ; un aller-retour supplémentaire ajoute une réflexion sur la face avant vue de l'intérieur ($r_{Aw}$) puis sur la face arrière.


**q3.** Vérifier que l'énergie se conserve : $\sum_{n\ge0}E_n^2=1$. Que représente chaque terme ? Quelle fraction de l'énergie
incidente est renvoyée par $E_0$ ? Par $E_1$, $E_2$, $E_3$ ?

> [!tip]- 💡 Coup de pouce
> $\sum_{n\ge1}E_n^2=(t_{wA}t_{Aw})^2\sum_{n\ge1}(r_{Aw}r_{Ab})^{2(n-1)}$ avec $r_{Ab}^2=1$ : série géométrique de raison $r_{wA}^2$.


**q4.** On mesure $\Delta t=4{,}70~\mu$s entre deux échos successifs. Calculer $e$. L'impulsion de durée
$0{,}4~\mu$s permet-elle de séparer les échos ? Quelle est l'incertitude relative sur $e$ pour une résolution de $10$ ns ?
Quelle fréquence minimale pour séparer les échos d'une plaque de $2$ mm avec une impulsion de $2$ périodes ?

**q5.** En réalité, on mesure $E_2/E_1=0{,}78$ au lieu de la valeur théorique. En déduire le facteur d'atténuation
sur un aller-retour, puis le coefficient d'atténuation $\alpha$ de l'aluminium à $5$ MHz (en Np/m et en dB/m).
Que peut-on déduire de $E_2/E_1$ si on ignore l'impédance de la plaque et si l'atténuation est négligeable ?

> [!tip]- 💡 Coup de pouce
> Si $\mathcal A$ est le facteur d'atténuation sur un aller-retour, $E_2/E_1=\mathcal A\,r_{Aw}r_{Ab}$. Pour la dernière question, inversez $|r|=(Z_A-Z_w)/(Z_A+Z_w)$.


**q6.** La plaque est maintenant collée sur un polymère d'impédance $Z_3=3{,}0\times10^6$ rayl. Calculer le nouveau coefficient
$r_{A3}$, l'amplitude de $E_1'$ et le rapport $E_2'/E_1'$. De combien de décibels l'écho $E_1$ varie-t-il
lorsque le collage disparaît (lame d'air) ? Comment détecte-t-on le défaut ?

> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex2-interface-entre-deux-milieux-notion-d-impedance-acoustique|Exercice 2 — Interface entre deux milieux, notion d'impédance acoustique]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex4-incidence-oblique-lois-de-snell-descartes-angle-critique-reflexion-totale-et-onde-evanescente|Exercice 4 — Incidence oblique : lois de Snell-Descartes, angle critique, réflexion totale et onde évanescente]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex5-sismique-refraction-ondes-coniques-et-epaisseur-d-une-couche|Exercice 5 — Sismique réfraction : ondes coniques et épaisseur d'une couche]] · [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex3-perle-sur-une-corde-jonction-massive-filtre-passe-bas-puis-passe-bande|Exercice 3 — Perle sur une corde : jonction massive, filtre passe-bas puis passe-bande]]

