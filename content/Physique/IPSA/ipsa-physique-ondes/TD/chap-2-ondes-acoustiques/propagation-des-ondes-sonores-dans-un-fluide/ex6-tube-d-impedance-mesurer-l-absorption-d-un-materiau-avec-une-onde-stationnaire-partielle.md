---
title: "Exercice 6 — Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/index|⬅ Retour]] · <a href="/pdfs/td2_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_PhV212_enonce)</a> · <a href="/pdfs/td2_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_enonce)</a> · <a href="/pdfs/td2_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_aides)</a> · <a href="/pdfs/td2_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td2_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_PhV212_corrige)</a> · <a href="/pdfs/td2_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_corrige)</a> · <a href="/pdfs/td2_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 6. Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle *(facultatif)*

Un ingénieur acousticien veut caractériser une mousse absorbante. Il place un échantillon à l'extrémité
$x=0$ d'un tube rigide cylindrique de rayon $a=2{,}0$ cm. Un haut-parleur, placé loin à gauche, envoie dans
le tube ($x<0$) une onde plane de fréquence $f=1000$ Hz. Dans l'air ($c=340~\text{m}\cdot\text{s}^{-1}$),
la surpression est la somme d'une onde incidente et d'une onde réfléchie par l'échantillon :
$$\tilde p_I=A\,e^{i(\omega t-kx)},\qquad\tilde p_R=R\,A\,e^{i(\omega t+kx)},\qquad R=|R|\,e^{i\varphi}\in\mathbb C,\quad A>0.$$
Un microphone-sonde mobile mesure l'amplitude $|\tilde p|$ en fonction de la distance $d=-x$ à l'échantillon.
On relève : $|\tilde p|_{\max}/|\tilde p|_{\min}=3$ et le premier minimum, le plus proche de l'échantillon,
est situé à $d_1=4{,}25$ cm.

**q1.** Montrer que $|\tilde p(x)|^2=A^2\big(1+|R|^2+2|R|\cos(2kx+\varphi)\big)$ et que le signal total se décompose
en une onde progressive et une onde stationnaire pure dont on précisera les amplitudes.

> [!tip]- 💡 Coup de pouce
> Écrivez $|a+b|^2=(a+b)(a+b)^{*}$. Pour la décomposition, écrivez $R=|R|e^{i\varphi}$ et séparez $1=(1-|R|)+|R|$.


> [!example]- 📝 Solution détaillée
> **Module au carré**
>
> $\tilde p=Ae^{i\omega t}\big(e^{-ikx}+Re^{ikx}\big)$, donc
> $$|\tilde p|^2=A^2\big(1+|R|^2+Re^{2ikx}+R^{*}e^{-2ikx}\big)=A^2\big(1+|R|^2+2|R|\cos(2kx+\varphi)\big).$$
>
> **Décomposition progressive + stationnaire**
>
> $$e^{-ikx}+|R|e^{i\varphi}e^{ikx}=(1-|R|)e^{-ikx}+|R|\big(e^{-ikx}+e^{i\varphi}e^{ikx}\big)=(1-|R|)e^{-ikx}+2|R|e^{i\varphi/2}\cos\!\big(kx+\tfrac\varphi2\big).$$
> Le premier terme est une onde progressive d'amplitude $A(1-|R|)$, qui transporte l'énergie vers l'échantillon (pour $|R|<1$) ; le second est une onde stationnaire pure d'amplitude de ventre $2A|R|$, qui ne transporte aucune énergie en moyenne (cf. exercice 5).


**q2.** Définir le rapport d'ondes stationnaires $s=p_{\max}/p_{\min}$ et l'exprimer en fonction de
$|R|$. En déduire $|R|(s)$. Que valent $s$ pour $|R|=0$ et $|R|=1$ ?

> [!tip]- 💡 Coup de pouce
> Maximum et minimum du cosinus : $\pm1$, donc $|\tilde p|_{\max/\min}=A\sqrt{1+|R|^2\pm2|R|}$.


> [!success]- ✅ Correction
> $s=\dfrac{1+|R|}{1-|R|}$, $|R|=\dfrac{s-1}{s+1}$ ; $s=1$ pour $R=0$, $s\to\infty$ pour $|R|=1$.


> [!example]- 📝 Solution détaillée
> **Maximum, minimum, rapport**
>
> $|\tilde p|_{\max}=A\sqrt{1+|R|^2+2|R|}=A(1+|R|)$ et $|\tilde p|_{\min}=A\sqrt{1+|R|^2-2|R|}=A(1-|R|)$. D'où
> $$s=\frac{1+|R|}{1-|R|}\quad\Longleftrightarrow\quad|R|=\frac{s-1}{s+1}.$$
> Le rapport $s$ ne dépend pas de l'amplitude $A$ incidente (qui dépend du haut-parleur) : c'est ce qui en fait une grandeur de mesure robuste. Pour $|R|=0$ (onde progressive pure), $s=1$ : le signal est plat. Pour $|R|=1$ (onde stationnaire pure), $p_{\min}=0$ et $s\to\infty$.


