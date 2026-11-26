---
title: "Exercice 1 — Séance 1 -- Théorie du choc et quantité de mouvement"
tags:
  - projet
  - application-a-la-propulsion-spatiale
---

[[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/index|⬅ Retour]] · <a href="/pdfs/projet1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/projet1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/Phv111_MP_Falcon9_Launch.xlsx" target="_blank" rel="noopener">📊 Fichier Excel – Falcon 9</a>

### Exercice 1. Séance 1 -- Théorie du choc et quantité de mouvement

*⭐ Indispensable · Difficulté ●●○○○ · ⏱ 30 min · Type : Cours actif / Théorie*

On considère un choc (ou collision) entre deux corps de masses $m_1$ et $m_2$ comme une interaction **très brève** et de **courte portée**, localisée dans le temps et l'espace : on distingue un **avant** et un **après** la collision. Lors du choc, les corps 1 et 2 exercent l'un sur l'autre les forces $\vec F_{1\to2}$ et $\vec F_{2\to1}$ ; l'ensemble des deux corps constitue un système **isolé**. On se place dans un référentiel galiléen.


> [!question]- 🪝 Accroche
> **Pourquoi la quantité de mouvement se conserve-t-elle ?**
>
> *Durée de l'introduction : 3 à 5 min*
>
> *Deux palets sur un coussin d'air se heurtent : chacun repart dans une autre direction avec une autre vitesse. **Qu'est-ce qui reste exactement le même** avant et après ? L'énergie ? La vitesse totale ? Autre chose ? Et pourquoi les forces très violentes du choc n'y changent-elles rien ?*
>
> **Idée clé : les forces du choc sont des paires action--réaction.** $\dfrac{\mathrm d\vec p_1}{\mathrm dt}=\vec F_{2\to1}$, $\dfrac{\mathrm d\vec p_2}{\mathrm dt}=-\vec F_{2\to1}$, donc $\dfrac{\mathrm d(\vec p_1+\vec p_2)}{\mathrm dt}=\vec0$ : **ce que l'un gagne, l'autre le perd**. La nature du choc (élastique ou non) se lit, elle, sur l'énergie cinétique.




> [!abstract]- 🧠 À savoir avant
> **Lois de Newton et notion de force**
>
> Principe d'inertie, principe fondamental $\sum\vec F=\dfrac{\mathrm d\vec p}{\mathrm dt}$, action--réaction (voir TD sur les lois de Newton). Une force extérieure est une action exercée par un objet n'appartenant pas au système.
>
> **Intégrale d'une fonction du temps**
>
> Si $\dfrac{\mathrm d\vec p}{\mathrm dt}=\vec F(t)$, alors $\Delta\vec p=\displaystyle\int_{t_1}^{t_2}\vec F(t)\,\mathrm dt=\bar{\vec F}\,\Delta t$ où $\bar{\vec F}$ est la force moyenne.




> [!info]- 🎯 Ce que tu sauras faire
> **Démontrer la conservation de la quantité de mouvement**
>
> Savoir définir $\vec p$, relier sa variation aux forces (2\textsuperscript{e} loi), et démontrer à partir de l'action--réaction que la quantité de mouvement totale d'un système isolé est conservée ; savoir classer les chocs (élastique, partiellement élastique, mou) par le bilan d'énergie cinétique.




