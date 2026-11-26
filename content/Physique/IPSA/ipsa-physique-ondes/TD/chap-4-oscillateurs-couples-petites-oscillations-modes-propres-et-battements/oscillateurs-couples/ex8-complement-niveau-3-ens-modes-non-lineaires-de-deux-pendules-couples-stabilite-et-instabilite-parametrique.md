---
title: "Exercice 8 — Complément (niveau 3, ENS) : modes non linéaires de deux pendules couplés, stabilité et instabilité paramétrique"
tags:
  - td
  - chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/index|⬅ Retour]] · <a href="/pdfs/td4_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td4_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td4_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a>

### Exercice 8. Complément (niveau 3, ENS) : modes non linéaires de deux pendules couplés, stabilité et instabilité paramétrique *(facultatif)*

*Difficulté ●●●●● · ⏱ 120 min · Type : Complément original, problème de type ENS*

**Exercice complémentaire original (niveau 3, type ENS).** Deux pendules simples identiques (longueur $\ell=1{,}00$ m, masse $m$, $\omega_0^2=g/\ell$, $g=9{,}81\ \mathrm{m\cdot s^{-2}}$) sont suspendus à la même hauteur, à la distance $d$ l'un de l'autre, et couplés par un ressort de raideur $k$, de longueur à vide $d$, accroché aux deux masses. On note $\kappa=k/m$ et $\alpha_1,\alpha_2$ les angles des fils avec la verticale (positifs vers la droite). *On ne fait aucune approximation des petits angles dans les questions 1 à 3.*

Les équations exactes établies à l'exercice 1 sont, avec $u=d+\ell(\sin\alpha_2-\sin\alpha_1)$, $v=\ell(\cos\alpha_1-\cos\alpha_2)$ et $\ell_s=\sqrt{u^2+v^2}$ (longueur du ressort) :
$$\ddot\alpha_1=-\omega_0^2\sin\alpha_1+\frac\kappa\ell\,\frac{\ell_s-d}{\ell_s}(u\cos\alpha_1+v\sin\alpha_1),\qquad\ddot\alpha_2=-\omega_0^2\sin\alpha_2-\frac\kappa\ell\,\frac{\ell_s-d}{\ell_s}(u\cos\alpha_2+v\sin\alpha_2).$$
Dans la théorie linéaire, il y a deux modes : en phase ($\omega_s=\omega_0$) et en opposition de phase ($\omega_a=\sqrt{\omega_0^2+2\kappa}$). La question est : *que deviennent ces modes à amplitude finie, et restent-ils stables ?*


> [!question]- 🪝 Accroche
> **Un mode propre est-il toujours stable ?**
>
> *Durée de l'introduction : 5 min*
>
> *Les deux pendules couplés oscillent en phase avec une grande amplitude. Le mouvement est-il stable si on introduit une toute petite différence entre les deux angles ?*
>
> **Idée clé : en régime linéaire les modes sont indépendants ; en régime non linéaire ils sont couplés.** À grande amplitude, le mode en phase peut transférer son énergie vers le mode en opposition : c'est l'instabilité paramétrique, due à la dépendance de la fréquence en l'amplitude.




> [!abstract]- 🧠 À savoir avant
> **Exercice 1 du TD4**
>
> Équations exactes des pendules couplés, modes en phase et en opposition, linéarisation.
>
> **Méthode de Poincaré--Lindstedt**
>
> Pour $\ddot x+\omega^2x+\varepsilon x^3=0$, la pulsation à l'amplitude $A$ est $\omega_A=\omega+\dfrac{3\varepsilon A^2}{8\omega}$.
>
> **Équation de Hill et de Mathieu**
>
> $\ddot q+[\omega^2+h\cos(2\omega_pt)]q=0$ : instabilité si $|\omega^2-\omega_p^2|<|h|/2$ (première zone, $\omega_p$ pulsation de modulation $/2$).




> [!info]- 🎯 Ce que tu sauras faire
> **Reconnaître une variété invariante**
>
> Montrer que les conditions $\alpha_1=\alpha_2$ et $\alpha_1=-\alpha_2$ sont préservées exactement par la dynamique non linéaire, et ramener le problème à une équation à une dimension.
>
> **Calculer la dépendance de la fréquence en amplitude**
>
> Utiliser un développement en série ou Poincaré--Lindstedt pour obtenir la correction cubique de la pulsation.
>
> **Étudier la stabilité d'un mouvement périodique**
>
> Linéariser autour d'une solution périodique, obtenir une équation de Hill, la réduire à une équation de Mathieu et trouver le seuil d'instabilité paramétrique.




