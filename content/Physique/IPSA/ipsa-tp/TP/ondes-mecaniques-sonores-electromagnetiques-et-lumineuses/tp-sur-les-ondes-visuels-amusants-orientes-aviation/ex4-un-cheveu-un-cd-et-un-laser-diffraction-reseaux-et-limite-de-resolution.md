---
title: "Exercice 4 — Un cheveu, un CD et un laser : diffraction, réseaux et limite de résolution"
tags:
  - tp
  - ondes-mecaniques-sonores-electromagnetiques-et-lumineuses
---

[[physique/IPSA/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/index|⬅ Retour]]

### Exercice 4. Un cheveu, un CD et un laser : diffraction, réseaux et limite de résolution

*⭐ Indispensable · Difficulté ●●●○○ · ⏱ 2 h · Type : TP expérimental visuel*

Un pointeur laser éclairant un cheveu tendu forme sur un mur une figure de diffraction faite de taches régulièrement espacées. La lumière contourne les obstacles : c'est la nature ondulatoire de la lumière. Le même laser envoyé sur un CD, un DVD ou un Blu-ray forme des taches à des angles très différents selon le disque, ce qui révèle le pas des pistes.

Ce TP mesure le diamètre d'un cheveu, le pas de pistes d'un CD et d'un DVD, puis relie la diffraction à des questions d'aviation : la limite de résolution de l'œil et l'ouverture du faisceau d'une antenne radar.

> [!abstract]+ 📚 Prérequis
> **Notions**
>
> Diffraction de Fraunhofer par une fente : $\sin\theta=\dfrac{n\lambda}{a}$ pour les minima ; formule des réseaux $\sin\theta=\dfrac{n\lambda}{p}$ (incidence normale) ; principe de Babinet.


> [!info]+ 🎯 Objectifs
> **Mesurer des tailles microscopiques avec la lumière**
>
> Déterminer le diamètre d'un cheveu ($\approx70\ \mu\text{m}$) et le pas des pistes d'un disque ($1{,}6\ \mu\text{m}$, $0{,}74\ \mu\text{m}$) à partir d'angles et de distances de l'ordre du mètre.


> [!note]+ 🧰 Matériel
> Pointeur laser rouge de classe 2 ($\lambda=650\pm10\ \text{nm}$ ; valeur à lire sur la notice)
>
> Cheveu tendu sur un cadre (papier cartonné ou cadre de diapositive), fil de pêche, fente réglable (facultatif)
>
> CD, DVD, Blu-ray, un morceau de réseau du commerce (facultatif)
>
> Mur blanc ou écran à $L=3{,}00\ \text{m}$ du cheveu, mètre ruban, règle ou papier millimétré, rapporteur
>
> Pied ou support pour fixer le laser, ruban adhésif


