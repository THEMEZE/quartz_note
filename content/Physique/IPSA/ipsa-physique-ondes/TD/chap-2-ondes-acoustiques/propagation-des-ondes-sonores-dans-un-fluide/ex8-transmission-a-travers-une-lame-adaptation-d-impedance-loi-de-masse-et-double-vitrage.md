---
title: "Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/index|⬅ Retour]] · <a href="/pdfs/td2_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_PhV212_enonce)</a> · <a href="/pdfs/td2_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_enonce)</a> · <a href="/pdfs/td2_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_aides)</a> · <a href="/pdfs/td2_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td2_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_PhV212_corrige)</a> · <a href="/pdfs/td2_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_corrige)</a>

### Exercice 8. Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage *(facultatif)*

*Difficulté ●●●●● · ⏱ 60 min · Type : Problème de synthèse / Approfondissement*

On étudie la transmission d'une onde plane, en incidence normale, à travers une *lame* d'épaisseur $e$
insérée entre deux fluides semi-infinis. Le fluide (1), d'impédance $Z_1=\rho_1c_1$, occupe $x<0$ ; la lame
(2), de masse volumique $\rho_2$, de célérité $c_2$, d'impédance $Z_2=\rho_2c_2$ et de nombre d'onde
$k_2=\omega/c_2$, occupe $0<x<e$ ; le fluide (3), d'impédance $Z_3$, occupe $x>e$. On pose $u=k_2e$.
Il n'y a pas d'onde incidente venant de la droite. En notation complexe $e^{i\omega t}$ :
$$\tilde p_1=A\big(e^{-ik_1x}+Re^{ik_1x}\big),\quad\tilde p_2=Be^{-ik_2x}+Ce^{ik_2x},\quad\tilde p_3=D\,e^{-ik_3(x-e)}.$$
Les vitesses particulaires s'en déduisent par $\tilde v=\pm\tilde p/Z$ selon le sens de propagation ($+$ pour $x$
croissant). On note $R_I=|R|^2$ et $T_I$ les coefficients énergétiques ($R_I+T_I=1$, milieux non absorbants).

> [!question]+ 🎣 Accroche
> **Pourquoi une vitre mince arrête-t-elle les sons graves moins bien que les aigus ?**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *Un mur de $20$ cm de béton arrête presque tout, une vitre de $4$ mm laisse passer la musique des voisins surtout dans les graves. Et l'échographe ? Il nécessite un gel, mais aussi, dans la sonde, une fine couche intermédiaire de matériau particulier. **Une couche très fine peut-elle changer la transmission ?***
>
> **Idée clé : une lame se comporte comme un milieu «~équivalent~» d'impédance $Z_{\mathrm{in}}$ qui dépend de son épaisseur en longueurs d'onde.** Épaisseur $\lambda_2/2$ : invisible. Épaisseur $\lambda_2/4$ avec $Z_2=\sqrt{Z_1Z_3}$ : réflexion annulée. Épaisseur $\ll\lambda_2$ et dense : elle se comporte comme une masse $m_s=\rho_2e$ par unité de surface, ce qui réduit la transmission d'autant plus que la fréquence est élevée.


> [!abstract]+ 📚 Prérequis
> **Coefficients de réflexion et de transmission à une interface**
>
> Connaître la continuité de la pression et de la vitesse normale à une interface, la relation $\tilde p=\pm Z\tilde v$, et le résultat $R=(Z_2-Z_1)/(Z_1+Z_2)$ de l'exercice 4. Savoir que la transmission d'énergie est $T_I=4Z_1Z_2/(Z_1+Z_2)^2$.
>
> **Ondes stationnaires dans un tube (exercices 2 et 3) et notion d'impédance d'une extrémité**
>
> Savoir que le rapport $\tilde p/\tilde v$ en un point donné définit une impédance, et que l'impédance «~vue~» en $x=0$ dépend de ce qui se trouve derrière.
>
> **Trigonométrie et nombres complexes**
>
> $e^{iu}\pm e^{-iu}$, $\cos^2u+\sin^2u=1$, $|a+ib|^2=a^2+b^2$.


> [!info]+ 🎯 Objectifs
> **Savoir traiter un empilement de milieux par la notion d'impédance ramenée**
>
> Savoir établir l'impédance «~ramenée~» en $x=0$ d'une lame suivie d'un milieu semi-infini, en déduire $R$ et $T_I$, puis dégager deux cas remarquables : la lame demi-onde (transparente) et la lame quart d'onde (adaptatrice).
>
> Savoir appliquer ces résultats à deux problèmes d'ingénieur : adaptation d'une sonde échographique et isolation phonique d'une paroi (loi de masse, double vitrage).


