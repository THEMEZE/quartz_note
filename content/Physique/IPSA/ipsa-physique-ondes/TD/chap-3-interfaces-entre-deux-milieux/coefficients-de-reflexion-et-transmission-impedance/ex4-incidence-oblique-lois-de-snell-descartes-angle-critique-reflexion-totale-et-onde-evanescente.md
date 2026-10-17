---
title: "Exercice 4 — Incidence oblique : lois de Snell-Descartes, angle critique, réflexion totale et onde évanescente"
tags:
  - td
  - chap-3-interfaces-entre-deux-milieux
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/index|⬅ Retour]] · <a href="/pdfs/td3_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_PhV212_enonce)</a> · <a href="/pdfs/td3_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_enonce)</a> · <a href="/pdfs/td3_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td3_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td3_PhV212_corrige)</a> · <a href="/pdfs/td3_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td3_corrige)</a> · <a href="/pdfs/td3_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 4. Incidence oblique : lois de Snell-Descartes, angle critique, réflexion totale et onde évanescente *(facultatif)*

Deux fluides parfaits semi-infinis sont séparés par le plan $x=0$ : le milieu (1) ($\rho_1,c_1,Z_1=\rho_1c_1$)
occupe $x<0$, le milieu (2) ($\rho_2,c_2,Z_2=\rho_2c_2$) occupe $x>0$. Une onde plane sinusoïdale de pulsation $\omega$
arrive du milieu (1) avec l'angle d'incidence $\theta_1$ par rapport à la normale $Ox$. Elle donne une onde réfléchie
(angle $\theta_1'$) et une onde transmise (angle $\theta_2$). En notation complexe ($e^{i\omega t}$), avec $\mathbf r=(x,y)$ :
$$p_I=A\,e^{i(\omega t-k_1x\cos\theta_1-k_1y\sin\theta_1)},\quad p_R=R\,A\,e^{i(\omega t+k_1x\cos\theta_1'-k_1y\sin\theta_1')},\quad p_T=T\,A\,e^{i(\omega t-k_2x\cos\theta_2-k_2y\sin\theta_2)},$$
avec $k_i=\omega/c_i$. À l'interface, la pression et la composante normale $v_x$ de la vitesse sont continues.
Pour une onde plane se propageant dans la direction $\hat{\mathbf u}$, on rappelle que $\mathbf v=(p/Z)\,\hat{\mathbf u}$.

Données : air ($\rho=1{,}2~\text{kg}\cdot\text{m}^{-3}$, $c=340~\text{m}\cdot\text{s}^{-1}$), eau
($\rho=1000~\text{kg}\cdot\text{m}^{-3}$, $c=1500~\text{m}\cdot\text{s}^{-1}$), sable saturé
($\rho=1900~\text{kg}\cdot\text{m}^{-3}$, $c=1700~\text{m}\cdot\text{s}^{-1}$), vase
($\rho=1400~\text{kg}\cdot\text{m}^{-3}$, $c=1450~\text{m}\cdot\text{s}^{-1}$).

**q1.** En écrivant la continuité de $p$ en $x=0$ pour tout $y$ et tout $t$, retrouver les lois de la réflexion
et de la réfraction de Snell-Descartes. Quelle grandeur physique est conservée à la traversée de l'interface ?

> [!tip]- 💡 Coup de pouce
> En $x=0$, les trois ondes s'écrivent $e^{i\omega t}e^{-ik_1y\sin\theta_1}$, $Re^{i\omega t}e^{-ik_1y\sin\theta_1'}$ et $Te^{i\omega t}e^{-ik_2y\sin\theta_2}$ : une somme d'exponentielles de $y$ ne peut être égale à une autre que si les dépendances en $y$ coïncident.


> [!success]- ✅ Correction
> $\theta_1'=\theta_1$ ; $k_1\sin\theta_1=k_2\sin\theta_2$, soit $\sin\theta_1/c_1=\sin\theta_2/c_2$ ; la composante tangentielle $k_y$ du vecteur d'onde est conservée.


