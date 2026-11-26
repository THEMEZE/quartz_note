---
title: "Propagation des ondes mécaniques sur une corde"
tags:
  - td
  - chap-1-equation-d-onde-de-d-alembert-corde-vibrante
---

[[physique/IPSA/ipsa-physique-ondes/index|⬅ Physique des ondes]]


> [!info] ℹ️ Chap. 1 — Équation d’onde de d’Alembert : corde vibrante
> Séance 1



<a href="/pdfs/td1_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé</a> · <a href="/pdfs/td1_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_aides)</a> · <a href="/pdfs/td1_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td1_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td1_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé</a> · <a href="/pdfs/td1_ex1_coup_de_pouce.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_coup_de_pouce)</a> · <a href="/pdfs/td1_ex1_solution_detaillee.pdf" target="_blank" rel="noopener">📄 PDF (td1_ex1_solution_detaillee)</a>


> [!question]- 🪝 Accroche
> **Une corde de guitare, un pont suspendu, un câble coaxial : une seule équation ?**
>
> *Durée de l'introduction : 5 à 8 min, avant les exercices*
>
> *Pourquoi une corde plus fine ou plus tendue sonne-t-elle plus aigu ? Pourquoi une impulsion se renverse-t-elle quand elle se réfléchit sur une extrémité fixe, mais pas sur une extrémité libre ? Comment un vibreur peut-il faire apparaître de beaux « fuseaux » à certaines fréquences seulement ? Et pourquoi une corde de piano, pourtant décrite par la même équation, est-elle accordée « faux » ?*
>
> **Idée clé : l'équation de d'Alembert résume la dynamique d'un milieu élastique linéaire.** Une perturbation se propage à la vitesse $c=\sqrt{F/\mu}$ fixée par le milieu :
> $$\partial_x^2y=\frac1{c^2}\,\partial_t^2y,\qquad y=f(x-ct)+g(x+ct).$$
> Quand la corde est limitée par des extrémités, les ondes se réfléchissent et se superposent : les **conditions aux limites** sélectionnent des fréquences discrètes (modes propres, $f_n=nc/2L$). Quand une source impose une fréquence, la corde répond à cette fréquence avec un profil fixé par les conditions aux limites : c'est le **régime forcé**, avec résonance près des fréquences propres. Enfin, les écarts à l'idéal (raideur, amortissement, charge locale, tension variable) **modifient la relation de dispersion** $\omega(k)$ ou les conditions aux limites, et c'est ce qui rend les instruments réels intéressants.



> [!abstract]- 🧠 À savoir avant
> **Dérivées partielles et équations aux dérivées partielles**
>
> Savoir dériver une fonction de deux variables $y(x,t)$ par rapport à $x$ ou à $t$ ($\partial_xy$, $\partial_t^2y$), dériver une fonction composée ($\partial_xf(x-ct)=f'$, $\partial_tf(x-ct)=-cf'$) et reconnaître qu'une EDP linéaire se résout par superposition.
>
> **Mécanique du point : deuxième loi de Newton**
>
> Principe fondamental de la dynamique appliqué à un élément de corde $[x,x+\mathrm dx]$ de masse $\mu\,\mathrm dx$ soumis aux tensions en $x$ et en $x+\mathrm dx$ ; décomposition d'une force sur deux axes ; approximation des petits angles $\sin\alpha\simeq\tan\alpha\simeq\alpha$.
>
> **Trigonométrie et fonctions sinusoïdales**
>
> $\cos(kx-\omega t+\phi)$, périodes spatiale $\lambda=2\pi/k$ et temporelle $T=2\pi/\omega$, formules d'addition ($\sin(a-b)$, $\cos a\cos b$, produit en somme), $\cos^2+\sin^2=1$, déphasage et conversion degrés $\leftrightarrow$ radians.
>
> **Nombres complexes et notation complexe**
>
> Écrire un signal sinusoïdal comme partie réelle de $\underline a\,\mathrm e^{j\omega t}$, dériver ($\partial_t\to j\omega$), calculer module et argument, notation $\underline k=k'-jk''$ (utile pour l'amortissement). Les exercices 5 et 14 utilisent systématiquement $j$ ($j^2=-1$).
>
> **Équations différentielles linéaires à coefficients constants**
>
> Résoudre $y''+k^2y=0$ ($\cos$, $\sin$), $y''-\kappa^2y=0$ ($\mathrm e^{\pm\kappa x}$, $\cosh$, $\sinh$), $\ddot\theta+\gamma\dot\theta+\omega_0^2\theta=0$ (équation caractéristique, régime pseudo-périodique), avec des conditions aux limites ou initiales.
>
> **Séries de Fourier, orthogonalité des modes**
>
> $\displaystyle\int_0^L\sin\frac{n\pi x}L\sin\frac{m\pi x}L\,\mathrm dx=\frac L2\,\delta_{nm}$ ; décomposition d'une fonction en série de sinus et calcul des coefficients par projection.
>
> **Analyse dimensionnelle et ordres de grandeur**
>
> $[F]=\mathrm{kg\,m\,s^{-2}}$, $[\mu]=\mathrm{kg\,m^{-1}}$, $[c]=\mathrm{m\,s^{-1}}$ ; ordres de grandeur : corde de guitare $c\sim100$--$400$ m/s, fréquences $\sim100$--$1000$ Hz ; câble de pont $c\sim100$ m/s, $f\sim1$ Hz.



