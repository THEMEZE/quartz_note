---
title: "Exercice 5 — Polarisation : écrans, lunettes de pilote, reflets et plastiques sous contrainte"
tags:
  - tp
  - ondes-mecaniques-sonores-electromagnetiques-et-lumineuses
---

[[physique/ipsa-tp/TP/ondes-mecaniques-sonores-electromagnetiques-et-lumineuses/tp-sur-les-ondes-visuels-amusants-orientes-aviation/index|⬅ Retour]] · [📄 Fiche enseignant](/pdfs/TP_IPSA_Generale_fiche.pdf)

### Exercice 5. Polarisation : écrans, lunettes de pilote, reflets et plastiques sous contrainte

Les lunettes de soleil polarisantes éliminent les reflets sur l'eau ou sur une piste mouillée, mais elles peuvent rendre un écran LCD noir quand on incline la tête. Dans un cockpit, cela pose la question de la lisibilité des instruments. Ce TP étudie la polarisation de la lumière avec trois objets du quotidien : un écran, une paire de lunettes polarisantes, et des morceaux de plastique transparent.

On vérifie la loi de Malus, on explique les reflets par l'angle de Brewster, on observe les couleurs dues à la contrainte dans des plastiques (visibles aussi dans certains pare-brise), et on discute l'orientation de la polarisation des écrans avec des lunettes de pilote.

**q1.** Loi de Malus. Vérifier que les données suivent la loi $I=I_{\max}\cos^2\theta+I_{\min}\sin^2\theta$ avec $I_{\max}=100$ et $I_{\min}=3$. Calculer le rapport d'extinction $I_{\max}/I_{\min}$. Que vaudrait $I$ à $45^\circ$ pour un polariseur idéal ?

> [!success]- ✅ Correction
> **Résultat**
>
> $\theta=30^\circ$ : $75+0{,}75=75{,}8$ ; $45^\circ$ : $50+1{,}5=51{,}5$ ; $60^\circ$ : $25+2{,}25=27{,}3$. Bon accord avec les données. Rapport d'extinction $\approx33$. Polariseur idéal à $45^\circ$ : $50$.


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> $\cos^230^\circ=0{,}75$ et $\sin^230^\circ=0{,}25$ donc $I=100\times0{,}75+3\times0{,}25=75{,}75$ ; à $45^\circ$ : $51{,}5$ ; à $60^\circ$ : $27{,}25$. Les données sont compatibles (écart $<1$ unité).
> Le rapport d'extinction est $\dfrac{100}{3}=33$ : un polariseur réel n'est pas parfait, il laisse passer $3\ \%$ dans la direction croisée. Ce défaut est fréquent dans les films peu coûteux.
> Le seul ajustement significatif est l'angle où l'intensité est maximale : il donne la direction de polarisation de l'écran.


**q2.** Reflets. (a) Établir que le rayon réfléchi est polarisé totalement lorsque l'angle d'incidence vérifie $\tan\theta_B=n$ (rayon réfléchi $\perp$ rayon réfracté). (b) Calculer $\theta_B$ pour l'eau ($n=1{,}33$) et le verre ($n=1{,}50$). (c) À quelle hauteur au-dessus de l'horizon est le Soleil quand son reflet sur un lac est complètement polarisé ? (d) Dans quelle direction faut-il orienter les lunettes polarisantes pour éliminer ce reflet ?

> [!tip]- 💡 Coup de pouce
> **Condition**
>
> À l'incidence de Brewster, $\theta_i+\theta_t=90^\circ$. Utiliser $\sin\theta_i=n\sin\theta_t$ et $\cos\theta_i=\sin\theta_t$.


> [!success]- ✅ Correction
> **Résultat**
>
> (a) $\sin\theta_i=n\sin\theta_t=n\cos\theta_i$ donc $\tan\theta_i=n$. (b) Eau : $53{,}1^\circ$ ; verre : $56{,}3^\circ$. (c) hauteur du Soleil $=90^\circ-53{,}1^\circ=36{,}9^\circ$. (d) Le reflet est polarisé horizontalement : les lunettes polarisantes ont leur axe de transmission vertical.


