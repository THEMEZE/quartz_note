---
title: "Exercice 7 — Complément (niveau 2, ambitieux) : oscillateurs désaccordés, anticroisement et transfert d'énergie"
tags:
  - td
  - chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/index|⬅ Retour]] · <a href="/pdfs/td4_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 7. Complément (niveau 2, ambitieux) : oscillateurs désaccordés, anticroisement et transfert d'énergie *(facultatif)*

*Difficulté ●●●●○ · ⏱ 75 min · Type : Complément original, problème guidé de type concours/ENS*

**Exercice complémentaire original (niveau 2).** Deux pendules simples de même masse $m$, de longueurs $\ell_a$ et $\ell_b$ légèrement différentes, sont suspendus côte à côte et couplés par un ressort horizontal de raideur $k_c$, accroché aux masses (ressort relâché quand les deux fils sont verticaux). On note $x_a$, $x_b$ les abscisses des masses (petits angles), $\omega_a^2=g/\ell_a$, $\omega_b^2=g/\ell_b$, $\Omega^2=k_c/m$ et $\omega_0^2=\dfrac{\omega_a^2+\omega_b^2}2$, $\Delta=\omega_b^2-\omega_a^2$ (désaccord). On suppose $\Omega^2\ll\omega_0^2$. Dans les applications numériques : $\omega_0^2=100\ \mathrm{s^{-2}}$, $\Omega^2=0{,}5\ \mathrm{s^{-2}}$.

Le but est de comprendre ce qui se passe quand on *désaccorde* deux oscillateurs couplés : comment les modes évoluent, pourquoi les fréquences ne se croisent jamais, et quelle fraction de l'énergie peut passer d'un oscillateur à l'autre.


> [!question]- 🪝 Accroche
> **Deux diapasons presque identiques**
>
> *Durée de l'introduction : 3 min*
>
> *Deux diapasons presque identiques sont posés sur la même caisse. On en frappe un seul. L'autre se met-il à vibrer ? Complètement ? Que se passe-t-il s'ils sont de plus en plus différents ?*
>
> **Idée clé : le transfert d'énergie est total seulement si les deux oscillateurs sont accordés.** Plus le désaccord $\Delta$ est grand devant le couplage $\Omega^2$, moins l'énergie passe : la fraction transférée vaut $\sin^22\theta$ avec $\tan2\theta=2\Omega^2/\Delta$.




> [!abstract]- 🧠 À savoir avant
> **Exercices 2 et 3 du TD4**
>
> Oscillateurs dissymétriques, matrice $K$, équation caractéristique bicarrée, rapport d'amplitudes.
>
> **Trigonométrie**
>
> $\tan2\theta=\dfrac{2\tan\theta}{1-\tan^2\theta}$, $\sin^22\theta=\dfrac{\tan^22\theta}{1+\tan^22\theta}$.




> [!info]- 🎯 Ce que tu sauras faire
> **Comprendre l'anticroisement des niveaux**
>
> Montrer que $\omega''^2-\omega'^2=2\sqrt{(\Delta/2)^2+\Omega^4}\ge2\Omega^2$ : le couplage empêche les fréquences de se croiser.
>
> **Introduire l'angle de mélange**
>
> Décrire les modes par $(\cos\theta,\sin\theta)$ et $(-\sin\theta,\cos\theta)$ avec $\tan2\theta=2\Omega^2/\Delta$.
>
> **Prévoir le transfert d'énergie**
>
> Montrer que la fraction maximale d'énergie transférée est $\sin^22\theta=\dfrac{4\Omega^4}{\Delta^2+4\Omega^4}$ et que la période de battement est $T_b=\dfrac{2\pi}{\omega''-\omega'}$.