> [!example]- 📝 Solution détaillée
> **Conservation de $k_y$**
>
> En $x=0$ : $A\,e^{-ik_1y\sin\theta_1}+RA\,e^{-ik_1y\sin\theta_1'}=TA\,e^{-ik_2y\sin\theta_2}$ pour tout $y$ (et la pulsation $\omega$ est commune). Trois fonctions exponentielles de $y$ ne peuvent satisfaire cette relation que si leurs exposants sont égaux :
> $$k_1\sin\theta_1=k_1\sin\theta_1'=k_2\sin\theta_2\ \Longrightarrow\ \theta_1'=\theta_1,\qquad\frac{\omega}{c_1}\sin\theta_1=\frac\omega{c_2}\sin\theta_2.$$
> La grandeur conservée est la composante $k_y$ du vecteur d'onde parallèle à l'interface (équivalente à la conservation de la longueur d'onde apparente $\lambda_y=2\pi/k_y$ le long de l'interface). Les lois de Snell-Descartes en sont la conséquence directe, sans aucune hypothèse géométrique supplémentaire.


**q2.** Écrire la continuité de la pression et de la composante normale de la vitesse en $x=0$ et en déduire
$R(\theta_1)$ et $T(\theta_1)$. Montrer que tout se passe comme en incidence normale avec des impédances apparentes.
Vérifier le cas $\theta_1=0$.

> [!tip]- 💡 Coup de pouce
> $v_x=(p/Z)\cos\theta$ pour l'onde incidente et pour l'onde transmise, mais $v_x=-(p/Z)\cos\theta_1$ pour l'onde réfléchie (elle se propage vers $-x$).


> [!success]- ✅ Correction
> $R=\dfrac{Z_2\cos\theta_1-Z_1\cos\theta_2}{Z_2\cos\theta_1+Z_1\cos\theta_2}$ ; $T=1+R=\dfrac{2Z_2\cos\theta_1}{Z_2\cos\theta_1+Z_1\cos\theta_2}$.


> [!example]- 📝 Solution détaillée
> **Système de raccord**
>
> $$1+R=T\quad(p),\qquad\frac{\cos\theta_1}{Z_1}(1-R)=\frac{\cos\theta_2}{Z_2}\,T\quad(v_x).$$
> En remplaçant $T$ : $Z_2\cos\theta_1(1-R)=Z_1\cos\theta_2(1+R)$, d'où
> $$\boxed{R=\frac{Z_2\cos\theta_1-Z_1\cos\theta_2}{Z_2\cos\theta_1+Z_1\cos\theta_2}},\qquad\boxed{T=1+R=\frac{2Z_2\cos\theta_1}{Z_2\cos\theta_1+Z_1\cos\theta_2}}.$$
>
> **Impédance apparente et incidence normale**
>
> Avec $Z_i^{\mathrm{app}}=Z_i/\cos\theta_i$ : $R=\dfrac{Z_2^{\mathrm{app}}-Z_1^{\mathrm{app}}}{Z_2^{\mathrm{app}}+Z_1^{\mathrm{app}}}$, c'est exactement la formule de l'incidence normale. Pour $\theta_1=0$, $\theta_2=0$ et on retrouve $R=\dfrac{Z_2-Z_1}{Z_1+Z_2}$, $T=\dfrac{2Z_2}{Z_1+Z_2}$ (TD2, exercice 4).


**q3.** Le flux d'énergie normal à l'interface d'une onde plane est $I_x=\langle p\,v_x\rangle$. Établir
$R_E=|R|^2$ et $T_E=|T|^2\dfrac{Z_1\cos\theta_2}{Z_2\cos\theta_1}$ (quand $\theta_2$ est réel) et montrer que $R_E+T_E=1$.

> [!tip]- 💡 Coup de pouce
> Posez $a=Z_2\cos\theta_1$ et $b=Z_1\cos\theta_2$ ; alors $R=\dfrac{a-b}{a+b}$, $T=\dfrac{2a}{a+b}$.


> [!example]- 📝 Solution détaillée
> **Coefficients énergétiques**
>
> Pour une onde plane, $\langle p\,v_x\rangle=\dfrac{|p|^2\cos\theta}{2Z}$ (en valeur absolue). D'où $R_E=|R|^2$ et
> $$T_E=\frac{|T|^2\cos\theta_2/Z_2}{\cos\theta_1/Z_1}=|T|^2\frac{Z_1\cos\theta_2}{Z_2\cos\theta_1}=\frac{4a^2}{(a+b)^2}\cdot\frac ba=\frac{4ab}{(a+b)^2}.$$
> (car $b/a=Z_1\cos\theta_2/(Z_2\cos\theta_1)$). En additionnant à $R_E=\dfrac{(a-b)^2}{(a+b)^2}$ :
> $$R_E+T_E=\frac{(a-b)^2+4ab}{(a+b)^2}=1.$$
> La conservation de l'énergie est ainsi vérifiée avec le bon facteur $\cos\theta/Z$ du flux normal.


**q4.** Existe-t-il un angle critique pour le passage air $\to$ eau ? eau $\to$ air ? eau $\to$ sable ? Calculer-le quand il existe.
Pour un son qui sort de l'eau, dans quel cône émerge-t-il dans l'air ? Quelle fraction de l'espace
(demi-sphère) de l'air est concernée pour l'entrée dans l'eau ?

> [!tip]- 💡 Coup de pouce
> $\sin\theta_2=(c_2/c_1)\sin\theta_1\leq1$ impose $\sin\theta_1\le c_1/c_2$ : il faut $c_2>c_1$. La fraction de demi-sphère contenue dans un cône d'angle $\theta_c$ est $1-\cos\theta_c$.


> [!success]- ✅ Correction
> Air $\to$ eau : $\theta_c=13{,}1^\circ$ ; eau $\to$ air : aucun ; eau $\to$ sable : $\theta_c=61{,}9^\circ$ ; cône d'émergence de $13{,}1^\circ$ ; fraction $\approx2{,}6\ \%$.


> [!example]- 📝 Solution détaillée
> **Existence de l'angle critique**
>
> L'angle critique existe si $c_2>c_1$ (le rayon transmis s'écarte de la normale et atteint $90^\circ$ avant que $\theta_1$ ne le fasse).
>
>
> - Air $\to$ eau ($340\to1500$) : $\sin\theta_c=340/1500=0{,}227$, $\theta_c=13{,}1^\circ$.
> - Eau $\to$ air ($c_2<c_1$) : *pas d'angle critique*. $\sin\theta_2=0{,}227\sin\theta_1\le0{,}227$, donc le rayon émerge toujours dans le cône $\theta_2\le13{,}1^\circ$ autour de la verticale, quelle que soit la direction d'émission sous l'eau.
> - Eau $\to$ sable ($1500\to1700$) : $\sin\theta_c=1500/1700=0{,}882$, $\theta_c=61{,}9^\circ$.
>
> **Interprétation**
>
> Pour l'entrée dans l'eau depuis une source aérienne, seule la fraction $1-\cos13{,}1^\circ=1-0{,}974\approx2{,}6\ \%$ de la demi-sphère des directions d'incidence conduit à une transmission : toutes les autres sont totalement réfléchies. S'ajoute à cela le désaccord d'impédance (exercice 2) : un plongeur entend très mal les sons aériens, sauf ceux qui arrivent à peu près de la verticale.


