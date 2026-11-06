---
title: "Exercice 4 — Système de deux blocs"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 4. Système de deux blocs

Deux blocs de masses $m_A=4$ kg et $m_B=5$ kg sont reliés par une corde passant par une poulie fixée au sommet d'un bloc triangulaire dont les faces sont inclinées de $\alpha=30^\circ$ (face portant $A$) et $\beta=60^\circ$ (face portant $B$). On néglige tous les frottements ainsi que les masses de la corde et de la poulie, la corde est inextensible, et on prendra $g=10~\mathrm{m\,s^{-2}}$. Le système est initialement au repos ; les blocs sont lâchés à $t=0$.

**q1.** - [(a)] Citer et représenter sur la figure les forces qui s'exercent sur le bloc $A$ et sur le bloc $B$.
- [(b)] Pour chaque bloc, tracer un repère et donner les composantes des forces.
- [(c)] Relier le déplacement $s_A$ du bloc $A$ au déplacement $s_B$ du bloc $B$. En déduire la relation entre les accélérations.

> [!tip]- 💡 Coup de pouce
> Pour chaque bloc, prenez un axe $Ox$ le long de la pente, orienté dans le sens du mouvement présumé (A monte, B descend), et un axe $Oy$ perpendiculaire.


> [!success]- ✅ Correction
> Forces : poids, réaction normale, tension. Composantes selon la pente : $A$ : $(T-m_Ag\sin\alpha,\ N_A-m_Ag\cos\alpha)$ ; $B$ : $(m_Bg\sin\beta-T,\ N_B-m_Bg\cos\beta)$. $s_A=s_B$ donc $a_A=a_B=a$.


> [!example]- 📝 Solution détaillée
> **(a) Forces**
>
> Chaque bloc subit trois forces : son poids $m\vec g$ (vertical), la réaction normale $\vec N$ de la face (perpendiculaire à la face, pas de frottement), la tension $\vec T$ de la corde (le long de la face, vers la poulie). La tension a la même norme $T$ pour A et B.
>
> **(b) Repères et composantes**
>
> Pour chaque bloc : axe $Ox_i$ le long de la pente dans le sens du mouvement présumé ($A$ vers le haut de sa pente, $B$ vers le bas de la sienne), $Oy_i$ perpendiculaire à la pente. Composantes :
> $$A:\ \vec T\,(T,\,0),\quad m_A\vec g\,(-m_Ag\sin\alpha,\,-m_Ag\cos\alpha),\quad\vec N_A\,(0,\,N_A).$$
> $$B:\ \vec T\,(-T,\,0),\quad m_B\vec g\,(m_Bg\sin\beta,\,-m_Bg\cos\beta),\quad\vec N_B\,(0,\,N_B).$$
>
> **(c) Contrainte du fil**
>
> La corde est inextensible : si $A$ monte de $s_A$ le long de sa pente, $B$ descend de la même longueur $s_B$ le long de la sienne :
> $$\boxed{s_A=s_B}\ \Rightarrow\ \boxed{a_A=a_B=a}.$$


**q2.** - [(d)] Énoncer le principe fondamental de la dynamique et l'appliquer à chaque bloc.
- [(e)] Déterminer l'accélération des deux blocs.
- [(f)] En déduire la tension de la corde.
- [(g)] Quelle est la vitesse des blocs lorsqu'ils se sont déplacés d'une distance $d=40$ cm ?

> [!tip]- 💡 Coup de pouce
> Projetez la 2\textsuperscript{e} loi sur l'axe de la pente pour chaque bloc, avec la même accélération $a$. Additionnez les deux équations pour éliminer $T$.


> [!success]- ✅ Correction
> $a=g\dfrac{m_B\sin\beta-m_A\sin\alpha}{m_A+m_B}\approx2{,}59~\mathrm{m\,s^{-2}}$ ; $T=m_A(g\sin\alpha+a)\approx30{,}4$ N ; $v=\sqrt{2ad}\approx1{,}44~\mathrm{m/s}$.


> [!example]- 📝 Solution détaillée
> **(d) Principe fondamental**
>
> Dans un référentiel galiléen, pour un point matériel de masse $m$ : $\sum\vec F=m\vec a$. Projeté sur $Ox_i$ :
> $$A:\ T-m_Ag\sin\alpha=m_Aa,\qquad B:\ m_Bg\sin\beta-T=m_Ba .$$
> Selon $Oy_i$ : $N_A=m_Ag\cos\alpha$ et $N_B=m_Bg\cos\beta$ (pas de mouvement perpendiculaire).
>
> **(e) Accélération**
>
> On additionne les deux équations : $m_Bg\sin\beta-m_Ag\sin\alpha=(m_A+m_B)a$, donc
> $$a=g\,\frac{m_B\sin\beta-m_A\sin\alpha}{m_A+m_B}=10\times\frac{5\times0{,}866-4\times0{,}5}{9}=\boxed{2{,}59~\mathrm{m\,s^{-2}}}.$$
> $a>0$ confirme le sens supposé : $B$ descend, $A$ monte.
>
> **(f) Tension**
>
> $T=m_A(g\sin\alpha+a)=4\times(5+2{,}59)\approx\boxed{30{,}4~\text{N}}$. Vérification avec $B$ : $m_B(g\sin\beta-a)=5\times(8{,}66-2{,}59)\approx30{,}4$ N. $\surd$ On a bien $20~\text{N}<T<43{,}3~\text{N}$.
>
> **(g) Vitesse après $d=40$ cm**
>
> Départ du repos, accélération constante : $v^2=2ad$, donc
> $$v=\sqrt{2\times2{,}59\times0{,}40}\approx\boxed{1{,}44~\mathrm{m/s}}.$$


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex1-exercices-elementaires|Exercice 1 — Exercices élémentaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex3-machine-d-atwood|Exercice 3 — Machine d'Atwood]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex7-chute-avec-frottement-fluide-vitesse-limite|Exercice 7 — Chute avec frottement fluide : vitesse limite]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]]

