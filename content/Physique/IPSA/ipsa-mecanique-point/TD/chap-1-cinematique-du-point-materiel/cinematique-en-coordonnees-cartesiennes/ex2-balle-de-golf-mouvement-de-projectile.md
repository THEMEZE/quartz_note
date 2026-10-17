---
title: "Exercice 2 — Balle de golf (mouvement de projectile)"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · <a href="/pdfs/td1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td1_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 2. Balle de golf (mouvement de projectile)

On se place dans le référentiel terrestre, supposé galiléen, d'intensité de pesanteur $g=9{,}81$ S.I.,
muni d'un repère cartésien $Oxz$ (le mouvement se faisant dans le plan vertical, $y(t)=0$ à tout instant).
Les équations horaires d'une balle de golf lancée à $t=0$ avec la vitesse initiale $\vec v_0$ faisant un
angle $\alpha$ avec l'horizontale sont :
$$x(t) = v_0\cos(\alpha)\,t, \qquad y(t)=0, \qquad z(t) = -\frac{1}{2}g\,t^2 + v_0\sin(\alpha)\,t.$$

**q1.** - [(a)] Déterminer l'équation de la trajectoire de la balle et la représenter sur un graphique.
- [(b)] Déterminer l'expression du vecteur vitesse $\vec v$ de la balle. Représenter $\vec v_0$ et l'angle $\alpha$ sur le graphique.
- [(c)] Comment évolue la vitesse suivant $Ox$ ? suivant $Oz$ ?

> [!tip]- 💡 Coup de pouce
> Isolez $t$ dans $x(t)$ et reportez dans $z(t)$, comme dans l'exercice précédent.


> [!success]- ✅ Correction
> $z(x) = x\tan\alpha - \dfrac{g}{2v_0^2\cos^2\alpha}x^2$ : parabole. $v_x$ constant, $v_z$ affine décroissante (change de signe au sommet).


> [!example]- 📝 Solution détaillée
> **(a) Équation de la trajectoire**
>
> De $x(t) = v_0\cos\alpha\, t$, on tire $t = x/(v_0\cos\alpha)$. En reportant dans $z(t)$ :
> $$z(x) = -\frac{1}{2}g\left(\frac{x}{v_0\cos\alpha}\right)^2 + v_0\sin\alpha \cdot \frac{x}{v_0\cos\alpha} = \boxed{x\tan\alpha - \frac{g}{2v_0^2\cos^2\alpha}\,x^2}.$$
> C'est une **parabole**, passant par l'origine, tournée vers le bas (coefficient de $x^2$ négatif), de tangente à l'origine de pente $\tan\alpha$ (conforme au fait que la balle part avec un angle $\alpha$).
>
> **(b) Vecteur vitesse**
>
> En dérivant chaque coordonnée :
> $$\boxed{\vec v(t) = v_0\cos\alpha\,\vec u_x + (v_0\sin\alpha - g\,t)\,\vec u_z}.$$
> À $t=0$ : $\vec v(0) = v_0\cos\alpha\,\vec u_x + v_0\sin\alpha\,\vec u_z = v_0(\cos\alpha\,\vec u_x + \sin\alpha\,\vec u_z)$, vecteur de norme $v_0$ faisant l'angle $\alpha$ avec $Ox$ — on le représente tangent à la trajectoire à l'origine.
>
> **(c) Évolution des composantes de la vitesse**
>
> $v_x(t) = v_0\cos\alpha$ est **constante** : le mouvement est uniforme suivant $Ox$ (aucune force horizontale).
>
> $v_z(t) = v_0\sin\alpha - gt$ est **affine décroissante** : le mouvement est uniformément décéléré tant que $v_z>0$ (montée), s'annule au sommet de la trajectoire (flèche), puis devient négatif (la balle redescend, accélérée vers le bas).


**q2.** - [(d)] Donner l'expression de l'altitude maximale $h$ atteinte par la balle (la flèche) et de la portée horizontale $d$ du tir.
- [(e)] Pour quelle valeur de $\alpha$ la portée est-elle maximale ?
- [(f)] Montrer qu'une même portée peut être atteinte pour deux valeurs différentes de $\alpha$.

