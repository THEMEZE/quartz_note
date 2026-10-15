---
title: "Exercice 2 — Mouvement curviligne uniforme : cercle, parabole, applications"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td3_PhV111_corrige.pdf) · [📄 Énoncé](/pdfs/td3_PhV111_enonces.pdf) · [📄 Aides](/pdfs/td3_PhV111_aides.pdf) · [📄 Fiche enseignant](/pdfs/td3_PhV111_fiche.pdf)

### Exercice 2. Mouvement curviligne uniforme : cercle, parabole, applications

Un point matériel $M$ suit une trajectoire plane avec une vitesse $\vec v$ dont la **norme** $\|\vec v\|=v$ est
**constante**. On étudie ce mouvement pour une trajectoire circulaire, puis pour une trajectoire parabolique, et on
l'applique à des situations réelles (voiture, satellite, voltige aérienne).

**q1.** **1/ Mouvement circulaire uniforme.**


(a) Rappeler les grandeurs géométriques et cinématiques qui caractérisent le mouvement circulaire uniforme et les relations entre elles.

(b) Mettre les expressions obtenues en relation avec les expressions de la vitesse et de l'accélération dans la base de Frenet.

(c) Représenter la trajectoire sur un graphique et préciser, en différents points, la vitesse, l'accélération et la base de Frenet.

> [!tip]- 💡 Coup de pouce
> Pour (a), pensez à $R$, $\omega$, $T$, $f$, $v$, $a$. Pour (b), identifiez $\vec\tau$ et $\vec n$ dans la base polaire.


> [!success]- ✅ Correction
> (a) $R$, $\omega=\dot\theta$, $T=2\pi/\omega$, $f=1/T$, $v=R\omega$, $a=R\omega^2=v^2/R$, $s=R\theta=R\omega t$. (b) $\vec\tau=\vec u_\theta$, $\vec n=-\vec u_r$, $\vec v=R\omega\,\vec\tau$, $\vec a=\dfrac{v^2}R\,\vec n$. (c) $\vec v$ tangent, $\vec a$ vers le centre.


> [!example]- 📝 Solution détaillée
> **(a) Grandeurs caractéristiques**
>
> **Géométriques** : rayon $R$, centre $O$, angle $\theta$, abscisse curviligne $s=R\theta$ (arc parcouru). **Cinématiques** : vitesse angulaire $\omega=\dot\theta$ constante, période $T=\dfrac{2\pi}\omega$, fréquence $f=\dfrac1T=\dfrac\omega{2\pi}$, vitesse $v=R\omega$, accélération $a=R\omega^2=\dfrac{v^2}R=v\omega$. Relations : $\theta=\omega t$, $s=vt$, $v=\dfrac{2\pi R}T$.
>
> **(b) Lien avec la base de Frenet**
>
> En polaire, $\vec v=R\omega\,\vec u_\theta$ et $\vec a=-R\omega^2\,\vec u_r$. Comparons avec Frenet : $\vec\tau=\vec u_\theta$ (sens du mouvement pour $\omega>0$), $\vec n=-\vec u_r$ (vers le centre). Alors
> $$\vec v=v\,\vec\tau,\qquad\vec a=\frac{v^2}R\,\vec n,\qquad\dot v=0.$$
> La base de Frenet s'identifie à $(\vec u_\theta,-\vec u_r)$ : **elle tourne avec le mobile à la vitesse $\omega$**. Le rayon de courbure est le rayon du cercle : $R=R_0$ en tout point.
>
> **(c) Représentation**
>
> On dessine le cercle de centre $O$ et on place, aux points $\theta=0,\ \pi/2,\ \pi,\ 3\pi/2$, le vecteur $\vec v$ tangent au cercle (dans le sens trigonométrique pour $\omega>0$), le vecteur $\vec a$ dirigé de $M$ vers $O$ (même direction que $\vec n$), $\vec\tau$ et $\vec n$ unitaires. Les vecteurs $\vec v$ et $\vec a$ ont **même norme en tout point** ($R\omega$ et $R\omega^2$) mais **changent de direction**. Le centre de courbure est $O$ pour tous les points.


**q2.** **2/ Mouvement parabolique.** Le point $M$ décrit la parabole d'équation $y(x)=kx^2$ avec $k=1\ \mathrm{m^{-1}}$, à vitesse $v$ de norme constante.


