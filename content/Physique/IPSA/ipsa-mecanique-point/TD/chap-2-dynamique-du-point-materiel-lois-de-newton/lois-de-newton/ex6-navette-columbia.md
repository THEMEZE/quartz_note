---
title: "Exercice 6 — (*) Navette Columbia"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td4_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 6. (*) Navette Columbia *(facultatif)*

*Difficulté ●●○○○ · ⏱ 25 min · Type : Entraînement / Esprit critique*

Lors de son premier vol en 1981, la navette spatiale Columbia faisait partie d'un ensemble de masse $m=2{,}0\times10^6$ kg qui développait une poussée totale $F=2{,}85\times10^7$ N. On suppose le décollage vertical, dans le champ de pesanteur $g=9{,}81~\mathrm{m\,s^{-2}}$ ; la navette est assimilée à un point matériel et on néglige les frottements de l'air.

> [!question]+ 🎣 Accroche
> **Vérifier un chiffre de presse**
>
> *Durée de l'introduction : 3 min*
>
> *Un journal annonce que la navette atteint $33{,}5$ m/s six secondes après le décollage. **Avec seulement la masse et la poussée**, pouvez-vous vérifier ce chiffre ? Si l'écart est de $20\%$, qui a tort : le journaliste ou le modèle ?*
>
> **Idée clé : bilan des forces, puis intégration.** Poussée vers le haut, poids vers le bas : $ma=F-mg$. Avec $a$ constante : $v=at$. La comparaison avec la mesure indique ce que le modèle néglige.


> [!abstract]+ 📚 Prérequis
> **Poussée d'un moteur-fusée**
>
> La poussée est la force exercée sur la fusée par les gaz éjectés. Pour un décollage vertical, avec masse $m$ constante : $F-mg=ma$.


> [!info]+ 🎯 Objectifs
> **Comparer un modèle à une mesure et expliquer l'écart**
>
> Savoir appliquer la 2\textsuperscript{e} loi à un décollage, intégrer une accélération constante, comparer à une donnée expérimentale et identifier les hypothèses du modèle qui expliquent un écart.


> [!info]- 🧑‍🏫 Objectifs pédagogiques (enseignant)
> **Esprit critique sur un modèle**
>
> Le modèle à masse et poussée constantes sous-estime la vitesse d'environ $20\%$. Les étudiants doivent chercher les raisons : la masse diminue (consommation d'ergols), la poussée varie. Il est important de **quantifier** l'effet : combien de masse faut-il perdre pour expliquer l'écart ? Cela introduit l'idée d'un système à masse variable (équation de Tsiolkovski), hors programme ici.


> [!note]+ 📖 Point de cours
> **Décollage vertical**
>
> $a=\dfrac Fm-g$. Il faut $F>mg$ pour décoller. Avec $a$ constante partant du repos : $v=at$, $z=\tfrac12at^2$.


> [!note]- 🧮 Outils mathématiques
> **Notation scientifique**
>
> $2{,}85\times10^7/2{,}0\times10^6=14{,}25$ : manipuler les puissances de dix sans calculatrice.
>
> **Écart relatif**
>
> $\dfrac{|v_{\rm mesuré}-v_{\rm modèle}|}{v_{\rm mesuré}}=\dfrac{33{,}5-26{,}6}{33{,}5}\approx21\%$.
>
> **Résolution inverse**
>
> Pour trouver la masse moyenne qui donnerait $\bar a=33{,}5/6$ : $\bar m=\dfrac{F}{g+\bar a}$.


**q1.** - [(a)] Quelle était l'accélération de l'ensemble à pleine puissance ?
- [(b)] Selon les rapports de presse, $6{,}0$ s après s'être dégagée de la tour de soutien, la navette avait une vitesse de $33{,}5~\mathrm{m\,s^{-1}}$. Vérifier si les rapports sont corrects.
- [(c)] Proposer une explication s'il y a une différence.

> [!tip]- 💡 Coup de pouce
> Bilan sur l'axe vertical : poussée, poids. Supposez l'accélération constante et la vitesse initiale nulle. Pour (c), demandez-vous quelles grandeurs ont été supposées constantes.


> [!success]- ✅ Correction
> (a) $a=F/m-g\approx4{,}44~\mathrm{m\,s^{-2}}$ ; (b) $v=at\approx26{,}6$ m/s au lieu de $33{,}5$ m/s (écart $\approx20\%$) ; (c) masse et poussée ne sont pas constantes.


