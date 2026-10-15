---
title: "Exercice 5 — Le poisson-archer, expert en balistique"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td1_PhV111_corrige.pdf) · [📄 Énoncé](/pdfs/td1_PhV111_enonces.pdf) · [📄 Aides](/pdfs/td1_PhV111_aides.pdf) · [📄 Fiche enseignant](/pdfs/td1_PhV111_fiche.pdf)

### Exercice 5. Le poisson-archer, expert en balistique *(facultatif)*

Après avoir repéré un insecte posé sur une branche au-dessus de l'eau, le poisson-archer s'oriente et
projette un jet d'eau afin de l'atteindre et de le faire tomber.

Le poisson voit sa cible à une distance $d$, selon un axe incliné faisant un angle $\varphi$ avec
l'horizontale. Cependant, pour que la trajectoire du jet d'eau passe par l'insecte, la goutte d'eau
doit être lancée sous un angle $\alpha$ différent de l'angle de visée $\varphi$.

On néglige les frottements de l'air et la réfraction de la lumière à l'interface eau-air, et on
assimile la goutte à un point matériel en chute libre.

**q1.** Si $\varphi=36^\circ$ et $d=0{,}900$ m, quel est l'angle de lancement $\alpha$ nécessaire pour que la goutte d'eau atteigne l'insecte **au sommet de sa trajectoire** ?

> [!tip]- 💡 Coup de pouce
> Prenez l'origine au point de départ de la goutte. Au sommet, que vaut la composante verticale de la vitesse ? Exprimez l'abscisse et l'ordonnée du sommet en fonction de $v_0$ et $\alpha$, puis écrivez que le sommet coïncide avec la position $(d\cos\varphi,\,d\sin\varphi)$ de l'insecte. Vous pouvez aussi utiliser le théorème de l'énergie mécanique pour la hauteur.


> [!success]- ✅ Correction
> $\tan\alpha = 2\tan\varphi$, soit $\alpha = \arctan(2\tan 36^\circ)\approx 55{,}5^\circ$ (indépendant de $d$ et de $v_0$).


> [!example]- 📝 Solution détaillée
> **Repère et position de la cible**
>
> On prend l'origine $O$ à la bouche du poisson, $\vec u_x$ horizontal vers l'insecte et $\vec u_y$ vertical ascendant. La goutte part de $O$ avec la vitesse $v_0$ sous l'angle $\alpha$. L'insecte est en
> $$x_c=d\cos\varphi\approx0{,}728~\text{m},\qquad y_c=d\sin\varphi\approx0{,}529~\text{m}.$$
>
> **Équations horaires et condition de sommet**
>
> La goutte n'est soumise qu'à son poids :
> $$x(t)=v_0\cos\alpha\;t,\qquad y(t)=v_0\sin\alpha\;t-\tfrac12 g\,t^2 .$$
> Le sommet est atteint à l'instant $t_S$ tel que $v_y(t_S)=v_0\sin\alpha-g\,t_S=0$, soit $t_S=\dfrac{v_0\sin\alpha}{g}$. Ses coordonnées sont
> $$x_S=\frac{v_0^2\sin\alpha\cos\alpha}{g},\qquad y_S=\frac{v_0^2\sin^2\alpha}{2g}.$$
>
> [![](/figures/td1_ex4_pa_phv111.svg)](/figures/td1_ex4_pa_phv111.svg)
>
> **Condition « l'insecte est au sommet »**
>
> On impose $x_S=x_c$ et $y_S=y_c$. Le rapport des deux équations élimine $v_0$ et $g$ :
> $$\frac{y_S}{x_S}=\frac{\sin\alpha}{2\cos\alpha}=\frac{\tan\alpha}{2}=\frac{y_c}{x_c}=\tan\varphi,$$
> donc
> $$\boxed{\tan\alpha=2\tan\varphi}.$$
> Le résultat ne dépend ni de $d$ ni de $v_0$.
>
> **Application numérique**
>
> Avec $\varphi=36^\circ$ : $\tan36^\circ\approx0{,}7265$, donc $\tan\alpha\approx1{,}453$ et
> $$\boxed{\alpha=\arctan(1{,}453)\approx55{,}5^\circ}.$$
> L'angle de tir est nettement supérieur à l'angle de visée ($36^\circ$) : le poisson doit « viser au-dessus » de l'insecte.
>
> **Méthode alternative : théorème de l'énergie mécanique**
>
> La goutte n'est soumise qu'à son poids, force conservative : $E_m=\tfrac12 m v^2+m g y$ est constante. Entre le lancement ($y=0$, $v=v_0$) et le sommet ($y=y_S$, $v=v_S=v_0\cos\alpha$, car la composante horizontale de la vitesse est conservée et $v_y=0$) :
> $$\tfrac12 m v_0^2=\tfrac12 m v_0^2\cos^2\alpha+m g\,y_S\;\Longrightarrow\; y_S=\frac{v_0^2\sin^2\alpha}{2g}.$$
> On retrouve la même hauteur de sommet que par la cinématique. Avec en plus $x_S=v_0\cos\alpha\;t_S$ et $t_S=v_0\sin\alpha/g$, on conclut comme ci-dessus. Cette méthode évite d'écrire $y(t)$, mais ne se passe pas de la conservation de $v_x$.
>
> **Vitesse de tir nécessaire (complément)**
>
> De $y_S=y_c$ on tire $v_0^2=\dfrac{2g\,y_c}{\sin^2\alpha}$. Avec $y_c\approx0{,}529$ m et $\sin^2(55{,}5^\circ)\approx0{,}679$ :
> $$v_0\approx\sqrt{\frac{2\times9{,}81\times0{,}529}{0{,}679}}\approx3{,}9~\text{m/s},\qquad t_S=\frac{v_0\sin\alpha}{g}\approx0{,}33~\text{s}.$$
> Vérification avec l'abscisse : $x_S=v_0^2\sin\alpha\cos\alpha/g\approx15{,}3\times0{,}467/9{,}81\approx0{,}73~\text{m}=x_c$. $\surd$