> [!note]+ 📖 Point de cours
> **Impédance ramenée**
>
> Pour des ondes planes en incidence normale, le rapport $Z(x)=\tilde p(x)/\tilde v(x)$ est continu à travers toute interface. Un milieu semi-infini de même impédance $Z_3$ à droite impose $Z(x)=Z_3$ pour $x>e$. En se déplaçant à travers la lame, $Z(x)$ varie : l'impédance «~ramenée~» en $x=0$,
> $$Z_{\mathrm{in}}=Z_2\,\frac{Z_3\cos u+iZ_2\sin u}{Z_2\cos u+iZ_3\sin u},\qquad u=k_2e,$$
> joue le rôle d'une impédance de milieu semi-infini équivalent : la réflexion au niveau de $x=0$ est alors donnée par la formule de l'exercice 4 avec $Z_2\to Z_{\mathrm{in}}$. Le résultat périodique en $u$ (période $\pi$, soit $e=\lambda_2/2$) traduit les interférences entre les ondes qui font des allers-retours dans la lame.


> [!note]- 🧮 Outils mathématiques
> **Mise en facteur d'exponentielles complexes**
>
> $\dfrac{(Z_3+Z_2)e^{iu}+(Z_3-Z_2)e^{-iu}}{(Z_3+Z_2)e^{iu}-(Z_3-Z_2)e^{-iu}}=\dfrac{Z_3\cos u+iZ_2\sin u}{Z_2\cos u+iZ_3\sin u}$ en utilisant $e^{iu}\pm e^{-iu}$.
>
> **Module d'un complexe $a+ib$ avec $a,b$ réels**
>
> $|a+ib|^2=a^2+b^2$. Dans $R=\dfrac{Z_{\mathrm{in}}-Z_1}{Z_{\mathrm{in}}+Z_1}$, après mise au même dénominateur, les parties réelle et imaginaire apparaissent simplement (en $\cos u$ et $\sin u$).
>
> **Racines carrées et moyenne géométrique**
>
> La condition d'adaptation $Z_2=\sqrt{Z_1Z_3}$ est la moyenne géométrique des impédances : $\sqrt{30\times1{,}5}=6{,}7$ (en MRayl).
>
> **Développements limités pour $u\ll1$**
>
> $\cos u\approx1$, $\sin u\approx u$ : l'expression de $T_I$ se simplifie en $\big[1+(Z_2u/2Z_0)^2\big]^{-1}$ quand $Z_1=Z_3=Z_0\ll Z_2$.
>
> **Décibels et octaves**
>
> Doubler $\omega$ (ou $m_s$) dans $20\log_{10}(\omega m_s/2Z_0)$ ajoute $20\log_{10}2\approx6$ dB. Multiplier par $10^{n}$ ajoute $20n$ dB.
>
> **Pulsation d'un système à deux masses**
>
> Pour deux masses $m_1$, $m_2$ reliées par un ressort $K$, la coordonnée relative $\eta=\xi_1-\xi_2$ obéit à $\ddot\eta+K(1/m_1+1/m_2)\eta=0$ : la pulsation est $\sqrt{K/m_{\mathrm{red}}}$ avec $1/m_{\mathrm{red}}=1/m_1+1/m_2$.


**q1.** Écrire les vitesses particulaires dans chaque région, puis les quatre équations de continuité de
$\tilde p$ et $\tilde v$ en $x=0$ et $x=e$. Pourquoi $\tilde p_3$ ne comporte-t-il qu'une onde progressive ?

> [!tip]- 💡 Coup de pouce
> Une onde se propageant vers les $x$ décroissants a $\tilde v=-\tilde p/Z$. En $x=e$, $e^{-ik_3(x-e)}=1$.