(a) Calculer le rayon de courbure $R$, puis l'accélération $\vec a$ en $x=0$, puis en $x=1\ \mathrm m$.

(b) Représenter la trajectoire sur un graphique.

(c) Tracer sur la trajectoire les cercles osculateurs correspondant aux points $x=0$ et $x=1\ \mathrm m$, et représenter le vecteur accélération $\vec a$ en ces points.

> [!tip]- 💡 Coup de pouce
> Utilisez $R=\dfrac{(1+y'^2)^{3/2}}{|y''|}$ avec $y'=2kx$ et $y''=2k$. Puis $a=v^2/R$, dirigée selon $\vec n$ (vers le haut, côté concave). Pour le centre : $C=M+R\,\vec n$.


> [!success]- ✅ Correction
> $R(x)=\dfrac{(1+4k^2x^2)^{3/2}}{2k}$ ; $R(0)=0{,}5$ m, $a(0)=2v^2$ (vertical vers le haut) ; $R(1)=\dfrac{5\sqrt5}2\approx5{,}59$ m, $a(1)=\dfrac{2v^2}{5\sqrt5}\approx0{,}179\,v^2$, dirigée selon $\vec n=\dfrac{(-2,1)}{\sqrt5}$.


> [!example]- 📝 Solution détaillée
> **(a) Rayon de courbure et accélération**
>
> $y'=2kx$, $y''=2k$ :
> $$\boxed{R(x)=\frac{\left(1+4k^2x^2\right)^{3/2}}{2k}}.$$
> En $x=0$ : $R=\dfrac1{2k}=0{,}5\ \mathrm m$ et, $v$ étant constante, $a=\dfrac{v^2}R=2kv^2=2v^2$ ; $\vec a=2v^2\,\vec u_y$ (vers le haut, vers le centre $C_0=(0;0{,}5)$).
>
> En $x=1\ \mathrm m$ : $y'=2$, $R=\dfrac{5^{3/2}}2=\dfrac{5\sqrt5}2\approx5{,}59\ \mathrm m$, donc $a=\dfrac{v^2}R=\dfrac{2v^2}{5\sqrt5}\approx0{,}179\,v^2$. La direction de $\vec a$ est $\vec n$ : $\vec\tau=\dfrac{(1,2)}{\sqrt5}$, $\vec n=\dfrac{(-2,1)}{\sqrt5}$, soit $\vec a=a\,\vec n\approx v^2\,(-0{,}16;\ 0{,}08)$.
>
> **Rapport :** $\dfrac{a(0)}{a(1)}=\dfrac{R(1)}{R(0)}=5\sqrt5\approx11{,}2$ : l'accélération est plus de **dix fois plus grande** au sommet qu'en $x=1$, à vitesse égale.
>
> **(b) Trajectoire**
>
> Parabole de sommet $O$, d'axe $Oy$, ouverte vers le haut, passant par $(\pm1;1)$, $(\pm2;4)$. Elle est parcourue à vitesse de norme constante : le mobile « va plus vite horizontalement » au sommet et plus vite verticalement sur les bras.
>
> **(c) Cercles osculateurs**
>
> Pour $x=0$ : cercle de rayon $0{,}5$ centré en $(0;0{,}5)$ : il est tangent à la parabole en $O$ et reste **à l'intérieur** d'elle près du sommet (la parabole s'élargit plus vite que le cercle). Pour $x=1$ : centre $C_1=M+R\,\vec n=(1;1)+\dfrac{5\sqrt5}2\cdot\dfrac{(-2,1)}{\sqrt5}=(-4;\ 3{,}5)$ et rayon $5{,}59\ \mathrm m$ : un grand cercle de faible courbure. Le vecteur $\vec a$ est porté par la droite $MC$ en chaque point, dirigé vers le centre : court en $x=1$, long en $x=0$.


**q3.** **3/ (*) Applications.**


(a) Une voiture se déplace à la vitesse constante de $72\ \mathrm{km/h}$ sur une trajectoire de $100\ \mathrm m$ de rayon. Quelle est son accélération ?

(b) Un satellite est en orbite circulaire, à $640\ \mathrm{km}$ de la surface de la Terre, avec une période de $98{,}0$ minutes. Son mouvement étant circulaire uniforme, déterminer la vitesse du satellite. On donne le rayon de la Terre $R_T=6{,}37\times10^6\ \mathrm m$.

(c) La figure de couverture représente les voltiges d'avions acrobatiques. Représenter sur la figure les cercles osculateurs des trajectoires des trois avions aux points où se trouvent les trois avions.

> [!tip]- 💡 Coup de pouce
> (a) $a=v^2/R$ avec $v$ en $\mathrm{m/s}$. (b) $r=R_T+h$ puis $v=2\pi r/T$ avec $T$ en secondes. (c) Pour chaque avion : tangent à la trajectoire, centre du côté concave.


> [!success]- ✅ Correction
> (a) $a=4\ \mathrm{m\,s^{-2}}\approx0{,}41\,g$. (b) $r=7{,}01\times10^6\ \mathrm m$, $v=\dfrac{2\pi r}T\approx7{,}49\ \mathrm{km/s}$, $a=\dfrac{v^2}r\approx8{,}0\ \mathrm{m\,s^{-2}}$. (c) Construction géométrique.


> [!example]- 📝 Solution détaillée
> **(a) Voiture**
>
> $v=72/3{,}6=20\ \mathrm{m/s}$ ; $a=\dfrac{v^2}R=\dfrac{400}{100}=\boxed{4{,}0\ \mathrm{m\,s^{-2}}}\approx0{,}41\,g$. L'accélération est horizontale, perpendiculaire à la vitesse, dirigée vers le centre du virage. C'est l'ordre de grandeur d'un virage sportif sur route.
>
> **(b) Satellite**
>
> Rayon de l'orbite : $r=R_T+h=6{,}37\times10^6+0{,}640\times10^6=7{,}01\times10^6\ \mathrm m$. Période : $T=98{,}0\times60=5\,880\ \mathrm s$.
> $$v=\frac{2\pi r}T=\frac{2\pi\times7{,}01\times10^6}{5\,880}\approx\boxed{7{,}49\times10^3\ \mathrm{m/s}=7{,}49\ \mathrm{km/s}}\ (\approx27\,000\ \mathrm{km/h}).$$
> Accélération : $a=\dfrac{v^2}r\approx8{,}0\ \mathrm{m\,s^{-2}}$, très proche de $g(R_T/r)^2\approx8{,}1\ \mathrm{m\,s^{-2}}$ : le satellite est « en chute libre » autour de la Terre, ce qui prépare la dynamique.
>
> **(c) Cercles osculateurs des avions**
>
> Pour chaque avion : (1) tracer la tangente à la trajectoire à la position de l'avion ; (2) tracer la normale, du côté **concave** de la trajectoire ; (3) estimer le rayon en cherchant le cercle qui « colle » à la trajectoire sur un petit arc autour du point ; (4) tracer ce cercle. Un avion au sommet d'une boucle a un cercle osculateur dont le centre est **en dessous** ; un avion en bas de boucle a un centre **au-dessus** ; un avion sur un tronçon presque rectiligne a un très grand rayon (cercle presque une droite). Plus la trajectoire est serrée, plus le rayon est petit et plus le pilote subit une forte accélération $v^2/R$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex1-base-de-frenet-demonstrations-de-cours-et-applications|Exercice 1 — Base de Frenet : démonstrations de cours et applications]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex3-circuit-de-monaco-courbure-et-acceleration-a-vitesse-constante|Exercice 3 — Circuit de Monaco : courbure et accélération à vitesse constante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex4-abscisse-curviligne-et-rayon-de-courbure-d-une-trajectoire-parabolique|Exercice 4 — Abscisse curviligne et rayon de courbure d'une trajectoire parabolique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex5-cycloide-point-d-une-roue-qui-roule-sans-glisser|Exercice 5 — Cycloïde : point d'une roue qui roule sans glisser]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex6-raccordement-routier-en-clothoide-courbure-variable-et-jerk|Exercice 6 — Raccordement routier en clothoïde (courbure variable et « jerk »)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex7-cercle-d-adherence-freiner-et-tourner-en-meme-temps|Exercice 7 — Cercle d'adhérence : freiner et tourner en même temps]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex8-tir-parabolique-vu-dans-la-base-de-frenet|Exercice 8 — Tir parabolique vu dans la base de Frenet]]

