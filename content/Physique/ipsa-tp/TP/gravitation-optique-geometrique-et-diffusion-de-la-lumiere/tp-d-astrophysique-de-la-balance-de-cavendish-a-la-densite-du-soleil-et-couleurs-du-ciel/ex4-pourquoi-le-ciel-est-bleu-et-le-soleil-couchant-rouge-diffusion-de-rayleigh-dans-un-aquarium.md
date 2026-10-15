---
title: "Exercice 4 — Pourquoi le ciel est bleu et le Soleil couchant rouge : diffusion de Rayleigh dans un aquarium"
tags:
  - tp
  - gravitation-optique-geometrique-et-diffusion-de-la-lumiere
---

[[physique/ipsa-tp/TP/gravitation-optique-geometrique-et-diffusion-de-la-lumiere/tp-d-astrophysique-de-la-balance-de-cavendish-a-la-densite-du-soleil-et-couleurs-du-ciel/index|⬅ Retour]] · [📄 Fiche enseignant](/pdfs/TP_IPSA_Astrophysique_fiche.pdf)

### Exercice 4. Pourquoi le ciel est bleu et le Soleil couchant rouge : diffusion de Rayleigh dans un aquarium

La lumière du Soleil est blanche, et pourtant le ciel est bleu à midi alors que le Soleil paraît rouge-orangé à l'horizon. Les deux observations viennent de la même cause : la **diffusion de Rayleigh** de la lumière par les molécules de l'air, dont l'intensité varie en $\lambda^{-4}$. Le bleu est diffusé dans toutes les directions (d'où le ciel bleu) et il est donc retiré du faisceau direct ; plus le trajet dans l'atmosphère est long, plus le faisceau direct devient rouge.

Dans ce TP, on reproduit l'effet à petite échelle : un bac d'eau très légèrement troublée (quelques gouttes de lait) est éclairé par une lampe blanche. Vu de côté, le faisceau est bleuté ; vu dans l'axe, à travers une grande longueur d'eau, le spot devient orange. On **mesure** ensuite le rapport des coefficients d'extinction dans le bleu et dans le rouge à l'aide de photographies du smartphone.

**q1.** Diffusion de Rayleigh. L'intensité diffusée par des particules petites devant $\lambda$ varie comme $\lambda^{-4}$. Calculer les rapports $\dfrac{I(450\ \text{nm})}{I(650\ \text{nm})}$ et $\dfrac{I(400\ \text{nm})}{I(450\ \text{nm})}$. Pourquoi le ciel n'est-il pas violet, alors que le violet est plus diffusé que le bleu ?

> [!success]- ✅ Correction
> **Résultat**
>
> $\left(\dfrac{650}{450}\right)^4\approx4{,}35$ et $\left(\dfrac{450}{400}\right)^4\approx1{,}6$. Le violet est plus diffusé que le bleu, mais le Soleil en émet moins, le haut de l'atmosphère l'absorbe (ozone) et l'œil y est moins sensible : le ciel apparaît bleu clair.


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> $\dfrac{I(450)}{I(650)}=\left(\dfrac{650}{450}\right)^4=1{,}444^4=4{,}35$ : le bleu est diffusé $4$ fois plus que le rouge. $\dfrac{I(400)}{I(450)}=\left(\dfrac{450}{400}\right)^4=1{,}6$.
> Le ciel n'est pas violet parce que (i) le spectre du Soleil décroît vers le violet à la surface de la Terre, (ii) le violet est plus absorbé (ozone et diffusions multiples), (iii) l'œil est bien moins sensible à $400\ \text{nm}$ qu'à $470\ \text{nm}$ (les cônes bleus ont leur maximum de sensibilité vers $440$ à $450\ \text{nm}$, mais leurs signaux se combinent avec ceux des cônes verts). Le produit de ces facteurs donne la teinte cyan/bleu clair du ciel.


**q2.** Atmosphère et coucher de Soleil. L'épaisseur optique verticale de l'atmosphère à $550\ \text{nm}$ vaut $\tau_0\approx0{,}10$ (diffusion de Rayleigh seule). (a) Calculer $\tau$ à $450$, $550$ et $650\ \text{nm}$ pour un faisceau vertical. (b) Pour un Soleil à l'horizon, la masse d'air relative vaut $m\approx38$. Calculer la transmission $e^{-m\tau}$ dans chaque couleur. Quelle est la couleur du Soleil ? (c) Le Soleil est-il plus rouge quand il est bas sur l'horizon ou à $45^\circ$ ($m=1{,}41$) ?

> [!tip]- 💡 Coup de pouce
> **Loi d'échelle**
>
> $\tau(\lambda)=\tau_0\left(\dfrac{550}{\lambda}\right)^4$ et $T=e^{-m\tau}$.


