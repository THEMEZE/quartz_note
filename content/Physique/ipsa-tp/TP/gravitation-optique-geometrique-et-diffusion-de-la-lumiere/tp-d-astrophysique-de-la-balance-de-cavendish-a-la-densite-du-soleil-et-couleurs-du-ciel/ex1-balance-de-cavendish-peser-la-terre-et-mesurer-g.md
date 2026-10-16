---
title: "Exercice 1 — Balance de Cavendish : peser la Terre et mesurer G"
tags:
  - tp
  - gravitation-optique-geometrique-et-diffusion-de-la-lumiere
---

[[physique/ipsa-tp/TP/gravitation-optique-geometrique-et-diffusion-de-la-lumiere/tp-d-astrophysique-de-la-balance-de-cavendish-a-la-densite-du-soleil-et-couleurs-du-ciel/index|⬅ Retour]] · <a href="/pdfs/TP_IPSA_Astrophysique_fiche.pdf" target="_blank" rel="noopener">📄 Fiche enseignant</a>

### Exercice 1. Balance de Cavendish : peser la Terre et mesurer G

En 1798, Henry Cavendish mesure l'attraction gravitationnelle entre deux boules de plomb de quelques dizaines de centimètres à l'aide d'un fléau suspendu à un fil de torsion. Il en déduit la densité moyenne de la Terre. Sa mesure ne donne pas $G$ directement ; c'est le lien $g=GM_T/R_T^2$ qui permet, une fois $G$ connue, de « peser » la Terre.

Dans ce TP, on utilise une balance de Cavendish de démonstration (deux petites masses $m$ au bout d'un fléau, deux grosses masses $M$ mobiles, miroir et pointeur laser) pour **mesurer $G$**, évaluer une incertitude, et identifier les erreurs systématiques. La valeur de $G$ obtenue est réutilisée dans le TP A3 pour déterminer la densité du Soleil.

**q1.** Modèle. Deux masses $m$ sont placées aux extrémités d'un fléau de longueur $2r$ (masse négligée) suspendu à un fil de constante de torsion $\kappa$. Chaque petite masse subit de la part de la grosse masse la plus proche, à la distance $b$, la force $GMm/b^2$ (on néglige d'abord l'attraction de la grosse masse sur l'autre petite masse). À l'équilibre le fléau a tourné de l'angle $\theta$. Écrire l'équation d'équilibre des moments et la période $T$ des petites oscillations. En déduire
$$G=\frac{4\pi^2\,r\,b^2\,\theta}{M\,T^2}.$$

> [!tip]- 💡 Coup de pouce
> **Deux relations**
>
> Équilibre : $\kappa\theta=2r\times\dfrac{GMm}{b^2}$. Oscillations : $I\ddot\theta=-\kappa\theta$ avec $I=2mr^2$. Éliminer $\kappa$ pour que la masse $m$ disparaisse.


> [!success]- ✅ Correction
> **Résultat**
>
> $\kappa=\dfrac{4\pi^2I}{T^2}=\dfrac{8\pi^2mr^2}{T^2}$ et $\kappa\theta=\dfrac{2rGMm}{b^2}$, d'où $G=\dfrac{4\pi^2rb^2\theta}{MT^2}$.


