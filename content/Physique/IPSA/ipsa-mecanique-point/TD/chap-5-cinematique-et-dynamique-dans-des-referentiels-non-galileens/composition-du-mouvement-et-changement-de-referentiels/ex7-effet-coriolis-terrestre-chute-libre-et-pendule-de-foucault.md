---
title: "Exercice 7 — Effet Coriolis terrestre : chute libre et pendule de Foucault"
tags:
  - td
  - chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/index|⬅ Retour]]

### Exercice 7. Effet Coriolis terrestre : chute libre et pendule de Foucault *(facultatif)*

On étudie des mouvements à la surface de la Terre à la latitude $\lambda=48{,}85^\circ$ N (Paris). Le référentiel terrestre $\mathcal R'$ tourne autour de l'axe des pôles à la vitesse angulaire $\Omega=7{,}292\times10^{-5}\ {\rm rad\cdot s^{-1}}$ par rapport au référentiel géocentrique $\mathcal R$, supposé galiléen. On utilise le repère local $(O,\vec e_x,\vec e_y,\vec e_z)$ : $\vec e_x$ vers l'est, $\vec e_y$ vers le nord, $\vec e_z$ vertical ascendant. On prend $g=9{,}81\ {\rm m\cdot s^{-2}}$ (**pesanteur effective**, qui inclut déjà le terme centrifuge) et on néglige $\Omega^2$ devant $\Omega$ pour les effets de Coriolis.

**q1.** Un corps de masse $m$ est lâché sans vitesse initiale d'une hauteur $h=100$ m.


- [(a)] Écrire l'équation du mouvement dans $\mathcal R'$ et projeter $-2\vec\Omega\wedge\vec v_r$ sur $(\vec e_x,\vec e_y,\vec e_z)$.
- [(b)] Résoudre à l'ordre 0 puis à l'ordre 1 en $\Omega$ ; en déduire la déviation vers l'est $x(t)$.
- [(c)] Calculer la durée de chute et la déviation pour $h=100$ m à $\lambda=48{,}85^\circ$.

> [!tip]- 💡 Coup de pouce
> (a) $\vec\Omega=\Omega(\cos\lambda\vec e_y+\sin\lambda\vec e_z)$. (b) À l'ordre 0, $\vec v_0=-gt\,\vec e_z$ ; reporter dans le terme de Coriolis.


**q2.** - [(d)] Un obus est tiré horizontalement à $v=500$ m/s (vers l'est) : calculer la déviation latérale après $t=40$ s (on néglige la chute et les frottements).
- [(e)] Pendule de Foucault : le pendule oscille dans le plan horizontal avec une petite amplitude. Écrire les équations du mouvement horizontal (en négligeant $\ddot z$, $\dot z$) et montrer que le plan d'oscillation tourne à la vitesse angulaire $-\Omega\sin\lambda$.
- [(f)] Calculer la période de rotation du plan à Paris, et la rotation par heure ; comparer au pôle Nord et à l'équateur.

> [!tip]- 💡 Coup de pouce
> (d) Pour $\vec v=v\vec e_x$ (vers l'est), $-2\vec\Omega\wedge\vec v$ a pour composante horizontale $-2\Omega v\sin\lambda\,\vec e_y$ : force vers la droite du mouvement, donc vers le sud. (e) Équations : $\ddot x=-\omega_0^2x+2\Omega\sin\lambda\,\dot y$, $\ddot y=-\omega_0^2y-2\Omega\sin\lambda\,\dot x$. Poser $\zeta=x+\mathrm iy$. (f) $T=T_{\rm sid}/\sin\lambda$.

