---
title: "Exercice 6 — Raccordement routier en clothoïde (courbure variable et « jerk »)"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/index|⬅ Retour]] · <a href="/pdfs/td3_PhV111_enonces.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td3_PhV111_aides.pdf" target="_blank" rel="noopener">📄 Aides</a>

### Exercice 6. Raccordement routier en clothoïde (courbure variable et « jerk ») *(facultatif)*

Sur une route (ou une voie ferrée), le passage d'un alignement droit à un virage circulaire de rayon $R_f$ ne se
fait jamais brutalement : si le rayon passait instantanément de $\infty$ à $R_f$, l'accélération normale
$a_N=v^2/R$ ferait un **saut** (le conducteur serait « jeté » de côté) et le volant devrait être tourné
instantanément. On intercale donc un **raccordement progressif** dont la courbure croît **linéairement avec
l'abscisse curviligne** :
$$\frac1{R(s)}=\frac s{A^2},\qquad A>0\ \text{constante (en mètres)},$$
courbe appelée **clothoïde** (ou spirale d'Euler, spirale de Cornu). L'abscisse curviligne $s$ est comptée depuis
le début du raccordement, où la route est rectiligne et tangente à $Ox$. Un véhicule la parcourt à vitesse de norme
$v$ constante.

**q1.** **1/ La courbe.**


(a) Montrer que l'angle de la tangente avec $Ox$ est $\alpha(s)=\dfrac{s^2}{2A^2}$ et que $R(s)=\dfrac{A^2}s$. Que valent $\alpha$ et $R$ en $s=0$ et en $s=L$ ?

(b) Écrire $x(s)$ et $y(s)$ sous forme intégrale. Pour $\alpha\ll1$, montrer que $x\simeq s$ et $y\simeq\dfrac{s^3}{6A^2}$ : la clothoïde se confond avec une **parabole cubique**.

> [!tip]- 💡 Coup de pouce
> $\dfrac1R=\left|\dfrac{\mathrm d\alpha}{\mathrm ds}\right|$ avec $\alpha(0)=0$ (la route est d'abord tangente à $Ox$). Pour (b), $\dfrac{\mathrm dx}{\mathrm ds}=\cos\alpha$ et $\dfrac{\mathrm dy}{\mathrm ds}=\sin\alpha$.


**q2.** **2/ Cinématique et confort.** Le véhicule parcourt la clothoïde à vitesse $v$ constante, avec $s=vt$.


(a) Calculer $a_T$, $a_N$ en fonction de $t$ et le vecteur accélération dans la base de Frenet. Montrer que le jerk latéral $j=\dfrac{\mathrm da_N}{\mathrm dt}$ est constant et vaut $\dfrac{v^3}{A^2}$.

(b) Comparer à un raccordement brutal droite $\to$ cercle de rayon $R_f$ : quelle est la valeur de $a_N$ juste après le raccord ? Quel est le jerk ?

> [!tip]- 💡 Coup de pouce
> $v=$ cte donc $a_T=0$ et $a_N=v^2/R=v^2s/A^2$ avec $s=vt$.


**q3.** **3/ Dimensionnement.** Une route est conçue pour $v=90\ \mathrm{km/h}$, avec un virage de rayon $R_f=300\ \mathrm m$ et un jerk latéral maximal admissible $j_{\max}=0{,}6\ \mathrm{m\,s^{-3}}$.


(a) Calculer le paramètre $A$ de la clothoïde, la longueur $L$ de raccordement, sa durée de parcours, l'accélération normale finale et l'angle total dont la route a tourné à la fin du raccordement.

(b) Calculer le décalage latéral $y(L)$ de la route par rapport à la tangente initiale.

(c) Mêmes questions pour $130\ \mathrm{km/h}$ avec le même $j_{\max}$ et le même $R_f$ (autoroute). Commenter.

> [!tip]- 💡 Coup de pouce
> $j=v^3/A^2$ donc $A^2=v^3/j$ ; $L=A^2/R_f$ ; $a_{N,f}=v^2/R_f$ ; $\alpha_f=\dfrac L{2R_f}$ ; $y(L)\simeq\dfrac{L^2}{6R_f}$.


**q4.** **4/ (*) Python.** Tracer la clothoïde avec \texttt{scipy.special.fresnel} pour $A=161\ \mathrm m$ et $s\in[0,L]$. Superposer, aux points $s=L/4,\ L/2,\ L$ : $\vec\tau$, $\vec n$ et le cercle osculateur. Vérifier numériquement $y(L)$ et le comparer à $L^2/(6R_f)$.

> [!tip]- 💡 Coup de pouce
> Avec $u=\dfrac s{A\sqrt\pi}$ : $x=A\sqrt\pi\,C(u)$, $y=A\sqrt\pi\,S(u)$ ; \texttt{S,C=fresnel(u)}. Centre du cercle : $M+R\,\vec n$ avec $\vec n=(-\sin\alpha,\cos\alpha)$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex1-base-de-frenet-demonstrations-de-cours-et-applications|Exercice 1 — Base de Frenet : démonstrations de cours et applications]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex2-mouvement-curviligne-uniforme-cercle-parabole-applications|Exercice 2 — Mouvement curviligne uniforme : cercle, parabole, applications]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex3-circuit-de-monaco-courbure-et-acceleration-a-vitesse-constante|Exercice 3 — Circuit de Monaco : courbure et accélération à vitesse constante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex4-abscisse-curviligne-et-rayon-de-courbure-d-une-trajectoire-parabolique|Exercice 4 — Abscisse curviligne et rayon de courbure d'une trajectoire parabolique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex5-cycloide-point-d-une-roue-qui-roule-sans-glisser|Exercice 5 — Cycloïde : point d'une roue qui roule sans glisser]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex7-cercle-d-adherence-freiner-et-tourner-en-meme-temps|Exercice 7 — Cercle d'adhérence : freiner et tourner en même temps]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex8-tir-parabolique-vu-dans-la-base-de-frenet|Exercice 8 — Tir parabolique vu dans la base de Frenet]]

