---
title: "Coefficients de réflexion et transmission, impédance"
tags:
  - td
  - chap-3-interfaces-entre-deux-milieux
---

[[physique/IPSA/ipsa-physique-ondes/index|⬅ Physique des ondes]]

> [!info] ℹ️ Chap. 3 — Interfaces entre deux milieux
> Séance 4


<a href="/pdfs/td3_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_PhV212_enonce)</a> · <a href="/pdfs/td3_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td3_enonce)</a> · <a href="/pdfs/td3_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides</a> · <a href="/pdfs/td3_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td3_PhV212_corrige)</a> · <a href="/pdfs/td3_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td3_corrige)</a>

> [!question]+ 🎣 Accroche
> **Pourquoi un écho vient-il à l'endroit ou à l'envers, et pourquoi le gel est-il nécessaire ?**
>
> *Durée de l'introduction : 10 min, en début de séance*
>
> *Quatre questions simples : (1) une impulsion sur une corde fine rencontre une corde épaisse : l'écho est-il à l'endroit ou renversé ? (2) Pourquoi doit-on étaler du gel sur la peau pour une échographie ? (3) Pourquoi un son qui entre dans l'eau doit-il arriver à peu près de la verticale ? (4) Comment un géophysicien mesure-t-il l'épaisseur d'une couche de sol sans creuser ? **Que partagent ces quatre situations ?***
>
> **Idée clé : à toute interface, deux conditions de raccord, un rapport d'impédances.** Quand une onde rencontre une interface, deux grandeurs restent continues (déplacement et pente pour une corde ; pression et vitesse pour un fluide). La solution du système ne dépend que du *rapport des impédances* :
> $$r=\frac{Z_1-Z_2}{Z_1+Z_2},\qquad R_E=r^2,\qquad T_E=\frac{4Z_1Z_2}{(Z_1+Z_2)^2}.$$
> Une interface très désadaptée réfléchit tout (air/solide) ; une interface oblique ajoute la conservation de $k_y$ (Snell-Descartes) ; un élément localisé ajoute une impédance en série.

> [!abstract]+ 📚 Prérequis
> **Équation de d'Alembert et ondes progressives (chapitres 1 et 2)**
>
> Savoir que les petites perturbations d'une corde tendue ($y$) et d'un fluide ($p$, $v$) obéissent à $\partial_t^2u=c^2\partial_x^2u$, avec $c=\sqrt{F/\mu}$ pour une corde et $c=\sqrt{1/(\rho_0\chi_S)}$ pour un fluide ; savoir qu'une onde progressive sinusoïdale s'écrit $\cos(\omega t\mp kx)$ ou $e^{i(\omega t\mp kx)}$ avec $k=\omega/c$ et que le signe devant $kx$ fixe le sens de propagation.
>
> **Impédance caractéristique d'un milieu**
>
> Connaître la définition $Z=\rho c$ (fluide) et $Z=\mu c=\sqrt{F\mu}$ (corde), la relation $\tilde p=\pm Z\tilde v$ pour une onde plane progressive, et le fait que l'impédance mesure la « résistance » du milieu à être mis en mouvement : à $\omega$ fixé, $k$ est proportionnel à $Z$ pour deux cordes de même tension.
>
> **Conditions de raccord**
>
> Savoir écrire les conditions physiques à une interface : continuité du déplacement et de la force transverse (pente) pour deux cordes ; continuité de la pression et de la vitesse normale pour deux fluides. Savoir en déduire un système linéaire $2\times2$ pour les amplitudes réfléchie et transmise.
>
> **Énergie et intensité d'une onde (TD2)**
>
> Savoir que l'intensité acoustique moyenne est $p_{\mathrm{eff}}^2/Z$, que la puissance moyenne d'une onde de corde est $\tfrac12Z\omega^2A^2$, que les coefficients énergétiques s'obtiennent en rapportant ces flux, et que $R_E+T_E=1$ en l'absence de dissipation.
>
> **Nombres complexes et notation $e^{i\omega t}$**
>
> Module, argument, conjugué ; $\partial_t\to i\omega$ ; passage entre domaine fréquentiel et domaine temporel ($i\omega\leftrightarrow\partial_t$, $e^{-i\omega\tau}\leftrightarrow$ retard $\tau$) ; manipulation de fractions complexes.
>
> **Trigonométrie, systèmes linéaires et ordres de grandeur**
>
> Formules de trigonométrie ($\sin^2+\cos^2=1$, $\arcsin$), résolution d'un système linéaire $2\times2$, calculs avec des puissances de $10$ et des décibels, développement limité d'une fraction.

