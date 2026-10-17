---
title: "Exercice 7 — Résonateur de Helmholtz : la bouteille qui chante"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/index|⬅ Retour]] · <a href="/pdfs/td2_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_PhV212_enonce)</a> · <a href="/pdfs/td2_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_enonce)</a> · <a href="/pdfs/td2_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_aides)</a> · <a href="/pdfs/td2_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td2_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_PhV212_corrige)</a> · <a href="/pdfs/td2_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_corrige)</a> · <a href="/pdfs/td2_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

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


> [!success]- ✅ Correction
> $S=2{,}5\times10^{-4}$ m$^2$ ; $f_0\approx102$ Hz ; $\lambda\approx3{,}3$ m ; $k\ell'\approx0{,}2\ll1$ : hypothèses de basse fréquence satisfaites.


> [!example]- 📝 Solution détaillée
> **Section et fréquence**
>
> $S=\pi a^2=\pi(9\times10^{-3})^2\approx2{,}5\times10^{-4}~\text{m}^2$ ; $\ell'=0{,}08+1{,}7\times0{,}009=0{,}0953$ m. On trouvera à la question 3 $f_0\approx102$ Hz, donc $\lambda=c/f_0\approx3{,}3$ m.
>
> **Validité de l'hypothèse de basse fréquence**
>
> $$k\ell'=\frac{2\pi\ell'}{\lambda}\approx\frac{2\pi\times0{,}095}{3{,}3}\approx0{,}18\ll1,\qquad kD\sim\frac{2\pi\times0{,}2}{3{,}3}\approx0{,}4.$$
> Sur la longueur du goulot, la phase de l'onde varie de moins de $0{,}2$ rad : tout le bouchon se déplace en bloc (fluide incompressible à cette échelle). De même, la cavité est petite devant $\lambda$ et la pression y est uniforme à chaque instant. Les hypothèses d'éléments localisés sont satisfaites, avec une précision de l'ordre de $10\ \%$.


**q2.** Exprimer la surpression $p(t)$ dans la cavité en fonction de $\xi$ (compression isentropique), puis
écrire l'équation du mouvement du bouchon. En déduire la pulsation propre $\omega_0$ en fonction de $c$,
$S$, $V$ et $\ell'$.

> [!tip]- 💡 Coup de pouce
> Pour un déplacement $\xi$ vers l'intérieur, $\Delta V=-S\xi$. Utilisez la définition de $\chi_S$ pour obtenir $p$. La pression extérieure $P_0$ agit sur la face externe du bouchon : seule la surpression compte dans le bilan de forces.


