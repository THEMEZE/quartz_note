---
title: "Exercice 2 — Corde de nylon"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td1_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_ex1_coup_de_pouce.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_coup_de_pouce)</a> · <a href="/pdfs/td1_ex1_solution_detaillee.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_solution_detaillee)</a>

### Exercice 2. Corde de nylon

*⭐ Indispensable · Difficulté ●●○○○ · ⏱ 20 min · Type : Application directe du cours*

Une corde de nylon de diamètre $d = 1$ mm est tendue par une force
extérieure de module $F = 50$ N.

<p style="text-align:center"><a href="/figures/td1_ex1_corde_t0.svg" target="_blank" rel="noopener"><img src="/figures/td1_ex1_corde_t0.svg" alt="Allure de la corde à $t=0$." loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>

<p style="text-align:center"><a href="/animations/anim_corde_onde/animation.gif" target="_blank" rel="noopener"><img src="/animations/anim_corde_onde/animation.gif" alt="animation" loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>

[🎞️ Voir en .mp4](/animations/anim_corde_onde/animation.mp4)


> [!question]- 🪝 Accroche
> **Pourquoi une corde plus fine ou plus tendue sonne-t-elle plus aigu ?**
>
> *Durée de l'introduction : 5 min, avant de lire l'énoncé*
>
> *Sur une guitare, les cordes graves sont grosses et lourdes, les aiguës fines. Si l'on tend davantage une corde, la note monte. Pouvez-vous prévoir, **sans calcul**, comment la vitesse d'une onde sur la corde varie avec la tension et avec le diamètre ? Et la vitesse de l'onde est-elle la vitesse à laquelle bouge la corde ?*
>
> **Idée clé : la célérité ne dépend que du milieu.** Sur une corde tendue, $c=\sqrt{F/\mu}$ avec $\mu=\rho S$ la masse linéique : plus la tension est grande, plus l'onde est rapide ; plus la corde est lourde, plus elle est lente. Une onde sinusoïdale progressive s'écrit
> $$y(x,t)=a\cos(kx-\omega t+\phi),\qquad k=\frac{2\pi}{\lambda},\ \ \omega=\frac{2\pi}{T},\ \ c=\frac\lambda T=\frac\omega k .$$
> Il ne faut pas confondre la **célérité** $c$ de l'onde (le motif qui avance) et la **vitesse transversale** $\partial_t y$ d'un point de la corde (qui monte et descend).