**q3.** Montrer que les minima de $|\tilde p|$ sont aux distances $d_m=\dfrac{\varphi+\pi}{2k}+m\dfrac\lambda2$.
En déduire $\varphi$ en fonction de $d_1$ et $k$.

> [!tip]- 💡 Coup de pouce
> Dans la formule de la question 1, remplacez $x$ par $-d$ ; le minimum est atteint quand le cosinus vaut $-1$.


> [!success]- ✅ Correction
> $\varphi=2kd_1-\pi$ (modulo $2\pi$).


> [!example]- 📝 Solution détaillée
> **Positions des minima**
>
> Avec $x=-d$ : $\cos(\varphi-2kd)=-1\Longleftrightarrow\varphi-2kd=-\pi-2m'\pi$, soit $d=\dfrac{\varphi+\pi}{2k}+m'\pi/k=\dfrac{\varphi+\pi}{2k}+m'\dfrac\lambda2$. En choisissant $\varphi\in\,]-\pi,\pi]$, le premier minimum (le plus proche de l'échantillon) est $d_1=(\varphi+\pi)/(2k)\in\,]0,\lambda/2]$ :
> $$\boxed{\varphi=2kd_1-\pi}.$$


**q4.** Application numérique : calculer $\lambda$, $|R|$, $\varphi$ et $R$. En déduire le coefficient
d'absorption $\alpha=1-|R|^2$ puis l'impédance de l'échantillon $Z_s=\tilde p(0)/\tilde v(0)$,
en fonction de $Z_0$. Cet échantillon se comporte-t-il comme une masse ou comme un ressort ?

> [!tip]- 💡 Coup de pouce
> $\tilde v(x)=(A/Z_0)\big(e^{-ikx}-Re^{ikx}\big)e^{i\omega t}$ (onde réfléchie : signe moins). Pour la fraction complexe, multipliez par le conjugué du dénominateur.


> [!success]- ✅ Correction
> $\lambda=0{,}34$ m ; $|R|=0{,}5$ ; $\varphi\approx-\pi/2$ ; $R=-0{,}5i$ ; $\alpha=0{,}75$ ; $Z_s=Z_0(0{,}6-0{,}8i)$ : comportement de type raideur (ressort).


> [!example]- 📝 Solution détaillée
> **Module et phase de $R$**
>
> $\lambda=c/f=0{,}340$ m ; $k=2\pi/\lambda\approx18{,}5$ rad/m. D'après la question 2, $|R|=(3-1)/(3+1)=0{,}5$. D'après la question 3 :
> $$\varphi=2kd_1-\pi=2\times18{,}5\times0{,}0425-\pi\approx1{,}57-\pi\approx-\frac\pi2\quad(\text{car }d_1=\lambda/8).$$
> Donc $R=0{,}5\,e^{-i\pi/2}=-0{,}5\,i$. Absorption : $\alpha=1-|R|^2=0{,}75$ : $75\ \%$ de l'énergie incidente est absorbée par l'échantillon.
>
> **Impédance de l'échantillon**
>
> En $x=0$ : $\tilde p(0)=A(1+R)e^{i\omega t}$ et $\tilde v(0)=(A/Z_0)(1-R)e^{i\omega t}$, donc $Z_s=Z_0\dfrac{1+R}{1-R}$. Avec $R=-0{,}5i$ :
> $$\frac{Z_s}{Z_0}=\frac{1-0{,}5i}{1+0{,}5i}=\frac{(1-0{,}5i)^2}{1+0{,}25}=\frac{0{,}75-i}{1{,}25}=0{,}6-0{,}8i.$$
> La partie réelle positive ($0{,}6$) traduit la dissipation. Avec la convention $e^{+i\omega t}$, un ressort de raideur $K$ a pour impédance $K/(i\omega)=-iK/\omega$ (partie imaginaire négative) et une masse $i\omega m$ (partie imaginaire positive) : l'échantillon se comporte ici comme un ressort amorti (matériau poreux devant une cavité d'air, par exemple).


**q5.** Retrouver, avec ce formalisme, les cas limites : paroi rigide, extrémité ouverte idéale, matériau
parfaitement adapté. Pour chacun, donner $Z_s$, $R$, $s$ et la position du premier minimum.
Faire le lien avec les exercices 2 et 3.

