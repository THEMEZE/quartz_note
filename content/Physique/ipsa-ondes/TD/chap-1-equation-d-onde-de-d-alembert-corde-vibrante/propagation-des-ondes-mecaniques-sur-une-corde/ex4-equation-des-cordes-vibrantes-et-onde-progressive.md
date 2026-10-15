---
title: "Exercice 4 — Équation des cordes vibrantes et onde progressive"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td1_PhV212_corrige.pdf) · [📄 Énoncé](/pdfs/td1_PhV212_enonce.pdf) · [📄 Aides (td1_PhV212_aides)](/pdfs/td1_PhV212_aides.pdf) · [📄 Aides (td1_PhV212_exs_maison_aide)](/pdfs/td1_PhV212_exs_maison_aide.pdf) · [📄 PDF (td1_ex1_coup_de_pouce)](/pdfs/td1_ex1_coup_de_pouce.pdf) · [📄 PDF (td1_ex1_solution_detaillee)](/pdfs/td1_ex1_solution_detaillee.pdf) · [📄 Fiche enseignant (td1_PhV212_fiche)](/pdfs/td1_PhV212_fiche.pdf) · [📄 Fiche enseignant (td1_ex1_fiche)](/pdfs/td1_ex1_fiche.pdf) · [📄 Fiche enseignant (td1_exs_maison_fiche)](/pdfs/td1_exs_maison_fiche.pdf)

### Exercice 4. Équation des cordes vibrantes et onde progressive