> [!example]- 📝 Solution détaillée
> **Démonstration**
>
> Moment des deux forces (perpendiculaires au fléau) : $\Gamma=2\times r\times\dfrac{GMm}{b^2}$. À l'équilibre, ce moment est compensé par le moment de rappel du fil : $\kappa\theta=\Gamma$.
> Sans les grosses masses, le fléau de moment d'inertie $I=2mr^2$ oscille avec la période $T=2\pi\sqrt{I/\kappa}$, donc $\kappa=\dfrac{4\pi^2I}{T^2}=\dfrac{8\pi^2mr^2}{T^2}$.
> En reportant : $\dfrac{8\pi^2mr^2}{T^2}\theta=\dfrac{2rGMm}{b^2}\Rightarrow G=\dfrac{4\pi^2rb^2\theta}{MT^2}$.
> Remarque : la mesure de $G$ se ramène à la mesure d'un angle, d'une période et de longueurs ; on n'a besoin ni de $\kappa$ ni de $m$. C'est un avantage essentiel, puisque $\kappa$ (de l'ordre de $10^{-8}\ \text{N}\cdot\text{m}/\text{rad}$) est difficile à mesurer directement.


**q2.** Levier optique. Un miroir solidaire du fléau renvoie un faisceau laser sur un écran situé à $L$ du miroir. Montrer qu'un retournement des grosses masses qui fait tourner le fléau de $2\theta$ déplace le spot de $\Delta s=4\theta L$. Application numérique pour $\Delta s=78\ \text{mm}$ et $L=3{,}00\ \text{m}$.

> [!success]- ✅ Correction
> **Résultat**
>
> Rotation du fléau : $2\theta$. Rotation du faisceau réfléchi : $4\theta$. Donc $\Delta s\approx4\theta L$ et $\theta=\dfrac{\Delta s}{4L}=6{,}5\ \text{mrad}$.


> [!example]- 📝 Solution détaillée
> **Démonstration**
>
> La loi de la réflexion entraîne que, lorsque le miroir tourne d'un angle $\alpha$, le rayon réfléchi tourne de $2\alpha$. Le retournement des grosses masses fait passer le fléau de $-\theta$ à $+\theta$, soit $\alpha=2\theta$, donc le faisceau tourne de $4\theta$. Pour de petits angles, $\Delta s=4\theta L$ :
> $$\theta=\frac{\Delta s}{4L}=\frac{0{,}078}{4\times3{,}00}=6{,}5\times10^{-3}\ \text{rad}\ (0{,}37^\circ).$$
> Ainsi $G=\dfrac{\pi^2rb^2\,\Delta s}{M\,L\,T^2}$. Le levier optique amplifie l'angle de $6{,}5\ \text{mrad}$ (déplacement du fléau de $r\theta\approx0{,}3\ \text{mm}$) en $78\ \text{mm}$ sur l'écran.


**q3.** Correction de la géométrie. Les grosses masses attirent aussi la petite masse la plus éloignée, dont le moment s'oppose au moment principal. En plaçant chaque grosse masse à la distance $b$ perpendiculairement au fléau devant une petite masse, la distance à l'autre petite masse est $D=\sqrt{b^2+4r^2}$. Montrer que le moment total est $\Gamma=\dfrac{2rGMm}{b^2}(1-\beta)$ avec $\beta=\dfrac{b^3}{D^3}$. Calculer $\beta$ pour $b=46\ \text{mm}$ et $r=50\ \text{mm}$. Quelle conséquence sur $G$ ?

> [!tip]- 💡 Coup de pouce
> **Composante utile**
>
> La force de la grosse masse $A$ sur la petite masse éloignée fait un angle avec la perpendiculaire au fléau : sa composante utile est $\dfrac{GMm}{D^2}\times\dfrac{b}{D}$, avec un bras de levier $r$ et un signe opposé.


> [!success]- ✅ Correction
> **Résultat**
>
> $\beta=\dfrac{b^3}{(b^2+4r^2)^{3/2}}\approx0{,}073$. Sans correction, $G$ serait sous-estimée de $7{,}3\ \%$ ; la vraie valeur est $G=\dfrac{G_{\text{brut}}}{1-\beta}$.


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> Pour la grosse masse $A$ proche de la petite masse $1$ : moment $+r\dfrac{GMm}{b^2}$. Sur la petite masse $2$ (à la distance $D=\sqrt{b^2+4r^2}$), la force vaut $\dfrac{GMm}{D^2}$, avec une composante perpendiculaire au fléau $\dfrac{GMm}{D^2}\cdot\dfrac{b}{D}$, dirigée en sens inverse du moment principal, avec le bras de levier $r$ : moment $-r\dfrac{GMm\,b}{D^3}$. Le moment total de $A$ vaut $r\,GMm\left(\dfrac{1}{b^2}-\dfrac{b}{D^3}\right)=\dfrac{r\,GMm}{b^2}\left(1-\dfrac{b^3}{D^3}\right)$. La masse $B$ apporte la même contribution. D'où $\Gamma=\dfrac{2rGMm}{b^2}(1-\beta)$.
> $D^2=0{,}046^2+4\times0{,}05^2=0{,}012116\ \text{m}^2$, $D^3=1{,}334\times10^{-3}\ \text{m}^3$, $b^3=9{,}73\times10^{-5}\ \text{m}^3$, donc $\beta=0{,}073$.
> $$G=\frac{\pi^2rb^2\,\Delta s}{M\,L\,T^2\,(1-\beta)}.$$
> Cette correction est un effet de $7\ \%$ : plus grande que l'incertitude statistique. Une critique sérieuse de l'expérience ne peut pas l'ignorer.


**q4.** Calculer $G$ avec les données de l'énoncé, avant puis après correction. Estimer l'incertitude relative sur $G$ (i) par la méthode logarithmique en somme absolue (TD2 exercice 8), (ii) en somme quadratique (TD2 exercice 9). Comparer avec la valeur tabulée $6{,}674\times10^{-11}\ \text{N}\cdot\text{m}^2\cdot\text{kg}^{-2}$.

> [!tip]- 💡 Coup de pouce
> **Exposants**
>
> $G\propto r\,b^2\,\Delta s\,M^{-1}L^{-1}T^{-2}$ : les exposants $1,2,1,-1,-1,-2$ pondèrent les incertitudes relatives (le facteur $1-\beta$ est traité à part).


> [!success]- ✅ Correction
> **Résultat**
>
> $G_{\text{brut}}\approx6{,}21\times10^{-11}$ et $G\approx6{,}70\times10^{-11}\ \text{N}\cdot\text{m}^2\cdot\text{kg}^{-2}$ après correction. $\dfrac{\Delta G}{G}\approx10{,}8\ \%$ (somme absolue) ou $5{,}5\ \%$ (somme quadratique). Résultat : $G=(6{,}7\pm0{,}4)\times10^{-11}$ en quadratique, compatible avec $6{,}674\times10^{-11}$ (écart $0{,}3\ \%$).


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> $$G_{\text{brut}}=\frac{\pi^2\times0{,}050\times0{,}046^2\times0{,}078}{1{,}50\times3{,}00\times540^2}\approx6{,}21\times10^{-11},\qquad G=\frac{6{,}21\times10^{-11}}{1-0{,}073}\approx6{,}70\times10^{-11}.$$
> Incertitudes relatives : $\dfrac{\Delta r}{r}=1{,}0\ \%$ ($\times1$), $\dfrac{\Delta b}{b}=2{,}2\ \%$ ($\times2$, soit $4{,}3\ \%$), $\dfrac{\Delta\Delta s}{\Delta s}=2{,}6\ \%$, $\dfrac{\Delta M}{M}=0{,}7\ \%$, $\dfrac{\Delta L}{L}=0{,}3\ \%$, $\dfrac{\Delta T}{T}=0{,}9\ \%$ ($\times2$, soit $1{,}9\ \%$).
>
>
> - Somme absolue : $1{,}0+4{,}3+2{,}6+0{,}7+0{,}3+1{,}9\approx10{,}8\ \%$.
> - Somme quadratique : $\sqrt{1{,}0^2+4{,}3^2+2{,}6^2+0{,}7^2+0{,}3^2+1{,}9^2}\approx5{,}5\ \%$, soit $\Delta G\approx0{,}37\times10^{-11}$.
>
>
> La distance $b$ domine l'incertitude (elle intervient au carré et elle est mal définie, car $b$ dépend de la position exacte du fléau). Améliorer la mesure de $b$ est la priorité.


**q5.** Critique des mesures. Pour chacune des sources suivantes, dire dans quel sens elle biaise $G$ et proposer une manière de la contrôler : (a) équilibre non atteint, (b) courants d'air et gradients thermiques, (c) forces électrostatiques, (d) attraction des murs, de la table et de l'opérateur, (e) fil de torsion non linéaire et dérive, (f) fléau de masse non nulle, (g) mesure de $b$.

> [!success]- ✅ Correction
> **Résultat**
>
> (a) sous-estime $\Delta s$, donc $G$ ; ajuster l'équilibre par une loi sinusoïde amortie. (b) bruit et dérive ; boîtier fermé, pièce thermostatée, mesures de nuit. (c) forces parasites de charges statiques ; boîtier métallique relié à la terre, ne pas toucher le verre. (d) masses proches ; s'éloigner, opérer à distance en pilotant le retournement. (e) dérive lente ; comparer plusieurs cycles A-B-A-B. (f) $I$ plus grand, $T$ plus grand, $G$ surestimée ; l'inclure dans $I$. (g) $b$ étant au carré, dominante ; la mesurer avec un pied à coulisse à travers la vitre.


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> - **(a) Équilibre non atteint :** la position d'équilibre se situe entre deux extrema successifs (moyenne pondérée). Lire un extremum comme équilibre ferait une erreur de l'ordre de l'amplitude d'oscillation (parfois $50\ \%$ de $\Delta s$).
> - **(b) Convection :** un gradient de température de $0{,}1\ \text{K}$ entre deux côtés du boîtier suffit à produire des courants d'air dont la force sur le fléau est comparable à l'attraction gravitationnelle. Cavendish observait la balance à distance, avec une lunette, depuis une pièce voisine, précisément pour cette raison.
> - **(c) Électrostatique :** des charges de surface sur le verre ou sur les boules peuvent produire des forces de même ordre que $10^{-10}\ \text{N}$.
> - **(d) Masses parasites :** la personne qui s'approche (masse $70\ \text{kg}$ à $1\ \text{m}$) attire le fléau avec un moment comparable à celui des grosses masses : $\dfrac{70/1^2}{1{,}5/0{,}046^2}\approx10\ \%$ du signal en ordre de grandeur pour la petite masse.
> - **(e) Fil :** l'anélasticité fait dériver la position de repos ; le remède est de mesurer plusieurs cycles et de tenir compte de la dérive.
> - **(f) Fléau :** le moment d'inertie du fléau augmente $I$, donc $T$ ; comme $G\propto1/T^2$, ignorer ce moment surestime $\kappa$, donc $G$.
> - **(g) $b$ :** $\dfrac{\Delta G}{G}=2\dfrac{\Delta b}{b}$. Une erreur de $1\ \text{mm}$ sur $46\ \text{mm}$ donne $4{,}3\ \%$.


**q6.** Peser la Terre. Avec $g=9{,}81\ \text{m}\cdot\text{s}^{-2}$ et $R_T=6{,}371\times10^{6}\ \text{m}$, calculer la masse $M_T$ et la densité moyenne $\rho_T$ de la Terre à partir de votre valeur de $G$. Comparer avec la valeur de Cavendish ($5{,}45\ \text{g}\cdot\text{cm}^{-3}$) et avec les densités du granite ($2{,}7$) et du fer ($7{,}9$). Que peut-on en conclure sur l'intérieur de la Terre ?

> [!success]- ✅ Correction
> **Résultat**
>
> $M_T=\dfrac{gR_T^2}{G}\approx5{,}97\times10^{24}\ \text{kg}$ (avec $G=6{,}674\times10^{-11}$) et $\rho_T=\dfrac{3g}{4\pi GR_T}\approx5{,}5\times10^{3}\ \text{kg}\cdot\text{m}^{-3}$. Avec $G=6{,}70\times10^{-11}$ : $M_T\approx5{,}94\times10^{24}\ \text{kg}$ et $\rho_T\approx5{,}49\times10^{3}\ \text{kg}\cdot\text{m}^{-3}$. La densité moyenne est le double de celle du granite : l'intérieur est bien plus dense que la croûte (noyau de fer et de nickel).


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> $g=\dfrac{GM_T}{R_T^2}\Rightarrow M_T=\dfrac{gR_T^2}{G}=\dfrac{9{,}81\times(6{,}371\times10^6)^2}{6{,}674\times10^{-11}}\approx5{,}97\times10^{24}\ \text{kg}$.
> $\rho_T=\dfrac{M_T}{\frac{4}{3}\pi R_T^3}=\dfrac{3g}{4\pi GR_T}\approx5{,}51\times10^3\ \text{kg}\cdot\text{m}^{-3}$.
> La croûte est constituée de roches de densité $2{,}7$ à $3{,}3$ ; la densité moyenne de $5{,}5$ impose donc un intérieur plus dense (noyau métallique de densité $10$ à $13$ vers le centre). C'est la conclusion de Cavendish en 1798 : la Terre n'est pas creuse et est bien plus dense que ses roches de surface.


> [!note] 🔗 Voir aussi
> [[physique/ipsa-tp/TP/gravitation-optique-geometrique-et-diffusion-de-la-lumiere/tp-d-astrophysique-de-la-balance-de-cavendish-a-la-densite-du-soleil-et-couleurs-du-ciel/ex3-densite-du-soleil-de-cavendish-au-stenope|Exercice 3 — Densité du Soleil : de Cavendish au sténopé]]

