---
title: "Exercice 3 — Densité du Soleil : de Cavendish au sténopé"
tags:
  - tp
  - gravitation-optique-geometrique-et-diffusion-de-la-lumiere
---

[[physique/ipsa-tp/TP/gravitation-optique-geometrique-et-diffusion-de-la-lumiere/tp-d-astrophysique-de-la-balance-de-cavendish-a-la-densite-du-soleil-et-couleurs-du-ciel/index|⬅ Retour]] · [📄 Fiche enseignant](/pdfs/TP_IPSA_Astrophysique_fiche.pdf)

### Exercice 3. Densité du Soleil : de Cavendish au sténopé

Sans quitter la Terre, on peut trouver la densité moyenne du Soleil à partir de trois mesures : la constante de gravitation $G$ (TP A1, balance de Cavendish), le diamètre angulaire du Soleil $\theta$ (TP A2, sténopé) et la durée d'une année $T$. Aucune distance n'est nécessaire.

L'idée : la troisième loi de Kepler donne la combinaison $GM_\odot$, mais pas $M_\odot$ ; il faut $G$ pour passer à la masse. Le rayon s'obtient avec le sténopé si on connaît la distance, mais la distance disparaît dans le calcul de la densité.

On utilisera les résultats obtenus dans les TP précédents. À défaut, prendre $G=(6{,}70\pm0{,}37)\times10^{-11}\ \text{m}^3\cdot\text{kg}^{-1}\cdot\text{s}^{-2}$, $\theta=(9{,}31\pm0{,}28)\ \text{mrad}$ et $T=1\ \text{an}=3{,}156\times10^{7}\ \text{s}$.

**q1.** Établir la relation $GM_\odot=\dfrac{4\pi^2a^3}{T^2}$ pour une orbite circulaire de rayon $a$ et de période $T$ (Terre de masse $m\ll M_\odot$).

> [!success]- ✅ Correction
> **Résultat**
>
> $\dfrac{GM_\odot m}{a^2}=m\,a\left(\dfrac{2\pi}{T}\right)^2\Rightarrow GM_\odot=\dfrac{4\pi^2a^3}{T^2}$.


> [!example]- 📝 Solution détaillée
> **Démonstration**
>
> PFD appliqué à la Terre en mouvement circulaire uniforme autour du Soleil (référentiel héliocentrique supposé galiléen) : la force gravitationnelle $\dfrac{GM_\odot m}{a^2}$ est centripète et vaut $m\,\omega^2a$ avec $\omega=\dfrac{2\pi}{T}$. Donc $GM_\odot=\omega^2a^3=\dfrac{4\pi^2a^3}{T^2}$, ce qui est la troisième loi de Kepler ($a^3/T^2$ est constante). Numériquement, $GM_\odot=\dfrac{4\pi^2\times(1{,}496\times10^{11})^3}{(3{,}156\times10^{7})^2}=1{,}327\times10^{20}\ \text{m}^3\cdot\text{s}^{-2}$.


**q2.** Montrer que la densité moyenne du Soleil s'écrit
$$\rho_\odot=\frac{3\pi}{G\,T^2}\left(\frac{a}{R_\odot}\right)^3=\frac{24\pi}{G\,T^2\,\theta^3}$$
où $\theta$ est le diamètre angulaire ($\theta=2R_\odot/a$). Vérifier l'homogénéité. Pourquoi la distance $a$ n'apparaît-elle plus ?

> [!success]- ✅ Correction
> **Résultat**
>
> $\rho=\dfrac{M}{\frac{4}{3}\pi R^3}=\dfrac{3}{4\pi R^3}\cdot\dfrac{4\pi^2a^3}{GT^2}=\dfrac{3\pi}{GT^2}\left(\dfrac{a}{R}\right)^3$ et $\dfrac{a}{R}=\dfrac{2}{\theta}$. Homogénéité : $[GT^2]=\text{m}^3\cdot\text{kg}^{-1}$, donc $\rho$ en $\text{kg}\cdot\text{m}^{-3}$. Seul le rapport $a/R$, égal à $2/\theta$, intervient.


> [!example]- 📝 Solution détaillée
> **Démonstration**
>
> $M_\odot=\dfrac{4\pi^2a^3}{GT^2}$ (question 1) et $V=\dfrac{4}{3}\pi R_\odot^3$ donnent
> $$\rho_\odot=\frac{4\pi^2a^3}{GT^2}\cdot\frac{3}{4\pi R_\odot^3}=\frac{3\pi}{GT^2}\left(\frac{a}{R_\odot}\right)^3.$$
> Avec $\theta=\dfrac{2R_\odot}{a}$, $\left(\dfrac{a}{R_\odot}\right)^3=\dfrac{8}{\theta^3}$ et $\rho_\odot=\dfrac{24\pi}{GT^2\theta^3}$.
> Homogénéité : $G=\text{m}^3\cdot\text{kg}^{-1}\cdot\text{s}^{-2}$, donc $GT^2=\text{m}^3\cdot\text{kg}^{-1}$ et $\dfrac{1}{GT^2}=\text{kg}\cdot\text{m}^{-3}$ ; $\theta$ est sans dimension. L'expression est bien une masse volumique.
> $a$ disparaît car masse et volume varient tous les deux comme $a^3$ : seul le **rapport** entre la taille de l'orbite et celle du Soleil compte, et il est donné par l'angle.


