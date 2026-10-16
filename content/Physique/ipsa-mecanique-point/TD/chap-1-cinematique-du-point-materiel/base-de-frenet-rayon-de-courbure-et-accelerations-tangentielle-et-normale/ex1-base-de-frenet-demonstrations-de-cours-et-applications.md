---
title: "Exercice 1 — Base de Frenet : démonstrations de cours et applications"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/index|⬅ Retour]] · <a href="/pdfs/td3_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td3_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 1. Base de Frenet : démonstrations de cours et applications

La figure 1 représente la trajectoire d'un point matériel $M$ dans le plan $Oxy$. En $M$, la tangente à la
courbe fait l'angle $\alpha$ avec l'axe $Ox$ (cet angle est noté $\theta$ dans certains énoncés ; on le note $\alpha$
ici pour ne pas le confondre avec l'angle polaire du TD2). Le point $M'$ de la trajectoire est voisin de $M$, et la
tangente en $M'$ fait l'angle $\alpha+\mathrm d\alpha$ avec $Ox$. On note $\mathrm ds$ la longueur de l'arc $MM'$.

**q1.** **1/ Vitesse et accélération en base de Frenet (partie 1).**


(a) Représenter la base de Frenet $(\vec\tau,\vec n)$ associée au point $M$ sur la figure 1.

(b) Exprimer les vecteurs $\vec\tau$ et $\vec n$ dans la base cartésienne $(\vec u_x,\vec u_y)$ en fonction de $\alpha$. Établir une relation entre $\dfrac{\mathrm d\vec\tau}{\mathrm d\alpha}$ et $\vec n$, et entre $\dfrac{\mathrm d\vec n}{\mathrm d\alpha}$ et $\vec\tau$.

(c) Donner la définition de l'abscisse curviligne $s$.

(d) Donner l'expression du déplacement élémentaire $\mathrm d\overrightarrow{OM}$ dans la base de Frenet.

> [!tip]- 💡 Coup de pouce
> $\vec\tau$ est tangent à la courbe et dirigé dans le sens du mouvement : il fait l'angle $\alpha$ avec $Ox$. $\vec n$ lui est perpendiculaire, vers l'intérieur du virage. Pour (c), pensez à la longueur d'un petit segment $\|\mathrm d\overrightarrow{OM}\|$.


**q2.** (a) Écrire le vecteur vitesse $\vec v$ dans la base de Frenet.

(b) Le rayon $R$ du cercle osculateur en $M$ est donné par $\dfrac1R=\left|\dfrac{\mathrm d\alpha}{\mathrm ds}\right|$. Démontrer que, dans la base de Frenet, l'accélération s'écrit
    $$\vec a=\frac{\mathrm dv}{\mathrm dt}\,\vec\tau+\frac{v^2}R\,\vec n.$$

(c) Si le mouvement est uniforme, comment s'écrit l'accélération dans la base de Frenet ? Que dire de l'angle entre $\vec a$ et $\vec v$ ?

> [!tip]- 💡 Coup de pouce
> Pour (f), dérivez $\vec v=v\,\vec\tau$ par rapport au temps (dérivée d'un produit), puis écrivez $\dfrac{\mathrm d\vec\tau}{\mathrm dt}=\dfrac{\mathrm d\vec\tau}{\mathrm d\alpha}\dfrac{\mathrm d\alpha}{\mathrm ds}\dfrac{\mathrm ds}{\mathrm dt}$ et utilisez (b) et la définition de $R$.


**q3.** **2/ Expression du rayon de courbure $R$.**


(a) Calculer $\|\vec a\wedge\vec v\|$ à partir des expressions de $\vec v$ et de $\vec a$ dans la base de Frenet.

(b) En déduire une formule pour le rayon $R$ du cercle osculateur, indépendante du système de coordonnées.

(c) Donner l'expression du rayon $R$, appelé rayon de courbure, en coordonnées cartésiennes (mouvement plan).

(d) Que devient $R$ pour une trajectoire plane d'équation $y=y(x)$ ?

> [!tip]- 💡 Coup de pouce
> $\vec\tau\wedge\vec\tau=\vec0$ et $\vec n\wedge\vec\tau=-\vec k$. Pour (c), écrivez $\vec v=(\dot x,\dot y)$ et $\vec a=(\ddot x,\ddot y)$. Pour (d), prenez $x$ comme paramètre : $\dot x=1$, $\ddot x=0$.


**q4.** (a) (*) Même question pour une courbe plane en coordonnées polaires $r=r(\theta)$.

(b) **Application.** Déterminer le rayon de courbure des courbes suivantes :
    

- $y(x)=\exp(x)$ pour $x=0$ ;
- $r(\theta)=a\,(1-\cos\theta)$ pour $\theta=\pi$ ;
- $x(t)=a\cos\omega t$, $y(t)=b\sin\omega t$ pour $t=0$ ;
- $r(\theta)=\dfrac p{1+e\cos\theta}$ (ellipse) pour $\theta=0$.

> [!tip]- 💡 Coup de pouce
> Pour (e), prenez $\theta$ comme paramètre : $\dot\theta=1$, $\ddot\theta=0$, donc $\vec v=r'\,\vec u_r+r\,\vec u_\theta$ et $\vec a=(r''-r)\,\vec u_r+2r'\,\vec u_\theta$, puis utilisez $R=v^3/|v_ra_\theta-v_\theta a_r|$. Pour (f), choisissez la formule adaptée à chaque courbe.


**q5.** **3/ Accélération tangentielle $a_T$ et accélération normale $a_N$.**


(a) Montrer que dans un mouvement curviligne quelconque on a $a_T=\dfrac{\vec a\cdot\vec v}v$ et $a_N=\dfrac{\|\vec a\wedge\vec v\|}v$.

(b) Déterminer l'expression de $a_T$ pour un mobile de coordonnées $x(t)$, $y(t)$ et $z(t)$.

(c) Même question pour $a_N$.

> [!tip]- 💡 Coup de pouce
> $\vec a\cdot\vec v=(a_T\,\vec\tau+a_N\,\vec n)\cdot v\,\vec\tau$. Pour (c), $a^2=a_T^2+a_N^2$ évite de calculer le produit vectoriel à 3 composantes.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex4-abscisse-curviligne-et-rayon-de-courbure-d-une-trajectoire-parabolique|Exercice 4 — Abscisse curviligne et rayon de courbure d'une trajectoire parabolique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex5-cycloide-point-d-une-roue-qui-roule-sans-glisser|Exercice 5 — Cycloïde : point d'une roue qui roule sans glisser]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex6-raccordement-routier-en-clothoide-courbure-variable-et-jerk|Exercice 6 — Raccordement routier en clothoïde (courbure variable et « jerk »)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex2-mouvement-curviligne-uniforme-cercle-parabole-applications|Exercice 2 — Mouvement curviligne uniforme : cercle, parabole, applications]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex3-circuit-de-monaco-courbure-et-acceleration-a-vitesse-constante|Exercice 3 — Circuit de Monaco : courbure et accélération à vitesse constante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex7-cercle-d-adherence-freiner-et-tourner-en-meme-temps|Exercice 7 — Cercle d'adhérence : freiner et tourner en même temps]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex8-tir-parabolique-vu-dans-la-base-de-frenet|Exercice 8 — Tir parabolique vu dans la base de Frenet]]

