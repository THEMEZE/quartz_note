---
title: "Exercice 3 — Machine d'Atwood"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 3. Machine d'Atwood

La machine d'Atwood est constituée de deux masses $m_1$ et $m_2$ ($m_2>m_1$) reliées par un fil passant par une poulie. On néglige les masses de la poulie et du fil, on suppose le fil inextensible, la poulie sans frottement, et on prendra $g=9{,}81~\mathrm{m\,s^{-2}}$. À $t=0$, les masses sont lâchées sans vitesse.

**q1.** - [(a)] Pour chaque masse, tracer un repère et représenter les forces.
- [(b)] Appliquer le principe fondamental à chaque masse et le projeter sur les axes choisis.

> [!tip]- 💡 Coup de pouce
> Chaque masse subit son poids et la tension du fil. Choisissez le même axe vertical ascendant pour les deux (une seule contrainte cinématique à écrire ensuite).


> [!success]- ✅ Correction
> $T-m_1g=m_1a_1$ et $T-m_2g=m_2a_2$ (axe $Oz$ ascendant pour les deux).


> [!example]- 📝 Solution détaillée
> **(a) Schéma et forces**
>
> Pour chaque masse $i\in\{1,2\}$ : repère $(O_i,\vec u_z)$ vertical ascendant. Forces : poids $-m_ig\,\vec u_z$ et tension $T\,\vec u_z$ (fil au-dessus de la masse, même norme $T$ des deux côtés de la poulie idéale).
>
> **(b) Principe fondamental**
>
> $$m_1:\ T-m_1g=m_1a_1,\qquad m_2:\ T-m_2g=m_2a_2 .$$


**q2.** - [(c)] Déterminer les accélérations $a_1$ et $a_2$ des masses.
- [(d)] En déduire la distance parcourue à l'instant $t$ par les deux masses.
- [(e)] Quelle est la tension du fil ?
- [(f)] Que devient l'accélération $a_2$ pour $m_2\gg m_1$ ?

> [!tip]- 💡 Coup de pouce
> Le fil est inextensible : si $m_1$ monte de $\delta$, $m_2$ descend de $\delta$. En déduire la relation entre $a_1$ et $a_2$, puis soustraire les deux équations.


> [!success]- ✅ Correction
> $a_1=-a_2=\dfrac{m_2-m_1}{m_1+m_2}\,g$ ; $d=\tfrac12a\,t^2$ ; $T=\dfrac{2m_1m_2}{m_1+m_2}\,g$ ; $a_2\to-g$ (chute libre).


> [!example]- 📝 Solution détaillée
> **(c) Accélérations**
>
> Fil inextensible : $z_1+z_2=\text{cte}$, donc $a_2=-a_1$. En soustrayant les deux équations de (b) pour éliminer $T$ :
> $$-(m_2-m_1)g=m_2a_2-m_1a_1=-(m_1+m_2)a_1\Rightarrow\boxed{a_1=\frac{m_2-m_1}{m_1+m_2}\,g},\qquad\boxed{a_2=-a_1}.$$
> $m_1$ monte avec l'accélération $a=\dfrac{m_2-m_1}{m_1+m_2}\,g<g$, $m_2$ descend avec la même norme. Pour $m_1=m_2$ : $a=0$ (équilibre indifférent).
>
> **(d) Distance parcourue**
>
> Départ du repos : $v=at$ et
> $$\boxed{d(t)=\tfrac12\,a\,t^2=\frac12\,\frac{m_2-m_1}{m_1+m_2}\,g\,t^2}$$
> (montée de $m_1$, descente de $m_2$ de la même distance).
>
> **(e) Tension du fil**
>
> $T=m_1(g+a_1)=m_1g\Big(1+\frac{m_2-m_1}{m_1+m_2}\Big)=\boxed{\dfrac{2m_1m_2}{m_1+m_2}\,g}$. On vérifie $m_1g<T<m_2g$ ; pour $m_1=m_2=m$, $T=mg$ (équilibre).
>
> **(f) Cas $m_2\gg m_1$**
>
> $a\to g$ et $a_2\to-g$ : $m_2$ est en chute libre, le fil n'a plus d'effet sur elle. La tension tend vers $T\to2m_1g$ (la masse $m_1$ est accélérée à $+g$ vers le haut). La machine est un « ralentisseur » de chute libre dans le cas $m_2\approx m_1$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex1-exercices-elementaires|Exercice 1 — Exercices élémentaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex7-chute-avec-frottement-fluide-vitesse-limite|Exercice 7 — Chute avec frottement fluide : vitesse limite]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]]

