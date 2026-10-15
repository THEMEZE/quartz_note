---
title: "Exercice 12 — Adaptation d'impédance : lame quart d'onde entre deux cordes"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · [📄 Corrigé](/pdfs/td1_PhV212_corrige.pdf) · [📄 Énoncé](/pdfs/td1_PhV212_enonce.pdf) · [📄 Aides (td1_PhV212_aides)](/pdfs/td1_PhV212_aides.pdf) · [📄 Aides (td1_PhV212_exs_maison_aide)](/pdfs/td1_PhV212_exs_maison_aide.pdf) · [📄 PDF (td1_ex1_coup_de_pouce)](/pdfs/td1_ex1_coup_de_pouce.pdf) · [📄 PDF (td1_ex1_solution_detaillee)](/pdfs/td1_ex1_solution_detaillee.pdf) · [📄 Fiche enseignant (td1_PhV212_fiche)](/pdfs/td1_PhV212_fiche.pdf) · [📄 Fiche enseignant (td1_ex1_fiche)](/pdfs/td1_ex1_fiche.pdf) · [📄 Fiche enseignant (td1_exs_maison_fiche)](/pdfs/td1_exs_maison_fiche.pdf)

### Exercice 12. Adaptation d'impédance : lame quart d'onde entre deux cordes *(facultatif)*

On reprend les deux cordes de l'exercice 2, de même tension $F=400\ \text{N}$ et de masses linéiques $\mu_1=1{,}4\times10^{-4}\ \text{kg/m}$ et $\mu_2=2{,}8\times10^{-4}\ \text{kg/m}$. On les considère ici de longueur infinie, jointes en $x=0$. On note $Z_i=\sqrt{F\mu_i}$ leur impédance caractéristique (exercice 7) et $k_i=\omega/c_i$ leur nombre d'onde, avec $c_i=\sqrt{F/\mu_i}$.

Une onde sinusoïdale incidente $\underline{y}_i=e^{\,j(\omega t-k_1x)}$ arrive de la corde 1 ($x<0$). On cherche à supprimer la réflexion en intercalant entre les deux cordes un segment de corde de longueur $d$ et de masse linéique $\mu_m$ (soumis à la même tension $F$), analogue mécanique du traitement antireflet d'une lentille optique.

**q1.** Interface simple (sans lame). Écrire les conditions de continuité en $x=0$ pour l'onde incidente $\underline{y}_i$, l'onde réfléchie $\underline{r}\,e^{\,j(\omega t+k_1x)}$ et l'onde transmise $\underline{\tau}\,e^{\,j(\omega t-k_2x)}$. En déduire
$$\underline{r}=\frac{Z_1-Z_2}{Z_1+Z_2},\qquad\underline{\tau}=\frac{2Z_1}{Z_1+Z_2}.$$
Calculer les coefficients de réflexion et de transmission en puissance $R$ et $T$ (rappel : $T=\dfrac{Z_2}{Z_1}|\underline{\tau}|^2$) pour les deux cordes de l'énoncé. Vérifier $R+T=1$.

> [!tip]- 💡 Coup de pouce
> **Continuité**
>
> $y$ continue : $1+\underline{r}=\underline{\tau}$. $\partial_x y$ continue : $k_1(1-\underline{r})=k_2\underline{\tau}$. Utiliser $k_i\propto Z_i$.


> [!success]- ✅ Correction
> **Résultat**
>
> $\underline{r}=\dfrac{Z_1-Z_2}{Z_1+Z_2}=\dfrac{1-\sqrt2}{1+\sqrt2}\approx-0{,}172$ ; $R=\underline{r}^2\approx2{,}9\ \%$ et $T=\dfrac{4Z_1Z_2}{(Z_1+Z_2)^2}\approx97{,}1\ \%$.


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> Continuité de $y$ : $1+\underline{r}=\underline{\tau}$. Continuité de la pente : $-jk_1+jk_1\underline{r}=-jk_2\underline{\tau}$, soit $k_1(1-\underline{r})=k_2\underline{\tau}$. Avec $k_i\propto Z_i$ : $Z_1(1-\underline{r})=Z_2(1+\underline{r})$, d'où
> $$\underline{r}=\frac{Z_1-Z_2}{Z_1+Z_2},\qquad\underline{\tau}=1+\underline{r}=\frac{2Z_1}{Z_1+Z_2}.$$
> Ici $Z_1=\sqrt{400\times1{,}4\times10^{-4}}\approx0{,}2366\ \text{kg/s}$ et $Z_2=\sqrt{400\times2{,}8\times10^{-4}}\approx0{,}3347\ \text{kg/s}$, donc $Z_2/Z_1=\sqrt2$ et $\underline{r}=\dfrac{1-\sqrt2}{1+\sqrt2}\approx-0{,}1716$.
> Les puissances moyennes (exercice 7) valent $\tfrac{1}{2}Z_i\omega^2|\text{amp}|^2$, donc $R=\underline{r}^2\approx0{,}0294$ et $T=\dfrac{Z_2}{Z_1}\underline{\tau}^2=\dfrac{4Z_1Z_2}{(Z_1+Z_2)^2}\approx0{,}9706$. On vérifie $R+T=1$ :
> $$\frac{(Z_1-Z_2)^2+4Z_1Z_2}{(Z_1+Z_2)^2}=1.$$
> Le signe négatif de $\underline{r}$ indique une inversion du signe de l'onde, car on passe d'une corde légère à une corde plus lourde.


