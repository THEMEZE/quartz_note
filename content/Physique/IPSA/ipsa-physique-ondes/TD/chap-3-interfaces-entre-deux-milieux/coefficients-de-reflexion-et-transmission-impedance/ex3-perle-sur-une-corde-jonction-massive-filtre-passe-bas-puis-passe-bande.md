---
title: "Exercice 3 — Perle sur une corde : jonction massive, filtre passe-bas puis passe-bande"
tags:
  - td
  - chap-3-interfaces-entre-deux-milieux
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/index|⬅ Retour]] · <a href="/pdfs/td3_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_PhV212_enonce)</a> · <a href="/pdfs/td3_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_enonce)</a> · <a href="/pdfs/td3_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td3_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td3_PhV212_corrige)</a> · <a href="/pdfs/td3_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td3_corrige)</a>

### Exercice 3. Perle sur une corde : jonction massive, filtre passe-bas puis passe-bande *(facultatif)*

*Difficulté ●●●●○ · ⏱ 50 min · Type : Approfondissement / Problème de synthèse*

Deux cordes tendues horizontalement avec la même tension $F$ sont reliées en $O$ ($x=0$) : la corde (1),
de masse linéique $\mu_1$, occupe $x<0$ ; la corde (2), de masse linéique $\mu_2$, occupe $x>0$. On note
$Z_i=\sqrt{F\mu_i}$ leurs impédances mécaniques. Contrairement à l'exercice 1, on fixe en $O$ une
*perle* ponctuelle de masse $M$, qui ne peut se déplacer que transversalement (pesanteur négligée).

