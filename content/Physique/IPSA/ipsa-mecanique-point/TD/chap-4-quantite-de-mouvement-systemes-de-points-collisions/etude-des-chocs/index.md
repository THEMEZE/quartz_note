---
title: "Étude des chocs"
tags:
  - td
  - chap-4-quantite-de-mouvement-systemes-de-points-collisions
---

[[physique/IPSA/ipsa-mecanique-point/index|⬅ Mécanique du point — IPSA]]

> [!info] ℹ️ Chap. 4 — Quantité de mouvement, systèmes de points, collisions
> Séance 6


<a href="/pdfs/td6_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td6_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

> [!question]+ 🎣 Accroche
> **Pourquoi un airbag sauve-t-il des vies ?**
>
> *Durée de l'introduction : 5 min*
>
> *Une voiture s'arrête contre un mur en $0{,}1$ s ; avec un airbag, la tête s'arrête en $0{,}2$ s. **La variation de quantité de mouvement est la même : pourquoi la force est-elle différente ?** Et que se passe-t-il quand deux voitures identiques se percutent de plein fouet à $50$ km/h chacune ?*
>
> **Idée clé : pendant un choc, $\vec p$ se conserve (pseudo-isolé) ; l'énergie cinétique, elle, est en général dissipée.** $\bar F=\Delta p/\Delta t$ : allonger la durée du choc réduit la force. L'énergie perdue vaut $\tfrac12\mu_rv_{\rm rel}^2(1-e^2)$.

> [!abstract]+ 📚 Prérequis
> **Les lois de Newton et la quantité de mouvement**
>
> $\vec p=m\vec v$ ; $\dfrac{\mathrm d\vec p}{\mathrm dt}=\sum\vec F_{\rm ext}$ ; pour un système de points $\vec P=\sum m_i\vec v_i=M\vec v_G$.
>
> **Travail et énergie (TD5)**
>
> $E_c=\tfrac12mv^2$, théorème de l'énergie cinétique, $\Delta E_m=W_{\rm nc}$ ; utile pour la phase **avant et après le choc** (descente du pendule, glissement du bloc).
>
> **Projection des vecteurs**
>
> Composantes cartésiennes, angles remarquables ($30^\circ,45^\circ,60^\circ$), norme $\sqrt{v_x^2+v_y^2}$, angle $\arctan(v_y/v_x)$.
>
> **Système d'équations**
>
> Système $2\times2$ linéaire (substitution, combinaison) ; identité remarquable $a^2-b^2=(a-b)(a+b)$ ; développement limité $(1+\epsilon)^n\approx1+n\epsilon$.

> [!info]+ 🎯 Objectifs
> **Savoir ce qui se conserve dans un choc**
>
> Savoir justifier la conservation de la quantité de mouvement (système pseudo-isolé), distinguer choc élastique ($E_c$ conservée), partiellement élastique et parfaitement mou, calculer l'énergie dissipée, utiliser un coefficient de restitution.
>
> **Résoudre une collision 1D ou 2D**
>
> Savoir écrire les relations de conservation, les projeter, résoudre en vitesses finales ; savoir traiter un choc entre deux billes, une voiture et un mur, un projectile et un pendule.
>
> **Enchaîner mouvement, choc, mouvement**
>
> Savoir découper un problème en phases : (1) avant le choc (énergie), (2) choc (quantité de mouvement), (3) après le choc (énergie ou Newton). Utiliser les bons outils à chaque phase.