> [!example]- 📝 Solution détaillée
> **Démonstration**
>
> (a) Le champ réfléchi vient du rayonnement des dipôles du milieu, oscillant dans la direction du champ transmis. Un dipôle ne rayonne pas dans sa propre direction : si le rayon réfracté est perpendiculaire au rayon réfléchi, la composante $p$ (dans le plan d'incidence) du champ transmis ne peut pas rayonner dans la direction réfléchie. Il ne reste que la composante $s$ (perpendiculaire au plan d'incidence, donc parallèle à la surface). Condition : $\theta_i+\theta_t=90^\circ$, donc $\sin\theta_t=\cos\theta_i$ et $\sin\theta_i=n\cos\theta_i$, soit $\tan\theta_B=n$.
> (b) $\theta_B=\arctan1{,}33=53{,}1^\circ$ ; $\arctan1{,}50=56{,}3^\circ$.
> (c) L'angle d'incidence est mesuré par rapport à la normale : hauteur $=90^\circ-53{,}1^\circ=36{,}9^\circ$. Un pilote qui regarde le reflet du Soleil sur un lac ou une piste mouillée quand le Soleil est à $37^\circ$ voit un reflet fortement polarisé.
> (d) La lumière réfléchie est polarisée parallèlement à la surface (horizontalement). Les lunettes polarisantes ont donc leur axe de transmission vertical, pour éteindre la direction horizontale.
> À l'incidence de Brewster, la réflectivité de la composante $s$ vaut $\dfrac{\sin^2(\theta_i-\theta_t)}{\sin^2(\theta_i+\theta_t)}=\sin^2(16{,}1^\circ)=7{,}7\ \%$ : le reflet d'une lumière naturelle est $3{,}9\ \%$ de l'intensité et il est entièrement supprimé par un polariseur idéal.


**q3.** Biréfringence sous contrainte. Une plaque de plexiglas d'épaisseur $e=10\ \text{mm}$ subit une contrainte $\sigma=5\ \text{MPa}$. Le retard optique vaut $\Gamma=C\,\sigma\,e$ avec $C=4{,}5\times10^{-12}\ \text{Pa}^{-1}$ (coefficient photoélastique du PMMA). (a) Calculer $\Gamma$. (b) Entre polariseurs croisés, l'intensité transmise pour une lame orientée à $45^\circ$ est $I=I_0\sin^2\left(\dfrac{\pi\Gamma}{\lambda}\right)$ : calculer $I/I_0$ pour $\lambda=450$, $550$ et $650\ \text{nm}$. Quelle est la couleur de la plaque ? (c) Pourquoi voit-on des franges dans les zones où la contrainte varie ?

> [!success]- ✅ Correction
> **Résultat**
>
> (a) $\Gamma=4{,}5\times10^{-12}\times5\times10^{6}\times0{,}010=2{,}25\times10^{-7}\ \text{m}=225\ \text{nm}$. (b) $I/I_0=\sin^2(\pi\Gamma/\lambda)=1{,}00\ ;\ 0{,}92\ ;\ 0{,}79$ pour $450$, $550$ et $650\ \text{nm}$ : plaque blanche légèrement bleutée. (c) Chaque zone de contrainte différente donne un retard différent, donc une couleur différente ; les lignes de même contrainte forment les franges (isochromes).


> [!example]- 📝 Solution détaillée
> **Calcul**
>
> (a) $\Gamma=C\sigma e=4{,}5\times10^{-12}\times5\times10^{6}\times10^{-2}=2{,}25\times10^{-7}\ \text{m}$. (b) À $450\ \text{nm}$ : $\sin^2\left(\dfrac{\pi\times225}{450}\right)=\sin^2\dfrac{\pi}{2}=1$ ; à $550\ \text{nm}$ : $\pi\times225/550=1{,}285\ \text{rad}$, $\sin^2=0{,}92$ ; à $650\ \text{nm}$ : $\pi\times225/650=1{,}087\ \text{rad}$, $\sin^2=0{,}79$. Les trois couleurs sont à peu près également transmises avec un léger avantage au bleu : la plaque est blanc-bleuté. Pour une contrainte de $10\ \text{MPa}$ ($\Gamma=450\ \text{nm}$), le bleu ($450\ \text{nm}$) serait éteint et le rouge transmis : les couleurs changent nettement.
> (c) La contrainte n'est pas uniforme : autour des points de fixation des hublots ou des trous, elle varie fortement ; à chaque valeur de $\sigma$ correspond une couleur, d'où des franges colorées (isochromes) qui cartographient la contrainte. Les ingénieurs utilisent la photoélasticimétrie pour visualiser les contraintes dans des maquettes.


