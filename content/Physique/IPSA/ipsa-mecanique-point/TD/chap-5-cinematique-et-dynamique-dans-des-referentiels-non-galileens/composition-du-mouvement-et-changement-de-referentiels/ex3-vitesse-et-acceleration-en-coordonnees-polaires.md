---
title: "Exercice 3 — Vitesse et accélération en coordonnées polaires"
tags:
  - td
  - chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/index|⬅ Retour]] · <a href="/pdfs/td7_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td7_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 3. Vitesse et accélération en coordonnées polaires

*⭐ Indispensable · Difficulté ●●●●○ · ⏱ 40 min · Type : Démonstration générale*

Dans un plan fixe $Oxy$, on considère un système d'axes mobiles $OXY$, de même origine $O$, tel que $OX$ fasse avec $Ox$ un angle variable $\theta(t)$. Un point $M$ mobile sur l'axe $OX$ est repéré par $\overrightarrow{OM}=X\,\vec e_X$. Le mouvement **relatif** de $M$ est son mouvement par rapport à $OXY$, le mouvement **absolu** son mouvement par rapport à $Oxy$.


> [!question]- 🪝 Accroche
> **D'où vient le terme $2\dot r\dot\theta$ ?**
>
> *Durée de l'introduction : 3 min*
>
> *Un écureuil court sur le rayon d'une roue qui tourne. Combien de termes dans son accélération absolue et d'où viennent-ils ?*
>
> **Idée clé : l'accélération polaire est la somme de l'accélération relative, de l'accélération d'entraînement (deux termes) et de Coriolis.**




> [!abstract]- 🧠 À savoir avant
> **Dérivée des vecteurs de base mobiles**
>
> $\dot{\vec e}_X=\dot\theta\,\vec e_Y$, $\dot{\vec e}_Y=-\dot\theta\,\vec e_X$. Vecteur rotation $\vec\Omega=\dot\theta\,\vec e_z$.
>
> **Composition des vitesses et accélérations**
>
> $\vec v_a=\vec v_r+\vec v_e$ ; $\vec a_a=\vec a_r+\vec a_e+\vec a_c$ avec $\vec a_c=2\vec\Omega\wedge\vec v_r$.
>
> **Coordonnées polaires**
>
> $\vec v=\dot r\,\vec e_r+r\dot\theta\,\vec e_\theta$ ; $\vec a=(\ddot r-r\dot\theta^2)\vec e_r+(r\ddot\theta+2\dot r\dot\theta)\vec e_\theta$.




> [!info]- 🎯 Ce que tu sauras faire
> **Calculer $\vec v_r,\vec a_r,\vec v_e,\vec a_e,\vec a_c$ dans un cas général**
>
> Savoir appliquer méthodiquement les formules de composition pour un point sur un axe tournant, et retrouver l'accélération en coordonnées polaires.
>
> **Reconnaître les termes de l'accélération polaire**
>
> Identifier $-r\dot\theta^2$ (centripète d'entraînement), $r\ddot\theta$ (tangentielle d'entraînement), $2\dot r\dot\theta$ (Coriolis), $\ddot r$ (relative).




> [!tip]- 📖 Rappel de cours
> **Rotation d'axe fixe non uniforme**
>
> $\vec\Omega=\dot\theta\vec e_z$, $\dfrac{\mathrm d\vec\Omega}{\mathrm dt}=\ddot\theta\vec e_z$. $\vec a_e=\ddot\theta\,\vec e_z\wedge\overrightarrow{OM}+\vec\Omega\wedge(\vec\Omega\wedge\overrightarrow{OM})=X\ddot\theta\,\vec e_Y-X\dot\theta^2\,\vec e_X$.




> [!note]- 🧮 Outils mathématiques
> **Dérivée de $\vec e_X$ et $\vec e_Y$**
>
> $\vec e_X=\cos\theta\,\vec e_x+\sin\theta\,\vec e_y$, $\vec e_Y=-\sin\theta\,\vec e_x+\cos\theta\,\vec e_y$, donc $\dot{\vec e}_X=\dot\theta\vec e_Y$, $\dot{\vec e}_Y=-\dot\theta\vec e_X$.
>
> **Produit vectoriel**
>
> $\vec e_z\wedge\vec e_X=\vec e_Y$, $\vec e_z\wedge\vec e_Y=-\vec e_X$.



**q1.** - [(a)] Établir l'expression de la vitesse et de l'accélération **relatives** de $M$ selon les axes $OXY$.
- [(b)] Déterminer la vitesse et l'accélération d'**entraînement** selon les axes $OXY$.
- [(c)] Déterminer l'accélération complémentaire (de Coriolis).
- [(d)] En déduire $\vec v_a$ et $\vec a_a$ ; vérifier avec la formule polaire.


> [!tip]- 💡 Coup de pouce
> (a) $\vec e_X$ est constant dans $OXY$. (b) Fixer $M$ dans $OXY$ : mouvement circulaire de rayon $X$, de vitesse angulaire $\dot\theta$ non constante. (c) $\vec a_c=2\vec\Omega\wedge\vec v_r$ avec $\vec\Omega=\dot\theta\vec e_z$.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex1-vitesse-d-entrainement|Exercice 1 — Vitesse d'entraînement]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex2-traversee-d-une-riviere|Exercice 2 — Traversée d'une rivière]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex4-mouvement-sur-un-manege|Exercice 4 — Mouvement sur un manège]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex5-bille-sur-une-sphere-angle-de-decollage|Exercice 5 — (*) Bille sur une sphère : angle de décollage]]


