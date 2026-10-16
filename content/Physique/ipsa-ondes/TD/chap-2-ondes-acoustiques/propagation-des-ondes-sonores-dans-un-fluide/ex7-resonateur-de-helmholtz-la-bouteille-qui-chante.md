---
title: "Exercice 7 — Résonateur de Helmholtz : la bouteille qui chante"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/index|⬅ Retour]] · <a href="/pdfs/td2_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_PhV212_enonce)</a> · <a href="/pdfs/td2_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_enonce)</a> · <a href="/pdfs/td2_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_aides)</a> · <a href="/pdfs/td2_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_exs_maison_aide)</a>

### Exercice 7. Résonateur de Helmholtz : la bouteille qui chante *(facultatif)*

Lorsqu'on souffle en travers du goulot d'une bouteille, on entend une note grave bien définie. On modélise la
bouteille par une cavité de volume $V$ communiquant avec l'extérieur par un goulot cylindrique de section $S$ et de
longueur $\ell$. Les dimensions du goulot et de la cavité sont petites devant la longueur d'onde. Le «~bouchon~»
d'air contenu dans le goulot oscille comme un piston rigide, de masse $m=\rho_0S\ell'$, où
$\ell'=\ell+1{,}7\,a$ est une longueur effective tenant compte de l'air entraîné aux deux extrémités du goulot
(on l'admet, $a$ est le rayon du goulot). L'air de la cavité subit des compressions-détentes rapides.

Données : $V=0{,}75$ L, $a=9$ mm, $\ell=8$ cm, $P_0=10^5$ Pa, $\rho_0=1{,}2~\text{kg}\cdot\text{m}^{-3}$,
$\gamma=1{,}4$, $c=340~\text{m}\cdot\text{s}^{-1}$. On note $\xi(t)$ le déplacement du bouchon vers l'intérieur de la cavité.

**q1.** Calculer $S$, la fréquence approximative $f_0$ (voir question 3) et la longueur d'onde associée.
Justifier que le bouchon peut être traité comme un bloc rigide et la pression dans la cavité
comme uniforme.

> [!tip]- 💡 Coup de pouce
> Comparez $\lambda$ aux dimensions de la bouteille (goulot : $\ell'\approx10$ cm ; cavité : $\sim20$ cm) via les produits $k\ell'$ et $kD$.


**q2.** Exprimer la surpression $p(t)$ dans la cavité en fonction de $\xi$ (compression isentropique), puis
écrire l'équation du mouvement du bouchon. En déduire la pulsation propre $\omega_0$ en fonction de $c$,
$S$, $V$ et $\ell'$.

> [!tip]- 💡 Coup de pouce
> Pour un déplacement $\xi$ vers l'intérieur, $\Delta V=-S\xi$. Utilisez la définition de $\chi_S$ pour obtenir $p$. La pression extérieure $P_0$ agit sur la face externe du bouchon : seule la surpression compte dans le bilan de forces.


**q3.** Calculer numériquement $f_0$. Comparer au résultat sans longueur effective ($\ell'\to\ell$) et à l'estimation
d'un tube quart d'onde $c/(4\ell)$. Une mesure donne $f_{\mathrm{exp}}=103$ Hz : conclure.

**q4.** Refaire le calcul en supposant que l'air de la cavité subit une transformation isotherme. Quelle fréquence
prédit-on ? L'expérience de la question 3 permet-elle de trancher, comme à l'exercice 1 ?

> [!tip]- 💡 Coup de pouce
> Remplacez $\chi_S$ par $\chi_T=1/P_0$ dans l'expression de $p(\xi)$.


**q5.** On verse de l'eau dans la bouteille de façon que le volume d'air tombe à $V'=0{,}50$ L. Calculer la nouvelle
fréquence et vérifier le sens de variation observé expérimentalement. Dans quel rapport faut-il changer
$V$ pour monter d'une octave ?

**q6.** Montrer que le résonateur est analogue à un circuit $LC$. On définit le débit volumique
$q=S\dot\xi$. Identifier la tension, le courant, l'inductance $L_a$ et la capacité $C_a$, et retrouver
$\omega_0=1/\sqrt{L_aC_a}$.

> [!tip]- 💡 Coup de pouce
> Écrivez la loi du bouchon sous la forme $p=L_a\dot q$ et la loi de la cavité sous la forme $\dot p=q/C_a$ (au signe près selon l'orientation).


**q7.** Une salle parallélépipédique de longueur $L=5$ m (murs rigides) possède un mode axial gênant (boum
de basses). Calculer sa fréquence. On veut absorber ce mode avec un résonateur de Helmholtz de goulot
$S=1{,}0\times10^{-2}$ m$^2$ et $\ell'=10$ cm. Quel volume de cavité faut-il ? Commenter.

> [!tip]- 💡 Coup de pouce
> Entre deux parois rigides, les modes de pression ont des ventres aux deux bouts : $f_n=nc/(2L)$ (comme le tube ouvert-ouvert de l'exercice 2, mais ici avec des ventres de pression).


> [!note] 🔗 Voir aussi
> [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex1-celerite-d-une-onde-acoustique-dans-un-fluide-parfait|Exercice 1 — Célérité d'une onde acoustique dans un fluide parfait]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex4-reflexion-et-transmission-d-une-onde-acoustique-a-une-interface-entre-deux-fluides|Exercice 4 — Réflexion et transmission d'une onde acoustique à une interface entre deux fluides]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex8-transmission-a-travers-une-lame-adaptation-d-impedance-loi-de-masse-et-double-vitrage|Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex5-energie-intensite-acoustique-et-niveau-sonore-de-l-oreille-humaine-a-l-onde-stationnaire|Exercice 5 — Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire]] · [[physique/ipsa-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex6-tube-d-impedance-mesurer-l-absorption-d-un-materiau-avec-une-onde-stationnaire-partielle|Exercice 6 — Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle]]

