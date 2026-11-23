---
title: "Exercice 7 — (*) Modération des neutrons et chaîne de billes"
tags:
  - td
  - chap-4-quantite-de-mouvement-systemes-de-points-collisions
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/index|⬅ Retour]] · <a href="/pdfs/td6_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td6_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 7. (*) Modération des neutrons et chaîne de billes *(facultatif)*

*Difficulté ●●●●● · ⏱ 70 min · Type : Exercice non guidé / Physique nucléaire et optimisation*

Dans un réacteur nucléaire, les neutrons de fission sont émis avec une énergie de l'ordre de $E_0=2~\mathrm{MeV}$ ; pour entretenir la réaction en chaîne dans l'uranium $235$, il faut les ralentir jusqu'à l'énergie d'agitation thermique $E_f=0{,}025~\mathrm{eV}$ : c'est le rôle du **modérateur**. Le ralentissement se fait par chocs **élastiques** successifs sur des noyaux au repos de nombre de masse $A$ (masse $Am$, $m$ masse du neutron). On étudie d'abord un choc frontal, puis le cas général (diffusion isotrope dans le référentiel du centre de masse), puis un problème voisin, l'optimisation du transfert de vitesse dans une chaîne de billes.

> [!question]+ 🎣 Accroche
> **Pourquoi l'eau et le graphite, pas le plomb ?**
>
> *Durée de l'introduction : 4 min*
>
> *Pour ralentir un neutron rapide, on a le choix entre de l'eau, du graphite (carbone) ou du plomb. **Lequel est le plus efficace ?** Intuitivement, un mur de plomb « arrête tout »... est-ce vrai pour des **chocs élastiques** ?*
>
> **Idée clé : un choc élastique fait perdre d'autant plus d'énergie à la particule incidente que la cible a une masse voisine de la sienne.** $\alpha=\Big(\dfrac{A-1}{A+1}\Big)^2\to0$ pour $A=1$, $\to1$ pour $A\gg1$ : un noyau lourd renvoie le neutron sans le ralentir.


> [!abstract]+ 📚 Prérequis
> **Choc élastique frontal à cible immobile**
>
> $v_1'=\dfrac{m_1-m_2}{m_1+m_2}v_1$, $v_2'=\dfrac{2m_1}{m_1+m_2}v_1$.
>
> **Référentiel du centre de masse**
>
> $\vec v_G=\dfrac{m_1\vec v_1+m_2\vec v_2}{m_1+m_2}$ ; $\vec v^*=\vec v-\vec v_G$ ; en $\mathcal R^*$, choc élastique : les normes sont conservées, la direction change d'un angle $\chi$.
>
> **Valeur moyenne d'une grandeur sur une distribution uniforme**
>
> Si $u$ est uniformément distribuée sur $[a,b]$ : $\langle f(u)\rangle=\dfrac1{b-a}\displaystyle\int_a^bf(u)\,\mathrm du$.
>
> **Logarithmes**
>
> $\ln(E_0/E_f)=\ln(2\times10^6/0{,}025)=\ln(8\times10^7)=18{,}2$.


> [!info]+ 🎯 Objectifs
> **Quantifier un ralentissement par chocs successifs**
>
> Savoir exprimer la perte d'énergie d'un choc élastique avec cible immobile, passer à la moyenne sur les angles de diffusion (décrément logarithmique $\xi$), en déduire le nombre de chocs pour ralentir une particule, comparer plusieurs modérateurs et résoudre un problème d'optimisation de masses.


