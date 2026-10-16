---
title: "Exercice 1 — Corde non homogène, jonction entre deux cordes"
tags:
  - td
  - chap-3-interfaces-entre-deux-milieux
---

[[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/index|⬅ Retour]] · <a href="/pdfs/td3_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_PhV212_enonce)</a> · <a href="/pdfs/td3_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_enonce)</a> · <a href="/pdfs/td3_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td3_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td3_PhV212_corrige)</a> · <a href="/pdfs/td3_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td3_corrige)</a> · <a href="/pdfs/td3_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 1. Corde non homogène, jonction entre deux cordes

Deux cordes de longueur $L$ et de masses linéiques $\mu_1$ et $\mu_2=\alpha\mu_1$
sont attachées en un point de jonction $O$ pour former une corde tendue
horizontalement suivant l'axe $Ox$ avec une force de tension $F$. Le point
$O$ se situe en l'abscisse $x=0$.

Une onde transversale progressive se propageant dans le sens des $x$
décroissants (onde incidente) arrive au niveau de la jonction $O$. Il
s'agit d'une onde sinusoïdale d'amplitude $A_I$ et de pulsation $\omega$.
Elle donne naissance à une onde réfléchie se propageant dans le sens des
$x$ croissants ainsi qu'à une onde transmise se propageant dans le sens
des $x$ décroissants. Ces deux ondes sont aussi sinusoïdales et
progressives, de même pulsation $\omega$.

<p style="text-align:center"><a href="/figures/td3_ex1_corde_double.svg" target="_blank" rel="noopener"><img src="/figures/td3_ex1_corde_double.svg" alt="Suggestion : schéma de la corde double, jonction en $O$ ($x=0$) ; représenter la corde 1 (masse linéique $\mu_1$) où vivent l'onde incidente et l'onde réfléchie, et la corde 2 (masse linéique $\mu_2=\alpha\mu_1$) où se propage l'onde transmise, avec des flèches indiquant clairement les trois sens de propagation ($x$ décroissants pour l'incidente et la transmise, $x$ croissants pour la réfléchie)." loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>

**q1.** Donner l'expression de l'onde incidente $y_i(x,t)$ se déplaçant dans le sens des $x$ décroissants, d'amplitude $A_I$ et de déphasage $\phi=0$.

> [!tip]- 💡 Coup de pouce
> Une onde progressive vers les $x$ décroissants s'écrit $\cos(\omega t + kx)$ (le signe $+$ devant $kx$ est ce qui inverse le sens de propagation par rapport à la convention $\cos(\omega t-kx)$ rappelée dans les prérequis).


> [!success]- ✅ Correction
> $y_i(x,t)=A_I\cos(\omega t + k_1 x)$.


> [!example]- 📝 Solution détaillée
> **Justification du signe**
>
> Une onde progressive s'écrit de façon générale $y=A\cos(\omega t \mp kx)$. Pour un point d'amplitude maximale (crête), l'argument doit rester constant au cours du temps : $\omega t \pm kx = \text{cte}$, soit $x(t) = \mp(\omega/k)t+\text{cte}$. Avec le signe $+$ (celui retenu ici), $\mathrm{d}x/\mathrm{d}t = -\omega/k = -c <0$ : la crête se déplace bien vers les $x$ décroissants, conformément à l'énoncé. On a donc, avec $A_I$ l'amplitude et $\varphi=0$ le déphasage imposé :
> $$\boxed{y_i(x,t) = A_I\cos(\omega t + k_1 x)}.$$
> L'indice $1$ sur $k$ signale que cette onde vit dans la corde 1 (de masse linéique $\mu_1$), là où se trouvent à la fois l'onde incidente et l'onde réfléchie.


**q2.** Donner l'expression de l'onde réfléchie $y_r(x,t)$ se déplaçant dans le sens des $x$ croissants, d'amplitude $A_R$ et de déphasage $\phi=0$.

> [!success]- ✅ Correction
> $y_r(x,t)=A_R\cos(\omega t - k_1 x)$.