> [!note]- 🧮 Outils mathématiques
> **Intégrale elliptique**
>
> $T(A)=\dfrac{4}{\omega_0}K\big(\sin\tfrac A2\big)$ avec $K(\varkappa)=\displaystyle\int_0^{\pi/2}\dfrac{\mathrm d\phi}{\sqrt{1-\varkappa^2\sin^2\phi}}=\dfrac\pi2\Big(1+\dfrac{\varkappa^2}4+\dfrac{9\varkappa^4}{64}+\dots\Big)$.
>
> **Théorème de Floquet**
>
> Pour $\ddot q+p(t)q=0$ avec $p$ de période $T$, les solutions vérifient $q(t+T)=\mu\,q(t)$ ; les multiplicateurs $\mu$ sont les valeurs propres de la matrice de monodromie, de produit $1$ ; stabilité $\Leftrightarrow|\mu|=1$.
>
> **Développement en $A$**
>
> $\sin\beta=\beta-\beta^3/6$, $\sin2\beta=2\beta-4\beta^3/3$, $\cos\alpha=1-\alpha^2/2$, $\cos^2\alpha=1-\alpha^2$.



**q1.** **Question 1.** *Mode en phase.* Montrer que la condition $\alpha_1=\alpha_2=\alpha$ est compatible avec les équations exactes pour toute amplitude (variété invariante) et que $\alpha$ vérifie l'équation du pendule simple. Donner la période en fonction de l'amplitude $A$ jusqu'à l'ordre $A^2$.


> [!tip]- 💡 Coup de pouce
> **Longueur du ressort**
>
> Que valent $u$ et $v$ si $\alpha_1=\alpha_2$ ? Que vaut alors $\ell_s-d$ ?
>
> **Période du pendule**
>
> $T=T_0\dfrac2\pi K(\sin\tfrac A2)$ avec $K(\varkappa)\simeq\dfrac\pi2(1+\varkappa^2/4)$ ; $\sin^2\frac A2\simeq\frac{A^2}4$.




> [!success]- ✅ Correction
> **Résultat**
>
> $u=d$, $v=0$, $\ell_s=d$ : le ressort n'est jamais déformé ; $\ddot\alpha+\omega_0^2\sin\alpha=0$ ; $T=T_0\big(1+\dfrac{A^2}{16}+\dfrac{11A^4}{3072}+\dots\big)$.




> [!example]- 📝 Solution détaillée
> **Invariance**
>
> Si $\alpha_1=\alpha_2$ à un instant et $\dot\alpha_1=\dot\alpha_2$, alors $u=d$, $v=0$, $\ell_s=d$ : le facteur $\ell_s-d$ s'annule, donc les termes de ressort sont nuls dans les deux équations, qui deviennent la même : $\ddot\alpha=-\omega_0^2\sin\alpha$. Les deux angles restent égaux à tout instant (unicité des solutions). C'est exact, à toute amplitude, grâce à la symétrie $1\leftrightarrow2$ : le ressort ne sert à rien dans ce mouvement.
>
> **Période**
>
> Le pendule simple a pour période $T=\dfrac4{\omega_0}K\big(\sin\tfrac A2\big)$ ; avec $\sin^2\tfrac A2=\tfrac{A^2}4-\tfrac{A^4}{48}+\dots$ on trouve $T=T_0\Big(1+\dfrac{A^2}{16}+\dfrac{11A^4}{3072}+\dots\Big)$, $T_0=2\pi/\omega_0=2{,}006$ s. Ici : $A=0{,}6$ rad $\Rightarrow T=2{,}052$ s ($+2{,}3\,\%$) ; $A=1{,}0$ $\Rightarrow T=2{,}139$ s ($+6{,}7\,\%$). La pulsation *diminue* avec l'amplitude : le pendule est « mou » ($\sin\alpha<\alpha$).
>
> **Ce que le DL a justifié**
>
> Le développement $T=T_0(1+A^2/16)$ est le premier ordre au-delà du petit angle : le terme en $A^2$ est le premier qui n'est pas pris en compte par la linéarisation, et son coefficient mesure l'erreur : $<1\,\%$ si $A<0{,}4$ rad ($23^\circ$).