> [!tip]- 💡 Coup de pouce
> La flèche est atteinte quand $v_z=0$ ; la portée correspond au second instant où $z=0$ (l'autre que $t=0$).


> [!success]- ✅ Correction
> $h=\dfrac{v_0^2\sin^2\alpha}{2g}$, $d=\dfrac{v_0^2\sin(2\alpha)}{g}$ ; portée max pour $\alpha=45°$ ; $d(\alpha)=d(90°-\alpha)$.


> [!example]- 📝 Solution détaillée
> **(d) Flèche**
>
> La flèche est atteinte à l'instant $t^\star$ tel que $v_z(t^\star)=0$, soit $t^\star = v_0\sin\alpha/g$. En reportant dans $z(t)$ :
> $$h = z(t^\star) = -\frac{1}{2}g\left(\frac{v_0\sin\alpha}{g}\right)^2 + v_0\sin\alpha\cdot\frac{v_0\sin\alpha}{g} = \boxed{\frac{v_0^2\sin^2\alpha}{2g}}.$$
>
> **(d) Portée**
>
> La portée correspond à l'instant $t_d\neq 0$ tel que $z(t_d)=0$ :
> $$z(t)=t\left(v_0\sin\alpha - \frac{1}{2}gt\right)=0 \quad\Longrightarrow\quad t_d = \frac{2v_0\sin\alpha}{g}.$$
> D'où :
> $$d = x(t_d) = v_0\cos\alpha \cdot \frac{2v_0\sin\alpha}{g} = \boxed{\frac{v_0^2\sin(2\alpha)}{g}} \qquad (\text{en utilisant } 2\sin\alpha\cos\alpha=\sin(2\alpha)).$$
>
> **(e) Angle de portée maximale**
>
> À $v_0$ fixé, $d(\alpha)$ est maximale quand $\sin(2\alpha)=1$, c'est-à-dire $2\alpha = 90°$, soit :
> $$\boxed{\alpha = 45°}.$$
>
> **(f) Deux angles pour une même portée**
>
> On utilise l'identité $\sin(180°-2\alpha) = \sin(2\alpha)$. Ainsi, pour un angle $\alpha' = 90°-\alpha$, on a $\sin(2\alpha') = \sin(180°-2\alpha)=\sin(2\alpha)$, donc :
> $$d(\alpha') = \frac{v_0^2\sin(2\alpha')}{g} = \frac{v_0^2\sin(2\alpha)}{g} = d(\alpha).$$
> Les angles $\alpha$ et $90°-\alpha$ (complémentaires) donnent donc la même portée — l'un correspondant à un tir tendu (angle faible), l'autre à un tir plus haut (angle proche de la verticale), à la même vitesse initiale $v_0$.


**q3.** - [(g)] Une balle de golf tapée avec une vitesse oblique retombe à une distance $d_T=340$ m du joueur, sur Terre. À quelle distance $d_L$ du joueur retomberait une balle tapée dans les mêmes conditions de lancement, mais sur la Lune, où $g_L=1{,}6$ m/s² ?

> [!tip]- 💡 Coup de pouce
> "Mêmes conditions de lancement" signifie même $v_0$ et même $\alpha$. Utilisez l'expression de la portée $d=v_0^2\sin(2\alpha)/g$ pour comparer directement les deux situations sans recalculer $v_0$ ni $\alpha$.


> [!success]- ✅ Correction
> $d_L = d_T\,g_T/g_L \approx 2{,}08$ km.


> [!example]- 📝 Solution détaillée
> **Mise à l'échelle par le rapport des $g$**
>
> D'après la formule générale établie en (d), $d = v_0^2\sin(2\alpha)/g$. Comme $v_0$ et $\alpha$ sont **identiques** dans les deux situations (mêmes conditions de lancement), le produit $v_0^2\sin(2\alpha)$ est le même sur Terre et sur la Lune. On peut donc écrire, sans connaître ni $v_0$ ni $\alpha$ individuellement :
> $$d_T\,g_T = v_0^2\sin(2\alpha) = d_L\,g_L \quad\Longrightarrow\quad d_L = d_T\,\frac{g_T}{g_L}.$$
>
> **Application numérique**
>
> $$d_L = 340 \times \frac{9{,}81}{1{,}6} \approx 340 \times 6{,}13 \approx \boxed{2085~\text{m} \approx 2{,}08~\text{km}}.$$
> La balle irait donc presque 6,1 fois plus loin sur la Lune que sur Terre — un ordre de grandeur cohérent avec les images des astronautes d'Apollo 14 frappant des balles de golf sur la Lune. (En pratique, l'absence d'atmosphère lunaire supprime aussi les frottements de l'air, ce qui augmenterait encore un peu plus la portée réelle par rapport à ce facteur purement gravitationnel.)


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex6-parabole-de-s-rete-et-tir-sur-une-pente|Exercice 6 — Parabole de sûreté et tir sur une pente]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex7-balle-rebondissante-et-paradoxe-de-zenon|Exercice 7 — Balle rebondissante et paradoxe de Zénon]]

