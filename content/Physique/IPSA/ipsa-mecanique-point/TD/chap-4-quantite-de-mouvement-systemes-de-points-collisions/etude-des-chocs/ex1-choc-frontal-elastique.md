---
title: "Exercice 1 — Choc frontal élastique"
tags:
  - td
  - chap-4-quantite-de-mouvement-systemes-de-points-collisions
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/index|⬅ Retour]] · <a href="/pdfs/td6_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td6_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 1. Choc frontal élastique

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 45 min · Type : Cours actif / Application fondamentale*

Collision frontale **élastique** entre deux billes de masses $m_1$ et $m_2$, assimilées à deux points matériels. Toutes les vitesses sont colinéaires, suivant un axe $(Ox)$ ; on note $v_1,v_2$ les composantes algébriques avant le choc et $v_1',v_2'$ après le choc. Les frottements sont négligés.

> [!question]+ 🎣 Accroche
> **Pourquoi une boule de pétanque en plein dans la cible reste-t-elle sur place ?**
>
> *Durée de l'introduction : 3 min*
>
> *Au billard ou à la pétanque, une boule qui en frappe une autre **de plein fouet**, de même masse, s'arrête net. Que se passe-t-il si la boule frappée est beaucoup plus lourde ? beaucoup plus légère ?*
>
> **Idée clé : deux lois de conservation ($p$ et $E_c$) pour deux inconnues.** Le calcul donne $v_1'=\dfrac{m_1-m_2}{m_1+m_2}v_1$ : nul si $m_1=m_2$, négatif (rebond) si $m_1<m_2$.


> [!abstract]+ 📚 Prérequis
> **Système pseudo-isolé**
>
> Pendant le choc (durée très brève), les forces extérieures (poids, réaction) sont négligeables devant les forces d'interaction impulsives : $\vec p_{\rm tot}=\text{cte}$.
>
> **Choc élastique**
>
> $E_c$ totale conservée : $\tfrac12m_1v_1^2+\tfrac12m_2v_2^2=\tfrac12m_1v_1'^2+\tfrac12m_2v_2'^2$.
>
> **Identité remarquable**
>
> $a^2-b^2=(a-b)(a+b)$.


> [!info]+ 🎯 Objectifs
> **Établir les vitesses après un choc élastique frontal**
>
> Savoir écrire les deux lois de conservation, les combiner (identité remarquable) pour obtenir $v_1+v_1'=v_2+v_2'$, résoudre le système et discuter les cas limites ($m_1=m_2$, $m_1\gg m_2$, $m_1\ll m_2$).


> [!note]+ 📖 Point de cours
> **Résultats généraux**
>
> $v_1'=\dfrac{(m_1-m_2)v_1+2m_2v_2}{m_1+m_2}$ ; $v_2'=\dfrac{(m_2-m_1)v_2+2m_1v_1}{m_1+m_2}$ ; $v_2'-v_1'=-(v_2-v_1)$.
>
> **Transfert d'énergie**
>
> Avec $m_2$ au repos, la fraction d'énergie transférée à la bille 2 est $\dfrac{\Delta E_{c,2}}{E_{c,1}}=\dfrac{4m_1m_2}{(m_1+m_2)^2}\le1$, maximale pour $m_1=m_2$.


> [!note]- 🧮 Outils mathématiques
> **Identité remarquable et simplification**
>
> $m_1(v_1-v_1')(v_1+v_1')=m_2(v_2'-v_2)(v_2'+v_2)$ divisé par $m_1(v_1-v_1')=m_2(v_2'-v_2)$.
>
> **Développement limité**
>
> Pour $\epsilon\ll1$ : $\dfrac1{1+\epsilon}\approx1-\epsilon$ ; $\dfrac{1-\epsilon}{1+\epsilon}\approx1-2\epsilon$.


**q1.** - [(a)] Faire un schéma représentant les vitesses avant et après le choc.
- [(b)] Citer les grandeurs conservées lors de ce choc et écrire les relations qui en découlent.
- [(c)] En déduire les composantes algébriques $v_1'$ et $v_2'$ en fonction de $v_1$, $v_2$, $m_1$, $m_2$.

> [!tip]- 💡 Coup de pouce
> Deux lois de conservation : $p$ et $E_c$. Écrire $m_1(v_1-v_1')=m_2(v_2'-v_2)$ et $m_1(v_1^2-v_1'^2)=m_2(v_2'^2-v_2^2)$, puis diviser membre à membre.


**q2.** On suppose désormais que la masse $m_2$ est **immobile** avant le choc ($v_2=0$).


- [(d)] Donner $v_1'$ et $v_2'$.
- [(e)] Que se passe-t-il si $m_1=m_2$ ?
- [(f)] Que deviennent $v_1'$ et $v_2'$ si $m_1\gg m_2$ ? Interpréter. On pourra poser $\epsilon=m_2/m_1\ll1$ et utiliser $(1+\epsilon)^n\approx1+n\epsilon$.
- [(g)] Inversement, si $m_1\ll m_2$ ? Interpréter.
- [(h)] Calculer la fraction de l'énergie cinétique transférée à la bille 2. Pour quelle valeur du rapport $m_1/m_2$ est-elle maximale ? Application à $m_1/m_2=10$ et $m_1/m_2=\tfrac1{10}$.

> [!tip]- 💡 Coup de pouce
> (d) Poser $v_2=0$ dans (c). (f) Mettre $m_1$ en facteur au numérateur et au dénominateur. (h) $\dfrac12m_2v_2'^2/\big(\dfrac12m_1v_1^2\big)$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex4-systeme-pendule-bloc|Exercice 4 — (*) Système pendule-bloc]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex7-moderation-des-neutrons-et-chaine-de-billes|Exercice 7 — (*) Modération des neutrons et chaîne de billes]]