**q2.** **Question 2.** *Mode en opposition.* Montrer que $\alpha_1=-\alpha_2=\beta$ est invariant et que $\beta$ vérifie $\ddot\beta=-\omega_0^2\sin\beta-\kappa\sin2\beta$. Par la méthode de Poincaré--Lindstedt ou le développement de l'équation, montrer que la pulsation à l'amplitude $A$ est $\omega(A)\simeq\omega_a-\dfrac{(\omega_0^2+8\kappa)A^2}{16\,\omega_a}$.


> [!tip]- 💡 Coup de pouce
> **Longueur du ressort**
>
> Si $\alpha_2=-\alpha_1=-\beta$, calculez $v$ et $u=d-2\ell\sin\beta$. Le ressort reste-t-il horizontal ? Que valent $\ell_s-d$ et $\cos\alpha_1$ ?
>
> **Développement**
>
> $\sin\beta\simeq\beta-\beta^3/6$ et $\sin2\beta\simeq2\beta-4\beta^3/3$ : réécrivez l'équation sous la forme $\ddot\beta+\omega_a^2\beta-\gamma\beta^3=0$ et identifiez $\gamma$.




> [!success]- ✅ Correction
> **Résultat**
>
> $v=0$, $u=d-2\ell\sin\beta$, $\ell_s-d=-2\ell\sin\beta$ (si $u>0$) : $\ddot\beta=-\omega_0^2\sin\beta-\kappa\sin2\beta$ ; $\gamma=\dfrac{\omega_0^2+8\kappa}6$ et $\omega(A)\simeq\omega_a-\dfrac{3\gamma A^2}{8\omega_a}$.




> [!example]- 📝 Solution détaillée
> **Invariance et équation**
>
> Avec $\alpha_1=\beta$, $\alpha_2=-\beta$ : $v=\ell(\cos\beta-\cos\beta)=0$ et $u=d-2\ell\sin\beta$ : le ressort reste horizontal (exactement), avec l'allongement $\ell_s-d=u-d=-2\ell\sin\beta$ (si $u>0$, c'est-à-dire si les masses ne se touchent pas). La première équation donne $\ddot\beta=-\omega_0^2\sin\beta+\dfrac\kappa\ell(-2\ell\sin\beta)\cos\beta=-\omega_0^2\sin\beta-2\kappa\sin\beta\cos\beta=-\omega_0^2\sin\beta-\kappa\sin2\beta$ ; la seconde donne la même équation pour $-\beta$ (cohérent). L'équation est *exacte*, à une dimension.
>
> **Limite linéaire**
>
> $\ddot\beta+(\omega_0^2+2\kappa)\beta=0$ : $\omega_a^2=\omega_0^2+2\kappa$ : on retrouve la théorie linéaire.
>
> **Terme cubique**
>
> $\ddot\beta+\omega_0^2\Big(\beta-\dfrac{\beta^3}6\Big)+\kappa\Big(2\beta-\dfrac{4\beta^3}3\Big)=\ddot\beta+\omega_a^2\beta-\gamma\beta^3=0$ avec $\gamma=\dfrac{\omega_0^2}6+\dfrac{4\kappa}3=\dfrac{\omega_0^2+8\kappa}6$. C'est l'équation de Duffing « molle » ($\varepsilon=-\gamma<0$). L'absence de terme quadratique tient à la symétrie $\beta\to-\beta$ (l'énergie potentielle est paire).
>
> **Poincaré--Lindstedt**
>
> On cherche $\beta=A\cos\omega t+O(A^3)$ avec $\omega=\omega_a+\omega_2A^2$ ; l'élimination de la résonance (terme séculaire) à l'ordre $A^3$ impose $\omega_2=-\dfrac{3\gamma}{8\omega_a}$ (car $\cos^3\phi=\tfrac34\cos\phi+\tfrac14\cos3\phi$ : le terme en $\cos\phi$ doit être annulé). Donc
> $$\omega(A)\simeq\omega_a-\frac{(\omega_0^2+8\kappa)A^2}{16\,\omega_a}.$$
> Pour $\kappa=2\ \mathrm{s^{-2}}$, $\omega_a=\sqrt{13{,}81}=3{,}716$ rad/s : $A=0{,}3$ donne $T=1{,}709$ s (numérique : $1{,}7086$ s) ; $A=0{,}1$ donne $T=1{,}6927$ s. Dans le cas $\kappa=0$, on retrouve $-A^2\omega_0/16$ (pendule simple).
>
> **Comparaison des deux modes**
>
> Les deux modes « durcissent » ou « s'amollissent » différemment avec $A$ : $\Delta\omega/\omega=-A^2/16$ pour le mode en phase, $-\dfrac{(\omega_0^2+8\kappa)A^2}{16(\omega_0^2+2\kappa)}$ pour le mode en opposition : si $\kappa$ est grand, ce second coefficient tend vers $-A^2/4$, quatre fois plus grand. Le rapport $\omega_a/\omega_s$ change donc avec l'amplitude : les modes se rapprochent ou s'éloignent selon l'amplitude.



