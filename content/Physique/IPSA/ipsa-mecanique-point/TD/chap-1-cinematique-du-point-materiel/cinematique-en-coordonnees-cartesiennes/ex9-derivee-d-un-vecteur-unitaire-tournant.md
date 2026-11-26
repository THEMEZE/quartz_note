---
title: "Exercice 9 — Dérivée d'un vecteur unitaire tournant"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · <a href="/pdfs/td1_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td1_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/test.pdf" target="_blank" rel="noopener">📄 PDF</a> · <a href="/pdfs/td1_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 9. Dérivée d'un vecteur unitaire tournant

*⭐ Indispensable · Difficulté ●●○○○ · ⏱ 20 min · Type : Cours actif / Fondamental*

On se place dans l'espace muni d'un repère cartésien $Oxyz$ et d'une base cartésienne $(\vec\imath,\vec\jmath,\vec k)$.
Dans le plan $Oxy$, on considère deux vecteurs unitaires perpendiculaires $\vec u$ et $\vec v$, placés en $O$, tels que
$(\vec u,\vec v,\vec k)$ forme un trièdre direct. On note $\theta$ l'angle entre $\vec u$ et l'axe $(Ox)$.
L'objectif est d'établir l'expression des dérivées $\mathrm{d}\vec u/\mathrm{d}\theta$ et $\mathrm{d}\vec v/\mathrm{d}\theta$.


> [!question]- 🪝 Accroche
> **Une base qui tourne avec le mobile**
>
> *Durée de l'introduction : 3 à 5 min, avant de lire l'énoncé*
>
> *Un vecteur de longueur constante, comme l'aiguille d'une horloge, **peut-il avoir une dérivée non nulle** ? Dans quelle direction « pointe » alors cette dérivée ? Et si je vous disais que **deux formules** suffisent à décrire tous les mouvements de rotation de la physique ?*
>
> **Idée clé : dériver un vecteur unitaire tournant revient à le tourner de $+90^\circ$.** Pour $\vec u=\cos\theta\,\vec\imath+\sin\theta\,\vec\jmath$ et $\vec v$ son image par une rotation de $+90^\circ$ :
> $$\frac{\mathrm d\vec u}{\mathrm d\theta}=\vec v,\qquad\frac{\mathrm d\vec v}{\mathrm d\theta}=-\vec u .$$
> Le résultat est **purement géométrique** : il ne dépend d'aucune loi horaire $\theta(t)$. Combiné à la dérivée composée $\dfrac{\mathrm d\vec u}{\mathrm dt}=\dot\theta\,\dfrac{\mathrm d\vec u}{\mathrm d\theta}$, il donne toute la cinématique en coordonnées polaires, cylindriques et sphériques.




> [!abstract]- 🧠 À savoir avant
> **Décomposition d'un vecteur unitaire tournant sur une base fixe**
>
> Tout vecteur unitaire du plan $Oxy$ faisant un angle $\theta$ avec $Ox$ peut s'écrire $\cos\theta\,\vec\imath+\sin\theta\,\vec\jmath$ : c'est la définition même du cosinus et du sinus comme projections orthogonales sur les axes.




> [!info]- 🎯 Ce que tu sauras faire
> **Établir les formules fondamentales de la base polaire**
>
> Savoir redémontrer, à partir de la seule décomposition cartésienne, que $\mathrm{d}\vec u/\mathrm{d}\theta = \vec v$ et $\mathrm{d}\vec v/\mathrm{d}\theta = -\vec u$ : ce résultat, une fois acquis, sera systématiquement réutilisé (sans redémonstration) dès que l'on travaillera en coordonnées polaires ou cylindriques, avec $\vec u = \vec u_r$ et $\vec v=\vec u_\theta$.




> [!info]- 🧑‍🏫 Objectifs pédagogiques
> **Exercice fondateur pour la suite du cours**
>
> Ce court exercice est un prérequis technique incontournable avant d'aborder la cinématique en coordonnées polaires : toute la mécanique des mouvements circulaires ou plus généraux en base $(\vec u_r,\vec u_\theta)$ repose sur ces deux dérivées. Il est important que les étudiants comprennent que ce résultat est **purement géométrique** (il ne dépend d'aucune loi horaire particulière $\theta(t)$) : c'est la brique de base qui sera ensuite combinée à la règle de dérivation en chaîne ($\mathrm{d}\vec u/\mathrm{d}t = \dot\theta\,\mathrm{d}\vec u/\mathrm{d}\theta$) pour traiter des mouvements quelconques.




> [!tip]- 📖 Rappel de cours
> **Trièdre direct**
>
> Un trièdre $(\vec u,\vec v,\vec w)$ est dit direct s'il se déduit du trièdre de référence $(\vec\imath,\vec\jmath,\vec k)$ par une rotation (règle de la main droite / du tire-bouchon) : concrètement, $\vec w = \vec u\wedge\vec v$. Ici, cela impose que $\vec v$ se déduise de $\vec u$ par une rotation de $+90°$ dans le plan $Oxy$ (et non $-90°$).