> [!example]- 📝 Solution détaillée
> **Vitesses et conditions de raccord**
>
> $$\tilde v_1=\frac A{Z_1}\big(e^{-ik_1x}-Re^{ik_1x}\big),\quad\tilde v_2=\frac1{Z_2}\big(Be^{-ik_2x}-Ce^{ik_2x}\big),\quad\tilde v_3=\frac D{Z_3}e^{-ik_3(x-e)}.$$
> Continuité en $x=0$ : $A(1+R)=B+C$ et $\dfrac{A(1-R)}{Z_1}=\dfrac{B-C}{Z_2}$. Continuité en $x=e$ : $Be^{-iu}+Ce^{iu}=D$ et $\dfrac{Be^{-iu}-Ce^{iu}}{Z_2}=\dfrac D{Z_3}$.
>
> **Absence d'onde en retour dans le milieu (3)**
>
> Le milieu (3) est semi-infini et ne contient aucune source : il n'y a pas d'onde venant de l'infini en $x\to+\infty$ ; l'onde dans le milieu (3) est donc purement progressive, ce qui impose $Z(x)=\tilde p/\tilde v=Z_3$ pour $x\ge e$.


**q2.** Montrer que l'impédance ramenée $Z_{\mathrm{in}}=\tilde p(0)/\tilde v(0)$ vue dans la lame en $x=0^+$ vaut
$Z_{\mathrm{in}}=Z_2\dfrac{Z_3\cos u+iZ_2\sin u}{Z_2\cos u+iZ_3\sin u}$. En déduire $R$ en fonction de $Z_{\mathrm{in}}$ et $Z_1$.

> [!tip]- 💡 Coup de pouce
> En $x=e$, $\tilde p/\tilde v=Z_3$ : cela donne le rapport $C/B$. Reportez-le dans $\tilde p/\tilde v$ en $x=0$ et multipliez numérateur et dénominateur par $e^{iu}$.


> [!success]- ✅ Correction
> $R=(Z_{\mathrm{in}}-Z_1)/(Z_{\mathrm{in}}+Z_1)$.


> [!example]- 📝 Solution détaillée
> **Rapport $C/B$**
>
> En $x=e$, $Z_3=Z_2\dfrac{Be^{-iu}+Ce^{iu}}{Be^{-iu}-Ce^{iu}}$. En posant $\Gamma=\dfrac{Ce^{iu}}{Be^{-iu}}$ : $Z_3(1-\Gamma)=Z_2(1+\Gamma)$, d'où $\Gamma=\dfrac{Z_3-Z_2}{Z_3+Z_2}$ (c'est le coefficient de réflexion de la lame sur le milieu 3) et $C/B=\Gamma e^{-2iu}$.
>
> **Impédance en $x=0$**
>
> $$Z_{\mathrm{in}}=Z_2\frac{B+C}{B-C}=Z_2\frac{1+\Gamma e^{-2iu}}{1-\Gamma e^{-2iu}}=Z_2\frac{(Z_3+Z_2)e^{iu}+(Z_3-Z_2)e^{-iu}}{(Z_3+Z_2)e^{iu}-(Z_3-Z_2)e^{-iu}}=Z_2\frac{Z_3\cos u+iZ_2\sin u}{Z_2\cos u+iZ_3\sin u}.$$
>
> **Coefficient de réflexion**
>
> En $x=0$, $\tilde p/\tilde v=Z_1(1+R)/(1-R)=Z_{\mathrm{in}}$ (continuité de $\tilde p$ et $\tilde v$), donc
> $$R=\frac{Z_{\mathrm{in}}-Z_1}{Z_{\mathrm{in}}+Z_1}.$$
> C'est la formule de l'exercice 4, appliquée à un milieu $Z_{\mathrm{in}}$ équivalent.


**q3.** Calculer $Z_{\mathrm{in}}$ pour une lame demi-onde ($e=\lambda_2/2$) puis quart d'onde ($e=\lambda_2/4$).
Que peut-on en conclure sur le rôle de la lame quand $Z_1=Z_3$ dans le premier cas ?

> [!success]- ✅ Correction
> Demi-onde : $Z_{\mathrm{in}}=Z_3$ ; quart d'onde : $Z_{\mathrm{in}}=Z_2^2/Z_3$.