> [!note]- 🧮 Outils mathématiques
> **Aire d'un disque et masse linéique**
>
> $S=\pi d^2/4$ et $\mu=\rho S$. Penser à convertir : $1~\text{mm}=10^{-3}$ m, d'où $S=\pi(10^{-3})^2/4\approx7{,}85\times10^{-7}$ m$^2$. Maîtriser les puissances de dix évite les erreurs d'unités.
>
> **Analyse dimensionnelle**
>
> $[F/\mu]=\dfrac{\mathrm{kg\,m\,s^{-2}}}{\mathrm{kg\,m^{-1}}}=\mathrm{m^2\,s^{-2}}$ : la racine carrée est bien une vitesse. L'analyse dimensionnelle permet de **deviner** $c\propto\sqrt{F/\mu}$ à une constante sans dimension près.
>
> **Relations entre grandeurs ondulatoires**
>
> $k=2\pi/\lambda$, $\omega=2\pi/T=2\pi f$, $c=\lambda f=\omega/k$. Une période temporelle $T$ correspond à un déphasage de $2\pi$ ; une longueur d'onde $\lambda$ à un décalage spatial de $2\pi$.
>
> **Phase, degrés et radians**
>
> Une variation de phase de $60^\circ=\pi/3$ rad correspond à $\dfrac{60}{360}=\dfrac16$ de période : $\Delta t=T/6$. Règle de trois sur les angles.
>
> **Translation de graphe : $y(x,t+\Delta t)=y(x-c\Delta t,t)$**
>
> Entre $t$ et $t+T/8$ le profil se décale de $c\,T/8=\lambda/8$ vers les $x$ croissants. Même idée qu'en cinématique : un décalage $\Delta t$ correspond à un déplacement $c\,\Delta t$.
>
> **Dérivée partielle d'un cosinus**
>
> $v_y=\partial_t y=a\omega\sin(kx-\omega t+\phi)$, de valeur maximale $a\omega$. Un point où $y=0$ (passage par l'équilibre) est un point où $|v_y|=a\omega$ est maximale, car $\cos^2+\sin^2=1$.



**q1.** Calculer la masse linéique $\mu$ de la corde, sachant que la masse
volumique du nylon est de $950$ kg/m$^3$. Calculer la vitesse de
propagation $c$ des ondes transversales sur cette corde.


> [!tip]- 💡 Coup de pouce
> **Indication géométrique**
>
> $\mu = \rho\,S$ avec $S=\pi d^2/4$ la section de la corde.
>
> **Relation dynamique**
>
> La vitesse des ondes transverses sur une corde tendue est $c=\sqrt{F/\mu}$. (relation de d'Alembert, vue en cours).




> [!question]- 🔭 Aller plus loin — Lycée : Analogie musicale
> Analogie avec les cordes de guitare : plus une corde est tendue ou
> fine, plus la note produite est aiguë (fréquence plus grande).




> [!question]- 🔭 Aller plus loin — CPGE : Analyse dimensionnelle
> Retrouver $c=\sqrt{F/\mu}$ par analyse dimensionnelle
> ($[F]=$ kg·m·s$^{-2}$, $[\mu]=$ kg·m$^{-1}$).




> [!question]- 🔭 Aller plus loin — Licence : Démonstration PFD
> Redémontrer $c=\sqrt{F/\mu}$ à partir du PFD appliqué à un élément de corde $[x,x+dx]$ (cf. exercice 3).




> [!question]- 🔭 Aller plus loin — Master : Modèle de dispersion
> Discuter la limite du modèle de corde idéale (sans raideur de
> flexion) et l'apparition de dispersion pour une corde "raide"
> (câble métallique épais).




> [!success]- ✅ Correction
> **Méthode directe**
>
> $\mu = \rho\,S = \rho\,\dfrac{\pi d^2}{4} \approx 7.46\times10^{-4}\ \text{kg/m}.$
> $c=\sqrt{F/\mu}=\sqrt{50/7.46\times10^{-4}}\approx 259\ \text{m/s}.$




> [!example]- 📝 Solution détaillée
> **Rédaction pas à pas**
>
> On part de $\mu=\rho S$ avec $S=\pi d^2/4$ la section circulaire du fil,
> où $\rho=950$ kg/m$^3$ est la donnée de l'énoncé
> .
> Application numérique : $S=\pi(10^{-3})^2/4=7.85\times10^{-7}$ m$^2$, donc
> $\mu=950\times7.85\times10^{-7}\approx7.46\times10^{-4}$ kg/m.
> La relation de d'Alembert, démontrée en cours à partir du PFD appliqué à
> un élément de corde, donne $c=\sqrt{F/\mu}$. Application numérique :
> $c=\sqrt{50/7.46\times10^{-4}}\approx259$ m/s. On vérifie que l'unité
> est bien homogène à une vitesse : $[\sqrt{F/\mu}]=\sqrt{\text{N/(kg/m)}}=\text{m/s}$.



On suppose qu'une onde plane transversale se propage sur la corde dans
le sens des $x$ croissants. À l'instant $t=0$, la corde a l'allure
donnée sur la figure ci-dessus.


**2.**

  **a)** Quelle est la longueur d'onde $\lambda$ de l'onde se propageant sur la corde ?


> [!tip]- 💡 Coup de pouce
> **Graphique**
>
> Lisez directement $\lambda$ sur la figure (distance entre deux motifs identiques).




> [!success]- ✅ Correction
> **Lecture**
>
> $\lambda = 4\text{cm}$ m (lecture graphique directe sur la figure \ref{fig:cordet0}).




> [!example]- 📝 Solution détaillée
> **Lecture**
>
> $\lambda = 4\text{cm}$ m (lecture graphique directe sur la figure \ref{fig:cordet0}).
>
> <p style="text-align:center"><a href="/figures/td1_ex1_corde_t0_lambda.svg" target="_blank" rel="noopener"><img src="/figures/td1_ex1_corde_t0_lambda.svg" alt="Allure de la corde à $t=0$." loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>



  **b)** Quelle est sa période temporelle $T$ ?


> [!tip]- 💡 Coup de pouce
> **Relation célérité-période**
>
> Utilisez $c=\lambda/T$ avec la célérité trouvée en 1.




> [!success]- ✅ Correction
> **Calcul de T**
>
> $T=\lambda/c\approx 1/259\approx 1.55\times10^{-4}$ s.




> [!example]- 📝 Solution détaillée
> **Calcul de T**
>
> $T=\lambda/c\approx 1/259\approx 1.55\times10^{-4}$ s.



  **c)** Quel est le temps nécessaire pour que la phase en un point donné varie de $60°$ ?


> [!tip]- 💡 Coup de pouce
> **Proportionnalité de phase**
>
> Une variation de phase de $2\pi$ (ou $360^\circ$) correspond à une durée $T$.




> [!success]- ✅ Correction
> **Calcul de durée**
>
> $\Delta t = \dfrac{60}{360}T \approx 2.6\times10^{-5}$ s.