> [!note]- 🧮 Outils mathématiques
> **Valeurs propres d'une matrice symétrique $2\times2$**
>
> $\begin{pmatrix}p&q\\q&r\end{pmatrix}$ : $\lambda=\dfrac{p+r}2\pm\sqrt{\Big(\dfrac{p-r}2\Big)^2+q^2}$ ; angle $\tan2\theta=\dfrac{2q}{p-r}$.
>
> **Développement de la racine**
>
> $\sqrt{\Delta^2/4+\Omega^4}\simeq\dfrac{|\Delta|}2+\dfrac{\Omega^4}{|\Delta|}$ pour $|\Delta|\gg2\Omega^2$ (décalage perturbatif) ; $\simeq\Omega^2$ pour $\Delta\to0$.
>
> **Différence de racines**
>
> $\omega''-\omega'=\dfrac{\omega''^2-\omega'^2}{\omega''+\omega'}\simeq\dfrac{\omega''^2-\omega'^2}{2\omega_0}$.



**q1.** **Question 1.** Écrire les équations du mouvement de $x_a$ et $x_b$ (petits angles) et la matrice $\mathcal K$ telle que $\ddot X+\mathcal KX=0$. Exprimer $\mathcal K$ avec $\omega_0^2$, $\Delta$ et $\Omega^2$.


> [!tip]- 💡 Coup de pouce
> **Reprendre l'exercice 2**
>
> Chaque pendule a sa propre pulsation $\omega_a$ ou $\omega_b$ ; le ressort ajoute $\Omega^2$ sur la diagonale et $-\Omega^2$ hors diagonale.




> [!success]- ✅ Correction
> **Matrice**
>
> $\ddot x_a+(\omega_a^2+\Omega^2)x_a-\Omega^2x_b=0$, $\ddot x_b+(\omega_b^2+\Omega^2)x_b-\Omega^2x_a=0$ ; $\mathcal K=\begin{pmatrix}\omega_0^2-\Delta/2+\Omega^2&-\Omega^2\\-\Omega^2&\omega_0^2+\Delta/2+\Omega^2\end{pmatrix}$.




> [!example]- 📝 Solution détaillée
> **Équations**
>
> Pour chaque pendule, la projection sur la tangente donne le rappel de gravité $-\omega_{a,b}^2x_{a,b}$ ; le ressort (allongement $x_b-x_a$) ajoute $+\Omega^2(x_b-x_a)$ sur $a$ et $-\Omega^2(x_b-x_a)$ sur $b$ (même méthode que les exercices 1 et 3) : $\ddot x_a=-\omega_a^2x_a+\Omega^2(x_b-x_a)$, $\ddot x_b=-\omega_b^2x_b-\Omega^2(x_b-x_a)$.
>
> **Matrice et paramètres**
>
> $\omega_a^2=\omega_0^2-\Delta/2$ et $\omega_b^2=\omega_0^2+\Delta/2$ (définition de $\omega_0^2$ et $\Delta$), d'où $\mathcal K$ ci-dessus. Elle est symétrique : réciprocité. Les deux diagonales sont égales si et seulement si $\Delta=0$ ; alors seulement le découplage par somme et différence fonctionne (exercice 1).
>
> **Contrôles**
>
> $\Omega=0$ : $\mathcal K$ diagonale, pulsations $\omega_a,\omega_b$. $\Delta=0$ : exercice 1.



**q2.** **Question 2.** Calculer les pulsations propres $\omega'$ et $\omega''$. Montrer que $\omega''^2-\omega'^2=2\sqrt{\Delta^2/4+\Omega^4}\ge2\Omega^2$ : les niveaux ne se croisent jamais. Tracer l'allure de $\omega'^2$, $\omega''^2$ en fonction de $\Delta$ et préciser les asymptotes.


> [!tip]- 💡 Coup de pouce
> **Formule des valeurs propres**
>
> Appliquez $\lambda=\dfrac{p+r}2\pm\sqrt{\big(\tfrac{p-r}2\big)^2+q^2}$ à $\mathcal K$ : $p-r=-\Delta$, $q=-\Omega^2$.
>
> **Asymptotes**
>
> Pour $|\Delta|\to\infty$, développez la racine : $\sqrt{\Delta^2/4+\Omega^4}\simeq|\Delta|/2$.




