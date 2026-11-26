---
title: "Propagation des ondes sonores dans un fluide"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/IPSA/ipsa-physique-ondes/index|⬅ Physique des ondes]]


> [!info] ℹ️ Chap. 2 — Ondes acoustiques
> Séance 3



<a href="/pdfs/td2_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_PhV212_enonce)</a> · <a href="/pdfs/td2_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_enonce)</a> · <a href="/pdfs/td2_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_aides)</a> · <a href="/pdfs/td2_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td2_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_PhV212_corrige)</a> · <a href="/pdfs/td2_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_corrige)</a>


> [!question]- 🪝 Accroche
> **Du chant d'une bouteille à l'échographie : un seul formalisme**
>
> *Durée de l'introduction : 10 min, en début de séance*
>
> *Voici cinq situations : (1) on souffle en travers d'une bouteille et elle « chante » ; (2) on entend très mal une voix quand on a la tête sous l'eau ; (3) un échographe exige un gel sur la peau ; (4) une flûte et une clarinette de même longueur n'ont pas la même note ; (5) un sonomètre indique $60$ dB à $1$ m d'une conversation. Qu'ont en commun ces cinq situations ? Quelles sont les **trois grandeurs** qu'il faut connaître pour les comprendre ?*
>
> **Idée clé : trois ingrédients suffisent.** (i) La **célérité** $c=\sqrt{\gamma RT/M}$ : ce qui se propage et à quelle vitesse. (ii) L'**impédance** $Z=\rho_0c$ : ce que l'onde transmet ou réfléchit à une interface (eau, gel, vitre, goulot). (iii) Les **conditions aux limites** : ouvert ou fermé, qui sélectionnent les fréquences propres.
> $$c=\sqrt{\frac{\gamma RT}M},\qquad Z=\rho_0c,\qquad R=\frac{Z_2-Z_1}{Z_1+Z_2},\qquad f_n=\frac{nc}{2L}\ \text{ou}\ \frac{(2n-1)c}{4L}.$$
> Toutes les situations de la séance se ramènent à ces trois ingrédients, avec des habillages différents.



