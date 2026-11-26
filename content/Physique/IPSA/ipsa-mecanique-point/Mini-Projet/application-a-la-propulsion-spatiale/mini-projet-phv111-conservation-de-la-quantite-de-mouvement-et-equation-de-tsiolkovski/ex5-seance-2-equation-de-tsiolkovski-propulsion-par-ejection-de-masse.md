---
title: "Exercice 5 — Séance 2 -- Équation de Tsiolkovski : propulsion par éjection de masse"
tags:
  - projet
  - application-a-la-propulsion-spatiale
---

[[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/index|⬅ Retour]] · <a href="/pdfs/projet1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/projet1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/Phv111_MP_Falcon9_Launch.xlsx" target="_blank" rel="noopener">📊 Fichier Excel – Falcon 9</a>

### Exercice 5. Séance 2 -- Équation de Tsiolkovski : propulsion par éjection de masse

*⭐ Indispensable · Difficulté ●●●●○ · ⏱ 60 min · Type : Démonstration / Modélisation*

Une fusée de masse initiale $m_0$ (ergols compris) évolue dans l'espace, loin de tout astre : aucune force extérieure ne s'exerce sur elle. Elle éjecte, par sa tuyère, un gaz à la vitesse $\vec v_e$ **par rapport à la fusée**, dirigée vers l'arrière, de norme $v_e$ constante. À l'instant $t$, la masse de la fusée est $m(t)$ et sa vitesse $v(t)$ dans le référentiel galiléen $\mathcal R$. Pendant $\mathrm dt$, elle éjecte la masse $\delta m_e>0$ (donc $\mathrm dm=-\delta m_e<0$). On cherche la variation de vitesse $\Delta V$ de la fusée en fonction de $v_e$, $m_0$ et de la masse finale $m_f$.


> [!question]- 🪝 Accroche
> **Comment avancer dans le vide, sans rien pour pousser ?**
>
> *Durée de l'introduction : 5 min*
>
> *Dans l'espace, il n'y a ni air ni sol sur lequel s'appuyer. Pourtant les fusées accélèrent. Quelle grandeur se conserve pour que ce soit possible ? Pourquoi une fusée de $560$ t ne se pose-t-elle que $10$ t de charge utile en orbite ?*
>
> **Idée clé : on obtient la propulsion par conservation de la quantité de mouvement totale**, comme dans le choc de la séance 1 : fusée $+$ gaz forment un système isolé. Si le gaz part vers l'arrière avec $\vec p_{\rm gaz}$, la fusée part vers l'avant avec $-\vec p_{\rm gaz}$. En répétant ce processus de manière continue, on obtient $\Delta V=v_e\ln(m_0/m_f)$.




> [!abstract]- 🧠 À savoir avant
> **Conservation de $\vec p$ d'un système isolé**
>
> Vu en séance 1 : pour un système isolé **fermé**, $\vec p_{\rm tot}$ est constante. Ici, le système est choisi **fermé** : {fusée à $t$} $=$ {fusée à $t+\mathrm dt$} $+$ {gaz éjecté pendant $\mathrm dt$}.
>
> **Composition des vitesses**
>
> La vitesse du gaz dans $\mathcal R$ est $\vec v_{\rm gaz}=\vec v+\vec v_e$ (vitesse de la fusée plus vitesse relative). En 1D avec l'axe de la fusée : $v_{\rm gaz}=v-v_e$.
>
> **Primitive de $1/m$**
>
> $\displaystyle\int_{m_0}^{m_f}\frac{\mathrm dm}{m}=\ln\frac{m_f}{m_0}$.




> [!info]- 🎯 Ce que tu sauras faire
> **Établir et interpréter l'équation de Tsiolkovski**
>
> Savoir choisir un système **fermé**, écrire la conservation de $\vec p$ entre $t$ et $t+\mathrm dt$, négliger l'infiniment petit d'ordre 2, intégrer et obtenir $\Delta V=v_e\ln\dfrac{m_0}{m_f}$ ; savoir ce que devient ce résultat en présence de forces extérieures (gravité, traînée) ; interpréter le rôle de $v_e$ et du rapport de masses.




> [!tip]- 📖 Rappel de cours
> **Équation de Tsiolkovski**
>
> En l'absence de force extérieure, $m\,\dfrac{\mathrm dv}{\mathrm dt}=-v_e\,\dfrac{\mathrm dm}{\mathrm dt}$, soit $\boxed{\Delta V=v_e\ln\dfrac{m_0}{m_f}}$. Avec le débit massique $D=-\dfrac{\mathrm dm}{\mathrm dt}$, la poussée vaut $F=D\,v_e$.
>
> **Avec une force extérieure $\vec F_{\rm ext}$**
>
> $m\dfrac{\mathrm d\vec v}{\mathrm dt}=\vec F_{\rm ext}+D\,\vec v_e'$ où $\vec v_e'=-\vec v_e$ est dirigée vers l'avant : par exemple la pesanteur en vol vertical donne $v(t)=v_e\ln\dfrac{m_0}{m(t)}-gt$.




> [!note]- 🧮 Outils mathématiques
> **Différentielle et infiniment petits d'ordre 2**
>
> $(\mathrm dm)(\mathrm dv)$ est négligeable devant $m\,\mathrm dv$ et $v_e\,\mathrm dm$ quand $\mathrm dt\to0$.
>
> **Séparation des variables**
>
> $\mathrm dv=-v_e\dfrac{\mathrm dm}{m}$ s'intègre directement : $v-v_0=-v_e\ln\dfrac{m}{m_0}=v_e\ln\dfrac{m_0}{m}$.
>
> **Propriétés du logarithme**
>
> $\ln(ab)=\ln a+\ln b$ : les $\Delta V$ des étages s'ajoutent si les rapports de masses se multiplient. $\ln10\approx2{,}30$, $\ln2\approx0{,}69$.
>
> **Développement limité**
>
> Pour $\delta m\ll m$ : $\ln\dfrac{m_0}{m_0-\delta m}\approx\dfrac{\delta m}{m_0}$, d'où $\Delta V\approx v_e\dfrac{\delta m}{m_0}$ (petite éjection).



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
> [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex1-seance-1-theorie-du-choc-et-quantite-de-mouvement|Exercice 1 — Séance 1 -- Théorie du choc et quantité de mouvement]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex2-seance-1-exploitation-de-la-chronophotographie-vitesses-forces-lois-de-newton|Exercice 2 — Séance 1 -- Exploitation de la chronophotographie : vitesses, forces, lois de Newton]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex3-seance-1-conservation-de-la-quantite-de-mouvement-et-bilan-d-energie-cinetique|Exercice 3 — Séance 1 -- Conservation de la quantité de mouvement et bilan d'énergie cinétique]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex4-extension-choc-elastique-oblique-angle-maximal-de-deviation-et-transfert-d-energie|Exercice 4 — Extension -- Choc élastique oblique : angle maximal de déviation et transfert d'énergie]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex6-seance-2-application-un-lanceur-a-deux-etages-inspire-du-falcon-9|Exercice 6 — Séance 2 -- Application : un lanceur à deux étages inspiré du Falcon 9]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex7-extension-pourquoi-des-etages-optimisation-pertes-par-gravite-et-poussee-minimale|Exercice 7 — Extension -- Pourquoi des étages ? Optimisation, pertes par gravité et poussée minimale]]


