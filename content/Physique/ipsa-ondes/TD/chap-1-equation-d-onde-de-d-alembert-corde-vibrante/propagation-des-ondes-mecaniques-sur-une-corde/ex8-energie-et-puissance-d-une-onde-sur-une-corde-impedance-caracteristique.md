---
title: "Exercice 8 — Énergie et puissance d'une onde sur une corde : impédance caractéristique"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a>

### Exercice 8. Énergie et puissance d'une onde sur une corde : impédance caractéristique *(facultatif)*

Une corde homogène de masse linéique $\mu$, tendue avec la tension $F$, vibre transversalement dans l'approximation des petits angles. Le déplacement $y(x,t)$ vérifie l'équation de d'Alembert avec $c=\sqrt{F/\mu}$.

On admet que la corde possède, par unité de longueur, l'énergie mécanique
$$e(x,t)=\underbrace{\frac{1}{2}\mu\left(\frac{\partial y}{\partial t}\right)^2}_{\text{cinétique}}+\underbrace{\frac{1}{2}F\left(\frac{\partial y}{\partial x}\right)^2}_{\text{potentielle élastique}}.$$
La partie gauche de la corde ($x'<x$) exerce sur la partie droite une force dont la composante transversale est $-F\,\dfrac{\partial y}{\partial x}(x,t)$.

**q1.** Montrer, à l'aide de l'équation de d'Alembert, que l'énergie vérifie l'équation de conservation locale
$$\frac{\partial e}{\partial t}+\frac{\partial\mathcal{P}}{\partial x}=0,\qquad\text{avec}\qquad\mathcal{P}(x,t)=-F\,\frac{\partial y}{\partial x}\,\frac{\partial y}{\partial t}.$$
Donner la signification physique de $\mathcal{P}$ (indication : puissance d'une force).

> [!tip]- 💡 Coup de pouce
> **Dériver $e$**
>
> Calculer $\partial_t e$ et $\partial_x\mathcal{P}$ séparément, puis regrouper les termes en $\partial_t y$.


**q2.** Onde progressive $y=f(x-ct)$. Montrer que $e=F f'^2$, puis que $\mathcal{P}=c\,e$. En déduire que $\mathcal{P}=Z\left(\partial_t y\right)^2$ avec $Z=\sqrt{F\mu}$. Que devient ce résultat pour une onde régressive $y=g(x+ct)$ ?

> [!tip]- 💡 Coup de pouce
> **Dérivées**
>
> $\partial_x y=f'$ et $\partial_t y=-c\,f'$. N'oubliez pas $\mu c^2=F$.


**q3.** Onde sinusoïdale progressive $y=a\cos(kx-\omega t)$. Calculer la puissance moyenne $\langle\mathcal{P}\rangle$ et la densité linéique d'énergie moyenne $\langle e\rangle$. Application numérique avec les données de l'exercice 3 : $\mu=0{,}12\ \text{kg}\cdot\text{m}^{-1}$, $F=20\ \text{N}$, $a=2\ \text{mm}$, $\lambda=0{,}25\ \text{m}$.

> [!tip]- 💡 Coup de pouce
> **Moyenne**
>
> $\langle\sin^2\rangle=\tfrac{1}{2}$ sur une période. Calculer $\omega=2\pi c/\lambda$.


**q4.** Comment varie $\langle\mathcal{P}\rangle$ si (i) on double la fréquence à amplitude $a$ constante ; (ii) on double la tension $F$ à $\mu$, $\omega$ et $a$ constants ; (iii) on double l'amplitude ?

**q5.** Onde stationnaire $y=A\sin(kx)\cos(\omega t)$ avec $\omega=ck$. Calculer $\mathcal{P}(x,t)$ et sa moyenne temporelle. Que dire du transport d'énergie ? Calculer ensuite, pour le mode $N$ d'une corde fixée en $x=0$ et $x=L$ ($kL=N\pi$), les énergies cinétique $K(t)$ et potentielle $U(t)$ et leur somme.

> [!tip]- 💡 Coup de pouce
> **Formules trigonométriques**
>
> $\sin kx\cos kx=\tfrac{1}{2}\sin2kx$ et $\int_0^L\sin^2kx\,\mathrm{d}x=\int_0^L\cos^2kx\,\mathrm{d}x=\dfrac{L}{2}$ pour $kL=N\pi$.


**q6.** Application : la troisième corde de guitare de l'exercice 4 ($\mu=5{,}04\times10^{-4}\ \text{kg/m}$, $L=63\ \text{cm}$, $f_1=147\ \text{Hz}$) vibre sur son fondamental avec une amplitude de $1\ \text{mm}$ au ventre. Calculer son énergie mécanique.

> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex4-equation-des-cordes-vibrantes-et-onde-progressive|Exercice 4 — Équation des cordes vibrantes et onde progressive]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex10-corde-discrete-chaine-de-masses-dispersion-coupure-et-vitesse-de-groupe|Exercice 10 — Corde discrète (chaîne de masses) : dispersion, coupure et vitesse de groupe]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex11-une-perle-sur-la-corde-reflexion-transmission-et-filtre-passe-bas-mecanique|Exercice 11 — Une perle sur la corde : réflexion, transmission et filtre passe-bas mécanique]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex12-adaptation-d-impedance-lame-quart-d-onde-entre-deux-cordes|Exercice 12 — Adaptation d'impédance : lame quart d'onde entre deux cordes]]

