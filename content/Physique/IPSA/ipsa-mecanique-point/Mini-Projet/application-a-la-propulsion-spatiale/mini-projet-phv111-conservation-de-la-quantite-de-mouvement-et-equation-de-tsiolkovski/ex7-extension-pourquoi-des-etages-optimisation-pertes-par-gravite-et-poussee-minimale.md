---
title: "Exercice 7 — Extension -- Pourquoi des étages ? Optimisation, pertes par gravité et poussée minimale"
tags:
  - projet
  - application-a-la-propulsion-spatiale
---

[[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/index|⬅ Retour]] · <a href="/pdfs/projet1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/projet1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/Phv111_MP_Falcon9_Launch.xlsx" target="_blank" rel="noopener">📊 Fichier Excel – Falcon 9</a>

### Exercice 7. Extension -- Pourquoi des étages ? Optimisation, pertes par gravité et poussée minimale *(facultatif)*

*Difficulté ●●●●● · ⏱ 50 min · Type : Approfondissement / Modélisation*

On veut placer une charge utile $m_u=1$ t sur une trajectoire exigeant $\Delta V=9$ km/s (pesanteur et traînée comprises dans cette valeur), avec des moteurs de vitesse d'éjection $v_e=3{,}0$ km/s. Chaque étage de masse $m_s$ contient une structure de masse $\varepsilon\,m_s$ ($\varepsilon=0{,}10$) et $(1-\varepsilon)m_s$ d'ergols ; l'étage vide est largué après usage. On néglige la pesanteur dans les questions (a) à (c) ($\Delta V=9$ km/s est le besoin total) puis on la réintroduit en (d) et (e).

> [!question]+ 🎣 Accroche
> **Pourquoi ne peut-on pas faire une fusée à un seul étage ?**
>
> *Durée de l'introduction : 3 min*
>
> *Si $\Delta V=v_e\ln(m_0/m_f)$, il suffirait d'ajouter assez de carburant pour atteindre n'importe quelle vitesse. Pourquoi les lanceurs ont-ils alors presque tous plusieurs étages ?*
>
> **Idée clé : les réservoirs pèsent.** Pour transporter plus d'ergols, il faut plus de structure, ce qui donne un rapport $m_{\rm init}/m_{\rm fin}$ borné par $1/\varepsilon$. Larguer l'étage vide permet de repartir avec un $\varepsilon$ « neuf » : le $\Delta V$ total n'est plus borné.


> [!abstract]+ 📚 Prérequis
> **Équation de Tsiolkovski**
>
> $\Delta V=v_e\ln\dfrac{m_{\rm init}}{m_{\rm fin}}$ ; pour plusieurs étages, les $\Delta V$ s'ajoutent.
>
> **Vol vertical avec pesanteur**
>
> $v(t)=v_e\ln\dfrac{m_0}{m(t)}-g\,t$ ; décollage si $D\,v_e>m_0g$.


> [!info]+ 🎯 Objectifs
> **Comprendre l'intérêt de l'étagement par un calcul**
>
> Montrer qu'un étage unique ne peut pas atteindre un $\Delta V$ donné quelle que soit la quantité d'ergols, dimensionner un lanceur à deux étages, calculer la masse au décollage, et quantifier les pertes par gravité et la poussée minimale nécessaire.


> [!note]+ 📖 Point de cours
> **Masse d'un étage pour un $\Delta V$ donné**
>
> Avec $R=e^{\Delta V/v_e}$ et $R=\dfrac{m_s+m_u}{\varepsilon m_s+m_u}$ : $m_s=m_u\,\dfrac{R-1}{1-\varepsilon R}$, valable si $R<1/\varepsilon$.


> [!note]- 🧮 Outils mathématiques
> **Exponentielle et logarithme**
>
> $R=e^{\Delta V/v_e}$ ; $e^{1{,}5}=4{,}4817$ ; $\ln10=2{,}3026$.
>
> **Résolution d'une équation linéaire en $m_s$**
>
> $m_s+m_u=R(\varepsilon m_s+m_u)\Rightarrow m_s(1-R\varepsilon)=m_u(R-1)$.
>
> **Limites**
>
> Quand $R\to1/\varepsilon$, $m_s\to\infty$ : la charge utile tend vers $0$ pour une masse donnée.


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
> [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex5-seance-2-equation-de-tsiolkovski-propulsion-par-ejection-de-masse|Exercice 5 — Séance 2 -- Équation de Tsiolkovski : propulsion par éjection de masse]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex6-seance-2-application-un-lanceur-a-deux-etages-inspire-du-falcon-9|Exercice 6 — Séance 2 -- Application : un lanceur à deux étages inspiré du Falcon 9]]

