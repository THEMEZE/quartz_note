---
title: "Exercice 9 — Dérivée d'un vecteur unitaire tournant"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · <a href="/pdfs/td1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td1_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 9. Dérivée d'un vecteur unitaire tournant

On se place dans l'espace muni d'un repère cartésien $Oxyz$ et d'une base cartésienne $(\vec\imath,\vec\jmath,\vec k)$.
Dans le plan $Oxy$, on considère deux vecteurs unitaires perpendiculaires $\vec u$ et $\vec v$, placés en $O$, tels que
$(\vec u,\vec v,\vec k)$ forme un trièdre direct. On note $\theta$ l'angle entre $\vec u$ et l'axe $(Ox)$.
L'objectif est d'établir l'expression des dérivées $\mathrm{d}\vec u/\mathrm{d}\theta$ et $\mathrm{d}\vec v/\mathrm{d}\theta$.

**q1.** (a) Sur un graphique, représenter le repère $(Oxy)$ et les vecteurs de la base cartésienne $\vec\imath$ et $\vec\jmath$.

(b) Représenter les vecteurs $\vec u$ et $\vec v$ ainsi que l'angle $\theta$ dans le repère $(O,\vec\imath,\vec\jmath)$.

> [!tip]- 💡 Coup de pouce
> $\vec v$ doit être en avance de $90°$ sur $\vec u$ dans le sens trigonométrique, pour que $(\vec u,\vec v,\vec k)$ soit direct.


> [!success]- ✅ Correction
> Schéma : $\vec u$ à l'angle $\theta$ de $Ox$, $\vec v$ à l'angle $\theta+90°$ de $Ox$.


> [!example]- 📝 Solution détaillée
> **Représentation graphique**
>
> On trace le repère $(O,\vec\imath,\vec\jmath)$ orthonormé, puis le vecteur unitaire $\vec u$ faisant l'angle $\theta$ (compté positivement dans le sens trigonométrique) avec $\vec\imath$. Le vecteur $\vec v$, unitaire et perpendiculaire à $\vec u$, est tracé de sorte que $(\vec u, \vec v)$ tourne dans le même sens que $(\vec\imath,\vec\jmath)$ (condition de trièdre direct) : $\vec v$ est donc obtenu en faisant tourner $\vec u$ de $+90°$, il fait l'angle $\theta+90°$ avec $\vec\imath$.


**q2.** (a) [(c)] Exprimer les vecteurs $\vec u$ et $\vec v$ dans la base cartésienne $(\vec\imath,\vec\jmath)$ en fonction de $\theta$ (composantes suivant $Ox$ et $Oy$).

(b) [(d)] Calculer les dérivées des vecteurs $\vec u$ et $\vec v$ par rapport à $\theta$.

.

> [!tip]- 💡 Coup de pouce
> Pour (c), projetez géométriquement $\vec u$ et $\vec v$ sur $\vec\imath$ et $\vec\jmath$. Pour (d), dérivez composante par composante puisque $(\vec\imath,\vec\jmath)$ est fixe.


> [!success]- ✅ Correction
> $\vec u=\cos\theta\,\vec\imath+\sin\theta\,\vec\jmath$, $\vec v=-\sin\theta\,\vec\imath+\cos\theta\,\vec\jmath$ ; $\mathrm{d}\vec u/\mathrm{d}\theta=\vec v$, $\mathrm{d}\vec v/\mathrm{d}\theta=-\vec u$.


> [!example]- 📝 Solution détaillée
> **(c) Décomposition cartésienne de $\vec u$ et $\vec v$**
>
> Le vecteur $\vec u$, unitaire, faisant l'angle $\theta$ avec $\vec\imath$, a pour projections orthogonales sur $\vec\imath$ et $\vec\jmath$ respectivement $\cos\theta$ et $\sin\theta$ (définition du cosinus et du sinus) :
> $$\boxed{\vec u = \cos\theta\,\vec\imath + \sin\theta\,\vec\jmath}.$$
> Le vecteur $\vec v$ fait l'angle $\theta+90°$ avec $\vec\imath$, donc ses projections sont $\cos(\theta+90°)=-\sin\theta$ et $\sin(\theta+90°)=\cos\theta$ :
> $$\boxed{\vec v = -\sin\theta\,\vec\imath + \cos\theta\,\vec\jmath}.$$
> On vérifie la cohérence à $\theta=0$ : $\vec u=\vec\imath$ et $\vec v=\vec\jmath$, ce qui correspond bien au trièdre de référence $(\vec\imath,\vec\jmath,\vec k)$, direct.
>
> **(d) Dérivées par rapport à $\theta$**
>
> La base $(\vec\imath,\vec\jmath)$ étant fixe, on dérive directement chaque composante par rapport à $\theta$ :
> $$\frac{\mathrm{d}\vec u}{\mathrm{d}\theta} = -\sin\theta\,\vec\imath + \cos\theta\,\vec\jmath = \boxed{\vec v}.$$
> $$\frac{\mathrm{d}\vec v}{\mathrm{d}\theta} = -\cos\theta\,\vec\imath - \sin\theta\,\vec\jmath = -\big(\cos\theta\,\vec\imath+\sin\theta\,\vec\jmath\big) = \boxed{-\vec u}.$$
> On retiendra ces deux résultats fondamentaux, qui seront systématiquement réutilisés (avec $\vec u\to\vec u_r$ et $\vec v\to\vec u_\theta$) dès l'introduction des coordonnées polaires : dériver un vecteur unitaire tournant par rapport à son angle revient à lui faire subir une rotation de $+90°$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex6-parabole-de-s-rete-et-tir-sur-une-pente|Exercice 6 — Parabole de sûreté et tir sur une pente]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]]