**q4.** Orientation des écrans. Dans le TP, un téléphone en mode portrait est noir à travers les lunettes quand celles-ci sont tournées de $90^\circ$ par rapport à la verticale, et lisible en paysage. (a) Que peut-on dire de la direction de polarisation de l'écran ? (b) Un pilote porte des lunettes polarisantes (axe vertical) et lit une tablette dont la polarisation est verticale ou horizontale selon l'orientation : que se passe-t-il ? (c) Comment une lame quart d'onde placée devant l'écran résout-elle le problème ?

> [!success]- ✅ Correction
> **Résultat**
>
> (a) L'écran émet une lumière polarisée linéairement dans une direction fixe par rapport à l'appareil. (b) Si la polarisation est verticale, l'écran est lisible ; si elle est horizontale (tablette tournée de $90^\circ$), l'écran paraît noir. En inclinant la tête, l'intensité varie en $\cos^2$. (c) La lame quart d'onde à $45^\circ$ transforme la polarisation rectiligne en polarisation circulaire : l'intensité transmise par le polariseur est $I_0/2$ quelle que soit l'orientation.


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> (a) Le rétroéclairage traverse un polariseur avant la couche de cristaux liquides et un autre analyseur avant la sortie : la lumière de l'écran est donc polarisée linéairement dans la direction de l'analyseur (verticale, horizontale ou à $45^\circ$ selon les constructeurs).
> (b) Une lumière polarisée à l'angle $\alpha$ par rapport à l'axe des lunettes est transmise avec l'intensité $\cos^2\alpha$ : $100\ \%$ pour $\alpha=0$, $50\ \%$ à $45^\circ$, $0$ à $90^\circ$. Les pilotes signalent parfois des instruments « qui disparaissent » lorsqu'ils inclinent la tête.
> (c) Une lame quart d'onde d'axe à $45^\circ$ de la polarisation transforme la lumière en polarisation circulaire, qui a une intensité transmise $I_0/2$ pour tout angle du polariseur. Certains constructeurs ajoutent cette lame dans les écrans de cockpit et dans les tablettes conçues pour être lues avec des lunettes polarisantes.
> On peut aussi tester les vitres et les pare-brise : le plexiglas moulé montre des motifs colorés à travers les lunettes.


**q5.** (*) Ciel polarisé. On regarde le ciel à $90^\circ$ du Soleil à travers un polariseur que l'on tourne. On mesure $I_{\max}=85$ et $I_{\min}=15$ (unités arbitraires). Calculer le degré de polarisation $P=\dfrac{I_{\max}-I_{\min}}{I_{\max}+I_{\min}}$. Comparer avec la valeur théorique de Rayleigh $P(\gamma)=\dfrac{\sin^2\gamma}{1+\cos^2\gamma}$ pour $\gamma=90^\circ$ et $\gamma=45^\circ$, et expliquer pourquoi la valeur mesurée est plus faible (voir aussi TP A4).

> [!success]- ✅ Correction
> **Résultat**
>
> $P=\dfrac{85-15}{85+15}=0{,}70$. Théorie : $P(90^\circ)=1$ et $P(45^\circ)=\dfrac{0{,}5}{1{,}5}=0{,}33$. La valeur mesurée est plus faible à cause de la diffusion multiple, des aérosols et du sol qui renvoie de la lumière non polarisée.


> [!example]- 📝 Solution détaillée
> **Discussion**
>
> $P=\dfrac{85-15}{85+15}=0{,}70$. Pour une diffusion de Rayleigh par des dipôles isotropes, à $\gamma=90^\circ$ du Soleil : $P=1$. Aux autres angles : $P(45^\circ)=\dfrac{\sin^245^\circ}{1+\cos^245^\circ}=\dfrac{0{,}5}{1{,}5}=0{,}33$.
> Les valeurs mesurées ($\approx0{,}7$ à $0{,}8$ dans un ciel très clair) sont plus faibles parce que : la molécule d'air n'est pas un dipôle isotrope (léger dépolarisant, $\approx5\ \%$), une partie de la lumière a subi plusieurs diffusions (polarisation brouillée), la lumière réfléchie par le sol est reprise par l'atmosphère, et les aérosols (diffusion de Mie) sont peu polarisants. Dans une brume épaisse, $P$ tombe à quelques pourcents.
> Application : la polarisation du ciel donne la direction du Soleil même sous un ciel partiellement couvert (boussole polarisée utilisée par les abeilles et par des navigateurs polaires, pour les vols dans les régions où les compas magnétiques sont peu fiables).