> [!abstract]- 🧠 À savoir avant
> **Les équations de l'acoustique linéaire**
>
> Connaître la démarche du cours : un fluide parfait au repos ($\rho_0$, $P_0$) est traversé par une petite perturbation ($p$, $\rho'$, $\vec v$) ; on linéarise l'équation d'Euler, la conservation de la masse et l'équation d'état, ce qui donne
> $$\rho_0\frac{\partial\vec v}{\partial t}=-\overrightarrow{\mathrm{grad}}\,p,\qquad\frac{\partial\rho'}{\partial t}+\rho_0\,\mathrm{div}\,\vec v=0,\qquad\rho'=\rho_0\chi\,p.$$
> En éliminant, on obtient l'équation de d'Alembert $\Delta p-\dfrac1{c^2}\dfrac{\partial^2p}{\partial t^2}=0$ avec $c^2=\dfrac1{\rho_0\chi}$. Savoir que le déplacement $\vec\Psi$ (avec $\vec v=\partial_t\vec\Psi$) et la vitesse $\vec v$ vérifient la même équation, et que l'écoulement est irrotationnel.
>
> **Ondes planes progressives et notation complexe**
>
> Savoir qu'une onde plane progressive vers $+x$ s'écrit $f(t-x/c)$ ou, en harmonique, $\tilde A\,e^{i(\omega t-kx)}$ avec $k=\omega/c$, que la relation de dispersion est linéaire (milieu non dispersif), et que la partie réelle de la grandeur complexe est la grandeur physique. Retenir la convention $e^{+i\omega t}$ utilisée dans tout le TD : $\partial_t\to i\omega$, $\partial_x\to\mp ik$ pour une onde se propageant vers $\pm x$.
>
> Savoir que les grandeurs quadratiques (énergie, intensité) ne se calculent **pas** avec les produits de grandeurs complexes.
>
> **Thermodynamique du gaz parfait**
>
> Connaître l'équation d'état $PV=nRT$, les capacités calorifiques et le coefficient $\gamma=C_P/C_V$, les lois de Laplace pour une transformation adiabatique réversible, et les compressibilités $\chi_T=1/P$ et $\chi_S=1/(\gamma P)$ (cf. exercice 1).
>
> **Superposition, ondes stationnaires et cordes vibrantes (chapitre 1)**
>
> Savoir construire une onde stationnaire comme somme d'une onde incidente et d'une onde réfléchie, repérer nœuds et ventres, quantifier les fréquences propres par des conditions aux limites, et connaître l'analogie avec les cordes vibrantes (fixe-fixe, fixe-libre).
>
> **Impédance et analogies électriques**
>
> Avoir déjà rencontré la notion d'impédance en électrocinétique ($Z=U/I$, association série/parallèle, circuit $LC$, résonance) : elle est réutilisée dans les exercices 4, 6, 7 et 8.
>
> **Outils mathématiques de base**
>
> Nombres complexes (module, argument, conjugué), trigonométrie ($\cos$, $\sin$, formules d'Euler, formules d'addition), dérivées partielles, résolution de $\ddot\xi+\omega_0^2\xi=0$, logarithmes (décibels), systèmes linéaires $2\times2$ et développements limités.



> [!info]- 🎯 Ce que tu sauras faire
> **Relier le modèle physique à une prédiction quantitative et la confronter à l'expérience**
>
> Savoir mener une démarche complète : choisir un modèle (isotherme ou isentropique, tube ouvert ou fermé, lame mince ou épaisse), en tirer une prédiction chiffrée, la comparer à une mesure (vitesse du son, fréquence d'une bouteille, absorption d'un matériau) et, s'il y a désaccord, remettre en cause l'hypothèse plutôt que le calcul.
>
> **Maîtriser le triptyque célérité - impédance - conditions aux limites**
>
> Savoir calculer la célérité $c=\sqrt{\gamma RT/M}$ et l'impédance $Z=\rho_0c$ ; savoir traduire une extrémité ouverte, fermée ou une interface entre deux milieux en conditions mathématiques sur $p$ et $v$ ; en déduire fréquences propres, coefficients $R$ et $T$ et résonances.
>
> **Manipuler la notation complexe sans erreur**
>
> Savoir sommer des exponentielles complexes pour obtenir une onde stationnaire, dériver pour passer de $\Psi$ à $p$ ou à $\theta$, extraire module et phase d'un coefficient complexe ($R$), et repasser aux grandeurs réelles pour un calcul d'énergie.
>
> **Raisonner en énergie et en ordres de grandeur**
>
> Savoir exprimer une intensité, un niveau en décibels, évaluer des amplitudes ($\xi_0\sim10^{-11}$ m au seuil d'audition), juger de la validité de l'approximation acoustique, et additionner correctement des sources cohérentes ou non.
>
> **Reconnaître un système connu sous un déguisement**
>
> Savoir identifier, sous des habillages différents (bouteille, sonde échographique, vitre), un oscillateur masse-ressort, une adaptation d'impédance ou un résonateur $\lambda/4$, et transposer ses résultats d'une discipline à une autre (optique, électricité, mécanique).



> [!tip]- 📖 Rappel de cours
> **Fil conducteur du TD : proposition de progression**
>
> **À introduire en début de séance**
>
>
>
> 1. **Équation d'onde et célérité**
>
>     Les équations linéarisées donnent $\Delta p-\dfrac1{c^2}\partial_t^2p=0$ avec
>     $$c=\frac1{\sqrt{\rho_0\chi_S}}=\sqrt{\frac{\gamma P_0}{\rho_0}}=\sqrt{\frac{\gamma RT}{M}}.$$
>     La célérité d'un gaz parfait ne dépend que de $T$ (à composition donnée). Le caractère isentropique tient à la rapidité de l'oscillation devant la diffusion thermique.
> 2. **Onde progressive et impédance**
>
>     Pour une onde plane vers $\pm x$, $\tilde p=\pm Z\tilde v$ avec $Z=\rho_0c$. L'impédance relie la pression à la vitesse du fluide, comme $U=ZI$. Elle contrôle ce qui se passe à toute interface.
> 3. **Conditions aux limites et ondes stationnaires**
>
>     Extrémité ouverte : nœud de surpression, ventre de déplacement ($Z\to0$, $R=-1$). Extrémité fermée : nœud de déplacement, ventre de surpression ($Z\to\infty$, $R=+1$).
>     $$\text{ouvert-ouvert : }f_n=\frac{nc}{2L};\qquad\text{ouvert-fermé : }f_n=\frac{(2n-1)c}{4L}.$$
> 4. **Interface entre deux fluides**
>
>     Continuité de $p$ et de $v$ ; $R=\dfrac{Z_2-Z_1}{Z_1+Z_2}$, $T=\dfrac{2Z_2}{Z_1+Z_2}$, $R_I+T_I=1$ ; seul le contraste d'impédance compte.
>
>
>
> **Pour approfondir (exercices 5 à 8)**
>
>
>
> 1. \setcounter{enumi}{4}
> 2. **Énergie et intensité**
>
>     $e=\tfrac12\rho_0v^2+\tfrac12\chi p^2$, flux $\Pi=pv$, $\partial_te+\partial_x\Pi=0$ ; pour une onde progressive $I=p_{\mathrm{eff}}^2/Z=c\langle e\rangle$ ; $L=10\log_{10}(I/I_0)$ ; une onde stationnaire stocke l'énergie sans la transporter.
> 3. **Impédance ramenée et lame**
>
>     $Z_{\mathrm{in}}=Z_2\dfrac{Z_3\cos u+iZ_2\sin u}{Z_2\cos u+iZ_3\sin u}$ ; lame $\lambda/2$ transparente, lame $\lambda/4$ adaptatrice si $Z_2=\sqrt{Z_1Z_3}$.
> 4. **Éléments localisés**
>
>     Si $\lambda\gg D$, un conduit étroit est une masse $\rho_0S\ell'$ et une cavité un ressort $\gamma P_0S^2/V$ : $f_0=\dfrac c{2\pi}\sqrt{\dfrac S{V\ell'}}$.
>
> **Tableau de correspondance conditions aux limites / grandeurs physiques**
>
> $$
> \begin{array}{c|c|c|c|c}
>   \textbf{Extrémité} & \textbf{Déplacement } \Psi & \textbf{Surpression } p & Z_s & R\\
>   \hline
>   \text{Ouverte (idéale)} & \text{ventre} & \text{nœud} & 0 & -1\\
>   \text{Fermée (paroi rigide)} & \text{nœud} & \text{ventre} & \infty & +1\\
>   \text{Matériau adapté} & \text{—} & \text{—} & Z_0 & 0\\
>   \text{Matériau absorbant} & \text{—} & \text{—} & Z_0\dfrac{1+R}{1-R} & |R|<1
> \end{array}
> $$
>
> À mémoriser : la pression et la vitesse (ou le déplacement) sont toujours en quadrature spatiale dans une onde stationnaire, et en quadrature temporelle (aucun flux moyen d'énergie).



> [!note]- 🧮 Outils mathématiques
> **Notation complexe et formules d'Euler**
>
> $e^{iu}\pm e^{-iu}=2\cos u$ ou $2i\sin u$. Pour sommer des ondes de même fréquence, factoriser $e^{i\omega t}$ et un facteur de phase global ; la partie réelle redonne l'expression physique. Pour un produit de grandeurs réelles, $\langle ab\rangle=\tfrac12\operatorname{Re}(\tilde a\tilde b^{*})$.
>
> **Dérivées partielles et linéarisation**
>
> Développement au premier ordre d'une fonction d'une petite perturbation : $P(\rho)\approx P_0+(\partial P/\partial\rho)\rho'$. Savoir passer de $\partial_t\to i\omega$, $\partial_x\to\mp ik$ en notation complexe.
>
> **Résolution de $\ddot\xi+\omega_0^2\xi=0$ et analogie $LC$**
>
> Solution $\xi=\xi_m\cos(\omega_0t+\phi)$ ; la pulsation propre est lue dans le coefficient de $\xi$. Même équation pour une masse-ressort, un circuit $LC$ et un résonateur de Helmholtz.
>
> **Zéros des fonctions trigonométriques et quantification**
>
> $\sin u=0\Leftrightarrow u=n\pi$ ; $\cos u=0\Leftrightarrow u=(2n-1)\pi/2$. La nature de la condition ($\sin$ ou $\cos$) décide du spectre de fréquences : tous les entiers ou seulement les impairs.
>
> **Systèmes linéaires $2\times2$ et fractions complexes**
>
> Raccord à une interface : deux équations, deux inconnues ($R$, $T$). Pour une fraction complexe, multiplier haut et bas par le conjugué du dénominateur ; pour $|R|^2$, séparer parties réelle et imaginaire.
>
> **Logarithmes décimaux et décibels**
>
> $L=10\log_{10}(I/I_0)=20\log_{10}(p/p_0)$ ; $10\log_{10}2\approx3$ dB ; $20\log_{10}2\approx6$ dB ; $\log_{10}(ab)=\log_{10}a+\log_{10}b$.
>
> **Développements limités et ordres de grandeur**
>
> $\cos u\approx1-u^2/2$, $\sin u\approx u$, $(1+\varepsilon)^{1/2}\approx1+\varepsilon/2$ ; estimation de nombres sans dimension ($p_0/P_0$, $v_0/c$, $k\ell$, $u=ke$) pour valider une hypothèse.
>
> **Moyennes temporelles**
>
> $\langle\cos^2\omega t\rangle=\tfrac12$, $\langle\sin\omega t\cos\omega t\rangle=0$ ; intégrale d'un $\cos^2$ sur un nombre entier de demi-périodes spatiales $=L/2$.
>
> **Racines carrées de rapports et moyenne géométrique**
>
> $c\propto\sqrt T$ ; $f_0\propto V^{-1/2}$ ; $Z_2=\sqrt{Z_1Z_3}$ : savoir faire des estimations rapides ($\sqrt\gamma=1{,}18$, $\sqrt2=1{,}41$, $\sqrt{1{,}5}=1{,}22$).



## Exercices

- [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex1-celerite-d-une-onde-acoustique-dans-un-fluide-parfait|Exercice 1 — Célérité d'une onde acoustique dans un fluide parfait]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex2-onde-stationnaire-tube-de-kundt-ouvert|Exercice 2 — Onde stationnaire, tube de Kundt ouvert]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex3-onde-stationnaire-tube-de-kundt-ferme-a-faire-a-la-maison|Exercice 3 — Onde stationnaire, tube de Kundt fermé (à faire à la maison)]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex4-reflexion-et-transmission-d-une-onde-acoustique-a-une-interface-entre-deux-fluides|Exercice 4 — Réflexion et transmission d'une onde acoustique à une interface entre deux fluides]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex5-energie-intensite-acoustique-et-niveau-sonore-de-l-oreille-humaine-a-l-onde-stationnaire|Exercice 5 — Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex6-tube-d-impedance-mesurer-l-absorption-d-un-materiau-avec-une-onde-stationnaire-partielle|Exercice 6 — Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex7-resonateur-de-helmholtz-la-bouteille-qui-chante|Exercice 7 — Résonateur de Helmholtz : la bouteille qui chante]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex8-transmission-a-travers-une-lame-adaptation-d-impedance-loi-de-masse-et-double-vitrage|Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage]]