**q3.** **Question 3.** *Stabilité du mode en phase.* On perturbe le mode en phase : $\alpha_{1,2}=\alpha(t)\pm q/2$ avec $q$ petit. Montrer que $q$ vérifie, à l'ordre $1$ en $q$, $\ddot q+\cos\alpha(t)\,[\omega_0^2+2\kappa\cos\alpha(t)]\,q=0$. Pour $\alpha=A\cos\omega_st$ avec $A$ petit, ramener cette équation à une équation de Mathieu et trouver le seuil $A_c$ de l'instabilité. Application numérique pour $\kappa/\omega_0^2=0{,}02$.


> [!tip]- 💡 Coup de pouce
> **Linéariser les équations exactes en $q$**
>
> Écrivez l'équation de $q=\alpha_1-\alpha_2$ en soustrayant les deux équations exactes puis développez au premier ordre en $q$ autour de $q=0$ (dérivée par rapport à $q$ en $q=0$). Le ressort contribue par $-2\kappa\cos^2\alpha\,q$.
>
> **Mathieu**
>
> Développez $\cos\alpha\simeq1-\alpha^2/2$, $\cos^2\alpha\simeq1-\alpha^2$, puis $\cos^2\omega_st=\tfrac12(1+\cos2\omega_st)$ ; sans oublier le décalage de fréquence $\omega_s=\omega_0(1-A^2/16)$.
>
> **Zone d'instabilité**
>
> $\ddot q+[\Omega_e^2+h\cos2\omega_st]q=0$ est instable si $|\Omega_e^2-\omega_s^2|<|h|/2$.




> [!success]- ✅ Correction
> **Résultat**
>
> $\Omega_e^2-\omega_s^2=2\kappa-A^2\Big(\dfrac{\omega_0^2}8+\kappa\Big)$, $|h|=A^2\Big(\dfrac{\omega_0^2}4+\kappa\Big)$ ; instabilité si $A>A_c$, $A_c^2=\dfrac{8\kappa}{\omega_0^2+6\kappa}$. Pour $\kappa=0{,}02\omega_0^2$ : $A_c=0{,}378$ rad $=21{,}7^\circ$.