> [!danger] 🦺 Sécurité
> **Laser**
>
> Utiliser uniquement un pointeur de classe 2 ($<1\ \text{mW}$, longueur d'onde $635$–$650\ \text{nm}$ ou $532\ \text{nm}$). Ne jamais viser une personne, une vitre, une surface très réfléchissante non contrôlée ou le ciel. Le pointage d'un laser vers un aéronef est une infraction et met en danger l'équipage.
>
> **Surfaces réfléchissantes**
>
> Le CD renvoie le faisceau dans plusieurs directions : le tenir à l'écart de la hauteur des yeux et utiliser un écran ou un mur, hors de la trajectoire des personnes.


> [!note]+ 🔬 Manipulation
> **1. Diffraction par le cheveu**
>
> Fixer le laser à hauteur du cheveu, à $L=3{,}00\ \text{m}$ du mur. Placer le cheveu dans le faisceau : on doit voir une tache centrale allongée et des taches secondaires régulières perpendiculairement au cheveu. Marquer les centres des minima (ou des taches) sur du papier et mesurer la distance $D_{10}$ correspondant à $10$ intervalles.
>
> **2. CD et DVD**
>
> Envoyer le faisceau sur la face gravée d'un CD, sous incidence normale (rayon réfléchi revenant vers le laser). Repérer les taches d'ordre $\pm1$ sur un écran situé entre le laser et le CD (feuille avec un trou pour laisser passer le faisceau). Mesurer l'angle $\theta_1$ entre l'ordre $0$ et l'ordre $1$ avec $L$ et la distance $x_1$ au centre. Répéter avec un DVD, puis un Blu-ray.
>
> **3. Lien avec l'observation de la lumière naturelle**
>
> Regarder la face gravée d'un CD à la lumière du jour (arc-en-ciel), et l'aile d'un papillon ou une plume d'oiseau contre un point lumineux. Photographier.


**q1.** Diffraction par le cheveu. (a) Justifier que la distance entre deux minima consécutifs vaut $i=\dfrac{\lambda L}{a}$ pour $x\ll L$. (b) Calculer $i$ avec $D_{10}$, puis le diamètre $a$ du cheveu. (c) Incertitude relative et résultat. (d) Que devient la figure pour un cheveu plus fin ?

> [!tip]- 💡 Coup de pouce
> **Petits angles**
>
> Les minima sont pour $\sin\theta_n=\dfrac{n\lambda}{a}$ et $x_n=L\tan\theta_n\approx L\sin\theta_n$.


> [!success]- ✅ Correction
> **Résultat**
>
> (a) $x_n=\dfrac{n\lambda L}{a}$ donc $i=\dfrac{\lambda L}{a}$. (b) $i=\dfrac{279}{10}=27{,}9\ \text{mm}$ et $a=\dfrac{\lambda L}{i}=\dfrac{650\times10^{-9}\times3{,}00}{27{,}9\times10^{-3}}=69{,}9\ \mu\text{m}$. (c) $\dfrac{\Delta a}{a}=\dfrac{\Delta\lambda}{\lambda}+\dfrac{\Delta L}{L}+\dfrac{\Delta i}{i}=1{,}5+0{,}3+1{,}1=2{,}9\ \%$ : $a=(70\pm2)\ \mu\text{m}$. (d) Un cheveu plus fin donne une figure plus large.


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> (a) Le $n$-ième minimum est à l'angle $\sin\theta_n=\dfrac{n\lambda}{a}$. Pour $\theta\ll1$, $x_n\approx L\dfrac{n\lambda}{a}$, donc deux minima consécutifs sont séparés par $i=\dfrac{\lambda L}{a}$.
> (b) $i=\dfrac{D_{10}}{10}=27{,}9\ \text{mm}$ (mesurer sur $10$ intervalles divise par $10$ l'incertitude de pointé). $a=\dfrac{650\times10^{-9}\times3{,}00}{0{,}0279}=69{,}9\ \mu\text{m}$.
> (c) Incertitudes : $\dfrac{\Delta\lambda}{\lambda}=\dfrac{10}{650}=1{,}5\ \%$, $\dfrac{\Delta L}{L}=0{,}3\ \%$, $\dfrac{\Delta i}{i}=\dfrac{3}{279}=1{,}1\ \%$, donc $2{,}9\ \%$ (somme absolue), soit $a=(70\pm2)\ \mu\text{m}$. La valeur est compatible avec les diamètres usuels d'un cheveu ($50$ à $100\ \mu\text{m}$). Le laser dont la longueur d'onde est mal connue (dispersion entre pointeurs) est ici la principale source d'incertitude ; on peut la mesurer avec une fente calibrée.
> (d) $i\propto1/a$ : un cheveu plus fin donne des taches plus espacées.


**q2.** Réseau CD/DVD. (a) Justifier $\sin\theta_1=\dfrac{\lambda}{p}$ pour un réseau par réflexion sous incidence normale. (b) Calculer le pas $p$ du CD et du DVD avec les angles mesurés. (c) Comparer avec les valeurs de référence ($1{,}6\ \mu\text{m}$ et $0{,}74\ \mu\text{m}$). (d) Pourquoi n'observe-t-on aucun ordre $1$ avec un Blu-ray (pas $0{,}32\ \mu\text{m}$) ? Que se passe-t-il avec un laser vert ($532\ \text{nm}$) sur le CD ?

> [!success]- ✅ Correction
> **Résultat**
>
> (a) Les rayons diffractés par deux pistes voisines sont en phase si $p\sin\theta=n\lambda$. (b) CD : $p=\dfrac{650}{\sin24^\circ}=1{,}60\ \mu\text{m}$ ; DVD : $p=\dfrac{650}{\sin61^\circ}=0{,}74\ \mu\text{m}$. (c) Accord. (d) $\dfrac{\lambda}{p}=\dfrac{650}{320}>1$ : $\sin\theta_1$ ne peut pas dépasser $1$, donc pas d'ordre $1$ (seule la réflexion $n=0$). Avec $532\ \text{nm}$ sur un CD : $\sin\theta_1=\dfrac{532}{1600}$, $\theta_1=19{,}4^\circ$ (plus petit).


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> (a) Deux pistes voisines sont séparées de $p$ ; sous incidence normale, la différence de marche entre les rayons diffractés à l'angle $\theta$ est $p\sin\theta$ ; l'interférence est constructive si $p\sin\theta=n\lambda$.
> (b) $p_{\text{CD}}=\dfrac{650\times10^{-9}}{\sin24^\circ}=\dfrac{650}{0{,}4067}\ \text{nm}=1{,}60\ \mu\text{m}$. $p_{\text{DVD}}=\dfrac{650}{\sin61^\circ}=\dfrac{650}{0{,}8746}=743\ \text{nm}$. Incertitude : $\Delta\theta=1^\circ=0{,}017\ \text{rad}$ donne $\dfrac{\Delta p}{p}=\dfrac{\cos\theta}{\sin\theta}\Delta\theta=\dfrac{\Delta\theta}{\tan\theta}=3{,}9\ \%$ pour le CD et $1{,}0\ \%$ pour le DVD : un grand angle est plus précis.
> (d) Blu-ray : $\dfrac{\lambda}{p}=2{,}03>1$, donc il n'y a pas d'ordre $1$ ; le disque se comporte comme un miroir pour la lumière rouge et verte. Les lecteurs Blu-ray utilisent un laser bleu-violet ($405\ \text{nm}$), donc $\dfrac{\lambda}{p}=1{,}27$ : même dans ce cas il n'y a pas d'ordre diffracté vers l'extérieur ; le disque est lu par la lumière réfléchie ou non par des cuvettes de profondeur $\lambda/4$.


**q3.** Aviation. (a) Calculer la limite angulaire de résolution de l'œil dû à la diffraction, pupille de $3\ \text{mm}$ et $\lambda=550\ \text{nm}$, et la comparer à l'acuité visuelle standard de $1'$. (b) À quelle distance un avion de $10\ \text{m}$ d'envergure est-il vu sous un angle de $1'$ ? Commenter la doctrine « voir et éviter ». (c) Une antenne de radar météo de diamètre $75\ \text{cm}$ fonctionne à $9{,}4\ \text{GHz}$ ; calculer l'ouverture angulaire $1{,}22\dfrac{\lambda}{D}$ et la largeur du faisceau à $100\ \text{km}$.

> [!success]- ✅ Correction
> **Résultat**
>
> (a) $\theta_{\min}=1{,}22\times\dfrac{550\times10^{-9}}{3\times10^{-3}}=2{,}2\times10^{-4}\ \text{rad}=0{,}77'$ (à comparer à $1'=2{,}9\times10^{-4}\ \text{rad}$). (b) $d=\dfrac{10}{2{,}9\times10^{-4}}=34\ \text{km}$ (limite théorique, très optimiste). (c) $\theta=1{,}22\dfrac{3{,}19\times10^{-2}}{0{,}75}=5{,}2\times10^{-2}\ \text{rad}=3{,}0^\circ$ ; largeur à $100\ \text{km}$ : $5{,}2\ \text{km}$.


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> (a) $\theta_{\min}=1{,}22\dfrac{\lambda}{D}=2{,}2\times10^{-4}\ \text{rad}=0{,}77'$ : la diffraction de la pupille et l'acuité de $1'$ sont du même ordre : l'œil est un instrument presque parfait à la limite de diffraction.
> (b) $d=\dfrac{10\ \text{m}}{2{,}9\times10^{-4}}=34\ \text{km}$. En réalité, il faut que l'objet soit contrasté, que l'observateur balaie la bonne zone du ciel : les distances de détection d'un avion léger sont typiquement de quelques kilomètres. La vitesse de rapprochement de deux avions ($\approx200\ \text{m/s}$) laisse moins de $20\ \text{s}$ à $4\ \text{km}$ : la limite de la doctrine « voir et éviter ».
> (c) $\lambda=\dfrac{c}{f}=3{,}19\ \text{cm}$, $\theta=1{,}22\dfrac{0{,}0319}{0{,}75}=0{,}052\ \text{rad}=3{,}0^\circ$ : à $100\ \text{km}$, la largeur du faisceau est $\approx5{,}2\ \text{km}$, ce qui limite la résolution latérale d'un radar de bord. Un plus grand diamètre (ou une longueur d'onde plus courte) réduit la largeur du faisceau : d'où le radôme en nez d'avion aussi grand que possible.