> [!note]+ 📖 Point de cours
> **Quantité de mouvement et système pseudo-isolé**
>
> $\vec p=m\vec v$. Pour un système de points : $\vec P=\sum_im_i\vec v_i=M\vec v_G$ et $\dfrac{\mathrm d\vec P}{\mathrm dt}=\sum\vec F_{\rm ext}$. Si $\sum\vec F_{\rm ext}=\vec0$ (système isolé) ou si elles sont négligeables devant les forces impulsives (pseudo-isolé), $\vec P$ est conservée : $\vec P_{\rm avant}=\vec P_{\rm après}$. La conservation est **vectorielle** : une équation par composante.
>
> **Impulsion**
>
> $\vec J=\displaystyle\int_{t_1}^{t_2}\vec F\,\mathrm dt=\Delta\vec p$. Un choc de durée $\Delta t$ avec une force moyenne $\bar F$ : $\bar F\,\Delta t=\Delta p$. Réduire $\Delta t$ (mur rigide) augmente $\bar F$ ; allonger $\Delta t$ (airbag, zone de déformation) la réduit : lien avec la sécurité routière.
>
> **Classification des chocs**
>
> **Élastique** : $E_c$ conservée. **Parfaitement mou** : les corps restent liés après le choc, $\vec v_1'=\vec v_2'$, perte maximale. **Partiellement élastique** : intermédiaire. L'énergie perdue est transformée en déformation, chaleur, son. Toujours $\Delta E_c\le0$.
>
> **Coefficient de restitution**
>
> Choc frontal 1D : $e=-\dfrac{v_2'-v_1'}{v_2-v_1}$ (rapport des vitesses relatives après/avant), $0\le e\le1$ : $e=1$ élastique, $e=0$ parfaitement mou. Combiné avec la conservation de $p$ : $v_1'=\dfrac{(m_1-em_2)v_1+(1+e)m_2v_2}{m_1+m_2}$, $v_2'=\dfrac{(m_2-em_1)v_2+(1+e)m_1v_1}{m_1+m_2}$. Perte d'énergie : $\Delta E_c=-\tfrac12\mu_r(1-e^2)(v_1-v_2)^2$ avec $\mu_r=\dfrac{m_1m_2}{m_1+m_2}$.
>
> **Choc frontal élastique entre deux billes**
>
> $v_1'=\dfrac{(m_1-m_2)v_1+2m_2v_2}{m_1+m_2}$, $v_2'=\dfrac{(m_2-m_1)v_2+2m_1v_1}{m_1+m_2}$ ; la vitesse relative s'inverse : $v_2'-v_1'=-(v_2-v_1)$. Cas $m_2$ au repos : $v_1'=\dfrac{m_1-m_2}{m_1+m_2}v_1$, $v_2'=\dfrac{2m_1}{m_1+m_2}v_1$. Cas limites : $m_1=m_2$ échange des vitesses ; $m_1\gg m_2$ : $v_1'\approx v_1$, $v_2'\approx2v_1$ ; $m_1\ll m_2$ : $v_1'\approx-v_1$, $v_2'\approx0$ (rebond sur un mur).
>
> **Référentiel du centre de masse**
>
> $\vec v_G=\dfrac{m_1\vec v_1+m_2\vec v_2}{m_1+m_2}$ ; dans $\mathcal R^*$ (de vitesse $\vec v_G$), la quantité de mouvement totale est nulle : $\vec p_1^*=-\vec p_2^*$. Pour un choc élastique, les vitesses **pivotent** sans changer de norme (en 1D : inversion de signe). Énergie cinétique relative : $E_c^*=\tfrac12\mu_rv_{\rm rel}^2$, la seule énergie qui peut être dissipée ; $\tfrac12(m_1+m_2)v_G^2$ est conservée dans tous les cas.
>
> **Choc dans le plan : conservation vectorielle**
>
> Deux équations scalaires (projections sur $Ox$ et $Oy$) pour quatre inconnues (deux normes et deux angles de diffusion) : il faut **deux** données (un angle, un coefficient de restitution, la conservation de $E_c$). Deux billes identiques, choc élastique, l'une au repos : les vitesses finales sont **perpendiculaires** ($\theta_1+\theta_2=90^\circ$) ; si $\theta_1+\theta_2<90^\circ$ le choc est inélastique (cas de l'exercice 2).
>
> **Choc parfaitement mou**
>
> $\vec V=\dfrac{m_1\vec v_1+m_2\vec v_2}{m_1+m_2}=\vec v_G$ ; énergie perdue $\Delta E_c=-\tfrac12\mu_rv_{\rm rel}^2$ avec $v_{\rm rel}=\|\vec v_1-\vec v_2\|$ : **elle ne dépend que de la vitesse relative**. Exemple : deux voitures identiques (masse $m$) qui se percutent de plein fouet à la vitesse $v$ chacune : $v_{\rm rel}=2v$, $\mu_r=m/2$, énergie dissipée $mv^2$ au total, soit $\tfrac12mv^2$ par voiture : **chaque voiture subit la même dissipation que contre un mur rigide à $v$** (et non à $2v$).
>
> **Les trois phases : avant, choc, après**
>
> Pendule balistique, boule qui frappe un bloc : (1) **avant** : énergie mécanique (chute sans frottement), (2) **choc** : quantité de mouvement (et énergie si élastique), (3) **après** : énergie ou Newton (remontée, frottement). Ne jamais appliquer la conservation de $E_m$ à travers le choc sauf choc élastique, ni la conservation de $p$ à travers la phase de glissement (frottement extérieur non négligeable).

> [!note]- 🧮 Outils mathématiques
> **Résolution d'un système linéaire $2\times2$**
>
> Deux équations de conservation (projections) $\to$ deux inconnues ; élimination par combinaison linéaire.
>
> **Identité remarquable**
>
> $a^2-b^2=(a-b)(a+b)$ : transforme la conservation de $E_c$ ($m_1(v_1^2-v_1'^2)=m_2(v_2'^2-v_2^2)$) en $v_1+v_1'=v_2+v_2'$ après division par l'équation de $p$.
>
> **Développement limité**
>
> $(1+\epsilon)^n\approx1+n\epsilon$, $\dfrac1{1+\epsilon}\approx1-\epsilon$, $\sqrt{1+\epsilon}\approx1+\tfrac\epsilon2$ pour $|\epsilon|\ll1$.
>
> **Suite géométrique**
>
> $\displaystyle\sum_{n=0}^\infty q^n=\dfrac1{1-q}$ pour $|q|<1$ (rebonds successifs, exercice 6).
>
> **Trigonométrie**
>
> $\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$ ; $\cos30^\circ=\tfrac{\sqrt3}2$, $\sin45^\circ=\tfrac{\sqrt2}2$.


## Exercices

- [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex1-choc-frontal-elastique|Exercice 1 — Choc frontal élastique]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex2-choc-dans-le-plan-et-perte-d-energie|Exercice 2 — Choc dans le plan et perte d'énergie]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex3-choc-parfaitement-mou-entre-deux-voitures|Exercice 3 — Choc parfaitement mou entre deux voitures]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex4-systeme-pendule-bloc|Exercice 4 — (*) Système pendule-bloc]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex5-pendule-balistique|Exercice 5 — (*) Pendule balistique]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex6-balle-rebondissante-et-coefficient-de-restitution|Exercice 6 — (*) Balle rebondissante et coefficient de restitution]]
- [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex7-moderation-des-neutrons-et-chaine-de-billes|Exercice 7 — (*) Modération des neutrons et chaîne de billes]]