> [!success]- ✅ Correction
> Paroi rigide : $Z_s\to\infty$, $R=1$, $d_1=\lambda/4$. Extrémité ouverte : $Z_s=0$, $R=-1$, $d_1=\lambda/2$ ($\equiv0$). Adapté : $Z_s=Z_0$, $R=0$, $s=1$.


> [!example]- 📝 Solution détaillée
> **Trois cas limites**
>
> - **Paroi rigide** : $\tilde v(0)=0$, $Z_s\to\infty$, $R=+1$, $\varphi=0$, $s\to\infty$. Le premier minimum de pression est à $d_1=\lambda/4$ de la paroi, et $x=0$ est un ventre de pression : c'est le cas de l'extrémité fermée de l'exercice 3.
> - **Extrémité ouverte idéale** : $\tilde p(0)=0$, $Z_s=0$, $R=-1$, $\varphi=\pi$, $s\to\infty$ ; $d_1=\lambda/2$, c'est-à-dire un minimum (nœud de pression) en $x=0$ : cas de l'exercice 2.
> - **Matériau adapté** : $Z_s=Z_0$, $R=0$, $s=1$ : plus aucune onde réfléchie, onde progressive pure, $\alpha=1$. C'est l'objectif d'un traitement anéchoïque (cf. exercice 8).


**q6.** Pour mesurer $R$ sur toute une bande de fréquences, on utilise deux microphones fixes en $x_1$ et
$x_2$ ($x_1-x_2=\sigma>0$). On mesure la fonction de transfert complexe
$H=\tilde p(x_2)/\tilde p(x_1)$. Exprimer $R$ en fonction de $H$, $k$, $x_1$, $x_2$.
Pourquoi la méthode échoue-t-elle quand $k\sigma=\pi$ ? En déduire la fréquence maximale
d'utilisation pour $\sigma=5$ cm. Pourquoi le tube de rayon $a=2$ cm impose-t-il aussi une limite
haute (on admettra que la propagation est plane si $f<1{,}84\,c/(2\pi a)$) ?

> [!tip]- 💡 Coup de pouce
> $H$ est une fonction affine de $R$ : écrivez $H\,\tilde p(x_1)=\tilde p(x_2)$ et isolez $R$.


> [!success]- ✅ Correction
> $R=\dfrac{He^{-ikx_1}-e^{-ikx_2}}{e^{ikx_2}-He^{ikx_1}}$ ; $f<c/(2\sigma)=3{,}4$ kHz ; $f<1{,}84c/(2\pi a)\approx5$ kHz.


> [!example]- 📝 Solution détaillée
> **Expression de $R$**
>
> $$H\big(e^{-ikx_1}+Re^{ikx_1}\big)=e^{-ikx_2}+Re^{ikx_2}\quad\Longrightarrow\quad\boxed{R=\frac{He^{-ikx_1}-e^{-ikx_2}}{e^{ikx_2}-He^{ikx_1}}}.$$
>
> **Conditions d'application**
>
> Si $k\sigma=\pi$, alors $e^{-ikx_2}=e^{-ik x_1}e^{ik\sigma}=-e^{-ikx_1}$ et de même $e^{ikx_2}=-e^{ikx_1}$ : donc $\tilde p(x_2)=-\tilde p(x_1)$ quelle que soit la valeur de $R$, et $H=-1$ ne contient plus aucune information : le dénominateur s'annule. Il faut $\sigma<\lambda/2$, soit $f<c/(2\sigma)=340/0{,}1=3{,}4$ kHz (en pratique on se limite à $0{,}45\lambda$). Pour le tube, l'hypothèse d'onde plane suppose que seul le mode de pression uniforme sur la section se propage : au-delà de $f_c=1{,}84\,c/(2\pi a)=1{,}84\times340/(2\pi\times0{,}02)\approx5$ kHz, des modes transverses apparaissent et la décomposition en deux ondes planes n'est plus valable.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex2-onde-stationnaire-tube-de-kundt-ouvert|Exercice 2 — Onde stationnaire, tube de Kundt ouvert]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex3-onde-stationnaire-tube-de-kundt-ferme-a-faire-a-la-maison|Exercice 3 — Onde stationnaire, tube de Kundt fermé (à faire à la maison)]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex5-energie-intensite-acoustique-et-niveau-sonore-de-l-oreille-humaine-a-l-onde-stationnaire|Exercice 5 — Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex8-transmission-a-travers-une-lame-adaptation-d-impedance-loi-de-masse-et-double-vitrage|Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex4-reflexion-et-transmission-d-une-onde-acoustique-a-une-interface-entre-deux-fluides|Exercice 4 — Réflexion et transmission d'une onde acoustique à une interface entre deux fluides]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex7-resonateur-de-helmholtz-la-bouteille-qui-chante|Exercice 7 — Résonateur de Helmholtz : la bouteille qui chante]]