> [!example]- 📝 Solution détaillée
> **Équation de la perturbation**
>
> Soustraire les deux équations exactes donne $\ddot q=-\omega_0^2(\sin\alpha_1-\sin\alpha_2)+\dfrac\kappa\ell\dfrac{\ell_s-d}{\ell_s}\big[u(\cos\alpha_1+\cos\alpha_2)+v(\sin\alpha_1+\sin\alpha_2)\big]$. À l'ordre $1$ en $q$ : $\sin\alpha_1-\sin\alpha_2\simeq q\cos\alpha$ ; $v=O(q\cdot\alpha\,q)$ est d'ordre $2$ en $q$ ; $u-d=\ell(\sin\alpha_2-\sin\alpha_1)\simeq-\ell q\cos\alpha$ ; $\ell_s\simeq u\simeq d$ et $\cos\alpha_1+\cos\alpha_2\simeq2\cos\alpha$. D'où $\ddot q=-\omega_0^2\cos\alpha\,q-2\kappa\cos^2\alpha\,q$, soit
> $$\ddot q+\cos\alpha(t)\,[\omega_0^2+2\kappa\cos\alpha(t)]\,q=0.$$
> (Confirmé par un calcul symbolique de $\partial(\ddot\alpha_1-\ddot\alpha_2)/\partial q$ sur les équations exactes.) C'est une équation de Hill : coefficient périodique (période $T_s/2$ puisque $\cos\alpha(t)$ est périodique de période $T_s$ et le coefficient est pair en $\alpha$).
>
> **Réduction à l'équation de Mathieu**
>
> Avec $\alpha=A\cos\omega_st$, $\cos\alpha\simeq1-\dfrac{A^2}2\cos^2\omega_st$ et $\cos^2\alpha\simeq1-A^2\cos^2\omega_st$ : le coefficient de $q$ est $\omega_a^2-\Big(\dfrac{\omega_0^2}2+2\kappa\Big)A^2\cos^2\omega_st=\omega_a^2-\Big(\dfrac{\omega_0^2}4+\kappa\Big)A^2-\Big(\dfrac{\omega_0^2}4+\kappa\Big)A^2\cos2\omega_st$. D'où $\Omega_e^2=\omega_a^2-\Big(\dfrac{\omega_0^2}4+\kappa\Big)A^2$ et $|h|=\Big(\dfrac{\omega_0^2}4+\kappa\Big)A^2$ (modulation à la pulsation $2\omega_s$).
> La pulsation de la modulation est elle-même décalée par l'amplitude : $\omega_s=\omega_0(1-A^2/16)$, $\omega_s^2\simeq\omega_0^2\Big(1-\dfrac{A^2}8\Big)$. Donc
> $$\Omega_e^2-\omega_s^2=2\kappa-A^2\Big(\dfrac{\omega_0^2}8+\kappa\Big).$$
>
> **Seuil**
>
> Instabilité : $|\Omega_e^2-\omega_s^2|<|h|/2$. Branche utile : $2\kappa-A^2\Big(\dfrac{\omega_0^2}8+\kappa\Big)<A^2\Big(\dfrac{\omega_0^2}8+\dfrac\kappa2\Big)$, soit $2\kappa<A^2\Big(\dfrac{\omega_0^2}4+\dfrac{3\kappa}2\Big)$, c'est-à-dire
> $$A^2>A_c^2=\frac{8\kappa}{\omega_0^2+6\kappa}.$$
> Pour $\kappa=0{,}02\,\omega_0^2$ : $A_c^2=\dfrac{0{,}16}{1{,}12}$, $A_c=0{,}378$ rad $=21{,}7^\circ$ (valeur approchée à petit $\kappa$ : $2\sqrt2\sqrt{\kappa}/\omega_0=0{,}40$). L'intégration numérique de l'équation de Hill avec la matrice de monodromie donne $A_c=0{,}381$ : accord à $1\,\%$.
>
> **Interprétation physique**
>
> Pour $A<A_c$ les multiplicateurs de Floquet sont de module $1$ : le mode en phase est stable. Au-delà, un multiplicateur $|\mu|>1$ : l'écart $q$ croît exponentiellement (numériquement $|\mu|_{\max}=1{,}11$ à $A=1{,}3A_c$) et l'énergie passe du mode en phase au mode en opposition. Mécanisme : le mode en phase module à la pulsation $2\omega_s$ la raideur effective « vue » par $q$ ; quand cette fréquence est voisine de $2\Omega_e$, on a résonance paramétrique. À petite amplitude, $\Omega_e=\omega_a=\sqrt{\omega_0^2+2\kappa}>\omega_s=\omega_0$ : le décalage $2\kappa$ empêche la résonance ; il est compensé quand $A$ augmente car les fréquences *diminuent* avec $A$.



**q4.** **Question 4.** *Discussion.* Que dit le résultat de la question 3 de la notion de « mode propre » ? Pourquoi la théorie linéaire ne peut-elle pas le prévoir ? Quelle condition sur $A$ et $\kappa$ garantit que la linéarisation est valable ?


> [!tip]- 💡 Coup de pouce
> **Ce qui est conservé et ce qui change**
>
> Les deux mouvements sont des solutions exactes ; que dire de leur stabilité ? Que se passe-t-il pour le couplage entre modes dans un système linéaire ?




> [!success]- ✅ Correction
> **Éléments de réponse**
>
> En régime linéaire les modes sont indépendants : l'énergie de chacun est constante. À amplitude finie, la symétrie préserve l'existence des deux mouvements, mais pas leur stabilité : le seuil $A_c\simeq2\sqrt{2\kappa}/\omega_0$ montre que la linéarisation est valable pour $A\ll A_c$ *et non seulement $A\ll1$*.




