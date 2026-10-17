---
title: "Exercice 10 — Corde discrète (chaîne de masses) : dispersion, coupure et vitesse de groupe"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td1_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_ex1_coup_de_pouce.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_coup_de_pouce)</a> · <a href="/pdfs/td1_ex1_solution_detaillee.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_solution_detaillee)</a> · <a href="/pdfs/td1_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_PhV212_fiche)</a> · <a href="/pdfs/td1_ex1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_ex1_fiche)</a> · <a href="/pdfs/td1_exs_maison_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_exs_maison_fiche)</a>

### Exercice 10. Corde discrète (chaîne de masses) : dispersion, coupure et vitesse de groupe *(facultatif)*

Une corde n'est pas un milieu continu : on modélise ici une corde « discrète » par $N$ masses ponctuelles identiques $m$, régulièrement espacées de la distance $a$ au repos, reliées par des fils sans masse tendus avec la tension $F$ (constante, considérée comme identique pour tous les fils). La masse $n$ a pour position au repos $x_n=na$ et se déplace transversalement de $y_n(t)$. On suppose les déplacements petits devant $a$.

**q1.** Écrire le PFD sur la masse $n$ (projection transversale, petits angles) et établir
$$m\,\ddot y_n=\frac{F}{a}\left(y_{n+1}-2y_n+y_{n-1}\right).$$

> [!tip]- 💡 Coup de pouce
> **Pente des fils**
>
> Le fil entre $n$ et $n+1$ a pour pente $\dfrac{y_{n+1}-y_n}{a}$. Sa tension a pour composante transversale $F\times\text{pente}$.


> [!success]- ✅ Correction
> **Résultat**
>
> Force du fil de droite : $+F\dfrac{y_{n+1}-y_n}{a}$ ; force du fil de gauche : $-F\dfrac{y_n-y_{n-1}}{a}$. La somme donne l'équation demandée.


> [!example]- 📝 Solution détaillée
> **Établissement**
>
> La masse $n$ subit deux tensions. La composante transversale de la tension du fil de droite est $F\sin\alpha_+\approx F\tan\alpha_+=F\dfrac{y_{n+1}-y_n}{a}$ (dirigée vers le haut si $y_{n+1}>y_n$), celle du fil de gauche est $-F\dfrac{y_n-y_{n-1}}{a}$. Le poids est négligé. Le PFD transversal s'écrit
> $$m\ddot y_n=F\,\frac{y_{n+1}-y_n}{a}-F\,\frac{y_n-y_{n-1}}{a}=\frac{F}{a}\left(y_{n+1}-2y_n+y_{n-1}\right).$$
> La tension reste égale à $F$ à l'ordre 1 (variation de longueur du second ordre).


**q2.** Limite continue. On pose $\mu=m/a$ et $y_n(t)=y(na,t)$. Développer $y_{n\pm1}$ en série de Taylor en $x=na$ jusqu'à l'ordre 4 et montrer que l'équation devient
$$\frac{\partial^2y}{\partial t^2}=c_0^2\left(\frac{\partial^2y}{\partial x^2}+\frac{a^2}{12}\frac{\partial^4y}{\partial x^4}+\dots\right)$$
avec $c_0=\sqrt{F/\mu}$. Commenter : à quelle condition retrouve-t-on l'équation de d'Alembert ?