> [!note]+ 📖 Point de cours
> **Choc élastique avec une cible immobile : énergie finale**
>
> Frontal : $\dfrac{E'}E=\alpha=\Big(\dfrac{A-1}{A+1}\Big)^2$ (perte maximale, $1-\alpha$). Quelconque, de déviation $\chi$ dans $\mathcal R^*$ : $\dfrac{E'}E=\dfrac{1+A^2+2A\cos\chi}{(A+1)^2}=\tfrac12\big[(1+\alpha)+(1-\alpha)\cos\chi\big]$.
>
> **Décrément logarithmique moyen**
>
> $\xi=\Big\langle\ln\dfrac E{E'}\Big\rangle=1+\dfrac{\alpha\ln\alpha}{1-\alpha}$ (diffusion isotrope), indépendant de l'énergie ; après $n$ chocs, $\ln\dfrac{E_0}{E_n}=n\xi$ en moyenne.
>
> **Transfert maximal d'énergie**
>
> Fraction transférée à la cible en choc frontal : $\dfrac{4m_1m_2}{(m_1+m_2)^2}$, maximale pour $m_1=m_2$ (le neutron ralenti à l'arrêt par un proton).


> [!note]- 🧮 Outils mathématiques
> **Intégrale du logarithme**
>
> $\displaystyle\int\ln u\,\mathrm du=u\ln u-u$ ; $\displaystyle\int_\alpha^1\ln\dfrac1u\,\mathrm du=1-\alpha+\alpha\ln\alpha$.
>
> **Formule d'Al-Kashi dans le triangle des vitesses**
>
> $\|\vec v_G+\vec v^*\|^2=v_G^2+v^{*2}+2v_Gv^*\cos\chi$.
>
> **Racines et symétrie $A\leftrightarrow1/A$**
>
> $\alpha$ est invariant par $A\to1/A$ : un projectile lourd sur une cible légère perd la même fraction qu'un projectile léger sur une cible lourde.
>
> **Optimisation d'une fonction d'une variable**
>
> Maximiser $\dfrac{m_2}{(m_1+m_2)(m_2+m_3)}$ : dériver par rapport à $m_2$ ; la dérivée s'annule en $m_2^2=m_1m_3$.


**q1.** - [(a)] Un neutron de masse $m$ et de vitesse $v$ heurte **de plein fouet** un noyau de masse $Am$ au repos (choc élastique). Exprimer le rapport $E'/E$ des énergies cinétiques du neutron après et avant le choc, en fonction de $A$. Calculer-le pour l'hydrogène ($A=1$), le deutérium ($A=2$), le carbone ($A=12$), le fer ($A=56$) et le plomb ($A=207$).
- [(b)] Quel modérateur ralentit le mieux un neutron en un seul choc frontal ? Pourquoi un noyau lourd est-il un mauvais modérateur ?
- [(c)] Pourquoi le choc frontal ne suffit-il pas à décrire le ralentissement réel ?

> [!tip]- 💡 Coup de pouce
> Utiliser les formules de l'exercice 1 avec $m_1=m$, $m_2=Am$, $v_2=0$ : $v'=\dfrac{1-A}{1+A}v$.


**q2.** - [(d)] Choc quelconque. Se placer dans $\mathcal R^*$ (centre de masse) : montrer que la vitesse du neutron après le choc, dans $\mathcal R$, vérifie $\dfrac{E'}E=\dfrac{1+A^2+2A\cos\chi}{(1+A)^2}$ où $\chi$ est l'angle de déviation dans $\mathcal R^*$. Retrouver le cas frontal ($\chi=\pi$).
- [(e)] Si la diffusion est isotrope dans $\mathcal R^*$, montrer que $E'/E$ est uniformément distribué entre $\alpha$ et $1$, puis que la perte logarithmique moyenne $\xi=\langle\ln(E/E')\rangle$ vaut $1+\dfrac{\alpha\ln\alpha}{1-\alpha}$.
- [(f)] En déduire le nombre moyen de chocs nécessaires pour ralentir un neutron de $2$ MeV à $0{,}025$ eV pour $A=1$, $2$, $12$, $56$ et $207$. Commenter.

> [!tip]- 💡 Coup de pouce
> (d) $\vec v_G=\dfrac{\vec v}{1+A}$, vitesse du neutron dans $\mathcal R^*$ : $\vec v^*=\dfrac A{1+A}\vec v$ ; après le choc, $\vec v'=\vec v_G+\vec v^{*\prime}$ avec $\|\vec v^{*\prime}\|=\|\vec v^*\|$. (e) $\cos\chi$ uniforme dans $[-1,1]$ pour une diffusion isotrope (angle solide $2\pi\,\mathrm d\cos\chi$). (f) $\ln(E_0/E_n)=n\xi$.


**q3.** **Empiler pour accélérer.** Trois billes $1,2,3$ de masses $m_1>m_2>m_3$ sont alignées sur une table lisse. La bille $1$ arrive à la vitesse $v_1$ sur la bille $2$ au repos ; la bille $2$ frappe ensuite la bille $3$ au repos. Chocs frontaux **élastiques**.


- [(g)] Exprimer $v_3'$ en fonction de $v_1$ et des masses. Pour $m_1$ et $m_3$ fixées, quelle masse $m_2$ maximise $v_3'$ ? Calculer $v_3'/v_1$ pour $m_1=1$ kg, $m_3=10$ g, et comparer au choc direct $1\to3$.
- [(h)] **Balle de tennis sur un ballon de basket.** Un ballon de basket ($M=600$ g) surmonté d'une balle de tennis ($m=57$ g) est lâché de $h_0=1{,}00$ m. Le ballon rebondit élastiquement sur le sol, puis heurte la balle encore en descente. Calculer la vitesse de la balle juste après son choc avec le ballon et la hauteur qu'elle atteint. Comparer au cas idéal $M\gg m$.

> [!tip]- 💡 Coup de pouce
> (g) $v_2'=\dfrac{2m_1}{m_1+m_2}v_1$ puis $v_3'=\dfrac{2m_2}{m_2+m_3}v_2'$ ; maximiser le produit en $m_2$. (h) Après le rebond, le ballon monte à $+v$ ; la balle descend encore à $-v$, avec $v=\sqrt{2gh_0}$ : appliquer la formule de l'exercice 1 avec $v_1=+v$, $v_2=-v$.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex1-choc-frontal-elastique|Exercice 1 — Choc frontal élastique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex4-systeme-pendule-bloc|Exercice 4 — (*) Système pendule-bloc]]

