---
title: "Exercice 3 — Machine d'Atwood"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td4_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 3. Machine d'Atwood

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 40 min · Type : Application / Fondamental*

La machine d'Atwood est constituée de deux masses $m_1$ et $m_2$ ($m_2>m_1$) reliées par un fil passant par une poulie. On néglige les masses de la poulie et du fil, on suppose le fil inextensible, la poulie sans frottement, et on prendra $g=9{,}81~\mathrm{m\,s^{-2}}$. À $t=0$, les masses sont lâchées sans vitesse.


> [!question]- 🪝 Accroche
> **Ralentir la chute pour la mesurer**
>
> *Durée de l'introduction : 3 min*
>
> *Au XVIII\textsuperscript{e} siècle, la chute libre est trop rapide pour être mesurée précisément. Comment **ralentir** une chute, sans changer la gravité ? Que se passe-t-il si les deux masses sont presque égales ? Et si l'une est énorme ?*
>
> **Idée clé : deux masses liées partagent la même accélération (en norme).** L'accélération est $a=\dfrac{m_2-m_1}{m_1+m_2}\,g$ : elle est d'autant plus petite que les masses sont proches. Le fil transmet une tension $T$ comprise entre $m_1g$ et $m_2g$.




> [!abstract]- 🧠 À savoir avant
> **Fil idéal sur une poulie idéale**
>
> Pour un fil sans masse passant sur une poulie sans masse ni frottement, la tension a la même norme $T$ en tout point du fil. Un fil inextensible impose que les déplacements des deux extrémités soient égaux et opposés : $z_1+z_2=\text{cte}$.




> [!info]- 🎯 Ce que tu sauras faire
> **Traiter un système lié par un fil**
>
> Savoir isoler chaque masse, choisir un repère pour chacune, écrire la 2\textsuperscript{e} loi, traduire l'inextensibilité du fil par une relation entre accélérations, résoudre le système et vérifier les cas limites.




> [!info]- 🧑‍🏫 Objectifs pédagogiques
> **L'exercice type de système lié**
>
> Deux équations de Newton plus une contrainte cinématique donnent trois relations pour trois inconnues ($a_1,a_2,T$). La difficulté est dans **la contrainte** $a_1=-a_2$ avec axes verticaux ascendants identiques. Insister sur la discussion des cas limites ($m_1=m_2$, $m_2\gg m_1$) comme contrôle du résultat.




> [!tip]- 📖 Rappel de cours
> **Méthode pour un système de solides liés**
>
> On isole **chaque** solide, on écrit sa 2\textsuperscript{e} loi, et on ajoute les relations de liaison (fil inextensible, contact). Si l'on choisit un axe $Oz$ vertical ascendant commun, l'inextensibilité donne $a_1=-a_2$.




> [!note]- 🧮 Outils mathématiques
> **Résolution d'un système linéaire**
>
> Deux équations $T-m_1g=m_1a_1$, $T-m_2g=m_2a_2$ avec $a_2=-a_1$ : on soustrait pour éliminer $T$.
>
> **Mouvement uniformément accéléré**
>
> Départ du repos : $v=at$, $d=\tfrac12at^2$.
>
> **Étude de cas limites**
>
> $m_1=m_2\Rightarrow a=0$ ; $m_1\to0\Rightarrow a\to g$, $T\to0$ ; $m_2\gg m_1\Rightarrow a\to g$, $T\to2m_1g$. Un résultat doit passer ces tests.



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




> [!note]- 🔗 Liens avec d'autres disciplines
> **Histoire des sciences**
>
> George Atwood (1784) a conçu cette machine pour mesurer $g$ avec les horloges de l'époque.
>
> **Ingénierie**
>
> Ascenseurs avec contrepoids, grues à contrepoids, funiculaires : même principe, on équilibre une masse par une autre pour réduire la force motrice.




> [!warning]- 🪤 Écueils classiques
> **Penser que $T=m_1g$ ou $T=m_2g$**
>
> Les masses accélèrent : $T$ est comprise strictement entre $m_1g$ et $m_2g$. $T=m_1g$ n'est vrai qu'à l'équilibre.
>
> **Oublier le signe de la contrainte**
>
> Avec deux axes ascendants, si $m_1$ monte, $m_2$ descend : $a_1=-a_2$. Se tromper de signe conduit à $a=0$ ou à $a=\dfrac{(m_1+m_2)g}{m_2-m_1}$.
>
> **Une tension différente de chaque côté**
>
> Pour une poulie idéale (sans masse, sans frottement), la tension est la même de chaque côté. Cette hypothèse tombe pour une poulie de masse non nulle (voir « aller plus loin »).




> [!tip]- 🎙️ Conseils d'animation
> **Manipulation**
>
> Avec deux masses marquées et un chronomètre, mesurer le temps de chute de $1$ m pour $m_2=m_1+\Delta m$ : $g$ en est déduit avec $g=\dfrac{(m_1+m_2)\,2d}{(m_2-m_1)\,t^2}$. C'est l'expérience d'Atwood (1784) qui permettait de « ralentir » la chute libre.




> [!success]- 🏁 Bilan pédagogique
> **Résultats de la machine d'Atwood**
>
> $a_2=-a_1=-\dfrac{m_2-m_1}{m_1+m_2}\,g$ (descente de $m_2$) ; $T=\dfrac{2m_1m_2}{m_1+m_2}\,g$ ; $d=\tfrac12\dfrac{m_2-m_1}{m_1+m_2}\,g\,t^2$. Si $m_2\gg m_1$ : $a\to g$ (chute libre de $m_2$), $T\to2m_1g$.




> [!question]- 🔭 Aller plus loin — CPGE : Poulie de masse non négligeable
> Pour une poulie de moment d'inertie $J$ et de rayon $r$, les tensions diffèrent de chaque côté. Montrer, avec le théorème du moment cinétique, que $a=\dfrac{(m_2-m_1)g}{m_1+m_2+J/r^2}$.




> [!question]- 🔭 Aller plus loin — Licence : Mesure de $g$ et incertitudes
> Avec $g=\dfrac{(m_1+m_2)}{(m_2-m_1)}\dfrac{2d}{t^2}$, estimer l'incertitude sur $g$ pour $d=1{,}00\pm0{,}01$ m, $t=2{,}0\pm0{,}1$ s, et $m_2-m_1$ connue à $1\%$ : quelle grandeur domine ?




> [!question]- 🔭 Aller plus loin — Master : Atwood avec frottement visqueux sur le fil
> Ajouter un frottement fluide $-\lambda v$ sur chaque masse. Établir l'équation différentielle de $v(t)$, montrer qu'il existe une vitesse limite $v_\ell=\dfrac{(m_2-m_1)g}{2\lambda}$ et tracer $v(t)$.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex1-exercices-elementaires|Exercice 1 — Exercices élémentaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex7-chute-avec-frottement-fluide-vitesse-limite|Exercice 7 — Chute avec frottement fluide : vitesse limite]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex4-systeme-pendule-bloc|Exercice 4 — (*) Système pendule-bloc]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex5-pendule-balistique|Exercice 5 — (*) Pendule balistique]]


