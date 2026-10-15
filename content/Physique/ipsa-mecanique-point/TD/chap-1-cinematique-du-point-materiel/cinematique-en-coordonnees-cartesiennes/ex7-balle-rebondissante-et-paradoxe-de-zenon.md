---
title: "Exercice 7 — Balle rebondissante et paradoxe de Zénon"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td1_PhV111_corrige.pdf) · [📄 Énoncé](/pdfs/td1_PhV111_enonces.pdf) · [📄 Aides](/pdfs/td1_PhV111_aides.pdf) · [📄 Fiche enseignant](/pdfs/td1_PhV111_fiche.pdf)

### Exercice 7. Balle rebondissante et paradoxe de Zénon *(facultatif)*

Une balle est lâchée sans vitesse initiale d'une hauteur $h_0=1{,}00$ m au-dessus d'un sol horizontal. On néglige les frottements de l'air et on assimile la balle à un point matériel dans le champ de pesanteur $g=9{,}81~\mathrm{m\,s^{-2}}$.
Chaque choc avec le sol est supposé **instantané** : la composante verticale de la vitesse est inversée et **multipliée par** un coefficient de restitution $e$ (avec $0<e<1$) ; on prendra $e=0{,}80$. On repère la balle par son altitude $z$ (axe $Oz$ vertical ascendant, origine au sol), l'origine des temps étant l'instant du lâcher.

**q1.** - [(a)] Calculer la vitesse $v_0$ de la balle juste avant le premier choc et la durée $t_0$ de la première chute.
- [(b)] Après le $n$-ième choc ($n\ge1$), exprimer la vitesse initiale $v_n$ de la balle, la hauteur maximale $h_n$ atteinte et la durée $T_n$ qui sépare le $n$-ième du $(n+1)$-ième choc, en fonction de $e$, $v_0$, $h_0$ et $t_0$.
- [(c)] Représenter schématiquement $z(t)$ sur les premiers rebonds.

> [!tip]- 💡 Coup de pouce
> Après chaque choc, la balle repart verticalement vers le haut avec la vitesse $e$ fois celle de l'arrivée : c'est un lancer vertical. Utilisez les résultats d'un lancer vertical ($h=v^2/2g$, durée aller-retour $2v/g$).


> [!success]- ✅ Correction
> $v_0=\sqrt{2gh_0}\approx4{,}43~\mathrm{m/s}$, $t_0=\sqrt{2h_0/g}\approx0{,}452$ s ; $v_n=e^nv_0$, $h_n=e^{2n}h_0$, $T_n=2e^nt_0$.


> [!example]- 📝 Solution détaillée
> **(a) Première chute**
>
> Chute libre sans vitesse initiale depuis $h_0$ : $z(t)=h_0-\tfrac12gt^2$. La balle touche le sol en
> $$t_0=\sqrt{\frac{2h_0}{g}}\approx\boxed{0{,}452~\text{s}},\qquad v_0=g\,t_0=\sqrt{2gh_0}\approx\boxed{4{,}43~\mathrm{m\,s^{-1}}}.$$
>
> **(b) Suites géométriques**
>
> La vitesse après le $n$-ième choc est $e$ fois la vitesse juste avant, qui vaut (par symétrie de la chute libre) $v_{n-1}$ : $v_n=e\,v_{n-1}$, donc
> $$\boxed{v_n=e^nv_0}.$$
> C'est un lancer vertical à la vitesse $v_n$ : la hauteur maximale est $h_n=\dfrac{v_n^2}{2g}$ et la durée d'un aller-retour est $\dfrac{2v_n}{g}$ :
> $$\boxed{h_n=e^{2n}h_0},\qquad\boxed{T_n=\frac{2v_n}{g}=2\,e^n\,t_0}\quad(\text{car }v_0/g=t_0).$$
> Les vitesses et les durées forment des suites géométriques de raison $e$ ; les hauteurs, de raison $e^2$.
>
> **(c) Allure de $z(t)$**
>
> Le graphe est une succession d'**arches de paraboles** (concavité vers le bas) commençant par la parabole descendante de la première chute. Les arches ont des sommets de plus en plus bas ($h_n=e^{2n}h_0$) et des bases de plus en plus étroites ($T_n=2e^nt_0$). Elles se resserrent vers un point d'accumulation sur l'axe des temps, à l'instant $t_\infty$ calculé ci-dessous.