> [!success]- ✅ Correction
> $p=\gamma P_0S\xi/V$ ; $\ddot\xi+\omega_0^2\xi=0$ avec $\omega_0=c\sqrt{S/(V\ell')}$.


> [!example]- 📝 Solution détaillée
> **Surpression dans la cavité**
>
> La compression est isentropique ($\chi_S=1/(\gamma P_0)$). Pour une petite variation de volume $\Delta V=-S\xi$ :
> $$\frac{\Delta V}{V}=-\chi_S\,p\quad\Longrightarrow\quad p=-\frac{\Delta V}{\chi_SV}=\frac{\gamma P_0S}{V}\,\xi.$$
>
> **Équation du mouvement**
>
> La surpression $p$ de la cavité pousse le bouchon vers l'extérieur avec la force $-pS$ (le bouchon se déplace dans le sens $+\xi$ vers l'intérieur) :
> $$\rho_0S\ell'\,\ddot\xi=-pS=-\frac{\gamma P_0S^2}{V}\,\xi\quad\Longrightarrow\quad\ddot\xi+\frac{\gamma P_0S}{\rho_0\ell'V}\xi=0.$$
> Avec $c^2=\gamma P_0/\rho_0$ :
> $$\boxed{\omega_0=c\sqrt{\frac{S}{V\ell'}}},\qquad f_0=\frac{c}{2\pi}\sqrt{\frac{S}{V\ell'}}.$$
> La raideur équivalente est $K=\gamma P_0S^2/V$ et la masse $m=\rho_0S\ell'$ : on retrouve bien $\omega_0=\sqrt{K/m}$.


**q3.** Calculer numériquement $f_0$. Comparer au résultat sans longueur effective ($\ell'\to\ell$) et à l'estimation
d'un tube quart d'onde $c/(4\ell)$. Une mesure donne $f_{\mathrm{exp}}=103$ Hz : conclure.

> [!success]- ✅ Correction
> $f_0\approx102$ Hz ; sans correction $\approx111$ Hz ; $c/(4\ell)\approx1{,}06$ kHz ; accord à $1\ \%$ avec l'expérience.


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> $$f_0=\frac{340}{2\pi}\sqrt{\frac{2{,}54\times10^{-4}}{7{,}5\times10^{-4}\times0{,}0953}}=54{,}1\times\sqrt{3{,}56}\approx54{,}1\times1{,}89\approx102~\text{Hz}.$$
> Sans correction de longueur : $f=54{,}1\times\sqrt{2{,}54\times10^{-4}/(7{,}5\times10^{-4}\times0{,}08)}\approx111$ Hz, soit $9\ \%$ d'écart. Un tube quart d'onde de même longueur donnerait $c/(4\ell)=340/0{,}32\approx1{,}06$ kHz, une dizaine de fois plus : ce n'est pas le bon modèle.
>
> **Comparaison à l'expérience**
>
> $f_{\mathrm{exp}}=103$ Hz est en excellent accord (à $1\ \%$) avec la prédiction du modèle masse-ressort avec longueur effective. Il confirme à la fois l'hypothèse des éléments localisés et la correction d'extrémité.


**q4.** Refaire le calcul en supposant que l'air de la cavité subit une transformation isotherme. Quelle fréquence
prédit-on ? L'expérience de la question 3 permet-elle de trancher, comme à l'exercice 1 ?

> [!tip]- 💡 Coup de pouce
> Remplacez $\chi_S$ par $\chi_T=1/P_0$ dans l'expression de $p(\xi)$.


> [!success]- ✅ Correction
> $f_T=f_0/\sqrt\gamma\approx86$ Hz : en désaccord à $16\ \%$ avec $f_{\mathrm{exp}}=103$ Hz ; l'hypothèse isentropique est la bonne.


> [!example]- 📝 Solution détaillée
> **Cas isotherme**
>
> Avec $\chi_T=1/P_0$ : $p=P_0S\xi/V$, $K_T=P_0S^2/V$ et $\omega_T=\omega_0/\sqrt\gamma$, soit
> $$f_T=\frac{f_0}{\sqrt{1{,}4}}\approx\frac{102}{1{,}18}\approx86~\text{Hz}.$$
>
> **Conclusion**
>
> L'écart de $16\ \%$ avec la mesure ($103$ Hz) est très supérieur à l'incertitude expérimentale : comme à l'exercice 1, le modèle isotherme est exclu. À $100$ Hz, la période est de $10$ ms et le temps caractéristique de diffusion thermique sur les dimensions de la bouteille ($\sim D^2/D_{\mathrm{th}}\sim(0{,}1)^2/(2\times10^{-5})\sim500$ s) est incomparablement plus long : la compression de l'air est bien adiabatique. (Le gradient thermique reste efficace dans une fine couche limite proche des parois, ce qui explique l'amortissement.)


**q5.** On verse de l'eau dans la bouteille de façon que le volume d'air tombe à $V'=0{,}50$ L. Calculer la nouvelle
fréquence et vérifier le sens de variation observé expérimentalement. Dans quel rapport faut-il changer
$V$ pour monter d'une octave ?

> [!success]- ✅ Correction
> $f'=f_0\sqrt{V/V'}\approx125$ Hz ; une octave exige $V'=V/4$.


> [!example]- 📝 Solution détaillée
> **Dépendance en volume**
>
> À $S$ et $\ell'$ fixés, $f_0\propto V^{-1/2}$. Donc
> $$f'=f_0\sqrt{\frac V{V'}}=102\times\sqrt{1{,}5}\approx102\times1{,}22\approx125~\text{Hz}.$$
> La note monte quand la bouteille se remplit : le ressort est plus raide ($K\propto1/V$) pour la même masse. Pour gagner une octave ($f'=2f_0$), il faut diviser le volume par quatre : $V'=V/4$.


**q6.** Montrer que le résonateur est analogue à un circuit $LC$. On définit le débit volumique
$q=S\dot\xi$. Identifier la tension, le courant, l'inductance $L_a$ et la capacité $C_a$, et retrouver
$\omega_0=1/\sqrt{L_aC_a}$.

> [!tip]- 💡 Coup de pouce
> Écrivez la loi du bouchon sous la forme $p=L_a\dot q$ et la loi de la cavité sous la forme $\dot p=q/C_a$ (au signe près selon l'orientation).


> [!success]- ✅ Correction
> $L_a=\rho_0\ell'/S$ ; $C_a=V/(\rho_0c^2)$ ; $\omega_0=1/\sqrt{L_aC_a}$.


> [!example]- 📝 Solution détaillée
> **Identification terme à terme**
>
> Le bouchon obéit à $\rho_0\ell'\,\dot q/S=-p$, c'est-à-dire $p=-L_a\dot q$ avec $L_a=\rho_0\ell'/S$ (inertance, en kg$\cdot$m$^{-4}$). La cavité obéit à $\dot p=\dfrac{\gamma P_0}{V}q=\dfrac{\rho_0c^2}{V}q$ (le volume diminue de $q\,\mathrm dt$), c'est-à-dire $q=C_a\dot p$ avec $C_a=V/(\rho_0c^2)$ (compliance). On reconnaît les équations d'un circuit $LC$ avec $p\leftrightarrow u$, $q\leftrightarrow i$, et
> $$\omega_0=\frac1{\sqrt{L_aC_a}}=\sqrt{\frac{S}{\rho_0\ell'}\times\frac{\rho_0c^2}{V}}=c\sqrt{\frac S{V\ell'}}.$$
> Cette analogie permet de traiter de grands systèmes (silencieux, instruments, haut-parleurs) comme des circuits électriques.


**q7.** Une salle parallélépipédique de longueur $L=5$ m (murs rigides) possède un mode axial gênant (boum
de basses). Calculer sa fréquence. On veut absorber ce mode avec un résonateur de Helmholtz de goulot
$S=1{,}0\times10^{-2}$ m$^2$ et $\ell'=10$ cm. Quel volume de cavité faut-il ? Commenter.

> [!tip]- 💡 Coup de pouce
> Entre deux parois rigides, les modes de pression ont des ventres aux deux bouts : $f_n=nc/(2L)$ (comme le tube ouvert-ouvert de l'exercice 2, mais ici avec des ventres de pression).


> [!success]- ✅ Correction
> $f_1=c/(2L)=34$ Hz ; $V=c^2S/(\omega_0^2\ell')\approx0{,}25$ m$^3$ = 250 L.


> [!example]- 📝 Solution détaillée
> **Mode de la salle**
>
> Le champ de pression entre deux parois rigides est un cosinus avec un ventre de pression en chaque paroi (vitesse nulle) : $kL=n\pi$, $f_n=nc/(2L)$, soit $f_1=340/10=34$ Hz.
>
> **Dimensionnement du résonateur**
>
> On impose $\omega_0=2\pi\times34\approx214~\text{rad}\cdot\text{s}^{-1}$ :
> $$V=\frac{c^2S}{\omega_0^2\ell'}=\frac{340^2\times10^{-2}}{214^2\times0{,}10}\approx\frac{1156}{4580}\approx0{,}25~\text{m}^3.$$
> Il faut une cavité de $250$ L : les basses fréquences exigent de grands volumes ($V\propto1/\omega_0^2$), ce qui explique pourquoi l'absorption des graves est coûteuse en place. Pour un résonateur plus compact, on réduit $S$ ou on allonge le col, au prix d'un amortissement plus fort et d'une bande plus étroite.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex1-celerite-d-une-onde-acoustique-dans-un-fluide-parfait|Exercice 1 — Célérité d'une onde acoustique dans un fluide parfait]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex4-reflexion-et-transmission-d-une-onde-acoustique-a-une-interface-entre-deux-fluides|Exercice 4 — Réflexion et transmission d'une onde acoustique à une interface entre deux fluides]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex8-transmission-a-travers-une-lame-adaptation-d-impedance-loi-de-masse-et-double-vitrage|Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex5-energie-intensite-acoustique-et-niveau-sonore-de-l-oreille-humaine-a-l-onde-stationnaire|Exercice 5 — Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex6-tube-d-impedance-mesurer-l-absorption-d-un-materiau-avec-une-onde-stationnaire-partielle|Exercice 6 — Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle]]

