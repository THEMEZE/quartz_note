---
title: "Exercice 6 — (*) Navette Columbia"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 6. (*) Navette Columbia *(facultatif)*

Lors de son premier vol en 1981, la navette spatiale Columbia faisait partie d'un ensemble de masse $m=2{,}0\times10^6$ kg qui développait une poussée totale $F=2{,}85\times10^7$ N. On suppose le décollage vertical, dans le champ de pesanteur $g=9{,}81~\mathrm{m\,s^{-2}}$ ; la navette est assimilée à un point matériel et on néglige les frottements de l'air.

**q1.** - [(a)] Quelle était l'accélération de l'ensemble à pleine puissance ?
- [(b)] Selon les rapports de presse, $6{,}0$ s après s'être dégagée de la tour de soutien, la navette avait une vitesse de $33{,}5~\mathrm{m\,s^{-1}}$. Vérifier si les rapports sont corrects.
- [(c)] Proposer une explication s'il y a une différence.

> [!tip]- 💡 Coup de pouce
> Bilan sur l'axe vertical : poussée, poids. Supposez l'accélération constante et la vitesse initiale nulle. Pour (c), demandez-vous quelles grandeurs ont été supposées constantes.


> [!success]- ✅ Correction
> (a) $a=F/m-g\approx4{,}44~\mathrm{m\,s^{-2}}$ ; (b) $v=at\approx26{,}6$ m/s au lieu de $33{,}5$ m/s (écart $\approx20\%$) ; (c) masse et poussée ne sont pas constantes.


> [!example]- 📝 Solution détaillée
> **(a) Accélération**
>
> Système : l'ensemble navette $+$ réservoirs $+$ propulseurs. Forces : poussée $F\,\vec u_z$, poids $-mg\,\vec u_z$. Projection sur $Oz$ : $F-mg=ma$, donc
> $$a=\frac Fm-g=\frac{2{,}85\times10^7}{2{,}0\times10^6}-9{,}81=14{,}25-9{,}81\approx\boxed{4{,}4~\mathrm{m\,s^{-2}}}.$$
> Le rapport poussée/poids vaut $F/(mg)\approx1{,}45$.
>
> **(b) Vitesse après 6 s**
>
> Accélération constante, départ du repos : $v=at\approx4{,}44\times6{,}0\approx\boxed{26{,}6~\mathrm{m/s}}$, soit environ $96$ km/h. Les rapports annoncent $33{,}5$ m/s, soit $\approx26\%$ de plus que ce modèle (écart de $\approx21\%$ par rapport à la valeur annoncée) : **le modèle simple ne reproduit pas la valeur rapportée**.
>
> **(c) Explication de l'écart**
>
> Le modèle suppose $m$ et $F$ constantes, ce qui est faux :
>
>
> - **la masse diminue** : la navette brûle plusieurs tonnes d'ergols par seconde, donc $a=F/m-g$ augmente au cours du temps ;
> - **la poussée varie** : elle dépend de la pression ambiante, donc de l'altitude, et du régime des moteurs ;
> - les chiffres de départ sont arrondis : $a$ est une petite différence de grands nombres ($14{,}25-9{,}81$), donc très sensible à $\pm2\%$ sur $F$ ou $m$.
>
>
> **Ordre de grandeur** : pour obtenir $\bar a=33{,}5/6\approx5{,}6~\mathrm{m\,s^{-2}}$, il faudrait une masse moyenne $\bar m=F/(g+\bar a)\approx1{,}85\times10^6$ kg, soit $\approx150$ t perdues en moyenne : la perte de masse seule est insuffisante (consommation de l'ordre de dix tonnes par seconde), donc la variation de poussée et l'imprécision des données jouent aussi.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex1-exercices-elementaires|Exercice 1 — Exercices élémentaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex3-machine-d-atwood|Exercice 3 — Machine d'Atwood]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex7-chute-avec-frottement-fluide-vitesse-limite|Exercice 7 — Chute avec frottement fluide : vitesse limite]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]]