> [!info]- 🎯 Ce que tu sauras faire
> **Établir et interpréter l'équation de d'Alembert**
>
> Savoir appliquer le principe fondamental à un élément de corde, utiliser l'approximation des petits angles, obtenir $\partial_x^2y=\dfrac1{c^2}\partial_t^2y$ avec $c=\sqrt{F/\mu}$ et en déduire que la célérité ne dépend que du **milieu**, pas de l'onde.
>
> **Manipuler les solutions de l'équation d'onde**
>
> Reconnaître et écrire des ondes progressives $f(x\mp ct)$ et sinusoïdales $a\cos(kx-\omega t+\phi)$ ; relier $\lambda$, $T$, $k$, $\omega$, $c$ ; distinguer la **célérité** de l'onde de la **vitesse transversale** d'un point $\partial_ty$ ; dessiner un profil à un instant ultérieur par simple translation.
>
> **Passer de la propagation aux modes propres**
>
> Traduire des conditions aux limites (extrémité fixe, libre, masse, vibreur) en conditions sur $y$ ou $\partial_xy$ ; obtenir les ondes stationnaires $\sin(kx)\cos(\omega t)$, les fréquences propres $f_n=nc/(2L)$ ou $(2n-1)c/(4L)$ ; calculer les coefficients d'une décomposition modale par projection sur les modes.
>
> **Étudier un régime forcé et une résonance**
>
> Calculer le profil d'une corde excitée par un vibreur (Melde), repérer les résonances et expliquer pourquoi l'amplitude reste finie en présence d'amortissement ($A\sim Qa$) ; connaître le lien entre $Q$, la largeur de résonance et le temps d'extinction.
>
> **Aborder énergie, impédance, réflexion et transmission**
>
> Écrire les densités d'énergie cinétique et potentielle d'une onde, la puissance transportée et l'impédance caractéristique $Z_c=\sqrt{\mu F}$ ; décrire la réflexion et la transmission à une discontinuité de $\mu$, l'adaptation d'impédance (lame quart d'onde).
>
> **Reconnaître les limites du modèle de la corde idéale**
>
> Savoir qu'une corde réelle peut avoir une tension variable (corde pesante), être dispersive (raideur de flexion, chaîne de masses discrètes), être amortie (frottement) ou avoir une charge locale (perle, masse) ; calculer une relation de dispersion $\omega(k)$ et les vitesses de phase et de groupe.
>
> **Compétences transversales**
>
> Faire un schéma soigné (corde, axes, repères de phase), mener des calculs trigonométriques et complexes sans erreur, **valider** (homogénéité, cas limites, ordre de grandeur) et utiliser Python pour tracer des profils, des animations et des spectres.