Une corde homogène et inextensible, de masse linéique $\mu$, est tendue
horizontalement (suivant l'axe $Ox$) avec une tension $F$ constante. La corde,
déplacée de sa position d'équilibre en $x=0$, acquiert un mouvement décrit
à l'instant $t$ par le déplacement $y(x,t)$ quasi vertical.

À l'instant $t$, la tension $\vec{T}(x,t)$ exercée par la partie droite sur la
partie gauche fait un angle petit $\alpha(x,t)$ avec l'axe horizontal. On néglige
les forces de pesanteur. Le déplacement transversal $y(x,t)$ obéit à l'équation :
$$\dfrac{\partial^2 y}{\partial x^2} = \dfrac{1}{c^2}\dfrac{\partial^2 y}{\partial t^2}$$

[![Schémat tronçon de corde](/figures/td1_ex3_phv212_demo.svg)](/figures/td1_ex3_phv212_demo.svg)

**q1.** Quelle est la nature de l'onde $y(x,t)$ créée par la perturbation sur la corde ?
Soyez aussi précis que possible. Exprimer la célérité $c$ de l'onde en fonction de $F$ et de $\mu$.

> [!tip]- 💡 Coup de pouce
> **Nature de l'onde et PFD**
>
> Réfléchissez à la direction du déplacement $y$ par rapport à la direction de propagation $x$.
> Pour exprimer $c$, appliquez le PFD projeté transversalement sur un tronçon $[x, x+dx]$.


> [!success]- ✅ Correction
> **Synthèse**
>
> Il s'agit d'une **onde plane transversale progressive** se propageant le long de l'axe $Ox$.
> La célérité vaut $c = \sqrt{F/\mu}$.


> [!example]- 📝 Solution détaillée
> **Démonstration complète**
>
> - **Nature :** Le déplacement particulaire $y(x,t)$ est perpendiculaire à l'axe de propagation $Ox$ : l'onde est donc **transversale**. En l'absence d'obstacles, elle est **plane et progressive et linéaire**.
>
> **Démonstration complète**
>
> - **Expression de $c$ :** On applique un PFD au tronçon de corde compris entre les points $A=(x,y(x,t))$ et $B=(x+dx,y(x+dx,t))$. 
>
>
> - Le référentiel du laboratoire est supposé galiléen.
> - Le système est le tronçon $AB$, de longueur $d\ell$ et de masse $dm=\mu\,d\ell$. Pour $dx\to0$, \[ dy=y(x+dx,t)-y(x,t) =\partial_x y(x,t)\,dx+o(dx), \] d'où \[ d\ell =\sqrt{dx^2+dy^2} =|dx|\sqrt{1+\left(\frac{dy}{dx}\right)^2} =|dx|\sqrt{1+\left(\partial_x y\right)^2+o(1)}. \] Dans l'approximation des faibles pentes $\left|\partial_x y\right|\ll1$, \[ d\ell =|dx|\left[ 1+\frac12\left(\partial_x y\right)^2 +o\!\left(\left(\partial_x y\right)^2\right) \right] \underset{(\partial_x y)^2\ll1}{=} |dx|\left[1+o(1)\right] \underset{(\partial_x y)^2\ll1}{\simeq} |dx|. \] En prenant $dx>0$, on obtient finalement \[ \boxed{d\ell\underset{(\partial_x y)^2\ll1}{\simeq}dx}, \qquad \boxed{dm=\mu\,d\ell\underset{(\partial_x y)^2\ll1}{\simeq}\mu\,dx}. \]
> - Le poids du tronçon de la corde est négligé. Le système et sous mis aux force de tension $\vec{T}(x, t )$ et  $\vec{T}(x + dx, t )$ tel que 
>   $$
>   \vec{T}(x, t ) = F \left ( \begin{array}{c} - \cos\alpha(x,t) \\ -\sin\alpha(x,t) \end{array} \right )_{\vec{e}_x , \vec{e}_y }, \quad \vec{T}(x + dx , t ) = F \left ( \begin{array}{c} \cos\alpha(x+ dx,t) \\ \sin\alpha(x+ dx,t) \end{array} \right )_{\vec{e}_x , \vec{e}_y }.
>   $$
>
>   $$
>   d m\, \left ( \begin{array}{c} \frac{\partial^2 x}{\partial t^2} \\ \frac{\partial^2 y}{\partial t^2} \end{array} \right )_{\vec{e}_x , \vec{e}_y } = \overbrace{F \left ( \begin{array}{c} - \cos\alpha(x,t) \\ -\sin\alpha(x,t) \end{array} \right )_{\vec{e}_x , \vec{e}_y }}^{\vec{T}(x, t )} + \overbrace{F \left ( \begin{array}{c} \cos\alpha(x+ dx,t) \\ \sin\alpha(x+ dx,t) \end{array} \right )_{\vec{e}_x , \vec{e}_y }}^{\vec{T}(x + dx, t )}
>   $$
>
> [![](/figures/td1_ex3_phv212_demo.svg)](/figures/td1_ex3_phv212_demo.svg)
>
> **Démonstration complète**
>
> - **PFD projeté sur $\vec e_x$ :**
>   Le PFD appliqué au tronçon $[x,x+dx]$, de masse $dm=\mu\,dx$, donne
>   \[
>     \mu\,dx\,\frac{\partial^2 x}{\partial t^2}
>     =
>     F\cos\alpha(x+dx,t)-F\cos\alpha(x,t).
>   \]
>   Pour de petits angles,
>   \[
>     \cos\alpha
>     =1-\frac{\alpha^2}{2}+o(\alpha^2)
>     \underset{|\alpha|\ll1}{=}
>     1-\frac{\alpha^2}{2}+o(\alpha^2),
>   \]
>   d'où
>   \[
>     F\cos\alpha(x+dx,t)-F\cos\alpha(x,t)
>     =
>     -\frac{F}{2}
>     \left[
>       \alpha^2(x+dx,t)-\alpha^2(x,t)
>     \right]
>     +o(\alpha^2).
>   \]
>   Or, dans l'approximation des faibles pentes,
>   \[
>     \tan\alpha=\frac{\partial y}{\partial x}
>     \qquad\Longrightarrow\qquad
>     \alpha
>     \underset{|\alpha|\ll1}{=}
>     \frac{\partial y}{\partial x}
>     +o\!\left(\frac{\partial y}{\partial x}\right).
>   \]
>   Ainsi, la composante longitudinale des forces est d'ordre
>   \[
>     O\!\left(\left(\frac{\partial y}{\partial x}\right)^2\right),
>   \]
>   et donc négligeable devant les termes d'ordre $1$ dans l'approximation linéaire :
>   \[
>     \boxed{
>     \frac{\partial^2 x}{\partial t^2}
>     \underset{|\partial_x y|\ll1}{=}
>     O\!\left((\partial_x y)^2\right)
>     }.
>   \]
>   Le mouvement longitudinal est donc négligé à l'ordre $1$ ; on ne conserve que le mouvement transverse.
>
> **Démonstration complète**
>
> - **PFD projeté sur $\vec e_y$ :**
>   La projection verticale du PFD donne
>   \[
>     \mu\,dx\,\frac{\partial^2 y}{\partial t^2}
>     =
>     F\sin\alpha(x+dx,t)-F\sin\alpha(x,t).
>   \]
>   Pour $|\alpha|\ll1$,
>   \[
>     \sin\alpha
>     =\alpha+o(\alpha)
>     \underset{|\alpha|\ll1}{=}
>     \tan\alpha+o(\alpha)
>     =
>     \frac{\partial y}{\partial x}
>     +o\!\left(\frac{\partial y}{\partial x}\right).
>   \]
>   On obtient alors, à l'ordre $1$,
>   \[
>     \mu\,dx\,\frac{\partial^2 y}{\partial t^2}
>     \underset{|\partial_x y|\ll1}{=}
>     F\left[
>       \frac{\partial y}{\partial x}(x+dx,t)
>       -
>       \frac{\partial y}{\partial x}(x,t)
>     \right]
>     +o(dx).
>   \]
>   Or
>   \[
>     \frac{\partial y}{\partial x}(x+dx,t)
>     -
>     \frac{\partial y}{\partial x}(x,t)
>     =
>     \frac{\partial^2y}{\partial x^2}\,dx+o(dx),
>   \]
>   d'où
>   \[
>     \mu\,dx\,\frac{\partial^2 y}{\partial t^2}
>     =
>     F\,\frac{\partial^2y}{\partial x^2}\,dx
>     +o(dx).
>   \]
>   En divisant par $dx$ et en prenant la limite $dx\to0$,
>   \[
>     \boxed{
>     \frac{\partial^2y}{\partial t^2}
>     =
>     \frac{F}{\mu}\frac{\partial^2y}{\partial x^2}
>     }.
>   \]
>   En identifiant avec l'équation de d'Alembert
>   \[
>     \frac{\partial^2y}{\partial t^2}
>     =
>     c^2\frac{\partial^2y}{\partial x^2},
>   \]
>   on obtient finalement
>   \[
>     \boxed{c=\sqrt{\frac{F}{\mu}}}.
>   \]
>
>
>
>   %Le PFD appliqué sur un tronçon $[x, x+dx]$ de masse $dm = \mu\,dx$ s'écrit en projection verticale :
>   %$$\mu\,dx\,\frac{\partial^2 y}{\partial t^2} = F\sin\alpha(x+dx,t) - F\sin\alpha(x,t)$$
>   %Pour de petits angles, $\sin\alpha \approx \tan\alpha = \dfrac{\partial y}{\partial x}$. Ainsi :
>   %$$\mu\,dx\,\frac{\partial^2 y}{\partial t^2} \approx F\left[\frac{\partial y}{\partial x}(x+dx,t) - \frac{\partial y}{\partial x}(x,t)\right] = F\,\frac{\partial^2 y}{\partial x^2}\,dx$$
>   %En simplifiant par $dx$, on identifie à l'équation de d'Alembert $\dfrac{\partial^2 y}{\partial x^2} = \dfrac{1}{c^2}%\dfrac{\partial^2 y}{\partial t^2}$ avec $c = \sqrt{\dfrac{F}{\mu}}$.


**q2.** Comment est modifiée l'équation d'onde si on ne néglige plus le poids de la corde ?

> [!tip]- 💡 Coup de pouce
> **Ajout de la pesanteur**
>
> Le poids du tronçon $dm\cdot g = \mu\,g\,dx$ s'ajoute vers le bas dans le bilan des forces transversales.


> [!success]- ✅ Correction
> **Nouvelle équation**
>
> $\dfrac{\partial^2 y}{\partial x^2} - \dfrac{\mu g}{F} = \dfrac{1}{c^2}\dfrac{\partial^2 y}{\partial t^2}$ (ou l'apparition d'un terme source lié au poids).


> [!example]- 📝 Solution détaillée
> **Établissement**
>
> En incluant le poids $\vec{dP} = -\mu g\,dx\,\vec{e}_y$, le PFD projeté donne :
> $$\mu\,dx\,\frac{\partial^2 y}{\partial t^2} = F\,\frac{\partial^2 y}{\partial x^2}\,dx - \mu g\,dx$$
> En divisant par $F\,dx$, on obtient :
> $$\frac{\partial^2 y}{\partial x^2} - \frac{\mu g}{F} = \frac{1}{c^2}\frac{\partial^2 y}{\partial t^2}$$
> Ce terme constant déforme la position d'équilibre (la corde prend la forme d'une chaînette/parabole au repos), mais n'affecte pas la vitesse de propagation $c$ des petites perturbations autour de cette position d'équilibre.
>
> [![](/figures/td1_ex3_phv212_demo_poidg.svg)](/figures/td1_ex3_phv212_demo_poidg.svg)