> [!info]+ 🎯 Objectifs
> **Savoir établir et interpréter des coefficients de réflexion et de transmission**
>
> Savoir écrire les conditions de raccord à une jonction (corde ou fluide), résoudre le système obtenu, exprimer $r$ et $t$ en fonction des impédances, en déduire les coefficients énergétiques $R_E=|r|^2$ et $T_E=1-R_E$, et vérifier systématiquement la conservation de l'énergie.
>
> **Reconnaître l'universalité de la notion d'impédance**
>
> Savoir transposer un résultat d'un domaine à un autre : corde, acoustique, ligne électrique, optique, mécanique quantique partagent la même structure $r=(Z_1-Z_2)/(Z_1+Z_2)$ ou $(Z_2-Z_1)/(Z_1+Z_2)$ selon la grandeur raccordée (type « force » ou type « vitesse »).
>
> **Savoir ajouter un élément au raccord et en lire l'effet en fréquence**
>
> Savoir traiter une masse, un ressort ou un amortisseur à une jonction comme une impédance additionnelle en série, en déduire un filtre passe-bas, passe-bande ou une terminaison absorbante, et interpréter le résultat dans le domaine temporel (retard, dérivation).
>
> **Savoir traiter l'incidence oblique**
>
> Savoir démontrer les lois de Snell-Descartes par conservation de $k_y$, calculer $R(\theta)$ avec les impédances apparentes $Z/\cos\theta$, déterminer l'angle critique, et interpréter la réflexion totale par une onde évanescente de flux moyen nul.
>
> **Savoir résoudre un problème d'ingénieur à partir de mesures**
>
> Savoir exploiter un enregistrement (temps d'arrivée en sismique réfraction, train d'échos ultrasonore) pour en déduire une vitesse, une épaisseur, une impédance, une atténuation ou un défaut, en justifiant les hypothèses et en estimant les incertitudes.

> [!note]+ 📖 Point de cours
> **Synthèse du chapitre : de la jonction de deux cordes aux interfaces acoustiques**
>
> 1. **Raccord à une interface plane en incidence normale**
>
>     Deux conditions de continuité relient les amplitudes incidente, réfléchie et transmise. Pour une corde : $y$ et $\partial_xy$ ; pour un fluide : $p$ et $v$. On obtient, en amplitude,
>     $$r=\frac{Z_1-Z_2}{Z_1+Z_2},\quad t=\frac{2Z_1}{Z_1+Z_2}\ \ (\text{déplacement}),\qquad R=\frac{Z_2-Z_1}{Z_1+Z_2},\quad T=\frac{2Z_2}{Z_1+Z_2}\ \ (\text{pression}).$$
> 2. **Coefficients énergétiques**
>
>     $R_E=|r|^2$ et $T_E=\dfrac{Z_2}{Z_1}|t|^2=\dfrac{4Z_1Z_2}{(Z_1+Z_2)^2}$, avec $R_E+T_E=1$ : le coefficient de transmission en énergie est symétrique ($1\to2$ et $2\to1$ donnent la même valeur), seul le contraste d'impédance compte.
> 3. **Impédance en série : éléments localisés**
>
>     Une masse $M$ à la jonction ajoute $iM\omega$, un ressort de raideur $K$ ajoute $K/(i\omega)$, un amortisseur $\eta$ ajoute $\eta$ : $r=\dfrac{Z_1-Z_2-Z_s}{Z_1+Z_2+Z_s}$. La jonction devient un filtre.
> 4. **Incidence oblique**
>
>     La composante tangentielle $k_y$ est conservée : $\theta_1'=\theta_1$ et $\sin\theta_1/c_1=\sin\theta_2/c_2$. Les coefficients de Fresnel acoustiques s'obtiennent avec $Z\to Z/\cos\theta$. Si $c_2>c_1$, l'angle critique $\theta_c=\arcsin(c_1/c_2)$ sépare la transmission de la réflexion totale (onde évanescente).
> 5. **Échos et couches**
>
>     En régime impulsionnel, chaque écho d'une plaque est un produit de coefficients, avec des retards multiples de $2e/c$ ; en régime sinusoïdal, les échos interfèrent (lame demi-onde, lame quart d'onde, TD2 exercice 8).
>
> **Dictionnaire des analogies**
>
> $$
> \begin{array}{c|c|c|c|c}
>   \textbf{Système} & \text{variable de type « force »} & \text{variable de type « vitesse »} & Z & r\ \text{(variable « force »)}\\
>   \hline
>   \text{Corde} & -F\partial_xy & \partial_ty\ (\text{ou } y) & \sqrt{F\mu} & \dfrac{Z_2-Z_1}{Z_1+Z_2}\\
>   \text{Acoustique} & p & v & \rho c & \dfrac{Z_2-Z_1}{Z_1+Z_2}\\
>   \text{Ligne électrique} & U & I & \sqrt{L'/C'} & \dfrac{Z_2-Z_1}{Z_1+Z_2}\\
>   \text{Optique (E, H)} & E & H & Z_0/n & \dfrac{n_1-n_2}{n_1+n_2}
> \end{array}
> $$
> Pour la variable de type « vitesse » (déplacement de la corde, courant, $H$), $r$ change de signe : $r_{\mathrm{vitesse}}=-r_{\mathrm{force}}=\dfrac{Z_1-Z_2}{Z_1+Z_2}$. C'est la raison de la différence de signe entre l'exercice 1 de ce TD (déplacement) et les exercices du TD2 (pression).