> [!example]- 📝 Solution détaillée
> **Calcul de durée**
>
> $\Delta t = \dfrac{60}{360}T \approx 2.6\times10^{-5}$ s.



  **d)** Dessiner l'allure de la corde à l'instant $t=T/8$.


> [!tip]- 💡 Coup de pouce
> **Décalage spatial**
>
> Un décalage temporel $T/8$ correspond à un décalage spatial de $\lambda/8$ dans le sens de propagation.




> [!success]- ✅ Correction
> **Interpretation graphique**
>
> La corde de la figure 1 est translatée de $\lambda/8$ vers les $x$ croissants.




> [!example]- 📝 Solution détaillée
> **Interpretation graphique**
>
> La corde de la figure 1 est translatée de $\lambda/8$ vers les $x$ croissants.
>
> <p style="text-align:center"><a href="/figures/td1_ex1_corde_t_t8.svg" target="_blank" rel="noopener"><img src="/figures/td1_ex1_corde_t_t8.svg" alt="Allure de la corde à $t = T/8$." loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>



  **e)** Donner la loi $y(x,t)$.


> [!tip]- 💡 Coup de pouce
> **Forme générale**
>
> Une onde plane progressive sinusoïdale se propageant vers les $x$ croissants s'écrit $y(x,t)=a\cos(kx-\omega t+\phi)$.




> [!success]- ✅ Correction
> **Expression**
>
> $y(x,t) = a\cos\!\big(k(x-ct)+\phi\big)$ avec $k=2\pi/\lambda$, $a$ et $\phi$ fixés par la figure 1.




> [!example]- 📝 Solution détaillée
> **Expression**
>
> $y(x,t) = a\cos\!\big(k(x-ct)+\phi\big)$ avec $k=2\pi/\lambda$, $a$ et $\phi$ fixés par la figure 1.



  **f)** Quelle est la vitesse du point $P$ de la corde à l'instant $t=0$ ?


> [!tip]- 💡 Coup de pouce
> **Vitesse particulaire vs célérité**
>
> La vitesse transversale d'un point est $\partial y/\partial t$, à ne pas confondre avec la célérité $c$ de l'onde.




> [!success]- ✅ Correction
> **Derivation temporel**
>
> $v_y(x_P,0) = \partial_t y(x_P,0) = a\,\omega\sin(kx_P+\phi)$, lue sur la pente de la courbe en $x_P$.




> [!example]- 📝 Solution détaillée
> **Derivation temporel**
>
> $v_y(x_P,0) = \partial_t y(x_P,0) = a\,\omega\sin(kx_P+\phi)$, lue sur la pente de la courbe en $x_P$.\\
>
> On note $\Phi(x, t) = k(x-ct)+\phi$ la phase. Or $y(x_P,0) \propto \cos(\Phi(x_p, t=0)) = 0$ donc $v_y(x_P,0) \propto \sin(\Phi(x_p, t=0)) = \pm 1$. Donc $v_y(x_P,0)  = \pm \, a\,\omega$.




> [!note]- 🔗 Liens avec d'autres disciplines
> **Musique et lutherie**
>
> La hauteur d'une note est liée à la fréquence $f_1=c/(2L)$ : on accorde une guitare en changeant la tension $F$ (clé d'accord) et on choisit des cordes de $\mu$ différents (cordes filées pour les graves).
>
> **Cinématique**
>
> Décaler un profil de $\lambda/8$ pour $T/8$ revient à un mouvement uniforme de vitesse $c=\lambda/T$ : le motif se comporte comme un mobile.
>
> **Génie civil**
>
> On estime la tension d'un hauban de pont en le faisant vibrer et en mesurant sa fréquence propre : $F=4\mu L^2f_1^2$.
>
> **Électricité et signaux**
>
> Un signal sinusoïdal $a\cos(\omega t+\phi)$ est caractérisé par son amplitude, sa pulsation et sa phase. Le déphasage entre deux points de la corde est le même que le déphasage entre deux tensions alternatives retardées.




> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex3-partie-c-masse-lineique-de-la-corde-par-deux-methodes|Exercice 3 — Partie C — Masse linéique de la corde par deux méthodes]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex3-celerite-d-une-onde-sur-une-corde-homogene|Exercice 3 — Célérité d’une onde sur une corde homogène]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde]] · [[physique/IPSA/ipsa-physique-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante/ex5-synthese-scientifique-du-tp|Exercice 5 — Synthèse scientifique du TP]] · [[physique/IPSA/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex1-ondes-sur-un-ressort-long-slinky-filmees-au-ralenti-impulsions-reflexions-et-modes-propres|Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres]]