> [!success]- ✅ Correction
> **Résultat**
>
> $\omega'^2,\omega''^2=\omega_0^2+\Omega^2\mp\sqrt{\dfrac{\Delta^2}4+\Omega^4}$. Asymptotes : $\omega_a^2+\Omega^2$ et $\omega_b^2+\Omega^2$ (droites de pente $\mp\tfrac12$ en $\Delta$). Écart minimal $2\Omega^2$ à $\Delta=0$ : hyperbole d'anticroisement.




> [!example]- 📝 Solution détaillée
> **Valeurs propres**
>
> $\mathrm{tr}\,\mathcal K=2(\omega_0^2+\Omega^2)$ et $\det\mathcal K=(\omega_0^2+\Omega^2)^2-\dfrac{\Delta^2}4-\Omega^4$ donnent $\omega^2=\omega_0^2+\Omega^2\pm\sqrt{\dfrac{\Delta^2}4+\Omega^4}$. Le discriminant est strictement positif dès que $\Omega\ne0$ : jamais de dégénérescence.
>
> **Anticroisement**
>
> $\omega''^2-\omega'^2=2\sqrt{\Delta^2/4+\Omega^4}$ est minimal en $\Delta=0$ et vaut $2\Omega^2$. Sans couplage ($\Omega=0$) les deux pulsations propres $\omega_a^2=\omega_0^2-\Delta/2$ et $\omega_b^2=\omega_0^2+\Delta/2$ sont deux droites qui se croisent en $\Delta=0$ ; avec couplage elles forment les deux branches d'une hyperbole. Le croisement est *évité*.
>
> **Application numérique**
>
> $\omega_0^2=100$, $\Omega^2=0{,}5$, $\Delta=0$ : $\omega'^2=100{,}5$ ($\omega'=10{,}025$) et $\omega''^2=101{,}5$ ($\omega''=10{,}075$) ; $\omega''-\omega'=0{,}0499\ \mathrm{rad\cdot s^{-1}}$.
>
> **Perturbation à grand désaccord**
>
> Pour $|\Delta|\gg2\Omega^2$ : $\omega'^2\simeq\omega_a^2+\Omega^2-\dfrac{\Omega^4}{\Delta}$, $\omega''^2\simeq\omega_b^2+\Omega^2+\dfrac{\Omega^4}\Delta$ (pour $\Delta>0$) : chaque niveau est décalé de $\Omega^2$ (le ressort s'ajoute à la raideur) et repoussé de $\Omega^4/\Delta$ par l'autre : c'est la perturbation du second ordre, qui disparaît lentement avec le désaccord.



**q3.** **Question 3.** Déterminer les modes propres sous la forme $\vec u'=(\cos\theta,\sin\theta)$ et $\vec u''=(-\sin\theta,\cos\theta)$. Montrer que $\tan2\theta=\dfrac{2\Omega^2}{\Delta}$ et discuter les cas $\Delta=0$, $\Delta\gg\Omega^2$, $\Delta\ll-\Omega^2$.


> [!tip]- 💡 Coup de pouce
> **Rotation**
>
> Écrivez $P^{\mathsf T}\mathcal KP$ avec $P=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$ et imposez que le terme hors diagonale soit nul.




> [!success]- ✅ Correction
> **Angle de mélange**
>
> $\tan\theta=\dfrac{\sqrt{\Delta^2/4+\Omega^4}-\Delta/2}{\Omega^2}$, d'où $\tan2\theta=\dfrac{2\Omega^2}{\Delta}$ ; $\theta=\pi/4$ à l'accord.