**q5.** Eau $\to$ sable, avec $\theta_1>\theta_c$. Montrer que $\cos\theta_2$ est imaginaire pur, que $|R|=1$, et exprimer
la phase $\varphi$ de $R$. Montrer que l'onde dans le sable est évanescente, calculer sa profondeur de pénétration
$\delta$ puis que sa puissance moyenne normale est nulle. Applications numériques pour $\theta_1=75^\circ$ et $f=1$ kHz.

> [!tip]- 💡 Coup de pouce
> Posez $n=c_2/c_1$ ; $\cos^2\theta_2=1-n^2\sin^2\theta_1<0$. On choisit $\cos\theta_2=-i\beta$ ($\beta>0$) pour que l'onde décroisse avec $x$.


> [!success]- ✅ Correction
> $\beta=0{,}445$ ; $|R|=1$, $\varphi\approx77^\circ$ ; $\kappa=1{,}6$ rad/m, $\delta\approx0{,}6$ m ; $\langle p\,v_x\rangle=0$.


> [!example]- 📝 Solution détaillée
> **Angle imaginaire et réflexion totale**
>
> $\cos^2\theta_2=1-n^2\sin^2\theta_1<0$ ; on pose $\cos\theta_2=-i\beta$ avec $\beta=\sqrt{n^2\sin^2\theta_1-1}>0$. Alors
> $$R=\frac{Z_2\cos\theta_1+iZ_1\beta}{Z_2\cos\theta_1-iZ_1\beta}\ \Rightarrow\ |R|=1,\qquad R=e^{i\varphi},\ \ \varphi=2\arctan\frac{Z_1\beta}{Z_2\cos\theta_1}.$$
> $\varphi$ passe de $0$ en $\theta_c$ à $\pi$ en incidence rasante.
>
> **Application numérique**
>
> $n=1700/1500=1{,}133$, $n\sin75^\circ=1{,}095$, $\beta=\sqrt{1{,}198-1}=0{,}445$. $Z_1=1{,}5\times10^6$ et $Z_2=1900\times1700=3{,}23\times10^6$ rayl : $\dfrac{Z_1\beta}{Z_2\cos\theta_1}=\dfrac{1{,}5\times0{,}445}{3{,}23\times0{,}259}\approx0{,}80$, d'où $\varphi=2\arctan(0{,}80)\approx77^\circ$.
>
> **Onde évanescente**
>
> $p_T\propto e^{-ik_2x\cos\theta_2}=e^{-\kappa x}$ avec $\kappa=k_2\beta=k_1\sqrt{\sin^2\theta_1-\sin^2\theta_c}$ : l'onde décroît exponentiellement dans le sable tout en se propageant le long de l'interface, avec la vitesse de phase $c_1/\sin\theta_1<c_2$. À $1$ kHz, $\lambda_1=1{,}5$ m, $k_1=4{,}19$ rad/m, $\kappa=4{,}19\times\sqrt{0{,}933-0{,}779}=1{,}65$ rad/m et $\delta=1/\kappa\approx0{,}6$ m $\approx0{,}4\lambda_1$.
>
> **Flux moyen nul**
>
> L'équation d'Euler donne $i\omega\rho_2v_x=-\partial_xp_T=\kappa p_T$, soit $v_x=-i\kappa p_T/(\omega\rho_2)$ : $p_T$ et $v_x$ sont en quadrature et $\langle p_Tv_x\rangle=\tfrac12\operatorname{Re}(p_Tv_x^{*})=0$. L'onde évanescente est pilotée par l'interface mais ne transporte aucune énergie vers l'intérieur du sable ; toute la puissance incidente est renvoyée, cohérent avec $|R|=1$.