> [!example]- 📝 Solution détaillée
> **Onde réfléchie**
>
> L'onde réfléchie repart en sens inverse de l'onde incidente, vers les $x$ croissants, tout en restant dans la même corde 1 (même $\mu_1$, donc même $k_1$ que l'onde incidente, la pulsation $\omega$ étant imposée par la source et donc commune à toutes les ondes du problème). En reprenant la convention $y=A\cos(\omega t-kx)$ pour une onde vers les $x$ croissants (cf. question 1) :
> $$\boxed{y_r(x,t) = A_R\cos(\omega t - k_1 x)}.$$


**q3.** Donner l'expression de l'onde transmise $y_t(x,t)$ se déplaçant dans le sens des $x$ décroissants, d'amplitude $A_T$ et de déphasage $\phi=0$.

> [!success]- ✅ Correction
> $y_t(x,t)=A_T\cos(\omega t + k_2 x)$.


> [!example]- 📝 Solution détaillée
> **Onde transmise**
>
> L'onde transmise poursuit sa route dans la corde 2 (masse linéique $\mu_2$, donc nombre d'onde $k_2\neq k_1$ en général), en conservant le même sens de propagation que l'onde incidente (vers les $x$ décroissants) et la même pulsation $\omega$ (imposée par la continuité temporelle en $O$, cf. question 4). D'après la convention établie en question 1 pour une onde vers les $x$ décroissants :
> $$\boxed{y_t(x,t) = A_T\cos(\omega t + k_2 x)}.$$


**q4.** Pour chaque corde, donner la relation entre $k$, $\omega$ et $c$. Comment s'appelle cette relation ? Exprimer $k_1$ en fonction de $k_2$ et $\alpha$.

> [!tip]- 💡 Coup de pouce
> Relation de dispersion $\omega=kc$ avec $c=\sqrt{F/\mu}$ propre à chaque corde (cf. point cours) ; la pulsation $\omega$ est la même des deux côtés car le régime est établi et le point $O$ oscille avec une seule et même pulsation (continuité temporelle en $O$).


> [!success]- ✅ Correction
> Relation de dispersion. $k_1=\omega/c_1=\omega\sqrt{\mu_1/F}$ et $k_2=\omega\sqrt{\mu_2/F}=\omega\sqrt{\alpha\mu_1/F}$, donc $k_1=k_2/\sqrt{\alpha}$.


> [!example]- 📝 Solution détaillée
> **Relation de dispersion propre à chaque corde**
>
> D'après le point cours, l'équation de d'Alembert admet des solutions progressives sinusoïdales à condition que $\omega=kc$ : c'est la **relation de dispersion** (ici non dispersive : $c$ ne dépend pas de $\omega$). Pour chaque corde, avec $c_i=\sqrt{F/\mu_i}$ :
> $$k_1 = \frac{\omega}{c_1} = \omega\sqrt{\frac{\mu_1}{F}}, \qquad k_2 = \frac{\omega}{c_2} = \omega\sqrt{\frac{\mu_2}{F}} = \omega\sqrt{\frac{\alpha\mu_1}{F}} = \sqrt{\alpha}\,k_1.$$
>
> **Relation entre $k_1$ et $k_2$**
>
> On en déduit immédiatement :
> $$\boxed{k_1 = \frac{k_2}{\sqrt{\alpha}}}.$$
> Le fait que $\omega$ soit identique pour les trois ondes (incidente, réfléchie, transmise) est une conséquence physique du régime sinusoïdal établi : le point $O$, commun aux deux cordes, oscille avec une unique fréquence, imposée par la source, quelle que soit la corde considérée.


**q5.** Exprimer les déplacements verticaux $y_1(x,t)$ et $y_2(x,t)$ sur les cordes 1 et 2 respectivement.

> [!success]- ✅ Correction
> $y_1=y_i+y_r=A_I\cos(\omega t+k_1x)+A_R\cos(\omega t-k_1x)$ ; $y_2=y_t=A_T\cos(\omega t+k_2x)$.


> [!example]- 📝 Solution détaillée
> **Superposition dans la corde 1, onde unique dans la corde 2**
>
> Dans la corde 1, les deux ondes (incidente et réfléchie) coexistent : par principe de superposition (l'équation de d'Alembert étant linéaire), le déplacement total est leur somme :
> $$y_1(x,t) = y_i(x,t)+y_r(x,t) = A_I\cos(\omega t+k_1x) + A_R\cos(\omega t-k_1x).$$
> Dans la corde 2, seule l'onde transmise existe (aucune onde n'y revient vers $O$, la corde étant supposée de longueur $L$ finie mais son extrémité lointaine non concernée par ce problème local de jonction) :
> $$y_2(x,t) = y_t(x,t) = A_T\cos(\omega t+k_2x).$$


**q6.** Écrire la condition de continuité sur le déplacement vertical $y(x,t)$ de la corde à la position $x=0$. Traduire cette relation en termes de $A_I$, $A_R$ et $A_T$.

