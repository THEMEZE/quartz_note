---
title: "Exercice 7 — (*) Modération des neutrons et chaîne de billes"
tags:
  - td
  - chap-4-quantite-de-mouvement-systemes-de-points-collisions
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/index|⬅ Retour]]

### Exercice 7. (*) Modération des neutrons et chaîne de billes *(facultatif)*

Dans un réacteur nucléaire, les neutrons de fission sont émis avec une énergie de l'ordre de $E_0=2~\mathrm{MeV}$ ; pour entretenir la réaction en chaîne dans l'uranium $235$, il faut les ralentir jusqu'à l'énergie d'agitation thermique $E_f=0{,}025~\mathrm{eV}$ : c'est le rôle du **modérateur**. Le ralentissement se fait par chocs **élastiques** successifs sur des noyaux au repos de nombre de masse $A$ (masse $Am$, $m$ masse du neutron). On étudie d'abord un choc frontal, puis le cas général (diffusion isotrope dans le référentiel du centre de masse), puis un problème voisin, l'optimisation du transfert de vitesse dans une chaîne de billes.

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

