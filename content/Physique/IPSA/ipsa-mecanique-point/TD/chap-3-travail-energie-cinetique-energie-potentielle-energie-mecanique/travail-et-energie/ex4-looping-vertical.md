---
title: "Exercice 4 — Looping vertical"
tags:
  - td
  - chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/index|⬅ Retour]] · <a href="/pdfs/td5_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td5_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 4. Looping vertical

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 45 min · Type : Application / Synthèse énergie et Newton*

Le wagon d'un manège, de masse $m$ assimilé à un point matériel $M$, est lâché **sans vitesse initiale** d'une hauteur $H$ au point $A$, glisse le long d'une grande descente, puis effectue un looping circulaire de rayon $R=19$ m. Le point $B$ est le sommet du looping, le point $C$ le point le plus bas. On néglige les frottements, on prendra $g=9{,}81~\mathrm{m\,s^{-2}}$ et on repère l'altitude $z$ à partir du sol (point $C$).


> [!question]- 🪝 Accroche
> **Pourquoi ne tombe-t-on pas la tête en bas ?**
>
> *Durée de l'introduction : 3 min*
>
> *Au sommet d'un looping, les passagers sont **la tête en bas** et ne tombent pas, sans être attachés par le haut. **À quelle vitesse minimale** faut-il arriver au sommet ? De quelle hauteur faut-il lâcher le wagon ?*
>
> **Idée clé : au sommet, le poids seul peut fournir la force centripète.** $N+mg=mv^2/R$ : si $v^2=gR$, $N=0$ et le poids suffit ; au-dessus, le rail pousse. La vitesse vient de l'énergie : $v^2=2g(H-2R)$.




> [!abstract]- 🧠 À savoir avant
> **Conservation de l'énergie mécanique**
>
> La réaction normale du rail lisse est perpendiculaire à $\vec v$, elle ne travaille pas ; seul le poids travaille : $E_m=\tfrac12mv^2+mgz=\text{cte}$.
>
> **Base de Frenet**
>
> $\vec a=\dfrac{\mathrm dv}{\mathrm dt}\vec t+\dfrac{v^2}{\rho}\vec n$, $\vec n$ dirigé vers le centre de courbure ; sur un cercle, $\rho=R$.
>
> **Condition de contact**
>
> $N\ge0$ ; le contact est rompu quand $N=0$.




> [!info]- 🎯 Ce que tu sauras faire
> **Combiner énergie et loi de Newton**
>
> Savoir obtenir la vitesse par l'énergie, la réaction par la projection normale, puis écrire la condition $N\ge0$ et en déduire une hauteur minimale. Chercher le **point le plus critique** du trajet.




> [!tip]- 📖 Rappel de cours
> **Méthode**
>
> (1) Conservation de $E_m$ entre $A$ et le point étudié ; (2) PFD projeté sur la normale ; (3) $N\ge0$ en chaque point ; (4) étude du minimum de $N$ sur le trajet.
>
> **Rail lisse : un paramètre angulaire**
>
> Repérer la position par l'angle $\theta$ (mesuré depuis le bas du looping) : $z=R(1-\cos\theta)$. La projection de $m\vec a=m\vec g+\vec N$ sur la normale centripète donne $N-mg\cos\theta=\dfrac{mv^2}R$ ($\theta=0$ en bas, $\theta=\pi$ en haut).




> [!note]- 🧮 Outils mathématiques
> **Résolution d'inégalités**
>
> $2g(H-2R)\ge gR\iff H\ge\tfrac52R$ (diviser par $g>0$).
>
> **Position angulaire sur un cercle**
>
> Avec $\theta$ depuis le bas : $z=R(1-\cos\theta)$, composante radiale du poids $-mg\cos\theta$ (vers le centre pour $\cos\theta<0$).



**q1.** - [(a)] Appliquer la conservation de l'énergie mécanique du wagon entre $A$ et $B$.
- [(b)] En déduire l'expression de sa vitesse $v_B$ au point $B$ en fonction de $H$, $R$ et $g$.
- [(c)] Faire le bilan des forces qui s'exercent sur le wagon en $B$.


> [!tip]- 💡 Coup de pouce
> $A$ est à l'altitude $H$ avec $v_A=0$ ; $B$ est à l'altitude $2R$. La réaction du rail ne travaille pas.



**q2.** - [(d)] Rappeler l'expression de l'accélération dans la base de Frenet.
- [(e)] Appliquer le PFD en $B$ et le projeter dans la base de Frenet.
- [(f)] Sous quelle condition physique le wagon se détache-t-il du rail ?
- [(g)] En déduire la vitesse minimale $v_{\min}$ en $B$ pour que le wagon reste en contact ; valeur numérique.
- [(h)] En déduire la hauteur minimale $H_{\min}$ permettant au wagon de franchir le looping jusqu'en $C$.


> [!tip]- 💡 Coup de pouce
> Au sommet, $\vec n$ est dirigé vers le bas. $\vec a=\dfrac{\mathrm dv}{\mathrm dt}\vec t+\dfrac{v^2}R\vec n$. Le contact est rompu quand la réaction s'annule.



**q3.** **Compléments (le sommet est-il le pire point ?)** On repère le wagon par l'angle $\theta$ entre le rayon $\overrightarrow{OM}$ et la verticale descendante ($\theta=0$ en bas du looping, $\theta=\pi$ au sommet).


- [(i)] Exprimer l'altitude $z(\theta)$, puis $v^2(\theta)$ par l'énergie.
- [(j)] Établir $N(\theta)$ par le PFD projeté sur la normale centripète. Montrer que $N$ est minimale au sommet.
- [(k)] Pour $H=H_{\min}=\tfrac52R$, calculer $N_{\rm bas}/(mg)$ et commenter.


> [!tip]- 💡 Coup de pouce
> $z=R(1-\cos\theta)$. Projeter sur la direction vers le centre : $N-mg\cos\theta=mv^2/R$ (le poids a une composante vers le centre égale à $-mg\cos\theta$).




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex5-bille-sur-une-sphere-angle-de-decollage|Exercice 5 — (*) Bille sur une sphère : angle de décollage]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex4-systeme-pendule-bloc|Exercice 4 — (*) Système pendule-bloc]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex5-pendule-balistique|Exercice 5 — (*) Pendule balistique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]]


