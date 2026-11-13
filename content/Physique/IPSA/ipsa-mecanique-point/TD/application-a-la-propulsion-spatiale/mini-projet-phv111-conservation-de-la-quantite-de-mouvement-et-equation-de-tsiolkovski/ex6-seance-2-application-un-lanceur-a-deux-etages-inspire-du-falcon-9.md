---
title: "Exercice 6 — Séance 2 -- Application : un lanceur à deux étages inspiré du Falcon 9"
tags:
  - td
  - application-a-la-propulsion-spatiale
---

[[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/index|⬅ Retour]] · <a href="/pdfs/projet1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/projet1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 6. Séance 2 -- Application : un lanceur à deux étages inspiré du Falcon 9

On applique l'équation de Tsiolkovski à un lanceur à deux étages. **Les données réelles du Falcon 9 sont fournies dans le fichier tableur du projet** (non reproduit ici) : on les saisit à la place des valeurs ci-dessous. Pour que cette fiche soit autonome, on utilise un **lanceur fictif, de caractéristiques voisines** (données illustratives, **pas** les valeurs officielles) : masse au décollage $m_0=560$ t ; étage 1 : vitesse d'éjection effective $v_{e1}=2900$ m/s, débit $D_1=2531$ kg/s, masse en fin de combustion (étages 1 et 2 réunis, avant largage) $m_{1f}=150$ t ; étage 2 : après largage de l'étage 1 vide, masse $m_{2i}=125$ t, $v_{e2}=3400$ m/s, $D_2=272$ kg/s, masse finale (étage 2 vide $+$ charge utile) $m_{2f}=17$ t. On prend $g=9{,}81~\mathrm{m\,s^{-2}}$ constant.

**q1.** Pour chaque étage du lanceur fictif :


- [1.] Calculer le rapport de masses $R_i$ et le $\Delta V_i$ idéal. Que vaut le $\Delta V$ total ?
- [2.] Calculer la durée de combustion $t_{bi}$ et la poussée $F_i=D_iv_{ei}$.
- [3.] Calculer le rapport poussée/poids au décollage. Le lanceur décolle-t-il ?

> [!tip]- 💡 Coup de pouce
> Étage 1 : $m_{\rm init}=m_0=560$ t, $m_{\rm fin}=m_{1f}=150$ t. Étage 2 : $m_{\rm init}=m_{2i}=125$ t, $m_{\rm fin}=m_{2f}=17$ t.


**q2.** - [4.] Écrire $v(t)$ pendant l'étage 1 (vol vertical, $g$ constant). Calculer $v$ à $t=80$ s et à la fin de la combustion ($t_{b1}$).
- [5.] Calculer la perte par gravité sur l'étage 1 et la comparer à $\Delta V_1$. Que conclure ?
- [6.] Montrer que l'altitude à la fin de la combustion de l'étage 1 est $h=v_{e}\tau\Big[1-\dfrac{1+\ln R_1}{R_1}\Big]-\tfrac12gt_{b1}^2$ avec $\tau=m_0/D_1$ et la calculer.

> [!tip]- 💡 Coup de pouce
> $v(t)=v_e\ln\dfrac{m_0}{m_0-D_1t}-gt$. Pour l'altitude, intégrez $v(t)$ entre $0$ et $t_{b1}$ avec le changement $x=t/\tau$ ; $\int-\ln(1-x)\,\mathrm dx=(1-x)\ln(1-x)+x$.


**q3.** - [7.] Les données du tableur du projet donnent d'autres valeurs : indiquer, pour le Falcon 9 réel, quelles grandeurs il faut lire dans le fichier et comment calculer $\Delta V_1$, $\Delta V_2$, $F_1/(m_0g)$ et $t_{b1}$.
- [8.] Le $\Delta V$ idéal est-il suffisant pour une orbite basse (vitesse $7{,}8$ km/s, pertes de $\approx1{,}5$ à $2$ km/s) ? Faire un bilan critique.

> [!tip]- 💡 Coup de pouce
> Il faut 4 grandeurs par étage : masse initiale, masse finale, débit (ou durée) et $v_e$ (ou $I_{sp}$). Pensez au $I_{sp}$ : $v_e=g_0I_{sp}$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex5-seance-2-equation-de-tsiolkovski-propulsion-par-ejection-de-masse|Exercice 5 — Séance 2 -- Équation de Tsiolkovski : propulsion par éjection de masse]] · [[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex7-extension-pourquoi-des-etages-optimisation-pertes-par-gravite-et-poussee-minimale|Exercice 7 — Extension -- Pourquoi des étages ? Optimisation, pertes par gravité et poussée minimale]] · [[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex1-seance-1-theorie-du-choc-et-quantite-de-mouvement|Exercice 1 — Séance 1 -- Théorie du choc et quantité de mouvement]] · [[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex2-seance-1-exploitation-de-la-chronophotographie-vitesses-forces-lois-de-newton|Exercice 2 — Séance 1 -- Exploitation de la chronophotographie : vitesses, forces, lois de Newton]] · [[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex3-seance-1-conservation-de-la-quantite-de-mouvement-et-bilan-d-energie-cinetique|Exercice 3 — Séance 1 -- Conservation de la quantité de mouvement et bilan d'énergie cinétique]] · [[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex4-extension-choc-elastique-oblique-angle-maximal-de-deviation-et-transfert-d-energie|Exercice 4 — Extension -- Choc élastique oblique : angle maximal de déviation et transfert d'énergie]]