## QCM liés à ce document


**S'entraîner librement** (3 question(s) liées à ce document) :

<a href="/qcm/physique-ondes-ipsa/?c=td1_qcm" target="_blank" rel="noopener">td1_qcm</a><br><a href="/qcm/physique-ondes-ipsa/?c=td1_qcm" target="_blank" rel="noopener"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNjQiIGhlaWdodD0iMTY0IiBjbGFzcz0ic2Vnbm8iPjxwYXRoIHRyYW5zZm9ybT0ic2NhbGUoNCkiIGNsYXNzPSJxcmxpbmUiIHN0cm9rZT0iIzE2MzIzZiIgZD0iTTIgMi41aDdtMSAwaDRtMiAwaDNtMSAwaDJtNCAwaDJtMSAwaDFtMiAwaDdtLTM3IDFoMW01IDBoMW05IDBoM20xIDBoMm0yIDBoMm0yIDBoMW0xIDBoMW01IDBoMW0tMzcgMWgxbTEgMGgzbTEgMGgxbTMgMGgxbTIgMGgzbTEgMGg1bTEgMGgxbTIgMGgxbTEgMGgxbTEgMGgxbTEgMGgzbTEgMGgxbS0zNyAxaDFtMSAwaDNtMSAwaDFtMSAwaDNtMiAwaDFtNCAwaDJtMyAwaDVtMiAwaDFtMSAwaDNtMSAwaDFtLTM3IDFoMW0xIDBoM20xIDBoMW0xIDBoMW00IDBoMW0xIDBoMW0yIDBoMW0yIDBoMW0xIDBoMW0yIDBoM20xIDBoMW0xIDBoM20xIDBoMW0tMzcgMWgxbTUgMGgxbTEgMGgxbTIgMGgxbTEgMGgxbTEgMGgybTEgMGgybTEgMGgybTIgMGgxbTIgMGgxbTEgMGgxbTUgMGgxbS0zNyAxaDdtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDdtLTI5IDFoNm0yIDBoM20zIDBoMm0yIDBoMW0xIDBoMW0tMjkgMWgxbTMgMGgxbTEgMGgzbTEgMGgzbTEgMGgxbTMgMGgybTIgMGgxbTEgMGgxbTQgMGg1bTIgMGgxbS0zNSAxaDFtNSAwaDFtMSAwaDVtMSAwaDJtMSAwaDNtMiAwaDFtMiAwaDJtMyAwaDRtLTM2IDFoNG0yIDBoMm0zIDBoNG0xIDBoM20xIDBoOG0xIDBoMW0xIDBoMW0yIDBoMW0tMzUgMWgxbTIgMGgybTQgMGgybTEgMGgybTMgMGgybTIgMGgxbTEgMGgybTUgMGgzbTEgMGgybS0zNiAxaDJtMiAwaDFtMSAwaDFtMSAwaDFtMiAwaDJtMiAwaDVtMSAwaDRtMiAwaDVtMiAwaDNtLTM3IDFoMW0xIDBoMW0xIDBoMm0xIDBoMW0zIDBoMW0xIDBoMW0xIDBoNG00IDBoMW0xIDBoMW0xIDBoMm0zIDBoMm0tMzQgMWgybTEgMGgybTEgMGgxbTEgMGgxbTEgMGgybTEgMGgzbTIgMGgxbTEgMGg0bTIgMGgxMG0tMzUgMWgybTIgMGgxbTMgMGgxbTEgMGgxbTIgMGgzbTIgMGgzbTIgMGgxbTYgMGgybTEgMGgxbS0zNSAxaDJtNCAwaDFtMiAwaDNtMyAwaDJtMyAwaDFtMyAwaDFtMiAwaDVtMSAwaDRtLTM1IDFoNG0xIDBoMW0xIDBoNG00IDBoM20xIDBoM20xIDBoM20xIDBoMW0xIDBoNW0tMzYgMWgybTMgMGg1bTMgMGgzbTIgMGgybTMgMGgzbTEgMGgxbTIgMGgzbS0zMiAxaDFtMSAwaDNtMSAwaDFtMiAwaDFtMSAwaDFtMSAwaDhtNCAwaDFtMyAwaDFtMyAwaDJtLTM2IDFoMm0xIDBoNG0xIDBoMm0xIDBoMW0yIDBoMW0yIDBoMW0yIDBoM200IDBoMW0xIDBoM20yIDBoMW0tMzIgMWgxbTEgMGgxbTEgMGgybTEgMGgxbTIgMGg0bTMgMGgybTEgMGgxbTEgMGgzbTEgMGgxbTEgMGgybS0zMyAxaDJtMSAwaDJtMSAwaDJtMyAwaDFtMSAwaDNtMSAwaDFtNSAwaDJtMSAwaDJtMSAwaDFtMSAwaDRtLTMzIDFoMW0xIDBoMm00IDBoNW0xIDBoNG0yIDBoM20zIDBoMm0xIDBoMm0xIDBoMW0tMzQgMWgybTMgMGgxbTEgMGgybTEgMGg0bTMgMGgybTIgMGgxbTEgMGgxbTEgMGgxbTIgMGgybTIgMGg0bS0zNyAxaDFtMiAwaDFtMSAwaDFtNCAwaDFtMyAwaDFtMSAwaDFtMiAwaDNtMSAwaDFtMSAwaDFtMSAwaDFtMSAwaDFtMiAwaDNtLTMzIDFoNm0xIDBoNW0yIDBoMm0yIDBoMW0yIDBoMm0xIDBoMm0zIDBoMW0xIDBoMW0tMzIgMWgxbTEgMGgxbTIgMGgybTEgMGgxbTIgMGgybTIgMGgxbTMgMGgzbTIgMGgzbTIgMGgxbTIgMGgzbS0zNyAxaDNtMSAwaDFtMSAwaDFtMSAwaDFtMyAwaDZtMSAwaDFtMSAwaDFtMiAwaDFtMyAwaDVtMSAwaDFtMSAwaDFtLTI5IDFoMm0yIDBoMm0xIDBoNG00IDBoMW0xIDBoMW0xIDBoMm0zIDBoMW0yIDBoMW0tMzYgMWg3bTEgMGgxbTEgMGgxbTQgMGgxbTIgMGgxbTIgMGg0bTMgMGgxbTEgMGgxbTEgMGgxbS0zMyAxaDFtNSAwaDFtMiAwaDFtMyAwaDFtMSAwaDJtMiAwaDNtMSAwaDJtMSAwaDFtMSAwaDFtMyAwaDNtLTM1IDFoMW0xIDBoM20xIDBoMW0xIDBoMm0yIDBoMW0yIDBoMm0yIDBoMm0yIDBoMW0xIDBoMW0yIDBoN20xIDBoMW0tMzcgMWgxbTEgMGgzbTEgMGgxbTMgMGg0bTMgMGgzbTEgMGgzbTEgMGgxbTIgMGg0bTEgMGgxbTIgMGgxbS0zNyAxaDFtMSAwaDNtMSAwaDFtMiAwaDVtMSAwaDFtMSAwaDFtMSAwaDFtMyAwaDJtMSAwaDNtMSAwaDFtMiAwaDJtLTM1IDFoMW01IDBoMW0yIDBoMW0xIDBoN20xIDBoNG0xIDBoMW0yIDBoMW0xIDBoMW0yIDBoMW0xIDBoMm0tMzYgMWg3bTEgMGgxbTEgMGgybTEgMGgxbTIgMGgybTIgMGg1bTEgMGgybTEgMGgxbTEgMGgxbTIgMGgzIi8+PC9zdmc+Cg==" width="110" height="110" alt="QR code : td1_qcm" style="image-rendering:pixelated"></a>