> [!tip]- 📖 Rappel de cours
> **Équation de d'Alembert pour la corde**
>
> Le PFD sur un élément $[x,x+\mathrm dx]$ pour de petits angles donne
> $$\mu\,\mathrm dx\,\partial_t^2y=F\,\partial_x^2y\,\mathrm dx\ \Longrightarrow\ \boxed{\partial_x^2y-\frac1{c^2}\,\partial_t^2y=0},\qquad c=\sqrt{\frac F\mu}.$$
> La célérité ne dépend que de la tension et de la masse linéique.
>
> **Solutions : ondes progressives et stationnaires**
>
> Solution générale : $y(x,t)=f(x-ct)+g(x+ct)$. Onde sinusoïdale progressive : $y=a\cos(kx-\omega t+\phi)$ avec $k=\dfrac{2\pi}\lambda$, $\omega=\dfrac{2\pi}T$, $c=\dfrac\lambda T=\dfrac\omega k$. Onde stationnaire : $y=A\sin(kx+\varphi)\cos(\omega t+\phi)$ : les points oscillent en phase ou en opposition, avec des **nœuds** fixes et des **ventres**. Vitesse transversale d'un point : $v_y=\partial_ty$ (à ne pas confondre avec $c$).
>
> **Modes propres et conditions aux limites**
>
> Fixe : $y=0$ (nœud). Libre : $\partial_xy=0$ (ventre). Corde fixe-fixe de longueur $L$ : $k_nL=n\pi$, $f_n=n\dfrac c{2L}$ ; fixe-libre : $k_nL=(2n-1)\dfrac\pi2$, $f_n=(2n-1)\dfrac c{4L}$. Toute solution libre est une **superposition de modes** $\sum(A_n\cos\omega_nt+B_n\sin\omega_nt)\sin k_nx$ dont les coefficients se calculent par projection sur les conditions initiales.
>
> **Régime forcé et résonance (Melde)**
>
> Vibreur en $x=0$ : $\underline y(0,t)=a\,\mathrm e^{j\omega t}$ ; extrémité fixée en $x=\ell$ : $\underline Y(x)=a\dfrac{\sin k(\ell-x)}{\sin k\ell}$. Résonance quand $\sin k\ell=0$ ($f=Nc/(2\ell)$). Avec amortissement, l'amplitude reste finie, de l'ordre de $Q\,a$.
>
> **Énergie, puissance, impédance**
>
> Densités linéiques : énergie cinétique $\tfrac12\mu(\partial_ty)^2$, potentielle $\tfrac12F(\partial_xy)^2$ ; puissance transportée par une onde progressive $\mathcal P=Z_c\,(\partial_ty)^2$ avec l'**impédance caractéristique** $Z_c=\sqrt{\mu F}=\mu c$. À l'interface entre deux cordes d'impédances $Z_1$ et $Z_2$ : $r=\dfrac{Z_1-Z_2}{Z_1+Z_2}$, $t=\dfrac{2Z_1}{Z_1+Z_2}$.
>
> **Dispersion, vitesse de phase et de groupe**
>
> Pour un milieu où $\omega$ n'est pas proportionnel à $k$, $v_\varphi=\omega/k$ et $v_g=\mathrm d\omega/\mathrm dk$. Exemples : chaîne de masses ($\omega=2\omega_0|\sin(ka/2)|$), corde raide ($\omega^2=c^2k^2(1+\kappa k^2)$), corde amortie ($\underline k^2=(\omega^2-j\gamma\omega)/c^2$).
>
> **Méthode d'étude d'un problème de corde**
>
> (1) Schéma, repère, conventions, sens de propagation. (2) Écrire l'équation du mouvement (d'Alembert ou modifiée pour la perturbation étudiée). (3) Identifier la nature de la solution cherchée : progressive, stationnaire, modes, régime forcé. (4) Imposer les conditions aux limites et initiales. (5) Calculer les grandeurs demandées ($c$, $f_n$, amplitudes, énergie, $Q$). (6) **Valider** : homogénéité, cas limites, ordre de grandeur.