> [!example]- 📝 Solution détaillée
> **(a) Accélération**
>
> Système : l'ensemble navette $+$ réservoirs $+$ propulseurs. Forces : poussée $F\,\vec u_z$, poids $-mg\,\vec u_z$. Projection sur $Oz$ : $F-mg=ma$, donc
> $$a=\frac Fm-g=\frac{2{,}85\times10^7}{2{,}0\times10^6}-9{,}81=14{,}25-9{,}81\approx\boxed{4{,}4~\mathrm{m\,s^{-2}}}.$$
> Le rapport poussée/poids vaut $F/(mg)\approx1{,}45$.
>
> **(b) Vitesse après 6 s**
>
> Accélération constante, départ du repos : $v=at\approx4{,}44\times6{,}0\approx\boxed{26{,}6~\mathrm{m/s}}$, soit environ $96$ km/h. Les rapports annoncent $33{,}5$ m/s, soit $\approx26\%$ de plus que ce modèle (écart de $\approx21\%$ par rapport à la valeur annoncée) : **le modèle simple ne reproduit pas la valeur rapportée**.
>
> **(c) Explication de l'écart**
>
> Le modèle suppose $m$ et $F$ constantes, ce qui est faux :
>
>
> - **la masse diminue** : la navette brûle plusieurs tonnes d'ergols par seconde, donc $a=F/m-g$ augmente au cours du temps ;
> - **la poussée varie** : elle dépend de la pression ambiante, donc de l'altitude, et du régime des moteurs ;
> - les chiffres de départ sont arrondis : $a$ est une petite différence de grands nombres ($14{,}25-9{,}81$), donc très sensible à $\pm2\%$ sur $F$ ou $m$.
>
>
> **Ordre de grandeur** : pour obtenir $\bar a=33{,}5/6\approx5{,}6~\mathrm{m\,s^{-2}}$, il faudrait une masse moyenne $\bar m=F/(g+\bar a)\approx1{,}85\times10^6$ kg, soit $\approx150$ t perdues en moyenne : la perte de masse seule est insuffisante (consommation de l'ordre de dix tonnes par seconde), donc la variation de poussée et l'imprécision des données jouent aussi.


> [!warning]- 🪤 Écueils classiques
> **Oublier le poids**
>
> $a=F/m=14{,}25~\mathrm{m\,s^{-2}}$ est faux : l'accélération réelle vaut $F/m-g=4{,}44~\mathrm{m\,s^{-2}}$. Le rapport poussée/poids est ici $\approx1{,}45$.
>
> **Conclure « le rapport de presse est faux »**
>
> Un écart entre modèle et mesure montre les limites du modèle, pas forcément une erreur de mesure. La question (c) demande précisément d'expliquer l'écart.


> [!tip]- 🎙️ Conseils d'animation
> **Estimer l'ordre de grandeur de la perte de masse**
>
> Demander : « de combien la masse doit-elle diminuer en moyenne pour obtenir la vitesse annoncée ? » Comparer à la consommation réelle de l'ordre de dix tonnes par seconde : l'effet de la masse seul est insuffisant, donc la poussée varie aussi.


> [!note]- 🔗 Liens avec d'autres disciplines
> **Astronautique**
>
> Rapport poussée/poids au décollage (de $1{,}2$ à $1{,}5$ pour les lanceurs), étagement, équation de Tsiolkovski.
>
> **Esprit critique et sciences**
>
> Confronter un modèle à une mesure et identifier les hypothèses en cause est la base de la démarche expérimentale.


> [!success]- 🏁 Bilan
> **Un modèle simple a des limites**
>
> Poussée et masse constantes : $a\approx4{,}44~\mathrm{m\,s^{-2}}$ et $v(6~\mathrm s)\approx26{,}6~\mathrm{m/s}$, soit $20\%$ de moins que les $33{,}5~\mathrm{m/s}$ annoncés. L'accélération moyenne annoncée est $5{,}58~\mathrm{m\,s^{-2}}$.


> [!question]- 🔭 Aller plus loin — Licence : Fusée à masse variable
> Avec un débit massique $D$ constant d'éjection de gaz à la vitesse $u$ relative à la fusée, la poussée vaut $F=Du$ et $m(t)=m_0-Dt$. Montrer que $\dfrac{\mathrm dv}{\mathrm dt}=\dfrac{Du}{m_0-Dt}-g$ et intégrer : $v(t)=-u\ln\Big(1-\dfrac{Dt}{m_0}\Big)-gt$ (équation de Tsiolkovski avec gravité).


> [!question]- 🔭 Aller plus loin — Master : Vitesse de satellisation
> Pour une fusée à étage unique de rapport de masses $m_0/m_f=10$ et $u=3{,}0$ km/s, estimer le gain de vitesse $u\ln(m_0/m_f)$ et le comparer à la vitesse orbitale basse ($7{,}8$ km/s) : pourquoi utilise-t-on des fusées à étages ?


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex1-exercices-elementaires|Exercice 1 — Exercices élémentaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex3-machine-d-atwood|Exercice 3 — Machine d'Atwood]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex7-chute-avec-frottement-fluide-vitesse-limite|Exercice 7 — Chute avec frottement fluide : vitesse limite]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex4-systeme-pendule-bloc|Exercice 4 — (*) Système pendule-bloc]] · [[physique/IPSA/ipsa-mecanique-point/Mini-Projet/application-a-la-propulsion-spatiale/mini-projet-phv111-conservation-de-la-quantite-de-mouvement-et-equation-de-tsiolkovski/ex5-seance-2-equation-de-tsiolkovski-propulsion-par-ejection-de-masse|Exercice 5 — Séance 2 -- Équation de Tsiolkovski : propulsion par éjection de masse]]

