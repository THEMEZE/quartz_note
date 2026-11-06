---
title: "Exercice 7 — Chute avec frottement fluide : vitesse limite"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 7. Chute avec frottement fluide : vitesse limite *(facultatif)*

Une bille de masse $m=50$ g est lâchée sans vitesse initiale dans un fluide visqueux (huile). En plus de son poids, elle subit une force de frottement fluide $\vec f=-\lambda\,\vec v$ avec $\lambda=0{,}50~\mathrm{kg\,s^{-1}}$. On néglige la poussée d'Archimède. On prendra $g=9{,}81~\mathrm{m\,s^{-2}}$. L'axe $Oz$ est vertical **descendant**, l'origine $O$ est le point de lâcher, et $t=0$ est l'instant du lâcher.

**q1.** - [(a)] Établir l'équation différentielle vérifiée par la vitesse $v(t)=\dot z$ de la bille.
- [(b)] Sans résoudre l'équation, déterminer la vitesse limite $v_\ell$ et le temps caractéristique $\tau$. Applications numériques.
- [(c)] Résoudre l'équation avec la condition initiale. Tracer $v(t)$.

> [!tip]- 💡 Coup de pouce
> Avec $Oz$ descendant : poids $+mg$, frottement $-\lambda v$. La vitesse limite correspond à $\mathrm dv/\mathrm dt=0$. Solution de la forme $v=v_\ell+C\mathrm e^{-t/\tau}$.


> [!success]- ✅ Correction
> $m\dot v+\lambda v=mg$ ; $v_\ell=mg/\lambda\approx0{,}98$ m/s, $\tau=m/\lambda=0{,}10$ s ; $v=v_\ell(1-\mathrm e^{-t/\tau})$.


> [!example]- 📝 Solution détaillée
> **(a) Équation différentielle**
>
> Système : la bille. Forces : poids $mg\,\vec u_z$, frottement $-\lambda v\,\vec u_z$. Projection de $m\vec a=\sum\vec F$ sur $Oz$ :
> $$\boxed{m\,\dot v=mg-\lambda v}\iff\dot v+\frac v\tau=g\quad\text{avec}\quad\tau=\frac m\lambda .$$
>
> **(b) Vitesse limite et temps caractéristique**
>
> Vitesse limite : $\dot v=0\Rightarrow\boxed{v_\ell=\dfrac{mg}\lambda}=\dfrac{0{,}050\times9{,}81}{0{,}50}\approx\boxed{0{,}98~\mathrm{m/s}}$. Temps caractéristique : $\boxed{\tau=\dfrac m\lambda}=\dfrac{0{,}050}{0{,}50}=\boxed{0{,}10~\text{s}}$. On a $v_\ell=g\tau$ : la bille atteindrait $v_\ell$ en $\tau$ si l'accélération restait égale à $g$.
>
> **(c) Résolution**
>
> Solution : $v(t)=v_\ell+C\,\mathrm e^{-t/\tau}$. Condition $v(0)=0\Rightarrow C=-v_\ell$ :
> $$\boxed{v(t)=v_\ell\big(1-\mathrm e^{-t/\tau}\big)}.$$
> Courbe : part de $0$ avec la pente $g$ (tangente $v=gt$), croît en concavité vers le bas, tend vers l'asymptote horizontale $v_\ell$. À $t=\tau$ : $63\%$ de $v_\ell$ ($0{,}62$ m/s) ; à $t=0{,}2$ s : $0{,}85$ m/s.


**q2.** - [(d)] Déterminer $z(t)$. Quelle distance la bille a-t-elle parcourue au bout de $0{,}50$ s ?
- [(e)] À quel instant la vitesse atteint-elle $99\%$ de $v_\ell$ ? Quelle distance a été parcourue alors ?
- [(f)] Montrer que pour $t\ll\tau$ on retrouve la chute libre.

> [!tip]- 💡 Coup de pouce
> Intégrez $v(t)$ avec $z(0)=0$. Pour (e), résolvez $\mathrm e^{-t/\tau}=0{,}01$. Pour (f), développez l'exponentielle à l'ordre $2$.


> [!success]- ✅ Correction
> $z(t)=v_\ell\big[t-\tau(1-\mathrm e^{-t/\tau})\big]$ ; $z(0{,}5)\approx0{,}39$ m ; $t_{99}=\tau\ln100\approx0{,}46$ s, $z\approx0{,}35$ m ; $z\approx\tfrac12gt^2$ pour $t\ll\tau$.