> [!note]- 🧮 Outils mathématiques
> **Système linéaire $2\times2$ de raccord**
>
> Deux équations en $(r,t)$ ou $(R,T)$ : on substitue $t=1+r$ (continuité) puis on isole $r$. Le résultat ne dépend que du rapport $Z_2/Z_1$.
>
> **Fractions complexes, module et phase**
>
> $\dfrac{a+ib}{a-ib}=e^{2i\arctan(b/a)}$ de module $1$ ; $|a+ib|^2=a^2+b^2$ ; multiplication par le conjugué pour séparer parties réelle et imaginaire.
>
> **Domaine fréquentiel et domaine temporel**
>
> $i\omega\leftrightarrow\partial_t$ ; $e^{-i\omega\tau}\leftrightarrow$ retard de $\tau$ ; un filtre $1/(1+i\omega\tau)$ est un passe-bas du premier ordre de coupure $1/\tau$, équivalent à un retard $\tau$ à basse fréquence.
>
> **Trigonométrie et angles**
>
> $\cos\theta_2=\sqrt{1-n^2\sin^2\theta_1}$ ; si $n\sin\theta_1>1$, $\cos\theta_2=-i\sqrt{n^2\sin^2\theta_1-1}$ ; construction géométrique d'un trajet brisé ($h/\cos\theta$, $h\tan\theta$).
>
> **Séries géométriques**
>
> $\sum_{n\ge0}q^n=\dfrac1{1-q}$ pour $|q|<1$ : somme des échos d'une plaque ou d'une cavité.
>
> **Ordres de grandeur, notation scientifique et décibels**
>
> Rapports d'impédances de $10^4$, $10\log_{10}$ pour l'énergie et $20\log_{10}$ pour l'amplitude ; éviter la soustraction de deux nombres proches en passant par la formule directe $T_E=4Z_1Z_2/(Z_1+Z_2)^2$.
>
> **Lecture graphique et régression à la main**
>
> Pente d'une droite sur un graphe de temps d'arrivée, ordonnée à l'origine, intersection de deux droites : outils indispensables pour la sismique réfraction (exercice 5).


## Exercices

- [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex1-corde-non-homogene-jonction-entre-deux-cordes|Exercice 1 — Corde non homogène, jonction entre deux cordes]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex2-interface-entre-deux-milieux-notion-d-impedance-acoustique|Exercice 2 — Interface entre deux milieux, notion d'impédance acoustique]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex3-perle-sur-une-corde-jonction-massive-filtre-passe-bas-puis-passe-bande|Exercice 3 — Perle sur une corde : jonction massive, filtre passe-bas puis passe-bande]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex4-incidence-oblique-lois-de-snell-descartes-angle-critique-reflexion-totale-et-onde-evanescente|Exercice 4 — Incidence oblique : lois de Snell-Descartes, angle critique, réflexion totale et onde évanescente]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex5-sismique-refraction-ondes-coniques-et-epaisseur-d-une-couche|Exercice 5 — Sismique réfraction : ondes coniques et épaisseur d'une couche]]
- [[physique/IPSA/ipsa-physique-ondes/TD/chap-3-interfaces-entre-deux-milieux/coefficients-de-reflexion-et-transmission-impedance/ex6-controle-ultrasonore-d-une-plaque-immergee-train-d-echos-epaisseur-attenuation-et-defaut-de-collage|Exercice 6 — Contrôle ultrasonore d'une plaque immergée : train d'échos, épaisseur, atténuation et défaut de collage]]