> [!example]- 📝 Solution détaillée
> **Modes non linéaires**
>
> Les deux variétés $\alpha_1=\pm\alpha_2$ sont les « modes non linéaires normaux » (Rosenberg) : des solutions exactes périodiques qui se réduisent aux modes propres linéaires à petite amplitude. Elles existent ici par symétrie ; la dépendance de la période en l'amplitude en est la signature non linéaire.
>
> **Pourquoi la théorie linéaire ne voit rien**
>
> Dans $M\ddot X+KX=0$ les modes sont découplés par construction : aucune énergie ne passe de l'un à l'autre. L'instabilité vient du terme cubique (le décalage de fréquence $-A^2/16$ et le terme de couplage de $q$ à $\alpha^2$) : c'est un phénomène d'ordre $A^2$ qui joue sur un temps long $\sim1/(\text{croissance})\sim\omega_0/(A^2\omega_0^2)$.
>
> **Condition de validité**
>
> Pour que le mode en phase soit stable il faut $A<A_c=\sqrt{8\kappa/(\omega_0^2+6\kappa)}$ ; avec un couplage faible ($\kappa\ll\omega_0^2$), $A_c\simeq2\sqrt2\,\omega_c/\omega_0\ll1$ : *plus le couplage est faible, plus la région de validité des petits angles est étroite.* Pour $\kappa=0{,}02\omega_0^2$, $A_c=22^\circ$ : de plus petits angles que ceux où l'erreur sur la période ($A^2/16$) devient gênante ($\sim1\,\%$ à $0{,}4$ rad). C'est une illustration que « petit » n'a de sens que relativement à une échelle physique qu'il faut identifier : ici le rapport $\omega_c/\omega_0$.




> [!note]- 🔗 Liens avec d'autres disciplines
> **Physique des plasmas et optique non linéaire**
>
> Instabilité paramétrique : un mode de grande amplitude (onde pompe) amplifie une paire de modes de fréquences moitiés ; même mathématique que le seuil de Mathieu.
>
> **Mécanique**
>
> Le pendule de Faraday et l'instabilité paramétrique d'une balançoire : on excite une oscillation en modulant à deux fois la fréquence propre.




> [!question]- 🔭 Aller plus loin — Licence : Dessiner les portraits de phase
> Tracer le portrait de phase $(\beta,\dot\beta)$ du mode en opposition : l'énergie potentielle $\omega_0^2(1-\cos\beta)+\tfrac\kappa2(1-\cos2\beta)$ est à un seul puits. Le mode en phase correspond à celui du pendule simple.




> [!question]- 🔭 Aller plus loin — Master : Perturbations dans le mode en opposition
> Étudier de la même façon la stabilité du mode en opposition : montrer que l'équation de $q$ est $\ddot q+\dots$ et trouver s'il existe un seuil.




> [!question]- 🔭 Aller plus loin — Master : Chaos
> Au-delà du seuil, le mouvement devient irrégulier pour des énergies élevées : étudier numériquement les sections de Poincaré.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex2-couplage-de-deux-oscillateurs-harmoniques-dissymetriques|Exercice 2 — Couplage de deux oscillateurs harmoniques dissymétriques]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex3-oscillations-libres-et-forcees-d-un-couplage-pendule-chariot|Exercice 3 — Oscillations libres et forcées d'un couplage pendule-chariot]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex4-frequence-propre-d-une-molecule-diatomique|Exercice 4 — Fréquence propre d'une molécule diatomique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex5-complement-niveau-1-cpge-pendules-couples-par-un-ressort-attache-a-mi-hauteur|Exercice 5 — Complément (niveau 1, CPGE) : pendules couplés par un ressort attaché à mi-hauteur]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex6-complement-niveau-2-ambitieux-trois-masses-quatre-ressorts-diagonalisation-et-perturbation|Exercice 6 — Complément (niveau 2, ambitieux) : trois masses, quatre ressorts, diagonalisation et perturbation]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex7-complement-niveau-2-ambitieux-oscillateurs-desaccordes-anticroisement-et-transfert-d-energie|Exercice 7 — Complément (niveau 2, ambitieux) : oscillateurs désaccordés, anticroisement et transfert d'énergie]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex9-complement-niveau-3-ens-anneau-de-n-oscillateurs-modes-de-fourier-et-propagation-du-signal|Exercice 9 — Complément (niveau 3, ENS) : anneau de N oscillateurs, modes de Fourier et propagation du signal]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-4-oscillateurs-couples-petites-oscillations-modes-propres-et-battements/oscillateurs-couples/ex1-pendules-couples-et-battements|Exercice 1 — Pendules couplés et battements]]