**q3.** Calculer $\rho_\odot$ avec $G=6{,}70\times10^{-11}\ \text{m}^3\cdot\text{kg}^{-1}\cdot\text{s}^{-2}$, $T=3{,}156\times10^{7}\ \text{s}$ et $\theta=9{,}31\ \text{mrad}$. Calculer aussi $M_\odot$ et $R_\odot$. Comparer avec les valeurs tabulées ($\rho=1408\ \text{kg}\cdot\text{m}^{-3}$, $M=1{,}989\times10^{30}\ \text{kg}$, $R=6{,}957\times10^{8}\ \text{m}$).

> [!success]- ✅ Correction
> **Résultat**
>
> $\rho_\odot\approx1{,}40\times10^{3}\ \text{kg}\cdot\text{m}^{-3}$ ($1{,}4\ \text{g}\cdot\text{cm}^{-3}$), $M_\odot\approx1{,}98\times10^{30}\ \text{kg}$, $R_\odot\approx6{,}96\times10^{8}\ \text{m}$.


> [!example]- 📝 Solution détaillée
> **Application numérique**
>
> $\theta^3=(9{,}31\times10^{-3})^3=8{,}07\times10^{-7}$ ; $T^2=9{,}96\times10^{14}\ \text{s}^2$ ; $GT^2\theta^3=6{,}70\times10^{-11}\times9{,}96\times10^{14}\times8{,}07\times10^{-7}=5{,}38\times10^{-2}\ \text{m}^3\cdot\text{kg}^{-1}$.
> $$\rho_\odot=\frac{24\pi}{5{,}38\times10^{-2}}=\frac{75{,}4}{5{,}38\times10^{-2}}\approx1{,}40\times10^{3}\ \text{kg}\cdot\text{m}^{-3}.$$
> $M_\odot=\dfrac{GM_\odot}{G}=\dfrac{1{,}327\times10^{20}}{6{,}70\times10^{-11}}\approx1{,}98\times10^{30}\ \text{kg}$ ; $R_\odot=\dfrac{a\theta}{2}=6{,}96\times10^{8}\ \text{m}$. Les trois valeurs sont à moins de $1\ \%$ des valeurs de référence. Remarque : la proximité est en partie due à la compensation d'erreurs ; l'incertitude estimée (question 4) est plus grande que l'écart.


**q4.** Propager les incertitudes : établir $\dfrac{\Delta\rho}{\rho}$ (somme absolue puis quadratique), calculer $\Delta\rho$ et écrire le résultat avec les bons chiffres significatifs. Quelle mesure limite la précision ? Que faut-il améliorer pour diviser $\Delta\rho$ par $2$ ?

> [!tip]- 💡 Coup de pouce
> **Exposants**
>
> $\rho\propto G^{-1}T^{-2}\theta^{-3}$. Avec $\dfrac{\Delta G}{G}=5{,}5\ \%$, $\dfrac{\Delta\theta}{\theta}=3\ \%$ et $\dfrac{\Delta T}{T}\approx0$.


> [!success]- ✅ Correction
> **Résultat**
>
> $\dfrac{\Delta\rho}{\rho}=\dfrac{\Delta G}{G}+3\dfrac{\Delta\theta}{\theta}\approx5{,}5+9{,}0=14{,}5\ \%$ (somme absolue) ou $\sqrt{5{,}5^2+9{,}0^2}\approx10{,}5\ \%$ (quadratique). Résultat : $\rho_\odot=(1{,}4\pm0{,}2)\times10^{3}\ \text{kg}\cdot\text{m}^{-3}$ en somme absolue, $(1{,}40\pm0{,}15)\times10^{3}$ en quadratique. La mesure de $\theta$ contribue à $62\ \%$ de la somme absolue.


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> $\ln\rho=\ln24\pi-\ln G-2\ln T-3\ln\theta$, donc $\dfrac{\Delta\rho}{\rho}=\dfrac{\Delta G}{G}+2\dfrac{\Delta T}{T}+3\dfrac{\Delta\theta}{\theta}$ ; $T$ est connue à mieux que $10^{-6}$.
> Contributions : $G$ : $5{,}5\ \%$ ; $\theta$ : $3\times3=9{,}0\ \%$. Somme absolue $14{,}5\ \%$, $\Delta\rho\approx0{,}20\times10^{3}$ ; somme quadratique $10{,}5\ \%$, $\Delta\rho\approx0{,}15\times10^{3}$.
> La valeur tabulée ($1408$) est à l'intérieur de l'incertitude. La mesure de $\theta$ domine : améliorer $\Delta\theta/\theta$ de $3\ \%$ à $1\ \%$ ramène l'incertitude quadratique à $\sqrt{5{,}5^2+3^2}=6{,}3\ \%$, soit une division de $\Delta\rho$ par $1{,}7$. Pour la diviser par $2$, il faut aussi améliorer $G$ (en corrigeant les mesures de $b$ dans le TP A1).