**q2.** - [(d)] Calculer la durée totale $t_\infty$ entre le lâcher et l'immobilisation (limite), en fonction de $t_0$ et $e$. Application numérique.
- [(e)] Calculer la distance totale $D$ parcourue par la balle. Application numérique.
- [(f)] À partir de quel rebond la hauteur maximale devient-elle inférieure à $1$ mm ?
- [(g)] La balle effectue-t-elle un nombre fini ou infini de rebonds ? Commenter.

> [!tip]- 💡 Coup de pouce
> La durée totale est $t_0+\sum_{n\ge1}T_n$ : une série géométrique de raison $e$. La distance est la somme de la hauteur initiale $h_0$ et des montées-descentes ($2h_n$). Pour (f), résolvez $e^{2n}h_0<10^{-3}$ avec un logarithme.


> [!success]- ✅ Correction
> $t_\infty=t_0\dfrac{1+e}{1-e}\approx9\,t_0\approx4{,}06$ s ; $D=h_0\dfrac{1+e^2}{1-e^2}\approx4{,}56$ m ; $n\ge16$ rebonds ; infinité de rebonds en temps fini.


> [!example]- 📝 Solution détaillée
> **(d) Durée totale**
>
> $$t_\infty=t_0+\sum_{n=1}^{\infty}T_n=t_0+2t_0\sum_{n=1}^{\infty}e^n=t_0+2t_0\,\frac{e}{1-e}=t_0\,\frac{1-e+2e}{1-e}=\boxed{t_0\,\frac{1+e}{1-e}}.$$
> Application numérique : $\dfrac{1+0{,}8}{1-0{,}8}=9$, donc $t_\infty=9\times0{,}452\approx\boxed{4{,}06~\text{s}}$.
>
> **(e) Distance totale parcourue**
>
> La balle parcourt $h_0$ à la descente initiale, puis, après chaque choc $n\ge1$, la distance $2h_n$ (montée et descente) :
> $$D=h_0+2\sum_{n=1}^{\infty}e^{2n}h_0=h_0\left(1+\frac{2e^2}{1-e^2}\right)=\boxed{h_0\,\frac{1+e^2}{1-e^2}}.$$
> Application numérique : $\dfrac{1+0{,}64}{1-0{,}64}=\dfrac{1{,}64}{0{,}36}\approx4{,}56$, soit $D\approx\boxed{4{,}56~\text{m}}$.
>
> **(f) Nombre de rebonds pour $h_n<1$ mm**
>
> $h_n=e^{2n}h_0<10^{-3}~\text{m}\iff2n\ln e<\ln(10^{-3})\iff n>\dfrac{\ln(10^{-3})}{2\ln0{,}8}=\dfrac{-6{,}908}{-0{,}4463}\approx15{,}5$.
>
> Donc dès le **$16^{\rm e}$ rebond**. Vérification : $h_{15}=0{,}8^{30}\approx1{,}2$ mm et $h_{16}=0{,}8^{32}\approx0{,}8$ mm.
>
> **(g) Une infinité de rebonds en un temps fini**
>
> Il y a une infinité de chocs (la hauteur $h_n=e^{2n}h_0$ n'est jamais strictement nulle), mais comme la série $\sum T_n$ converge, ils se produisent tous avant l'instant $t_\infty\approx4{,}06$ s : c'est une version mécanique du **paradoxe de Zénon**. Les instants de choc s'accumulent vers $t_\infty$.
>
> Physiquement, le modèle s'arrête bien avant : au-delà d'une certaine vitesse minimale la déformation du sol, l'adhérence et le bruit empêchent des rebonds de hauteur sub-micrométrique. Un moteur de simulation impose donc un seuil d'arrêt.


**q3.** - [(h)] On enregistre le son des chocs d'une balle lâchée sans vitesse initiale d'une hauteur inconnue. Les quatre premiers chocs se produisent aux instants $0{,}45$ s ; $1{,}17$ s ; $1{,}75$ s ; $2{,}21$ s. En déduire le coefficient de restitution $e$ et la hauteur de lâcher $h_0$.
- [(i)] La balle est maintenant **lancée horizontalement** depuis la hauteur $h_0=1{,}00$ m avec la vitesse $v_x=2{,}0~\mathrm{m\,s^{-1}}$, sans frottement à l'impact (la composante horizontale de la vitesse est conservée). Quelle distance horizontale totale $L$ parcourt-elle ? Quelle est la longueur de la première arche ?

> [!tip]- 💡 Coup de pouce
> Pour (h), les intervalles entre chocs successifs sont $T_1,T_2,T_3$ : calculez leurs rapports. Le premier instant de choc est $t_0=\sqrt{2h_0/g}$. Pour (i), le temps est commun aux deux mouvements : la distance horizontale se déduit de la durée totale.


> [!success]- ✅ Correction
> Intervalles $0{,}72$ ; $0{,}58$ ; $0{,}46$ s : rapports $\approx0{,}80$, donc $e\approx0{,}80$ ; $h_0=\tfrac12gt_0^2\approx0{,}99$ m $\approx1{,}0$ m. Horizontalement : $L=v_xt_\infty\approx8{,}1$ m ; première arche : $v_xt_0\approx0{,}90$ m jusqu'au premier choc.


> [!example]- 📝 Solution détaillée
> **(h) Exploitation des données**
>
> Intervalles entre chocs : $T_1=1{,}17-0{,}45=0{,}72$ s ; $T_2=1{,}75-1{,}17=0{,}58$ s ; $T_3=2{,}21-1{,}75=0{,}46$ s. Comme $T_{n+1}=e\,T_n$ :
> $$\frac{T_2}{T_1}\approx0{,}806,\qquad\frac{T_3}{T_2}\approx0{,}793\;\Longrightarrow\;\boxed{e\approx0{,}80}.$$
> Seconde méthode : $T_1=2e\,t_0$ avec $t_0=0{,}45$ s donne $e=\dfrac{0{,}72}{0{,}90}=0{,}80$. Les deux estimations concordent.
>
> Le premier choc a lieu à l'instant $t_0=0{,}45$ s, d'où
> $$h_0=\tfrac12\,g\,t_0^2=\tfrac12\times9{,}81\times0{,}45^2\approx\boxed{0{,}99~\text{m}\approx1{,}0~\text{m}}.$$
>
> **(i) Lancer horizontal**
>
> Les deux mouvements ont lieu en même temps : $x(t)=v_xt$ pour $t\le t_\infty$. La distance horizontale totale est
> $$L=v_x\,t_\infty=v_x\,t_0\,\frac{1+e}{1-e}=2{,}0\times0{,}452\times9\approx\boxed{8{,}1~\text{m}}.$$
> La première arche (de $t=0$ au premier choc) a pour longueur $v_xt_0\approx2{,}0\times0{,}452\approx\boxed{0{,}90~\text{m}}$. Les arches suivantes ont pour longueur $v_xT_n=2e^n\,v_xt_0$ : ce sont des arches de plus en plus courtes, en progression géométrique de raison $e$. Leur somme est finie : la balle **ne parcourt qu'une distance horizontale finie**, bien qu'elle effectue une infinité de rebonds.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex3-course-automobile-rattrapage-de-deux-mobiles|Exercice 3 — Course automobile : rattrapage de deux mobiles]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex4-le-dilemme-du-feu-orange|Exercice 4 — Le dilemme du feu orange]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex6-parabole-de-s-rete-et-tir-sur-une-pente|Exercice 6 — Parabole de sûreté et tir sur une pente]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]]