**q2.** On insère entre $x=0$ et $x=d$ un segment de corde $m$ (impédance $Z_m$, nombre d'onde $k_m$). Dans ce segment, $\underline{Y}(x)$ (amplitude complexe) vérifie $\underline{Y}''+k_m^2\underline{Y}=0$. Pour $x>d$ on a seulement une onde transmise : $\underline{Y}(x)=\underline{\tau}\,e^{-jk_2x}$. On choisit $d=\lambda_m/4$ (c'est-à-dire $k_md=\pi/2$).
Montrer que $\underline{Y}(d)=\underline{Y}'(0)/k_m$ et $\underline{Y}'(d)=-k_m\underline{Y}(0)$. En écrivant la continuité de $\underline{Y}$ et de $\underline{Y}'$ en $x=d$, puis en $x=0$, établir
$$\frac{1-\underline{r}}{1+\underline{r}}=\frac{Z_m^2}{Z_1Z_2}.$$

> [!tip]- 💡 Coup de pouce
> **Solution dans la lame**
>
> $\underline{Y}(x)=\underline{Y}(0)\cos k_mx+\dfrac{\underline{Y}'(0)}{k_m}\sin k_mx$, donc $\underline{Y}'(x)=-k_m\underline{Y}(0)\sin k_mx+\underline{Y}'(0)\cos k_mx$.
>
> **Sur la corde 2**
>
> En $x=d$, $\underline{Y}'(d)=-jk_2\underline{Y}(d)$ (car il n'y a que l'onde progressive $e^{-jk_2x}$). En $x=0^-$ : $\underline{Y}(0)=1+\underline{r}$ et $\underline{Y}'(0)=-jk_1(1-\underline{r})$.


> [!success]- ✅ Correction
> **Résultat**
>
> $\underline{Y}(d)=\underline{Y}'(0)/k_m$ et $\underline{Y}'(d)=-k_m\underline{Y}(0)$. La condition en $d$ donne $\underline{Y}'(0)/\underline{Y}(0)=-jk_m^2/k_2$, soit $\dfrac{1-\underline{r}}{1+\underline{r}}=\dfrac{k_m^2}{k_1k_2}=\dfrac{Z_m^2}{Z_1Z_2}$.


> [!example]- 📝 Solution détaillée
> **Démonstration**
>
> Avec $k_md=\pi/2$ : $\cos k_md=0$ et $\sin k_md=1$, d'où $\underline{Y}(d)=\underline{Y}'(0)/k_m$ et $\underline{Y}'(d)=-k_m\underline{Y}(0)$.
> Continuité en $x=d$ avec la corde 2 : $\underline{Y}'(d)=-jk_2\underline{Y}(d)$, soit $-k_m\underline{Y}(0)=-jk_2\,\dfrac{\underline{Y}'(0)}{k_m}$, donc
> $$\frac{\underline{Y}'(0)}{\underline{Y}(0)}=\frac{k_m^2}{jk_2}=-j\,\frac{k_m^2}{k_2}.$$
> Continuité en $x=0$ avec la corde 1 : $\dfrac{\underline{Y}'(0)}{\underline{Y}(0)}=\dfrac{-jk_1(1-\underline{r})}{1+\underline{r}}$. En égalant :
> $$\frac{1-\underline{r}}{1+\underline{r}}=\frac{k_m^2}{k_1k_2}=\frac{Z_m^2}{Z_1Z_2}\qquad(k_i\propto Z_i).$$
> Avec $\rho=\dfrac{Z_m^2}{Z_1Z_2}$ : $\underline{r}=\dfrac{1-\rho}{1+\rho}=\dfrac{Z_1Z_2-Z_m^2}{Z_1Z_2+Z_m^2}$.


**q3.** En déduire la condition d'adaptation, l'expression de $\mu_m$ en fonction de $\mu_1$ et $\mu_2$ et la valeur numérique de $\mu_m$. Calculer la célérité $c_m$ dans la lame, puis la longueur $d$ pour une adaptation parfaite à $f_0=1000\ \text{Hz}$. À quelles autres fréquences la réflexion est-elle nulle ?

> [!success]- ✅ Correction
> **Résultat**
>
> $\underline{r}=0\Leftrightarrow Z_m^2=Z_1Z_2$, soit $\mu_m=\sqrt{\mu_1\mu_2}\approx1{,}98\times10^{-4}\ \text{kg/m}$. $c_m=\sqrt{c_1c_2}\approx1421\ \text{m/s}$ et $d=\dfrac{c_m}{4f_0}\approx35{,}5\ \text{cm}$. La réflexion est nulle aux fréquences $f_p=(2p+1)f_0$ ($p\in\mathbb{N}$) : $1000$, $3000$, $5000\ \text{Hz},\dots$


> [!example]- 📝 Solution détaillée
> **Application numérique**
>
> $\underline{r}=0\Leftrightarrow Z_m^2=Z_1Z_2\Leftrightarrow F\mu_m=F\sqrt{\mu_1\mu_2}\Leftrightarrow\mu_m=\sqrt{\mu_1\mu_2}=\sqrt{1{,}4\times2{,}8}\times10^{-4}\approx1{,}98\times10^{-4}\ \text{kg/m}$ (moyenne géométrique).
> $c_m=\sqrt{F/\mu_m}=\sqrt{400/1{,}98\times10^{-4}}\approx1421\ \text{m/s}=\sqrt{c_1c_2}$ (avec $c_1\approx1690\ \text{m/s}$ et $c_2\approx1195\ \text{m/s}$).
> Pour $f_0=1000\ \text{Hz}$ : $\lambda_m=c_m/f_0=1{,}42\ \text{m}$ et $d=\lambda_m/4\approx0{,}355\ \text{m}$.
> La condition $k_md=\pi/2\ [\pi]$ soit $d=(2p+1)\lambda_m/4$ donne $f_p=(2p+1)\dfrac{c_m}{4d}=(2p+1)f_0$.
> Le segment coûte peu : la puissance transmise passe de $97{,}1\ \%$ à $100\ \%$ à $f_0$.


**q4.** (*) Pour une longueur $d$ quelconque, on admet que
$$\frac{1-\underline{r}}{1+\underline{r}}=\frac{Z_m}{Z_1}\,\frac{Z_2\cos\varphi+jZ_m\sin\varphi}{Z_m\cos\varphi+jZ_2\sin\varphi},\qquad\varphi=k_md.$$
Vérifier que cette expression redonne (i) le résultat de la question 1 pour $d=0$ et (ii) celui de la question 2 pour $\varphi=\pi/2$. Puis, avec $d$ fixée par la question 3 et $Z_m$ adapté, on donne la valeur de $R$ pour $\varphi=\pi/4$ ($f=f_0/2$), $\pi/2$ ($f=f_0$), $3\pi/4$ ($f=3f_0/2$) et $\pi$ ($f=2f_0$) : $R\approx1{,}5\ \%$, $0$, $1{,}5\ \%$ et $2{,}9\ \%$. Commenter.

> [!success]- ✅ Correction
> **Résultat**
>
> (i) $\varphi=0$ : $\dfrac{1-\underline{r}}{1+\underline{r}}=\dfrac{Z_m}{Z_1}\dfrac{Z_2}{Z_m}=\dfrac{Z_2}{Z_1}$, soit $\underline{r}=\dfrac{Z_1-Z_2}{Z_1+Z_2}$. (ii) $\varphi=\pi/2$ : $\dfrac{Z_m}{Z_1}\dfrac{jZ_m}{jZ_2}=\dfrac{Z_m^2}{Z_1Z_2}$. La lame est efficace autour de $f_0$ ($R\le1{,}5\ \%$ pour $f_0/2\le f\le3f_0/2$) et sans effet pour $f=2f_0$ (lame demi-onde : elle est « invisible », on retrouve $R=2{,}9\ \%$).


> [!example]- 📝 Solution détaillée
> **Vérifications et commentaire**
>
> (i) Pour $d=0$, $\varphi=0$, $\cos\varphi=1$ et $\sin\varphi=0$ : le second facteur vaut $Z_2/Z_m$, donc $\dfrac{1-\underline{r}}{1+\underline{r}}=\dfrac{Z_2}{Z_1}$, ce qui redonne $\underline{r}=\dfrac{Z_1-Z_2}{Z_1+Z_2}$.
> (ii) Pour $\varphi=\pi/2$ : $\cos\varphi=0$, $\sin\varphi=1$ : le second facteur vaut $\dfrac{jZ_m}{jZ_2}=\dfrac{Z_m}{Z_2}$, donc $\dfrac{1-\underline{r}}{1+\underline{r}}=\dfrac{Z_m^2}{Z_1Z_2}$ (question 2).
>
> Commentaire : à la fréquence de conception $f_0$, la réflexion est nulle ; elle reste inférieure à $1{,}5\ \%$ pour $f_0/2\le f\le3f_0/2$ et ne dépasse jamais la valeur $R_0=2{,}9\ \%$ sans lame. Pour $f=2f_0$, $\varphi=\pi$ : la lame est une demi-onde et se comporte comme si elle n'existait pas ($R=R_0=2{,}9\ \%$). L'adaptation est donc à bande étroite ; en élargissant la bande avec plusieurs lames, on obtient une transmission très proche de $1$ sur un large intervalle de fréquences.


**q5.** (*) Fonctionnement en impulsion. Pourquoi une impulsion brève ne peut-elle pas être parfaitement adaptée par la lame quart d'onde de la question 3 ? Que se passe-t-il pour la partie de l'impulsion réfléchie sur chaque interface ? Estimer le retard entre les deux échos.

> [!success]- ✅ Correction
> **Résultat**
>
> Une impulsion brève contient un large spectre de fréquences, alors que l'adaptation est parfaite seulement à $f_0$ et ses multiples impairs. Deux échos apparaissent, réfléchis à $x=0$ et $x=d$, séparés par $\Delta t=\dfrac{2d}{c_m}=\dfrac{1}{2f_0}=0{,}5\ \text{ms}$ ; ils sont de même signe : pour une impulsion, ils ne s'annulent pas. Ils ne se compensent que pour une sinusoïde de fréquence $f_0$, car le retard $\Delta t$ vaut alors une demi-période.


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> Les deux interfaces réfléchissent avec des coefficients de même signe : $\underline{r}_{1m}=\dfrac{Z_1-Z_m}{Z_1+Z_m}\approx-0{,}086$ (corde 1 / lame) et $\underline{r}_{m2}=\dfrac{Z_m-Z_2}{Z_m+Z_2}\approx-0{,}086$ (lame / corde 2). Le second écho a parcouru en plus un aller-retour $2d=\lambda_m/2$ dans la lame, soit un retard $\Delta t=\dfrac{2d}{c_m}=\dfrac{T_0}{2}=0{,}5\ \text{ms}$ à $f_0$. Pour une sinusoïde de fréquence $f_0$, ce retard correspond à un déphasage de $\pi$ : les deux ondes réfléchies sont en opposition de phase et s'annulent (interférences en couches minces, comme pour un traitement antireflet en optique). Pour une impulsion de durée très inférieure à $\Delta t=0{,}5\ \text{ms}$, les deux échos sont distincts et de même signe : rien ne s'annule et l'énergie réfléchie totale est proche de celle sans lame. La compensation est un effet spectral, limité au voisinage de $f_0$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex3-celerite-d-une-onde-sur-une-corde-homogene|Exercice 3 — Célérité d’une onde sur une corde homogène]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex11-une-perle-sur-la-corde-reflexion-transmission-et-filtre-passe-bas-mecanique|Exercice 11 — Une perle sur la corde : réflexion, transmission et filtre passe-bas mécanique]] · [[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex1-ondes-sur-un-ressort-long-slinky-filmees-au-ralenti-impulsions-reflexions-et-modes-propres|Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex8-energie-et-puissance-d-une-onde-sur-une-corde-impedance-caracteristique|Exercice 8 — Énergie et puissance d'une onde sur une corde : impédance caractéristique]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex5-corde-fixee-a-ses-deux-extremites-et-ondes-stationnaires|Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales-color-blue-part-a-normal-modes-of-a-helical-spring-longitudinal-waves|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres-color-blue-part-d-compatibility-of-wavelengths-with-the-normal-mode-model|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres {\color{blue}(Part D — Compatibility of wavelengths with the normal-mode model)}]]