**q5.** Critique. Pour chacune des hypothèses suivantes, dire dans quel sens elle influence $\rho_\odot$ : (a) orbite circulaire alors que $e=0{,}0167$, (b) $\theta$ mesuré un jour de janvier (périhélie) ou de juillet (aphélie), (c) image sténopéique plus large que l'image géométrique à cause du flou, (d) $M_\odot$ mesurée avec la Terre incluse, (e) choix de la définition du bord du Soleil.

> [!success]- ✅ Correction
> **Résultat**
>
> (a) négligeable : la troisième loi reste exacte avec $a$ le demi-grand axe. (b) $\theta$ varie de $\pm1{,}7\ \%$ : $\rho\propto\theta^{-3}$ varie de $\mp5\ \%$ ; utiliser $\theta$ moyen ou la valeur à la date avec $a$ de la date. (c) $\theta$ surestimé donc $\rho$ sous-estimé de $3\times\dfrac{s}{D\theta}$ ; l'ajustement avec ordonnée à l'origine corrige. (d) $m/M=3\times10^{-6}$, négligeable. (e) la photosphère n'a pas un bord net : correction de l'ordre de $0{,}1\ \%$ sur $R$.


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> - **(a)** La troisième loi est exacte en ellipse avec le demi-grand axe $a$ ; pour l'obtenir avec $a/R$ il faut le diamètre angulaire *moyen* $\bar\theta=9{,}30\ \text{mrad}$ (la valeur en $a$ moyen). L'excentricité ne modifie pas la formule.
> - **(b)** La distance Terre-Soleil varie de $1{,}471$ à $1{,}521\times10^{11}\ \text{m}$ ($\pm1{,}7\ \%$), donc $\theta$ de $9{,}15$ à $9{,}46\ \text{mrad}$. Si l'on utilise $\theta$ mesuré en janvier avec le $a$ moyen, on introduit une erreur relative $3\times1{,}7\approx5\ \%$ sur $\rho$ : erreur systématique de même ordre que l'incertitude statistique. Il faut donc noter la date de mesure ou utiliser la distance instantanée.
> - **(c)** Dans le TP A2, $d=D\theta+s$ : un ajustement affine élimine $s$. Avec la simple proportion $d/D$, à $D=1\ \text{m}$ et $s=1\ \text{mm}$, $\theta$ est surestimé de $11\ \%$, ce qui sous-estime $\rho$ de $\approx27\ \%$.
> - **(d)** La masse de la Terre est $3\times10^{-6}M_\odot$ : négligeable.
> - **(e)** Le Soleil est une sphère gazeuse sans surface solide ; le bord de la photosphère ($\tau=2/3$) est défini à environ $0{,}1\ \%$ près.
>
>
> La densité obtenue est une densité **moyenne** : le Soleil n'est pas homogène.


**q6.** Comparer $\rho_\odot$ avec celles de l'eau, de la Terre (calculée dans le TP A1, question 6) et de Jupiter ($1330\ \text{kg}\cdot\text{m}^{-3}$). Comment un objet de densité proche de l'eau peut-il être une boule de gaz à $5\,800\ \text{K}$ en surface ? Et pourquoi ne s'effondre-t-il pas ?

> [!success]- ✅ Correction
> **Résultat**
>
> $\rho_\odot/\rho_{\text{eau}}\approx1{,}4$ ; $\rho_\odot/\rho_{\text{Terre}}\approx0{,}26$ ; $\rho_\odot\approx\rho_{\text{Jupiter}}$. La densité est moyenne : gaz comprimé par sa propre gravité (centre à $150\ \text{g}\cdot\text{cm}^{-3}$). L'équilibre est hydrostatique : la pression interne, entretenue par la fusion, compense la gravité.


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> Le Soleil est presque uniquement composé d'hydrogène (73 %) et d'hélium (25 %). La densité moyenne est comparable à celle de l'eau parce que la gravité comprime fortement le gaz, dont la pression centrale atteint $2\times10^{16}\ \text{Pa}$. À ces densités et à $1{,}5\times10^{7}\ \text{K}$, le gaz est complètement ionisé (plasma) et se comporte comme un gaz parfait. Le Soleil ne s'effondre pas car le gradient de pression équilibre la pesanteur ($\mathrm{d}P/\mathrm{d}r=-\rho g$) : la pression thermique est entretenue par l'énergie des réactions de fusion.
> Jupiter (densité voisine) est un cas différent : sa pression interne résulte de la dégénérescence électronique et non de la fusion.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-tp/TP/gravitation-optique-geometrique-et-diffusion-de-la-lumiere/tp-d-astrophysique-de-la-balance-de-cavendish-a-la-densite-du-soleil-et-couleurs-du-ciel/ex1-balance-de-cavendish-peser-la-terre-et-mesurer-g|Exercice 1 — Balance de Cavendish : peser la Terre et mesurer G]]

