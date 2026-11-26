---
title: "Exercice 2 — Décollage d'un corps"
tags:
  - td
  - chap-2-dynamique-du-point-materiel-lois-de-newton
---

[[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/index|⬅ Retour]] · <a href="/pdfs/td4_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV111_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td4_PhV111_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 2. Décollage d'un corps

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 45 min · Type : Application / Cours actif*

Un corps de masse $m$ repose sur un plan horizontal et subit une force $\vec F$ dont la norme varie suivant la loi $F(t)=kt$, avec $k$ une constante positive. La force forme un angle $\alpha$ constant avec le plan (dirigée vers le haut et vers l'avant) et commence à agir à $t=0$, le corps étant au repos. On néglige les frottements et on prendra $g=9{,}81~\mathrm{m\,s^{-2}}$. Le repère $Oxy$ est choisi avec $Ox$ horizontal dans le sens de la force et $Oy$ vertical ascendant.


> [!question]- 🪝 Accroche
> **Quand le sol ne pousse plus**
>
> *Durée de l'introduction : 3 min*
>
> *Vous tirez une valise posée au sol avec une corde oblique, de plus en plus fort. Elle finit par **se soulever**. **À quel instant exact** ? Que vaut alors la réaction du sol ?*
>
> **Idée clé : décoller, c'est $N=0$.** Tant que le corps touche le plan, $a_y=0$ ; la projection verticale donne $N(t)=mg-kt\sin\alpha$, et le décollage a lieu à l'instant où cette expression s'annule.




> [!abstract]- 🧠 À savoir avant
> **Réaction normale d'un support**
>
> Un support exerce une réaction $\vec N$ perpendiculaire à sa surface, toujours dirigée vers l'extérieur : $N\ge0$. Le contact est rompu quand $N$ s'annule.




> [!info]- 🎯 Ce que tu sauras faire
> **Traduire une condition physique en équation**
>
> Savoir exprimer « le corps décolle » par $N=0$, utiliser l'absence de mouvement vertical avant le décollage ($a_y=0$) pour obtenir $N(t)$, puis intégrer une accélération qui dépend du temps avec les bonnes conditions initiales.




> [!info]- 🧑‍🏫 Objectifs pédagogiques
> **Une condition de contact, deux phases**
>
> Avant le décollage, le mouvement est horizontal ($a_y=0$), c'est ce qui fixe $N(t)$ ; le décollage est repéré par $N=0$. L'exercice enchaîne analyse dimensionnelle, bilan de forces, projection, intégration d'une accélération non constante. On peut demander de discuter les cas limites ($\alpha\to0$ : jamais de décollage ; $\alpha\to90^\circ$ : aucun déplacement horizontal).




> [!tip]- 📖 Rappel de cours
> **Conditions de contact**
>
> Tant que le corps reste sur le plan : $a_y=0$ et $N\ge0$. Le décollage a lieu à l'instant où $N=0$ (et $N<0$ serait impossible : le plan ne peut pas tirer).




> [!note]- 🧮 Outils mathématiques
> **Analyse dimensionnelle**
>
> $[kt]=[F]\Rightarrow[k]=\mathrm N\,\mathrm s^{-1}=\mathrm{kg\,m\,s^{-3}}$.
>
> **Primitives de puissances de $t$**
>
> $\int t\,\mathrm dt=\dfrac{t^2}2$ et $\int t^2\,\mathrm dt=\dfrac{t^3}3$ ; constantes fixées par $v(0)=0$, $x(0)=0$.
>
> **Résolution d'une équation affine**
>
> $mg-kt\sin\alpha=0\iff t=\dfrac{mg}{k\sin\alpha}$.



**q1.** - [(a)] Quelle est l'unité de $k$ dans le système international ?
- [(b)] Faire le bilan des forces qui agissent sur le corps et les projeter selon $Ox$ et $Oy$.
- [(c)] Quelle est la condition physique pour que le corps décolle du plan ?
- [(d)] Que peut-on dire de la composante verticale de l'accélération avant le décollage ?
- [(e)] Appliquer le principe fondamental de la dynamique et projeter selon $Ox$ et $Oy$ afin d'obtenir deux équations.


> [!tip]- 💡 Coup de pouce
> $F=kt$ impose les dimensions de $k$. Les forces sont le poids, la réaction normale et $\vec F$ ; le décollage correspond à la perte du contact.




> [!success]- ✅ Correction
> $[k]=\mathrm N\,\mathrm s^{-1}$ ; forces $m\vec g$, $\vec N$, $\vec F$ ; décollage $\Leftrightarrow N=0$ ; $a_y=0$ avant décollage ; $ma_x=kt\cos\alpha$ et $N+kt\sin\alpha-mg=0$.




> [!example]- 📝 Solution détaillée
> **(a) Unité de $k$**
>
> $F=kt$ donc $k=F/t$ : $[k]=\mathrm N\cdot\mathrm s^{-1}=\boxed{\mathrm{kg\,m\,s^{-3}}}$.
>
> **(b) Bilan des forces**
>
> Système : le corps. Référentiel terrestre galiléen. Forces : poids $\vec P=-mg\,\vec u_y$ ; réaction normale $\vec N=N\,\vec u_y$ (pas de frottement) ; force $\vec F$. Projections :
> $$\vec P:\ (0,\,-mg),\qquad\vec N:\ (0,\,N),\qquad\vec F:\ (kt\cos\alpha,\ kt\sin\alpha).$$
>
> **(c) Condition de décollage**
>
> Le plan ne peut que pousser, jamais tirer ($N\ge0$). Le corps quitte le plan quand le contact est rompu : $\boxed{N=0}$.
>
> **(d) Avant le décollage**
>
> Le corps reste sur le plan horizontal : son altitude est constante, donc $v_y=0$ et $\boxed{a_y=0}$.
>
> **(e) Principe fondamental**
>
> $\vec P+\vec N+\vec F=m\vec a$ se projette en
> $$\text{(Ox)}:\ m\,a_x=kt\cos\alpha,\qquad\text{(Oy)}:\ N+kt\sin\alpha-mg=m\,a_y=0 .$$
> On en tire la réaction : $N(t)=mg-kt\sin\alpha$.



**q2.** - [(f)] Donner l'accélération $a(t)$ du corps en fonction des paramètres du problème et en déduire sa vitesse $v(t)$.
- [(g)] Appliquer la condition de décollage pour calculer l'instant $t_d$ du décollage.
- [(h)] En déduire la vitesse au décollage $v(t_d)$.
- [(i)] Quelle est la distance parcourue par le corps jusqu'au décollage ?


> [!tip]- 💡 Coup de pouce
> L'accélération vient de (Ox). Intégrez deux fois en partant du repos. Pour (g), résolvez $N(t_d)=0$ dans l'équation de (Oy).




> [!success]- ✅ Correction
> $a=\dfrac{kt\cos\alpha}m$, $v=\dfrac{k\cos\alpha}{2m}t^2$ ; $t_d=\dfrac{mg}{k\sin\alpha}$ ; $v(t_d)=\dfrac{mg^2\cos\alpha}{2k\sin^2\alpha}$ ; $x(t_d)=\dfrac{m^2g^3\cos\alpha}{6k^2\sin^3\alpha}$.




> [!example]- 📝 Solution détaillée
> **(f) Accélération et vitesse**
>
> $$a(t)=\boxed{\frac{k\cos\alpha}{m}\,t}\quad\Rightarrow\quad v(t)=\int_0^ta\,\mathrm dt'=\boxed{\frac{k\cos\alpha}{2m}\,t^2}\qquad(v(0)=0).$$
>
> **(g) Instant du décollage**
>
> $N(t_d)=0\iff mg-kt_d\sin\alpha=0$, donc $\boxed{t_d=\dfrac{mg}{k\sin\alpha}}$ (valable si $\alpha\ne0$ ; pour $\alpha=0$ il n'y a jamais de décollage).
>
> **(h) Vitesse au décollage**
>
> $$v(t_d)=\frac{k\cos\alpha}{2m}\cdot\frac{m^2g^2}{k^2\sin^2\alpha}=\boxed{\frac{m\,g^2\cos\alpha}{2k\sin^2\alpha}}.$$
>
> **(i) Distance parcourue**
>
> $$x(t)=\int_0^tv\,\mathrm dt'=\frac{k\cos\alpha}{6m}t^3\ \Rightarrow\ x(t_d)=\frac{k\cos\alpha}{6m}\cdot\frac{m^3g^3}{k^3\sin^3\alpha}=\boxed{\frac{m^2g^3\cos\alpha}{6k^2\sin^3\alpha}}.$$
> Contrôle dimensionnel : $\dfrac{\mathrm{kg^2\,(m\,s^{-2})^3}}{(\mathrm{kg\,m\,s^{-3}})^2}=\mathrm m$. $\surd$




> [!note]- 🔗 Liens avec d'autres disciplines
> **Aéronautique**
>
> Décollage d'un avion : la portance doit compenser le poids, la réaction de la piste s'annule à la rotation.
>
> **Robotique**
>
> Un robot qui tire sur un câble : la force verticale doit rester inférieure au poids pour garder le contact.




> [!warning]- 🪤 Écueils classiques
> **Prendre $N=mg$ partout**
>
> $N=mg$ n'est vrai que si la force $\vec F$ n'a pas de composante verticale. Ici $N(t)=mg-kt\sin\alpha$ décroît avec le temps.
>
> **Oublier de projeter $\vec F$**
>
> La composante horizontale est $F\cos\alpha$, la composante verticale $F\sin\alpha$. Seule la seconde participe au décollage.
>
> **Intégrer sans constante**
>
> $v(t)=\dfrac{k\cos\alpha}{2m}t^2$ : la constante est nulle parce que le corps part du repos. Le dire explicitement.




> [!tip]- 🎙️ Conseils d'animation
> **Visualiser $N(t)$**
>
> Faire tracer $N(t)$ : droite décroissante qui coupe l'axe des temps en $t_d$. Demander ce qui se passe ensuite (le corps quitte le plan et suit une trajectoire de projectile avec force variable).




> [!success]- 🏁 Bilan pédagogique
> **Décollage**
>
> $N(t)=mg-kt\sin\alpha$, $t_d=\dfrac{mg}{k\sin\alpha}$, $v(t_d)=\dfrac{mg^2\cos\alpha}{2k\sin^2\alpha}$, distance $\dfrac{m^2g^3\cos\alpha}{6k^2\sin^3\alpha}$. Une force augmentant linéairement avec le temps donne $a\propto t$, $v\propto t^2$, $x\propto t^3$.




> [!question]- 🔭 Aller plus loin — CPGE : Avec frottement solide
> Ajouter un frottement de Coulomb $f=\mu N$. Montrer que le corps ne démarre qu'à partir de l'instant $t_0=\dfrac{\mu mg}{k(\cos\alpha+\mu\sin\alpha)}$ (où $kt\cos\alpha=\mu(mg-kt\sin\alpha)$), que $t_0<t_d=\dfrac{mg}{k\sin\alpha}$ quel que soit $\mu$, et que le décollage n'est donc pas modifié (il a lieu en $N=0$, où le frottement s'annule) ; calculer la vitesse au décollage dans ce cas.




> [!question]- 🔭 Aller plus loin — Licence : Après le décollage
> Écrire les équations du mouvement après $t_d$ (force toujours en $kt$), intégrer, et déterminer l'instant où le corps retombe si la force est coupée à $t_d$ : on obtient alors un tir parabolique.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex1-exercices-elementaires|Exercice 1 — Exercices élémentaires]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex3-machine-d-atwood|Exercice 3 — Machine d'Atwood]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex4-systeme-de-deux-blocs|Exercice 4 — Système de deux blocs]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex5-voiture-sur-une-bosse|Exercice 5 — Voiture sur une bosse]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex6-navette-columbia|Exercice 6 — (*) Navette Columbia]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex7-chute-avec-frottement-fluide-vitesse-limite|Exercice 7 — Chute avec frottement fluide : vitesse limite]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex8-pendule-conique|Exercice 8 — Pendule conique]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-2-dynamique-du-point-materiel-lois-de-newton/lois-de-newton/ex9-virage-releve-et-frottement-solide|Exercice 9 — Virage relevé et frottement solide]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-4-quantite-de-mouvement-systemes-de-points-collisions/etude-des-chocs/ex4-systeme-pendule-bloc|Exercice 4 — (*) Système pendule-bloc]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex4-looping-vertical|Exercice 4 — Looping vertical]] · [[physique/IPSA/ipsa-mecanique-point/TD/chap-3-travail-energie-cinetique-energie-potentielle-energie-mecanique/travail-et-energie/ex5-bille-sur-une-sphere-angle-de-decollage|Exercice 5 — (*) Bille sur une sphère : angle de décollage]]