**q6.** Interface air $\to$ eau. Calculer $T_E$ en incidence normale puis pour $\theta_1=10^\circ$. Commenter
(comparer à l'exercice 2 du TD3 et au cône de la question 4).

> [!tip]- 💡 Coup de pouce
> $Z_1=1{,}2\times340=408$ rayl, $Z_2=1{,}5\times10^6$ rayl ; $T_E=4ab/(a+b)^2$ avec $a=Z_2\cos\theta_1$ et $b=Z_1\cos\theta_2$.


> [!success]- ✅ Correction
> $T_E(0^\circ)=1{,}09\times10^{-3}$ ; $T_E(10^\circ)=7{,}1\times10^{-4}$.


> [!example]- 📝 Solution détaillée
> **Incidence normale**
>
> $T_E(0)=\dfrac{4Z_1Z_2}{(Z_1+Z_2)^2}=\dfrac{4\times408\times1{,}5\times10^6}{(1{,}5004\times10^6)^2}=1{,}09\times10^{-3}$ (soit $0{,}11\ \%$ : l'énergie qui passe de l'air à l'eau).
>
> **À $10^\circ$**
>
> $\sin\theta_2=\dfrac{1500}{340}\sin10^\circ=0{,}766$, $\cos\theta_2=0{,}643$, $\cos\theta_1=0{,}985$. $a=1{,}477\times10^6$, $b=408\times0{,}643=262$ : $T_E=\dfrac{4ab}{(a+b)^2}=7{,}1\times10^{-4}$.
> La transmission décroît quand l'incidence augmente et s'annule à $\theta_c=13{,}1^\circ$ ($\cos\theta_2=0$, donc $b=0$ et $T_E=0$). Le son qui descend de l'air vers l'eau passe donc très mal, et seulement dans un cône étroit.


**q7.** *Angle d'intromission.* Montrer que $R=0$ pour un angle $\theta_B$ tel que
$\sin^2\theta_B=\dfrac{Z_2^2-Z_1^2}{Z_2^2-n^2Z_1^2}$ ($n=c_2/c_1$). Pour quelles combinaisons
$(\rho_2/\rho_1,\ c_2/c_1)$ cet angle existe-t-il ? L'angle existe-t-il pour l'interface air $\to$ eau ? Calculer $\theta_B$ pour
l'interface eau $\to$ vase et vérifier numériquement que $R=0$.

> [!tip]- 💡 Coup de pouce
> $R=0\Leftrightarrow Z_2\cos\theta_1=Z_1\cos\theta_2$. Élevez au carré et utilisez $\cos^2\theta_2=1-n^2\sin^2\theta_1$. Notez que $Z_2^2-n^2Z_1^2=c_2^2(\rho_2^2-\rho_1^2)$.


> [!success]- ✅ Correction
> $\theta_B\approx74^\circ$ (eau $\to$ vase) ; il faut $\rho_2>\rho_1$ et $c_2<c_1$ (ou l'inverse avec $Z_2<Z_1$) ; pas d'angle de Brewster pour air $\to$ eau.


> [!example]- 📝 Solution détaillée
> **Calcul de $\theta_B$**
>
> $Z_2\cos\theta_1=Z_1\cos\theta_2\ \Longrightarrow\ Z_2^2(1-s^2)=Z_1^2(1-n^2s^2)$ avec $s=\sin\theta_1$, d'où $s^2(Z_1^2n^2-Z_2^2)=Z_1^2-Z_2^2$ et
> $$\sin^2\theta_B=\frac{Z_2^2-Z_1^2}{Z_2^2-n^2Z_1^2}=\frac{\rho_2^2c_2^2-\rho_1^2c_1^2}{c_2^2(\rho_2^2-\rho_1^2)}.$$
>
> **Existence**
>
> Il faut $0\le\sin^2\theta_B\le1$. Pour $\rho_2>\rho_1$, la condition $\sin^2\theta_B\le1$ équivaut à $c_2\le c_1$ (milieu 2 plus dense *et plus lent*) ; la condition symétrique est $\rho_2<\rho_1$, $c_2>c_1$ et $Z_2<Z_1$. Pour l'interface air $\to$ eau ($\rho_2>\rho_1$ mais $c_2>c_1$), $\sin^2\theta_B>1$ : il n'y a pas d'angle d'intromission.
>
> **Eau $\to$ vase**
>
> $Z_1=1{,}5\times10^6$, $Z_2=1400\times1450=2{,}03\times10^6$, $n=0{,}967$ :
> $$\sin^2\theta_B=\frac{4{,}12-2{,}25}{4{,}12-2{,}10}=\frac{1{,}871}{2{,}018}=0{,}927\ \Rightarrow\ \theta_B\approx74^\circ.$$
> Vérification : $\cos\theta_1=0{,}270$, $\sin\theta_2=0{,}967\times0{,}963=0{,}931$, $\cos\theta_2=0{,}366$ ; $a=Z_2\cos\theta_1=5{,}49\times10^5$ et $b=Z_1\cos\theta_2=5{,}49\times10^5$ : $a=b$ donc $R=0$ et la transmission est totale à cet angle, bien que l'impédance soit différente. C'est l'analogue acoustique de l'angle de Brewster.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex2-interface-entre-deux-milieux-notion-d-impedance-acoustique|Exercice 2 — Interface entre deux milieux, notion d'impédance acoustique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex5-sismique-refraction-ondes-coniques-et-epaisseur-d-une-couche|Exercice 5 — Sismique réfraction : ondes coniques et épaisseur d'une couche]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex6-controle-ultrasonore-d-une-plaque-immergee-train-d-echos-epaisseur-attenuation-et-defaut-de-collage|Exercice 6 — Contrôle ultrasonore d'une plaque immergée : train d'échos, épaisseur, atténuation et défaut de collage]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex3-perle-sur-une-corde-jonction-massive-filtre-passe-bas-puis-passe-bande|Exercice 3 — Perle sur une corde : jonction massive, filtre passe-bas puis passe-bande]]

