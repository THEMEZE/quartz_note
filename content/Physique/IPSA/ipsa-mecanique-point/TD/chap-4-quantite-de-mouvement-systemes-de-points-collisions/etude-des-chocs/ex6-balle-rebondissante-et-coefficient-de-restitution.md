---
title: "Exercice 6 — (*) Balle rebondissante et coefficient de restitution"
tags:
  - td
  - chap-4-quantite-de-mouvement-systemes-de-points-collisions
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/index|⬅ Retour]] · <a href="/pdfs/td6_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td6_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 6. (*) Balle rebondissante et coefficient de restitution *(facultatif)*

*Difficulté ●●●●○ · ⏱ 60 min · Type : Exercice non guidé / Modélisation*

Une balle est lâchée sans vitesse initiale d'une hauteur $h_0=1{,}00$ m au-dessus d'un sol dur et horizontal. À chaque rebond, la composante normale de la vitesse est multipliée par $-e$ ($0<e<1$ : coefficient de restitution), la composante tangentielle étant conservée (pas de frottement). On prendra $e=0{,}80$ et $g=9{,}81~\mathrm{m\,s^{-2}}$ ; les frottements de l'air sont négligés et les chocs sont supposés instantanés.

> [!question]+ 🎣 Accroche
> **Une balle qui rebondit s'arrête-t-elle en un temps fini ?**
>
> *Durée de l'introduction : 4 min*
>
> *Une balle rebondit une **infinité** de fois, de moins en moins haut. **S'arrête-t-elle en un temps fini ou infini ?** Quelle distance totale parcourt-elle ? Quelle fraction de son énergie est perdue à chaque rebond ?*
>
> **Idée clé : la vitesse est multipliée par $e$ à chaque rebond, la hauteur par $e^2$, la durée du vol par $e$.** La somme des durées est une série géométrique convergente : la balle s'arrête en un temps **fini**.


> [!abstract]+ 📚 Prérequis
> **Coefficient de restitution sur un sol fixe**
>
> Pour un choc contre un sol immobile infiniment massif : $e=-\dfrac{v_{\rm après}}{v_{\rm avant}}$, soit $v'=-ev$ (composante normale). Énergie : $E_c'=e^2E_c$.
>
> **Chute libre**
>
> Lâchée de $h$ sans vitesse : $t=\sqrt{2h/g}$, $v=\sqrt{2gh}$. Lancée vers le haut à $v$ : $h=\dfrac{v^2}{2g}$, durée de vol $\dfrac{2v}g$.
>
> **Série géométrique**
>
> $\displaystyle\sum_{n=0}^\infty q^n=\dfrac1{1-q}$, $\displaystyle\sum_{n=1}^\infty q^n=\dfrac q{1-q}$ pour $|q|<1$.


> [!info]+ 🎯 Objectifs
> **Décrire une suite de rebonds par un modèle**
>
> Savoir exprimer hauteurs, vitesses et durées des rebonds successifs, sommer une série géométrique pour obtenir une durée et une distance totales, traiter un rebond oblique et un rebond sur une paroi en mouvement (raquette).


> [!note]+ 📖 Point de cours
> **Rebond sur un sol fixe**
>
> Vitesse avant le rebond $n$ : $v_n=\sqrt{2gh_{n-1}}$. Après : $v_n'=ev_n$. Hauteur de remontée : $h_n=\dfrac{(ev_n)^2}{2g}=e^2h_{n-1}$, donc $h_n=e^{2n}h_0$.
>
> **Durées**
>
> Première chute : $t_0=\sqrt{2h_0/g}$. Entre le rebond $n$ et $n+1$ : $\tau_n=\dfrac{2v_n'}g=2t_0e^n$ ($n\ge1$). Durée totale : $t_0+2t_0\dfrac e{1-e}=t_0\dfrac{1+e}{1-e}$.
>
> **Rebond oblique et paroi mobile**
>
> Sans frottement : $v_t'=v_t$, $v_n'=-ev_n$. Rebond sur une paroi qui avance à la vitesse $V$ vers la balle : dans le référentiel de la paroi, la vitesse normale est inversée et multipliée par $e$ ; retour au référentiel du laboratoire en ajoutant $V$.


> [!note]- 🧮 Outils mathématiques
> **Série géométrique**
>
> $\sum_{n=0}^\infty e^n=\dfrac1{1-e}$ ; $\sum_{n=1}^\infty e^{2n}=\dfrac{e^2}{1-e^2}$.
>
> **Suite géométrique : terme général**
>
> $h_{n+1}=e^2h_n\Rightarrow h_n=h_0e^{2n}$ ; $h_n<\varepsilon\iff n>\dfrac{\ln(\varepsilon/h_0)}{2\ln e}$.
>
> **Logarithmes**
>
> $\ln0{,}8=-0{,}223$ ; $\dfrac{\ln0{,}01}{2\ln0{,}8}=\dfrac{-4{,}605}{-0{,}446}=10{,}3$.


**q1.** - [(a)] Calculer la durée $t_0$ de la première chute et la vitesse $v_1$ juste avant le premier rebond.
- [(b)] Établir la hauteur $h_n$ atteinte après le $n$-ième rebond. Application numérique pour $n=1$, $2$, $5$. Combien de rebonds jusqu'à une hauteur $<1$ cm ?
- [(c)] Quelle fraction de l'énergie mécanique est dissipée à chaque rebond ?

> [!tip]- 💡 Coup de pouce
> Après le rebond $n$, la vitesse vaut $v_n'=ev_n$ ; la hauteur atteinte est $h_n=v_n'^2/(2g)$ et la vitesse de retour au sol est $\sqrt{2gh_n}$.


**q2.** - [(d)] Montrer que l'intervalle de temps entre le $n$-ième et le $(n+1)$-ième rebond vaut $\tau_n=2t_0e^n$. En déduire la durée totale $t_{\rm tot}$ jusqu'à l'arrêt ; AN. La balle s'arrête-t-elle en un temps fini ?
- [(e)] Calculer la distance verticale totale parcourue. AN.
- [(f)] **Rebond oblique** : la balle arrive sur le sol avec un angle $\theta=30^\circ$ par rapport à la normale (vitesse $v$). Quelle est la direction après le rebond ? Quel est le rapport $v'/v$ ? Application numérique.

> [!tip]- 💡 Coup de pouce
> (d) Durée d'un aller-retour : $2v_n'/g$ avec $v_n'=ev_n=e^nv_1$. (e) $h_0+2\sum_{n\ge1}h_n$. (f) Composante tangentielle conservée, composante normale multipliée par $-e$.


**q3.** - [(g)] **Rebond sur une raquette.** Une balle de tennis de vitesse $v=20~\mathrm{m/s}$ (vers la droite) est frappée par une raquette de masse très grande devant celle de la balle, animée d'une vitesse $V=30~\mathrm{m/s}$ (vers la gauche). Le coefficient de restitution est $e=0{,}75$. Calculer la vitesse de la balle après le choc, par un raisonnement dans le référentiel de la raquette. Quelle fraction de l'énergie fournie par la raquette est transmise ? Pourquoi une balle ne repart-elle pas à $2V$ ?

> [!tip]- 💡 Coup de pouce
> Se placer dans le référentiel de la raquette (immobile) : la balle arrive à $v+V$ et repart à $e(v+V)$. Revenir au référentiel du laboratoire.

