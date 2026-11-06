---
title: "Exercice 5 — Voiture sur une bosse"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 5. Voiture sur une bosse

Une automobile s'engage sur une portion de route en forme de bosse. Le véhicule est assimilé à un point matériel $M$ de masse $m$, et la norme $v>0$ de sa vitesse est constante tout au long du mouvement. La bosse est modélisée par deux portions rectilignes raccordées par un arc de cercle de centre $O$, de rayon $R$ et d'ouverture angulaire $2\alpha$ (le centre $O$ est sous la route). On repère $M$ sur l'arc par l'angle $\theta$ entre la verticale ascendante passant par $O$ et le rayon $\overrightarrow{OM}$ ; $\theta$ est compté positivement dans le sens trigonométrique, de sorte que la voiture, qui avance vers la droite, parcourt l'arc de $\theta=+\alpha$ à $\theta=-\alpha$. On prendra $g=9{,}81~\mathrm{m\,s^{-2}}$.

On cherche à quelle condition sur $v$ l'automobile garde le contact avec le sol tout au long de son chemin.

**q1.** **1/ Cinématique**


- [(a)] Représenter sur la figure les vecteurs $(\vec e_r,\vec e_\theta)$ de la base polaire associée au point $M$.
- [(b)] Rappeler l'expression des dérivées de ces deux vecteurs par rapport à $\theta(t)$. (Si vous avez oublié, refaire le calcul.)
- [(c)] Donner, dans le cas général, l'expression du vecteur vitesse $\vec v$ en coordonnées polaires. Que devient-elle pour la voiture sur la partie courbe ?

> [!tip]- 💡 Coup de pouce
> $\vec e_r$ pointe de $O$ vers $M$ et $\vec e_\theta$ s'en déduit par une rotation de $+90^\circ$. Sur l'arc, $r=R$ est constant.


> [!success]- ✅ Correction
> $\dfrac{\mathrm d\vec e_r}{\mathrm d\theta}=\vec e_\theta$, $\dfrac{\mathrm d\vec e_\theta}{\mathrm d\theta}=-\vec e_r$ ; $\vec v=\dot r\,\vec e_r+r\dot\theta\,\vec e_\theta$ ; sur l'arc $\vec v=R\dot\theta\,\vec e_\theta$.


> [!example]- 📝 Solution détaillée
> **(a) Base polaire**
>
> $\vec e_r$ est unitaire, porté par $\overrightarrow{OM}$ (vers le haut et vers l'extérieur de l'arc) ; $\vec e_\theta$ est tangent à l'arc, obtenu en tournant $\vec e_r$ de $+90^\circ$ (sens trigonométrique, donc vers la gauche au sommet).
>
> **(b) Dérivées**
>
> Avec $\theta$ compté depuis la verticale, $\vec e_r=-\sin\theta\,\vec u_x+\cos\theta\,\vec u_y$ et $\vec e_\theta=-\cos\theta\,\vec u_x-\sin\theta\,\vec u_y$, d'où $\boxed{\dfrac{\mathrm d\vec e_r}{\mathrm d\theta}=\vec e_\theta}$ et $\boxed{\dfrac{\mathrm d\vec e_\theta}{\mathrm d\theta}=-\vec e_r}$ (on retrouve les formules du TD1 : l'origine de l'angle n'a pas d'importance, seule la rotation de $+90^\circ$ compte). Par dérivée composée : $\dot{\vec e}_r=\dot\theta\,\vec e_\theta$ et $\dot{\vec e}_\theta=-\dot\theta\,\vec e_r$.
>
> **(c) Vitesse**
>
> $\overrightarrow{OM}=r\,\vec e_r\Rightarrow\boxed{\vec v=\dot r\,\vec e_r+r\dot\theta\,\vec e_\theta}$. Sur l'arc, $r=R$ donc $\dot r=0$ et $\boxed{\vec v=R\dot\theta\,\vec e_\theta}$ : vitesse tangente à l'arc.