> [!note]- 🔗 Liens avec d'autres disciplines
> **Thermodynamique**
>
> Le choix entre $\chi_T$ et $\chi_S$ (exercice 1) est un exemple direct de transformation réelle ; on y utilise les lois de Laplace, la relation de Mayer, le rapport $\gamma$ des capacités calorifiques. À $300$ K, $c$ dans l'hélium ($\gamma=5/3$, $M=4$ g/mol) est environ $3$ fois celle de l'air : la voix « de canard » après inhalation d'hélium est un effet de $c$, non de la hauteur du son émis.
>
> **Cordes vibrantes (chapitre 1) et mécanique des milieux continus**
>
> Les nœuds de pression d'un tube ouvert-ouvert jouent le rôle des nœuds de déplacement d'une corde fixe-fixe ; le tube ouvert-fermé joue celui de la corde fixe-libre ; l'impédance $Z=\rho_0c$ est l'analogue de $Z=\sqrt{T_0\mu}$ pour une corde.
>
> **Électrocinétique et lignes de transmission**
>
> Pression $\leftrightarrow$ tension, débit volumique $\leftrightarrow$ courant, masse acoustique $\leftrightarrow$ inductance, cavité $\leftrightarrow$ capacité. Les coefficients $R$ et $T$, l'adaptation d'impédance, la ligne quart d'onde et le ROS sont identiques.
>
> **Optique ondulatoire**
>
> Coefficients de Fresnel en incidence normale, traitements antireflets $\lambda/4$, franges d'interférences d'une lame, résonateur de Fabry-Pérot : tous ces objets ont un analogue exact dans les exercices 4, 6 et 8.
>
> **Mécanique quantique**
>
> Les fonctions d'onde du puits infini ($\sin(n\pi x/L)$) sont les modes d'un tube ouvert-ouvert ; la barrière de potentiel donne des coefficients de réflexion/transmission formellement identiques à ceux d'une interface ; la quantification vient des conditions aux limites.
>
> **Musique, lutherie et acoustique musicale**
>
> Flûte (ouvert-ouvert), clarinette (ouvert-fermé), tuyaux d'orgue, caisse de résonance de guitare (Helmholtz), harmoniques et timbre, longueur effective des tuyaux.
>
> **Médecine et physiologie**
>
> Échographie (contrastes d'impédance, gel, couche d'adaptation), audition (seuil à $10^{-12}$ W/m$^2$, résonance du conduit auditif vers $3$ kHz, échelle logarithmique), ultrasons thérapeutiques.
>
> **Génie civil, bâtiment et environnement sonore**
>
> Loi de masse, double vitrage et sa résonance masse-ressort-masse, absorbants et bass traps, mesure du bruit en dB(A), réglementation de l'exposition sonore.
>
> **Géophysique, océanographie et astrophysique**
>
> Sismologie (réflexions aux interfaces, ondes P), canal SOFAR et sonar sous-marin, héliosismologie (modes acoustiques du Soleil, quantifiés par des conditions aux limites comme dans un tube).
>
> **Ingénierie et environnement industriel**
>
> Silencieux (chambres de Helmholtz, couches d'impédance), contrôle actif du bruit, contrôle non destructif par ultrasons (couplant, adaptation d'impédance, lame demi-onde).



