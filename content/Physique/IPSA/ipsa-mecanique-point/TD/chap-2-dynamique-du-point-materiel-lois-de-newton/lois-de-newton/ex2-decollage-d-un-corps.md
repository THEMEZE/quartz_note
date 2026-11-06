---
title: "Exercice 2 — Décollage d'un corps"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 2. Décollage d'un corps

Un corps de masse $m$ repose sur un plan horizontal et subit une force $\vec F$ dont la norme varie suivant la loi $F(t)=kt$, avec $k$ une constante positive. La force forme un angle $\alpha$ constant avec le plan (dirigée vers le haut et vers l'avant) et commence à agir à $t=0$, le corps étant au repos. On néglige les frottements et on prendra $g=9{,}81~\mathrm{m\,s^{-2}}$. Le repère $Oxy$ est choisi avec $Ox$ horizontal dans le sens de la force et $Oy$ vertical ascendant.

**q1.** - [(a)] Quelle est l'unité de $k$ dans le système international ?
- [(b)] Faire le bilan des forces qui agissent sur le corps et les projeter selon $Ox$ et $Oy$.
- [(c)] Quelle est la condition physique pour que le corps décolle du plan ?
- [(d)] Que peut-on dire de la composante verticale de l'accélération avant le décollage ?
- [(e)] Appliquer le principe fondamental de la dynamique et projeter selon $Ox$ et $Oy$ afin d'obtenir deux équations.

> [!tip]- 💡 Coup de pouce
> $F=kt$ impose les dimensions de $k$. Les forces sont le poids, la réaction normale et $\vec F$ ; le décollage correspond à la perte du contact.


> [!success]- ✅ Correction
> $[k]=\mathrm N\,\mathrm s^{-1}$ ; forces $m\vec g$, $\vec N$, $\vec F$ ; décollage $\Leftrightarrow N=0$ ; $a_y=0$ avant décollage ; $ma_x=kt\cos\alpha$ et $N+kt\sin\alpha-mg=0$.


> [!example]- 📝 Solution détaillée
> **(a) Unité de $k$**
>
> $F=kt$ donc $k=F/t$ : $[k]=\mathrm N\cdot\mathrm s^{-1}=\boxed{\mathrm{kg\,m\,s^{-3}}}$.
>
> **(b) Bilan des forces**
>
> Système : le corps. Référentiel terrestre galiléen. Forces : poids $\vec P=-mg\,\vec u_y$ ; réaction normale $\vec N=N\,\vec u_y$ (pas de frottement) ; force $\vec F$. Projections :
> $$\vec P:\ (0,\,-mg),\qquad\vec N:\ (0,\,N),\qquad\vec F:\ (kt\cos\alpha,\ kt\sin\alpha).$$
>
> **(c) Condition de décollage**
>
> Le plan ne peut que pousser, jamais tirer ($N\ge0$). Le corps quitte le plan quand le contact est rompu : $\boxed{N=0}$.
>
> **(d) Avant le décollage**
>
> Le corps reste sur le plan horizontal : son altitude est constante, donc $v_y=0$ et $\boxed{a_y=0}$.
>
> **(e) Principe fondamental**
>
> $\vec P+\vec N+\vec F=m\vec a$ se projette en
> $$\text{(Ox)}:\ m\,a_x=kt\cos\alpha,\qquad\text{(Oy)}:\ N+kt\sin\alpha-mg=m\,a_y=0 .$$
> On en tire la réaction : $N(t)=mg-kt\sin\alpha$.


**q2.** - [(f)] Donner l'accélération $a(t)$ du corps en fonction des paramètres du problème et en déduire sa vitesse $v(t)$.
- [(g)] Appliquer la condition de décollage pour calculer l'instant $t_d$ du décollage.
- [(h)] En déduire la vitesse au décollage $v(t_d)$.
- [(i)] Quelle est la distance parcourue par le corps jusqu'au décollage ?

> [!tip]- 💡 Coup de pouce
> L'accélération vient de (Ox). Intégrez deux fois en partant du repos. Pour (g), résolvez $N(t_d)=0$ dans l'équation de (Oy).


> [!success]- ✅ Correction
> $a=\dfrac{kt\cos\alpha}m$, $v=\dfrac{k\cos\alpha}{2m}t^2$ ; $t_d=\dfrac{mg}{k\sin\alpha}$ ; $v(t_d)=\dfrac{mg^2\cos\alpha}{2k\sin^2\alpha}$ ; $x(t_d)=\dfrac{m^2g^3\cos\alpha}{6k^2\sin^3\alpha}$.


> [!example]- 📝 Solution détaillée
> **(f) Accélération et vitesse**
>
> $$a(t)=\boxed{\frac{k\cos\alpha}{m}\,t}\quad\Rightarrow\quad v(t)=\int_0^ta\,\mathrm dt'=\boxed{\frac{k\cos\alpha}{2m}\,t^2}\qquad(v(0)=0).$$
>
> **(g) Instant du décollage**
>
> $N(t_d)=0\iff mg-kt_d\sin\alpha=0$, donc $\boxed{t_d=\dfrac{mg}{k\sin\alpha}}$ (valable si $\alpha\ne0$ ; pour $\alpha=0$ il n'y a jamais de décollage).
>
> **(h) Vitesse au décollage**
>
> $$v(t_d)=\frac{k\cos\alpha}{2m}\cdot\frac{m^2g^2}{k^2\sin^2\alpha}=\boxed{\frac{m\,g^2\cos\alpha}{2k\sin^2\alpha}}.$$
>
> **(i) Distance parcourue**
>
> $$x(t)=\int_0^tv\,\mathrm dt'=\frac{k\cos\alpha}{6m}t^3\ \Rightarrow\ x(t_d)=\frac{k\cos\alpha}{6m}\cdot\frac{m^3g^3}{k^3\sin^3\alpha}=\boxed{\frac{m^2g^3\cos\alpha}{6k^2\sin^3\alpha}}.$$
> Contrôle dimensionnel : $\dfrac{\mathrm{kg^2\,(m\,s^{-2})^3}}{(\mathrm{kg\,m\,s^{-3}})^2}=\mathrm m$. $\surd$


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex1-exercices-elementaires|Exercice 1 — Exercices élémentaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex3-machine-d-atwood|Exercice 3 — Machine d'Atwood]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex7-chute-avec-frottement-fluide-vitesse-limite|Exercice 7 — Chute avec frottement fluide : vitesse limite]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]]

