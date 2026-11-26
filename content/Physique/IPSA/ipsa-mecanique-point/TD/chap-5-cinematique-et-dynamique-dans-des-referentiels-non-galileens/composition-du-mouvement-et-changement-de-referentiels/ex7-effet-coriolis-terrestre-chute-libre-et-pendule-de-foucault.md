---
title: "Exercice 7 — Effet Coriolis terrestre : chute libre et pendule de Foucault"
tags:
  - td
  - chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-5-cinematique-et-dynamique-dans-des-referentiels-non-galileens/composition-du-mouvement-et-changement-de-referentiels/index|⬅ Retour]] · <a href="/pdfs/td7_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td7_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 7. Effet Coriolis terrestre : chute libre et pendule de Foucault *(facultatif)*

*Difficulté ●●●●● · ⏱ 1 h · Type : Complément original / Référentiel terrestre*

On étudie des mouvements à la surface de la Terre à la latitude $\lambda=48{,}85^\circ$ N (Paris). Le référentiel terrestre $\mathcal R'$ tourne autour de l'axe des pôles à la vitesse angulaire $\Omega=7{,}292\times10^{-5}\ {\rm rad\cdot s^{-1}}$ par rapport au référentiel géocentrique $\mathcal R$, supposé galiléen. On utilise le repère local $(O,\vec e_x,\vec e_y,\vec e_z)$ : $\vec e_x$ vers l'est, $\vec e_y$ vers le nord, $\vec e_z$ vertical ascendant. On prend $g=9{,}81\ {\rm m\cdot s^{-2}}$ (**pesanteur effective**, qui inclut déjà le terme centrifuge) et on néglige $\Omega^2$ devant $\Omega$ pour les effets de Coriolis.


> [!question]- 🪝 Accroche
> **Une pierre lâchée du haut d'une tour tombe-t-elle exactement au pied de la tour ?**
>
> *Durée de l'introduction : 3 min*
>
> *Newton, Hooke puis Reich ont tenté l'expérience : la pierre tombe légèrement à l'est. Pourquoi, et de combien pour une tour de 100 m ?*
>
> **Idée clé : la Terre est un référentiel tournant.** Dans $\mathcal R'$ un corps en mouvement subit $-2m\vec\Omega\wedge\vec v_r$ ; la déviation est faible (cm) mais mesurable.




> [!abstract]- 🧠 À savoir avant
> **Vecteur rotation dans le repère local**
>
> $\vec\Omega=\Omega\,(\cos\lambda\,\vec e_y+\sin\lambda\,\vec e_z)$.
>
> **Force de Coriolis**
>
> $\vec F_{ic}=-2m\,\vec\Omega\wedge\vec v_r$.
>
> **Produit vectoriel en composantes**
>
> $\vec e_x\wedge\vec e_y=\vec e_z$, $\vec e_y\wedge\vec e_z=\vec e_x$, $\vec e_z\wedge\vec e_x=\vec e_y$.




> [!info]- 🎯 Ce que tu sauras faire
> **Calculer une déviation par perturbation**
>
> Savoir intégrer l'équation du mouvement à l'ordre 1 en $\Omega$ (la trajectoire d'ordre 0 est celle sans rotation).
>
> **Interpréter les effets de Coriolis terrestres**
>
> Déviation vers l'est d'un corps qui tombe, vers la droite pour une trajectoire horizontale (hémisphère Nord), rotation du plan d'oscillation du pendule de Foucault.




> [!tip]- 📖 Rappel de cours
> **Équation du mouvement**
>
> $\dfrac{\mathrm d\vec v_r}{\mathrm dt}=\vec g+\dfrac{\vec F}{m}-2\vec\Omega\wedge\vec v_r$.
>
> **Composantes de Coriolis**
>
> Pour $\vec v=(v_x,v_y,v_z)$ : $-2\vec\Omega\wedge\vec v=2\Omega\big(v_y\sin\lambda-v_z\cos\lambda,\ -v_x\sin\lambda,\ v_x\cos\lambda\big)$.
>
> **Ordres de grandeur**
>
> $2\Omega v\approx1{,}5\times10^{-4}\,v$ (m/s²) : négligeable pour des mouvements courts ($t\ll1/\Omega\approx3{,}8$ h) ; important pour les masses d'air (cyclones), les courants marins, la balistique à longue portée.




> [!note]- 🧮 Outils mathématiques
> **Intégration successive**
>
> $\ddot x=2\Omega gt\cos\lambda\Rightarrow\dot x=\Omega gt^2\cos\lambda\Rightarrow x=\tfrac13\Omega gt^3\cos\lambda$.
>
> **Notation complexe**
>
> $\zeta=x+\mathrm iy$ transforme le système couplé du pendule en une seule équation.
>
> **Développement perturbatif**
>
> $\vec r=\vec r_0+\Omega\vec r_1+\dots$



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