> [!question]- 🔭 Aller plus loin — CPGE : Ondes sphériques et cylindriques
> Pour une source ponctuelle, la solution à symétrie sphérique de l'équation de d'Alembert est $p=\dfrac{f(t-r/c)}{r}$ : l'amplitude décroît en $1/r$ et l'intensité en $1/r^2$ (exercice 5, question 5). On pourra établir que $r\,p$ vérifie l'équation de d'Alembert à une dimension.



> [!question]- 🔭 Aller plus loin — Licence : Absorption classique : viscosité et conduction thermique
> Dans un fluide réel, la viscosité et la conduction thermique atténuent l'onde en $e^{-\alpha x}$ avec $\alpha\propto\omega^2$ (formule de Stokes-Kirchhoff). On pourra estimer $\alpha$ dans l'air à $10$ kHz et $1$ MHz, et comprendre pourquoi les ultrasons sont absorbés sur de courtes distances dans l'air mais se propagent très loin dans l'eau.



> [!question]- 🔭 Aller plus loin — Licence : Effet Doppler et onde de choc
> Pour une source mobile à la vitesse $v_s$, $f'=f/(1-v_s/c)$ en approche. Lorsque $v_s>c$, les fronts d'onde s'accumulent sur un cône de demi-angle $\sin\theta=c/v_s$ (cône de Mach) : c'est le « bang » supersonique.