**q4.** Critique. Citer trois sources d'erreur dans la mesure du cheveu et proposer un moyen de les réduire. La fente rectangulaire réglable donnerait-elle une mesure plus fiable ?

> [!success]- ✅ Correction
> **Résultat**
>
> Longueur d'onde inconnue du laser ($\pm1$ à $2\ \%$) ; pointé des minima (tache lumineuse large) ; cheveu non perpendiculaire au faisceau et non tendu ; mur non perpendiculaire. Une fente calibrée est plus fiable si sa largeur est connue à mieux de $1\ \mu\text{m}$.


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> (i) $\lambda$ : les pointeurs bon marché ont $\pm10\ \text{nm}$ ; la calibrer avec un réseau connu (par exemple $600$ traits/mm) réduit cette source d'erreur. (ii) Pointé : les minima sont larges ; on pointe le milieu des zones sombres et l'on mesure sur $10$ intervalles. (iii) Géométrie : un mur non perpendiculaire déforme les distances ; mesurer $L$ le long du faisceau. (iv) Le cheveu doit être tendu et perpendiculaire au faisceau. Une fente calibrée évite les variations de diamètre d'un cheveu à l'autre mais nécessite un réglage à mieux que le micromètre.


> [!note]- ✈️ Lien avec l'aviation
> **Résolution de l'œil et faisceau radar**
>
> L'œil humain est limité par la diffraction de la pupille ($\theta\approx1{,}22\lambda/D$). Une antenne de radar météo de bord de $75\ \text{cm}$ à $9{,}4\ \text{GHz}$ a un faisceau limité par la même formule : quelques degrés. Ces deux limites ont la même origine physique que la figure de diffraction du cheveu.


> [!question]- 🔭 Aller plus loin — Licence : Diffraction et transformée de Fourier
> La figure de diffraction de Fraunhofer est la transformée de Fourier de l'ouverture. Un objet de taille $a$ a un spectre spatial de largeur $\sim1/a$.


> [!question]- 🔭 Aller plus loin — Master : Structure de couleurs des plumes
> Les couleurs de nombreuses plumes et ailes de papillon ne sont pas des pigments mais des structures périodiques de l'ordre de $\lambda/2$ (couleurs structurelles).

