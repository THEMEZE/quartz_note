---
title: "Exercice 1 — Base de Frenet : démonstrations de cours et applications"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td3_PhV111_corrige.pdf) · [📄 Énoncé](/pdfs/td3_PhV111_enonces.pdf) · [📄 Aides](/pdfs/td3_PhV111_aides.pdf) · [📄 Fiche enseignant](/pdfs/td3_PhV111_fiche.pdf)

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


> [!success]- ✅ Correction
> (b) $\vec\tau=\cos\alpha\,\vec u_x+\sin\alpha\,\vec u_y$, $\vec n=-\sin\alpha\,\vec u_x+\cos\alpha\,\vec u_y$, $\dfrac{\mathrm d\vec\tau}{\mathrm d\alpha}=\vec n$, $\dfrac{\mathrm d\vec n}{\mathrm d\alpha}=-\vec\tau$. (c) $\mathrm ds=\|\mathrm d\overrightarrow{OM}\|$, $s=\int\|\vec v\|\,\mathrm dt$. (d) $\mathrm d\overrightarrow{OM}=\mathrm ds\,\vec\tau$.


> [!example]- 📝 Solution détaillée
> **(a) Construction de la base**
>
> On trace en $M$ la tangente à la courbe ; $\vec\tau$ est le vecteur unitaire porté par cette tangente, orienté dans le **sens du mouvement**. Le vecteur $\vec n$ est le vecteur unitaire perpendiculaire à $\vec\tau$ obtenu par rotation de $+\pi/2$, c'est-à-dire dirigé vers le **côté concave** de la courbe (vers le point d'intersection $C$ des normales en $M$ et $M'$). On vérifie sur la figure que $\vec n$ est du même côté que $C$.
>
> **(b) Composantes cartésiennes**
>
> $\vec\tau$ fait l'angle $\alpha$ avec $Ox$ :
> $$\boxed{\vec\tau=\cos\alpha\,\vec u_x+\sin\alpha\,\vec u_y},\qquad\boxed{\vec n=-\sin\alpha\,\vec u_x+\cos\alpha\,\vec u_y}$$
> (pour $\mathrm d\alpha>0$, c'est-à-dire courbe qui tourne vers la gauche ; pour $\mathrm d\alpha<0$ on prend $\vec n$ de signe opposé afin qu'il pointe toujours vers le centre de courbure). On vérifie $\|\vec\tau\|=\|\vec n\|=1$ et $\vec\tau\cdot\vec n=-\cos\alpha\sin\alpha+\sin\alpha\cos\alpha=0$. En dérivant par rapport à $\alpha$ :
> $$\boxed{\frac{\mathrm d\vec\tau}{\mathrm d\alpha}=\vec n},\qquad\boxed{\frac{\mathrm d\vec n}{\mathrm d\alpha}=-\vec\tau}.$$
> La dérivée de chaque vecteur est l'autre, à un signe près : propriété identique à celle de $(\vec u_r,\vec u_\theta)$ avec $\theta\to\alpha$.
>
> **(c) Abscisse curviligne**
>
> L'**abscisse curviligne** $s$ est la longueur de l'arc de trajectoire parcourue, comptée à partir d'une origine choisie sur la courbe et dans le sens du mouvement : $\mathrm ds=\|\mathrm d\overrightarrow{OM}\|=\|\vec v\|\,\mathrm dt$, donc
> $$s(t)=\int_{t_0}^t\|\vec v(t')\|\,\mathrm dt'.$$
> Elle est croissante si l'on parcourt la courbe toujours dans le même sens ($\dot s=\|\vec v\|>0$).
>
> **(d) Déplacement élémentaire**
>
> Pour un déplacement infinitésimal, la corde $MM'$ se confond avec l'arc et avec la tangente :
> $$\boxed{\mathrm d\overrightarrow{OM}=\mathrm ds\,\vec\tau}.$$
> Seul le terme tangent subsiste : il n'y a pas de composante selon $\vec n$ au premier ordre. (Comparer à la base polaire : $\mathrm d\overrightarrow{OM}=\mathrm dr\,\vec u_r+r\,\mathrm d\theta\,\vec u_\theta$.)


**q2.** (a) Écrire le vecteur vitesse $\vec v$ dans la base de Frenet.

(b) Le rayon $R$ du cercle osculateur en $M$ est donné par $\dfrac1R=\left|\dfrac{\mathrm d\alpha}{\mathrm ds}\right|$. Démontrer que, dans la base de Frenet, l'accélération s'écrit
    $$\vec a=\frac{\mathrm dv}{\mathrm dt}\,\vec\tau+\frac{v^2}R\,\vec n.$$

(c) Si le mouvement est uniforme, comment s'écrit l'accélération dans la base de Frenet ? Que dire de l'angle entre $\vec a$ et $\vec v$ ?

> [!tip]- 💡 Coup de pouce
> Pour (f), dérivez $\vec v=v\,\vec\tau$ par rapport au temps (dérivée d'un produit), puis écrivez $\dfrac{\mathrm d\vec\tau}{\mathrm dt}=\dfrac{\mathrm d\vec\tau}{\mathrm d\alpha}\dfrac{\mathrm d\alpha}{\mathrm ds}\dfrac{\mathrm ds}{\mathrm dt}$ et utilisez (b) et la définition de $R$.


> [!success]- ✅ Correction
> (e) $\vec v=\dot s\,\vec\tau=v\,\vec\tau$. (f) $\dfrac{\mathrm d\vec\tau}{\mathrm dt}=\dfrac vR\,\vec n$ donc $\vec a=\dot v\,\vec\tau+\dfrac{v^2}R\,\vec n$. (g) $v=$ cte : $\vec a=\dfrac{v^2}R\,\vec n\perp\vec v$.


> [!example]- 📝 Solution détaillée
> **(e) Vecteur vitesse**
>
> $\vec v=\dfrac{\mathrm d\overrightarrow{OM}}{\mathrm dt}=\dfrac{\mathrm ds}{\mathrm dt}\,\vec\tau$, soit
> $$\boxed{\vec v=\dot s\,\vec\tau=v\,\vec\tau},\qquad v=\|\vec v\|=\dot s.$$
> La vitesse est **toujours tangente** à la trajectoire : elle n'a aucune composante selon $\vec n$.
>
> **(f) Accélération**
>
> On dérive $\vec v=v\,\vec\tau$ :
> $$\vec a=\frac{\mathrm dv}{\mathrm dt}\,\vec\tau+v\,\frac{\mathrm d\vec\tau}{\mathrm dt}.$$
> Le vecteur $\vec\tau$ dépend du temps par l'intermédiaire de $\alpha(s(t))$ :
> $$\frac{\mathrm d\vec\tau}{\mathrm dt}=\frac{\mathrm d\vec\tau}{\mathrm d\alpha}\,\frac{\mathrm d\alpha}{\mathrm ds}\,\frac{\mathrm ds}{\mathrm dt}=\frac{\mathrm d\vec\tau}{\mathrm d\alpha}\,\frac{\mathrm d\alpha}{\mathrm ds}\,v.$$
> On oriente $\vec n$ vers le centre de courbure : alors $\dfrac{\mathrm d\alpha}{\mathrm ds}\,\dfrac{\mathrm d\vec\tau}{\mathrm d\alpha}=\dfrac1R\,\vec n$ (le signe éventuel de $\mathrm d\alpha$ est absorbé dans l'orientation de $\vec n$, et $\left|\dfrac{\mathrm d\alpha}{\mathrm ds}\right|=\dfrac1R$). Donc $\dfrac{\mathrm d\vec\tau}{\mathrm dt}=\dfrac vR\,\vec n$ et
> $$\boxed{\vec a=\frac{\mathrm dv}{\mathrm dt}\,\vec\tau+\frac{v^2}R\,\vec n}.$$
> **Interprétation :** $a_T=\dot v$ traduit la variation de la **norme** de la vitesse ; $a_N=v^2/R$ traduit la rotation du **vecteur vitesse**, toujours dirigée vers le centre de courbure. Vérification dimensionnelle : $[v^2/R]=\mathrm{L^2T^{-2}/L}=\mathrm{LT^{-2}}$.
>
> **(g) Mouvement uniforme**
>
> Si $v=$ cte, $\dot v=0$ :
> $$\boxed{\vec a=\frac{v^2}R\,\vec n}.$$
> L'accélération est purement **normale**, dirigée vers le centre de courbure, donc **perpendiculaire à $\vec v$** : $\vec a\cdot\vec v=0$. Elle est nulle seulement pour $R=\infty$ (trajectoire rectiligne). Pour un cercle de rayon $R_0$, on retrouve $a=v^2/R_0=R_0\omega^2$.


**q3.** **2/ Expression du rayon de courbure $R$.**


(a) Calculer $\|\vec a\wedge\vec v\|$ à partir des expressions de $\vec v$ et de $\vec a$ dans la base de Frenet.

(b) En déduire une formule pour le rayon $R$ du cercle osculateur, indépendante du système de coordonnées.

(c) Donner l'expression du rayon $R$, appelé rayon de courbure, en coordonnées cartésiennes (mouvement plan).

(d) Que devient $R$ pour une trajectoire plane d'équation $y=y(x)$ ?

> [!tip]- 💡 Coup de pouce
> $\vec\tau\wedge\vec\tau=\vec0$ et $\vec n\wedge\vec\tau=-\vec k$. Pour (c), écrivez $\vec v=(\dot x,\dot y)$ et $\vec a=(\ddot x,\ddot y)$. Pour (d), prenez $x$ comme paramètre : $\dot x=1$, $\ddot x=0$.


> [!success]- ✅ Correction
> (a) $\|\vec a\wedge\vec v\|=\dfrac{v^3}R$. (b) $R=\dfrac{v^3}{\|\vec a\wedge\vec v\|}$. (c) $R=\dfrac{(\dot x^2+\dot y^2)^{3/2}}{|\dot x\ddot y-\dot y\ddot x|}$. (d) $R=\dfrac{(1+y'^2)^{3/2}}{|y''|}$.


> [!example]- 📝 Solution détaillée
> **(a) Produit vectoriel**
>
> $\vec a\wedge\vec v=\left(a_T\,\vec\tau+a_N\,\vec n\right)\wedge v\,\vec\tau=a_Nv\,\vec n\wedge\vec\tau=-a_Nv\,\vec k$ puisque $\vec\tau\wedge\vec\tau=\vec0$. Donc
> $$\|\vec a\wedge\vec v\|=a_Nv=\frac{v^3}R.$$
>
> **(b) Formule intrinsèque**
>
> $$\boxed{R=\frac{\|\vec v\|^3}{\|\vec a\wedge\vec v\|}}.$$
> Cette formule ne fait intervenir que $\vec v$ et $\vec a$ : elle est valable en 2D comme en 3D, dans n'importe quel système de coordonnées. On en déduit aussi $\boxed{a_N=\dfrac{\|\vec a\wedge\vec v\|}v}$.
>
> **(c) En coordonnées cartésiennes (plan)**
>
> $\vec a\wedge\vec v=(\ddot x\,\dot y-\ddot y\,\dot x)\,\vec k$ et $v=\sqrt{\dot x^2+\dot y^2}$ :
> $$\boxed{R=\frac{\left(\dot x^2+\dot y^2\right)^{3/2}}{\left|\dot x\,\ddot y-\dot y\,\ddot x\right|}}.$$
> En 3D : $R=\dfrac{(\dot x^2+\dot y^2+\dot z^2)^{3/2}}{\|\vec v\wedge\vec a\|}$ avec les trois composantes du produit vectoriel.
>
> **(d) Courbe $y=y(x)$**
>
> En prenant $x$ comme paramètre ($R$ ne dépend pas de la paramétrisation) : $\dot x=1$, $\ddot x=0$, $\dot y=y'$, $\ddot y=y''$ :
> $$\boxed{R=\frac{\left(1+y'^2\right)^{3/2}}{|y''|}}.$$
> Cas limites : $y''=0$ (droite, point d'inflexion) donne $R=\infty$ ; en un extremum de $y$ ($y'=0$) : $R=1/|y''|$.


**q4.** (a) (*) Même question pour une courbe plane en coordonnées polaires $r=r(\theta)$.

(b) **Application.** Déterminer le rayon de courbure des courbes suivantes :
    

- $y(x)=\exp(x)$ pour $x=0$ ;
- $r(\theta)=a\,(1-\cos\theta)$ pour $\theta=\pi$ ;
- $x(t)=a\cos\omega t$, $y(t)=b\sin\omega t$ pour $t=0$ ;
- $r(\theta)=\dfrac p{1+e\cos\theta}$ (ellipse) pour $\theta=0$.

> [!tip]- 💡 Coup de pouce
> Pour (e), prenez $\theta$ comme paramètre : $\dot\theta=1$, $\ddot\theta=0$, donc $\vec v=r'\,\vec u_r+r\,\vec u_\theta$ et $\vec a=(r''-r)\,\vec u_r+2r'\,\vec u_\theta$, puis utilisez $R=v^3/|v_ra_\theta-v_\theta a_r|$. Pour (f), choisissez la formule adaptée à chaque courbe.


> [!success]- ✅ Correction
> (e) $R=\dfrac{(r^2+r'^2)^{3/2}}{|r^2+2r'^2-r\,r''|}$. (f) $2\sqrt2$ ; $\dfrac43a$ ; $\dfrac{b^2}a$ ; $p$.


> [!example]- 📝 Solution détaillée
> **(e) Rayon de courbure en polaire**
>
> On paramètre la courbe par $\theta$ lui-même ($\dot\theta=1$, $\ddot\theta=0$, $\dot r=r'$, $\ddot r=r''$). Avec les formules du TD2 :
> $$\vec v=r'\,\vec u_r+r\,\vec u_\theta,\qquad\vec a=(r''-r)\,\vec u_r+2r'\,\vec u_\theta.$$
> Dans la base orthonormée $(\vec u_r,\vec u_\theta)$ : $v_ra_\theta-v_\theta a_r=2r'^2-r(r''-r)=r^2+2r'^2-r\,r''$ et $v^2=r^2+r'^2$ :
> $$\boxed{R=\frac{\left(r^2+r'^2\right)^{3/2}}{\left|r^2+2r'^2-r\,r''\right|}}.$$
> Vérification : cercle $r=R_0$, $r'=r''=0$ : $R=R_0^3/R_0^2=R_0$.
>
> **(f) $y=\mathrm e^x$ en $x=0$**
>
> $y'=y''=\mathrm e^x$, donc $y'(0)=y''(0)=1$ et $R=\dfrac{(1+1)^{3/2}}{1}=\boxed{2\sqrt2\approx2{,}83}$ (en unités de longueur).
>
> **(f) Cardioïde $r=a(1-\cos\theta)$ en $\theta=\pi$**
>
> $r'=a\sin\theta$, $r''=a\cos\theta$. En $\theta=\pi$ : $r=2a$, $r'=0$, $r''=-a$. Numérateur : $(4a^2)^{3/2}=8a^3$ ; dénominateur : $4a^2+0-2a\cdot(-a)=6a^2$. Donc
> $$R=\frac{8a^3}{6a^2}=\boxed{\tfrac43\,a}.$$
> Plus généralement $R=\tfrac43a\left|\sin\tfrac\theta2\right|$ : $R\to0$ au point de rebroussement $\theta=0$.
>
> **(f) Ellipse paramétrique en $t=0$**
>
> $\vec v=(-a\omega\sin\omega t,\ b\omega\cos\omega t)$ et $\vec a=-\omega^2(a\cos\omega t,\ b\sin\omega t)$. En $t=0$ : $\vec v=(0,b\omega)$ et $\vec a=(-a\omega^2,0)$, donc $v=b\omega$ et $\|\vec v\wedge\vec a\|=|0\cdot0-b\omega\cdot(-a\omega^2)|=ab\omega^3$ :
> $$R=\frac{b^3\omega^3}{ab\omega^3}=\boxed{\frac{b^2}a}.$$
> Par symétrie, en $t=\pi/2$ (extrémité du petit axe) : $R=a^2/b$. Pour $a=b$ : $R=a$ (cercle).
>
> **(f) Ellipse polaire $r=p/(1+e\cos\theta)$ en $\theta=0$**
>
> $r'=\dfrac{p\,e\sin\theta}{(1+e\cos\theta)^2}$ ; en $\theta=0$ : $r=\dfrac p{1+e}$, $r'=0$ et $r''=\dfrac{p\,e\cos\theta}{(1+e\cos\theta)^2}+\dots=\dfrac{p\,e}{(1+e)^2}$ (les autres termes contiennent $\sin\theta$). Alors $R=\dfrac{r^3}{r^2-r\,r''}=\dfrac{r^2}{r-r''}$ avec $r-r''=\dfrac p{1+e}-\dfrac{p\,e}{(1+e)^2}=\dfrac p{(1+e)^2}$ et $r^2=\dfrac{p^2}{(1+e)^2}$ :
> $$R=\boxed{p}.$$
> Le rayon de courbure au périhélie est le **paramètre** de l'ellipse. Cohérence avec l'ellipse paramétrique : $R=\dfrac{b^2}a=p$ (car $b^2=ap$).


**q5.** **3/ Accélération tangentielle $a_T$ et accélération normale $a_N$.**


(a) Montrer que dans un mouvement curviligne quelconque on a $a_T=\dfrac{\vec a\cdot\vec v}v$ et $a_N=\dfrac{\|\vec a\wedge\vec v\|}v$.

(b) Déterminer l'expression de $a_T$ pour un mobile de coordonnées $x(t)$, $y(t)$ et $z(t)$.

(c) Même question pour $a_N$.

> [!tip]- 💡 Coup de pouce
> $\vec a\cdot\vec v=(a_T\,\vec\tau+a_N\,\vec n)\cdot v\,\vec\tau$. Pour (c), $a^2=a_T^2+a_N^2$ évite de calculer le produit vectoriel à 3 composantes.


> [!success]- ✅ Correction
> (a) $\vec a\cdot\vec v=a_Tv$ et $\|\vec a\wedge\vec v\|=a_Nv$. (b) $a_T=\dfrac{\dot x\ddot x+\dot y\ddot y+\dot z\ddot z}{\sqrt{\dot x^2+\dot y^2+\dot z^2}}$. (c) $a_N=\sqrt{\ddot x^2+\ddot y^2+\ddot z^2-a_T^2}$.


> [!example]- 📝 Solution détaillée
> **(a) Les deux composantes**
>
> $\vec a\cdot\vec v=(a_T\,\vec\tau+a_N\,\vec n)\cdot v\,\vec\tau=a_Tv$ car $\vec\tau\cdot\vec\tau=1$ et $\vec n\cdot\vec\tau=0$ : $\boxed{a_T=\dfrac{\vec a\cdot\vec v}v}$ (projection de $\vec a$ sur $\vec\tau$). Le calcul du 2(a) donne $\|\vec a\wedge\vec v\|=a_Nv$ : $\boxed{a_N=\dfrac{\|\vec a\wedge\vec v\|}v}$. On retrouve que $a_T=\dot v$ : $\dfrac{\mathrm d(v^2)}{\mathrm dt}=2\vec v\cdot\vec a$ donne $v\dot v=\vec a\cdot\vec v$.
>
> **(b) $a_T$ en cartésien**
>
> $$\boxed{a_T=\frac{\dot x\ddot x+\dot y\ddot y+\dot z\ddot z}{\sqrt{\dot x^2+\dot y^2+\dot z^2}}}.$$
>
> **(c) $a_N$ en cartésien**
>
> $$\boxed{a_N=\frac{\sqrt{(\dot y\ddot z-\dot z\ddot y)^2+(\dot z\ddot x-\dot x\ddot z)^2+(\dot x\ddot y-\dot y\ddot x)^2}}{\sqrt{\dot x^2+\dot y^2+\dot z^2}}}.$$
> Alternative plus rapide : $a_N=\sqrt{\ddot x^2+\ddot y^2+\ddot z^2-a_T^2}$. **Vérification** (obligatoire) : $a_T^2+a_N^2=\|\vec a\|^2$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex4-abscisse-curviligne-et-rayon-de-courbure-d-une-trajectoire-parabolique|Exercice 4 — Abscisse curviligne et rayon de courbure d'une trajectoire parabolique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex5-cycloide-point-d-une-roue-qui-roule-sans-glisser|Exercice 5 — Cycloïde : point d'une roue qui roule sans glisser]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex6-raccordement-routier-en-clothoide-courbure-variable-et-jerk|Exercice 6 — Raccordement routier en clothoïde (courbure variable et « jerk »)]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex2-mouvement-curviligne-uniforme-cercle-parabole-applications|Exercice 2 — Mouvement curviligne uniforme : cercle, parabole, applications]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex3-circuit-de-monaco-courbure-et-acceleration-a-vitesse-constante|Exercice 3 — Circuit de Monaco : courbure et accélération à vitesse constante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex7-cercle-d-adherence-freiner-et-tourner-en-meme-temps|Exercice 7 — Cercle d'adhérence : freiner et tourner en même temps]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex8-tir-parabolique-vu-dans-la-base-de-frenet|Exercice 8 — Tir parabolique vu dans la base de Frenet]]