> [!tip]- 💡 Coup de pouce
> **Développement**
>
> $y(x\pm a)=y\pm a\,y'+\dfrac{a^2}{2}y''\pm\dfrac{a^3}{6}y'''+\dfrac{a^4}{24}y''''+\dots$ La somme $y(x+a)+y(x-a)$ élimine les termes impairs.


> [!success]- ✅ Correction
> **Résultat**
>
> $y_{n+1}-2y_n+y_{n-1}=a^2y''+\dfrac{a^4}{12}y''''+\dots$ On retrouve d'Alembert si $a\ll\lambda$ (les dérivées d'ordre 4 sont alors négligeables devant les dérivées d'ordre 2).


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> $$y(x+a)+y(x-a)-2y(x)=a^2y''+\frac{2a^4}{24}y''''+\dots=a^2y''+\frac{a^4}{12}y''''+\dots$$
> En divisant l'équation de la question 1 par $m$ et en utilisant $\dfrac{F}{ma}=\dfrac{F}{\mu a^2}=\dfrac{c_0^2}{a^2}$ :
> $$\ddot y=\frac{c_0^2}{a^2}\left(a^2y''+\frac{a^4}{12}y''''+\dots\right)=c_0^2\left(y''+\frac{a^2}{12}y''''+\dots\right).$$
> Pour une onde de longueur d'onde $\lambda$, $y''''\sim(2\pi/\lambda)^2y''$, donc le second terme est de l'ordre de $\dfrac{1}{12}\left(\dfrac{2\pi a}{\lambda}\right)^2$ devant le premier. La limite continue est valable si $a\ll\lambda$. Le terme en $y''''$ est la source de la dispersion.


**q3.** On cherche $y_n=\text{Re}\left[A\,e^{\,j(\omega t-kna)}\right]$. Établir la relation de dispersion
$$\omega=\omega_{\max}\left|\sin\frac{ka}{2}\right|,\qquad\omega_{\max}=2\sqrt{\frac{F}{ma}}.$$
Montrer qu'on retrouve $\omega\simeq c_0k$ pour $ka\ll1$. Pourquoi peut-on se limiter à $|k|\le\pi/a$ ?

> [!tip]- 💡 Coup de pouce
> **Injection**
>
> $y_{n\pm1}=y_n\,e^{\mp jka}$ en complexes. Utiliser $2\cos\theta-2=-4\sin^2(\theta/2)$.


> [!success]- ✅ Correction
> **Résultat**
>
> $-m\omega^2=\dfrac{F}{a}\left(2\cos ka-2\right)=-\dfrac{4F}{a}\sin^2\dfrac{ka}{2}$, donc $\omega=2\sqrt{\dfrac{F}{ma}}\left|\sin\dfrac{ka}{2}\right|$.


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> En reportant $\underline{y}_n=A\,e^{\,j(\omega t-kna)}$ dans l'équation de la question 1 :
> $$-m\omega^2=\frac{F}{a}\left(e^{-jka}-2+e^{jka}\right)=\frac{F}{a}\left(2\cos ka-2\right)=-\frac{4F}{a}\sin^2\frac{ka}{2}.$$
> Donc $\omega^2=\dfrac{4F}{ma}\sin^2\dfrac{ka}{2}$ et $\omega=\omega_{\max}\left|\sin\dfrac{ka}{2}\right|$ avec $\omega_{\max}=2\sqrt{F/(ma)}=2c_0/a$.
>
> Pour $ka\ll1$ : $\sin\dfrac{ka}{2}\approx\dfrac{ka}{2}$, donc $\omega\approx\omega_{\max}\dfrac{ka}{2}=\sqrt{\dfrac{F}{ma}}\,ka=\sqrt{\dfrac{Fa}{m}}\,k=c_0k$ : c'est la relation de dispersion de d'Alembert.
>
> Comme $e^{-jk'na}=e^{-jkna}$ dès que $k'=k+2\pi p/a$ ($p$ entier), $k$ et $k+2\pi/a$ décrivent les mêmes déplacements : il n'y a que $|k|\le\pi/a$ à considérer (première zone de Brillouin).


**q4.** Calculer la vitesse de phase $v_\varphi=\omega/k$ et la vitesse de groupe $v_g=\dfrac{\mathrm{d}\omega}{\mathrm{d}k}$ en fonction de $c_0$ et de $ka$. Que valent-elles pour $ka\to0$ et pour $k=\pi/a$ ? Interpréter. Application numérique : $F=10\ \text{N}$, $m=10\ \text{g}$, $a=10\ \text{cm}$, calculer $c_0$, $\omega_{\max}$, $f_{\max}$, puis $k$, $\lambda$, $v_\varphi$ et $v_g$ pour $\omega=0{,}9\,\omega_{\max}$.

> [!tip]- 💡 Coup de pouce
> **Dérivée**
>
> $\dfrac{\mathrm{d}}{\mathrm{d}k}\sin\dfrac{ka}{2}=\dfrac{a}{2}\cos\dfrac{ka}{2}$.


> [!success]- ✅ Correction
> **Résultat**
>
> $v_\varphi=c_0\dfrac{\sin(ka/2)}{ka/2}$ et $v_g=c_0\cos\dfrac{ka}{2}$. Pour $ka\to0$ les deux valent $c_0$. Pour $k=\pi/a$ : $v_g=0$ et $v_\varphi=\dfrac{2c_0}{\pi}$. Numériquement : $c_0=10\ \text{m/s}$, $\omega_{\max}=200\ \text{rad/s}$ ($f_{\max}\approx31{,}8\ \text{Hz}$) ; pour $\omega=0{,}9\omega_{\max}$ : $k\approx22{,}4\ \text{rad/m}$, $\lambda\approx0{,}28\ \text{m}$ ($\approx2{,}8a$), $v_\varphi\approx8{,}0\ \text{m/s}$, $v_g\approx4{,}4\ \text{m/s}$.


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> $$v_\varphi=\frac{\omega}{k}=\frac{\omega_{\max}\sin(ka/2)}{k}=\frac{2c_0}{a}\cdot\frac{\sin(ka/2)}{k}=c_0\,\frac{\sin(ka/2)}{ka/2},\qquad v_g=\frac{\mathrm{d}\omega}{\mathrm{d}k}=\frac{\omega_{\max}a}{2}\cos\frac{ka}{2}=c_0\cos\frac{ka}{2}.$$
> Pour $ka\to0$ : $v_\varphi\to c_0$ et $v_g\to c_0$ (milieu non dispersif). Pour $ka=\pi$ : $v_g=0$ (onde stationnaire : $y_n\propto(-1)^n$, masses voisines en opposition de phase), $v_\varphi=2c_0/\pi\approx0{,}64\,c_0$.
>
> Application numérique : $c_0=\sqrt{Fa/m}=\sqrt{10\times0{,}1/0{,}01}=10\ \text{m/s}$, $\omega_{\max}=2c_0/a=200\ \text{rad/s}$, $f_{\max}\approx31{,}8\ \text{Hz}$.
> Pour $\omega=0{,}9\omega_{\max}$ : $\sin(ka/2)=0{,}9$, $ka/2=1{,}120\ \text{rad}$, $ka\approx2{,}240$, $k\approx22{,}4\ \text{rad/m}$, $\lambda=2\pi/k\approx0{,}281\ \text{m}$. $v_\varphi=180/22{,}4\approx8{,}04\ \text{m/s}$ et $v_g=10\times\cos(1{,}120)\approx4{,}36\ \text{m/s}$.
> Le paquet d'ondes (donc l'énergie, cf. exercice 7) avance environ deux fois plus lentement que les crêtes.


**q5.** (*) Fréquence supérieure à la coupure. On excite la chaîne à $\omega>\omega_{\max}$. On cherche $y_n=A\,(-1)^n e^{-qn}\cos\omega t$ avec $q>0$. Montrer que cela est possible et exprimer $q$ en fonction de $\omega/\omega_{\max}$. Application : $\omega=1{,}25\,\omega_{\max}$. Que devient l'onde ?

> [!tip]- 💡 Coup de pouce
> **Nombre d'onde complexe**
>
> Poser $ka=\pi+jq$ dans la relation de la question 3 et utiliser $\sin\left(\dfrac{\pi}{2}+j\dfrac{q}{2}\right)=\cosh\dfrac{q}{2}$.


> [!success]- ✅ Correction
> **Résultat**
>
> $\cosh\dfrac{q}{2}=\dfrac{\omega}{\omega_{\max}}$, soit $q=2\,\text{arcosh}\dfrac{\omega}{\omega_{\max}}$. Pour $\omega=1{,}25\omega_{\max}$ : $q/2=\ln2$, $q=2\ln2\approx1{,}39$ : l'amplitude est multipliée par $e^{-q}=1/4$ (avec changement de signe) de masse en masse. L'onde est évanescente : la chaîne se comporte comme un filtre passe-bas.


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> On injecte $y_n=A\,r^n\cos\omega t$, avec $r=-e^{-q}$, dans l'équation de la question 1 :
> $$-m\omega^2=\frac{F}{a}\left(r+\frac{1}{r}-2\right)=\frac{F}{a}\left(-e^{-q}-e^{q}-2\right)=-\frac{4F}{a}\cosh^2\frac{q}{2}.$$
> Donc $\omega^2=\omega_{\max}^2\cosh^2\dfrac{q}{2}$, soit $\cosh\dfrac{q}{2}=\dfrac{\omega}{\omega_{\max}}\ge1$ : c'est possible si et seulement si $\omega\ge\omega_{\max}$.
> Pour $\omega=1{,}25\,\omega_{\max}$ : $\cosh(q/2)=1{,}25\Rightarrow q/2=\ln\left(1{,}25+\sqrt{1{,}25^2-1}\right)=\ln2$, donc $q=2\ln2\approx1{,}39$ et $e^{-q}=\dfrac14$.
> L'excitation ne se propage pas : elle décroît exponentiellement sur une longueur $\approx a/q\approx0{,}72\,a$. Il n'y a pas de transport d'énergie : la chaîne coupe les hautes fréquences.


**q6.** (*) Chaîne finie. La chaîne comporte $N$ masses et les deux extrémités sont fixes ($y_0=y_{N+1}=0$). Montrer que les modes propres sont $y_n\propto\sin\dfrac{np\pi}{N+1}$ avec $p=1,\dots,N$ et exprimer $\omega_p$. Pour $N=3$, $F=10\ \text{N}$, $m=10\ \text{g}$, $a=10\ \text{cm}$, comparer les pulsations aux modes de la corde continue de même longueur $L=(N+1)a$ et de même masse linéique. Conclure.

> [!tip]- 💡 Coup de pouce
> **Ondes stationnaires**
>
> Chercher $y_n=A\sin(kna+\varphi)\cos\omega t$. Les conditions aux limites fixent $\varphi$ et $k$.


> [!success]- ✅ Correction
> **Résultat**
>
> $k_p=\dfrac{p\pi}{(N+1)a}$ et $\omega_p=2\sqrt{\dfrac{F}{ma}}\sin\dfrac{p\pi}{2(N+1)}$. Pour $N=3$ : $\omega_p\approx76{,}5\ ;\ 141{,}4\ ;\ 184{,}8\ \text{rad/s}$, contre $78{,}5\ ;\ 157{,}1\ ;\ 235{,}6\ \text{rad/s}$ pour la corde continue. L'écart est de $2{,}5\ \%$ pour $p=1$, $10\ \%$ pour $p=2$ et $22\ \%$ pour $p=3$.


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> $y_0=0$ impose $\varphi=0$ : $y_n=A\sin(kna)\cos\omega t$ (la relation de dispersion de la question 3 reste valable, car les ondes stationnaires sont des superpositions de deux ondes progressives de même $\omega$). $y_{N+1}=0$ impose $k(N+1)a=p\pi$, soit $k_p=\dfrac{p\pi}{(N+1)a}=\dfrac{p\pi}{L}$. Les $N$ valeurs $p=1,\dots,N$ donnent $N$ modes distincts (pour $p=N+1$, $y_n\equiv0$). Alors
> $$\omega_p=\omega_{\max}\sin\frac{k_pa}{2}=2\sqrt{\frac{F}{ma}}\sin\frac{p\pi}{2(N+1)}.$$
> Pour $N=3$ ($\omega_{\max}=200\ \text{rad/s}$) : $\omega_1=200\sin\dfrac{\pi}{8}\approx76{,}5$, $\omega_2=200\sin\dfrac{\pi}{4}\approx141{,}4$, $\omega_3=200\sin\dfrac{3\pi}{8}\approx184{,}8\ \text{rad/s}$.
> Corde continue de longueur $L=0{,}4\ \text{m}$ et $c_0=10\ \text{m/s}$ : $\omega_p^{\text{cont}}=\dfrac{p\pi c_0}{L}=78{,}5\,p\ \text{rad/s}$.
> Le nombre de modes de la chaîne est limité à $N$ et leurs fréquences s'écartent d'autant plus des harmoniques $pf_1$ que $p$ est grand : le modèle continu n'est valable que pour $ka\ll1$, c'est-à-dire pour les premiers modes ($p\ll N+1$).


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex4-equation-des-cordes-vibrantes-et-onde-progressive|Exercice 4 — Équation des cordes vibrantes et onde progressive]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex8-energie-et-puissance-d-une-onde-sur-une-corde-impedance-caracteristique|Exercice 8 — Énergie et puissance d'une onde sur une corde : impédance caractéristique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]]