> [!tip]- 💡 Coup de pouce
> $y_1(0,t)=y_2(0,t)$ à tout instant $t$ (cf.  point cours, condition 1).


> [!success]- ✅ Correction
> $A_I+A_R=A_T$.


> [!example]- 📝 Solution détaillée
> **Écriture et évaluation en $x=0$**
>
> La condition physique de continuité du déplacement (la corde ne se rompt pas en $O$) s'écrit $y_1(0,t)=y_2(0,t)$ pour tout $t$. En évaluant les expressions de la question 5 en $x=0$ :
> $$A_I\cos(\omega t) + A_R\cos(\omega t) = A_T\cos(\omega t).$$
> Cette égalité devant être vraie à tout instant $t$, et le facteur $\cos(\omega t)$ étant commun et non identiquement nul, on peut le simplifier, ce qui donne directement :
> $$\boxed{A_I+A_R=A_T}.$$


**q7.** La relation de continuité de la force en $x=0$ donne $\left.\partial y_1/\partial x\right|_{x=0} = \left.\partial y_2/\partial x\right|_{x=0}$. Traduire cette relation en termes de $A_I$, $A_R$ et $A_T$.

> [!tip]- 💡 Coup de pouce
> Dérivez $y_1$ et $y_2$ par rapport à $x$, puis évaluez en $x=0$ ; les cosinus deviennent des sinus qui s'annulent sauf le terme en $x$ dérivé, attention aux signes de $k_1$ dans $y_i$ et $y_r$ (cf. remarque pédagogique sur ce point).


> [!success]- ✅ Correction
> $k_1(A_I - A_R) = k_2 A_T$.


> [!example]- 📝 Solution détaillée
> **Dérivation de $y_1$ et $y_2$**
>
> On dérive séparément chaque terme de $y_1(x,t)=A_I\cos(\omega t+k_1x)+A_R\cos(\omega t-k_1x)$ par rapport à $x$ (attention au signe de $k_1$ dans chaque terme) :
> $$\frac{\partial y_1}{\partial x} = -A_I k_1 \sin(\omega t+k_1x) + A_R k_1 \sin(\omega t-k_1x).$$
> De même pour $y_2(x,t)=A_T\cos(\omega t+k_2x)$ :
> $$\frac{\partial y_2}{\partial x} = -A_T k_2\sin(\omega t+k_2x).$$
>
> **Évaluation en $x=0$ et simplification**
>
> En $x=0$ :
> $$\left.\frac{\partial y_1}{\partial x}\right|_0 = k_1(A_R-A_I)\sin(\omega t), \qquad \left.\frac{\partial y_2}{\partial x}\right|_0 = -k_2 A_T\sin(\omega t).$$
> En égalant (à tout instant $t$, donc en simplifiant par $\sin(\omega t)$) :
> $$k_1(A_R-A_I) = -k_2 A_T \quad\Longrightarrow\quad \boxed{k_1(A_I-A_R) = k_2 A_T}.$$


**q8.** En déduire les coefficients de réflexion $r$ et de transmission $t$, en amplitude, en fonction de $\alpha$. Écrire $r$ et $t$ en fonction des impédances des deux milieux après avoir défini $Z_1$ et $Z_2$, lesdites impédances.

> [!tip]- 💡 Coup de pouce
> Combinez les deux relations de continuité (questions 6 et 7) comme un système linéaire en $A_R,A_T$. Impédance mécanique d'une corde : $Z=\mu c=\sqrt{F\mu}$ (cf. point cours) ; attention, $Z$ et $k$ sont ici *directement* proportionnels (à $\omega,F$ fixés), et non inversement proportionnels.


> [!success]- ✅ Correction
> $r=\dfrac{k_1-k_2}{k_1+k_2}=\dfrac{1-\sqrt{\alpha}}{1+\sqrt{\alpha}}$,
> $t=\dfrac{2k_1}{k_1+k_2}=\dfrac{2}{1+\sqrt{\alpha}}$. En impédance :
> $r=\dfrac{Z_1-Z_2}{Z_1+Z_2}$, $t=\dfrac{2Z_1}{Z_1+Z_2}$.