Une corde vibrante très longue, de masse linéique $\mu = 0.12$ kg/m et de tension $F = 20$ N,
est le siège d'une onde progressive sinusoïdale transversale d'amplitude $a = 2$ mm et de longueur d'onde $\lambda = 0.25$ m.


**3.**

  **a)** Dans ce cas, calculer la vitesse de propagation $c$ de l'onde.

> [!tip]- 💡 Coup de pouce
> **Calcul direct**
>
> Appliquez la formule $c = \sqrt{F/\mu}$ avec les valeurs numériques de la question.


> [!success]- ✅ Correction
> **Résultat**
>
> $c = \sqrt{20 / 0.12} \approx 12.9\ \text{m/s}$.


> [!example]- 📝 Solution détaillée
> **Application numérique**
>
> $c = \sqrt{\dfrac{F}{\mu}} = \sqrt{\dfrac{20}{0.12}} = \sqrt{166.67} \approx 12.91\ \text{m/s}$.


  **b)** Calculer la vitesse transversale maximale d'un élément de corde. Que remarquez-vous ?

> [!tip]- 💡 Coup de pouce
> **Vitesse particulaire vs célérité**
>
> L'onde s'écrit $y(x,t) = a\cos(kx - \omega t + \phi)$. La vitesse transversale est $v_y = \partial_t y$. Son maximum est $v_{\text{max}} = a\omega$ avec $\omega = 2\pi c / \lambda$.


