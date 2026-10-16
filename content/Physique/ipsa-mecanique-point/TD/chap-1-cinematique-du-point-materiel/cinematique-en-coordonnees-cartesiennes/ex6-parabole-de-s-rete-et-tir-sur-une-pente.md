---
title: "Exercice 6 — Parabole de sûreté et tir sur une pente"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · <a href="/pdfs/td1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 6. Parabole de sûreté et tir sur une pente *(facultatif)*

Un pompier dispose d'une lance dont le jet sort, au niveau du sol, avec une vitesse de norme fixée $v_0=20~\mathrm{m\,s^{-1}}$ ; il peut
seulement choisir l'angle de tir $\alpha$ du jet avec l'horizontale. On néglige les frottements de l'air et on assimile une particule d'eau à un point matériel en chute libre dans le champ de pesanteur $g=9{,}81~\mathrm{m\,s^{-2}}$.
On choisit un repère $Oxz$ (le mouvement est plan), l'origine $O$ à la sortie de la lance, $Oz$ vertical ascendant. Les équations horaires sont celles de l'exercice « balle de golf » :
$$x(t)=v_0\cos\alpha\;t,\qquad z(t)=-\tfrac12\,g\,t^2+v_0\sin\alpha\;t,$$
d'où l'équation de la trajectoire
$$z(x)=x\tan\alpha-\frac{g\,x^2}{2v_0^2}\,\big(1+\tan^2\alpha\big).$$
Dans tout l'exercice, $v_0$ est fixé et **c'est $\alpha$ qui est l'inconnue**.

**q1.** - [(a)] Montrer que, pour atteindre le point $(x,z)$, l'angle de tir doit vérifier une équation du second degré dont l'inconnue est $u=\tan\alpha$.
- [(b)] À quelle condition sur $z$ (à $x$ fixé) cette équation a-t-elle des solutions réelles ? En déduire l'expression de la parabole de sûreté $z_s(x)$.
- [(c)] Une fenêtre est située à $x=25$ m et $z=10$ m. Peut-on l'atteindre ? Calculer les angles de tir possibles et les durées de vol correspondantes. Comparer les vitesses d'arrivée.

> [!tip]- 💡 Coup de pouce
> Pour (a), partez de $z=x\tan\alpha-\dfrac{g x^2}{2v_0^2}(1+\tan^2\alpha)$ et regroupez les termes en puissances de $u$. Pour (b), calculez $\Delta=B^2-4AC$ et résolvez $\Delta\ge0$ en $z$. Pour la vitesse d'arrivée, pensez à la conservation de l'énergie mécanique.


**q2.** - [(d)] Déterminer les points d'intersection de la parabole de sûreté avec le sol et avec l'axe $Oz$, et leur signification physique.
- [(e)] Pour un point $P(x,z_s(x))$ de la parabole de sûreté, déterminer l'unique angle de tir. Vérifier que la trajectoire correspondante est **tangente** à la parabole de sûreté en $P$.

> [!tip]- 💡 Coup de pouce
> Pour (e), à $\Delta=0$ la racine double est $u=-B/(2A)$. Pour la tangence, comparez la pente $\mathrm dz/\mathrm dx$ de la trajectoire en $P$ avec celle de $z_s$.


**q3.** Le jet est maintenant dirigé vers un talus plan, montant, faisant l'angle $\beta=30^\circ$ avec l'horizontale (le plan du talus contient l'axe $Ox$ et la direction de plus grande pente). On note $d$ la distance, mesurée le long du talus, entre $O$ et le point d'impact.


- [(f)] Exprimer $d$ en fonction de $v_0$, $g$, $\alpha$ et $\beta$.
- [(g)] Déterminer l'angle $\alpha^\star$ qui maximise $d$ et la portée maximale $d_{\max}$ ; application numérique. Que devient le résultat sur un talus **descendant** de même angle ?
- [(h)] Retrouver $d_{\max}$ en utilisant la parabole de sûreté, et interpréter géométriquement $\alpha^\star$.

> [!tip]- 💡 Coup de pouce
> Le point d'impact est sur le talus : $(x,z)=(d\cos\beta,\,d\sin\beta)$. Reportez dans l'équation de trajectoire et simplifiez par $d\ne0$. Utilisez ensuite $2\cos\alpha\sin(\alpha-\beta)=\sin(2\alpha-\beta)-\sin\beta$. Pour (h), cherchez l'intersection de la droite $z=x\tan\beta$ avec $z_s(x)$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex7-balle-rebondissante-et-paradoxe-de-zenon|Exercice 7 — Balle rebondissante et paradoxe de Zénon]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]]

