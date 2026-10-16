---
title: "Exercice 11 — Une perle sur la corde : réflexion, transmission et filtre passe-bas mécanique"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a>

### Exercice 11. Une perle sur la corde : réflexion, transmission et filtre passe-bas mécanique *(facultatif)*

Une corde homogène infinie, de masse linéique $\mu=0{,}02\ \text{kg}\cdot\text{m}^{-1}$ et de tension $F=50\ \text{N}$, est le siège d'ondes transversales. Une petite perle de masse $m=5\ \text{g}$ est fixée à la corde au point $x=0$. On néglige le poids et les frottements.

Une onde sinusoïdale incidente $\underline{y}_i=e^{\,j(\omega t-kx)}$ arrive de la gauche ($x<0$). Il apparaît une onde réfléchie $\underline{y}_r=\underline{r}\,e^{\,j(\omega t+kx)}$ et une onde transmise $\underline{y}_t=\underline{\tau}\,e^{\,j(\omega t-kx)}$ ($x>0$).

On note $c=\sqrt{F/\mu}$, $k=\omega/c$ et $Z=\sqrt{F\mu}$ l'impédance caractéristique de la corde (exercice 7).

**q1.** Écrire les deux conditions de raccordement en $x=0$. Pour la seconde, établir
$$m\,\frac{\partial^2y}{\partial t^2}(0,t)=F\left[\frac{\partial y}{\partial x}(0^+,t)-\frac{\partial y}{\partial x}(0^-,t)\right].$$

> [!tip]- 💡 Coup de pouce
> **Forces sur la perle**
>
> La corde de droite tire la perle avec la composante transversale $+F\,\partial_x y(0^+)$, celle de gauche avec $-F\,\partial_x y(0^-)$ (cf. exercice 3).


**q2.** En déduire les coefficients
$$\underline{\tau}=\frac{1}{1+j\beta},\qquad\underline{r}=\frac{-j\beta}{1+j\beta},\qquad\text{avec}\quad\beta=\frac{m\omega}{2Z}.$$
Vérifier que $\underline{\tau}=1+\underline{r}$ et que $|\underline{r}|^2+|\underline{\tau}|^2=1$.

> [!tip]- 💡 Coup de pouce
> **Utiliser $Z$**
>
> $kF=\dfrac{\omega}{c}F=\omega\sqrt{F\mu}=\omega Z$. Reporter les expressions de $\partial_x y$ dans (2).


**q3.** Puissances. Exprimer les coefficients de réflexion et de transmission en puissance, $R=|\underline{r}|^2$ et $T=|\underline{\tau}|^2$ (les impédances des deux côtés sont égales). Montrer que $R+T=1$ et interpréter. Définir la fréquence de coupure $f_c$ par $R=T=\tfrac{1}{2}$ et la calculer. Calculer $R$ et $T$ à $f=20\ \text{Hz}$ et à $f=100\ \text{Hz}$.

> [!tip]- 💡 Coup de pouce
> **Puissances**
>
> D'après l'exercice 7, pour une onde progressive $\langle\mathcal{P}\rangle=\tfrac{1}{2}Z\omega^2|\text{amplitude}|^2$ : avec le même $Z$ et le même $\omega$, les rapports de puissances sont les rapports des modules au carré.


**q4.** Déphasage. Calculer l'argument de $\underline{\tau}$. À la fréquence de coupure, quel est le retard temporel de l'onde transmise par rapport à ce qu'elle serait sans perle ? Comparer avec la période.

**q5.** (*) Approche temporelle. On envoie une onde de forme quelconque $y_i(x,t)=s(t-x/c)$. Notons $y_i(0,t)=s(t)$, $y_r(0,t)$ et $y_t(0,t)$ les déplacements en $x=0$. Montrer que $y_t(0,t)=y_i(0,t)+y_r(0,t)$ et que, pour des ondes qui partent du repos,
$$\theta\,\dot y_t(0,t)+y_t(0,t)=y_i(0,t),\qquad\theta=\frac{m}{2Z}.$$
Calculer $\theta$. Résoudre pour un échelon $s(t)=Y_0$ ($t>0$) et donner le déplacement réfléchi.

> [!tip]- 💡 Coup de pouce
> **Ondes progressives**
>
> $y_i=s(t-x/c)$ donne $\partial_x y_i=-\dot s/c$. Pour l'onde réfléchie, $y_r=u(t+x/c)$ donne $\partial_x y_r=+\dot u/c$. Pour l'onde transmise, $\partial_x y_t=-\dot y_t/c$. Utiliser $F/c=Z$.


**q6.** Cas limites. Que deviennent $\underline{r}$, $\underline{\tau}$ quand $m\to0$ ? quand $m\to\infty$ ? quand $\omega\to0$ ? Dans chaque cas, donner la situation physique correspondante.

**q7.** (**) On dispose $M$ perles identiques régulièrement espacées d'une distance $d$ sur la même corde. Sans calcul, expliquer qualitativement pourquoi, pour $\omega\ll\omega_c$, l'onde se propage presque librement mais avec une vitesse plus faible, puis faire le lien avec l'exercice 9.

> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex3-celerite-d-une-onde-sur-une-corde-homogene|Exercice 3 — Célérité d’une onde sur une corde homogène]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex12-adaptation-d-impedance-lame-quart-d-onde-entre-deux-cordes|Exercice 12 — Adaptation d'impédance : lame quart d'onde entre deux cordes]] · [[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex1-ondes-sur-un-ressort-long-slinky-filmees-au-ralenti-impulsions-reflexions-et-modes-propres|Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex8-energie-et-puissance-d-une-onde-sur-une-corde-impedance-caracteristique|Exercice 8 — Énergie et puissance d'une onde sur une corde : impédance caractéristique]]