> [!success]- ✅ Correction
> **Résultat**
>
> (a) $\tau=0{,}223\ ;\ 0{,}100\ ;\ 0{,}051$. (b) Transmission à l'horizon : $2\times10^{-4}$ (bleu), $0{,}022$ (vert), $0{,}14$ (rouge) : il ne reste que le rouge, le Soleil est rouge-orangé et bien moins brillant. (c) À $45^\circ$ : $T_B=0{,}73$, $T_G=0{,}87$, $T_R=0{,}93$ : le Soleil est légèrement jaune.


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> (a) $\tau(450)=0{,}10\times\left(\dfrac{550}{450}\right)^4=0{,}10\times2{,}23=0{,}223$ ; $\tau(650)=0{,}10\times\left(\dfrac{550}{650}\right)^4=0{,}051$.
> (b) $m=38$ : $T_B=e^{-8{,}5}=2{,}1\times10^{-4}$, $T_G=e^{-3{,}8}=0{,}022$, $T_R=e^{-1{,}95}=0{,}14$. Le rapport rouge/bleu vaut $\approx700$ : la lumière directe est rouge. En pratique, l'absorption et la diffusion de Mie par les aérosols renforcent l'effet (couchers de soleil très rouges après une éruption volcanique).
> (c) À $45^\circ$ : $T_B=e^{-0{,}31}=0{,}73$, $T_G=e^{-0{,}14}=0{,}87$, $T_R=e^{-0{,}072}=0{,}93$ : la lumière directe est un peu jaunie, ce qui est le cas du Soleil « jaune » de l'après-midi. Le Soleil est en réalité blanc au-dessus de l'atmosphère.
> Le 12 août 2026, l'éclipse partielle avait lieu alors que le Soleil était bas sur l'horizon ouest : le disque était à la fois rouge-orangé (extinction) et partiellement masqué (Lune).


**q3.** Analyse des mesures. Avec les données de l'énoncé, tracer $\ln(I/I_0)$ en fonction de $L$ pour les canaux rouge et bleu. Ajuster deux droites passant par l'origine, en déduire $\alpha_R$, $\alpha_B$ et le rapport $\alpha_B/\alpha_R$. Comparer avec $\left(\dfrac{\lambda_R}{\lambda_B}\right)^4$ pour $\lambda_R=620\ \text{nm}$ et $\lambda_B=450\ \text{nm}$.

> [!tip]- 💡 Coup de pouce
> **Linéarisation**
>
> $\ln\dfrac{I}{I_0}=-\alpha L$. La pente d'un ajustement par l'origine est $-\dfrac{\sum L_i\ln(I_i/I_0)}{\sum L_i^2}$.


> [!success]- ✅ Correction
> **Résultat**
>
> $\alpha_R\approx0{,}0100\ \text{cm}^{-1}$ et $\alpha_B\approx0{,}0358\ \text{cm}^{-1}$, donc $\dfrac{\alpha_B}{\alpha_R}\approx3{,}6$, en accord avec $\left(\dfrac{620}{450}\right)^4=3{,}60$.


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> Rouge : $\ln(I/I_0)=-0{,}105\ ;\ -0{,}198\ ;\ -0{,}301\ ;\ -0{,}400$ pour $L=10\ ;\ 20\ ;\ 30\ ;\ 40\ \text{cm}$, donc $\alpha_R=\dfrac{1{,}05+3{,}96+9{,}03+16{,}0}{100+400+900+1600}=\dfrac{30{,}04}{3000}=0{,}0100\ \text{cm}^{-1}$.
> Bleu : $\ln(I/I_0)=-0{,}357\ ;\ -0{,}713\ ;\ -1{,}079\ ;\ -1{,}427$, donc $\alpha_B=\dfrac{3{,}57+14{,}26+32{,}37+57{,}08}{3000}=\dfrac{107{,}3}{3000}=0{,}0358\ \text{cm}^{-1}$.
> Rapport $\dfrac{\alpha_B}{\alpha_R}\approx3{,}6$. La loi de Rayleigh prévoit $\left(\dfrac{620}{450}\right)^4=3{,}60$ pour les longueurs d'onde effectives des canaux rouge et bleu d'un capteur RGB (le canal n'est pas monochromatique : l'écart est de l'ordre de $10\ \%$ selon les longueurs d'onde choisies).
> Mise en garde : les longueurs d'onde effectives des canaux dépendent du capteur ; un accord meilleur que $10\ \%$ serait fortuit.


**q4.** Critique. Citer trois causes d'erreur sur $\alpha_B/\alpha_R$ dans la manipulation et proposer comment les contrôler.