**q2.** - [(d)] Déterminer l'expression reliant $v$, $R$ et $\mathrm d\theta/\mathrm dt$ en analysant soigneusement le signe de $\mathrm d\theta/\mathrm dt$.
- [(e)] Donner, dans le cas général, l'expression du vecteur accélération $\vec a$ en polaires. Que devient-elle pour la voiture sur la partie courbe ?

> [!tip]- 💡 Coup de pouce
> La voiture va vers la droite au sommet ; que fait $\theta$ ? $v$ est la norme de $\vec v$, donc positive. Dérivez $\vec v$ en utilisant les dérivées de $\vec e_r$ et $\vec e_\theta$.


> [!success]- ✅ Correction
> $\dot\theta=-\dfrac vR$ ; $\vec a=(\ddot r-r\dot\theta^2)\vec e_r+(r\ddot\theta+2\dot r\dot\theta)\vec e_\theta$ ; sur l'arc $\vec a=-\dfrac{v^2}R\,\vec e_r$.


> [!example]- 📝 Solution détaillée
> **(d) Lien entre $v$, $R$ et $\dot\theta$**
>
> Sur l'arc, $\|\vec v\|=R|\dot\theta|=v$. La voiture va de $\theta=+\alpha$ à $\theta=-\alpha$ : $\theta$ décroît, donc $\dot\theta<0$ :
> $$\boxed{\dot\theta=-\frac vR},\qquad\vec v=R\dot\theta\,\vec e_\theta=-v\,\vec e_\theta .$$
> Au sommet ($\theta=0$), $\vec e_\theta=-\vec u_x$ : $\vec v=+v\,\vec u_x$, vers la droite. $\surd$
>
> **(e) Accélération**
>
> On dérive $\vec v=\dot r\,\vec e_r+r\dot\theta\,\vec e_\theta$ avec $\dot{\vec e}_r=\dot\theta\vec e_\theta$ et $\dot{\vec e}_\theta=-\dot\theta\vec e_r$ :
> $$\boxed{\vec a=(\ddot r-r\dot\theta^2)\,\vec e_r+(r\ddot\theta+2\dot r\dot\theta)\,\vec e_\theta}.$$
> Sur l'arc ($r=R$, $\dot\theta=-v/R$ constante donc $\ddot\theta=0$) :
> $$\boxed{\vec a=-R\dot\theta^2\,\vec e_r=-\frac{v^2}{R}\,\vec e_r}.$$
> Accélération centripète, dirigée vers $O$ (vers le bas au sommet), indépendante du signe de $\dot\theta$.


**q3.** **2/ Dynamique**


- [(a)] Faire le bilan des forces sur l'automobile : la route exerce une réaction $\vec R=\vec N+\vec T$, avec $\vec N$ la composante normale et $\vec T$ la composante tangentielle (frottements solides). Les représenter sur le schéma.
- [(b)] Comment exprimer au moyen d'une inégalité sur $\vec N$ que la voiture est ou non en contact avec la route ?
- [(c)] En appliquant la relation fondamentale de la dynamique projetée sur $\vec e_r$, donner l'expression reliant $\|\vec N\|$, $m$, $v$, $R$, $g$ et $\theta$.

> [!tip]- 💡 Coup de pouce
> Le poids est vertical vers le bas ; $\vec N$ est perpendiculaire à la route, donc selon $\vec e_r$ ; $\vec T$ est tangent, donc selon $\vec e_\theta$. Le contact exige que la route « pousse ».


> [!success]- ✅ Correction
> Forces : $m\vec g$, $\vec N=N\vec e_r$, $\vec T=T\vec e_\theta$. Contact $\iff N\ge0$. $N=m\Big(g\cos\theta-\dfrac{v^2}R\Big)$.


