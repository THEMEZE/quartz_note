---
title: "Exercice 8 — Énergie et puissance d'une onde sur une corde : impédance caractéristique"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td1_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_ex1_coup_de_pouce.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_coup_de_pouce)</a> · <a href="/pdfs/td1_ex1_solution_detaillee.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_solution_detaillee)</a>

### Exercice 8. Énergie et puissance d'une onde sur une corde : impédance caractéristique *(facultatif)*

*Difficulté ●●●●○ · ⏱ 45 min · Type : Approfondissement*

Une corde homogène de masse linéique $\mu$, tendue avec la tension $F$, vibre transversalement dans l'approximation des petits angles. Le déplacement $y(x,t)$ vérifie l'équation de d'Alembert avec $c=\sqrt{F/\mu}$.

On admet que la corde possède, par unité de longueur, l'énergie mécanique
$$e(x,t)=\underbrace{\frac{1}{2}\mu\left(\frac{\partial y}{\partial t}\right)^2}_{\text{cinétique}}+\underbrace{\frac{1}{2}F\left(\frac{\partial y}{\partial x}\right)^2}_{\text{potentielle élastique}}.$$
La partie gauche de la corde ($x'<x$) exerce sur la partie droite une force dont la composante transversale est $-F\,\dfrac{\partial y}{\partial x}(x,t)$.


> [!question]- 🪝 Accroche
> **Qu'est-ce qui se propage vraiment le long d'une corde ?**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *Quand une onde parcourt une corde, aucun morceau de corde ne voyage : chacun monte et descend sur place. Pourtant, quelque chose est transporté d'un bout à l'autre : l'**énergie**. Quelle puissance faut-il fournir à un vibreur pour entretenir l'onde ? Et pourquoi une onde **stationnaire** ne transporte-t-elle rien ?*
>
> **Idée clé : l'énergie obéit à une loi de conservation locale.** Avec $e=\tfrac12\mu\dot y^2+\tfrac12Fy'^2$ et $\mathcal P=-F\,\partial_x y\,\partial_t y$ (puissance de la force de tension) :
> $$\frac{\partial e}{\partial t}+\frac{\partial\mathcal P}{\partial x}=0.$$
> Pour une onde progressive, $\mathcal P=c\,e=Z\,(\partial_t y)^2$ avec $Z=\sqrt{F\mu}$ l'**impédance caractéristique** : l'énergie est transportée à la vitesse $c$. Pour une onde sinusoïdale, $\langle\mathcal P\rangle=\tfrac12Z\omega^2a^2$ ; pour une onde stationnaire, $\langle\mathcal P\rangle=0$.




> [!abstract]- 🧠 À savoir avant
> **Équation de d'Alembert et ondes progressives**
>
> Exercices 0 et 3 : solutions $f(x-ct)$, $g(x+ct)$, équation des cordes vibrantes, modes propres d'une corde fixée (exercice 4).




> [!info]- 🎯 Ce que tu sauras faire
> **Suivre l'énergie plutôt que le déplacement**
>
> Établir un bilan local d'énergie, calculer la puissance transportée par une onde progressive, comprendre pourquoi une onde stationnaire ne transporte pas d'énergie en moyenne.




> [!note]- 🧮 Outils mathématiques
> **Moyenne temporelle : $\langle\sin^2\rangle=\langle\cos^2\rangle=\tfrac12$**
>
> D'après $\cos2u=1-2\sin^2u$ et $\langle\cos2u\rangle=0$, on a $\langle\sin^2u\rangle=\tfrac12$. Oublier ce facteur double les résultats. De même $\langle\sin u\cos u\rangle=\tfrac12\langle\sin2u\rangle=0$.
>
> **Formule de duplication : $\sin(2x)=2\sin x\cos x$**
>
> Pour l'onde stationnaire, $\mathcal P=FA^2k\omega\sin kx\cos kx\sin\omega t\cos\omega t=\tfrac14FA^2k\omega\sin(2kx)\sin(2\omega t)$ : produit de deux sinus de moyenne nulle.
>
> **Dérivée d'un produit et dérivées croisées**
>
> $\partial_x(\partial_x y\,\partial_t y)=\partial_x^2y\,\partial_t y+\partial_x y\,\partial_x\partial_t y$, et $\partial_x\partial_t y=\partial_t\partial_x y$ (théorème de Schwarz). Les termes croisés se compensent dans la conservation de l'énergie.
>
> **Équation de continuité**
>
> $\partial_t e+\partial_x\mathcal P=0$ est de la forme « variation locale de densité + divergence du flux = 0 » (conservation d'une grandeur : charge, masse, énergie).
>
> **Intégrales trigonométriques**
>
> $\displaystyle\int_0^L\sin^2(kx)\,\mathrm dx=\int_0^L\cos^2(kx)\,\mathrm dx=\frac L2$ si $kL=N\pi$. Permet de calculer l'énergie totale d'un mode : $E=\tfrac14\mu\omega^2A^2L$.
>
> **Analyse dimensionnelle et proportionnalités**
>
> $[Z]=\mathrm{kg\,s^{-1}}$ ; $\langle\mathcal P\rangle\propto\omega^2a^2\sqrt F$. Doubler $\omega$ ou $a$ multiplie par $4$ ; doubler $F$ multiplie par $\sqrt2$.




> [!tip]- 💡 Coup de pouce
> **Stratégie générale**
>
> Pour chaque question, écrire $\partial_x y$ et $\partial_t y$ en fonction de la variable $u=x-ct$ (ou de la phase), puis remplacer dans $e$ ou dans $\mathcal{P}=-F\,\partial_x y\,\partial_t y$.



**q1.** Montrer, à l'aide de l'équation de d'Alembert, que l'énergie vérifie l'équation de conservation locale
$$\frac{\partial e}{\partial t}+\frac{\partial\mathcal{P}}{\partial x}=0,\qquad\text{avec}\qquad\mathcal{P}(x,t)=-F\,\frac{\partial y}{\partial x}\,\frac{\partial y}{\partial t}.$$
Donner la signification physique de $\mathcal{P}$ (indication : puissance d'une force).


> [!tip]- 💡 Coup de pouce
> **Dériver $e$**
>
> Calculer $\partial_t e$ et $\partial_x\mathcal{P}$ séparément, puis regrouper les termes en $\partial_t y$.




> [!success]- ✅ Correction
> **Résultat**
>
> $\partial_t e+\partial_x\mathcal{P}=\partial_t y\,(\mu\,\partial_t^2y-F\,\partial_x^2y)=0$. $\mathcal{P}$ est la puissance que la partie gauche fournit à la partie droite à travers la section $x$.




> [!example]- 📝 Solution détaillée
> **Démonstration**
>
> $$\partial_t e=\mu\,\partial_t y\,\partial_t^2y+F\,\partial_x y\,\partial_x\partial_t y,$$
> $$\partial_x\mathcal{P}=-F\,\partial_x^2y\,\partial_t y-F\,\partial_x y\,\partial_x\partial_t y.$$
> En additionnant, les termes en $F\,\partial_x y\,\partial_x\partial_t y$ se compensent :
> $$\partial_t e+\partial_x\mathcal{P}=\partial_t y\left(\mu\,\partial_t^2 y-F\,\partial_x^2 y\right)=0$$
> car $\mu\,\partial_t^2 y=F\,\partial_x^2 y$ (équation d'onde).
>
> **Signification :** la force transversale exercée par la gauche sur la droite en $x$ est $-F\,\partial_x y$ ; la vitesse du point d'application est $\partial_t y$. La puissance de cette force est donc $-F\,\partial_x y\,\partial_t y=\mathcal{P}$ : c'est le flux d'énergie qui traverse la section $x$ de gauche à droite.



**q2.** Onde progressive $y=f(x-ct)$. Montrer que $e=F f'^2$, puis que $\mathcal{P}=c\,e$. En déduire que $\mathcal{P}=Z\left(\partial_t y\right)^2$ avec $Z=\sqrt{F\mu}$. Que devient ce résultat pour une onde régressive $y=g(x+ct)$ ?


> [!tip]- 💡 Coup de pouce
> **Dérivées**
>
> $\partial_x y=f'$ et $\partial_t y=-c\,f'$. N'oubliez pas $\mu c^2=F$.




> [!success]- ✅ Correction
> **Résultat**
>
> $e=Ff'^2$, $\mathcal{P}=Fc\,f'^2=c\,e$, et comme $F/c=\sqrt{F\mu}=Z$ : $\mathcal{P}=Z(\partial_t y)^2>0$. Pour $g(x+ct)$ : $\mathcal{P}=-Z(\partial_t y)^2<0$ (énergie transportée vers les $x$ décroissants).




> [!example]- 📝 Solution détaillée
> **Calcul**
>
> $$e=\frac{1}{2}\mu c^2f'^2+\frac{1}{2}Ff'^2=\frac{1}{2}Ff'^2+\frac{1}{2}Ff'^2=Ff'^2$$
> $$\mathcal{P}=-F\,f'\cdot(-c\,f')=F\,c\,f'^2=c\,e.$$
> Comme $\partial_t y=-cf'$, on a $f'^2=(\partial_t y)^2/c^2$, donc $\mathcal{P}=\dfrac{F}{c}(\partial_t y)^2=Z(\partial_t y)^2$ car $\dfrac{F}{c}=\dfrac{F}{\sqrt{F/\mu}}=\sqrt{F\mu}$.
>
> Dans une onde progressive, énergies cinétique et potentielle sont égales en chaque point, et l'énergie est transportée à la célérité $c$. Pour l'onde régressive $\partial_x y=g'$ et $\partial_t y=+c\,g'$, donc $\mathcal{P}=-Fc\,g'^2=-Z(\partial_t y)^2$.
>
> **Interprétation de $Z$ :** $Z$ est le rapport (au signe près) entre la force transversale $-F\partial_x y$ et la vitesse transversale $\partial_t y$ : $-F\,\partial_x y=Z\,\partial_t y$ pour une onde progressive. Sa dimension est $[Z]=\text{kg}\cdot\text{s}^{-1}$.



**q3.** Onde sinusoïdale progressive $y=a\cos(kx-\omega t)$. Calculer la puissance moyenne $\langle\mathcal{P}\rangle$ et la densité linéique d'énergie moyenne $\langle e\rangle$. Application numérique avec les données de l'exercice 3 : $\mu=0{,}12\ \text{kg}\cdot\text{m}^{-1}$, $F=20\ \text{N}$, $a=2\ \text{mm}$, $\lambda=0{,}25\ \text{m}$.


> [!tip]- 💡 Coup de pouce
> **Moyenne**
>
> $\langle\sin^2\rangle=\tfrac{1}{2}$ sur une période. Calculer $\omega=2\pi c/\lambda$.




> [!success]- ✅ Correction
> **Résultat**
>
> $\langle\mathcal{P}\rangle=\tfrac{1}{2}Z\omega^2a^2$ et $\langle e\rangle=\tfrac{1}{2}\mu\omega^2a^2$, avec $\langle\mathcal{P}\rangle=c\langle e\rangle$. Ici $c\approx12{,}9\ \text{m/s}$, $Z\approx1{,}55\ \text{kg/s}$, $\omega\approx324\ \text{rad/s}$, $\langle e\rangle\approx0{,}025\ \text{J/m}$ et $\langle\mathcal{P}\rangle\approx0{,}33\ \text{W}$.




> [!example]- 📝 Solution détaillée
> **Calcul**
>
> $\partial_t y=a\omega\sin(kx-\omega t)$ donc, avec $\mathcal{P}=Z(\partial_t y)^2$ :
> $$\langle\mathcal{P}\rangle=Z\,a^2\omega^2\,\langle\sin^2\rangle=\frac{1}{2}Z\,\omega^2a^2.$$
> De même $e=Ff'^2=F k^2a^2\sin^2(kx-\omega t)$, donc
> $$\langle e\rangle=\frac{1}{2}Fk^2a^2=\frac{1}{2}\mu\omega^2a^2\quad(\text{car }F k^2=\mu\omega^2).$$
> Application numérique : $c=\sqrt{20/0{,}12}\approx12{,}91\ \text{m/s}$, $\omega=\dfrac{2\pi c}{\lambda}\approx324{,}5\ \text{rad/s}$, $Z=\sqrt{20\times0{,}12}\approx1{,}549\ \text{kg/s}$.
> $$\langle\mathcal{P}\rangle=\tfrac{1}{2}\times1{,}549\times(324{,}5)^2\times(2\times10^{-3})^2\approx0{,}326\ \text{W}\qquad\langle e\rangle\approx0{,}0253\ \text{J/m}.$$
> Vérification : $c\langle e\rangle=12{,}91\times0{,}0253\approx0{,}326\ \text{W}$.



**q4.** Comment varie $\langle\mathcal{P}\rangle$ si (i) on double la fréquence à amplitude $a$ constante ; (ii) on double la tension $F$ à $\mu$, $\omega$ et $a$ constants ; (iii) on double l'amplitude ?


> [!success]- ✅ Correction
> **Résultat**
>
> (i) $\times4$ ; (ii) $\times\sqrt{2}$ (car $Z\propto\sqrt{F}$) ; (iii) $\times4$.




> [!example]- 📝 Solution détaillée
> **Justification**
>
> $\langle\mathcal{P}\rangle=\tfrac{1}{2}\sqrt{F\mu}\,\omega^2a^2$. Elle est proportionnelle à $\omega^2$ (donc à $f^2$), à $a^2$ et à $\sqrt{F}$. Doubler $F$ multiplie donc $\langle\mathcal{P}\rangle$ par $\sqrt{2}$.



**q5.** Onde stationnaire $y=A\sin(kx)\cos(\omega t)$ avec $\omega=ck$. Calculer $\mathcal{P}(x,t)$ et sa moyenne temporelle. Que dire du transport d'énergie ? Calculer ensuite, pour le mode $N$ d'une corde fixée en $x=0$ et $x=L$ ($kL=N\pi$), les énergies cinétique $K(t)$ et potentielle $U(t)$ et leur somme.


> [!tip]- 💡 Coup de pouce
> **Formules trigonométriques**
>
> $\sin kx\cos kx=\tfrac{1}{2}\sin2kx$ et $\int_0^L\sin^2kx\,\mathrm{d}x=\int_0^L\cos^2kx\,\mathrm{d}x=\dfrac{L}{2}$ pour $kL=N\pi$.




> [!success]- ✅ Correction
> **Résultat**
>
> $\mathcal{P}=\dfrac{1}{4}FA^2k\omega\,\sin(2kx)\sin(2\omega t)$, de moyenne nulle : pas de transport net d'énergie. $K=\dfrac{1}{4}\mu\omega^2A^2L\sin^2\omega t$, $U=\dfrac{1}{4}\mu\omega^2A^2L\cos^2\omega t$, $E=K+U=\dfrac{1}{4}\mu\omega^2A^2L$ constante.




> [!example]- 📝 Solution détaillée
> **Calcul**
>
> $\partial_x y=Ak\cos kx\cos\omega t$ et $\partial_t y=-A\omega\sin kx\sin\omega t$, donc
> $$\mathcal{P}=FA^2k\omega\,\sin kx\cos kx\,\sin\omega t\cos\omega t=\frac{1}{4}FA^2k\omega\,\sin(2kx)\,\sin(2\omega t).$$
> Sa moyenne temporelle est nulle en tout point : l'énergie oscille sur place entre énergie cinétique et énergie potentielle sans être transportée.
>
> $$K=\int_0^L\frac{1}{2}\mu A^2\omega^2\sin^2kx\,\sin^2\omega t\,\mathrm{d}x=\frac{1}{4}\mu\omega^2A^2L\,\sin^2\omega t,$$
> $$U=\int_0^L\frac{1}{2}FA^2k^2\cos^2kx\,\cos^2\omega t\,\mathrm{d}x=\frac{1}{4}\mu\omega^2A^2L\,\cos^2\omega t.$$
> Donc $E=K+U=\dfrac{1}{4}\mu\omega^2A^2L$ ne dépend pas du temps. L'énergie cinétique est maximale quand la corde passe par sa position d'équilibre, et l'énergie potentielle maximale quand la corde est à son élongation maximale.



**q6.** Application : la troisième corde de guitare de l'exercice 4 ($\mu=5{,}04\times10^{-4}\ \text{kg/m}$, $L=63\ \text{cm}$, $f_1=147\ \text{Hz}$) vibre sur son fondamental avec une amplitude de $1\ \text{mm}$ au ventre. Calculer son énergie mécanique.


> [!success]- ✅ Correction
> **Résultat**
>
> $E=\tfrac{1}{4}\mu\omega_1^2A^2L\approx6{,}8\times10^{-5}\ \text{J}$ (environ $68\ \mu\text{J}$).




> [!example]- 📝 Solution détaillée
> **Application numérique**
>
> $\omega_1=2\pi\times147\approx923{,}6\ \text{rad/s}$.
> $$E=\frac{1}{4}\times5{,}04\times10^{-4}\times(923{,}6)^2\times(10^{-3})^2\times0{,}63\approx6{,}8\times10^{-5}\ \text{J}.$$
> Cette énergie est très faible : une corde pincée seule est un mauvais radiateur acoustique, d'où la caisse de résonance.




> [!note]- 🔗 Liens avec d'autres disciplines
> **Électromagnétisme**
>
> Le théorème de Poynting, $\partial_t u+\nabla\cdot\vec S=0$, est exactement la même équation avec $u$ la densité d'énergie électromagnétique et $\vec S$ le flux d'énergie.
>
> **Électricité (lignes et impédance)**
>
> Un câble coaxial a une impédance caractéristique $Z_0=\sqrt{L/C}$ qui relie tension et courant d'une onde progressive, comme $Z=\sqrt{F\mu}$ relie force et vitesse. L'adaptation d'impédance évite les réflexions.
>
> **Acoustique**
>
> L'impédance acoustique $Z=\rho c$ relie pression et vitesse ; l'intensité sonore est $I=\tfrac12Z\,v_m^2$ et se mesure en décibels.
>
> **Mécanique analytique**
>
> $e$ dérive du lagrangien $\mathcal L=\tfrac12\mu\dot y^2-\tfrac12Fy'^2$ ; l'équation d'onde est l'équation d'Euler-Lagrange et la conservation de l'énergie est le théorème de Noether pour l'invariance par translation dans le temps.
>
> **Lutherie**
>
> L'énergie d'une corde pincée est très faible ($\approx6{,}8\times10^{-5}$ J) : sans caisse de résonance, le son est inaudible à distance.




> [!question]- 🔭 Aller plus loin — Licence : Lagrangien de la corde
> $e$ est l'énergie associée au lagrangien $\mathcal{L}=\frac{1}{2}\mu\dot y^2-\frac{1}{2}Fy'^2$. L'équation d'onde est l'équation d'Euler-Lagrange, et $\partial_t e+\partial_x\mathcal{P}=0$ est le théorème de Noether pour l'invariance par translation dans le temps.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex4-equation-des-cordes-vibrantes-et-onde-progressive|Exercice 4 — Équation des cordes vibrantes et onde progressive]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex10-corde-discrete-chaine-de-masses-dispersion-coupure-et-vitesse-de-groupe|Exercice 10 — Corde discrète (chaîne de masses) : dispersion, coupure et vitesse de groupe]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex11-une-perle-sur-la-corde-reflexion-transmission-et-filtre-passe-bas-mecanique|Exercice 11 — Une perle sur la corde : réflexion, transmission et filtre passe-bas mécanique]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex12-adaptation-d-impedance-lame-quart-d-onde-entre-deux-cordes|Exercice 12 — Adaptation d'impédance : lame quart d'onde entre deux cordes]]