> [!note]- 🔗 Liens avec d'autres disciplines
> **Optique**
>
> Coefficients de Fresnel, antireflet quart d'onde ($n=\sqrt{n_1n_2}$), réflexion totale et onde évanescente, lame mince et interférences : tous les résultats de ce TD ont un analogue optique exact, avec l'indice $n$ à la place de l'impédance.
>
> **Électricité : lignes de transmission**
>
> Réflexion d'une impulsion sur un câble d'impédance $Z_0$ chargé par $Z_L$ ($r=(Z_L-Z_0)/(Z_L+Z_0)$), adaptation d'impédance, réflectométrie temporelle (TDR), filtre à inductance série ($\leftrightarrow$ perle de l'exercice 3).
>
> **Mécanique quantique**
>
> Marche et barrière de potentiel : $\psi$ et $\psi'$ continues, $r=(k_1-k_2)/(k_1+k_2)$ ; réflexion totale avec onde évanescente ($E<V$) et effet tunnel (lame fine) ; densité de courant de probabilité à la place de l'intensité.
>
> **Imagerie médicale**
>
> Échographie (gel, couches d'adaptation, interfaces entre organes, ombres des côtes), échographie Doppler, ultrasons thérapeutiques.
>
> **Contrôle non destructif et industrie**
>
> Mesure d'épaisseur et détection de défauts par échos ultrasonores, contrôle de collage, ondes rasantes, couplage par immersion.
>
> **Géophysique et sismologie**
>
> Sismique réfraction et réflexion, discontinuité de Mohorovičić, zones d'ombre, structure de la Terre (noyau, manteau), prospection pétrolière et hydrogéologique.
>
> **Acoustique sous-marine et sonar**
>
> Angle critique du fond marin, propagation guidée, canal SOFAR, réflectivité des sédiments, angle d'intromission.
>
> **Acoustique du bâtiment et lutherie**
>
> Loi de masse, double paroi, sourdine de violon et capodastre (jonction chargée), cordes filées, impédance du chevalet et rendement acoustique d'un instrument.
>
> **Biologie et physiologie de l'audition**
>
> L'oreille moyenne est un adaptateur d'impédance entre l'air et le liquide de l'oreille interne ; la perte à l'interface air-eau explique que l'on entend mal sous l'eau.

> [!question]- 🔭 Aller plus loin — Licence : Coefficients énergétiques, adaptation d'impédance et lames
> Établir $R_E+T_E=1$ pour la corde et l'acoustique, puis étudier une couche d'épaisseur $\lambda/4$ et d'impédance $\sqrt{Z_1Z_3}$ qui annule la réflexion entre deux milieux (TD2, exercice 8 ; exercice 6 en régime impulsionnel). Faire le lien avec les antireflets optiques et les transformateurs quart d'onde en hyperfréquences.

> [!question]- 🔭 Aller plus loin — Licence : Ondes de surface et ondes guidées
> Au-delà de l'angle critique, l'onde évanescente se propage le long de l'interface : c'est l'origine des ondes de surface (Rayleigh, Scholte) et de la propagation guidée (fibre optique, canal sonore profond SOFAR, guides d'ondes acoustiques).

> [!question]- 🔭 Aller plus loin — Master : Matrices de transfert et milieux stratifiés
> Le raccord de $N$ couches se traite par produit de matrices $2\times2$ reliant $(p,v)$ ; on retrouve les résonances d'un empilement (miroir de Bragg, cristal phononique) et les bandes interdites.

> [!question]- 🔭 Aller plus loin — Master : Solides : ondes P et S, conversions de mode, ondes de Rayleigh
> Dans un solide, une interface en incidence oblique convertit les ondes P en ondes S et inversement ; le raccord impose la continuité des contraintes normale et tangentielle. On pourra établir les équations de Zoeppritz et les deux angles critiques d'une interface eau-acier.

> [!question]- 🔭 Aller plus loin — Master : Interface en mouvement et effet Doppler
> Si l'interface se déplace à la vitesse $V$, la fréquence réfléchie est décalée : c'est le principe de l'échographie Doppler (mesure de la vitesse du sang) et du radar routier. On pourra établir $f_r=f\,\dfrac{c+V}{c-V}$ pour une réflexion sur un obstacle approchant.

> [!question]- 🔭 Aller plus loin — Doctorat : Métamatériaux et réflexion non réciproque
> Des résonateurs locaux (perles sur ressort, cavités de Helmholtz) intégrés à l'interface permettent de dépasser la loi de masse, de créer des bandes interdites ou des interfaces non réciproques ; la jonction à perle de l'exercice 3 en est la brique de base.