> [!example]- 📝 Solution détaillée
> **(a) Bilan des forces**
>
> Système : la voiture (point $M$). Référentiel : terrestre, galiléen. Forces : le poids $m\vec g=-mg\,\vec u_y=-mg\cos\theta\,\vec e_r+mg\sin\theta\,\vec e_\theta$ ; la réaction normale $\vec N=N\,\vec e_r$ ; la réaction tangentielle $\vec T=T\,\vec e_\theta$ (frottement et force motrice des roues).
>
> **(b) Condition de contact**
>
> La route ne peut que pousser : $\boxed{N\ge0}$ signifie contact maintenu ; $N=0$ est la limite du décollage ; $N<0$ est impossible (le véhicule a quitté la route).
>
> **(c) Projection radiale**
>
> $m\vec a=m\vec g+\vec N+\vec T$ se projette sur $\vec e_r$ : $-\dfrac{mv^2}R=-mg\cos\theta+N$, donc
> $$\boxed{N=m\left(g\cos\theta-\frac{v^2}{R}\right)}.$$
> La projection sur $\vec e_\theta$ donne $0=mg\sin\theta+T$, soit $T=-mg\sin\theta$ : le frottement (ou la force motrice) maintient la vitesse constante.


**q4.** - [(d)] Quelle inégalité relie $v$, $R$, $g$ et $\theta$ pour que la voiture reste sur la route quel que soit l'angle $\theta$ ?
- [(e)] En déduire la relation liant $v$, $R$, $g$ et $\alpha$ pour que la voiture reste sur la route tout le long du trajet.
- [(f)] Application numérique : calculer $v_{\max}$ pour $\alpha=10^\circ$ et $R=6{,}0$ m.

> [!tip]- 💡 Coup de pouce
> $N\ge0$ s'écrit $v^2\le gR\cos\theta$. Cette inégalité doit être vraie pour tous les $\theta\in[-\alpha,\alpha]$ : cherchez la valeur de $\theta$ qui rend le second membre minimal.


> [!success]- ✅ Correction
> $v\le\sqrt{gR\cos\theta}$ ; pour tout l'arc $v\le\sqrt{gR\cos\alpha}$ ; $v_{\max}\approx7{,}6~\mathrm{m/s}\approx27$ km/h.


> [!example]- 📝 Solution détaillée
> **(d) Condition pour un angle donné**
>
> $N\ge0\iff g\cos\theta\ge\dfrac{v^2}R\iff\boxed{v\le\sqrt{gR\cos\theta}}$.
>
> **(e) Condition sur tout l'arc**
>
> Il faut que l'inégalité soit vraie pour tout $\theta\in[-\alpha,\alpha]$. Le second membre est minimal quand $\cos\theta$ l'est, c'est-à-dire en $\theta=\pm\alpha$ (les extrémités de l'arc) :
> $$\boxed{v\le v_{\max}=\sqrt{g\,R\cos\alpha}}.$$
> La contrainte la plus sévère n'est pas au sommet (où $v\le\sqrt{gR}$) mais aux extrémités de l'arc, où le poids a la plus petite composante radiale.
>
> **(f) Application numérique**
>
> $$v_{\max}=\sqrt{9{,}81\times6{,}0\times\cos10^\circ}=\sqrt{57{,}97}\approx\boxed{7{,}6~\mathrm{m/s}}\approx27~\text{km/h}.$$
> Au-delà, la voiture décolle dès l'entrée de l'arc. Ordre de grandeur cohérent avec la vitesse de franchissement prudente d'un dos-d'âne ($\approx30$ km/h).


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex1-exercices-elementaires|Exercice 1 — Exercices élémentaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex2-decollage-d-un-corps|Exercice 2 — Décollage d'un corps]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex3-machine-d-atwood|Exercice 3 — Machine d'Atwood]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex7-chute-avec-frottement-fluide-vitesse-limite|Exercice 7 — Chute avec frottement fluide : vitesse limite]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]]