> [!example]- 📝 Solution détaillée
> **(d) Position**
>
> $$z(t)=\int_0^tv\,\mathrm dt'=\boxed{v_\ell\Big[t-\tau\big(1-\mathrm e^{-t/\tau}\big)\Big]}.$$
> À $t=0{,}50$ s : $z=0{,}981\times[0{,}50-0{,}10\times(1-\mathrm e^{-5})]\approx0{,}981\times0{,}4007\approx\boxed{0{,}39~\text{m}}$ (contre $1{,}2$ m en chute libre).
>
> **(e) Temps pour atteindre 99 \% de $v_\ell$**
>
> $1-\mathrm e^{-t/\tau}=0{,}99\Rightarrow t_{99}=\tau\ln100\approx\boxed{0{,}46~\text{s}}$. Distance : $z=v_\ell[t_{99}-0{,}99\tau]=0{,}981\times(0{,}4605-0{,}099)\approx\boxed{0{,}35~\text{m}}$. Au-delà, le mouvement est quasi uniforme : environ $v_\ell\Delta t$ de plus par seconde.
>
> **(f) Temps courts : chute libre**
>
> Pour $x=t/\tau\ll1$ : $\mathrm e^{-x}\approx1-x+\dfrac{x^2}2$, d'où $v\approx v_\ell\Big(\dfrac t\tau-\dfrac{t^2}{2\tau^2}\Big)\approx gt$ (car $v_\ell/\tau=g$) et $z\approx v_\ell\dfrac{t^2}{2\tau}=\tfrac12gt^2$. Le frottement est négligeable tant que $t\ll\tau$ : c'est le régime de chute libre.


**q3.** - [(g)] La bille est maintenant lancée **vers le haut** avec la vitesse $v_0=2{,}0~\mathrm{m/s}$ dans le même fluide (axe $Oz$ désormais ascendant). Établir la vitesse $v_z(t)$, l'instant $t_s$ du sommet et la hauteur maximale $h$. Application numérique.
- [(h)] Vérifier que le résultat redonne $h=v_0^2/(2g)$ quand le frottement tend vers $0$ ($\lambda\to0$). Comparer à la valeur numérique sans frottement.

> [!tip]- 💡 Coup de pouce
> Avec $Oz$ ascendant : $m\dot v_z=-mg-\lambda v_z$. Posez $v_\ell=mg/\lambda$ : la solution est $v_z=-v_\ell+(v_0+v_\ell)\mathrm e^{-t/\tau}$. Le sommet est atteint quand $v_z=0$. Pour (h), développez $\ln(1+x)$ à l'ordre $2$.


> [!success]- ✅ Correction
> $t_s=\tau\ln\Big(1+\dfrac{v_0}{v_\ell}\Big)\approx0{,}111$ s ; $h=v_0\tau-v_\ell\tau\ln\Big(1+\dfrac{v_0}{v_\ell}\Big)\approx9{,}1$ cm (contre $20{,}4$ cm sans frottement) ; limite $\lambda\to0$ : $v_0^2/(2g)$.


> [!example]- 📝 Solution détaillée
> **(g) Lancer vers le haut**
>
> Axe ascendant : $m\dot v_z=-mg-\lambda v_z\Rightarrow\dot v_z+\dfrac{v_z}\tau=-g$, solution $v_z=-v_\ell+C\,\mathrm e^{-t/\tau}$ avec $v_z(0)=v_0\Rightarrow C=v_0+v_\ell$ :
> $$v_z(t)=-v_\ell+(v_0+v_\ell)\,\mathrm e^{-t/\tau}.$$
> Sommet : $v_z=0\Rightarrow\mathrm e^{-t_s/\tau}=\dfrac{v_\ell}{v_0+v_\ell}$, soit
> $$\boxed{t_s=\tau\ln\Big(1+\frac{v_0}{v_\ell}\Big)}=0{,}10\times\ln(3{,}04)\approx0{,}111~\text{s}.$$
> Hauteur : $z(t)=-v_\ell t+(v_0+v_\ell)\tau\big(1-\mathrm e^{-t/\tau}\big)$, et en $t_s$, $1-\mathrm e^{-t_s/\tau}=\dfrac{v_0}{v_0+v_\ell}$ :
> $$\boxed{h=v_0\tau-v_\ell\tau\ln\Big(1+\frac{v_0}{v_\ell}\Big)}=0{,}200-0{,}0981\times1{,}112\approx\boxed{0{,}091~\text{m}}.$$
>
> **(h) Limite sans frottement**
>
> Quand $\lambda\to0$, $v_\ell\to\infty$ avec $v_\ell/\tau=g$ fixé, donc $x=v_0/v_\ell\to0$. Avec $\ln(1+x)\approx x-\dfrac{x^2}2$ :
> $$h\approx v_0\tau-v_\ell\tau\Big(\frac{v_0}{v_\ell}-\frac{v_0^2}{2v_\ell^2}\Big)=\frac{v_0^2\tau}{2v_\ell}=\frac{v_0^2}{2g}.\ \surd$$
> Numériquement, sans frottement : $h_0=\dfrac{4}{2\times9{,}81}\approx0{,}204$ m : le frottement visqueux divise la hauteur atteinte par $\approx2{,}2$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex1-exercices-elementaires|Exercice 1 — Exercices élémentaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex3-machine-d-atwood|Exercice 3 — Machine d'Atwood]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]]