> [!note]- 🧮 Outils mathématiques
> **Dérivées partielles et dérivée composée**
>
> $\partial_xf(x-ct)=f'$ et $\partial_tf(x-ct)=-cf'$ ; $\partial_x^2$ et $\partial_t^2$ donnent $f''$ et $c^2f''$, d'où $f$ solution de l'équation de d'Alembert. Pour $y=a\cos(kx-\omega t)$ : $\partial_ty=a\omega\sin(kx-\omega t)$ et $\partial_t^2y=-\omega^2y$.
>
> **Notation complexe et relation de dispersion**
>
> $y=\Re[\underline a\,\mathrm e^{j(\omega t-kx)}]$ : $\partial_t\to j\omega$, $\partial_x\to-jk$ ; une EDP linéaire devient une équation algébrique $D(\omega,k)=0$. $v_\varphi=\omega/k$, $v_g=\mathrm d\omega/\mathrm dk$. Avec amortissement, $k=k'-jk''$ et l'amplitude décroît en $\mathrm e^{-k''x}$.
>
> **Trigonométrie : produits, sommes, angles complexes**
>
> $\sin(a-b)=\sin a\cos b-\cos a\sin b$ ; $\cos a\cos b=\tfrac12[\cos(a+b)+\cos(a-b)]$ ; $\sin(a-jb)=\sin a\cosh b-j\cos a\sinh b$ ; $|\sin(a-jb)|^2=\sin^2a+\sinh^2b$ ; $1-\cos a=2\sin^2\tfrac a2$ (chaîne de masses).
>
> **Séries de Fourier en sinus et orthogonalité**
>
> $y_0(x)=\sum b_n\sin\dfrac{n\pi x}L\Rightarrow b_n=\dfrac2L\displaystyle\int_0^Ly_0\sin\dfrac{n\pi x}L\,\mathrm dx$. Pour un profil à pente discontinue, $b_n\propto1/n^2$ ; pour une vitesse initiale concentrée, $b_n\propto1/n$. $\displaystyle\sum_{n\ge1}\dfrac{\sin^2n\theta}{n^2}=\dfrac{\theta(\pi-\theta)}2$ pour $0\le\theta\le\pi$.
>
> **Équations transcendantes et résolution graphique**
>
> Pour $u\tan u=\varepsilon$ : chercher les intersections de $\tan u$ et de $\varepsilon/u$ ; une solution par intervalle ; développements limités autour de $0$ ($\tan u\simeq u+u^3/3$) et de $n\pi$ ($\tan(n\pi+\delta)\simeq\delta$).
>
> **Équation caractéristique et régimes d'un oscillateur**
>
> $\ddot\theta+\gamma\dot\theta+\omega_0^2\theta=0$ : $s=-\dfrac\gamma2\pm j\sqrt{\omega_0^2-\gamma^2/4}$ ; régime pseudo-périodique, critique ou apériodique ; facteur de qualité $Q=\omega_0/\gamma$ ; temps de décroissance de l'amplitude $\tau=2/\gamma$.
>
> **Développements limités et ordres de grandeur**
>
> $\sqrt{1+\varepsilon}\simeq1+\varepsilon/2$, $\sqrt{1-j\varepsilon}\simeq1-j\varepsilon/2$, $\sin\varepsilon\simeq\varepsilon$, $\ln(1+\varepsilon)\simeq\varepsilon$. Conversion en **cents** : $1200\log_2(f'/f)$.
>
> **Énergie et puissance d'une onde**
>
> $e=\tfrac12\mu(\partial_ty)^2+\tfrac12F(\partial_xy)^2$ ; flux $\mathcal P=-F\,\partial_xy\,\partial_ty$ ; pour une onde progressive $y=f(x-ct)$, $\mathcal P=Z_c(\partial_ty)^2$ avec $Z_c=\sqrt{\mu F}$ ; valeur moyenne d'une onde sinusoïdale $\langle\mathcal P\rangle=\tfrac12Z_c\omega^2a^2$.



## Exercices

- [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex1-solutions-de-l-equation-de-d-alembert|Exercice 1 — Solutions de l'équation de d'Alembert]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex2-corde-de-nylon|Exercice 2 — Corde de nylon]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex3-celerite-d-une-onde-sur-une-corde-homogene|Exercice 3 — Célérité d’une onde sur une corde homogène]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex4-equation-des-cordes-vibrantes-et-onde-progressive|Exercice 4 — Équation des cordes vibrantes et onde progressive]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex5-corde-fixee-a-ses-deux-extremites-et-ondes-stationnaires|Exercice 5 — Corde fixée à ses deux extrémités et ondes stationnaires]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex6-experience-de-melde-oscillations-forcees-d-une-corde-resonance|Exercice 6 — Expérience de Melde, oscillations forcées d'une corde, résonance]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex7-ondes-stationnaires-sur-une-corde-avec-une-extremite-libre|Exercice 7 — Ondes stationnaires sur une corde avec une extrémité libre]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex8-energie-et-puissance-d-une-onde-sur-une-corde-impedance-caracteristique|Exercice 8 — Énergie et puissance d'une onde sur une corde : impédance caractéristique]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex9-corde-pesante-suspendue-milieu-inhomogene-bosse-acceleree-et-coup-de-fouet|Exercice 9 — Corde pesante suspendue : milieu inhomogène, bosse accélérée et coup de fouet]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex10-corde-discrete-chaine-de-masses-dispersion-coupure-et-vitesse-de-groupe|Exercice 10 — Corde discrète (chaîne de masses) : dispersion, coupure et vitesse de groupe]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex11-une-perle-sur-la-corde-reflexion-transmission-et-filtre-passe-bas-mecanique|Exercice 11 — Une perle sur la corde : réflexion, transmission et filtre passe-bas mécanique]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex12-adaptation-d-impedance-lame-quart-d-onde-entre-deux-cordes|Exercice 12 — Adaptation d'impédance : lame quart d'onde entre deux cordes]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex13-corde-pincee-timbre-harmoniques-absents-et-energie-des-modes|Exercice 13 — Corde pincée : timbre, harmoniques absents et énergie des modes]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex14-corde-de-piano-raide-dispersion-et-inharmonicite|Exercice 14 — Corde de piano raide : dispersion et inharmonicité]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex15-corde-amortie-attenuation-facteur-de-qualite-et-resonance-de-melde|Exercice 15 — Corde amortie : atténuation, facteur de qualité et résonance de Melde]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex16-masse-en-bout-de-corde-condition-aux-limites-dynamique-et-equation-transcendante|Exercice 16 — Masse en bout de corde : condition aux limites dynamique et équation transcendante]]

