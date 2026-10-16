---
title: "Exercice 2 — Corde de nylon"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/index|⬅ Retour]] · <a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td1_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_ex1_coup_de_pouce.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_coup_de_pouce)</a> · <a href="/pdfs/td1_ex1_solution_detaillee.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_solution_detaillee)</a> · <a href="/pdfs/td1_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_PhV212_fiche)</a> · <a href="/pdfs/td1_ex1_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_ex1_fiche)</a> · <a href="/pdfs/td1_exs_maison_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant (td1_exs_maison_fiche)</a>

### Exercice 2. Corde de nylon

Une corde de nylon de diamètre $d = 1$ mm est tendue par une force
extérieure de module $F = 50$ N.

<p style="text-align:center"><a href="/figures/td1_ex1_corde_t0.svg" target="_blank" rel="noopener"><img src="/figures/td1_ex1_corde_t0.svg" alt="Allure de la corde à $t=0$." loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>

<p style="text-align:center"><a href="/animations/anim_corde_onde/animation.gif" target="_blank" rel="noopener"><img src="/animations/anim_corde_onde/animation.gif" alt="animation" loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>

[🎞️ Voir en .mp4](/animations/anim_corde_onde/animation.mp4)

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


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex3-partie-c-masse-lineique-de-la-corde-par-deux-methodes-color-blue-part-c-linear-mass-density-of-the-string-by-two-methods|Exercice 3 — Partie C — Masse linéique de la corde par deux méthodes {\color{blue}(Part C — Linear mass density of the string by two methods)}]] · [[physique/ipsa-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex3-celerite-d-une-onde-sur-une-corde-homogene|Exercice 3 — Célérité d’une onde sur une corde homogène]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex2-partie-b-effet-de-la-tension-sur-les-modes-propres-d-une-corde-color-blue-part-b-effect-of-tension-on-the-normal-modes-of-a-string|Exercice 2 — Partie B — Effet de la tension sur les modes propres d'une corde {\color{blue}(Part B — Effect of tension on the normal modes of a string)}]] · [[physique/ipsa-ondes/TP/chap-1-equation-d-onde-de-d-alembert-corde-vibrante-voir-td1-ex-4-5-et-6/tp-ondes-stationnaires-modes-propres-d-un-ressort-helicoidal-et-d-une-corde-vibrante-color-blue-standing-waves-normal-modes-of-a-helical-spring-and-a-vibrating-string/ex5-synthese-scientifique-du-tp-color-blue-scientific-summary-of-the-lab|Exercice 5 — Synthèse scientifique du TP {\color{blue}(Scientific summary of the lab)}]] · [[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/ex1-ondes-sur-un-ressort-long-slinky-filmees-au-ralenti-impulsions-reflexions-et-modes-propres|Exercice 1 — Ondes sur un ressort long (Slinky) filmées au ralenti : impulsions, réflexions et modes propres]]

