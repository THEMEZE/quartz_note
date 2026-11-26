---
title: "Exercice 4 — Mouvement sur un manège"
tags:
  - td
  - chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/index|⬅ Retour]] · <a href="/pdfs/td7_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td7_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 4. Mouvement sur un manège

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 40 min · Type : Cours actif / Application fondamentale*

Un manège pour enfants tourne à une vitesse angulaire constante $\omega>0$ par rapport au sol. Le propriétaire (point $M$) parcourt la plate-forme pour ramasser les tickets. $\mathcal R$ est le référentiel du sol (repère $(Oxyz)$, base $(\vec e_x,\vec e_y,\vec e_z)$), $\mathcal R'$ celui du manège (repère $(Ox'y'z')$, base $(\vec e_x{}',\vec e_y{}',\vec e_z{}')$) ; les origines et les axes $Oz$, $Oz'$ coïncident (axe de rotation). Partant du centre à $t=0$, le propriétaire suit un mouvement uniforme de vitesse $v_0$ le long de l'axe $Ox'$ du manège.


> [!question]- 🪝 Accroche
> **Pourquoi un enfant marchant du centre vers le bord d'un manège est-il « tiré de côté » ?**
>
> *Durée de l'introduction : 3 min*
>
> *Quelle force tire l'enfant de côté ? Existe-t-elle vraiment, ou est-ce un effet de point de vue ?*
>
> **Idée clé : un mouvement rectiligne dans le manège devient une spirale dans le sol.** L'accélération perpendiculaire ($2\omega v_0$) est celle de Coriolis.




> [!abstract]- 🧠 À savoir avant
> **Rotation uniforme**
>
> $\vec\Omega=\omega\vec e_z$, $\theta=\omega t$ ; $\dot{\vec e}_x{}'=\omega\vec e_y{}'$, $\dot{\vec e}_y{}'=-\omega\vec e_x{}'$.
>
> **Composition des vitesses et accélérations**
>
> $\vec v_a=\vec v_r+\vec v_e$ ; $\vec a_a=\vec a_r+\vec a_e+\vec a_c$.
>
> **Résultat de l'exercice 3**
>
> Pour un point sur un axe tournant : $\vec a_e=-X\dot\theta^2\vec e_X+X\ddot\theta\vec e_Y$, $\vec a_c=2\dot X\dot\theta\vec e_Y$.




> [!info]- 🎯 Ce que tu sauras faire
> **Caractériser le mouvement de $\mathcal R'$ par rapport à $\mathcal R$**
>
> Savoir que c'est une rotation uniforme de vecteur $\vec\Omega=\omega\vec e_z$.
>
> **Trajectoire relative et absolue**
>
> Savoir que la trajectoire est une droite dans $\mathcal R'$ mais une spirale d'Archimède dans $\mathcal R$.
>
> **Calculer $\vec v_a$ et $\vec a_a$**
>
> Savoir appliquer les lois de composition en rotation uniforme et exprimer le résultat dans la base du manège.




> [!tip]- 📖 Rappel de cours
> **Rotation uniforme**
>
> $\vec v_e=\vec\Omega\wedge\overrightarrow{OM}$, $\vec a_e=-\omega^2\,\overrightarrow{HM}$ (ici $H=O$ si $M$ est dans le plan), $\vec a_c=2\vec\Omega\wedge\vec v_r$.




> [!note]- 🧮 Outils mathématiques
> **Dérivation dans une base tournante**
>
> $\dfrac{\mathrm d}{\mathrm dt}(t\,\vec e_x{}')=\vec e_x{}'+\omega t\,\vec e_y{}'$.
>
> **Spirale d'Archimède**
>
> $r=a\theta$ avec $a=v_0/\omega$ ; pas de la spirale $2\pi a$.



**q1.** - [(a)] Quelle grandeur caractérise le mouvement de $\mathcal R'$ par rapport à $\mathcal R$ ?
- [(b)] Partant du centre à $t=0$, $M$ suit un mouvement uniforme de vitesse $v_0$ le long de $Ox'$. Quelle est la nature de sa trajectoire par rapport à $\mathcal R'$ ? Déterminer son équation horaire $\vec r(t)=\overrightarrow{OM}(t)$ dans $\mathcal R'$, puis sa vitesse relative $\vec v_r$ dans la base $(\vec e_x{}',\vec e_y{}',\vec e_z{}')$.


> [!tip]- 💡 Coup de pouce
> (a) Le référentiel $\mathcal R'$ tourne autour de l'axe commun $Oz$ à vitesse angulaire constante. (b) Dans $\mathcal R'$, la base $(\vec e_x{}',\vec e_y{}',\vec e_z{}')$ est fixe.



**q2.** Étude du mouvement dans le référentiel absolu $\mathcal R$.


- [(c)] Rappeler la loi de composition des vitesses. En déduire $\vec v_a$ dans la base $(\vec e_x{}',\vec e_y{}',\vec e_z{}')$.
- [(d)] Rappeler la loi de composition des accélérations. En déduire $\vec a_a$.
- [(e)] Retrouver $\vec v_a$ et $\vec a_a$ par un calcul direct dans $\mathcal R$ (dériver $\overrightarrow{OM}$ dans $\mathcal R$).
- [(f)] Écrire l'équation polaire de la trajectoire dans $\mathcal R$. Application numérique : $v_0=1$ m/s, $\omega=2$ rad/s, valeurs de $\vec v_a$, $\vec a_a$ et de leurs normes à $t=2$ s.


> [!tip]- 💡 Coup de pouce
> (c) $\vec v_e=\vec\Omega\wedge\overrightarrow{OM}$. (d) $\vec a_e=-\omega^2\overrightarrow{OM}$, $\vec a_c=2\vec\Omega\wedge\vec v_r$. (e) Dériver $\overrightarrow{OM}=v_0t\,\vec e_x{}'$ dans $\mathcal R$ avec $\dot{\vec e}_x{}'=\omega\vec e_y{}'$.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex1-vitesse-d-entrainement|Exercice 1 — Vitesse d'entraînement]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex2-traversee-d-une-riviere|Exercice 2 — Traversée d'une rivière]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex3-vitesse-et-acceleration-en-coordonnees-polaires|Exercice 3 — Vitesse et accélération en coordonnées polaires]]