## QCM de réveil liés à ce document



> [!question]- QCM — 🌅 Début de cours
> **Sur une corde de guitare, qu'est-ce qui change la hauteur (la fréquence) du son quand on serre la clé d'accordage ?**
>
> <p style="text-align:center"><a href="/animations/anim_corde_onde/animation.gif" target="_blank" rel="noopener"><img src="/animations/anim_corde_onde/animation.gif" alt="animation" loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>
>
> - On augmente la tension F de la corde
> - On change la couleur de la corde
> - Je ne sais pas encore
>
> *Réponds en direct sur <a href="/qcm/physique-ondes-ipsa/" target="_blank" rel="noopener">l'appli QCM</a> (QR code affiché en cours).*




> [!question]- QCM — 🔄 Milieu de cours
> **Sur une corde fixée à ses deux extrémités, en un noeud de vibration, l'amplitude du mouvement est...**
>
> <p style="text-align:center"><a href="/animations/anim_corde_stationnaire/animation.gif" target="_blank" rel="noopener"><img src="/animations/anim_corde_stationnaire/animation.gif" alt="animation" loading="lazy" style="background:#fff;padding:10px;border-radius:10px;max-width:100%;height:auto"></a></p>
>
> - Maximale
> - Toujours nulle
> - Ca dépend du mode N
> - Je ne sais pas encore
>
> *Réponds en direct sur <a href="/qcm/physique-ondes-ipsa/" target="_blank" rel="noopener">l'appli QCM</a> (QR code affiché en cours).*
>
> En lien avec [[physique/IPSA/ipsa-physique-ondes/TD/chap-1-equation-d-onde-de-d-alembert-corde-vibrante/propagation-des-ondes-mecaniques-sur-une-corde/ex4-equation-des-cordes-vibrantes-et-onde-progressive|cet exercice]].




> [!question]- QCM — 🌇 Fin de cours
> **Si on double la tension F d'une corde (sans rien changer d'autre), la célérité c des ondes est multipliée par...**
>
> - 2
> - sqrt(2) ≈ 1.41
> - 4
> - Je ne sais pas encore
>
> *Réponds en direct sur <a href="/qcm/physique-ondes-ipsa/" target="_blank" rel="noopener">l'appli QCM</a> (QR code affiché en cours).*



**S'entraîner librement** (3 question(s) liées à ce document) :