> [!example]- 📝 Solution détaillée
> **Lame demi-onde**
>
> $u=k_2\lambda_2/2=\pi$ : $\cos u=-1$, $\sin u=0$, donc $Z_{\mathrm{in}}=Z_2\dfrac{-Z_3}{-Z_2}=Z_3$ : la lame est «~invisible~» pour le milieu 1, qui «~voit~» directement le milieu 3. Si $Z_1=Z_3$, $R=0$ : transmission totale, quelles que soient les propriétés de la lame (c'est le principe d'une fenêtre sonar, d'un radôme ou d'un hublot de sonde).
>
> **Lame quart d'onde**
>
> $u=\pi/2$ : $\cos u=0$, $\sin u=1$, donc $Z_{\mathrm{in}}=Z_2\dfrac{iZ_2}{iZ_3}=\dfrac{Z_2^2}{Z_3}$. La lame quart d'onde *transforme* l'impédance $Z_3$ en $Z_2^2/Z_3$ (inversion de l'impédance).


**q4.** Démontrer que $T_I=\dfrac{4Z_1Z_3}{(Z_1+Z_3)^2\cos^2u+\left(Z_2+Z_1Z_3/Z_2\right)^2\sin^2u}$.
En déduire la condition d'annulation de la réflexion et la valeur de $T_I$ dans ce cas.

> [!tip]- 💡 Coup de pouce
> Mettez $R=(Z_{\mathrm{in}}-Z_1)/(Z_{\mathrm{in}}+Z_1)$ sous la forme $(a+ib)/(c+id)$ avec $a,b,c,d$ réels, puis calculez $1-|R|^2$.


> [!success]- ✅ Correction
> $R=0\Leftrightarrow u=\pi/2\ [\pi]$ et $Z_2=\sqrt{Z_1Z_3}$ ; alors $T_I=1$.


> [!example]- 📝 Solution détaillée
> **Calcul de $R$**
>
> $$R=\frac{Z_2(Z_3\cos u+iZ_2\sin u)-Z_1(Z_2\cos u+iZ_3\sin u)}{Z_2(Z_3\cos u+iZ_2\sin u)+Z_1(Z_2\cos u+iZ_3\sin u)}=\frac{Z_2(Z_3-Z_1)\cos u+i(Z_2^2-Z_1Z_3)\sin u}{Z_2(Z_3+Z_1)\cos u+i(Z_2^2+Z_1Z_3)\sin u}.$$
>
> **Coefficient énergétique de transmission**
>
> Les milieux étant non absorbants, $T_I=1-|R|^2$. En utilisant $|a+ib|^2=a^2+b^2$ :
> $$1-|R|^2=\frac{Z_2^2\cos^2u\big[(Z_3+Z_1)^2-(Z_3-Z_1)^2\big]+\sin^2u\big[(Z_2^2+Z_1Z_3)^2-(Z_2^2-Z_1Z_3)^2\big]}{Z_2^2(Z_3+Z_1)^2\cos^2u+(Z_2^2+Z_1Z_3)^2\sin^2u}=\frac{4Z_1Z_2^2Z_3\,(\cos^2u+\sin^2u)}{\cdots}.$$
> En divisant haut et bas par $Z_2^2$ :
> $$\boxed{T_I=\frac{4Z_1Z_3}{(Z_1+Z_3)^2\cos^2u+\big(Z_2+Z_1Z_3/Z_2\big)^2\sin^2u}}.$$
> Vérifications : $u=n\pi$ redonne $T_I=4Z_1Z_3/(Z_1+Z_3)^2$ (interface directe 1-3) ; $Z_2=Z_1$ donne le même résultat pour tout $u$.
>
> **Adaptation**
>
> $R=0$ exige à la fois $Z_2(Z_3-Z_1)\cos u=0$ et $(Z_2^2-Z_1Z_3)\sin u=0$. Si $Z_1\neq Z_3$ : $\cos u=0$ (lame quart d'onde, $e=\lambda_2/4$ modulo $\lambda_2/2$) et $Z_2=\sqrt{Z_1Z_3}$ (moyenne géométrique). Alors $T_I=\dfrac{4Z_1Z_3}{(Z_2+Z_1Z_3/Z_2)^2}=\dfrac{4Z_1Z_3}{(2Z_2)^2}=1$ : transmission totale, à la fréquence particulière $f_0=c_2/(4e)$.


**q5.** Sonde échographique : céramique ($Z_1=30$ MRayl) vers tissu ($Z_3=1{,}5$ MRayl) à $f_0=3$ MHz. Calculer $T_I$
sans lame. On insère une couche d'adaptation de célérité $c_2=2700$ m/s : quelle impédance $Z_2$,
quelle épaisseur $e$, quelle valeur de $T_I$ ? Calculer $T_I$ à $0{,}8f_0$ et $1{,}2f_0$.
Pourquoi ne gagne-t-on pas «~un facteur 5~» sur le signal aller-retour mais davantage ?

> [!tip]- 💡 Coup de pouce
> $1~\text{MRayl}=10^6~\text{kg}\cdot\text{m}^{-2}\cdot\text{s}^{-1}$. À la fréquence $f=\beta f_0$, $u=\beta\pi/2$.


> [!success]- ✅ Correction
> Sans lame : $T_I=0{,}18$ ; $Z_2=6{,}7$ MRayl, $e=225\ \mu$m, $T_I=1$ ; à $0{,}8f_0$ et $1{,}2f_0$ : $T_I\approx0{,}70$.


> [!example]- 📝 Solution détaillée
> **Sans lame et dimensionnement**
>
> Sans lame : $T_I=\dfrac{4\times30\times1{,}5}{(31{,}5)^2}=\dfrac{180}{992}\approx0{,}18$ : $82\ \%$ de l'énergie est réfléchie par la différence d'impédance.
>
> Avec lame quart d'onde adaptée : $Z_2=\sqrt{30\times1{,}5}=\sqrt{45}\approx6{,}7$ MRayl (soit, avec $c_2=2700$ m/s, $\rho_2\approx2480~\text{kg}\cdot\text{m}^{-3}$ : une résine chargée), $\lambda_2=c_2/f_0=0{,}90$ mm et $e=\lambda_2/4\approx225~\mu\text{m}$, avec $T_I=1$ à $f_0$ (gain de $10\log_{10}(1/0{,}18)\approx7{,}4$ dB).
>
> **Bande passante**
>
> À $\beta=0{,}8$ : $u=0{,}4\pi$, $\cos^2u=0{,}0955$, $\sin^2u=0{,}9045$. Avec $Z_2+Z_1Z_3/Z_2=2Z_2=13{,}4$ MRayl :
> $$T_I=\frac{180}{992\times0{,}0955+180\times0{,}9045}=\frac{180}{94{,}8+162{,}8}\approx0{,}70.$$
> À $\beta=1{,}2$ ($u=0{,}6\pi$), les valeurs de $\cos^2u$ et $\sin^2u$ sont identiques : $T_I\approx0{,}70$. La lame améliore donc la transmission de $0{,}18$ à plus de $0{,}7$ sur $\pm20\ \%$ de bande autour de $f_0$.
>
> **Aller-retour**
>
> En échographie, l'onde traverse la lame deux fois (émission puis réception) : le facteur de transmission énergétique de l'aller-retour est $T_I^2$ : $0{,}18^2\approx0{,}033$ sans lame, $1$ avec : un gain d'un facteur $\sim30$ en énergie, soit $\sim15$ dB, d'où l'importance de l'adaptation d'impédance en imagerie.


**q6.** Loi de masse. Une paroi mince (épaisseur $e$, masse volumique $\rho_2$, impédance $Z_2\gg Z_0$) sépare deux
zones d'air ($Z_1=Z_3=Z_0$). En supposant $u\ll1$, montrer que $T_I\approx\left[1+\left(\dfrac{\omega m_s}{2Z_0}\right)^2\right]^{-1}$
avec $m_s=\rho_2e$. Calculer la perte par transmission $TL=10\log_{10}(1/T_I)$ pour une vitre de $4$ mm
($\rho_2=2500~\text{kg}\cdot\text{m}^{-3}$, $c_2=5000~\text{m}\cdot\text{s}^{-1}$) à $1$ kHz. Quel est l'effet d'un doublement de la fréquence ou de la masse ?

> [!tip]- 💡 Coup de pouce
> Pour $u\ll1$, $\cos u\approx1$, $\sin u\approx u$, et $Z_2u=\rho_2c_2\omega e/c_2=\omega m_s$.


> [!success]- ✅ Correction
> $TL\approx20\log_{10}(\omega m_s/2Z_0)\approx38$ dB à $1$ kHz ; $+6$ dB par doublement de $f$ ou de $m_s$.


> [!example]- 📝 Solution détaillée
> **Simplification de $T_I$**
>
> Avec $Z_1=Z_3=Z_0$, $\cos u\approx1$, $\sin u\approx u$ :
> $$T_I=\frac{4Z_0^2}{4Z_0^2+(Z_2+Z_0^2/Z_2)^2u^2}\approx\frac{1}{1+\left(\dfrac{Z_2u}{2Z_0}\right)^2}=\frac{1}{1+\left(\dfrac{\omega m_s}{2Z_0}\right)^2},$$
> car $Z_0^2/Z_2\ll Z_2$ et $Z_2u=\rho_2c_2\cdot\omega e/c_2=\omega\rho_2e=\omega m_s$. Seule la *masse surfacique* de la paroi compte, pas sa célérité ni son impédance séparément : la lame se comporte comme une masse pure.
>
> **Application numérique**
>
> $m_s=2500\times0{,}004=10~\text{kg}\cdot\text{m}^{-2}$, $u=\omega e/c_2=2\pi\times10^3\times0{,}004/5000\approx5\times10^{-3}\ll1$ (hypothèse vérifiée), $Z_0=408$ :
> $$\frac{\omega m_s}{2Z_0}=\frac{2\pi\times10^3\times10}{816}\approx77\quad\Longrightarrow\quad TL\approx20\log_{10}77\approx38~\text{dB}.$$
> Doubler la fréquence ou la masse surfacique double l'argument et ajoute $20\log_{10}2\approx6$ dB. C'est la **loi de masse** : $+6$ dB par octave et par doublement de masse. (Les parois réelles donnent des valeurs plus faibles à cause de la flexion et de la coïncidence.)


**q7.** Double paroi. Deux plaques de masses surfaciques $m_1$ et $m_2$ sont séparées par une lame d'air d'épaisseur
$d\ll\lambda$. L'air se comporte comme un ressort de raideur surfacique $K$ (isentropique).


1. Montrer que $K=\rho_0c^2/d$.
2. Écrire les équations du mouvement des deux plaques ; en déduire la fréquence de résonance masse-ressort-masse $f_{mam}$.
3. Application : deux vitres de $4$ mm ($m_1=m_2=10~\text{kg}\cdot\text{m}^{-2}$), $d=12$ mm. Commenter l'intérêt et la limite du double vitrage.

> [!tip]- 💡 Coup de pouce
> Pour des déplacements $\xi_1$ et $\xi_2$, l'épaisseur de la lame d'air varie de $\xi_2-\xi_1$. Utilisez $p=-\Delta V/(\chi_SV)$ comme dans l'exercice 7.


> [!success]- ✅ Correction
> $K=\rho_0c^2/d$ ; $f_{mam}=\frac1{2\pi}\sqrt{K(1/m_1+1/m_2)}\approx240$ Hz.


> [!example]- 📝 Solution détaillée
> **Raideur de la lame d'air**
>
> Pour une surface unité, $V=d$ et $\Delta V=\xi_2-\xi_1$. La surpression dans la lame (uniforme car $d\ll\lambda$) est
> $$p=-\frac{\Delta V}{\chi_SV}=\frac{\rho_0c^2}{d}(\xi_1-\xi_2)=K(\xi_1-\xi_2),\qquad K=\frac{\rho_0c^2}{d}=\frac{\gamma P_0}d.$$
>
> **Équations du mouvement et résonance**
>
> La surpression pousse la plaque 1 vers les $x<0$ et la plaque 2 vers les $x>0$ :
> $$m_1\ddot\xi_1=-K(\xi_1-\xi_2),\qquad m_2\ddot\xi_2=+K(\xi_1-\xi_2).$$
> Pour $\eta=\xi_1-\xi_2$, $\ddot\eta+K\left(\dfrac1{m_1}+\dfrac1{m_2}\right)\eta=0$, donc
> $$\boxed{f_{mam}=\frac1{2\pi}\sqrt{\frac{\rho_0c^2}d\left(\frac1{m_1}+\frac1{m_2}\right)}}.$$
>
> **Application et commentaire**
>
> $K=\dfrac{1{,}2\times340^2}{0{,}012}\approx1{,}16\times10^7~\text{N}\cdot\text{m}^{-3}$ et $\dfrac1{m_1}+\dfrac1{m_2}=0{,}2~\text{m}^2\cdot\text{kg}^{-1}$, d'où $\omega_{mam}=\sqrt{2{,}3\times10^6}\approx1{,}5\times10^3$ rad/s et $f_{mam}\approx240$ Hz.
>
> En dessous de $f_{mam}$, les deux vitres se déplacent ensemble et le système se comporte comme une paroi unique de masse $m_1+m_2$ ; autour de $f_{mam}$, la transmission est même *dégradée* ; au-dessus, la perte par transmission croît beaucoup plus vite (jusqu'à $12$ dB par octave de plus que la loi de masse simple, soit $\sim18$ dB par octave en tout). Le double vitrage est donc surtout efficace pour les moyennes et hautes fréquences, avec un point faible vers $200$--$300$ Hz (trafic routier), qu'on atténue en augmentant $d$ ou en dissymétrisant les masses ($m_1\neq m_2$) pour étaler la résonance.


> [!note]- 🔗 Liens avec d'autres disciplines
> **Optique : traitements antireflets**
>
> Une couche mince de $\lambda/4$ d'indice $n=\sqrt{n_1n_3}$ annule la réflexion (lunettes, objectifs, cellules solaires). L'impédance $Z$ joue le rôle de l'indice, et les formules sont strictement les mêmes.
>
> **Imagerie médicale**
>
> Les sondes échographiques ($3$ à $10$ MHz) comportent une ou plusieurs couches d'adaptation $\lambda/4$ entre la céramique piézoélectrique ($Z\approx30$ MRayl) et le gel puis les tissus ($Z\approx1{,}5$ MRayl).
>
> **Bâtiment et isolation phonique**
>
> La loi de masse guide le dimensionnement des cloisons (doubler la masse surfacique apporte $\sim6$ dB). Les doubles vitrages, les cloisons à ossature et les planchers flottants sont des systèmes masse-ressort-masse dont il faut décaler la fréquence de résonance en dehors de la bande utile.
>
> **Lignes de transmission**
>
> Le transformateur quart d'onde, qui adapte une charge $Z_L$ à une ligne $Z_0$ avec une section de ligne $Z_c=\sqrt{Z_0Z_L}$, est exactement le dispositif de la question 4.
>
> **Sonar et acoustique sous-marine**
>
> Les revêtements anéchoïques des sous-marins (couches de caoutchouc à cavités) et les fenêtres de dôme sonar à lame demi-onde (transparente en eau) utilisent le formalisme de cet exercice.


> [!question]- 🔭 Aller plus loin — Master : Matrices de transfert
> Le calcul se généralise à $N$ couches par produit de matrices $2\times2$ reliant $(p,v)$ de part et d'autre de chaque couche : $\begin{pmatrix}p\\v\end{pmatrix}_{x=0}=\begin{pmatrix}\cos u&iZ_2\sin u\\ i\sin u/Z_2&\cos u\end{pmatrix}\begin{pmatrix}p\\v\end{pmatrix}_{x=e}$. On pourra retrouver $Z_{\mathrm{in}}$ et étudier une multicouche (miroir de Bragg acoustique, cristal phononique).


> [!question]- 🔭 Aller plus loin — Master : Fréquence de coïncidence et flexion des plaques
> Une plaque réelle obéit à une équation de flexion dispersive : à la fréquence de coïncidence, la vitesse des ondes de flexion égale la projection de la vitesse du son dans l'air, et la paroi devient transparente. C'est la principale cause d'écart à la loi de masse dans les vitrages.


> [!question]- 🔭 Aller plus loin — Doctorat : Métamatériaux acoustiques
> Des résonateurs de Helmholtz (cf. exercice 7) répartis dans une paroi permettent de dépasser la loi de masse autour de leur fréquence de résonance : c'est le principe des métamatériaux acoustiques à masse effective négative.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex4-reflexion-et-transmission-d-une-onde-acoustique-a-une-interface-entre-deux-fluides|Exercice 4 — Réflexion et transmission d'une onde acoustique à une interface entre deux fluides]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex5-energie-intensite-acoustique-et-niveau-sonore-de-l-oreille-humaine-a-l-onde-stationnaire|Exercice 5 — Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex6-tube-d-impedance-mesurer-l-absorption-d-un-materiau-avec-une-onde-stationnaire-partielle|Exercice 6 — Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex7-resonateur-de-helmholtz-la-bouteille-qui-chante|Exercice 7 — Résonateur de Helmholtz : la bouteille qui chante]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex2-onde-stationnaire-tube-de-kundt-ouvert|Exercice 2 — Onde stationnaire, tube de Kundt ouvert]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex3-onde-stationnaire-tube-de-kundt-ferme-a-faire-a-la-maison|Exercice 3 — Onde stationnaire, tube de Kundt fermé (à faire à la maison)]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex1-celerite-d-une-onde-acoustique-dans-un-fluide-parfait|Exercice 1 — Célérité d'une onde acoustique dans un fluide parfait]]