> [!example]- 📝 Solution détaillée
> **Résolution du système en $(A_I,A_R,A_T)$**
>
> On dispose des deux relations
> $$A_I+A_R=A_T \qquad (\star), \qquad k_1(A_I-A_R)=k_2A_T \qquad (\star\star).$$
> On substitue $A_T$ de $(\star)$ dans $(\star\star)$ :
> $$k_1(A_I-A_R) = k_2(A_I+A_R) \quad\Longrightarrow\quad A_I(k_1-k_2) = A_R(k_1+k_2),$$
> d'où le coefficient de réflexion en amplitude :
> $$r = \frac{A_R}{A_I} = \frac{k_1-k_2}{k_1+k_2}.$$
> En reportant dans $(\star)$, $t=A_T/A_I=1+r$ :
> $$t = 1+\frac{k_1-k_2}{k_1+k_2} = \frac{2k_1}{k_1+k_2}.$$
>
> **Expression en fonction de $\alpha$**
>
> En utilisant $k_1=k_2/\sqrt{\alpha}$ (question 4), on divise numérateur et dénominateur par $k_2$, puis on multiplie par $\sqrt{\alpha}$ pour éliminer la fraction interne :
> $$r = \frac{1/\sqrt{\alpha}-1}{1/\sqrt{\alpha}+1} = \boxed{\frac{1-\sqrt{\alpha}}{1+\sqrt{\alpha}}}, \qquad t = \frac{2/\sqrt{\alpha}}{1/\sqrt{\alpha}+1} = \boxed{\frac{2}{1+\sqrt{\alpha}}}.$$
>
> **Définition de l'impédance et expression en fonction de $Z_1,Z_2$**
>
> On définit l'impédance mécanique caractéristique de chaque corde par $Z_i=\mu_i c_i=\sqrt{F\mu_i}$ (cf. point cours). Comme la tension $F$ est commune aux deux cordes, on a montré dans le point cours que $k_i=(\omega/F)\,Z_i$, c'est-à-dire que $k$ et $Z$ sont **directement proportionnels**, avec le *même* coefficient de proportionnalité $\omega/F$ pour les deux cordes. Le rapport $k_1/k_2$ est donc rigoureusement égal au rapport $Z_1/Z_2$ :
> $$\frac{k_1}{k_2} = \frac{Z_1}{Z_2}.$$
> En reportant cette proportionnalité dans les expressions de $r$ et $t$ obtenues ci-dessus (le facteur commun $\omega/F$ se simplifie directement dans le rapport $(k_1-k_2)/(k_1+k_2)$) :
> $$\boxed{r = \frac{Z_1-Z_2}{Z_1+Z_2}}, \qquad \boxed{t = \frac{2Z_1}{Z_1+Z_2}}.$$
> On retrouve ainsi, pour une onde mécanique sur corde, exactement la même structure de coefficients que pour l'onde acoustique du TD2 (à un renversement de l'ordre $Z_1\leftrightarrow Z_2$ près dans le numérateur de $r$, qui provient du choix de grandeur physique raccordée — déplacement ici, pression dans le cas acoustique — et non d'une erreur).


**q9.** Commenter dans le cas où $\alpha=1$.

> [!tip]- 💡 Coup de pouce
> Si $\alpha=1$, les deux cordes sont identiques : il n'y a plus vraiment de jonction.


> [!success]- ✅ Correction
> $\alpha=1 \Rightarrow r=0,\ t=1$ : pas de réflexion, l'onde incidente est intégralement transmise -- cohérent, la corde est alors homogène (pas d'interface).


> [!example]- 📝 Solution détaillée
> **Vérification directe et interprétation**
>
> Pour $\alpha=1$, on a $\mu_2=\mu_1$, donc $c_1=c_2$, $k_1=k_2$ et $Z_1=Z_2$. Les formules donnent immédiatement :
> $$r = \frac{1-\sqrt{1}}{1+\sqrt{1}} = 0, \qquad t = \frac{2}{1+\sqrt{1}} = 1.$$
> Ce résultat est physiquement attendu : si $\alpha=1$, les deux cordes sont en réalité identiques, et il n'existe alors plus de véritable discontinuité mécanique au point $O$ — on retrouve simplement une corde homogène le long de laquelle l'onde se propage sans aucune réflexion ($r=0$) et se transmet intégralement ($t=1$). Ce cas limite constitue une bonne vérification de cohérence des formules générales obtenues en question 8 : l'absence d'interface physique doit nécessairement se traduire par l'absence de réflexion.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex3-perle-sur-une-corde-jonction-massive-filtre-passe-bas-puis-passe-bande|Exercice 3 — Perle sur une corde : jonction massive, filtre passe-bas puis passe-bande]]