> [!tip]- 📖 Rappel de cours
> **Quantité de mouvement et deuxième loi sous forme générale**
>
> $\vec p=m\vec v$ (kg\,m\,s$^{-1}$). Forme générale de la 2\textsuperscript{e} loi : $\dfrac{\mathrm d\vec p}{\mathrm dt}=\sum\vec F_{\rm ext}$. Pour un système isolé ou pseudo-isolé ($\sum\vec F_{\rm ext}=\vec0$), $\vec p_{\rm tot}$ est constante.
>
> **Classification des chocs**
>
> **Élastique** : $E_c$ conservée ($E_c'=E_c$). **Partiellement élastique** (ou inélastique) : $E_c'<E_c$, les corps repartent séparément. **Mou** (parfaitement inélastique) : les corps restent collés, vitesse commune $\vec v_f=\dfrac{m_1\vec v_1+m_2\vec v_2}{m_1+m_2}$, perte maximale d'énergie cinétique. Dans tous les cas, $\vec p_{\rm tot}$ est conservée.




> [!note]- 🧮 Outils mathématiques
> **Somme vectorielle et inégalité triangulaire**
>
> $\|\vec u+\vec v\|\le\|\vec u\|+\|\vec v\|$, avec égalité si les vecteurs sont de même sens. La somme se calcule par composantes ou par la règle du parallélogramme.
>
> **Intégrale d'une force sur la durée du choc**
>
> $\displaystyle\int_{t_1}^{t_2}\vec F\,\mathrm dt=\Delta\vec p$ : l'aire sous la courbe $F(t)$ (pic bref et intense) est la variation de quantité de mouvement.
>
> **Dérivée d'une somme**
>
> $\dfrac{\mathrm d}{\mathrm dt}(\vec p_1+\vec p_2)=\dfrac{\mathrm d\vec p_1}{\mathrm dt}+\dfrac{\mathrm d\vec p_2}{\mathrm dt}$ : la linéarité de la dérivée permet de sommer les deux équations.



**q1.** - [1.] Rappeler la notion de quantité de mouvement $\vec p$.
- [2.] Rappeler les 3 lois de Newton. Quelle grandeur physique est modifiée sous l'action d'une force extérieure ? Écrire le principe d'action--réaction qui relie $\vec F_{1\to2}$ et $\vec F_{2\to1}$ lors d'un choc.
- [3.] Avant et après le choc, les corps ne sont soumis à aucune force. Que peut-on dire de leurs quantités de mouvement $\vec p_1,\vec p_2$ avant le choc ? Et de $\vec p_1',\vec p_2'$ après le choc ?


> [!tip]- 💡 Coup de pouce
> Pensez au principe d'inertie : sans force, la vitesse est constante, donc $\vec p=m\vec v$ aussi (la masse est constante).



**q2.** - [4.] Lors du choc, le corps 1 est soumis à $\vec F_{2\to1}$ et le corps 2 à $\vec F_{1\to2}$. Écrire ce qu'implique la 2\textsuperscript{e} loi de Newton pour $\vec p_1$, puis pour $\vec p_2$.
- [5.] On définit $\vec p_{\rm tot}=\vec p_1+\vec p_2$. Montrer, en partant du principe d'action--réaction, que $\vec p_{\rm tot}$ est conservé.
- [6.] Définir les notions de choc élastique, choc partiellement élastique et choc mou.


> [!tip]- 💡 Coup de pouce
> Écrivez les deux équations $\mathrm d\vec p_i/\mathrm dt=\dots$, additionnez-les, puis utilisez la 3\textsuperscript{e} loi. Pour les chocs, comparez l'énergie cinétique avant et après.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex2-seance-1-exploitation-de-la-chronophotographie-vitesses-forces-lois-de-newton|Exercice 2 — Séance 1 -- Exploitation de la chronophotographie : vitesses, forces, lois de Newton]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex3-seance-1-conservation-de-la-quantite-de-mouvement-et-bilan-d-energie-cinetique|Exercice 3 — Séance 1 -- Conservation de la quantité de mouvement et bilan d'énergie cinétique]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex4-extension-choc-elastique-oblique-angle-maximal-de-deviation-et-transfert-d-energie|Exercice 4 — Extension -- Choc élastique oblique : angle maximal de déviation et transfert d'énergie]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex5-seance-2-equation-de-tsiolkovski-propulsion-par-ejection-de-masse|Exercice 5 — Séance 2 -- Équation de Tsiolkovski : propulsion par éjection de masse]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex6-seance-2-application-un-lanceur-a-deux-etages-inspire-du-falcon-9|Exercice 6 — Séance 2 -- Application : un lanceur à deux étages inspiré du Falcon 9]]


