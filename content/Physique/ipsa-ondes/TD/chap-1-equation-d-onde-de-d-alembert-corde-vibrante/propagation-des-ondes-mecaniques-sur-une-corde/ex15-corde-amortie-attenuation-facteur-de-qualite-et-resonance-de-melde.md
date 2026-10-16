---
title: "Exercice 15 — Corde amortie : atténuation, facteur de qualité et résonance de Melde"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a>

### Exercice 15. Corde amortie : atténuation, facteur de qualité et résonance de Melde *(facultatif)*

Une corde de masse linéique $\mu$, tendue avec la force $F$ ($c=\sqrt{F/\mu}$), vibre dans un fluide visqueux (air, eau). Le fluide exerce
sur chaque élément de corde une force de frottement fluide **linéique** $-\lambda\,\partial_ty$ (opposée à la vitesse transversale),
avec $\lambda>0$ en N$\cdot$s$\cdot$m$^{-2}$. On note $\gamma=\lambda/\mu$ (en s$^{-1}$). Pour de petits mouvements, l'équation du mouvement est
$$\frac{\partial^2y}{\partial t^2}+\gamma\,\frac{\partial y}{\partial t}=c^2\,\frac{\partial^2y}{\partial x^2}.$$
On étudie d'abord la propagation, puis les modes propres d'une corde de longueur $\ell$ fixée en $x=0$ et $x=\ell$, enfin le montage de
Melde (exercice 5) avec amortissement.

**q1.** **Propagation.**


(a) Chercher une solution $\underline y=\underline a\,\mathrm e^{j(\omega t-\underline kx)}$ et établir $\underline k^2=\dfrac{\omega^2-j\gamma\omega}{c^2}$.

(b) Pour $\gamma\ll\omega$, montrer que $\underline k\simeq\dfrac\omega c-j\dfrac\gamma{2c}$. En déduire la forme réelle de l'onde, la longueur d'atténuation $\delta$ (amplitude divisée par $\mathrm e$) et la célérité de phase. Commenter l'indépendance en $\omega$.

(c) Dans la limite opposée ($\omega\ll\gamma$), quelle équation aux dérivées partielles retrouve-t-on ? Quel est le comportement de $\underline k$ ?

> [!tip]- 💡 Coup de pouce
> **Dispersion**
>
> Remplacez $\partial_t\to j\omega$ et $\partial_x\to-j\underline k$ ; isolez $\underline k^2$.
>
> **Limite $\omega\ll\gamma$**
>
> Négligez $\partial_t^2y$ devant $\gamma\partial_ty$ : quelle équation obtient-on ?


**q2.** **Modes propres de la corde de longueur $\ell$, fixée aux deux extrémités.**


(a) On cherche des solutions $y=\sin(k_nx)\,\Theta_n(t)$. Établir $\ddot\Theta_n+\gamma\dot\Theta_n+\omega_n^2\Theta_n=0$ avec $\omega_n=n\pi c/\ell$. Résoudre pour $\gamma<2\omega_n$ et montrer que tous les modes sont amortis par le même facteur $\mathrm e^{-\gamma t/2}$.

(b) Déterminer la pseudo-pulsation $\omega_n'$ et le facteur de qualité $Q_n=\omega_n/\gamma$. Comment $Q_n$ dépend-il de $n$ ? Interpréter : pour quel $n$ le mode devient-il surcritique ?

(c) Application : corde de $\ell=0{,}65$ m, $c=143$ m/s, $\gamma=2{,}0$ s$^{-1}$ (cf. ex. 12). Calculer $f_1$, $Q_1$, la durée $\tau$ au bout de laquelle l'amplitude est divisée par $\mathrm e$ et le nombre d'oscillations correspondant.

> [!tip]- 💡 Coup de pouce
> **Séparation**
>
> $\sin(k_nx)\,[\ddot\Theta+\gamma\dot\Theta]=-c^2k_n^2\sin(k_nx)\,\Theta$ (en notant $\omega_n=ck_n$).
>
> **Équation caractéristique**
>
> $\Theta=\mathrm e^{st}$ : $s^2+\gamma s+\omega_n^2=0$.


**q3.** **Melde amorti.** Le vibreur impose $y(0,t)=a\,\mathrm e^{j\omega t}$ ; la corde est fixée en $x=\ell$.


(a) Montrer que $\underline y(x,t)=a\,\dfrac{\sin\!\big(\underline k(\ell-x)\big)}{\sin(\underline k\ell)}\,\mathrm e^{j\omega t}$ avec $\underline k$ de la question (a).

(b) À la fréquence $\omega=\omega_N$ ($k'\ell=N\pi$), montrer que l'amplitude des ventres vaut $A_v\simeq\dfrac{2ca}{\gamma\ell}=\dfrac{2Q_N}{N\pi}\,a$ pour $\gamma\ll\omega_N$. Interpréter.

(c) Un expérimentateur mesure, à la résonance fondamentale ($c=50$ m/s, $\ell=0{,}50$ m), un rapport $A_v/a=40$. Déterminer $\gamma$, $Q_1$, la largeur de la résonance $\Delta f$ et la durée d'extinction libre $\tau$ après arrêt du vibreur.

> [!tip]- 💡 Coup de pouce
> **Transposer ex. 5**
>
> L'équation de Helmholtz $\underline Y''+\underline k^2\underline Y=0$ avec $\underline Y(0)=a$ et $\underline Y(\ell)=0$ a la même solution que pour la corde idéale, avec $k\to\underline k$.
>
> **Sinus complexe**
>
> $\sin(N\pi-jb)=-(-1)^N\,j\sinh b$ avec $b=k''\ell$.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex14-corde-de-piano-raide-dispersion-et-inharmonicite|Exercice 14 — Corde de piano raide : dispersion et inharmonicité]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex6-experience-de-melde-oscillations-forcees-d-une-corde-resonance|Exercice 6 — Expérience de Melde, oscillations forcées d'une corde, résonance]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex1-partie-a-modes-propres-d-un-ressort-helicoidal-ondes-longitudinales-color-blue-part-a-normal-modes-of-a-helical-spring-longitudinal-waves|Exercice 1 — Partie A — Modes propres d'un ressort hélicoïdal (ondes longitudinales) {\color{blue}(Part A — Normal modes of a helical spring, longitudinal waves)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde-color-blue-part-b-effect-of-tension-on-the-normal-modes-of-a-string|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde {\color{blue}(Part B — Effect of tension on the normal modes of a string)}]] · [[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex3-mesurer-la-vitesse-de-la-lumiere-avec-un-four-a-micro-ondes-et-du-chocolat|Exercice 3 — Mesurer la vitesse de la lumière avec un four à micro-ondes et du chocolat]]