> [!success]- ✅ Correction
> **Résultat**
>
> Saturation du capteur ; diffusion multiple (trop de lait) ; lumière ambiante ; balance des blancs automatique ; largeur des canaux RGB ; homogénéité de la suspension.


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> - **Capteur :** saturation (surexposition du canal rouge) et non-linéarité (gamma) des images JPEG. Utiliser des images RAW, ou vérifier la linéarité avec des filtres gris.
> - **Diffusion multiple :** si l'eau est trop trouble, le faisceau n'obéit plus à Beer-Lambert. Contrôle : vérifier que $\ln(I/I_0)$ est linéaire en $L$.
> - **Lumière parasite :** lumière ambiante et réflexions sur les parois du bac. Utiliser un cache, un papier noir et une pièce sombre.
> - **Balance des blancs automatique :** elle modifie le rapport bleu/rouge. La bloquer.
> - **Lumière de la lampe :** une LED blanche a un pic bleu et un large fond jaune ; $I_0$ doit être mesurée dans chaque canal.


**q5.** Polarisation. Observer le faisceau à $90^\circ$ à travers un polariseur. (a) Que voit-on quand on tourne le polariseur ? (b) Justifier avec le modèle du dipôle rayonnant : le champ $\vec E$ de la lumière incidente est perpendiculaire à la direction de propagation ; il fait osciller les charges de la molécule dans le plan perpendiculaire. (c) Où faut-il regarder dans le ciel pour observer la polarisation maximale ? Pour quelle direction est-elle nulle ?

> [!success]- ✅ Correction
> **Résultat**
>
> (a) L'intensité passe d'un maximum à un minimum presque nul quand on tourne le polariseur de $90^\circ$. (b) Les charges oscillent perpendiculairement au faisceau incident ; un dipôle ne rayonne pas dans sa propre direction, donc la lumière vue à $90^\circ$ est polarisée linéairement, perpendiculairement au plan formé par le faisceau et la direction d'observation. (c) Polarisation maximale à $90^\circ$ du Soleil ; nulle dans la direction du Soleil et à l'opposé (diffusion avant ou arrière).


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> Le champ de l'onde incidente est transversal. Vu à $90^\circ$, on observe le rayonnement des dipôles qui oscillent dans la direction perpendiculaire à la fois au faisceau et à la ligne de visée : la lumière est donc polarisée linéairement. Dans l'axe du faisceau, toutes les directions transversales sont possibles : pas de polarisation privilégiée.
> Dans le ciel, la polarisation est maximale sur un grand cercle à $90^\circ$ du Soleil ($P\approx0{,}7$ à $0{,}8$ dans un ciel clair), avec des directions $\vec E$ tangentes à des cercles centrés sur le Soleil. La polarisation est plus faible en présence de brume ou de nuages (diffusion multiple). De nombreux insectes (abeilles, fourmis) utilisent cette polarisation pour se repérer ; les marins vikings auraient utilisé des cristaux (« pierres de soleil  ») pour la même raison.


**q6.** (*) Aviation et visibilité. La loi de Koschmieder définit la visibilité météorologique par la distance $V$ à laquelle le contraste d'un objet noir sur l'horizon tombe à $2\ \%$ : $V=\dfrac{\ln(1/0{,}02)}{\sigma}=\dfrac{3{,}91}{\sigma}$. (a) Quelle est la visibilité si $\sigma=0{,}4\ \text{km}^{-1}$ ? (b) L'extinction due à la seule diffusion de Rayleigh vaut $\sigma_R\approx1{,}2\times10^{-2}\ \text{km}^{-1}$ à $550\ \text{nm}$ : quelle serait la visibilité maximale dans un air parfaitement pur ? (c) Un pilote voit deux montagnes lointaines : pourquoi la plus éloignée est-elle plus bleue et moins contrastée ?

> [!success]- ✅ Correction
> **Résultat**
>
> (a) $V=3{,}91/0{,}4\approx9{,}8\ \text{km}$. (b) $V_{\max}=3{,}91/0{,}012\approx330\ \text{km}$ (à comparer aux $\approx250$ à $300\ \text{km}$ observés au mieux). (c) Plus la distance est grande, plus la lumière diffusée par l'air entre le pilote et la montagne (bleuâtre) domine la lumière directe atténuée de la montagne.


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> (a) $V=\dfrac{3{,}91}{0{,}4}\approx9{,}8\ \text{km}$ (brume légère). (b) $V=\dfrac{3{,}91}{1{,}2\times10^{-2}}\approx326\ \text{km}$ : même dans un air parfaitement pur, la diffusion de Rayleigh limite la visibilité à quelques centaines de kilomètres.
> (c) La luminance apparente d'un objet à la distance $d$ est $L=L_0e^{-\sigma d}+L_{\text{air}}(1-e^{-\sigma d})$ : le premier terme (objet) décroît et le second (lumière diffusée par l'air, plutôt bleue) augmente. Au loin, l'objet se confond avec l'horizon : c'est pourquoi les massifs lointains sont bleutés et les ombres (contraste) disparaissent, ce que les peintres appellent la perspective atmosphérique.
> Pour un pilote, c'est un piège connu : dans une brume, les repères lointains paraissent plus éloignés qu'ils ne le sont ; dans un air très clair, ils paraissent plus proches que la réalité, ce qui conduit à sous-estimer les distances en montagne.

