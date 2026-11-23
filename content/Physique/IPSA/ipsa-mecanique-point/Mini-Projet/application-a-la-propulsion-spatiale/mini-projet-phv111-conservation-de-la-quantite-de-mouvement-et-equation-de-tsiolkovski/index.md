---
title: "Mini-projet Phv111 -- Conservation de la quantité de mouvement et équation de Tsiolkovski"
tags:
  - projet
  - application-a-la-propulsion-spatiale
---

[[physique/IPSA/ipsa-mecanique-point/index|⬅ Mécanique du point — IPSA]]

> [!info] ℹ️ Application à la propulsion spatiale
> Séance 1


<a href="/pdfs/projet1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/projet1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/Phv111_MP_Falcon9_Launch.xlsx" target="_blank" rel="noopener">📊 Fichier Excel – Falcon 9</a>

> [!info]+ 🗓️ Organisation
> **Séance 1 (choc et quantité de mouvement)**
>
> Partie I.1 théorie du choc (30 min), I.2 exploitation de la chronophotographie de l'annexe : vitesses, quantités de mouvement, forces (60 min), I.3--I.4 conservation de $\vec p$ et bilan d'énergie (30 min). À l'issue de la séance 1 : **synthèse** (rappel théorique, tracés, résultats) déposée en PDF sur Moodle **sous deux semaines**.
>
> **Séance 2 (propulsion)**
>
> Partie II.1 équation de Tsiolkovski (60 min), II.2 application à un lanceur à deux étages inspiré du Falcon 9 avec le fichier tableur fourni (60 min). Les exercices d'extension sont facultatifs.
>
> **Rendu final**
>
> **Compte rendu final** à déposer avant le **vendredi 10 décembre** : démarches, résultats numériques avec incertitudes, discussion critique.

> [!question]+ 🎣 Accroche
> **Du billard à la fusée : une seule loi**
>
> *Durée de l'introduction : 5 min*
>
> *Deux boules de billard qui s'entrechoquent et une fusée qui accélère dans le vide : quel point commun ? Quelle grandeur se conserve dans les deux cas, et pourquoi ?*
>
> **Idée clé : la quantité de mouvement totale d'un système isolé est conservée.** Dans un choc, elle se redistribue entre deux mobiles ; dans une fusée, entre la fusée et son gaz d'éjection. La 3\textsuperscript{e} loi de Newton garantit que ce que l'un gagne, l'autre le perd.

> [!abstract]+ 📚 Prérequis
> **Cinématique du point**
>
> Vecteur vitesse, mouvement rectiligne uniforme, repérage par coordonnées cartésiennes, échelle d'une figure.
>
> **Lois de Newton**
>
> Principe d'inertie, $\sum\vec F=\mathrm d\vec p/\mathrm dt$, action--réaction ; notions de système et de force extérieure.
>
> **Énergie cinétique**
>
> $E_c=\tfrac12mv^2$, grandeur scalaire additive.
>
> **Outils numériques**
>
> Tableur (formules, graphique), logarithme népérien, incertitudes de mesure.

> [!info]+ 🎯 Objectifs
> **Comprendre la conservation de la quantité de mouvement**
>
> Démontrer $\vec p_{\rm tot}=\text{cte}$ à partir de la 3\textsuperscript{e} loi, la vérifier expérimentalement sur une chronophotographie, la classer parmi les lois de conservation (énergie, moment cinétique).
>
> **Mesurer et exploiter des données expérimentales**
>
> Passer d'une feuille de points à des vitesses, des impulsions, des forces et des énergies, estimer les incertitudes, comparer à la théorie avec esprit critique.
>
> **Établir et utiliser l'équation de Tsiolkovski**
>
> Écrire un bilan de quantité de mouvement sur un système **fermé** à masse apparente variable, intégrer, interpréter, puis dimensionner un lanceur à plusieurs étages avec pesanteur.
>
> **Rédiger un compte rendu scientifique**
>
> Structurer un rapport (introduction, méthode, résultats, discussion), justifier les approximations, présenter les résultats avec leurs unités et incertitudes.

> [!note]+ 📖 Point de cours
> **Quantité de mouvement et deuxième loi**
>
> $\vec p=m\vec v$ ; $\dfrac{\mathrm d\vec p}{\mathrm dt}=\sum\vec F_{\rm ext}$ ; $\Delta\vec p=\bar{\vec F}\,\Delta t$. Pour un système isolé : $\vec p_{\rm tot}=\text{cte}$.
>
> **Chocs**
>
> $\vec p_{\rm tot}$ est conservée dans tout choc d'un système isolé ; $E_c$ est conservée seulement pour un choc élastique ; choc mou : $\vec v_f=\dfrac{m_1\vec v_1+m_2\vec v_2}{m_1+m_2}$.
>
> **Propulsion par réaction**
>
> $m\,\mathrm dv=-v_e\,\mathrm dm$ donc $\Delta V=v_e\ln\dfrac{m_0}{m_f}$ ; poussée $F=Dv_e$ ; avec pesanteur : $v=v_e\ln\dfrac{m_0}{m}-gt$.
>
> **Étagement**
>
> Les $\Delta V$ des étages s'ajoutent ; un étage unique est limité à $v_e\ln(1/\varepsilon)$ ($\varepsilon$ : coefficient de structure).

> [!note]- 🧮 Outils mathématiques
> **Vecteurs**
>
> Somme, différence, composantes, norme ; construction à l'échelle.
>
> **Logarithme, exponentielle**
>
> $\ln(ab)=\ln a+\ln b$ ; $\int\mathrm dm/m=\ln m$ ; $e^{x}$ pour inverser une relation logarithmique.
>
> **Incertitudes**
>
> Incertitude relative : $\delta(ab)/ab\approx\delta a/a+\delta b/b$ ; $\delta(v^2)/v^2=2\,\delta v/v$.
>
> **Tableur**
>
> Formules, références absolues, graphique $v(t)$ ; comparaison de plusieurs jeux de paramètres.


## Exercices

- [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex1-seance-1-theorie-du-choc-et-quantite-de-mouvement|Exercice 1 — Séance 1 -- Théorie du choc et quantité de mouvement]]
- [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex2-seance-1-exploitation-de-la-chronophotographie-vitesses-forces-lois-de-newton|Exercice 2 — Séance 1 -- Exploitation de la chronophotographie : vitesses, forces, lois de Newton]]
- [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex3-seance-1-conservation-de-la-quantite-de-mouvement-et-bilan-d-energie-cinetique|Exercice 3 — Séance 1 -- Conservation de la quantité de mouvement et bilan d'énergie cinétique]]
- [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex4-extension-choc-elastique-oblique-angle-maximal-de-deviation-et-transfert-d-energie|Exercice 4 — Extension -- Choc élastique oblique : angle maximal de déviation et transfert d'énergie]]
- [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex5-seance-2-equation-de-tsiolkovski-propulsion-par-ejection-de-masse|Exercice 5 — Séance 2 -- Équation de Tsiolkovski : propulsion par éjection de masse]]
- [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex6-seance-2-application-un-lanceur-a-deux-etages-inspire-du-falcon-9|Exercice 6 — Séance 2 -- Application : un lanceur à deux étages inspiré du Falcon 9]]
- [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex7-extension-pourquoi-des-etages-optimisation-pertes-par-gravite-et-poussee-minimale|Exercice 7 — Extension -- Pourquoi des étages ? Optimisation, pertes par gravité et poussée minimale]]