> [!success]- ✅ Correction
> **Résultat**
>
> $v_{\text{max}} = a\omega = a\dfrac{2\pi c}{\lambda} \approx 2\cdot 10^{-3} \times \dfrac{2\pi \times 12.91}{0.25} \approx 0.65\ \text{m/s}$.
> On remarque que $v_{\text{max}} \ll c$ ($0.65\ \text{m/s} \ll 12.91\ \text{m/s}$).


> [!example]- 📝 Solution détaillée
> **Détail du calcul**
>
> La vitesse d'un point de la corde est $v_y(x,t) = \dfrac{\partial y}{\partial t} = a\omega \sin(kx - \omega t + \phi)$.
> L'amplitude maximale de cette vitesse est $v_{\text{max}} = a\,\omega$.
> Comme $\omega = 2\pi f = \dfrac{2\pi c}{\lambda}$ :
> $$v_{\text{max}} = a \frac{2\pi c}{\lambda} = 2\times 10^{-3} \times \frac{2\pi \times 12.91}{0.25} \approx 0.649\ \text{m/s}$$
> **Remarque :** La vitesse maximale de déplacement de la matière ($0.65$ m/s) est très inférieure à la vitesse de propagation du signal/de l'onde $c$ ($12.91$ m/s).


  **c)** Calculer la composante transversale maximale de la tension en un point quelconque de la corde.

> [!tip]- 💡 Coup de pouce
> **Projection de la tension**
>
> La composante transversale de la tension est $T_y = F\sin\alpha \approx F \dfrac{\partial y}{\partial x}$.


> [!success]- ✅ Correction
> **Résultat**
>
> $T_{y,\text{max}} = F\,k\,a = F\dfrac{2\pi}{\lambda}a = 20 \times \dfrac{2\pi}{0.25} \times 2\cdot 10^{-3} \approx 1.01\ \text{N}$.


> [!example]- 📝 Solution détaillée
> **Détail du calcul**
>
> $T_y(x,t) = F \frac{\partial y}{\partial x} = -F\,k\,a \sin(kx - \omega t + \phi)$.
> Son module maximal vaut :
> $$T_{y,\text{max}} = F\,k\,a = F \frac{2\pi}{\lambda} a = 20 \times \frac{2\pi}{0.25} \times 2\times 10^{-3} \approx 1.005\ \text{N}$$


  **d)** Quelle est la phase de l'onde lorsque ces deux maxima (vitesse et tension transversale) sont atteints ?
Calculer le déplacement correspondant $y(x,t)$ de l'élément de corde.

> [!tip]- 💡 Coup de pouce
> **Analyse des fonctions sinus / cosinus**
>
> Examinez la phase $\Phi(x,t) = kx - \omega t + \phi$ lorsque $\sin\Phi(x,t) = \pm 1$. Que vaut $\cos\Phi(x,t)$ à cet instant ?


> [!success]- ✅ Correction
> **Résultat**
>
> Phase : $\Phi = \pi/2 [\pi]$.
> Déplacement correspondant : $y(x,t) = 0$ (la corde passe par sa position d'équilibre).


> [!example]- 📝 Solution détaillée
> **Raisonnement pas à pas**
>
> $v_y$ et $T_y$ sont toutes deux proportionnelles à $\sin(kx - \omega t + \phi)$.
> Leur valeur maximale en module est atteinte quand $|\sin(kx - \omega t + \phi)| = 1$, soit pour une phase :
> $$\Phi(x,t) = kx - \omega t + \phi = \frac{\pi}{2} \quad [\pi]$$
> À cet instant, le cosinus est nul ($\cos\Phi = 0$), d'où :
> $$y(x,t) = a\cos\Phi(x,t) = 0$$
> Les maxima de vitesse transversale et de tension transversale ont lieu simultanément au moment où l'élément de corde passe par sa position d'équilibre ($y=0$).


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex8-energie-et-puissance-d-une-onde-sur-une-corde-impedance-caracteristique|Exercice 8 — Énergie et puissance d'une onde sur une corde : impédance caractéristique]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex10-corde-discrete-chaine-de-masses-dispersion-coupure-et-vitesse-de-groupe|Exercice 10 — Corde discrète (chaîne de masses) : dispersion, coupure et vitesse de groupe]]