<a href="/qcm/physique-ondes-ipsa/?c=td1_qcm" target="_blank" rel="noopener">Chapitre td1_qcm</a><br><a href="/qcm/physique-ondes-ipsa/?c=td1_qcm" target="_blank" rel="noopener"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNjQiIGhlaWdodD0iMTY0IiBjbGFzcz0ic2Vnbm8iPjxwYXRoIHRyYW5zZm9ybT0ic2NhbGUoNCkiIGNsYXNzPSJxcmxpbmUiIHN0cm9rZT0iIzE2MzIzZiIgZD0iTTIgMi41aDdtMSAwaDRtMiAwaDNtMSAwaDJtNCAwaDJtMSAwaDFtMiAwaDdtLTM3IDFoMW01IDBoMW05IDBoM20xIDBoMm0yIDBoMm0yIDBoMW0xIDBoMW01IDBoMW0tMzcgMWgxbTEgMGgzbTEgMGgxbTMgMGgxbTIgMGgzbTEgMGg1bTEgMGgxbTIgMGgxbTEgMGgxbTEgMGgxbTEgMGgzbTEgMGgxbS0zNyAxaDFtMSAwaDNtMSAwaDFtMSAwaDNtMiAwaDFtNCAwaDJtMyAwaDVtMiAwaDFtMSAwaDNtMSAwaDFtLTM3IDFoMW0xIDBoM20xIDBoMW0xIDBoMW00IDBoMW0xIDBoMW0yIDBoMW0yIDBoMW0xIDBoMW0yIDBoM20xIDBoMW0xIDBoM20xIDBoMW0tMzcgMWgxbTUgMGgxbTEgMGgxbTIgMGgxbTEgMGgxbTEgMGgybTEgMGgybTEgMGgybTIgMGgxbTIgMGgxbTEgMGgxbTUgMGgxbS0zNyAxaDdtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDdtLTI5IDFoNm0yIDBoM20zIDBoMm0yIDBoMW0xIDBoMW0tMjkgMWgxbTMgMGgxbTEgMGgzbTEgMGgzbTEgMGgxbTMgMGgybTIgMGgxbTEgMGgxbTQgMGg1bTIgMGgxbS0zNSAxaDFtNSAwaDFtMSAwaDVtMSAwaDJtMSAwaDNtMiAwaDFtMiAwaDJtMyAwaDRtLTM2IDFoNG0yIDBoMm0zIDBoNG0xIDBoM20xIDBoOG0xIDBoMW0xIDBoMW0yIDBoMW0tMzUgMWgxbTIgMGgybTQgMGgybTEgMGgybTMgMGgybTIgMGgxbTEgMGgybTUgMGgzbTEgMGgybS0zNiAxaDJtMiAwaDFtMSAwaDFtMSAwaDFtMiAwaDJtMiAwaDVtMSAwaDRtMiAwaDVtMiAwaDNtLTM3IDFoMW0xIDBoMW0xIDBoMm0xIDBoMW0zIDBoMW0xIDBoMW0xIDBoNG00IDBoMW0xIDBoMW0xIDBoMm0zIDBoMm0tMzQgMWgybTEgMGgybTEgMGgxbTEgMGgxbTEgMGgybTEgMGgzbTIgMGgxbTEgMGg0bTIgMGgxMG0tMzUgMWgybTIgMGgxbTMgMGgxbTEgMGgxbTIgMGgzbTIgMGgzbTIgMGgxbTYgMGgybTEgMGgxbS0zNSAxaDJtNCAwaDFtMiAwaDNtMyAwaDJtMyAwaDFtMyAwaDFtMiAwaDVtMSAwaDRtLTM1IDFoNG0xIDBoMW0xIDBoNG00IDBoM20xIDBoM20xIDBoM20xIDBoMW0xIDBoNW0tMzYgMWgybTMgMGg1bTMgMGgzbTIgMGgybTMgMGgzbTEgMGgxbTIgMGgzbS0zMiAxaDFtMSAwaDNtMSAwaDFtMiAwaDFtMSAwaDFtMSAwaDhtNCAwaDFtMyAwaDFtMyAwaDJtLTM2IDFoMm0xIDBoNG0xIDBoMm0xIDBoMW0yIDBoMW0yIDBoMW0yIDBoM200IDBoMW0xIDBoM20yIDBoMW0tMzIgMWgxbTEgMGgxbTEgMGgybTEgMGgxbTIgMGg0bTMgMGgybTEgMGgxbTEgMGgzbTEgMGgxbTEgMGgybS0zMyAxaDJtMSAwaDJtMSAwaDJtMyAwaDFtMSAwaDNtMSAwaDFtNSAwaDJtMSAwaDJtMSAwaDFtMSAwaDRtLTMzIDFoMW0xIDBoMm00IDBoNW0xIDBoNG0yIDBoM20zIDBoMm0xIDBoMm0xIDBoMW0tMzQgMWgybTMgMGgxbTEgMGgybTEgMGg0bTMgMGgybTIgMGgxbTEgMGgxbTEgMGgxbTIgMGgybTIgMGg0bS0zNyAxaDFtMiAwaDFtMSAwaDFtNCAwaDFtMyAwaDFtMSAwaDFtMiAwaDNtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMiAwaDNtLTMzIDFoNm0xIDBoNW0yIDBoMm0yIDBoMW0yIDBoMm0xIDBoMm0zIDBoMW0xIDBoMW0tMzIgMWgxbTEgMGgxbTIgMGgybTEgMGgxbTIgMGgybTIgMGgxbTMgMGgzbTIgMGgzbTIgMGgxbTIgMGgzbS0zNyAxaDNtMSAwaDFtMSAwaDFtMSAwaDFtMyAwaDZtMSAwaDFtMSAwaDFtMiAwaDFtMyAwaDVtMSAwaDFtMSAwaDFtLTI5IDFoMm0yIDBoMm0xIDBoNG00IDBoMW0xIDBoMW0xIDBoMm0zIDBoMW0yIDBoMW0tMzYgMWg3bTEgMGgxbTEgMGgxbTQgMGgxbTIgMGgxbTIgMGg0bTMgMGgxbTEgMGgxbTEgMGgxbS0zMyAxaDFtNSAwaDFtMiAwaDFtMyAwaDFtMSAwaDJtMiAwaDNtMSAwaDJtMSAwaDFtMSAwaDFtMyAwaDNtLTM1IDFoMW0xIDBoM20xIDBoMW0xIDBoMm0yIDBoMW0yIDBoMm0yIDBoMm0yIDBoMW0xIDBoMW0yIDBoN20xIDBoMW0tMzcgMWgxbTEgMGgzbTEgMGgxbTMgMGg0bTMgMGgzbTEgMGgzbTEgMGgxbTIgMGg0bTEgMGgxbTIgMGgxbS0zNyAxaDFtMSAwaDNtMSAwaDFtMiAwaDVtMSAwaDFtMSAwaDFtMSAwaDFtMyAwaDJtMSAwaDNtMSAwaDFtMiAwaDJtLTM1IDFoMW01IDBoMW0yIDBoMW0xIDBoN20xIDBoNG0xIDBoMW0yIDBoMW0xIDBoMW0yIDBoMW0xIDBoMm0tMzYgMWg3bTEgMGgxbTEgMGgybTEgMGgxbTIgMGgybTIgMGg1bTEgMGgybTEgMGgxbTEgMGgxbTIgMGgzIi8+PC9zdmc+Cg==" width="110" height="110" alt="QR code : Chapitre td1_qcm" style="image-rendering:pixelated"></a>