**Convention de cet exercice** (différente de l'exercice 1) : l'onde incidente se propage vers les $x$
*croissants*. En notation complexe $e^{i\omega t}$, les déplacements sont
$$y_1(x,t)=A\big(e^{-ik_1x}+r\,e^{ik_1x}\big)e^{i\omega t}\ (x<0),\qquad y_2(x,t)=t\,A\,e^{-ik_2x}e^{i\omega t}\ (x>0),$$
avec $k_i=\omega\sqrt{\mu_i/F}$, de sorte que $r$ et $t$ sont les coefficients de réflexion et de transmission
en amplitude de *déplacement*.

Données numériques (cordes identiques, parties numériques) : $F=100$ N, $\mu_1=\mu_2=4{,}0~\text{g}\cdot\text{m}^{-1}$,
$M=2{,}0$ g.


> [!question]- 🪝 Accroche
> **Une toute petite masse peut-elle bloquer une onde ?**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *Sur une corde tendue, on fixe une perle de $2$ g, dont la masse est comparable à celle de $50$ cm de corde. Une ondulation lente (large) passe-t-elle ? Une ondulation rapide (étroite) passe-t-elle ? **Qu'est-ce qui change entre les deux ?** Et si on ajoute un ressort entre la perle et le support ?*
>
> **Idée clé : la perle ajoute en série une impédance $iM\omega$ qui grandit avec la fréquence.** Les coefficients ne sont plus ceux de l'exercice 1 mais
> $$r=\frac{Z_1-Z_2-iM\omega}{Z_1+Z_2+iM\omega},\qquad t=\frac{2Z_1}{Z_1+Z_2+iM\omega}.$$
> À basse fréquence ($M\omega\ll Z$), on retrouve la corde sans perle ; à haute fréquence ($M\omega\gg Z$), $t\to0$ et $r\to-1$ : tout est réfléchi, la perle se comporte comme un point fixe.




> [!abstract]- 🧠 À savoir avant
> **Jonction entre deux cordes (exercice 1)**
>
> Connaître les deux conditions de raccord en l'absence de masse en $O$ (continuité de $y$ et de $\partial_xy$), les coefficients $r=\dfrac{Z_1-Z_2}{Z_1+Z_2}$ et $t=\dfrac{2Z_1}{Z_1+Z_2}$ qui en résultent, et la relation $k_i=\omega Z_i/F$.
>
> **Deuxième loi de Newton pour un point matériel**
>
> $M\,\ddot y=\sum F_{\mathrm{transv}}$. La force transverse exercée par une corde de tension $F$ sur une extrémité est $\pm F\,\partial_xy$ (petits angles), avec le signe $+$ si la corde est située à droite du point et $-$ si elle est à gauche.
>
> **Puissance transportée par une onde de corde**
>
> Pour une onde progressive sinusoïdale de déplacement d'amplitude $A$, $\langle\mathcal P\rangle=\tfrac12Z\omega^2A^2$ (cf. exercice 1, aller plus loin).




> [!info]- 🎯 Ce que tu sauras faire
> **Modifier une condition de raccord et en tirer la conséquence en fréquence**
>
> Savoir écrire le bilan des forces sur une masse placée à une jonction, en déduire de nouveaux coefficients $r(\omega)$ et $t(\omega)$ *complexes et dépendant de la fréquence*, et interpréter la perle comme une impédance additionnelle placée en série avec celle de la corde (analogie avec une inductance).
>
> Savoir passer du domaine fréquentiel au domaine temporel (multiplication par $i\omega$ $\leftrightarrow$ dérivation, $e^{-i\omega\tau}\leftrightarrow$ retard $\tau$) et reconnaître un filtre passe-bas puis passe-bande.




> [!tip]- 📖 Rappel de cours
> **Impédance mécanique et éléments en série**
>
> Pour une onde progressive vers $+x$ sur une corde, la force transverse que la partie gauche exerce sur la partie droite est $-F\,\partial_xy=ikF\,y$ et la vitesse transverse est $\partial_ty=i\omega y$ : leur rapport est $kF/\omega=Z$. L'impédance mécanique est donc le rapport *force transverse / vitesse transverse*.
>
> Un élément ponctuel placé en $O$ partage la même vitesse transverse que les deux cordes ($y$ est continu) et les forces s'y additionnent : il se met donc en **série** avec elles, comme dans un circuit où la vitesse joue le rôle du courant et la force celui de la tension. Une masse a pour impédance $iM\omega$ (comme une inductance $iL\omega$), un ressort de raideur $K$ relié à un support fixe a pour impédance $K/(i\omega)$ (comme une capacité), un amortisseur visqueux de coefficient $\eta$ a pour impédance $\eta$ (comme une résistance).




> [!note]- 🧮 Outils mathématiques
> **Fractions complexes et module au carré**
>
> $|a+ib|^2=a^2+b^2$ ; $\left|\dfrac{a-ib}{a+ib}\right|^2=1$ quand $a,b$ sont réels. Pour $|r|^2$ et $|t|^2$, écrire numérateur et dénominateur sous la forme $a+ib$.
>
> **Dérivation par rapport au temps et notation complexe**
>
> $\partial_t\to i\omega$ : $\partial_t^2y=-\omega^2y$ ; réciproquement, la multiplication d'un spectre par $i\omega$ correspond à une dérivation temporelle et celle par $e^{-i\omega\tau}$ à un retard $\tau$.
>
> **Développement limité en $\omega\tau$**
>
> $\dfrac1{1+i\omega\tau}\approx1-i\omega\tau\approx e^{-i\omega\tau}$ pour $\omega\tau\ll1$ ; $\dfrac{-i\omega\tau}{1+i\omega\tau}\approx-i\omega\tau$.
>
> **Filtre du premier ordre : fréquence de coupure et décibels**
>
> $T_E=\dfrac1{1+(\omega/\omega_c)^2}$ vaut $\tfrac12$ ($-3$ dB) en $\omega_c$ ; à haute fréquence $T_E\approx(\omega_c/\omega)^2$, soit $-6$ dB par octave ($-20$ dB par décade).
>
> **Résonance : réactance et largeur à mi-puissance**
>
> Avec $X(\omega)=M\omega-K/\omega$, $X(\omega_0)=0$ et, au voisinage de $\omega_0$, $X\approx2M(\omega-\omega_0)$. La transmission $T_E=\dfrac{4Z^2}{4Z^2+X^2}$ tombe à $1/2$ pour $|X|=2Z$, soit $|\omega-\omega_0|=Z/M$.
>
> **Intégrale ou maximum d'une gaussienne dérivée**
>
> $\dfrac{\mathrm d}{\mathrm dt}e^{-t^2/2\sigma^2}=-\dfrac t{\sigma^2}e^{-t^2/2\sigma^2}$ ; $te^{-t^2/2\sigma^2}$ est maximal en $t=\sigma$ et vaut $\sigma e^{-1/2}$.



**q1.** Écrire la condition de continuité sur $y$ en $x=0$ et l'équation du mouvement de la perle de masse $M$.
Justifier le signe des deux forces de tension exercées sur la perle.


> [!tip]- 💡 Coup de pouce
> Dessinez la perle avec la corde (1) à gauche et la corde (2) à droite ; chaque corde tire la perle le long de sa propre direction, avec une composante verticale $\pm F\sin\theta\approx\pm F\,\partial_xy$.




> [!success]- ✅ Correction
> $y_1(0,t)=y_2(0,t)$ ; $M\,\partial_t^2y(0,t)=F\big(\partial_xy_2-\partial_xy_1\big)_{x=0}$.




> [!example]- 📝 Solution détaillée
> **Continuité du déplacement**
>
> La perle est solidaire des deux cordes : $y_1(0,t)=y_2(0,t)\equiv y(0,t)$, ce qui en notation complexe donne $1+r=t$.
>
> **Bilan des forces transverses**
>
> La corde (2), à droite, tire la perle vers elle ; sa tension fait l'angle $\theta_2$ avec l'horizontale, d'où la composante transverse $+F\sin\theta_2\approx+F\,\partial_xy_2(0^+)$. La corde (1), à gauche, tire la perle vers la gauche : la composante transverse est $-F\sin\theta_1\approx-F\,\partial_xy_1(0^-)$. La deuxième loi de Newton donne
> $$M\frac{\partial^2y}{\partial t^2}(0,t)=F\left[\frac{\partial y_2}{\partial x}-\frac{\partial y_1}{\partial x}\right]_{x=0}.$$
> Pour $M=0$, on retrouve la continuité de la pente de l'exercice 1.



**q2.** En déduire $r$ et $t$ en fonction de $Z_1$, $Z_2$, $M$ et $\omega$.
Vérifier qu'on retrouve l'exercice 1 pour $M=0$.


> [!tip]- 💡 Coup de pouce
> Utilisez $1+r=t$, puis $F\,k_i=\omega Z_i$ pour remplacer les nombres d'onde par des impédances.




> [!success]- ✅ Correction
> $r=\dfrac{Z_1-Z_2-iM\omega}{Z_1+Z_2+iM\omega}$, $t=1+r=\dfrac{2Z_1}{Z_1+Z_2+iM\omega}$.




> [!example]- 📝 Solution détaillée
> **Dérivation des deux champs en $x=0$**
>
> $\partial_xy_1(0)=-ik_1A(1-r)$ et $\partial_xy_2(0)=-ik_2\,t\,A=-ik_2(1+r)A$, d'où
> $$\left[\partial_xy_2-\partial_xy_1\right]_0=-iA\big[(k_2-k_1)+r(k_1+k_2)\big],\qquad M\partial_t^2y(0,t)=-M\omega^2(1+r)A\,e^{i\omega t}.$$
>
> **Résolution**
>
> En reportant et en utilisant $Fk_i=\omega Z_i$ :
> $$-M\omega^2(1+r)=-i\omega\big[(Z_2-Z_1)+r(Z_1+Z_2)\big]\ \Longrightarrow\ -iM\omega(1+r)=(Z_2-Z_1)+r(Z_1+Z_2),$$
> soit
> $$\boxed{r=\frac{Z_1-Z_2-iM\omega}{Z_1+Z_2+iM\omega}},\qquad\boxed{t=1+r=\frac{2Z_1}{Z_1+Z_2+iM\omega}}.$$
> Pour $M=0$ : $r=\dfrac{Z_1-Z_2}{Z_1+Z_2}$ et $t=\dfrac{2Z_1}{Z_1+Z_2}$, résultats de l'exercice 1 (réels, indépendants de $\omega$).



**q3.** Montrer que la perle se comporte comme une impédance $Z_M=iM\omega$ placée en série avec la corde (2).
Quel est l'analogue électrique ? Pourquoi les nombres $r$ et $t$ sont-ils maintenant complexes ?


> [!tip]- 💡 Coup de pouce
> Comparez avec $r=(Z_1-Z_2')/(Z_1+Z_2')$ en posant $Z_2'=Z_2+iM\omega$.




> [!example]- 📝 Solution détaillée
> **Impédance équivalente**
>
> Les expressions de la question 2 sont celles de l'exercice 1 avec $Z_2\to Z_2'=Z_2+iM\omega$ : vu de la corde (1), le « reste de la ligne » a pour impédance la somme $Z_2+iM\omega$, comme un circuit où la vitesse transverse (commune aux deux cordes et à la perle) joue le rôle du courant et la force celui de la tension. La perle est l'analogue d'une **inductance** $L=M$ en série dans une ligne de transmission.
>
> **Pourquoi des coefficients complexes**
>
> La partie imaginaire de $Z_M$ traduit un stockage d'énergie cinétique (la perle) et non une dissipation. Elle introduit un déphasage entre force et vitesse, et donc entre l'onde incidente d'une part, l'onde réfléchie et l'onde transmise d'autre part. Le module de $r$ et de $t$ dépend de $\omega$ : la jonction est un filtre.



**q4.** La puissance moyenne transportée par une onde progressive est $\langle\mathcal P\rangle=\tfrac12Z\omega^2|A|^2$.
Établir les coefficients énergétiques $R_E=|r|^2$ et $T_E=(Z_2/Z_1)|t|^2$ et montrer que $R_E+T_E=1$.


> [!success]- ✅ Correction
> $T_E=\dfrac{4Z_1Z_2}{(Z_1+Z_2)^2+M^2\omega^2}$ ; $R_E+T_E=1$ : pas de dissipation, la perle stocke puis restitue l'énergie.




> [!example]- 📝 Solution détaillée
> **Coefficients énergétiques**
>
> Les puissances incidente, réfléchie et transmise valent $\tfrac12Z_1\omega^2A^2$, $\tfrac12Z_1\omega^2|r|^2A^2$ et $\tfrac12Z_2\omega^2|t|^2A^2$. D'où
> $$R_E=|r|^2=\frac{(Z_1-Z_2)^2+M^2\omega^2}{(Z_1+Z_2)^2+M^2\omega^2},\qquad T_E=\frac{Z_2}{Z_1}|t|^2=\frac{4Z_1Z_2}{(Z_1+Z_2)^2+M^2\omega^2}.$$
>
> **Conservation de l'énergie**
>
> $$R_E+T_E=\frac{(Z_1-Z_2)^2+4Z_1Z_2+M^2\omega^2}{(Z_1+Z_2)^2+M^2\omega^2}=1.$$
> Aucune puissance n'est dissipée en moyenne : l'énergie cinétique de la perle oscille mais sa valeur moyenne est constante en régime sinusoïdal établi. Cette vérification confirme les signes de la question 1.



**q5.** Cordes identiques ($Z_1=Z_2=Z$). Calculer $Z$, montrer que $T_E=\big[1+(M\omega/2Z)^2\big]^{-1}$,
identifier le type de filtre et sa fréquence de coupure à $-3$ dB. Calculer $T_E$ à $25$, $100$ et $400$ Hz
et l'atténuation à haute fréquence en dB par octave.


> [!tip]- 💡 Coup de pouce
> $Z=\sqrt{F\mu}$ avec $\mu$ en kg/m. La coupure est atteinte quand $T_E=1/2$.




> [!success]- ✅ Correction
> $Z=0{,}63$ kg/s ; passe-bas, $f_c=Z/(\pi M)\approx100$ Hz ; $T_E\approx0{,}94$ ; $0{,}50$ ; $0{,}06$ ; $-6$ dB par octave.




> [!example]- 📝 Solution détaillée
> **Impédance et filtre passe-bas**
>
> $Z=\sqrt{100\times4{,}0\times10^{-3}}=\sqrt{0{,}40}\approx0{,}632~\text{kg}\cdot\text{s}^{-1}$ (c'est aussi des N$\cdot$s$\cdot$m$^{-1}$). Avec $Z_1=Z_2=Z$ :
> $$T_E=\frac{4Z^2}{4Z^2+M^2\omega^2}=\frac1{1+(M\omega/2Z)^2}.$$
> $T_E$ décroît de $1$ (basse fréquence) vers $0$ (haute fréquence) : c'est un **filtre passe-bas**. La coupure à $-3$ dB ($T_E=1/2$) est en $\omega_c=2Z/M=632~\text{rad}\cdot\text{s}^{-1}$, soit
> $$f_c=\frac{\omega_c}{2\pi}=\frac{Z}{\pi M}\approx100~\text{Hz}.$$
>
> **Application numérique à trois fréquences**
>
> Avec $M\omega/2Z=f/f_c\times1{,}00$ (puisque $f_c\approx100$ Hz), on obtient :
> $$f=25~\text{Hz}:\ T_E\approx0{,}94\ (-0{,}26~\text{dB});\qquad f=100~\text{Hz}:\ T_E\approx0{,}50\ (-3~\text{dB});\qquad f=400~\text{Hz}:\ T_E\approx0{,}06\ (-12~\text{dB}).$$
> Pour $f\gg f_c$, $T_E\approx(f_c/f)^2$ : l'atténuation augmente de $20\log_{10}2\approx6$ dB à chaque doublement de la fréquence (**$-6$ dB par octave**), comme pour la loi de masse d'une paroi (TD2, exercice 8).



**q6.** Régime transitoire. Montrer que, pour une impulsion dont le spectre est contenu dans $\omega\ll\omega_c$, l'onde
transmise est l'onde incidente retardée d'un temps $\tau=M/(2Z)$ et que l'onde réfléchie vaut
$y_r(0,t)\approx-\tau\,\partial_ty_i(0,t)$. Calculer $\tau$ et l'amplitude maximale de l'écho pour une impulsion
gaussienne $y_i(0,t)=Ae^{-t^2/2\sigma^2}$ avec $\sigma=20$ ms. Quelle est l'allure de l'écho ?


> [!tip]- 💡 Coup de pouce
> Développez $t(\omega)=1/(1+i\omega\tau)$ et $r(\omega)=-i\omega\tau/(1+i\omega\tau)$ au premier ordre en $\omega\tau$, puis revenez dans le domaine temporel ($i\omega\leftrightarrow\partial_t$).




> [!success]- ✅ Correction
> $\tau=M/(2Z)\approx1{,}6$ ms ; écho bipolaire d'amplitude maximale $\approx0{,}05\,A$ (soit $5\ \%$ de l'incident).




> [!example]- 📝 Solution détaillée
> **Développement à basse fréquence**
>
> Pour $Z_1=Z_2=Z$ et $\tau=M/(2Z)=1/\omega_c$ :
> $$t(\omega)=\frac1{1+i\omega\tau}\approx1-i\omega\tau\approx e^{-i\omega\tau},\qquad r(\omega)=\frac{-i\omega\tau}{1+i\omega\tau}\approx-i\omega\tau.$$
> Dans le domaine temporel, la multiplication par $e^{-i\omega\tau}$ est un retard : $y_t(0,t)\approx y_i(0,t-\tau)$. La multiplication par $-i\omega\tau$ est une dérivation : $y_r(0,t)\approx-\tau\,\partial_ty_i(0,t)$.
>
> **Application numérique**
>
> $\tau=M/(2Z)=2{,}0\times10^{-3}/1{,}265\approx1{,}6$ ms : l'impulsion transmise est retardée de $1{,}6$ ms (pour $\sigma=20$ ms, la condition $\omega\tau\ll1$ est excellente). L'écho est
> $$y_r(0,t)=\tau\frac{t}{\sigma^2}Ae^{-t^2/2\sigma^2},$$
> *bipolaire* (antisymétrique en $t$ : un pic positif puis un pic négatif), d'amplitude maximale en $t=\pm\sigma$ égale à $\dfrac\tau\sigma e^{-1/2}A=\dfrac{1{,}6}{20}\times0{,}61\,A\approx0{,}05\,A$. Une impulsion large ne voit donc la perle que comme un léger retard et un petit écho dérivé.



**q7.** La perle est maintenant reliée à un support fixe par un ressort de raideur $K$ (rappel transversal $-Ky(0,t)$).
Montrer que $r=\dfrac{Z_1-Z_2-iX}{Z_1+Z_2+iX}$ avec $X=M\omega-K/\omega$. Pour des cordes identiques, à quelle
fréquence la transmission est-elle totale ? Calculer $K$ pour $f_0=250$ Hz, la largeur à mi-puissance
et le facteur de qualité de ce passe-bande.


> [!tip]- 💡 Coup de pouce
> L'équation de la perle devient $M\ddot y=F(\partial_xy_2-\partial_xy_1)-Ky$. Comparez à la question 2 en remplaçant $M\omega^2$ par $M\omega^2-K$.




> [!success]- ✅ Correction
> $T_E=\dfrac{4Z^2}{4Z^2+X^2}=1$ en $\omega_0=\sqrt{K/M}$ ; $K\approx4{,}9\times10^3$ N/m ; $\Delta f\approx100$ Hz ; $Q\approx2{,}5$.




> [!example]- 📝 Solution détaillée
> **Nouvelle équation et réactance**
>
> $-M\omega^2(1+r)A=F[\ldots]-K(1+r)A$ avec $F[\ldots]=-i\omega A\big[(Z_2-Z_1)+r(Z_1+Z_2)\big]$, soit
> $$-i\left(M\omega-\frac K\omega\right)(1+r)=(Z_2-Z_1)+r(Z_1+Z_2)\ \Longrightarrow\ \boxed{r=\frac{Z_1-Z_2-iX}{Z_1+Z_2+iX}},\quad X=M\omega-\frac K\omega.$$
> Le ressort est une impédance série $K/(i\omega)=-iK/\omega$ : analogue d'une capacité en série avec l'inductance de la perle.
>
> **Transparence et sélectivité**
>
> Pour $Z_1=Z_2=Z$, $T_E=\dfrac{4Z^2}{4Z^2+X^2}$ vaut $1$ si $X=0$, soit $\omega_0=\sqrt{K/M}$ : à cette fréquence la perle oscille en phase avec la force du ressort, $Z_{\mathrm{série}}=0$ et la jonction est totalement transparente. Pour $\omega\to0$ le ressort bloque la corde ($r\to-1$) ; pour $\omega\to\infty$, c'est la masse ($r\to-1$) : c'est un **passe-bande**.
>
> **Application numérique**
>
> $\omega_0=2\pi\times250=1571$ rad/s donc $K=M\omega_0^2=2{,}0\times10^{-3}\times2{,}47\times10^6\approx4{,}9\times10^3~\text{N}\cdot\text{m}^{-1}$. Au voisinage de $\omega_0$, $X\approx2M(\omega-\omega_0)$ et $T_E=\tfrac12$ pour $|X|=2Z$, soit $|\omega-\omega_0|=Z/M=316$ rad/s. La largeur à mi-puissance est donc $\Delta\omega=2Z/M=\omega_c=632$ rad/s, soit $\Delta f\approx100$ Hz, et le facteur de qualité $Q=\dfrac{f_0}{\Delta f}\approx\dfrac{250}{100}=2{,}5$. Le filtre est peu sélectif : pour le rendre plus fin, il faut une perle plus lourde (ou des cordes plus légères).




> [!note]- 🔗 Liens avec d'autres disciplines
> **Électrocinétique**
>
> Une inductance série dans une ligne de transmission est un filtre passe-bas ; une inductance et une capacité en série forment un passe-bande, exactement comme ici (force $\leftrightarrow$ tension, vitesse $\leftrightarrow$ courant, masse $\leftrightarrow$ inductance, ressort $\leftrightarrow$ capacité).
>
> **Acoustique du bâtiment**
>
> La loi de masse d'une paroi (TD2, exercice 8) est le même calcul avec une masse surfacique ; la résonance du double vitrage est le montage perle + ressort.
>
> **Instruments à cordes**
>
> Le chevalet, la sourdine (petite masse sur le chevalet de violon), le capodastre et les masses d'accord des guitares ajoutent un élément ponctuel sur la corde : ils filtrent les harmoniques élevés et modifient le timbre.
>
> **Génie civil et sismologie**
>
> Les amortisseurs à masse accordée (une masse montée sur ressort fixée à un bâtiment ou à un pont) sont l'application du montage perle + ressort : en transparence totale à $\omega_0$, on évacue l'énergie vers l'oscillateur au lieu de la réfléchir.
>
> **Physique du solide**
>
> La chaîne de masses reliées par des ressorts, modèle de cristal unidimensionnel, a une fréquence de coupure et des bandes interdites ; la perle isolée en est le défaut ponctuel.




> [!question]- 🔭 Aller plus loin — Licence : Amortisseur : terminaison et absorption
> Un amortisseur visqueux (coefficient $\eta$) fixé en $O$ ajoute en série une impédance réelle $\eta$. On pourra montrer que la fraction d'énergie absorbée est $1-R_E-T_E=\dfrac{4Z_1\eta}{(Z_1+Z_2+\eta)^2}$ pour $\omega$ quelconque, et qu'une corde semi-infinie terminée par $\eta=Z$ n'a aucune réflexion (terminaison adaptée, principe de l'absorbeur d'extrémité d'une corde ou d'une ligne).




> [!question]- 🔭 Aller plus loin — Master : Corde chargée périodiquement : réseau de perles
> Pour des perles de masse $m$ régulièrement espacées d'une distance $a$ sur une corde, on établit la relation de dispersion $\omega=2\sqrt{\dfrac{F}{ma}}\,\left|\sin\dfrac{ka}2\right|$ : le milieu devient dispersif et il existe une fréquence de coupure $\omega_{\max}=2\sqrt{F/(ma)}$ au-delà de laquelle l'onde ne se propage plus (bande interdite). C'est la version mécanique du filtre passe-bas à cellules LC, et le premier modèle de vibration d'un cristal.




> [!question]- 🔭 Aller plus loin — Master : Matrice de transfert d'un élément ponctuel
> Un élément de impédance série $Z_s$ s'écrit sous la forme d'une matrice $\begin{pmatrix}1&Z_s\\0&1\end{pmatrix}$ reliant (force, vitesse) de part et d'autre ; l'association d'éléments en série, de lames et d'interfaces se traite alors par produit de matrices (voir TD2, exercice 8).




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex1-corde-non-homogene-jonction-entre-deux-cordes|Exercice 1 — Corde non homogène, jonction entre deux cordes]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex2-interface-entre-deux-milieux-notion-d-impedance-acoustique|Exercice 2 — Interface entre deux milieux, notion d'impédance acoustique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex4-incidence-oblique-lois-de-snell-descartes-angle-critique-reflexion-totale-et-onde-evanescente|Exercice 4 — Incidence oblique : lois de Snell-Descartes, angle critique, réflexion totale et onde évanescente]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex6-controle-ultrasonore-d-une-plaque-immergee-train-d-echos-epaisseur-attenuation-et-defaut-de-collage|Exercice 6 — Contrôle ultrasonore d'une plaque immergée : train d'échos, épaisseur, atténuation et défaut de collage]]


