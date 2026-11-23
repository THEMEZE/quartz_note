---
title: "Exercice 2 — Choc dans le plan et perte d'énergie"
tags:
  - td
  - chap-4-quantite-de-mouvement-systemes-de-points-collisions
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/index|⬅ Retour]] · <a href="/pdfs/td6_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td6_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 2. Choc dans le plan et perte d'énergie

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 40 min · Type : Application / Cours actif*

Deux boules identiques $A$ et $B$, de masse $m$, sont mobiles sans frottement sur un plan horizontal. La boule $B$, initialement au repos, est heurtée par la boule $A$ de vitesse $v_A=4~\mathrm{m/s}$. Après le choc, les trajectoires de $A$ et $B$ font respectivement les angles $30^\circ$ et $45^\circ$ avec la trajectoire incidente, de part et d'autre de celle-ci. On note $\vec v_A'$ et $\vec v_B'$ les vitesses après le choc ; l'axe $(Ox)$ est la direction incidente de $A$, $(Oy)$ perpendiculaire dans le plan.

> [!question]+ 🎣 Accroche
> **Billard : où vont les deux billes ?**
>
> *Durée de l'introduction : 3 min*
>
> *Au billard, une bille en frappe une autre **de côté**. Les deux billes repartent dans des directions différentes. **Que peut-on dire de ces directions ?** Si on mesure les angles, comment savoir si le choc est élastique ?*
>
> **Idée clé : $\vec p$ est conservée (vectoriellement) pour tout choc ; $E_c$ seulement pour un choc élastique.** Pour deux billes identiques, la conservation de $\vec p$ et de $E_c$ imposent un angle droit entre les trajectoires.


> [!abstract]+ 📚 Prérequis
> **Conservation vectorielle de $\vec p$**
>
> $\vec p_A+\vec p_B=\vec p_A'+\vec p_B'$ : deux équations scalaires.
>
> **Trigonométrie**
>
> $\cos30^\circ=\tfrac{\sqrt3}2$, $\sin30^\circ=\tfrac12$, $\cos45^\circ=\sin45^\circ=\tfrac{\sqrt2}2$.
>
> **Nature d'un choc**
>
> Élastique si $E_c$ est conservée ; partiellement élastique si $E_c$ diminue sans que les corps restent liés ; parfaitement mou si les corps restent liés.


> [!info]+ 🎯 Objectifs
> **Résoudre un choc plan à partir des angles**
>
> Savoir projeter la conservation de $\vec p$, résoudre pour les deux normes, calculer l'énergie avant/après pour identifier la nature du choc, et démontrer le résultat de l'angle droit pour deux masses identiques.


> [!note]+ 📖 Point de cours
> **Choc plan : méthode**
>
> (1) Schéma avec angles ; (2) $\vec p$ avant et après ; (3) projections sur $Ox,Oy$ ; (4) résolution ; (5) énergie avant/après.
>
> **Billes identiques, une au repos, choc élastique**
>
> $\vec v=\vec v_1'+\vec v_2'$ et $v^2=v_1'^2+v_2'^2$ $\Rightarrow$ $\vec v_1'\perp\vec v_2'$ ; $v_1'=v\cos\theta_1$, $v_2'=v\sin\theta_1$.


> [!note]- 🧮 Outils mathématiques
> **Projections et angles**
>
> Une vitesse de norme $v$ faisant l'angle $\theta$ avec $Ox$ a pour composantes $(v\cos\theta,\ v\sin\theta)$.
>
> **Produit scalaire**
>
> $\|\vec a+\vec b\|^2=a^2+2\vec a\cdot\vec b+b^2$ ; si $\vec a\perp\vec b$ (Pythagore) : $a^2+b^2$.
>
> **Rationaliser une expression**
>
> $\dfrac2{\sqrt3+1}=\sqrt3-1\approx0{,}732$, d'où $v_A'=v_A(\sqrt3-1)=4\times0{,}732\approx2{,}93$ m/s ; et $v_B'=\dfrac{v_A'}{\sqrt2}\approx2{,}07$ m/s.


**q1.** - [(a)] Faire un schéma avant et après le choc, en prenant l'axe $(Ox)$ suivant la trajectoire incidente de $A$ ; représenter les données.
- [(b)] Écrire la conservation de la quantité de mouvement et la projeter sur $(Ox)$ et $(Oy)$.
- [(c)] Établir les expressions de $v_A'$ et $v_B'$ en fonction de $v_A$.
- [(d)] Calculer $v_A'$ et $v_B'$ pour $v_A=4~\mathrm{m/s}$.

> [!tip]- 💡 Coup de pouce
> Avant : $\vec p=(mv_A,0)$. Après : $\vec p_A'=mv_A'(\cos30^\circ,\sin30^\circ)$, $\vec p_B'=mv_B'(\cos45^\circ,-\sin45^\circ)$. La composante selon $Oy$ donne $v_B'$ en fonction de $v_A'$.


**q2.** - [(e)] Quelle est la nature de ce choc (parfaitement élastique, partiellement élastique ou parfaitement mou) ? Calculer le pourcentage d'énergie cinétique perdue.
- [(f)] Montrer que, si la somme des angles de déviation est égale à $90^\circ$, le choc est élastique (deux masses identiques). Que valent alors $v_A'$ et $v_B'$ pour $\theta_A=30^\circ$ ?

> [!tip]- 💡 Coup de pouce
> (e) Comparer $\tfrac12mv_A^2$ à $\tfrac12m(v_A'^2+v_B'^2)$. (f) $\vec v_A=\vec v_A'+\vec v_B'$ (masses égales) ; élever au carré.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex3-choc-parfaitement-mou-entre-deux-voitures|Exercice 3 — Choc parfaitement mou entre deux voitures]]