> [!note]- 🔗 Liens avec d'autres disciplines
> **Musique, acoustique musicale et lutherie**
>
> $f_1=\dfrac1{2L}\sqrt{F/\mu}$ explique l'accord des instruments à cordes (tension, longueur, masse linéique) ; le point de pincement ou de frappe fixe le timbre (exercice 12) ; l'inharmonicité du piano (exercice 13) conduit à l'accord étiré ; les instruments à vent sont l'analogue du cas fixe-libre (exercice 6).
>
> **Électricité, lignes et câbles**
>
> L'équation de d'Alembert est celle d'un câble sans pertes (télégraphistes) avec $c=1/\sqrt{L_\ell C_\ell}$ et $Z_c=\sqrt{L_\ell/C_\ell}$ ; la réflexion sur un circuit ouvert ou fermé est l'analogue de la réflexion sur une extrémité libre ou fixe ; l'adaptation d'impédance par une ligne quart d'onde est celle de l'exercice 11 ; les pertes ohmiques correspondent au frottement de l'exercice 14.
>
> **Optique et ondes électromagnétiques**
>
> Réflexion et transmission à l'interface de deux milieux (en indice, $r=\frac{n_1-n_2}{n_1+n_2}$ à incidence normale), traitements antireflets (couche quart d'onde), cavités Fabry-Pérot (modes propres), dispersion (prisme, fibre optique).
>
> **Mécanique des solides et génie civil**
>
> Haubans de pont, câbles de téléphérique, poutres en flexion (équation d'Euler-Bernoulli, $\omega\propto k^2$), masses accordées (Taipei 101), passerelle du Millennium Bridge (résonance). La mesure de la fréquence propre d'un hauban donne sa tension : $F=4\mu L^2f_1^2$.
>
> **Mécanique quantique et physique du solide**
>
> Les ondes stationnaires sur une corde préfigurent les états stationnaires d'une particule dans un puits (quantification de $k$, $E\propto n^2$) ; la chaîne de masses est le modèle des phonons dans un cristal (relation de dispersion $\omega=2\omega_0|\sin(ka/2)|$, zone de Brillouin).
>
> **Sismologie et géophysique**
>
> Ondes sismiques : réflexion et transmission aux interfaces entre couches ; mesure des retards ; dispersion des ondes de surface ; modes propres de la Terre (« sonnerie » après un séisme majeur).
>
> **Informatique, traitement du signal et synthèse sonore**
>
> Série de Fourier et spectres, algorithme de Karplus-Strong (synthèse de cordes pincées), simulation numérique de l'équation d'onde (différences finies, stabilité CFL), filtrage.



> [!question]- 🔭 Aller plus loin — Lycée : Hauteur d'une note et instruments à cordes
> Comment un guitariste change-t-il la hauteur d'une note ? (tension, longueur vibrante par appui sur la touche, choix de la corde). Mesurer, avec un smartphone et une application de spectre, la fréquence $f_1$ d'une corde et vérifier $f_1=\dfrac1{2L}\sqrt{F/\mu}$.



> [!question]- 🔭 Aller plus loin — CPGE : Simulation numérique de l'équation d'onde
> Discrétiser $\partial_t^2y=c^2\partial_x^2y$ par différences finies ($y_i^{n+1}=2y_i^n-y_i^{n-1}+\sigma^2(y_{i+1}^n-2y_i^n+y_{i-1}^n)$ avec $\sigma=c\Delta t/\Delta x$) ; vérifier la condition de stabilité $\sigma\le1$ (CFL), simuler une corde pincée et comparer à la série de modes de l'exercice 12.



> [!question]- 🔭 Aller plus loin — Licence : Solution de d'Alembert et conditions initiales
> Montrer que, pour $y(x,0)=y_0(x)$ et $\partial_ty(x,0)=v_0(x)$ sur une corde infinie, $y(x,t)=\tfrac12[y_0(x-ct)+y_0(x+ct)]+\dfrac1{2c}\displaystyle\int_{x-ct}^{x+ct}v_0(s)\,\mathrm ds$ ; adapter à la corde finie par prolongement impair $2L$-périodique.



> [!question]- 🔭 Aller plus loin — Licence : Équation des télégraphistes et analogie électrique
> Établir l'équation d'onde pour la tension et le courant dans un câble ($L_\ell$, $C_\ell$ par unité de longueur), montrer que $c=1/\sqrt{L_\ell C_\ell}$ et $Z_c=\sqrt{L_\ell/C_\ell}$, et reprendre l'analogie corde $\leftrightarrow$ câble ($\mu\leftrightarrow L_\ell$, $1/F\leftrightarrow C_\ell$) : réflexion, adaptation d'impédance, ondes stationnaires dans un câble ouvert ou court-circuité.



> [!question]- 🔭 Aller plus loin — Master : Paquets d'ondes et dispersion
> Pour un paquet d'ondes de largeur spectrale $\Delta k$ autour de $k_0$ dans un milieu dispersif $\omega(k)$, montrer que l'enveloppe se déplace à $v_g(k_0)=\omega'(k_0)$ et s'étale avec un coefficient $\omega''(k_0)$ ; appliquer aux ondes sur la chaîne de masses et à la corde raide (chirp après impact).



> [!question]- 🔭 Aller plus loin — Master : Quantification de la corde : phonons
> Écrire l'énergie d'une corde fixée aux deux bouts comme somme d'oscillateurs harmoniques indépendants (un par mode), $E=\sum\tfrac12m_n(\dot q_n^2+\omega_n^2q_n^2)$, et indiquer comment la quantification de ces oscillateurs conduit aux **phonons** ; capacité thermique d'une corde (modèle de Debye à une dimension).


