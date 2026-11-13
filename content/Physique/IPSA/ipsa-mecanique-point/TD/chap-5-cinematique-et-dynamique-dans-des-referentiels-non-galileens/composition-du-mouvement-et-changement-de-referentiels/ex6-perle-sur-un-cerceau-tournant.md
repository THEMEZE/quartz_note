---
title: "Exercice 6 — Perle sur un cerceau tournant"
tags:
  - td
  - chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/index|⬅ Retour]]

### Exercice 6. Perle sur un cerceau tournant *(facultatif)*

Une perle $M$ de masse $m=50$ g, assimilée à un point, peut glisser **sans frottement** sur un cerceau circulaire de rayon $R=20$ cm. Le cerceau, dans un plan vertical, tourne à vitesse angulaire **constante** $\omega$ autour de son diamètre vertical $Oz$ (ascendant). On repère la perle par l'angle $\theta=(-\vec e_z,\overrightarrow{OM})$ avec la verticale descendante ; $g=9{,}81\ {\rm m\cdot s^{-2}}$. On étudie le mouvement dans le référentiel $\mathcal R'$ du cerceau (tournant), $\mathcal R$ étant le laboratoire (galiléen).

**q1.** - [(a)] Faire le bilan des forces dans $\mathcal R'$ sur la perle. Exprimer $\vec F_{ie}$ et $\vec F_{ic}$ en fonction de $\theta$ et $\dot\theta$.
- [(b)] Établir l'équation du mouvement $R\ddot\theta=\sin\theta\,(R\omega^2\cos\theta-g)$.
- [(c)] Retrouver cette équation par l'énergie : écrire l'énergie potentielle effective $E_{p,\rm eff}(\theta)$ et l'intégrale première.

> [!tip]- 💡 Coup de pouce
> (a) $\vec F_{ie}=m\omega^2\rho\vec e_\rho$ avec $\rho=R\sin\theta$. $\vec v_r=R\dot\theta\vec e_\theta$. (b) Projeter sur $\vec e_\theta=\cos\theta\vec e_\rho+\sin\theta\vec e_z$. (c) $E_m'=\tfrac12mv_r^2+E_p-\tfrac12m\omega^2\rho^2$.


**q2.** - [(d)] Déterminer les positions d'équilibre relatif. Montrer qu'il existe une vitesse critique $\omega_c$ à exprimer et calculer.
- [(e)] Étudier la stabilité de $\theta=0$ selon $\omega$. Calculer la pulsation des petites oscillations pour $\omega=5$ rad/s, puis le taux de croissance de l'instabilité pour $\omega=10$ rad/s.
- [(f)] Pour $\omega=10$ rad/s, calculer $\theta_0$ et la pulsation des petites oscillations autour de $\theta_0$.

> [!tip]- 💡 Coup de pouce
> (d) $\ddot\theta=0$ : $\sin\theta=0$ ou $\cos\theta=g/(R\omega^2)$ (nécessite $g/(R\omega^2)\le1$). (e), (f) Poser $\theta=\theta_0+\delta$ et linéariser : $\ddot\delta=f'(\theta_0)\delta$ avec $f=\dfrac1R\sin\theta(R\omega^2\cos\theta-g)$.


**q3.** - [(g)] Exprimer les composantes $N_r$ et $N_\varphi$ de la réaction. Calculer $N_r$ à l'équilibre en $\theta_0$ ($\omega=10$ rad/s) et à l'équilibre en $\theta=0$ ($\omega<\omega_c$).
- [(h)] La perle, lâchée sans vitesse relative juste après le bas ($\theta\approx0^+$) pour $\omega=10$ rad/s, atteint un angle maximal $\theta_m$. Calculer $\theta_m$.

> [!tip]- 💡 Coup de pouce
> (g) Projeter sur $\vec e_r$ et $\vec e_\varphi$ ; $\vec e_\rho\cdot\vec e_r=\sin\theta$, $\vec e_z\cdot\vec e_r=-\cos\theta$. (h) Conservation de $E_m'$ avec $E_m'(\theta\approx0)=-mgR$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/ex5-pendule-dans-un-wagon-accelere|Exercice 5 — Pendule dans un wagon accéléré]]