> [!question]- 🔭 Aller plus loin — Master : Acoustique non linéaire
> À forte amplitude, la célérité locale dépend de la perturbation, $c\approx c_0+\tfrac{\gamma+1}2v$ : les compressions rattrapent les détentes, le profil se raidit et forme une onde de choc (équation de Burgers). On pourra estimer la distance de formation du choc pour une onde à $140$ dB et $1$ kHz.



> [!question]- 🔭 Aller plus loin — Master : Acoustique des salles : modes propres et réverbération
> Dans une salle rectangulaire, les modes propres sont $f=\dfrac c2\sqrt{(n_x/L_x)^2+(n_y/L_y)^2+(n_z/L_z)^2}$ ; au-delà de la fréquence de Schroeder, leur densité est telle que le champ est diffus et la décroissance suit la loi de Sabine, $T_R=0{,}16\,V/A$.



> [!question]- 🔭 Aller plus loin — Master : Ondes élastiques dans les solides
> Dans un solide apparaissent des ondes longitudinales ($c_L$) et transversales ($c_T<c_L$). On pourra étendre le calcul d'impédance et de réflexion à l'interface fluide-solide, ce qui précise les hypothèses de la loi de masse (exercice 8).



> [!question]- 🔭 Aller plus loin — Doctorat : Cristaux phononiques et métamatériaux acoustiques
> Un milieu périodique (multicouche, réseau de résonateurs) possède des bandes de fréquences interdites (bandes gap), par interférences de type Bragg ou par résonances locales. On pourra les étudier avec les matrices de transfert de l'exercice 8.


