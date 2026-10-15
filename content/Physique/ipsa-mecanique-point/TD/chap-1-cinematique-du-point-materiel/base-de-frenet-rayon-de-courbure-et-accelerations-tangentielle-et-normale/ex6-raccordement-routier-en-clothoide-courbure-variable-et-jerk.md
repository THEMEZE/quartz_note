---
title: "Exercice 6 — Raccordement routier en clothoïde (courbure variable et « jerk »)"
tags:
  - td
  - chap-1-cinematique-du-point-materiel
---

[[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td3_PhV111_corrige.pdf) · [📄 Énoncé](/pdfs/td3_PhV111_enonces.pdf) · [📄 Aides](/pdfs/td3_PhV111_aides.pdf) · [📄 Fiche enseignant](/pdfs/td3_PhV111_fiche.pdf)

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


> [!success]- ✅ Correction
> (a) $\dfrac{\mathrm d\alpha}{\mathrm ds}=\dfrac s{A^2}$ donc $\alpha=\dfrac{s^2}{2A^2}$ ; $R=\dfrac{A^2}s$ ; $R(0)=\infty$, $R(L)=R_f$ si $L=\dfrac{A^2}{R_f}$ ; $\alpha(L)=\dfrac L{2R_f}$. (b) $x=\displaystyle\int_0^s\cos\frac{\sigma^2}{2A^2}\mathrm d\sigma$, $y=\int_0^s\sin\frac{\sigma^2}{2A^2}\mathrm d\sigma$ ; DL : $y\simeq\dfrac{s^3}{6A^2}$.


> [!example]- 📝 Solution détaillée
> **(a) Angle et rayon**
>
> La courbure vaut $\kappa=\dfrac1R=\dfrac s{A^2}=\dfrac{\mathrm d\alpha}{\mathrm ds}$ (virage dans le sens trigonométrique). Intégrer avec $\alpha(0)=0$ :
> $$\boxed{\alpha(s)=\frac{s^2}{2A^2}},\qquad\boxed{R(s)=\frac{A^2}s}.$$
> En $s=0$ : $\alpha=0$, $R=\infty$ (droite). En $s=L$ (fin du raccordement, raccord au cercle de rayon $R_f$) : $R(L)=R_f$ donne $\boxed{L=\dfrac{A^2}{R_f}}$ et $\alpha_f=\dfrac{L^2}{2A^2}=\dfrac L{2R_f}$ : l'angle de déviation est la moitié de celui d'un arc de cercle de même longueur et de rayon $R_f$.
>
> **(b) Équations paramétriques**
>
> $$x(s)=\int_0^s\cos\frac{\sigma^2}{2A^2}\,\mathrm d\sigma,\qquad y(s)=\int_0^s\sin\frac{\sigma^2}{2A^2}\,\mathrm d\sigma.$$
> Ces intégrales ne s'expriment pas avec des fonctions usuelles : on les relie aux intégrales de Fresnel. Pour $\alpha\ll1$, $\cos\alpha\simeq1-\dfrac{\alpha^2}2$ et $\sin\alpha\simeq\alpha$ :
> $$\boxed{x\simeq s-\frac{s^5}{40A^4}\simeq s},\qquad\boxed{y\simeq\frac{s^3}{6A^2}}.$$
> Donc $y\simeq\dfrac{x^3}{6A^2}$ : une **parabole cubique**, expression utilisée en topographie pour le tracé. À $s=L$ : $y(L)\simeq\dfrac{L^3}{6A^2}=\dfrac{L^2}{6R_f}$.


**q2.** **2/ Cinématique et confort.** Le véhicule parcourt la clothoïde à vitesse $v$ constante, avec $s=vt$.


(a) Calculer $a_T$, $a_N$ en fonction de $t$ et le vecteur accélération dans la base de Frenet. Montrer que le jerk latéral $j=\dfrac{\mathrm da_N}{\mathrm dt}$ est constant et vaut $\dfrac{v^3}{A^2}$.

(b) Comparer à un raccordement brutal droite $\to$ cercle de rayon $R_f$ : quelle est la valeur de $a_N$ juste après le raccord ? Quel est le jerk ?

> [!tip]- 💡 Coup de pouce
> $v=$ cte donc $a_T=0$ et $a_N=v^2/R=v^2s/A^2$ avec $s=vt$.


> [!success]- ✅ Correction
> (c) $a_T=0$, $a_N=\dfrac{v^3t}{A^2}$, $j=\dfrac{v^3}{A^2}$ constant. (d) Brutal : $a_N$ passe de $0$ à $\dfrac{v^2}{R_f}$ en $\Delta t\to0$ : jerk infini (en pratique très élevé).


> [!example]- 📝 Solution détaillée
> **(c) Accélération et jerk**
>
> $v$ constante donc $a_T=\dot v=0$ et
> $$\boxed{\vec a=\frac{v^2}{R}\,\vec n=\frac{v^2s}{A^2}\,\vec n=\frac{v^3t}{A^2}\,\vec n}.$$
> L'accélération normale croît **linéairement avec le temps** ; son taux de variation est le jerk latéral :
> $$\boxed{j=\frac{\mathrm da_N}{\mathrm dt}=\frac{v^3}{A^2}}=\text{cte}.$$
> Dimension : $[v^3/A^2]=\mathrm{L^3T^{-3}/L^2}=\mathrm{LT^{-3}}$ $\surd$.
>
> **(d) Comparaison avec un raccordement brutal**
>
> Sans raccordement : $a_N=0$ sur la droite, puis $a_N=\dfrac{v^2}{R_f}$ dès l'entrée sur le cercle. Le saut est instantané : $j\to\infty$ (en pratique, l'effet est limité par la souplesse de la direction et de la suspension, mais l'à-coup est brutal : la voiture « se jette » de côté). Avec la clothoïde, $a_N$ monte de $0$ à $v^2/R_f$ en la durée $\dfrac Lv$ avec une pente constante $j$ : le conducteur tourne son volant à vitesse **constante**, ce qui est naturel.


**q3.** **3/ Dimensionnement.** Une route est conçue pour $v=90\ \mathrm{km/h}$, avec un virage de rayon $R_f=300\ \mathrm m$ et un jerk latéral maximal admissible $j_{\max}=0{,}6\ \mathrm{m\,s^{-3}}$.


(a) Calculer le paramètre $A$ de la clothoïde, la longueur $L$ de raccordement, sa durée de parcours, l'accélération normale finale et l'angle total dont la route a tourné à la fin du raccordement.

(b) Calculer le décalage latéral $y(L)$ de la route par rapport à la tangente initiale.

(c) Mêmes questions pour $130\ \mathrm{km/h}$ avec le même $j_{\max}$ et le même $R_f$ (autoroute). Commenter.

> [!tip]- 💡 Coup de pouce
> $j=v^3/A^2$ donc $A^2=v^3/j$ ; $L=A^2/R_f$ ; $a_{N,f}=v^2/R_f$ ; $\alpha_f=\dfrac L{2R_f}$ ; $y(L)\simeq\dfrac{L^2}{6R_f}$.


> [!success]- ✅ Correction
> $v=25\ \mathrm{m/s}$ : $A^2=26\,042\ \mathrm{m^2}$, $A\approx161\ \mathrm m$, $L\approx86{,}8\ \mathrm m$, $\Delta t=3{,}47\ \mathrm s$, $a_{N,f}=2{,}08\ \mathrm{m\,s^{-2}}$, $\alpha_f\approx0{,}145\ \mathrm{rad}=8{,}3^\circ$, $y(L)\approx4{,}2\ \mathrm m$. À $130\ \mathrm{km/h}$ : $L\approx262\ \mathrm m$ ($\times3$).


> [!example]- 📝 Solution détaillée
> **(e) Paramètres de la clothoïde**
>
> $v=\dfrac{90}{3{,}6}=25\ \mathrm{m/s}$. $A^2=\dfrac{v^3}{j_{\max}}=\dfrac{15\,625}{0{,}6}\approx2{,}60\times10^4\ \mathrm{m^2}$, soit $\boxed{A\approx161\ \mathrm m}$. Longueur : $\boxed{L=\dfrac{A^2}{R_f}=\dfrac{26\,042}{300}\approx87\ \mathrm m}$ ; durée $\Delta t=\dfrac Lv\approx3{,}5\ \mathrm s$. Accélération normale finale : $\dfrac{v^2}{R_f}=\dfrac{625}{300}\approx2{,}08\ \mathrm{m\,s^{-2}}$ (cohérent : $j\,\Delta t=0{,}6\times3{,}47=2{,}08$ $\surd$). Angle de déviation : $\alpha_f=\dfrac L{2R_f}\approx0{,}145\ \mathrm{rad}\approx8{,}3^\circ$.
>
> **(f) Décalage latéral**
>
> $y(L)\simeq\dfrac{L^3}{6A^2}=\dfrac{L^2}{6R_f}=\dfrac{(86{,}8)^2}{1\,800}\approx\boxed{4{,}2\ \mathrm m}$ (valeur exacte par intégration numérique : $4{,}18\ \mathrm m$, écart $<0{,}2\ \%$). Le décalage latéral de $4{,}2\ \mathrm m$ correspond à la largeur d'une voie : c'est l'ordre de grandeur du **ripage** (décalage latéral) que le tracé doit prévoir dans l'emprise de la route.
>
> **(g) Autoroute**
>
> $v=\dfrac{130}{3{,}6}\approx36{,}1\ \mathrm{m/s}$ ; $A^2=\dfrac{v^3}j\approx7{,}8\times10^4\ \mathrm{m^2}$ ; $L=\dfrac{A^2}{R_f}\approx261\ \mathrm m$, soit $(36{,}1/25)^3\approx3{,}0$ fois plus long : la longueur de raccordement croît comme $v^3$ (à $j$ et $R_f$ fixés) ; la durée de parcours $L/v\approx7{,}2\ \mathrm s$ croît comme $v^2$. Mais ici $a_{N,f}=v^2/R_f\approx4{,}3\ \mathrm m/s^2$ (soit $0{,}44\,g$) est déjà proche de la limite d'adhérence en conditions humides : on voit pourquoi les rayons minimaux augmentent avec la vitesse de conception ($R_f\gtrsim v^2/a_{\max}$).


**q4.** **4/ (*) Python.** Tracer la clothoïde avec \texttt{scipy.special.fresnel} pour $A=161\ \mathrm m$ et $s\in[0,L]$. Superposer, aux points $s=L/4,\ L/2,\ L$ : $\vec\tau$, $\vec n$ et le cercle osculateur. Vérifier numériquement $y(L)$ et le comparer à $L^2/(6R_f)$.

> [!tip]- 💡 Coup de pouce
> Avec $u=\dfrac s{A\sqrt\pi}$ : $x=A\sqrt\pi\,C(u)$, $y=A\sqrt\pi\,S(u)$ ; \texttt{S,C=fresnel(u)}. Centre du cercle : $M+R\,\vec n$ avec $\vec n=(-\sin\alpha,\cos\alpha)$.


> [!success]- ✅ Correction
> Résultat attendu : $x(L)\approx86{,}6\ \mathrm m$, $y(L)\approx4{,}18\ \mathrm m$ ; $L^2/6R_f=4{,}19\ \mathrm m$.


> [!example]- 📝 Solution détaillée
> **Script**
>
> \begin{verbatim}
> import numpy as np, matplotlib.pyplot as plt
> from scipy.special import fresnel
> A = 161.4; Rf = 300; L = A**2/Rf
> s = np.linspace(0, L, 400)
> S, C = fresnel(s/(A*np.sqrt(np.pi)))
> x, y = A*np.sqrt(np.pi)*C, A*np.sqrt(np.pi)*S
> alpha = s**2/(2*A**2); R = A**2/np.maximum(s, 1e-9)
> for sk in (L/4, L/2, L):
>     i = np.argmin(abs(s-sk))
>     n = np.array([-np.sin(alpha[i]), np.cos(alpha[i])])
>     c = np.array([x[i], y[i]]) + R[i]*n
>     plt.gca().add_patch(plt.Circle(c, R[i], fill=False, ls='--'))
> plt.plot(x, y); plt.axis('equal'); plt.show()
> print(x[-1], y[-1], L**2/(6*Rf))
> \end{verbatim}


> [!note] 🔗 Voir aussi
> [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex1-base-de-frenet-demonstrations-de-cours-et-applications|Exercice 1 — Base de Frenet : démonstrations de cours et applications]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex2-mouvement-curviligne-uniforme-cercle-parabole-applications|Exercice 2 — Mouvement curviligne uniforme : cercle, parabole, applications]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex3-circuit-de-monaco-courbure-et-acceleration-a-vitesse-constante|Exercice 3 — Circuit de Monaco : courbure et accélération à vitesse constante]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex4-abscisse-curviligne-et-rayon-de-courbure-d-une-trajectoire-parabolique|Exercice 4 — Abscisse curviligne et rayon de courbure d'une trajectoire parabolique]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex5-cycloide-point-d-une-roue-qui-roule-sans-glisser|Exercice 5 — Cycloïde : point d'une roue qui roule sans glisser]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex7-cercle-d-adherence-freiner-et-tourner-en-meme-temps|Exercice 7 — Cercle d'adhérence : freiner et tourner en même temps]] · [[physique/ipsa-mecanique-point/TD/chap-1-cinematique-du-point-materiel/base-de-frenet-rayon-de-courbure-et-accelerations-tangentielle-et-normale/ex8-tir-parabolique-vu-dans-la-base-de-frenet|Exercice 8 — Tir parabolique vu dans la base de Frenet]]

