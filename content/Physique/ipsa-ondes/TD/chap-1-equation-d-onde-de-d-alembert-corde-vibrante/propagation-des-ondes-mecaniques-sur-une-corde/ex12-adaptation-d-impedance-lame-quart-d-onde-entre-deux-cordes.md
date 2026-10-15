---
title: "Exercice 12 — Adaptation d'impédance : lame quart d'onde entre deux cordes"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · [📄 Énoncé](/pdfs/td1_PhV212_enonce.pdf)

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


**q3.** En déduire la condition d'adaptation, l'expression de $\mu_m$ en fonction de $\mu_1$ et $\mu_2$ et la valeur numérique de $\mu_m$. Calculer la célérité $c_m$ dans la lame, puis la longueur $d$ pour une adaptation parfaite à $f_0=1000\ \text{Hz}$. À quelles autres fréquences la réflexion est-elle nulle ?

**q4.** (*) Pour une longueur $d$ quelconque, on admet que
$$\frac{1-\underline{r}}{1+\underline{r}}=\frac{Z_m}{Z_1}\,\frac{Z_2\cos\varphi+jZ_m\sin\varphi}{Z_m\cos\varphi+jZ_2\sin\varphi},\qquad\varphi=k_md.$$
Vérifier que cette expression redonne (i) le résultat de la question 1 pour $d=0$ et (ii) celui de la question 2 pour $\varphi=\pi/2$. Puis, avec $d$ fixée par la question 3 et $Z_m$ adapté, on donne la valeur de $R$ pour $\varphi=\pi/4$ ($f=f_0/2$), $\pi/2$ ($f=f_0$), $3\pi/4$ ($f=3f_0/2$) et $\pi$ ($f=2f_0$) : $R\approx1{,}5\ \%$, $0$, $1{,}5\ \%$ et $2{,}9\ \%$. Commenter.

**q5.** (*) Fonctionnement en impulsion. Pourquoi une impulsion brève ne peut-elle pas être parfaitement adaptée par la lame quart d'onde de la question 3 ? Que se passe-t-il pour la partie de l'impulsion réfléchie sur chaque interface ? Estimer le retard entre les deux échos.

> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex3-celerite-d-une-onde-sur-une-corde-homogene|Exercice 3 — Célérité d’une onde sur une corde homogène]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex11-une-perle-sur-la-corde-reflexion-transmission-et-filtre-passe-bas-mecanique|Exercice 11 — Une perle sur la corde : réflexion, transmission et filtre passe-bas mécanique]] · [[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex1-ondes-sur-un-ressort-long-slinky-filmees-au-ralenti-impulsions-reflexions-et-modes-propres|Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex8-energie-et-puissance-d-une-onde-sur-une-corde-impedance-caracteristique|Exercice 8 — Énergie et puissance d'une onde sur une corde : impédance caractéristique]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex5-corde-fixee-a-ses-deux-extremites-et-ondes-stationnaires|Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales-color-blue-part-a-normal-modes-of-a-helical-spring-longitudinal-waves|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex4-partie-d-compatibilite-des-longueurs-d-onde-avec-le-modele-des-modes-propres-color-blue-part-d-compatibility-of-wavelengths-with-the-normal-mode-model|Exercice 4 — Partie D — Compatibilité des longueurs d'onde avec le modèle des modes propres {\color{blue}(Part D — Compatibility of wavelengths with the normal-mode model)}]]

