---
title: "Exercice 5 — Séance 2 -- Équation de Tsiolkovski : propulsion par éjection de masse"
tags:
  - td
  - application-a-la-propulsion-spatiale
---

[[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/index|⬅ Retour]] · <a href="/pdfs/projet1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/projet1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 5. Séance 2 -- Équation de Tsiolkovski : propulsion par éjection de masse

Une fusée de masse initiale $m_0$ (ergols compris) évolue dans l'espace, loin de tout astre : aucune force extérieure ne s'exerce sur elle. Elle éjecte, par sa tuyère, un gaz à la vitesse $\vec v_e$ **par rapport à la fusée**, dirigée vers l'arrière, de norme $v_e$ constante. À l'instant $t$, la masse de la fusée est $m(t)$ et sa vitesse $v(t)$ dans le référentiel galiléen $\mathcal R$. Pendant $\mathrm dt$, elle éjecte la masse $\delta m_e>0$ (donc $\mathrm dm=-\delta m_e<0$). On cherche la variation de vitesse $\Delta V$ de la fusée en fonction de $v_e$, $m_0$ et de la masse finale $m_f$.

**q1.** On considère le système **fermé** $\Sigma$ constitué, à l'instant $t$, de la fusée seule (masse $m$, vitesse $v$) et, à l'instant $t+\mathrm dt$, de la fusée (masse $m+\mathrm dm$, vitesse $v+\mathrm dv$) et du gaz éjecté pendant $\mathrm dt$ (masse $\delta m_e=-\mathrm dm$, vitesse $v-v_e$ dans $\mathcal R$).


- [1.] Pourquoi le système $\Sigma$ est-il isolé ? Écrire sa quantité de mouvement $p(t)$ puis $p(t+\mathrm dt)$.
- [2.] En déduire une relation entre $m\,\mathrm dv$, $v_e$ et $\mathrm dm$. Quel terme néglige-t-on ?

> [!tip]- 💡 Coup de pouce
> Faites un dessin avant/après. La masse du gaz est $-\mathrm dm$ ($>0$). Développez $(m+\mathrm dm)(v+\mathrm dv)$ et simplifiez. Le terme en $\mathrm dm\,\mathrm dv$ est un infiniment petit d'ordre 2.


**q2.** - [3.] Intégrer la relation obtenue entre l'instant initial ($m_0$, $v_0$) et un instant $t$ ($m$, $v$). Donner $\Delta V=v-v_0$ en fonction de $v_e$ et de $m_0/m$.
- [4.] Application numérique : $v_e=3{,}0$ km/s. Quel rapport $m_0/m_f$ faut-il pour atteindre $\Delta V=7{,}8$ km/s (vitesse orbitale) ? Quelle fraction de $m_0$ est du carburant ? Commenter.
- [5.] Le résultat dépend-il du débit massique $D$ ? De la durée de combustion ? Commenter.

> [!tip]- 💡 Coup de pouce
> $\mathrm dv=-v_e\,\mathrm dm/m$ : séparation des variables, intégrale de $m_0$ à $m$. Pour (4), inversez : $m_0/m_f=\exp(\Delta V/v_e)$.


**q3.** - [6.] La fusée est maintenant soumise à une force extérieure $\vec F_{\rm ext}$ (par exemple son poids $m\vec g$ pour un vol vertical). Reprendre le bilan de quantité de mouvement entre $t$ et $t+\mathrm dt$ et montrer que $m\dfrac{\mathrm dv}{\mathrm dt}=-v_e\dfrac{\mathrm dm}{\mathrm dt}+F_{\rm ext}$. Que représente le terme $-v_e\,\mathrm dm/\mathrm dt$ ?
- [7.] Pour $F_{\rm ext}=-mg$ (vol vertical, $g$ supposé constant) et un débit constant $D$, intégrer et montrer que $v(t)=v_e\ln\dfrac{m_0}{m(t)}-g\,t$ avec $m(t)=m_0-Dt$.
- [8.] À quelle condition sur $D$ la fusée décolle-t-elle (à $t=0$, vitesse nulle) ? Interpréter $-gt$.

> [!tip]- 💡 Coup de pouce
> Théorème de la quantité de mouvement : $p(t+\mathrm dt)-p(t)=F_{\rm ext}\,\mathrm dt$. Pour l'intégration, divisez par $m$ : $\dfrac{\mathrm dv}{\mathrm dt}=\dfrac{Dv_e}{m_0-Dt}-g$. Décollage : $\dot v(0)>0$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex1-seance-1-theorie-du-choc-et-quantite-de-mouvement|Exercice 1 — Séance 1 -- Théorie du choc et quantité de mouvement]] · [[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex2-seance-1-exploitation-de-la-chronophotographie-vitesses-forces-lois-de-newton|Exercice 2 — Séance 1 -- Exploitation de la chronophotographie : vitesses, forces, lois de Newton]] · [[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex3-seance-1-conservation-de-la-quantite-de-mouvement-et-bilan-d-energie-cinetique|Exercice 3 — Séance 1 -- Conservation de la quantité de mouvement et bilan d'énergie cinétique]] · [[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex4-extension-choc-elastique-oblique-angle-maximal-de-deviation-et-transfert-d-energie|Exercice 4 — Extension -- Choc élastique oblique : angle maximal de déviation et transfert d'énergie]] · [[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex6-seance-2-application-un-lanceur-a-deux-etages-inspire-du-falcon-9|Exercice 6 — Séance 2 -- Application : un lanceur à deux étages inspiré du Falcon 9]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/TD/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex7-extension-pourquoi-des-etages-optimisation-pertes-par-gravite-et-poussee-minimale|Exercice 7 — Extension -- Pourquoi des étages ? Optimisation, pertes par gravité et poussée minimale]]

