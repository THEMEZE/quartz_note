---
title: "Exercice 3 — Circuit de Monaco : courbure et accélération à vitesse constante"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td3_PhV111_corrige.pdf) · [📄 Énoncé](/pdfs/td3_PhV111_enonces.pdf) · [📄 Aides](/pdfs/td3_PhV111_aides.pdf) · [📄 Fiche enseignant](/pdfs/td3_PhV111_fiche.pdf)

### Exercice 3. Circuit de Monaco : courbure et accélération à vitesse constante *(facultatif)*

On s'intéresse aux voitures qui roulent sur le circuit de Monaco, représenté sur le plan fourni (figure du TD).
Lors d'une phase de test, une automobile parcourt le circuit avec une vitesse de norme $\|\vec v\|$
**constante**. On considère la norme de l'accélération $a=\|\vec a\|$ de l'automobile aux virages 9 (Tunnel), 15 et
16 (Rascasse), notée respectivement $a_9$, $a_{15}$ et $a_{16}$.

**q1.** Laquelle des affirmations suivantes est vraie ?


(a) $a_9=a_{15}=a_{16}=0$

(b) $a_9=a_{15}=a_{16}=k$, $k$ constante non nulle

(c) $a_9<a_{15}<a_{16}$

(d) $a_9<a_{16}<a_{15}$

(e) $a_{15}<a_9<a_{16}$

(f) $a_{15}<a_{16}<a_9$

(g) $a_{16}<a_9<a_{15}$

(h) $a_{16}<a_{15}<a_9$

> [!tip]- 💡 Coup de pouce
> La vitesse est constante en norme. Que devient alors $\dot v$ ? Quelle composante de l'accélération reste ? De quelle grandeur géométrique dépend-elle ?


> [!success]- ✅ Correction
> $a=a_N=v^2/R$ : classer les accélérations revient à classer les $1/R$. Le Tunnel (virage 9) est large donc $a_9$ est la plus petite des trois ; l'ordre entre $a_{15}$ et $a_{16}$ se lit sur les rayons des cercles osculateurs tracés sur le plan : (c) si $R_{15}>R_{16}$, (d) si $R_{16}>R_{15}$. **À vérifier sur le plan fourni.**


> [!example]- 📝 Solution détaillée
> **Raisonnement**
>
> Comme $\|\vec v\|=$ cte, $a_T=\dot v=0$, donc $\vec a=\dfrac{v^2}R\,\vec n$ avec $a=\dfrac{v^2}R$. Les options (a) et (b) sont à écarter : (a) car $R$ est fini en un virage, (b) car $R$ diffère d'un virage à l'autre. L'accélération est **inversement proportionnelle au rayon de courbure**, donc **d'autant plus grande que le virage est serré**.
>
> On compare donc les rayons de courbure aux trois virages. Le virage 9 (Tunnel) est un virage large (grand rayon) : $a_9$ est la plus petite. Il reste à départager les virages 15 et 16 (Rascasse), plus serrés, en comparant les rayons des cercles osculateurs tracés (question 3). Le plus serré des deux a la plus grande accélération.
>
> **Remarque pour l'enseignant :** le rang exact dépend de la figure ; avec la numérotation et le tracé du plan d'origine, la réponse attendue est une des options (c) ou (d) ; elle doit être confirmée en traçant les cercles osculateurs sur le plan utilisé en séance.


**q2.** Justifier votre réponse.

> [!tip]- 💡 Coup de pouce
> Écrivez $\vec a$ dans la base de Frenet en annulant le terme tangentiel. Reliez ensuite le rayon de courbure à la forme de la trajectoire : une courbe serrée est-elle proche d'un petit ou d'un grand cercle ?


> [!success]- ✅ Correction
> $\vec a=\dfrac{v^2}R\,\vec n$ ; $a$ est proportionnelle à $1/R$ ; classement par comparaison des rayons des cercles osculateurs.


> [!example]- 📝 Solution détaillée
> **Justification**
>
> Dans la base de Frenet, $\vec a=\dot v\,\vec\tau+\dfrac{v^2}R\,\vec n$. Pour $\|\vec v\|=$ cte, seule la composante normale subsiste :
> $$a_9=\frac{v^2}{R_9},\quad a_{15}=\frac{v^2}{R_{15}},\quad a_{16}=\frac{v^2}{R_{16}}.$$
> $v$ étant la même, $a_i<a_j\iff R_i>R_j$. L'ordre des accélérations est l'**ordre inverse** des rayons de courbure. Un rayon grand correspond à un virage « ouvert » (le Tunnel, pris à grande vitesse) ; un rayon petit correspond à un virage serré (la Rascasse, qui est une épingle). **Ordres de grandeur** : $R_9\sim100$ à $200\ \mathrm m$ et $R_{16}\sim15$ à $25\ \mathrm m$ donnent, à $v=100\ \mathrm{km/h}\approx28\ \mathrm{m/s}$, $a_9\approx4$ à $8\ \mathrm{m\,s^{-2}}$ et $a_{16}\approx30$ à $50\ \mathrm{m\,s^{-2}}$ ($3$ à $5\,g$), valeurs que seule une voiture de course peut tenir (grâce à l'appui aérodynamique) : en pratique, la voiture **ralentit** dans l'épingle, ce qui est le sujet de l'exercice 7.


**q3.** Tracer approximativement, sur le circuit de Monaco, les cercles osculateurs aux points 9 (Tunnel), 15 et 16 (Rascasse) de la trajectoire.

> [!tip]- 💡 Coup de pouce
> En chaque point : tracez la tangente, puis la normale côté concave ; cherchez le cercle tangent à la trajectoire qui la suit le mieux sur un petit arc.


> [!success]- ✅ Correction
> Grand cercle (rayon $R_9$) au virage 9 ; cercles plus petits aux virages 15 et 16, de centre du côté intérieur de chaque virage.


> [!example]- 📝 Solution détaillée
> **Construction**
>
> Pour chaque point : (1) tracer la tangente à la trajectoire ; (2) tracer la normale, perpendiculaire, vers l'**intérieur du virage** ; (3) choisir sur cette normale le point $C$ tel que le cercle de centre $C$ passant par le point d'étude **épouse** la trajectoire de part et d'autre (en testant avec le compas) ; (4) tracer le cercle. On obtient un **grand cercle** au Tunnel (courbure faible) et des **petits cercles** aux virages 15 et 16 (courbure forte). Le rayon se lit avec l'échelle. Aux virages en épingle, le cercle osculateur est à peu près inscrit dans la largeur de la piste.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex1-base-de-frenet-demonstrations-de-cours-et-applications|Exercice 1 — Base de Frenet : démonstrations de cours et applications]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex2-mouvement-curviligne-uniforme-cercle-parabole-applications|Exercice 2 — Mouvement curviligne uniforme : cercle, parabole, applications]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex4-abscisse-curviligne-et-rayon-de-courbure-d-une-trajectoire-parabolique|Exercice 4 — Abscisse curviligne et rayon de courbure d'une trajectoire parabolique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex5-cycloide-point-d-une-roue-qui-roule-sans-glisser|Exercice 5 — Cycloïde : point d'une roue qui roule sans glisser]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex6-raccordement-routier-en-clothoide-courbure-variable-et-jerk|Exercice 6 — Raccordement routier en clothoïde (courbure variable et « jerk »)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex7-cercle-d-adherence-freiner-et-tourner-en-meme-temps|Exercice 7 — Cercle d'adhérence : freiner et tourner en même temps]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex8-tir-parabolique-vu-dans-la-base-de-frenet|Exercice 8 — Tir parabolique vu dans la base de Frenet]]

