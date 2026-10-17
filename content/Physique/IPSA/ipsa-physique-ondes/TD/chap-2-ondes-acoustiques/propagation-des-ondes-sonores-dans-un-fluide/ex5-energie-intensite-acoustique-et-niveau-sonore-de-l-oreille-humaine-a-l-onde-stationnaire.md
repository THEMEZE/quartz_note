---
title: "Exercice 5 — Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire"
tags:
  - td
  - chap-2-ondes-acoustiques
---

[[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/index|⬅ Retour]] · <a href="/pdfs/td2_PhV212_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_PhV212_enonce)</a> · <a href="/pdfs/td2_enonce.pdf" target="_blank" rel="noopener">📄 Énoncé (td2_enonce)</a> · <a href="/pdfs/td2_PhV212_aides.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_aides)</a> · <a href="/pdfs/td2_PhV212_exs_maison_aide.pdf" target="_blank" rel="noopener">📄 Aides (td2_PhV212_exs_maison_aide)</a> · <a href="/pdfs/td2_PhV212_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_PhV212_corrige)</a> · <a href="/pdfs/td2_corrige.pdf" target="_blank" rel="noopener">📄 Corrigé (td2_corrige)</a> · <a href="/pdfs/td2_PhV212_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 5. Énergie, intensité acoustique et niveau sonore : de l'oreille humaine à l'onde stationnaire *(facultatif)*

L'air est modélisé comme un fluide parfait, de masse volumique au repos
$\rho_0=1{,}2~\text{kg}\cdot\text{m}^{-3}$, de célérité $c=340~\text{m}\cdot\text{s}^{-1}$
(impédance $Z=\rho_0c=408~\text{kg}\cdot\text{m}^{-2}\cdot\text{s}^{-1}$) et de pression moyenne
$P_0=10^5$ Pa. On note $\chi=1/(\rho_0c^2)$ son coefficient de compressibilité isentropique.

On rappelle les équations de l'acoustique linéaire à une dimension :
$$\rho_0\frac{\partial v}{\partial t}=-\frac{\partial p}{\partial x},\qquad \frac{\partial\rho'}{\partial t}+\rho_0\frac{\partial v}{\partial x}=0,\qquad \rho'=\rho_0\chi\,p.$$

L'*intensité acoustique* est la moyenne temporelle de la puissance transportée par unité de surface, $I=\langle p\,v\rangle$. Le *niveau sonore* est $L=10\log_{10}(I/I_0)$ avec $I_0=10^{-12}~\text{W}\cdot\text{m}^{-2}$ (seuil d'audition à 1 kHz), exprimé en décibels (dB).

**q1.** À partir des équations linéarisées de l'énoncé, établir la loi de conservation
$\dfrac{\partial e}{\partial t}+\dfrac{\partial \Pi}{\partial x}=0$ avec
$e=\tfrac12\rho_0v^2+\tfrac12\chi p^2$ et $\Pi=pv$. Interpréter chaque terme.