> [!note]- 🧮 Outils mathématiques
> **Définition de la dérivée comme limite**
>
> $\dfrac{\mathrm d\vec u}{\mathrm d\theta}=\displaystyle\lim_{\Delta\theta\to0}\dfrac{\vec u(\theta+\Delta\theta)-\vec u(\theta)}{\Delta\theta}$. Géométriquement, la variation $\Delta\vec u$ est la corde d'un arc de cercle de rayon $1$ : sa longueur vaut $\approx\Delta\theta$ et sa direction tend vers la **tangente** au cercle, donc perpendiculaire à $\vec u$ : c'est $\vec v$.
>
> **Petits angles**
>
> Pour $\Delta\theta\to0$ : $\sin\Delta\theta\approx\Delta\theta$ et $\cos\Delta\theta\approx1$. On en déduit $\vec u(\theta+\Delta\theta)\approx\vec u+\Delta\theta\,\vec v$, qui redonne la formule sans dériver aucune composante.
>
> **Formules d'addition et décalage de $\pi/2$**
>
> $\cos(\theta+\tfrac\pi2)=-\sin\theta$ et $\sin(\theta+\tfrac\pi2)=\cos\theta$ (cas particulier de $\cos(a+b)=\cos a\cos b-\sin a\sin b$). C'est ce qui fournit les composantes de $\vec v$.
>
> **Dérivées de $\cos$ et $\sin$ ; dérivée composée**
>
> $(\cos\theta)'=-\sin\theta$, $(\sin\theta)'=\cos\theta$ ; et $\dfrac{\mathrm d}{\mathrm dt}f(\theta(t))=\dot\theta\,f'(\theta)$. C'est la **règle de la chaîne**, utilisée pour passer de $\mathrm d/\mathrm d\theta$ à $\mathrm d/\mathrm dt$.
>
> **Norme constante $\Rightarrow$ dérivée orthogonale**
>
> $\|\vec u\|^2=1\Rightarrow2\,\vec u\cdot\dfrac{\mathrm d\vec u}{\mathrm d\theta}=0$. Dans le plan, l'unique direction orthogonale à $\vec u$ est celle de $\vec v$ : la dérivée est donc colinéaire à $\vec v$.
>
> **Produit vectoriel et trièdre direct**
>
> $(\vec u,\vec v,\vec k)$ est direct si $\vec k=\vec u\wedge\vec v$ (règle de la main droite). Test rapide : à $\theta=0$, on doit retrouver $\vec u=\vec\imath$ et $\vec v=\vec\jmath$.



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
>
> <p style="text-align:center"><a href="/figures/td1_ex4_phv111.svg" target="_blank" rel="noopener"><img src="/figures/td1_ex4_phv111.svg" alt="" loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>



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




> [!note]- 🔗 Liens avec d'autres disciplines
> **Mathématiques (complexes)**
>
> Avec $e^{i\theta}=\cos\theta+i\sin\theta$, on a $\dfrac{\mathrm d}{\mathrm d\theta}e^{i\theta}=i\,e^{i\theta}$ : multiplier par $i$ est une rotation de $+90^\circ$. C'est la même formule, sous une autre écriture.
>
> **Algèbre linéaire**
>
> La matrice de rotation $R(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$ a pour colonnes $\vec u$ et $\vec v$ ; sa dérivée vaut $R'(\theta)=R(\theta)\begin{pmatrix}0&-1\\1&0\end{pmatrix}$.
>
> **Électricité / électrotechnique**
>
> Un champ magnétique tournant (moteur synchrone, alternateur triphasé) est un vecteur unitaire tournant de pulsation $\omega$ ; la tension alternative est son phaseur.
>
> **Mécanique du solide**
>
> Pour tout vecteur lié à un solide en rotation, $\dfrac{\mathrm d\vec e}{\mathrm dt}=\vec\Omega\wedge\vec e$ : avec $\vec\Omega=\dot\theta\,\vec k$ et $\vec e=\vec u$, on retrouve $\dot\theta\,\vec v$.




> [!warning]- 🪤 Écueils classiques
> **Erreur de signe sur $\vec v$**
>
> Une erreur très fréquente consiste à écrire $\vec v = \sin\theta\,\vec\imath - \cos\theta\,\vec\jmath$ (rotation de $-90°$) au lieu de $-\sin\theta\,\vec\imath+\cos\theta\,\vec\jmath$ (rotation de $+90°$), ce qui inverserait ensuite le signe de $\mathrm{d}\vec v/\mathrm{d}\theta$. Toujours vérifier la condition de trièdre direct en testant $\theta=0$ : on doit retrouver $\vec u=\vec\imath$ et $\vec v=\vec\jmath$ (et non $-\vec\jmath$).




> [!success]- 🏁 Bilan pédagogique
> **Les deux formules à retenir par cœur**
>
> $$\frac{\mathrm{d}\vec u}{\mathrm{d}\theta} = \vec v, \qquad \frac{\mathrm{d}\vec v}{\mathrm{d}\theta} = -\vec u.$$
> Ces deux relations, purement géométriques, seront reprises telles quelles (avec $\vec u=\vec u_r$, $\vec v=\vec u_\theta$) dans toute la suite du cours sur les coordonnées polaires, cylindriques et sphériques.




> [!question]- 🔭 Aller plus loin — CPGE : Généralisation : dérivée d'un vecteur de norme constante
> On peut montrer plus généralement que pour tout vecteur $\vec w(t)$ de norme constante, $\vec w\cdot\mathrm{d}\vec w/\mathrm{d}t = 0$ (la dérivée est orthogonale au vecteur lui-même) : c'est cette propriété générale qui explique, sans calcul explicite en coordonnées, pourquoi $\mathrm{d}\vec u/\mathrm{d}\theta$ est nécessairement colinéaire à $\vec v$ (l'unique direction orthogonale à $\vec u$ dans le plan).




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex5-le-poisson-archer-expert-en-balistique|Exercice 5 — Le poisson-archer, expert en balistique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex6-parabole-de-s-rete-et-tir-sur-une-pente|Exercice 6 — Parabole de sûreté et tir sur une pente]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]]