> [!example]- 📝 Solution détaillée
> **Calcul du terme hors diagonale**
>
> Avec $p=\omega_0^2-\Delta/2+\Omega^2$, $r=\omega_0^2+\Delta/2+\Omega^2$, $q=-\Omega^2$, la première ligne de $\mathcal K\vec u'=\omega'^2\vec u'$ donne $(p-\omega'^2)\cos\theta-\Omega^2\sin\theta=0$, soit $t=\tan\theta=\dfrac{p-\omega'^2}{\Omega^2}=\dfrac{s-\Delta/2}{\Omega^2}$ avec $s=\sqrt{\Delta^2/4+\Omega^4}$. Ce nombre est strictement positif : $\theta\in\,]0,\pi/2[$. C'est la racine positive de $\Omega^2t^2+\Delta t-\Omega^2=0$, d'où $1-t^2=\Delta t/\Omega^2$ et
> $$\tan2\theta=\frac{2t}{1-t^2}=\frac{2\Omega^2}{\Delta}.$$
>
> **Cas limites**
>
> - $\Delta=0$ : $\tan2\theta=\infty$, $\theta=\pi/4$ : modes $(1,1)/\sqrt2$ (en phase, $\omega'$) et $(-1,1)/\sqrt2$ (en opposition, $\omega''$) : mélange à $50/50$, exercice 1.
> - $\Delta\gg\Omega^2$ ($\omega_b\gg\omega_a$) : $\theta\simeq\Omega^2/\Delta\to0$ : $\vec u'\to(1,0)$ : le mode bas est le pendule $a$ seul, le mode haut le pendule $b$ seul.
> - $\Delta\ll-\Omega^2$ : $\theta\to\pi/2$ : $\vec u'\to(0,1)$ : le mode bas est maintenant le pendule $b$ (le plus lent), le mode haut le pendule $a$. Les modes ont « échangé leur caractère » en traversant la zone d'anticroisement.
>
> **Signification physique**
>
> L'angle $\theta$ mesure le mélange : $\cos^2\theta$ est la part de l'oscillateur $a$ dans le mode bas. À l'accord le mélange est maximal ; loin de l'accord il disparaît. L'orthogonalité de $\vec u'$ et $\vec u''$ est celle des modes d'une matrice symétrique : les amplitudes des deux modes se « partagent » sans fuite.



**q4.** **Question 4.** À $t=0$, on lâche le pendule $a$ avec l'amplitude $A$ sans vitesse, le pendule $b$ étant à l'équilibre. Calculer $x_a(t)$ et $x_b(t)$, puis la fraction maximale de l'énergie du pendule $a$ transférée au pendule $b$. Calculer la période de battement. Applications numériques pour $\Delta=0$ et $\Delta=2\ \mathrm{s^{-2}}$.


> [!tip]- 💡 Coup de pouce
> **Projection sur les modes**
>
> $X(0)=(A,0)=A\cos\theta\,\vec u'-A\sin\theta\,\vec u''$ : écrivez les deux coefficients modaux.
>
> **Amplitude de $x_b$**
>
> $x_b=A\sin\theta\cos\theta\,(\cos\omega't-\cos\omega''t)$ : quelle est la valeur maximale de $|\cos\omega't-\cos\omega''t|$ ?




> [!success]- ✅ Correction
> **Résultat**
>
> $x_a=A(\cos^2\theta\cos\omega't+\sin^2\theta\cos\omega''t)$, $x_b=\dfrac A2\sin2\theta(\cos\omega't-\cos\omega''t)$ ; amplitude maximale de $x_b$ : $A\sin2\theta$ ; fraction d'énergie transférée $\sin^22\theta=\dfrac{4\Omega^4}{\Delta^2+4\Omega^4}$ ; $T_b=\dfrac{2\pi}{\omega''-\omega'}$.




> [!example]- 📝 Solution détaillée
> **Décomposition**
>
> $x_a(0)=A$, $x_b(0)=0$ : $c'=\vec u'\cdot X(0)=A\cos\theta$, $c''=\vec u''\cdot X(0)=-A\sin\theta$. Vitesses nulles : $X(t)=A\cos\theta\,\vec u'\cos\omega't-A\sin\theta\,\vec u''\cos\omega''t$, d'où
> $$x_a=A\big(\cos^2\theta\cos\omega't+\sin^2\theta\cos\omega''t\big),\qquad x_b=A\sin\theta\cos\theta\,\big(\cos\omega't-\cos\omega''t\big).$$
>
> **Fraction transférée**
>
> $|x_b|_{\max}=A\sin\theta\cos\theta\cdot2=A\sin2\theta$ (quand les deux cosinus valent $\pm1$ en opposition). L'énergie de $b$ vaut $\tfrac12m\omega_b^2A_b^2$ ; avec $\omega_b\simeq\omega_a$ le rapport à l'énergie initiale $\tfrac12m\omega_a^2A^2$ est $\sin^22\theta$ à des corrections relatives $O(\Delta/\omega_0^2)$ près :
> $$\sin^22\theta=\frac{\tan^22\theta}{1+\tan^22\theta}=\frac{4\Omega^4}{\Delta^2+4\Omega^4}.$$
> À l'accord ($\theta=\pi/4$), $100\,\%$ : transfert complet. Pour $\Delta=2\ \mathrm{s^{-2}}$ : $\dfrac{4\times0{,}25}{4+1}=20\,\%$. Vérifié numériquement (intégration des équations).
>
> **Période de battement**
>
> Le motif se reproduit avec la période $T_b=\dfrac{2\pi}{\omega''-\omega'}$ (période du terme $\cos\omega't-\cos\omega''t$ pour l'enveloppe). Application numérique : à $\Delta=0$, $\omega''-\omega'=0{,}0499$ donc $T_b=126$ s ; pour $\Delta=2$ : $\omega''^2-\omega'^2=2\sqrt{1+0{,}25}=2{,}236$, $\omega''-\omega'=2{,}236/(2\times10{,}0)\simeq0{,}112$, $T_b\simeq56$ s. Formule approchée : $T_b\simeq\dfrac{2\pi}{\sqrt{\delta^2+\Omega^4/\omega_0^2}}$ avec $\delta=\Delta/(2\omega_0)$.
>
> **Lien avec l'exercice 1**
>
> À l'accord, $x_a=A\cos\Omega_mt\cos\Omega_0t$ et $x_b=A\sin\Omega_mt\sin\Omega_0t$ : le battement complet. Hors accord, l'amplitude de $x_b$ ne dépasse jamais $A\sin2\theta<A$ : le battement est « incomplet ».



**q5.** **Question 5.** *Discussion.* À partir de quel désaccord le transfert d'énergie tombe-t-il à $50\,\%$ ? Interpréter en comparant $\Delta$ et $2\Omega^2$. Que se passe-t-il si l'on fait varier lentement la longueur $\ell_b$ de part et d'autre de $\ell_a$ ?


> [!tip]- 💡 Coup de pouce
> **Condition**
>
> $\sin^22\theta=\tfrac12$ équivaut à $\tan2\theta=\pm1$, soit $|\Delta|=2\Omega^2$.




> [!success]- ✅ Correction
> **Résultat**
>
> $|\Delta|=2\Omega^2=1\ \mathrm{s^{-2}}$. Le transfert est important ($>50\,\%$) tant que le désaccord reste inférieur à l'écart minimal $2\Omega^2$ entre les modes : « couplage fort » si $|\Delta|\lesssim2\Omega^2$, « couplage faible » si $|\Delta|\gg2\Omega^2$.




> [!example]- 📝 Solution détaillée
> **Seuil à 50 %**
>
> $\sin^22\theta=\dfrac{4\Omega^4}{\Delta^2+4\Omega^4}=\dfrac12$ donne $\Delta^2=4\Omega^4$, soit $|\Delta|=2\Omega^2=1\ \mathrm{s^{-2}}$ (ici : $\ell_b/\ell_a-1\simeq\Delta/\omega_0^2=1\,\%$, très sensible !).
>
> **Interprétation**
>
> Deux échelles : le désaccord $\Delta$ (différence des raideurs effectives) et le couplage $2\Omega^2$ (l'écart minimal entre les modes). Le transfert est complet si $\Delta\ll2\Omega^2$ et négligeable si $\Delta\gg2\Omega^2$ (fraction $\simeq4\Omega^4/\Delta^2$). Avec un couplage de $0{,}5\ \mathrm{s^{-2}}$ sur $100\ \mathrm{s^{-2}}$, une différence de $1\,\%$ des longueurs suffit à réduire le transfert à $50\,\%$ : il faut donc des pendules très bien accordés pour voir de beaux battements.
>
> **Variation lente du désaccord**
>
> Si $\ell_b$ varie lentement (devant $T_b$) de $\Delta<0$ à $\Delta>0$ en traversant l'accord, l'énergie initialement dans le pendule $a$ *suit le mode* : elle reste dans le mode haut puis bas, donc passe finalement dans le pendule $b$ (transfert adiabatique) ; si la variation est rapide, l'énergie reste dans $a$ (mouvement diabatique). Le critère intermédiaire est celui de Landau--Zener.
>
> **Analogie quantique**
>
> En posant $x_{a,b}=\mathrm{Re}[c_{a,b}(t)e^{i\omega_0t}]$ avec des amplitudes lentes, les équations deviennent $i\dot c=\begin{pmatrix}-\delta+\kappa&-\kappa\\-\kappa&\delta+\kappa\end{pmatrix}c$ avec $\delta=\Delta/(4\omega_0)$ et $\kappa=\Omega^2/(2\omega_0)$ : un système à deux niveaux. Le désaccord est celui du laser par rapport à la résonance, la fréquence de Rabi généralisée est $\sqrt{4\delta^2+4\kappa^2}\simeq\omega''-\omega'$. La fraction transférée $\sin^22\theta$ est la formule de Rabi.




> [!note]- 🔗 Liens avec d'autres disciplines
> **Physique quantique**
>
> Système à deux niveaux : les niveaux d'énergie ne se croisent pas (anticroisement) ; l'oscillation de Rabi est l'analogue du battement.
>
> **Optique**
>
> Deux guides d'onde couplés : le transfert de puissance d'un guide à l'autre est complet seulement si leurs indices sont égaux (coupleur directionnel).




> [!question]- 🔭 Aller plus loin — Licence : Modes comme rotation d'un angle $\theta$
> Montrer que $P(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}$ diagonalise $K$ et que $\theta$ varie de $\pi/4$ (accord) à $0$ (grand désaccord).




> [!question]- 🔭 Aller plus loin — Master : Analogie quantique
> Montrer que les équations des amplitudes lentes sont celles d'un système à deux niveaux ($i\dot c=Hc$ avec $H=\begin{pmatrix}-\delta&\kappa\\\kappa&\delta\end{pmatrix}$) et identifier $\sqrt{\delta^2+\kappa^2}$ à la fréquence de Rabi généralisée.




> [!question]- 🔭 Aller plus loin — Master : Passage adiabatique
> Si $\Delta$ varie lentement de $-\infty$ à $+\infty$, montrer que l'énergie reste sur le mode : le pendule excité au début est excité à la fin sur l'autre oscillateur (« échange de caractère » ; formule de Landau--Zener pour une variation rapide).




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex2-couplage-de-deux-oscillateurs-harmoniques-dissymetriques|Exercice 2 — Couplage de deux oscillateurs harmoniques dissymétriques]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex3-oscillations-libres-et-forcees-d-un-couplage-pendule-chariot|Exercice 3 — Oscillations libres et forcées d'un couplage pendule-chariot]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex4-frequence-propre-d-une-molecule-diatomique|Exercice 4 — Fréquence propre d'une molécule diatomique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex5-complement-niveau-1-cpge-pendules-couples-par-un-ressort-attache-a-mi-hauteur|Exercice 5 — Complément (niveau 1, CPGE) : pendules couplés par un ressort attaché à mi-hauteur]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex6-complement-niveau-2-ambitieux-trois-masses-quatre-ressorts-diagonalisation-et-perturbation|Exercice 6 — Complément (niveau 2, ambitieux) : trois masses, quatre ressorts, diagonalisation et perturbation]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex8-complement-niveau-3-ens-modes-non-lineaires-de-deux-pendules-couples-stabilite-et-instabilite-parametrique|Exercice 8 — Complément (niveau 3, ENS) : modes non linéaires de deux pendules couplés, stabilité et instabilité paramétrique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex9-complement-niveau-3-ens-anneau-de-n-oscillateurs-modes-de-fourier-et-propagation-du-signal|Exercice 9 — Complément (niveau 3, ENS) : anneau de N oscillateurs, modes de Fourier et propagation du signal]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex1-pendules-couples-et-battements|Exercice 1 — Pendules couplés et battements]]