> [!tip]- 💡 Coup de pouce
> Multipliez l'équation d'Euler par $v$ et la conservation de la masse (après élimination de $\rho'$) par $p$, puis additionnez.


> [!example]- 📝 Solution détaillée
> **Deux équations multipliées**
>
> En éliminant $\rho'$ grâce à $\rho'=\rho_0\chi p$, la conservation de la masse devient $\chi\,\partial_tp=-\partial_xv$. On multiplie l'équation d'Euler par $v$ et cette dernière par $p$ :
> $$\frac{\partial}{\partial t}\left(\frac12\rho_0v^2\right)=-v\frac{\partial p}{\partial x},\qquad \frac{\partial}{\partial t}\left(\frac12\chi p^2\right)=-p\frac{\partial v}{\partial x}.$$
>
> **Somme et interprétation**
>
> En additionnant, on reconnaît la dérivée d'un produit :
> $$\frac{\partial}{\partial t}\left(\frac12\rho_0v^2+\frac12\chi p^2\right)=-\frac{\partial(pv)}{\partial x}.$$
> Le premier terme est l'énergie cinétique volumique du fluide, le second l'énergie potentielle élastique stockée dans la compression ($\chi p^2/2$ est l'analogue de $Kx^2/2$ pour un ressort). Le terme $pv$ est la puissance surfacique transmise par la pression du fluide en amont à celui en aval : c'est le flux d'énergie. L'énergie ne peut que se déplacer ou changer de forme, jamais disparaître.


**q2.** Pour une onde plane progressive harmonique $p=p_0\cos(\omega t-kx)$ se propageant vers $+x$, montrer que les
énergies cinétique et potentielle volumiques sont égales à chaque instant, puis que
$\langle I\rangle=\dfrac{p_0^2}{2Z}=\dfrac{p_{\mathrm{eff}}^2}{Z}=c\,\langle e\rangle$.

> [!tip]- 💡 Coup de pouce
> Utilisez $v=p/Z$ et $\chi=1/(\rho_0c^2)$ ; remarquez que $\rho_0/Z^2=\chi$.


> [!success]- ✅ Correction
> $e_c=e_p=\chi p^2/2$ ; $e=\chi p^2$ ; $\langle I\rangle=p_0^2/(2Z)=c\langle e\rangle$.


> [!example]- 📝 Solution détaillée
> **Équipartition de l'énergie**
>
> Pour une onde progressive vers $+x$, $v=p/Z$ donc $e_c=\tfrac12\rho_0v^2=\tfrac12\dfrac{\rho_0}{Z^2}p^2=\tfrac12\dfrac{1}{\rho_0c^2}p^2=\tfrac12\chi p^2=e_p$. Les deux formes d'énergie sont égales en tout point et à tout instant, et $e=\chi p^2=p_0^2\cos^2(\omega t-kx)/(\rho_0c^2)$.
>
> **Intensité**
>
> $$I=p\,v=\frac{p^2}{Z}\quad\Longrightarrow\quad\langle I\rangle=\frac{p_0^2}{Z}\langle\cos^2\rangle=\frac{p_0^2}{2Z}=\frac{p_{\mathrm{eff}}^2}{Z},\qquad p_{\mathrm{eff}}=\frac{p_0}{\sqrt2}.$$
> Par ailleurs $\langle e\rangle=\dfrac{p_0^2}{2\rho_0c^2}$, donc $\langle I\rangle=\dfrac{p_0^2}{2\rho_0c}=c\langle e\rangle$ : l'énergie est transportée à la célérité $c$, comme toute grandeur portée par une onde non dispersive.


**q3.** Vérifier que la pression de référence $p_{\mathrm{ref}}=2\times10^{-5}$ Pa (valeur efficace) correspond bien à
$I_0$. Pour un son pur de $1$ kHz au seuil d'audition ($0$ dB), calculer les amplitudes
de pression $p_0$, de vitesse $v_0$ et de déplacement $\xi_0$ des particules de fluide.
Comparer $\xi_0$ à la taille d'un atome ($\sim10^{-10}$ m).

> [!tip]- 💡 Coup de pouce
> $\xi_0=v_0/\omega$ pour une grandeur harmonique. Attention : $p_{\mathrm{ref}}$ est une valeur efficace.


> [!success]- ✅ Correction
> $I=p_{\mathrm{ref}}^2/Z\approx9{,}8\times10^{-13}$ W/m$^2\approx I_0$ ; $p_0\approx2{,}8\times10^{-5}$ Pa ; $v_0\approx7\times10^{-8}$ m/s ; $\xi_0\approx1\times10^{-11}$ m.


> [!example]- 📝 Solution détaillée
> **Cohérence des deux seuils**
>
> $$\frac{p_{\mathrm{ref}}^2}{Z}=\frac{(2\times10^{-5})^2}{408}=\frac{4\times10^{-10}}{408}\approx9{,}8\times10^{-13}~\text{W}\cdot\text{m}^{-2}\approx I_0.$$
>
> **Amplitudes au seuil d'audition**
>
> $$p_0=\sqrt2\,p_{\mathrm{ref}}\approx2{,}8\times10^{-5}~\text{Pa},\qquad v_0=\frac{p_0}{Z}\approx\frac{2{,}8\times10^{-5}}{408}\approx6{,}9\times10^{-8}~\text{m}\cdot\text{s}^{-1},$$
> $$\xi_0=\frac{v_0}{\omega}=\frac{6{,}9\times10^{-8}}{2\pi\times10^3}\approx1{,}1\times10^{-11}~\text{m}.$$
> Le déplacement des particules d'air au seuil d'audition est environ dix fois plus petit que la taille d'un atome : ce que l'oreille détecte est un mouvement collectif de très nombreuses molécules, bien inférieur au mouvement d'agitation thermique individuel. L'oreille humaine est un détecteur d'une sensibilité extraordinaire.


**q4.** Même question pour le seuil de douleur, $120$ dB. Justifier que l'approximation acoustique
(linéarisation) reste valable même à ce niveau.

> [!tip]- 💡 Coup de pouce
> Calculez les rapports adimensionnés $p_0/P_0$ et $v_0/c$ du point cours d'ouverture de l'exercice 1.


> [!success]- ✅ Correction
> $I=1$ W/m$^2$ ; $p_0\approx29$ Pa ; $v_0\approx7\times10^{-2}$ m/s ; $\xi_0\approx11~\mu$m ; $p_0/P_0\approx3\times10^{-4}\ll1$.


> [!example]- 📝 Solution détaillée
> **Amplitudes à 120 dB**
>
> $120$ dB correspond à $I=I_0\times10^{12}=1~\text{W}\cdot\text{m}^{-2}$. D'où $p_{\mathrm{eff}}=\sqrt{IZ}=\sqrt{408}\approx20~\text{Pa}$, puis
> $$p_0=\sqrt2\,p_{\mathrm{eff}}\approx29~\text{Pa},\qquad v_0=\frac{p_0}{Z}\approx7{,}0\times10^{-2}~\text{m}\cdot\text{s}^{-1},\qquad\xi_0=\frac{v_0}{\omega}\approx1{,}1\times10^{-5}~\text{m}.$$
> Un rapport de $10^{12}$ en intensité correspond à un rapport de $10^6$ en pression et en déplacement : c'est ce qui justifie l'échelle logarithmique.
>
> **Validité de la linéarisation**
>
> $$\frac{p_0}{P_0}\approx\frac{29}{10^5}\approx3\times10^{-4},\qquad\frac{v_0}{c}\approx\frac{7\times10^{-2}}{340}\approx2\times10^{-4}.$$
> Ces rapports sont très petits devant $1$ : même au seuil de douleur, les termes d'ordre 2 (convectif, $\rho'v$, etc.) sont négligeables devant les termes d'ordre 1. L'acoustique linéaire est donc excellente pour tous les sons de la vie courante (les effets non linéaires n'apparaissent qu'au-delà de $\sim150$ dB, ou à très longue distance).


**q5.** Une personne qui parle normalement est entendue à $60$ dB à $1$ m. On la modélise comme une source
ponctuelle isotrope rayonnant une puissance acoustique $\mathcal P$ en champ libre
(onde sphérique : $I(r)=\mathcal P/(4\pi r^2)$). Calculer $\mathcal P$. À quelle distance
le niveau est-il de $40$ dB ? Combien de personnes faut-il pour émettre $1$ W acoustique ?

> [!tip]- 💡 Coup de pouce
> La puissance se conserve à travers toute sphère centrée sur la source ; passez par $I(1~\text{m})$ puis exprimez $L(r)-L(r_0)$.


> [!success]- ✅ Correction
> $\mathcal P\approx1{,}3\times10^{-5}$ W ; $r=10$ m ; environ $8\times10^4$ personnes pour $1$ W.


> [!example]- 📝 Solution détaillée
> **Puissance rayonnée**
>
> $60$ dB $\Rightarrow I(1~\text{m})=10^{-12}\times10^6=10^{-6}~\text{W}\cdot\text{m}^{-2}$, donc
> $$\mathcal P=4\pi r^2I=4\pi\times10^{-6}\approx1{,}3\times10^{-5}~\text{W}=13~\mu\text{W}.$$
> La parole est un phénomène d'une puissance dérisoire : il faudrait environ $8\times10^4$ personnes parlant en même temps pour produire $1$ W acoustique.
>
> **Décroissance avec la distance**
>
> $$L(r)-L(r_0)=10\log_{10}\frac{I(r)}{I(r_0)}=10\log_{10}\frac{r_0^2}{r^2}=-20\log_{10}\frac r{r_0}.$$
> Chaque doublement de distance coûte donc $20\log_{10}2\approx6$ dB. Pour passer de $60$ à $40$ dB, il faut $20\log_{10}(r/1)=20$ soit $r=10$ m, en champ libre et sans absorption de l'air ni bruit ambiant.


**q6.** Deux sources produisent chacune $70$ dB au point d'écoute. Quel est le niveau total si :
(a) elles sont incohérentes ; (b) elles émettent le même signal, en phase en ce point ;
(c) elles sont en opposition de phase ? Que devient (a) pour $N=100$ sources identiques ?
Calculer enfin $70$ dB $+$ $60$ dB (incohérentes) et commenter.

> [!success]- ✅ Correction
> (a) $73$ dB ; (b) $76$ dB ; (c) silence ; $N=100$ : $+20$ dB ; $70+60$ dB $\approx70{,}4$ dB.


> [!example]- 📝 Solution détaillée
> **Sources incohérentes, cohérentes en phase, en opposition**
>
> - (a) Incohérentes : les intensités s'ajoutent, $I=2I_1$, soit $L=70+10\log_{10}2\approx73$ dB. Pour $N$ sources, $L=L_1+10\log_{10}N$ : $+20$ dB pour $N=100$.
> - (b) Cohérentes en phase : les *amplitudes* s'ajoutent, $p_0=2p_1$ donc $I=4I_1$ : $L=70+20\log_{10}2\approx76$ dB. Pour $N$ sources, $+20\log_{10}N$.
> - (c) En opposition de phase : $p=0$, donc $I=0$ en ce point : c'est le principe du contrôle actif du bruit (la compensation n'est vraie qu'au voisinage d'un point, sur une distance de l'ordre de $\lambda/10$).
>
> **Niveaux différents**
>
> $$L=10\log_{10}\big(10^{7}+10^{6}\big)=10\log_{10}(1{,}1\times10^7)\approx70{,}4~\text{dB}.$$
> Une source $10$ dB plus faible n'ajoute presque rien : le bruit le plus fort domine. En pratique, on ne peut pas « cacher » un bruit fort en ajoutant des bruits faibles.


**q7.** On reprend l'onde stationnaire du tube ouvert-ouvert de l'exercice 2, de section $S$, au mode propre $n$
($kL=n\pi$) : avec $x'=L-x$ et $\varphi=\omega t-kL$,
$\Psi=2A_I\cos(kx')\cos\varphi$ et $p=-2A_I\rho_0c\,\omega\sin(kx')\cos\varphi$ ($A_I$ réel).


1. Calculer $v$, puis le flux d'énergie instantané $\Pi=pv$. Montrer que $\langle\Pi\rangle=0$.
2. Calculer les densités d'énergie cinétique $e_c$ et potentielle $e_p$, puis leurs moyennes temporelles. Où chacune est-elle maximale ?
3. Calculer l'énergie totale $E(t)$ contenue dans le tube. Commenter.

> [!tip]- 💡 Coup de pouce
> Utilisez $\sin2a=2\sin a\cos a$. Pour la dernière question, $\int_0^L\cos^2(k(L-x))\,\mathrm dx=\int_0^L\sin^2(k(L-x))\,\mathrm dx=L/2$ lorsque $kL=n\pi$.


> [!success]- ✅ Correction
> $\langle\Pi\rangle=0$ ; $\langle e\rangle=\rho_0A_I^2\omega^2$ uniforme ; $E=\rho_0A_I^2\omega^2SL$ indépendante du temps.


> [!example]- 📝 Solution détaillée
> **Flux d'énergie : nul en moyenne**
>
> $v=\partial_t\Psi=-2A_I\omega\cos(kx')\sin\varphi$. On en déduit
> $$\Pi=p\,v=\rho_0cA_I^2\omega^2\,\sin(2kx')\,\sin(2\varphi).$$
> $\Pi$ n'est pas nul instantanément (l'énergie circule entre les nœuds et les ventres), mais $\langle\sin2\varphi\rangle=0$, donc $\boxed{\langle\Pi\rangle=0}$ en tout point : $p$ et $v$ sont en quadrature temporelle, aucune énergie n'est transportée en moyenne.
>
> **Densités d'énergie**
>
> $$e_c=\tfrac12\rho_0v^2=2\rho_0A_I^2\omega^2\cos^2(kx')\sin^2\varphi,\qquad e_p=\tfrac12\chi p^2=2\rho_0A_I^2\omega^2\sin^2(kx')\cos^2\varphi.$$
> Moyennes : $\langle e_c\rangle=\rho_0A_I^2\omega^2\cos^2(kx')$, maximale aux ventres de déplacement (nœuds de pression) ; $\langle e_p\rangle=\rho_0A_I^2\omega^2\sin^2(kx')$, maximale aux ventres de pression. Leur somme est *uniforme* : $\langle e\rangle=\rho_0A_I^2\omega^2$. On vérifie que $\partial_te=2\rho_0A_I^2\omega^3\sin2\varphi\cos2kx'$ et $\partial_x\Pi=-2\rho_0A_I^2\omega^3\sin2\varphi\cos2kx'$ s'annulent bien en somme.
>
> **Énergie totale et interprétation**
>
> Avec $\int_0^L\cos^2(kx')\mathrm dx=\int_0^L\sin^2(kx')\mathrm dx=L/2$ (car $kL=n\pi$) :
> $$E(t)=S\int_0^Le\,\mathrm dx=\rho_0A_I^2\omega^2SL\,(\sin^2\varphi+\cos^2\varphi)=\rho_0A_I^2\omega^2SL=\text{cste}.$$
> L'énergie totale est constante, mais sa forme oscille : tout cinétique quand $\varphi=\pi/2$ (fluide en mouvement, pression uniforme), tout potentielle quand $\varphi=0$ (fluide immobile, comprimé). C'est exactement le comportement d'un oscillateur harmonique, d'où la notion de facteur de qualité d'un résonateur : l'énergie stockée est entretenue par un apport très faible, nécessaire seulement pour compenser les pertes.


> [!note] 🔗 Voir aussi
> [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex4-reflexion-et-transmission-d-une-onde-acoustique-a-une-interface-entre-deux-fluides|Exercice 4 — Réflexion et transmission d'une onde acoustique à une interface entre deux fluides]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex6-tube-d-impedance-mesurer-l-absorption-d-un-materiau-avec-une-onde-stationnaire-partielle|Exercice 6 — Tube d'impédance : mesurer l'absorption d'un matériau avec une onde stationnaire partielle]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex7-resonateur-de-helmholtz-la-bouteille-qui-chante|Exercice 7 — Résonateur de Helmholtz : la bouteille qui chante]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex8-transmission-a-travers-une-lame-adaptation-d-impedance-loi-de-masse-et-double-vitrage|Exercice 8 — Transmission à travers une lame : adaptation d'impédance, loi de masse et double vitrage]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex2-onde-stationnaire-tube-de-kundt-ouvert|Exercice 2 — Onde stationnaire, tube de Kundt ouvert]] · [[physique/IPSA/ipsa-physique-ondes/TD/chap-2-ondes-acoustiques/propagation-des-ondes-sonores-dans-un-fluide/ex3-onde-stationnaire-tube-de-kundt-ferme-a-faire-a-la-maison|Exercice 3 — Onde stationnaire, tube de Kundt fermé (à faire à la maison)]]

