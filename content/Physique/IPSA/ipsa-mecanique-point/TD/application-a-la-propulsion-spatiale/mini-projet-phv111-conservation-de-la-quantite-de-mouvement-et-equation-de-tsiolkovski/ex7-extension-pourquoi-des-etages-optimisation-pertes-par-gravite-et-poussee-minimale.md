---
title: "Exercice 7 — Extension -- Pourquoi des étages ? Optimisation, pertes par gravité et poussée minimale"
tags:
  - td
  - application-a-la-propulsion-spatiale
---

[[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/index|⬅ Retour]] · <a href="/pdfs/projet1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/projet1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 7. Extension -- Pourquoi des étages ? Optimisation, pertes par gravité et poussée minimale *(facultatif)*

On veut placer une charge utile $m_u=1$ t sur une trajectoire exigeant $\Delta V=9$ km/s (pesanteur et traînée comprises dans cette valeur), avec des moteurs de vitesse d'éjection $v_e=3{,}0$ km/s. Chaque étage de masse $m_s$ contient une structure de masse $\varepsilon\,m_s$ ($\varepsilon=0{,}10$) et $(1-\varepsilon)m_s$ d'ergols ; l'étage vide est largué après usage. On néglige la pesanteur dans les questions (a) à (c) ($\Delta V=9$ km/s est le besoin total) puis on la réintroduit en (d) et (e).

**q1.** - [(a)] Montrer que pour un étage unique, $\Delta V$ est borné par $v_e\ln(1/\varepsilon)$ quelle que soit la quantité d'ergols. Conclure pour $\Delta V=9$ km/s.
- [(b)] Deux étages identiques en $v_e$ et $\varepsilon$ sont utilisés, chacun fournissant $\Delta V=4{,}5$ km/s. Calculer le rapport de masses $R$ de chaque étage.
- [(c)] Dimensionner le lanceur depuis le haut : calculer $m_{s2}$ (étage 2) puis $m_{s1}$ (étage 1) et la masse au décollage $m_0$ pour $m_u=1$ t. Quelle fraction de $m_0$ est la charge utile ?

> [!tip]- 💡 Coup de pouce
> (a) $R=\dfrac{m_s+m_u}{\varepsilon m_s+m_u}$ : que devient $R$ quand $m_s\to\infty$ ? (c) La charge utile de l'étage 1 est $m_{s2}+m_u$.


**q2.** On réintroduit maintenant la pesanteur pour l'étage 1 de la question précédente (vol vertical, $g=9{,}81~\mathrm{m\,s^{-2}}$ constante).


- [(d)] Quelle poussée minimale $F_{\min}$ l'étage 1 doit-il fournir pour décoller ? Pour une poussée $F=1{,}3\,m_0g$, calculer le débit $D$, la durée de combustion $t_b$ et la perte par gravité $g\,t_b$.
- [(e)] Même question pour $F=2{,}0\,m_0g$. Comparer. Quelle est l'accélération maximale subie en fin de combustion dans les deux cas ? Conclure sur le choix de la poussée.

> [!tip]- 💡 Coup de pouce
> $F=Dv_e$ donc $D=F/v_e$. La masse d'ergols de l'étage 1 est $(1-\varepsilon)m_{s1}$. En fin de combustion : $m_{\rm fin}=\varepsilon m_{s1}+7{,}31$ t $=11{,}92$ t. Accélération : $a=\dfrac{F}{m_{\rm fin}}-g$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex5-seance-2-equation-de-tsiolkovski-propulsion-par-ejection-de-masse|Exercice 5 — Séance 2 -- Équation de Tsiolkovski : propulsion par éjection de masse]] · [[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex6-seance-2-application-un-lanceur-a-deux-etages-inspire-du-falcon-9|Exercice 6 — Séance 2 -- Application : un lanceur à deux étages inspiré du Falcon 9]]