**q2.** (*) Entraînement : que se passe-t-il si le poisson tire directement vers l'insecte ($\alpha=\varphi$) avec la même vitesse $v_0$ ? Au niveau de l'insecte, la goutte passe-t-elle au-dessus ou en dessous ?

> [!tip]- 💡 Coup de pouce
> Calculez l'ordonnée $y(t)$ de la goutte à l'instant où son abscisse vaut $x_c=d\cos\varphi$.


> [!success]- ✅ Correction
> La goutte passe en dessous de l'insecte, d'une hauteur $\dfrac{g\,x_c^2}{2v_0^2\cos^2\varphi}$.


> [!example]- 📝 Solution détaillée
> **Tir direct**
>
> Avec $\alpha=\varphi$, la goutte atteint l'abscisse $x_c$ à $t_c=\dfrac{x_c}{v_0\cos\varphi}$ et son ordonnée vaut
> $$y(t_c)=x_c\tan\varphi-\frac{g\,x_c^2}{2v_0^2\cos^2\varphi}=y_c-\frac{g\,x_c^2}{2v_0^2\cos^2\varphi}<y_c .$$
> La goutte passe donc **sous** l'insecte, de la quantité $\Delta y=\dfrac{g\,x_c^2}{2v_0^2\cos^2\varphi}$ : c'est la chute due à la gravité pendant la durée du vol. Avec $v_0\approx3{,}9$ m/s, $\Delta y\approx0{,}26$ m : le tir direct manque nettement sa cible, ce qui justifie que le poisson doive tirer au-dessus de la ligne de visée.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex1-mouvement-a-2-dimensions|Exercice 1 — Mouvement à 2 dimensions]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex2-balle-de-golf-mouvement-de-projectile|Exercice 2 — Balle de golf (mouvement de projectile)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex8-mouvement-circulaire-en-base-cartesienne|Exercice 8 — Mouvement circulaire en base cartésienne]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex10-planeur-en-ascendance-trajectoire-helicoidale|Exercice 10 — Planeur en ascendance : trajectoire hélicoïdale]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex11-la-valve-du-velo-cycloide-d-une-roue-qui-roule|Exercice 11 — La valve du vélo : cycloïde d'une roue qui roule]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex12-equations-horaires-2d-ou-3d|Exercice 12 — (*) Équations horaires 2D ou 3D]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex2-mouvement-circulaire-en-base-polaire|Exercice 2 — Mouvement circulaire en base polaire]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex3-cardioide|Exercice 3 — Cardioïde]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex4-mouvement-helicoidal-extension-en-3d|Exercice 4 — Mouvement hélicoïdal (extension en 3D)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex5-perle-sur-une-tige-tournante|Exercice 5 — Perle sur une tige tournante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex6-spirale-equiangulaire-trajectoire-d-approche-d-un-faucon|Exercice 6 — Spirale équiangulaire (trajectoire d'approche d'un faucon)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex7-courbe-de-poursuite-les-trois-drones|Exercice 7 — Courbe de poursuite : les trois drones]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex8-ellipse-de-kepler-loi-des-aires-et-hodographe|Exercice 8 — Ellipse de Kepler, loi des aires et hodographe]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex6-parabole-de-s-rete-et-tir-sur-une-pente|Exercice 6 — Parabole de sûreté et tir sur une pente]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-cartesiennes/ex9-derivee-d-un-vecteur-unitaire-tournant|Exercice 9 — Dérivée d'un vecteur unitaire tournant]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/cinematique-en-coordonnees-polaires-2d-et-cylindriques-3d/ex1-coordonnees-cartesiennes-et-polaires|Exercice 1 — Coordonnées cartésiennes et polaires]]

